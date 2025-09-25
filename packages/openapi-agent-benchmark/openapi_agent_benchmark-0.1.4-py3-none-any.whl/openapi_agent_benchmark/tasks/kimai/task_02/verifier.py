import requests


def verify(agent_output: str, base_url: str, authenticated_session: requests.Session) -> bool:
    return all([
        'Google' in agent_output,
        'OpenAI' in agent_output,
    ])
