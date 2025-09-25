"""
Secure HTTP Client
==================

Centralized HTTP client with security enforcement, policy checks, and audit logging.
All HTTP operations must go through this module.
"""

import os
import logging
from typing import Optional, Dict, Any, Tuple
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from ..policy.enforcer import PolicyEnforcer
from ..auth.auth import AuthManager

logger = logging.getLogger(__name__)

# Default timeout (connect, read) in seconds
DEFAULT_TIMEOUT: Tuple[int, int] = (5, 30)

# Restricted headers that cannot be overridden
RESTRICTED_HEADERS = {"host", "content-length", "transfer-encoding"}

# Minimum TLS version
MIN_TLS_VERSION = "TLSv1.2"


class SecureHTTPSession:
    """Secure HTTP session with policy enforcement and audit logging"""

    def __init__(
        self,
        timeout: Optional[Tuple[int, int]] = None,
        max_retries: int = 3,
        backoff_factor: float = 0.3,
    ):
        """
        Initialize secure HTTP session.

        Args:
            timeout: Tuple of (connect_timeout, read_timeout) in seconds
            max_retries: Maximum number of retries for failed requests
            backoff_factor: Backoff factor for retries
        """
        self.timeout = timeout or DEFAULT_TIMEOUT
        self.policy_enforcer = PolicyEnforcer()
        self.auth_manager = AuthManager()

        # Create session with security defaults
        self.session = requests.Session()

        # Configure retries
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"],
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        # Security defaults
        self.session.verify = True  # Always verify SSL certificates
        self.session.headers.update(
            {
                "User-Agent": "GreenLang/0.2.3 (secure-client)",
            }
        )

    def _check_egress_policy(self, url: str, method: str = "GET") -> None:
        """
        Check if egress to URL is allowed by policy.

        Args:
            url: Target URL
            method: HTTP method

        Raises:
            PolicyViolationError: If egress is not allowed
        """
        parsed = urlparse(url)

        # Check protocol
        if parsed.scheme not in ("http", "https"):
            raise ValueError(f"Unsupported protocol: {parsed.scheme}")

        # Enforce HTTPS for production
        if os.getenv("GL_ENV") == "prod" and parsed.scheme != "https":
            raise ValueError("HTTP is not allowed in production environment")

        # Check egress policy
        policy_input = {
            "action": "network.egress",
            "url": url,
            "method": method.upper(),
            "host": parsed.hostname,
            "port": parsed.port or (443 if parsed.scheme == "https" else 80),
            "path": parsed.path,
            "env": os.getenv("GL_ENV", "prod"),
        }

        result = self.policy_enforcer.evaluate("egress", policy_input)
        if not result.get("allow", False):
            reason = result.get("reason", "Egress not allowed by policy")
            logger.error(f"Egress denied: {url} - {reason}")
            raise PermissionError(f"Policy violation: {reason}")

        logger.info(f"Egress allowed: {method} {url}")

    def _audit_log(
        self,
        method: str,
        url: str,
        response: Optional[requests.Response] = None,
        error: Optional[Exception] = None,
    ) -> None:
        """
        Log HTTP operation for audit trail.

        Args:
            method: HTTP method
            url: Target URL
            response: Response object if successful
            error: Exception if failed
        """
        audit_entry = {
            "action": "http.request",
            "method": method,
            "url": url,
            "timestamp": pd.Timestamp.now().isoformat() if "pd" in globals() else None,
            "env": os.getenv("GL_ENV", "prod"),
            "run_id": os.getenv("GL_RUN_ID"),
            "pack_id": os.getenv("GL_PACK_ID"),
        }

        if response:
            audit_entry.update(
                {
                    "status_code": response.status_code,
                    "response_time_ms": response.elapsed.total_seconds() * 1000,
                    "success": True,
                }
            )

        if error:
            audit_entry.update({"error": str(error), "success": False})

        logger.info(f"HTTP Audit: {audit_entry}")

    def request(
        self,
        method: str,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Any] = None,
        data: Optional[Any] = None,
        params: Optional[Dict[str, Any]] = None,
        timeout: Optional[Tuple[int, int]] = None,
        allow_redirects: bool = False,
        **kwargs,
    ) -> requests.Response:
        """
        Make a secure HTTP request with policy enforcement.

        Args:
            method: HTTP method (GET, POST, etc.)
            url: Target URL
            headers: Optional headers
            json: JSON payload
            data: Form data or raw body
            params: Query parameters
            timeout: Override default timeout
            allow_redirects: Whether to follow redirects (default: False for security)
            **kwargs: Additional arguments (restricted)

        Returns:
            Response object

        Raises:
            PermissionError: If policy denies the request
            requests.RequestException: For HTTP errors
        """
        # Validate and clean headers
        if headers:
            headers = {
                k: v for k, v in headers.items() if k.lower() not in RESTRICTED_HEADERS
            }

        # Policy check
        self._check_egress_policy(url, method)

        # Forbid dangerous kwargs
        forbidden_kwargs = {"verify", "cert", "proxies", "stream"}
        if any(k in kwargs for k in forbidden_kwargs):
            raise ValueError(
                f"Forbidden parameters: {forbidden_kwargs & set(kwargs.keys())}"
            )

        # Make request
        response = None
        error = None
        try:
            response = self.session.request(
                method=method.upper(),
                url=url,
                headers=headers,
                json=json,
                data=data,
                params=params,
                timeout=timeout or self.timeout,
                allow_redirects=allow_redirects,
                **kwargs,
            )
            response.raise_for_status()
            return response

        except Exception as e:
            error = e
            raise

        finally:
            self._audit_log(method, url, response, error)

    def get(self, url: str, **kwargs) -> requests.Response:
        """Secure GET request"""
        return self.request("GET", url, **kwargs)

    def post(self, url: str, **kwargs) -> requests.Response:
        """Secure POST request"""
        return self.request("POST", url, **kwargs)

    def put(self, url: str, **kwargs) -> requests.Response:
        """Secure PUT request"""
        return self.request("PUT", url, **kwargs)

    def delete(self, url: str, **kwargs) -> requests.Response:
        """Secure DELETE request"""
        return self.request("DELETE", url, **kwargs)

    def head(self, url: str, **kwargs) -> requests.Response:
        """Secure HEAD request"""
        return self.request("HEAD", url, **kwargs)

    def close(self) -> None:
        """Close the session"""
        self.session.close()

    def __enter__(self):
        """Context manager entry"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()


# Convenience functions for one-off requests
def request(method: str, url: str, **kwargs) -> requests.Response:
    """
    Make a secure HTTP request.

    This is a convenience function that creates a session, makes the request,
    and closes the session. For multiple requests, use SecureHTTPSession directly.
    """
    with SecureHTTPSession() as session:
        return session.request(method, url, **kwargs)


def get(url: str, **kwargs) -> requests.Response:
    """Secure GET request"""
    return request("GET", url, **kwargs)


def post(url: str, **kwargs) -> requests.Response:
    """Secure POST request"""
    return request("POST", url, **kwargs)


def put(url: str, **kwargs) -> requests.Response:
    """Secure PUT request"""
    return request("PUT", url, **kwargs)


def delete(url: str, **kwargs) -> requests.Response:
    """Secure DELETE request"""
    return request("DELETE", url, **kwargs)


def head(url: str, **kwargs) -> requests.Response:
    """Secure HEAD request"""
    return request("HEAD", url, **kwargs)
