"""Task evaluation functionality."""
import importlib
import uuid
from collections.abc import Callable
from pathlib import Path

import requests
import structlog

from openapi_agent_benchmark.applications.base import Application
from openapi_agent_benchmark.evaluations.models.openapi_agent import OpenAPIAgent
from openapi_agent_benchmark.evaluations.models.openapi_type import OpenAPIType
from openapi_agent_benchmark.evaluations.utils.multipass import Multipass
from openapi_agent_benchmark.evaluations.utils.waiter import wait_until_accessible
from openapi_agent_benchmark.generators.models import Task
from openapi_agent_benchmark.utils.name import sanitize

logger = structlog.get_logger(__name__)


def load_verifier(application: Application, task_path: Path) -> Callable[[str, str, requests.Session], bool] | None:
    """Dynamically imports and returns the verifier function for a given task."""
    try:
        sanitized_repo = sanitize(application.repo)
        module_path = (
            f'openapi_agent_benchmark.tasks.'
            f'{sanitized_repo}.{task_path.parent.name}.verifier'
        )
        print(module_path)
        module = importlib.import_module(module_path)
        return getattr(module, 'verify')
    except (ImportError, AttributeError, ModuleNotFoundError) as e:
        logger.error(
            'Verifier function not found',
            application=f"{application.owner}/{application.repo}",
            task=task_path.parent.name,
            module_path=module_path,
            error_type=type(e).__name__,
            error_msg=str(e),
        )
        return None


def run_evaluation_task(
    application: Application,
    spec_type: OpenAPIType,
    task_path: Path,
    openapi_file: Path,
    url: str,
    username: str,
    password: str,
    llm_model: str,
    llm_temperature: float,
    max_runs: int = 2,
    experiment: str = 'default',
):
    """
    Executes a single evaluation task in a clean, isolated VM environment.
    """
    task_id = task_path.parent.name
    spec_name = spec_type.value
    log = logger.bind(
        application=f"{application.owner}/{application.repo}",
        task_id=task_id,
        spec=spec_name,
    )

    task = Task.model_validate_json(task_path.read_text())
    verifier_function = load_verifier(application, task_path)

    if verifier_function is None:
        log.error(
            'Task execution aborted - verifier function unavailable',
        )
        return

    # Check if this task should be skipped based on existing successful runs
    from openapi_agent_benchmark.evaluations.utils.validator import count_successful_runs
    successful_runs_count = count_successful_runs(
        task_path, spec_type, experiment,
    )
    if successful_runs_count >= max_runs:
        log.info(
            'Task already completed - skipping',
            successful_runs=successful_runs_count,
            max_runs=max_runs,
        )
        return

    run_id = str(uuid.uuid4())
    result_path = task_path.parent / 'results' / experiment / \
        spec_name.lower() / run_id / 'result.json'
    result_path.parent.mkdir(parents=True, exist_ok=True)
    if result_path.exists():
        log.info(
            'Result file exists - skipping duplicate run',
            run_id=run_id,
        )
        return

    trace_path = task_path.parent / 'results' / experiment / \
        spec_name.lower() / run_id / 'trace.json'
    trace_path.parent.mkdir(parents=True, exist_ok=True)

    log.info(
        'Starting task evaluation',
        run_id=run_id,
        task_description=task.description[:100] + '...' if len(
            task.description,
        ) > 100 else task.description,
        llm_model=llm_model,
        llm_temperature=llm_temperature,
    )

    # The Multipass context manager handles VM reset, start, wait, and stop.
    with Multipass(
        instance_name=application.multipass_instance_name,
        snapshot_name=application.multipass_snapshot_name,
    ):
        try:
            wait_until_accessible(url)
            agent = OpenAPIAgent(
                application=application,
                username=username,
                password=password,
                trace_path=trace_path,
                result_path=result_path,
                llm_model=llm_model,
                llm_temperature=llm_temperature,
            )
            response = agent.run_query(
                openapi_file, url, task.description, verifier_function,
            )
            output = response.get('output', '')
            log.info(
                'Task evaluation completed successfully',
                run_id=run_id,
                output_length=len(output) if output else 0,
                output_preview=output[:100] +
                '...' if output and len(output) > 100 else output,
            )
        except Exception as e:
            log.error(
                'Task execution failed with unhandled exception',
                run_id=run_id,
                error_type=type(e).__name__,
                error_msg=str(e),
                exc_info=True,
            )
