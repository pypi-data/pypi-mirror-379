from urllib.parse import urlparse

import requests
import structlog
import typer

from openapi_agent_benchmark.authentication.provider import TokenAuthProvider

app = typer.Typer()
logger = structlog.get_logger(__name__)


class KoelAuthProvider(TokenAuthProvider):
    """Koel token authentication provider."""

    def get_token(self, url: str) -> str:
        """Get Koel authentication token."""
        logger.info('Attempting to get Koel authentication token...')
        parsed_url = urlparse(url)
        host = parsed_url.hostname
        port = parsed_url.port

        response = requests.post(
            f'http://{host}:{port}/api/me',
            data={
                'email': self.username,
                'password': self.password,
            },
            timeout=60,
        )
        if response.status_code != 200:
            raise Exception(
                f'Koel authentication failed with status code: {response.status_code}',
            )

        data = response.json()
        token = data['token']

        logger.info(
            'Koel authentication successful',
            token_length=len(token),
            token_prefix=f"{token[:10]}..." if len(token) > 10 else token,
        )
        return token


@app.command()
def main(
    url: str = typer.Option(
        ..., '--url',
        help='URL to get Koel authentication token from.',
    ),
    username: str = typer.Option(
        ..., '--username',
        help='Koel username.',
    ),
    password: str = typer.Option(
        ..., '--password',
        help='Koel password.',
    ),
):
    """Get Koel authentication token."""
    provider = KoelAuthProvider(username, password)
    try:
        logger.info('Koel authentication token', token=provider.get_token(url))
    except Exception as e:
        logger.error('Error getting Koel authentication token', error=e)


if __name__ == '__main__':
    app()
