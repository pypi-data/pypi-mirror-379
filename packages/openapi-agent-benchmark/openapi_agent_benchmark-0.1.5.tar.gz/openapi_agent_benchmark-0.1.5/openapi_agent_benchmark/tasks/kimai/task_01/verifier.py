import requests


def verify(agent_output: str, base_url: str, authenticated_session: requests.Session) -> bool:
    response = authenticated_session.get(f"{base_url}/api/projects")
    return any(project['name'] == 'Website Redesign' and project['parentTitle'] == 'Google' for project in response.json())
