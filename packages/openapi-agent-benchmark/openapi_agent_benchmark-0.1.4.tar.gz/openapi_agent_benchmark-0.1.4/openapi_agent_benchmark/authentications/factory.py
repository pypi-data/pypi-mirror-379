import structlog

from openapi_agent_benchmark.authentications.provider import BaseAuthProvider
from openapi_agent_benchmark.authentications.providers.bookstack import BookStackAuthProvider
from openapi_agent_benchmark.authentications.providers.coolify import CoolifyAuthProvider
from openapi_agent_benchmark.authentications.providers.fireflyiii import FireflyIIIAuthProvider
from openapi_agent_benchmark.authentications.providers.invoiceninja import InvoiceNinjaAuthProvider
from openapi_agent_benchmark.authentications.providers.kimai import KimaiAuthProvider
from openapi_agent_benchmark.authentications.providers.koel import KoelAuthProvider
from openapi_agent_benchmark.authentications.providers.partdbserver import PartDbServerAuthProvider

logger = structlog.get_logger(__name__)


class AuthProviderFactory:
    """Factory for creating authentication providers based on application type."""

    _providers: dict[tuple[str, str], type[BaseAuthProvider]] = {
        ('koel', 'koel'): KoelAuthProvider,
        ('part-db', 'part-db-server'): PartDbServerAuthProvider,
        ('coollabsio', 'coolify'): CoolifyAuthProvider,
        ('kimai', 'kimai'): KimaiAuthProvider,
        ('bookstackapp', 'bookstack'): BookStackAuthProvider,
        ('invoiceninja', 'invoiceninja'): InvoiceNinjaAuthProvider,
        ('firefly-iii', 'firefly-iii'): FireflyIIIAuthProvider,
    }

    @classmethod
    def create_provider(cls, owner: str, repo: str, username: str, password: str) -> BaseAuthProvider:
        """Create an authentication provider for the given application."""
        key = (owner, repo)

        if key not in cls._providers:
            raise ValueError(
                f'No authentication provider found for application {owner}/{repo}',
            )

        provider_class = cls._providers[key]
        logger.info(
            'Creating authentication provider',
            owner=owner,
            repo=repo,
            provider_type=provider_class.__name__,
        )
        return provider_class(username, password)
