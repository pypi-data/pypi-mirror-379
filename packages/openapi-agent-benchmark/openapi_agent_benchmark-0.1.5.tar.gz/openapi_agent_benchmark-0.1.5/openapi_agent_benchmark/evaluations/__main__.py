import dotenv
import structlog
import typer

from openapi_agent_benchmark.applications import get_applications
from openapi_agent_benchmark.evaluations.runner import run_continuous_evaluation

dotenv.load_dotenv()
logger = structlog.get_logger(__name__)
app = typer.Typer(add_completion=False, pretty_exceptions_enable=False)


@app.command()
def main(
    owner: str = typer.Option(
        None, '--owner', '-o',
        help='Owner of the project.',
    ),
    repo: str = typer.Option(
        None, '--repo', '-r',
        help='Repository of the project.',
    ),
    url: str = typer.Option(
        None, '--url', help='URL of the application.',
    ),
    username: str = typer.Option(
        None, '--username', help='Username of the application.',
    ),
    password: str = typer.Option(
        None, '--password', help='Password of the application.',
    ),
    llm_model: str = typer.Option(
        'deepseek-chat', '--llm-model', help='LLM model name.',
        show_default=True,
    ),
    llm_temperature: float = typer.Option(
        0.0, '--llm-temp', help='LLM temperature.',
    ),
    max_runs: int = typer.Option(
        1, '--max-runs', help='Maximum number of runs per task before skipping.',
        show_default=True,
    ),
    experiment: str = typer.Option(
        'default', '--experiment', '-e', help='Experiment name',
        show_default=True,
    ),
):
    """Main entry point for the automated agent evaluation harness."""
    applications = get_applications(owner, repo)
    for application in applications:
        run_continuous_evaluation(
            application=application,
            url=url,
            username=username,
            password=password,
            llm_model=llm_model,
            llm_temperature=llm_temperature,
            max_runs=max_runs,
            experiment=experiment,
        )


if __name__ == '__main__':
    app()
