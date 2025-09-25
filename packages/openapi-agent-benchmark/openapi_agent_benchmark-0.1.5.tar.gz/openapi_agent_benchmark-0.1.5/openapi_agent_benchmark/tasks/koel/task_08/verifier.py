import requests


def verify(agent_output: str, base_url: str, authenticated_session: requests.Session) -> bool:
    response = authenticated_session.get(f"{base_url}/api/songs")
    songs = [
        song['title'].lower()
        for song in response.json()['data']
    ]
    return 'wonderful tonight' not in songs
