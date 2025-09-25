import requests
import structlog

logger = structlog.get_logger(__name__)


def verify(agent_output: str, base_url: str, authenticated_session: requests.Session) -> bool:
    # Check if the playlist exists
    response = authenticated_session.get(f"{base_url}/api/playlists")
    logger.info(f'Response: {response.json()}')
    playlists = response.json()
    playlist_id = None
    for playlist in playlists:
        if playlist['name'] == 'Workout Mix':
            playlist_id = playlist['id']
            break
    if not playlist_id:
        logger.warning('Playlist `Workout Mix` not found')
        return False
    logger.info('Playlist `Workout Mix` created')

    # Check if the songs of the playlist are correct
    response = authenticated_session.get(
        f"{base_url}/api/playlists/{playlist_id}/songs",
    )
    logger.info(f'Response: {response.json()}')
    for expected_song in ['wonderful tonight', "blowin' in the wind", 'just like a woman']:
        if not any(song['title'].lower() == expected_song.lower() for song in response.json()):
            logger.warning(f'{expected_song} not found in playlist')
            return False
    return True
