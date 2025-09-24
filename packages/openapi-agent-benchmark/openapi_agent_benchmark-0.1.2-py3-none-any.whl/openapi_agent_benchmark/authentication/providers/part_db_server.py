import bs4
import requests
import structlog
import typer

from openapi_agent_benchmark.authentication.provider import CookieAuthProvider

app = typer.Typer()
logger = structlog.get_logger(__name__)


class PartDbServerAuthProvider(CookieAuthProvider):
    """PartDbServer session cookie authentication provider."""

    def authenticate_session(self, session: requests.Session, url: str) -> None:
        """Authenticate the session by performing PartDbServer login."""
        logger.info('Attempting PartDbServer authentication...')

        base_url = self._get_base_url(url)

        # Get CSRF token
        response = session.get(f'{base_url}/en/login')
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': '_csrf_token'})['value']
        logger.info('PartDbServer CSRF token obtained', csrf_token=csrf_token)

        # Login
        response = session.post(
            f'{base_url}/en/login',
            data={
                '_username': self.username,
                '_password': self.password,
                '_csrf_token': csrf_token,
                '_remember_me': 'on',
                '_target_path': '/',
            },
            allow_redirects=False,
        )

        if response.status_code != 302:
            raise Exception(
                f'Login failed with status code: {response.status_code}',
            )

        # Verify session cookie
        response = session.get(f'{base_url}/en/user/settings')
        if response.status_code != 200:
            raise Exception('Session verification failed')

        if self.username not in response.text:
            raise Exception('Session verification failed - username not found')

        logger.info('PartDbServer authentication successful')


@app.command()
def main(
    url: str = typer.Option(
        ..., '--url',
        help='URL to get PartDbServer session cookie from.',
    ),
    username: str = typer.Option(
        ..., '--username',
        help='PartDbServer username.',
    ),
    password: str = typer.Option(
        ..., '--password',
        help='PartDbServer password.',
    ),
):
    """Get PartDbServer session cookie."""
    provider = PartDbServerAuthProvider(username, password)
    try:
        session = provider.get_requests_session(url)
        logger.info(
            'PartDbServer authentication successful',
            cookies=dict(session.cookies),
        )
    except Exception as e:
        logger.error('Error getting PartDbServer session cookie', error=e)


if __name__ == '__main__':
    app()
