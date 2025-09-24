import requests
import structlog
import typer

from openapi_agent_benchmark.authentication.provider import TokenAuthProvider

app = typer.Typer()
logger = structlog.get_logger(__name__)


class InvoiceNinjaAuthProvider(TokenAuthProvider):
    """InvoiceNinja token authentication provider."""

    def get_token(self, url: str) -> str:
        """Get InvoiceNinja authentication token."""
        logger.info('Attempting to get InvoiceNinja authentication token...')
        base_url = self._get_base_url(url)

        response = requests.post(
            f"{base_url}/api/v1/login?first_load=true&include_static=true&einvoice=true",
            json={
                'email': self.username,
                'password': self.password,
                'one_time_password': '',
            },
            timeout=60,
        )
        token = response.json()['data'][0]['token']['token']

        logger.info(
            'InvoiceNinja authentication successful',
            token_length=len(token),
            token_prefix=f"{token[:10]}..." if len(token) > 10 else token,
        )
        return token


@app.command()
def main(
    url: str = typer.Option(
        ..., '--url',
        help='URL to get InvoiceNinja authentication token from.',
    ),
    username: str = typer.Option(
        ..., '--username',
        help='InvoiceNinja username.',
    ),
    password: str = typer.Option(
        ..., '--password',
        help='InvoiceNinja password.',
    ),
):
    """Get InvoiceNinja authentication token."""
    provider = InvoiceNinjaAuthProvider(username, password)
    try:
        logger.info(
            'InvoiceNinja authentication token',
            token=provider.get_token(url),
        )
    except Exception as e:
        logger.error(
            'Error getting InvoiceNinja authentication token', error=e,
        )


if __name__ == '__main__':
    app()
