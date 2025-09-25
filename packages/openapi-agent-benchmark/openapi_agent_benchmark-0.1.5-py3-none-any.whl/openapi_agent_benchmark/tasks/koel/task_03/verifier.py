import requests


def verify(agent_output: str, base_url: str, authenticated_session: requests.Session) -> bool:
    songs = ["blowin' in the wind", 'just like a woman']
    response_lower = agent_output.lower()
    return all(song in response_lower for song in songs)
