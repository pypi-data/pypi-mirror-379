import bs4
import requests
import structlog
import typer

from openapi_agent_benchmark.authentication.provider import CookieAuthProvider

app = typer.Typer()
logger = structlog.get_logger(__name__)


class BookStackAuthProvider(CookieAuthProvider):
    """BookStack session cookie authentication provider."""

    def authenticate_session(self, session: requests.Session, url: str) -> None:
        """Authenticate the session by performing BookStack login."""
        logger.info('Attempting BookStack authentication...')

        base_url = self._get_base_url(url)

        # Get CSRF token
        response = session.get(f'{base_url}/login')
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': '_token'})['value']
        logger.info('BookStack CSRF token obtained', csrf_token=csrf_token)

        # Login
        session.post(
            f'{base_url}/login',
            data={
                'email': self.username,
                'password': self.password,
                '_token': csrf_token,
                'remember': 'on',
            },
            timeout=60,
        )

        logger.info('BookStack authentication successful')


@app.command()
def main(
    url: str = typer.Option(
        ..., '--url',
        help='URL to get BookStack session cookie from.',
    ),
    username: str = typer.Option(
        ..., '--username',
        help='BookStack username.',
    ),
    password: str = typer.Option(
        ..., '--password',
        help='BookStack password.',
    ),
):
    """Get BookStack session cookie."""
    provider = BookStackAuthProvider(username, password)
    try:
        session = provider.get_requests_session(url)
        logger.info(
            'BookStack authentication successful',
            cookies=dict(session.cookies),
        )
    except Exception as e:
        logger.error('Error getting BookStack session cookie', error=e)


if __name__ == '__main__':
    app()
