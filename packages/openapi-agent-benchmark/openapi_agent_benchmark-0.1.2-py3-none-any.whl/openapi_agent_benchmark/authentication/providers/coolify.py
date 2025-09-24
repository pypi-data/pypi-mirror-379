import bs4
import requests
import structlog
import typer

from openapi_agent_benchmark.authentication.provider import CookieAuthProvider

app = typer.Typer()
logger = structlog.get_logger(__name__)


class CoolifyAuthProvider(CookieAuthProvider):
    """Coolify session cookie authentication provider."""

    def authenticate_session(self, session: requests.Session, url: str) -> None:
        """Authenticate the session by performing Coolify login."""
        logger.info('Attempting Coolify authentication...')

        base_url = self._get_base_url(url)

        # Get CSRF token
        response = session.get(f'{base_url}/login')
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': '_token'})['value']
        logger.info('Coolify CSRF token obtained', csrf_token=csrf_token)

        # Login
        response = session.post(
            f'{base_url}/login',
            data={
                'email': self.username,
                'password': self.password,
                '_token': csrf_token,
            },
            allow_redirects=False,
        )

        if response.status_code != 302:
            raise Exception(
                f'Login failed with status code: {response.status_code}',
            )

        logger.info('Coolify authentication successful')


@app.command()
def main(
    url: str = typer.Option(
        ..., '--url',
        help='URL to get Coolify session cookie from.',
    ),
    username: str = typer.Option(
        ..., '--username',
        help='Coolify username.',
    ),
    password: str = typer.Option(
        ..., '--password',
        help='Coolify password.',
    ),
):
    """Get Coolify session cookie."""
    provider = CoolifyAuthProvider(username, password)
    try:
        session = provider.get_requests_session(url)
        logger.info(
            'Coolify authentication successful',
            cookies=dict(session.cookies),
        )
    except Exception as e:
        logger.error('Error getting Coolify session cookie', error=e)


if __name__ == '__main__':
    app()
