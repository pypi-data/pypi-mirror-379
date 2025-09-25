# Filename: comprehensive_json_logging_callback.py
import json
from datetime import datetime
from datetime import timezone
from typing import Any
from uuid import UUID

from langchain_core.agents import AgentAction
from langchain_core.agents import AgentFinish
from langchain_core.callbacks.base import BaseCallbackHandler
from langchain_core.load import dumpd
from langchain_core.outputs import LLMResult


class JsonLoggingCallbackHandler(BaseCallbackHandler):
    """
    A comprehensive callback handler that logs all agent interactions into a
    structured JSON file, including timings, I/O, and detailed token usage.

    This class is designed as a context manager for robust log saving.
    """

    def __init__(self, log_file_path: str) -> None:
        self.log_file_path = log_file_path
        self._runs: list[dict[str, Any]] = []
        self._current_run: dict[str, Any] | None = None
        self.session_start_time: datetime | None = None
        self.session_token_summary: dict[str, int] = {
            'prompt_tokens': 0,
            'completion_tokens': 0,
            'total_tokens': 0,
        }

    def __enter__(self) -> 'JsonLoggingCallbackHandler':
        self.session_start_time = datetime.now(timezone.utc)
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.save_to_json()

    def _initialize_run(self, run_id: UUID, inputs: dict[str, Any]) -> None:
        """Initializes a new run log, including token counters."""
        if self._current_run:
            self._runs.append(self._current_run)

        self._current_run = {
            'run_id': str(run_id),
            'start_time': datetime.now(timezone.utc).isoformat(),
            'end_time': None,
            'duration_seconds': None,
            'inputs': inputs,
            'output': None,
            'error': None,
            'llm_calls': 0,
            'token_summary': {
                'prompt_tokens': 0,
                'completion_tokens': 0,
                'total_tokens': 0,
            },
            'steps': [],
        }

    def _finalize_run(self) -> None:
        """Finalizes the current run, calculates its duration, and adds it to the list."""
        if self._current_run:
            end_time = datetime.now(timezone.utc)
            self._current_run['end_time'] = end_time.isoformat()

            start_time = datetime.fromisoformat(
                self._current_run['start_time'],
            )
            duration = (end_time - start_time).total_seconds()
            self._current_run['duration_seconds'] = round(duration, 4)

            self._runs.append(self._current_run)
            self._current_run = None

    def save_to_json(self) -> None:
        """Saves all completed runs and session metadata to the specified JSON file."""
        if self._current_run:
            self._finalize_run()

        total_duration = 0.0
        if self.session_start_time:
            total_duration = (
                datetime.now(timezone.utc) -
                self.session_start_time
            ).total_seconds()

        final_log = {
            'metadata': {
                'total_duration_seconds': round(total_duration, 4),
                'run_count': len(self._runs),
                'session_start_time': self.session_start_time.isoformat() if self.session_start_time else None,
                'total_token_summary': self.session_token_summary,
            },
            'runs': self._runs,
        }

        try:
            with open(self.log_file_path, 'w', encoding='utf-8') as f:
                json.dump(final_log, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving log file: {e}")

    def _append_step(self, step_data: dict[str, Any]) -> None:
        if self._current_run:
            step_data['timestamp'] = datetime.now(timezone.utc).isoformat()
            self._current_run['steps'].append(step_data)

    def on_llm_end(self, response: LLMResult, *, run_id: UUID, **kwargs: Any) -> None:
        """
        Called when an LLM call ends. Extracts and aggregates token usage.
        """
        token_usage = response.llm_output.get('token_usage', {})
        prompt_tokens = token_usage.get('prompt_tokens', 0)
        completion_tokens = token_usage.get('completion_tokens', 0)
        total_tokens = token_usage.get('total_tokens', 0)

        step_data = {
            'type': 'llm_end',
            'run_id': str(run_id),
            'response': dumpd(response),
            'token_usage': {
                'prompt_tokens': prompt_tokens,
                'completion_tokens': completion_tokens,
                'total_tokens': total_tokens,
            },
        }
        self._append_step(step_data)

        if self._current_run:
            self._current_run['llm_calls'] += 1
            self._current_run['token_summary']['prompt_tokens'] += prompt_tokens
            self._current_run['token_summary']['completion_tokens'] += completion_tokens
            self._current_run['token_summary']['total_tokens'] += total_tokens

        self.session_token_summary['prompt_tokens'] += prompt_tokens
        self.session_token_summary['completion_tokens'] += completion_tokens
        self.session_token_summary['total_tokens'] += total_tokens

    def on_chain_start(
        self, serialized: dict[str, Any], inputs: dict[str, Any], *, run_id: UUID, **kwargs: Any,
    ) -> None:
        if self._current_run is None:
            self._initialize_run(run_id, inputs)

    def on_chain_end(self, outputs: dict[str, Any], *, run_id: UUID, **kwargs: Any) -> None:
        if self._current_run and self._current_run['run_id'] == str(run_id):
            self._current_run['output'] = outputs
            self._finalize_run()

    def on_chain_error(self, error: Exception | KeyboardInterrupt, *, run_id: UUID, **kwargs: Any) -> None:
        if self._current_run and self._current_run['run_id'] == str(run_id):
            self._current_run['error'] = str(error)
            self._finalize_run()
            # Save immediately when an error occurs to ensure we don't lose the trace
            self.save_to_json()

    def on_llm_start(
        self, serialized: dict[str, Any], prompts: list[str], *, run_id: UUID, **kwargs: Any,
    ) -> None:
        self._append_step(
            {'type': 'llm_start', 'run_id': str(run_id), 'prompts': prompts},
        )

    def on_tool_start(
        self, serialized: dict[str, Any], input_str: str, *, run_id: UUID, **kwargs: Any,
    ) -> None:
        self._append_step({
            'type': 'tool_start', 'run_id': str(
                run_id,
            ), 'tool_name': serialized.get('name'), 'tool_input': input_str,
        })

    def on_tool_end(self, output: str, *, run_id: UUID, **kwargs: Any) -> None:
        self._append_step(
            {'type': 'tool_end', 'run_id': str(run_id), 'tool_output': output},
        )

    def on_agent_action(self, action: AgentAction, *, run_id: UUID, **kwargs: Any) -> None:
        self._append_step(
            {
                'type': 'agent_action', 'run_id': str(
                    run_id,
                ), 'action': dumpd(action),
            },
        )

    def on_agent_finish(self, finish: AgentFinish, *, run_id: UUID, **kwargs: Any) -> None:
        self._append_step(
            {
                'type': 'agent_finish', 'run_id': str(
                    run_id,
                ), 'finish': dumpd(finish),
            },
        )
