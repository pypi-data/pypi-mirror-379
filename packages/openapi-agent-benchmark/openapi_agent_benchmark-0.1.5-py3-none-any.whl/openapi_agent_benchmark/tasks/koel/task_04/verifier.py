import requests


def verify(agent_output: str, base_url: str, authenticated_session: requests.Session) -> bool:
    response = authenticated_session.get(f"{base_url}/api/users")
    for user in response.json():
        if user['id'] == 2:
            return user['name'] == 'Bruce Lee'
    return False
