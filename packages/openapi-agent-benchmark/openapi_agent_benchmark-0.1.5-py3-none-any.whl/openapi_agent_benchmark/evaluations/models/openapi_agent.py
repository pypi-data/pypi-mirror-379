import json
import tempfile
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any

import requests
import structlog
from langchain_community.agent_toolkits.openapi import planner
from langchain_community.agent_toolkits.openapi.spec import reduce_openapi_spec
from langchain_community.utilities.requests import RequestsWrapper
from langchain_deepseek import ChatDeepSeek

from openapi_agent_benchmark.applications.base import Application
from openapi_agent_benchmark.authentications.factory import AuthProviderFactory
from openapi_agent_benchmark.evaluations.models.openapi_agent_result import OpenAPIAgentResult
from openapi_agent_benchmark.evaluations.models.openapi_agent_token_summary import OpenAPIAgentTokenSummary
from openapi_agent_benchmark.evaluations.tracer import JsonLoggingCallbackHandler

logger = structlog.get_logger(__name__)


class OpenAPIAgent:
    """Handles OpenAPI specification processing and agent management."""

    def __init__(
        self,
        application: Application,
        username: str,
        password: str,
        trace_path: Path,
        result_path: Path,
        llm_model: str = 'deepseek-coder',
        llm_temperature: float = 0.0,
    ):
        """
        Initializes the OpenAPIAgent.

        Args:
            application: The application context.
            trace_path: Path to save the detailed JSON trace file.
            llm_model: The language model to use.
            llm_temperature: The temperature for the language model.
        """
        self.application = application
        self.username = username
        self.password = password
        self.llm_model = llm_model
        self.llm_temperature = llm_temperature
        self.trace_path = trace_path
        self.trace_path.parent.mkdir(parents=True, exist_ok=True)
        self.result_path = result_path
        self.result_path.parent.mkdir(parents=True, exist_ok=True)

    def _update_server_config(self, api_spec: dict, url: str) -> dict:
        """Overrides the server URL in the OpenAPI spec."""
        api_spec['servers'] = [
            {'url': url},
        ]
        return api_spec

    def _get_api_spec(self, openapi_path: Path, url: str) -> dict:
        """Loads, updates, and reduces the OpenAPI spec."""
        logger.info('Preparing API spec...', path=str(openapi_path))
        raw_spec = json.loads(openapi_path.read_text(encoding='utf-8'))
        updated_spec = self._update_server_config(raw_spec, url)
        return reduce_openapi_spec(updated_spec)

    def _get_requests_wrapper(self, url: str) -> RequestsWrapper:
        """Get a configured RequestsWrapper for the API."""
        logger.info('Getting configured RequestsWrapper...')
        provider = AuthProviderFactory.create_provider(
            self.application.owner, self.application.repo, self.username, self.password,
        )
        requests_wrapper = provider.get_requests_wrapper(url)
        logger.info('RequestsWrapper configured successfully')
        return requests_wrapper

    def _get_requests_session(self, url: str) -> requests.Session:
        """Get a configured requests.Session for the API."""
        logger.info('Getting configured requests.Session...')
        provider = AuthProviderFactory.create_provider(
            self.application.owner, self.application.repo, self.username, self.password,
        )
        requests_session = provider.get_requests_session(url)
        logger.info('requests.Session configured successfully')
        return requests_session

    def _create_agent(self, api_spec: dict, requests_wrapper: RequestsWrapper):
        """Creates and configures an OpenAPI agent for the given spec and requests wrapper."""
        logger.info('Creating OpenAPI agent...')

        llm = ChatDeepSeek(
            model=self.llm_model,
            temperature=self.llm_temperature,
        )
        agent = planner.create_openapi_agent(
            api_spec, requests_wrapper, llm,
            allow_dangerous_requests=True,
            agent_executor_kwargs={
                'handle_parsing_errors': True,
            },
            # https://github.com/langchain-ai/langchain/issues/19440
            allowed_operations=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
        )
        return agent

    def run_query(self, openapi_path: Path, url: str, user_query: str, verify_function: Callable[[str, str, requests.Session], bool] = lambda x, y, z: False) -> dict[str, Any]:
        """
        Runs a single query against the API, logs a detailed trace, and returns the response.

        The trace, including duration, token usage, I/O, and all intermediate steps,
        is automatically saved to the `trace_path` specified during initialization.
        Both trace.json and result.json are always saved, regardless of success or failure.
        """

        # Create temporary files for result and trace
        temp_result_fd, temp_result_path = tempfile.mkstemp(
            suffix='.json', prefix='result_',
        )
        temp_trace_fd, temp_trace_path = tempfile.mkstemp(
            suffix='.json', prefix='trace_',
        )

        try:
            # Step 1: Prepare the spec, get the requests wrapper, and create the agent
            processed_spec = self._get_api_spec(openapi_path, url)
            requests_wrapper = self._get_requests_wrapper(url)
            requests_session = self._get_requests_session(url)
            agent = self._create_agent(processed_spec, requests_wrapper)

            response: dict[str, Any] = {}
            task_completed_successfully = False

            # The tracer context manager handles all logging and file saving automatically
            with JsonLoggingCallbackHandler(temp_trace_path) as tracer:
                logger.info(
                    'Invoking agent with query',
                    query_preview=f"{user_query[:70]}...",
                )
                start_time = time.time()
                try:
                    response = agent.invoke(
                        user_query, config={'callbacks': [tracer]},
                    )
                    task_completed_successfully = True
                except Exception as e:
                    # The tracer will still save the partial trace upon exiting the 'with' block
                    logger.error(
                        'Error during agent invocation',
                        error=str(e),
                        error_type=type(e).__name__,
                        exc_info=True,
                    )
                finally:
                    end_time = time.time()
                    output = response.get('output', '')
                    result = OpenAPIAgentResult(
                        start_time=start_time,
                        end_time=end_time,
                        duration=end_time - start_time,
                        token_summary=OpenAPIAgentTokenSummary(
                            prompt_tokens=tracer.session_token_summary['prompt_tokens'],
                            completion_tokens=tracer.session_token_summary['completion_tokens'],
                            total_tokens=tracer.session_token_summary['total_tokens'],
                        ),
                        input=user_query,
                        output=output,
                        verified=verify_function(
                            output, url, requests_session,
                        ),
                    )

                    # Always save result.json (success or failure)
                    with open(temp_result_fd, 'w', encoding='utf-8') as f:
                        f.write(
                            json.dumps(
                                result.model_dump(),
                                indent=4, ensure_ascii=False, sort_keys=True,
                            ),
                        )
                    logger.info('Result saved to temporary file')

            # Always move temporary files to final locations (success or failure)
            import shutil
            shutil.move(temp_trace_path, self.trace_path)
            shutil.move(temp_result_path, self.result_path)

            if task_completed_successfully:
                logger.info('Task completed successfully - files saved')
            else:
                logger.info(
                    'Task failed - files saved for debugging',
                    completed=task_completed_successfully,
                )

        finally:
            # Clean up temporary files
            try:
                import os
                os.close(temp_result_fd)
                os.close(temp_trace_fd)
                if temp_result_path and os.path.exists(temp_result_path):
                    os.unlink(temp_result_path)
                if temp_trace_path and os.path.exists(temp_trace_path):
                    os.unlink(temp_trace_path)
            except Exception as e:
                logger.warning(
                    'Error cleaning up temporary files', error=str(e),
                )

        if task_completed_successfully:
            logger.info('Agent invocation finished successfully.')
        else:
            logger.warning('Agent invocation finished with issues.')

        return response
