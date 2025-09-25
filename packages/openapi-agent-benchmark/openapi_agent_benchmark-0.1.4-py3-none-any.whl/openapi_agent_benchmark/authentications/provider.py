from abc import ABC
from abc import abstractmethod
from urllib.parse import urlparse

import requests
import structlog
from langchain_community.utilities.requests import RequestsWrapper

logger = structlog.get_logger(__name__)


class BaseAuthProvider(ABC):
    """Base class for authentication providers that contain the core auth logic."""

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @abstractmethod
    def get_requests_wrapper(self, url: str) -> RequestsWrapper:
        """Get a configured RequestsWrapper for the given URL."""

    def get_requests_session(self, url: str) -> requests.Session:
        """Return an authenticated requests.Session for the given URL.

        Default implementation builds a Session and applies headers returned by
        get_requests_wrapper. Subclasses may override for finer control.
        """
        wrapper = self.get_requests_wrapper(url)
        session = requests.Session()
        # RequestsWrapper exposes headers as an attribute; apply to session
        if getattr(wrapper, 'headers', None):
            session.headers.update(wrapper.headers)
        return session

    def _get_base_url(self, url: str) -> str:
        """Extract base URL from full URL."""
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}"


class TokenAuthProvider(BaseAuthProvider):
    """Base class for token-based authentication providers."""

    @abstractmethod
    def get_token(self, url: str) -> str:
        """Get authentication token."""

    def get_requests_wrapper(self, url: str) -> RequestsWrapper:
        """Get RequestsWrapper with token authentication."""
        token = self.get_token(url)
        headers = {
            'Authorization': f"Bearer {token}",
            'Accept': 'application/json, text/plain, */*',
        }
        return RequestsWrapper(headers=headers)

    def get_requests_session(self, url: str) -> requests.Session:
        """Return a Session with Authorization header."""
        token = self.get_token(url)
        session = requests.Session()
        session.headers.update({
            'Authorization': f"Bearer {token}",
        })
        return session


class CookieAuthProvider(BaseAuthProvider):
    """Base class for cookie-based authentication providers."""

    @abstractmethod
    def authenticate_session(self, session: requests.Session, url: str) -> None:
        """Authenticate the session by performing login and letting requests handle cookies automatically.

        This method should perform the authentication flow (login, etc.) using the provided
        session object. The session's cookie jar will automatically capture and store cookies
        from the authentication process.
        """

    def get_requests_wrapper(self, url: str) -> RequestsWrapper:
        """Get RequestsWrapper with cookie authentication."""
        headers = {
            'Accept': 'application/json, text/plain, */*',
        }
        return RequestsWrapper(headers=headers)

    def get_requests_session(self, url: str) -> requests.Session:
        """Return a Session with authentication performed automatically.

        The authentication process will populate the session's cookie jar,
        which requests will automatically use for subsequent requests.
        """
        session = requests.Session()
        self.authenticate_session(session, url)
        return session


class NoAuthProvider(BaseAuthProvider):
    """No authentication required."""

    def get_requests_wrapper(self, url: str) -> RequestsWrapper:
        """Get RequestsWrapper without authentication."""
        headers = {
            'Accept': 'application/json, text/plain, */*',
        }
        return RequestsWrapper(headers=headers)

    def get_requests_session(self, url: str) -> requests.Session:
        """Return a plain Session without authentication."""
        session = requests.Session()
        return session
