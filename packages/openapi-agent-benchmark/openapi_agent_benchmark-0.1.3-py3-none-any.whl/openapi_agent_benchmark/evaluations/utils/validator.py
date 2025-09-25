"""Utility functions for agent evaluation."""
import json
from pathlib import Path

import structlog
from rich.console import Console
from rich.table import Table

from openapi_agent_benchmark.evaluations.models.openapi_type import OpenAPIType

logger = structlog.get_logger(__name__)


def is_valid_json_file(file_path: Path) -> bool:
    """Check if a file exists and contains valid JSON."""
    try:
        if not file_path.exists():
            return False
        with open(file_path, encoding='utf-8') as f:
            json.load(f)
        return True
    except (json.JSONDecodeError, OSError, UnicodeDecodeError):
        return False


def is_valid_task_result(task_path: Path, result_file: Path) -> bool:
    """
    Check if a result file is valid for the given task.
    Validates that the result input matches the current task description.

    Args:
        task_path: Path to the task.json file
        result_file: Path to the result.json file

    Returns:
        True if the result is valid (description matches), False otherwise
    """
    # Check if result file is valid JSON
    if not is_valid_json_file(result_file):
        return False

    # Read the current task description
    try:
        task_data = json.loads(task_path.read_text())
        current_description = task_data.get('description', '')
    except (json.JSONDecodeError, OSError, UnicodeDecodeError):
        logger.warning(
            'Failed to read task description - skipping description validation',
            task_path=str(task_path),
        )
        return False

    # Read the result input
    try:
        result_data = json.loads(result_file.read_text())
        result_input = result_data.get('input', '')
    except (json.JSONDecodeError, OSError, UnicodeDecodeError) as e:
        logger.warning(
            'Failed to read result input - skipping description validation',
            task_path=str(task_path),
            result_file=str(result_file),
            error=str(e),
        )
        return False

    # Check if description matches input
    if current_description.strip() != result_input.strip():
        logger.debug(
            'Result description mismatch',
            task_id=task_path.parent.name,
            result_file=str(result_file),
            current_description=current_description[:100] + '...' if len(
                current_description,
            ) > 100 else current_description,
            result_input=result_input[:100] + '...' if len(
                result_input,
            ) > 100 else result_input,
        )
        return False

    return True


def count_successful_runs(task_path: Path, spec_type: OpenAPIType, experiment: str) -> int:
    """
    Count the number of successful runs for a given task and spec type.
    Only counts runs where the task description matches the result input.

    Args:
        task_path: Path to the task.json file
        spec_type: The OpenAPI spec type
        experiment: The experiment name
    Returns:
        Number of successful runs (with valid result.json and trace.json and matching description)
    """
    spec_name = spec_type.value
    spec_folder = task_path.parent / 'results' / experiment / spec_name.lower()

    if not spec_folder.exists():
        return 0

    successful_runs = []
    for run_dir in spec_folder.iterdir():
        if run_dir.is_dir():
            result_file = run_dir / 'result.json'
            trace_file = run_dir / 'trace.json'

            # Check if both files exist and are valid JSON
            if not all([
                is_valid_json_file(result_file),
                is_valid_json_file(trace_file),
            ]):
                continue

            # Check if the result is valid for this task (description matches)
            if not is_valid_task_result(task_path, result_file):
                continue

            successful_runs.append(run_dir)

    return len(successful_runs)


def print_task_status_table(
    all_task_paths: list[Path],
    openapi_paths: dict[OpenAPIType, Path],
    max_runs: int,
    experiment: str,
) -> None:
    """
    Print a table showing the execution status of all tasks using Rich.

    Args:
        all_task_paths: List of all task.json file paths
        openapi_paths: Dictionary mapping spec names to OpenAPI file paths
        max_runs: Maximum number of runs per task
        experiment: The experiment name
    """
    console = Console()

    # Create the main table
    table = Table(
        title='Task Execution Status',
        show_header=True, header_style='bold magenta',
    )
    table.add_column('Task ID', style='cyan', no_wrap=True)
    table.add_column('Spec', style='green', no_wrap=True)
    table.add_column('Expected', justify='center', style='blue')
    table.add_column('Completed', justify='center', style='yellow')
    table.add_column('Status', style='bold')
    table.add_column('Progress', justify='center')

    total_expected = 0
    total_completed = 0

    for spec_name in OpenAPIType:
        spec_type = OpenAPIType(spec_name)
        openapi_file = openapi_paths[spec_type]
        for task_path in all_task_paths:
            task_id = task_path.parent.name

            if not openapi_file.exists():
                status = '[red]SKIP (No Spec)[/red]'
                completed = 0
                progress = 'N/A'
            else:
                completed = count_successful_runs(
                    task_path, spec_type, experiment,
                )
                if completed >= max_runs:
                    status = '[green]COMPLETED[/green]'
                    progress = '[green]100%[/green]'
                elif completed > 0:
                    status = '[yellow]IN PROGRESS[/yellow]'
                    progress_percent = int(completed / max_runs * 100)
                    progress = f"[yellow]{progress_percent}%[/yellow]"
                else:
                    status = '[blue]PENDING[/blue]'
                    progress = '[blue]0%[/blue]'

            total_expected += max_runs
            total_completed += completed

            table.add_row(
                task_id,
                spec_name.value,
                str(max_runs),
                str(completed),
                status,
                progress,
            )

    # Add summary row
    overall_progress = int(
        total_completed / total_expected * 100,
    ) if total_expected > 0 else 0
    overall_progress_str = f"[bold green]{overall_progress}%[/bold green]" if overall_progress == 100 else f"[bold yellow]{overall_progress}%[/bold yellow]"

    table.add_row(
        '[bold]TOTAL[/bold]',
        '[bold]ALL[/bold]',
        f"[bold]{total_expected}[/bold]",
        f"[bold]{total_completed}[/bold]",
        '[bold]OVERALL[/bold]',
        overall_progress_str,
    )

    console.print(table)

    # Print summary information
    console.print('\n[bold]Summary:[/bold]')
    console.print(
        f"Total task-spec combinations: [cyan]{len(all_task_paths) * len(OpenAPIType)}[/cyan]",
    )
    console.print(f"Expected total runs: [blue]{total_expected}[/blue]")
    console.print(f"Completed runs: [green]{total_completed}[/green]")
    console.print(
        f"Remaining runs: [yellow]{total_expected - total_completed}[/yellow]",
    )
    console.print()
