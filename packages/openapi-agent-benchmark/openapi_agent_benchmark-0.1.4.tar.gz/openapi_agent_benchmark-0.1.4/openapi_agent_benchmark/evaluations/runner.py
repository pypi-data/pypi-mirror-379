"""Main evaluation runner functionality."""
import time
from pathlib import Path

import structlog

from openapi_agent_benchmark.applications.base import Application
from openapi_agent_benchmark.evaluations.evaluator import run_evaluation_task
from openapi_agent_benchmark.evaluations.models.openapi_type import OpenAPIType
from openapi_agent_benchmark.evaluations.utils.validator import count_successful_runs
from openapi_agent_benchmark.evaluations.utils.validator import print_task_status_table

logger = structlog.get_logger(__name__)


def get_incomplete_tasks(all_task_paths: list[Path], application: Application, max_runs: int, experiment: str) -> list[tuple[Path, OpenAPIType, Path]]:
    """Get all task/spec combinations that haven't reached max_runs yet."""
    incomplete_tasks = []
    for task_path in all_task_paths:
        for spec_name in OpenAPIType:
            spec_type = OpenAPIType(spec_name)
            openapi_file = application.openapi_paths[spec_type]

            if not openapi_file.exists():
                continue

            successful_runs = count_successful_runs(
                task_path, spec_type, experiment,
            )
            if successful_runs < max_runs:
                incomplete_tasks.append(
                    (task_path, spec_type, openapi_file),
                )

    return incomplete_tasks


def run_evaluation_cycle(
    incomplete_tasks: list[tuple[Path, OpenAPIType, Path]],
    application: Application,
    url: str,
    username: str,
    password: str,
    llm_model: str,
    llm_temperature: float,
    max_runs: int,
    cycle_count: int,
    start_time: float,
    experiment: str,
) -> int:
    """Run a single evaluation cycle and return number of completed tasks."""
    completed_tasks = 0

    for task_idx, (task_path, spec_type, openapi_file) in enumerate(incomplete_tasks, 1):
        logger.info(
            'Processing task',
            cycle=cycle_count,
            progress=f"{task_idx}/{len(incomplete_tasks)}",
            task_id=task_path.parent.name,
            spec=spec_type.value,
            current_runs=count_successful_runs(
                task_path, spec_type, experiment,
            ),
            max_runs=max_runs,
            elapsed_time=f"{time.time() - start_time:.1f}s",
        )

        run_evaluation_task(
            application=application,
            spec_type=spec_type,
            task_path=task_path,
            openapi_file=openapi_file,
            url=url,
            username=username,
            password=password,
            llm_model=llm_model,
            llm_temperature=llm_temperature,
            max_runs=max_runs,
            experiment=experiment,
        )
        completed_tasks += 1

    return completed_tasks


def run_continuous_evaluation(
    application: Application,
    url: str,
    username: str,
    password: str,
    llm_model: str,
    llm_temperature: float,
    max_runs: int,
    experiment: str,
) -> None:
    """Run continuous evaluation until all tasks are completed."""
    all_task_paths = application.task_path_list
    total_tasks = len(all_task_paths) * len(OpenAPIType)

    logger.info(
        'Starting evaluation run',
        application=f"{application.owner}/{application.repo}",
        url=url,
        specs=[s.value for s in OpenAPIType],
        total_tasks=total_tasks,
        llm_model=llm_model,
        llm_temperature=llm_temperature,
        max_runs_per_task=max_runs,
    )

    # Print initial task status table
    print_task_status_table(
        all_task_paths, application.openapi_paths,
        max_runs, experiment=experiment,
    )

    # Start continuous evaluation
    start_time = time.time()
    completed_tasks = 0
    skipped_tasks = 0
    cycle_count = 0

    logger.info(
        'Starting continuous evaluation run',
        application=f"{application.owner}/{application.repo}",
        url=url,
        specs=[s.value for s in OpenAPIType],
        total_task_spec_combinations=len(
            all_task_paths,
        ) * len(OpenAPIType),
        llm_model=llm_model,
        llm_temperature=llm_temperature,
        max_runs_per_task=max_runs,
    )

    while True:
        cycle_count += 1
        incomplete_tasks = get_incomplete_tasks(
            all_task_paths, application, max_runs, experiment=experiment,
        )

        if not incomplete_tasks:
            logger.info(
                'All tasks completed - evaluation finished',
                total_cycles=cycle_count,
                total_time=f"{time.time() - start_time:.1f}s",
            )
            break

        logger.info(
            'Starting evaluation cycle',
            cycle=cycle_count,
            incomplete_tasks=len(incomplete_tasks),
            total_task_spec_combinations=len(
                all_task_paths,
            ) * len(OpenAPIType),
            elapsed_time=f"{time.time() - start_time:.1f}s",
        )

        cycle_completed_tasks = run_evaluation_cycle(
            incomplete_tasks,
            application,
            url,
            username,
            password,
            llm_model,
            llm_temperature,
            max_runs,
            cycle_count,
            start_time,
            experiment,
        )
        completed_tasks += cycle_completed_tasks

        logger.info(
            'Cycle completed',
            cycle=cycle_count,
            tasks_processed_this_cycle=len(incomplete_tasks),
            total_tasks_processed=completed_tasks,
            tasks_skipped=skipped_tasks,
            elapsed_time=f"{time.time() - start_time:.1f}s",
        )

    total_time = time.time() - start_time
    logger.info(
        'Evaluation run completed',
        total_cycles=cycle_count,
        total_tasks_processed=completed_tasks,
        tasks_skipped=skipped_tasks,
        total_time=f"{total_time:.1f}s",
        avg_time_per_task=f"{total_time / max(completed_tasks, 1):.1f}s" if completed_tasks > 0 else 'N/A',
    )
