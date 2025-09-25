import requests


def verify(agent_output: str, base_url: str, authenticated_session: requests.Session) -> bool:
    response = authenticated_session.get(
        f"{base_url}/api/songs/9fdab923-f999-4ad8-bd65-fcc2a66ed39b",
    )
    return response.json()['album_name'] == 'Rush'
