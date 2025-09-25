import requests


def verify(agent_output: str, base_url: str, authenticated_session: requests.Session) -> bool:
    http_response = authenticated_session.get(f"{base_url}/api/users")
    return any(user['email'] == 'john@example.com' for user in http_response.json())
