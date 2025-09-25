import requests


def verify(agent_output: str, base_url: str, authenticated_session: requests.Session) -> bool:
    songs = [
        'wonderful tonight',
        "blowin' in the wind",
        'just like a woman',
        'hey jude',
        'tears in heaven',
    ]
    return all(song.lower() in agent_output.lower() for song in songs)
