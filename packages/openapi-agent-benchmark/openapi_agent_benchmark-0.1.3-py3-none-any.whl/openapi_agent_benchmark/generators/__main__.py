import os
import shutil
from pathlib import Path

import instructor
import requests
import structlog
import typer
from dotenv import load_dotenv
from jinja2 import Template
from openai import OpenAI

from openapi_agent_benchmark.applications import get_applications
from openapi_agent_benchmark.generators.models import TaskList

load_dotenv()

logger = structlog.get_logger(__name__)
app = typer.Typer()


def _get_openai_client() -> instructor.Instructor:
    """Create and return OpenAI client."""
    return instructor.from_openai(
        OpenAI(
            api_key=os.getenv('DEEPSEEK_API_KEY'),
            base_url='https://api.deepseek.com',
        ),
    )


def _render_prompt(description: str, num_tasks: int) -> str:
    """Render the prompt template with given parameters."""
    template_path = Path(__file__).parent / 'prompt.tpl'
    template = Template(template_path.read_text(encoding='utf-8'))
    return template.render(description=description, num_tasks=num_tasks)


def _generate_tasks_with_llm(prompt: str) -> TaskList:
    """Generate tasks using LLM from the given prompt."""
    client = _get_openai_client()
    logger.info(
        'Generating tasks with LLM',
        model='deepseek-chat',
        prompt_length=len(prompt),
    )

    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=[{'role': 'user', 'content': prompt}],
        response_model=TaskList,
    )
    logger.info(
        'Tasks generated successfully',
        task_count=len(response.tasks),
        model='deepseek-chat',
    )
    return response


@app.command()
def download_readme():
    """Download README files for all applications."""
    applications = get_applications()
    logger.info(
        'Starting README download process',
        total_applications=len(applications),
    )

    for i, application in enumerate(applications, 1):
        logger.info(
            'Downloading README',
            application=application.repo,
            owner=application.owner,
            progress=f'{i}/{len(applications)}',
            url=application.readme_url,
            target_path=str(application.readme_path),
        )

        # Create directory if it doesn't exist
        application.readme_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            # Download and save README
            response = requests.get(application.readme_url, timeout=30)
            response.raise_for_status()
            application.readme_path.write_bytes(response.content)

            logger.info(
                'README downloaded successfully',
                application=application.repo,
                file_size=len(response.content),
                status_code=response.status_code,
            )
        except requests.RequestException as e:
            logger.error(
                'Failed to download README',
                application=application.repo,
                url=application.readme_url,
                error=str(e),
                exc_info=True,
            )


@app.command()
def generate_description():
    """Copy README files to description files."""
    applications = get_applications()
    logger.info(
        'Starting description generation process',
        total_applications=len(applications),
    )

    for i, application in enumerate(applications, 1):
        logger.info(
            'Generating description',
            application=application.repo,
            owner=application.owner,
            progress=f'{i}/{len(applications)}',
            source_path=str(application.readme_path),
            target_path=str(application.agent_description_path),
        )

        try:
            shutil.copy(
                application.readme_path,
                application.agent_description_path,
            )
            logger.info(
                'Description generated successfully',
                application=application.repo,
            )
        except (OSError, shutil.Error) as e:
            logger.error(
                'Failed to generate description',
                application=application.repo,
                error=str(e),
                exc_info=True,
            )


@app.command()
def generate_prompt(num_tasks: int = typer.Option(10, help='Number of tasks to generate')):
    """Generate prompts from description files."""
    applications = get_applications()
    logger.info(
        'Starting prompt generation process',
        total_applications=len(applications),
        num_tasks=num_tasks,
    )

    for i, application in enumerate(applications, 1):
        logger.info(
            'Generating prompt',
            application=application.repo,
            owner=application.owner,
            progress=f'{i}/{len(applications)}',
            num_tasks=num_tasks,
            prompt_path=str(application.prompt_path),
        )

        try:
            prompt = _render_prompt(application.description, num_tasks)
            application.prompt_path.write_text(prompt, encoding='utf-8')

            logger.info(
                'Prompt generated successfully',
                application=application.repo,
                description_length=len(application.description),
                prompt_length=len(prompt),
            )
        except (OSError, UnicodeDecodeError) as e:
            logger.error(
                'Failed to generate prompt',
                application=application.repo,
                error=str(e),
                exc_info=True,
            )


@app.command()
def generate_tasks():
    """Generate tasks using LLM for all applications."""
    applications = get_applications()
    logger.info(
        'Starting task generation process',
        total_applications=len(applications),
        model='deepseek-chat',
    )

    for i, application in enumerate(applications, 1):
        logger.info(
            'Processing application',
            application=application.repo,
            owner=application.owner,
            progress=f'{i}/{len(applications)}',
            prompt_path=str(application.prompt_path),
            tasks_path=str(application.agent_tasks_path),
        )

        try:
            prompt = application.prompt_path.read_text(encoding='utf-8')
            logger.info(
                'Prompt loaded successfully',
                application=application.repo,
                prompt_length=len(prompt),
            )

            tasks = _generate_tasks_with_llm(prompt)

            # Save generated tasks
            tasks_json = tasks.model_dump_json(indent=2)
            application.agent_tasks_path.write_text(
                tasks_json, encoding='utf-8',
            )

            logger.info(
                'Tasks saved successfully',
                application=application.repo,
                task_count=len(tasks.tasks),
                output_size=len(tasks_json),
                output_path=str(application.agent_tasks_path),
            )

        except (OSError, requests.RequestException, ValueError) as e:
            logger.error(
                'Failed to generate tasks',
                application=application.repo,
                owner=application.owner,
                error_type=type(e).__name__,
                error=str(e),
                exc_info=True,
            )


if __name__ == '__main__':
    app()
