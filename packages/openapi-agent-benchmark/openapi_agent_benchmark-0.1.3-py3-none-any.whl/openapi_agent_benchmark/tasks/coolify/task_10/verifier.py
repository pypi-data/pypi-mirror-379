import requests
import structlog


logger = structlog.get_logger(__name__)


def verify(agent_output: str, base_url: str, authenticated_session: requests.Session) -> bool:
    raise NotImplementedError('Not implemented')
