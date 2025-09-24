import bs4
import requests
import structlog
import typer

from openapi_agent_benchmark.authentication.provider import CookieAuthProvider

app = typer.Typer()
logger = structlog.get_logger(__name__)


class FireflyIIIAuthProvider(CookieAuthProvider):
    """FireflyIII session cookie authentication provider."""

    def authenticate_session(self, session: requests.Session, url: str) -> None:
        """Authenticate the session by performing FireflyIII login."""
        logger.info('Attempting FireflyIII authentication...')

        base_url = self._get_base_url(url)

        try:
            # Get CSRF token
            response = session.get(f"{base_url}/login")

            csrf_token = bs4.BeautifulSoup(response.text, 'html.parser').find(
                'meta', {'name': 'csrf-token'},
            )
            if not csrf_token:
                raise ValueError('CSRF token not found in login page')

            # Login
            session.post(
                f"{base_url}/login",
                data={
                    '_token': csrf_token['content'],
                    'email': self.username,
                    'password': self.password,
                    'remember': '1',
                },
                timeout=60,
            )

            logger.info('FireflyIII authentication successful')

        except (requests.RequestException, KeyError, ValueError) as e:
            raise Exception(f"FireflyIII authentication failed: {str(e)}")


@app.command()
def main(
    url: str = typer.Option(
        ..., '--url',
        help='URL to get FireflyIII session cookie from.',
    ),
    username: str = typer.Option(
        ..., '--username',
        help='FireflyIII username.',
    ),
    password: str = typer.Option(
        ..., '--password',
        help='FireflyIII password.',
    ),
):
    """Get FireflyIII session cookie."""
    provider = FireflyIIIAuthProvider(username, password)
    try:
        session = provider.get_requests_session(url)
        logger.info(
            'FireflyIII authentication successful',
            cookies=dict(session.cookies),
        )
    except Exception as e:
        logger.error('Error getting FireflyIII session cookie', error=e)


if __name__ == '__main__':
    app()
