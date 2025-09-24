import structlog

from openapi_agent_benchmark.authentication.provider import BaseAuthProvider
from openapi_agent_benchmark.authentication.provider import NoAuthProvider
from openapi_agent_benchmark.authentication.providers.bookstack import BookStackAuthProvider
from openapi_agent_benchmark.authentication.providers.coolify import CoolifyAuthProvider
from openapi_agent_benchmark.authentication.providers.fireflyiii import FireflyIIIAuthProvider
from openapi_agent_benchmark.authentication.providers.invoiceninja import InvoiceNinjaAuthProvider
from openapi_agent_benchmark.authentication.providers.kimai import KimaiAuthProvider
from openapi_agent_benchmark.authentication.providers.koel import KoelAuthProvider
from openapi_agent_benchmark.authentication.providers.part_db_server import PartDbServerAuthProvider

logger = structlog.get_logger(__name__)


class AuthProviderFactory:
    """Factory for creating authentication providers based on application type."""

    _providers: dict[str, type[BaseAuthProvider]] = {
        'koel': KoelAuthProvider,
        'invoiceninja': InvoiceNinjaAuthProvider,
        'bookstack': BookStackAuthProvider,
        'firefly-iii': FireflyIIIAuthProvider,
        'part-db-server': PartDbServerAuthProvider,
        'coolify': CoolifyAuthProvider,
        'kimai': KimaiAuthProvider,
    }

    @classmethod
    def create_provider(cls, name: str, username: str, password: str) -> BaseAuthProvider:
        """Create an authentication provider for the given application."""
        if name not in cls._providers:
            logger.warning(
                'No authentication provider found for application',
                application=name,
                available_providers=list(cls._providers.keys()),
            )
            return NoAuthProvider(username, password)

        provider_class = cls._providers[name]
        logger.info(
            'Creating authentication provider',
            application=name,
            provider_type=provider_class.__name__,
        )
        return provider_class(username, password)

    @classmethod
    def register_provider(cls, name: str, provider_class: type[BaseAuthProvider]) -> None:
        """Register a new authentication provider."""
        cls._providers[name] = provider_class
        logger.info(
            'Registered new authentication provider',
            name=name,
            provider_type=provider_class.__name__,
        )

    @classmethod
    def get_available_providers(cls) -> list[tuple[str, str]]:
        """Get list of available provider names and their provider class names."""
        return [(name, provider.__name__) for name, provider in cls._providers.items()]
