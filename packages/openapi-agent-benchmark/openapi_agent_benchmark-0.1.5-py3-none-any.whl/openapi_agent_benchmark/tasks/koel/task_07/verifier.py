import requests
import structlog


logger = structlog.get_logger()


def verify(agent_output: str, base_url: str, authenticated_session: requests.Session) -> bool:
    response_lower = agent_output.lower()
    song2year = [
        ('tears in heaven', 1991),
        ('just like a woman', 1966),
        ("blowin' in the wind", 1963),
    ]
    # Check if the songs are in the response
    for song, _ in song2year:
        if song not in response_lower:
            logger.warning(f'Song `{song}` not found in response')
            return False
    # Check the order of the songs
    if not (response_lower.index('tears in heaven') < response_lower.index('just like a woman') < response_lower.index("blowin' in the wind")):
        logger.warning('Songs are not in the correct order')
        return False
    logger.info('Songs are in the correct order')
    return True


def main():
    assert verify("The songs by genre 'Folk' and sorted by year in descending order are: 1. 'Tears in Heaven' 2. 'Just Like A Woman' 3. 'Blowin' in the Wind'")
    assert not verify(
        "The songs by genre 'Folk' and sorted by year in descending order are: 1. 'Blowin' in the Wind' 2. 'Tears in Heaven' 3. 'Just Like A Woman'",
    )
    assert not verify(
        "The songs by genre 'Folk' and sorted by year in descending order are: 1. 'Blowin' in the Wind' 2. 'Just Like A Woman'",
    )


if __name__ == '__main__':
    main()
