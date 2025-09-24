import bs4
import requests
import structlog
import typer

from openapi_agent_benchmark.authentication.provider import CookieAuthProvider


app = typer.Typer()
logger = structlog.get_logger(__name__)


class KimaiAuthProvider(CookieAuthProvider):
    """Kimai session cookie authentication provider."""

    def authenticate_session(self, session: requests.Session, url: str) -> None:
        """Authenticate the session by performing Kimai login."""
        logger.info('Attempting Kimai authentication...')

        base_url = self._get_base_url(url)

        # Get CSRF token
        response = session.get(f'{base_url}/en/login')
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': '_csrf_token'})['value']
        logger.info('Kimai CSRF token obtained', csrf_token=csrf_token)

        # Login - cookies will be automatically captured by the session
        response = session.post(
            f'{base_url}/en/login_check',
            data={
                '_username': self.username,
                '_password': self.password,
                '_csrf_token': csrf_token,
            },
            allow_redirects=False,
        )

        if response.status_code != 302:
            raise Exception(
                f'Login failed with status code: {response.status_code}',
            )

        # Verify authentication by checking if we have the session cookie
        session_cookie = session.cookies.get('PHPSESSID')
        if not session_cookie:
            raise Exception('Kimai session cookie not found after login')

        logger.info(
            'Kimai session cookie captured',
            session_cookie=session_cookie,
        )

        # Verify session is working
        response = session.get(f'{base_url}/en/profile/admin')
        if response.status_code != 200:
            raise Exception('Session verification failed')

        if self.username not in response.text:
            raise Exception('Session verification failed - username not found')

        logger.info('Kimai authentication successful')


@app.command()
def main(
    url: str = typer.Option(
        ..., '--url',
        help='URL to authenticate with Kimai.',
    ),
    username: str = typer.Option(
        ..., '--username',
        help='Kimai username.',
    ),
    password: str = typer.Option(
        ..., '--password',
        help='Kimai password.',
    ),
):
    provider = KimaiAuthProvider(username, password)
    try:
        session = provider.get_requests_session(url)
        logger.info(
            'Kimai authentication successful',
            cookies=dict(session.cookies),
        )
    except Exception as e:
        logger.error('Error authenticating with Kimai', error=e)


if __name__ == '__main__':
    app()
