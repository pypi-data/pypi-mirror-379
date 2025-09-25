from dataclasses import dataclass
from pathlib import Path

from openapi_agent_benchmark.evaluations.models.openapi_type import OpenAPIType
from openapi_agent_benchmark.utils.name import sanitize


@dataclass
class Application:
    owner: str
    repo: str
    version: str
    commit_hash: str

    @property
    def readme_url(self) -> str:
        return f'https://raw.githubusercontent.com/{self.owner}/{self.repo}/{self.commit_hash}/README.md'

    @property
    def readme_path(self) -> Path:
        return Path(__file__).parent.parent / 'generators' / 'prompts' / self.owner / self.repo / self.version / self.commit_hash / 'README.md'

    @property
    def readme(self) -> str:
        return self.readme_path.read_text(encoding='utf-8')

    @property
    def description_path(self) -> Path:
        return Path(__file__).parent.parent / 'generators' / 'prompts' / self.owner / self.repo / self.version / self.commit_hash / 'description.txt'

    @property
    def description(self) -> str:
        description_path = Path(__file__).parent.parent / 'generators' / 'prompts' / \
            self.owner / self.repo / self.version / self.commit_hash / 'description.txt'
        return description_path.read_text(encoding='utf-8')

    @property
    def prompt_path(self) -> Path:
        return Path(__file__).parent.parent / 'generators' / 'prompts' / self.owner / self.repo / self.version / self.commit_hash / 'prompt.txt'

    @property
    def prompt(self) -> str:
        prompt_path = Path(__file__).parent.parent / 'generators' / 'prompts' / \
            self.owner / self.repo / self.version / self.commit_hash / 'prompt.txt'
        return prompt_path.read_text(encoding='utf-8')

    @property
    def multipass_instance_name(self) -> str:
        return sanitize(self.repo)

    @property
    def multipass_snapshot_name(self) -> str:
        return 'agent'

    @property
    def openapi_paths(self) -> dict[OpenAPIType, Path]:
        return {
            OpenAPIType.OFFICIAL: self.official_openapi_path,
            OpenAPIType.ENDPOINT: self.endpoint_openapi_path,
            OpenAPIType.ENDPOINT_PARAMETERS: self.endpoint_parameters_openapi_path,
            OpenAPIType.ENDPOINT_PARAMETERS_CONSTRAINTS: self.endpoint_parameters_constraints_openapi_path,
            OpenAPIType.ENDPOINT_PARAMETERS_CONSTRAINTS_FEEDBACK: self.endpoint_parameters_constraints_feedback_openapi_path,
        }

    @property
    def official_openapi_path(self) -> Path:
        return Path(__file__).parent.parent / 'specifications' / self.owner / self.repo / self.version / self.commit_hash / 'official' / 'openapi.json'

    @property
    def endpoint_openapi_path(self) -> Path:
        return Path(__file__).parent.parent / 'specifications' / self.owner / self.repo / self.version / self.commit_hash / 'endpoint' / 'openapi.json'

    @property
    def endpoint_parameters_openapi_path(self) -> Path:
        return Path(__file__).parent.parent / 'specifications' / self.owner / self.repo / self.version / self.commit_hash / 'endpoint-parameter' / 'openapi.json'

    @property
    def endpoint_parameters_constraints_openapi_path(self) -> Path:
        return Path(__file__).parent.parent / 'specifications' / self.owner / self.repo / self.version / self.commit_hash / 'endpoint-parameter-constraint' / 'openapi.json'

    @property
    def endpoint_parameters_constraints_feedback_openapi_path(self) -> Path:
        return Path(__file__).parent.parent / 'specifications' / self.owner / self.repo / self.version / self.commit_hash / 'endpoint-parameter-constraint-feedback' / 'openapi.json'

    @property
    def task_path_list(self) -> list[Path]:
        task_folder = Path(__file__).parent.parent / 'tasks' / self.repo
        return sorted(list(task_folder.glob('**/task.json')))
