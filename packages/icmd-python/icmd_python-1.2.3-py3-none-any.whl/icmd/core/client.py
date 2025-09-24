"""ICMD client - clean, fast, intuitive."""

import contextlib
import webbrowser
from datetime import UTC, datetime, timedelta
from getpass import getpass
from http import HTTPStatus
from typing import Any

import requests
from requests.adapters import HTTPAdapter

from .credentials import CredentialManager


class ICMDAuthenticationError(Exception):
    """Raised when authentication fails."""


class ICMDConnectionError(Exception):
    """Raised when connection to ICMD fails."""


class ICMDValidationError(Exception):
    """Raised when input validation fails."""


class ICMD:
    """ICMD client - supports multiple domains per process."""

    # Configuration constants
    _DEFAULT_POOL_CONNECTIONS = 20
    _DEFAULT_POOL_MAXSIZE = 20
    _DEFAULT_MAX_RETRIES = 3
    _DEFAULT_TIMEOUT = 30
    _TOKEN_EXPIRE_BUFFER_MS = 5000
    _HTTP_NOT_FOUND = 404

    def __init__(self, domain: str, jupyterlite: bool = False, skip_auth: bool = False):
        """Initialize ICMD client with required domain parameter.

        Args:
            domain: REQUIRED domain (e.g., 'icmd.questek.com', 'cust.icmd.questek.com')
            jupyterlite: Skip auto-authentication for JupyterLite
            skip_auth: Skip auto-authentication (useful for testing or non-interactive
                environments)

        Raises
        ------
        ValueError
            If domain is not provided or invalid
        """
        if not domain:
            raise ValueError("Domain is required: ICMD('icmd.questek.com')")

        self.domain = self._validate_domain(domain)
        self._session = requests.Session()
        self._session.headers.update({"Content-Type": "application/json"})

        # Connection pooling configuration
        adapter = HTTPAdapter(
            pool_connections=self._DEFAULT_POOL_CONNECTIONS,
            pool_maxsize=self._DEFAULT_POOL_MAXSIZE,
            max_retries=self._DEFAULT_MAX_RETRIES,
            pool_block=False,
        )
        self._session.mount("http://", adapter)
        self._session.mount("https://", adapter)

        # Set reasonable timeouts by default
        self._default_timeout = self._DEFAULT_TIMEOUT

        self._credentials = CredentialManager()
        self.auth_method = self._auto_detect_auth_method()
        self.jupyterlite = jupyterlite

        self._refresh_token = ""
        self._id_token = ""
        self._id_token_expiration = datetime.now(UTC)
        self._token_expire_buffer = timedelta(milliseconds=self._TOKEN_EXPIRE_BUFFER_MS)

        # Initialize default timeout (needed for tests that bypass __init__)
        if not hasattr(self, "_default_timeout"):
            self._default_timeout = self._DEFAULT_TIMEOUT

        self._load_cached_credentials()

        if not (jupyterlite or skip_auth):
            self._ensure_authenticated()

    def _validate_domain(self, domain: str) -> str:
        """Validate domain format and return normalized domain.

        Args
        ----
            domain: Domain to validate

        Returns
        -------
            Normalized domain string

        Raises
        ------
            ValueError: If domain format is invalid
        """
        if not domain or not isinstance(domain, str):
            raise ValueError(f"Invalid domain: {domain}. Must be a non-empty string.")

        normalized = self._normalize_domain(domain)

        # Accept: icmd.questek.com or *.icmd.questek.com
        if ".questek.com" in normalized:
            return normalized

        raise ValueError(f"Invalid domain: {domain}. Must be a 'questek.com' subdomain")

    def _normalize_domain(self, domain: str) -> str:
        """Normalize domain to https:// format."""
        if not isinstance(domain, str):
            raise ICMDValidationError("Domain must be a string")

        domain = domain.strip()
        if not domain:
            raise ICMDValidationError("Domain cannot be empty")

        if not domain.startswith("http"):
            domain = f"https://{domain}"
        return domain

    def _get_server_config(self) -> dict:
        """Fetch server configuration from /api/v1/public/config/ endpoint."""
        try:
            config_url = f"{self.api_root}/public/config/"
            response = self._session.get(config_url, timeout=5)

            if response.status_code == HTTPStatus.OK:
                return response.json()
        except (requests.RequestException, ValueError, OSError, Exception):
            # Network issues, JSON parsing errors, timeouts, or any other errors
            pass

        return {}

    def _enhance_auth_error(self, error_response: requests.Response, auth_method: str) -> str:
        """Enhance authentication error messages with Cognito-specific context."""
        base_error = f"{auth_method} authentication failed"
        enhanced_error = base_error

        try:
            error_data = error_response.json()
            if not isinstance(error_data, dict):
                return enhanced_error

            # Extract error message
            error_msg = error_data.get("error") or error_data.get("message", "")

            # Map error types to enhanced messages
            error_enhancements = {
                "InvalidParameterException": "Invalid credentials or user not found",
                "UserNotFoundException": "User account not found",
                "CodeMismatchException": "Invalid authentication code",
                "ExpiredCodeException": "Authentication code has expired, please try again",
                "TooManyRequestsException": "Too many attempts, please wait before trying again",
            }

            # Check for specific error types
            for error_type, enhancement in error_enhancements.items():
                if error_type in error_msg:
                    enhanced_error = f"{base_error}: {enhancement}"
                    break
            else:
                # Handle NotAuthorizedException with method-specific messages
                if "NotAuthorizedException" in error_msg:
                    if auth_method == "PASSWORD":
                        enhanced_error = f"{base_error}: Incorrect username or password"
                    else:
                        enhanced_error = f"{base_error}: Access denied by identity provider"
                # Handle networking errors
                elif "NetworkingError" in error_msg or "timeout" in error_msg.lower():
                    enhanced_error = (
                        f"{base_error}: Network connectivity issue with identity provider"
                    )
                # Generic error message if available
                elif error_msg:
                    enhanced_error = f"{base_error}: {error_msg}"

        except (ValueError, KeyError):
            pass

        return enhanced_error

    def _auto_detect_auth_method(self) -> str:
        """Enhanced auth method detection using server config discovery."""
        if cached := self._credentials.get_auth_method(self.domain):
            return cached

        # Server config discovery for Cognito IdP detection
        config = self._get_server_config()
        if idps := config.get("identityProviders", []):
            # Prefer external IdP (Azure AD, etc.) over native Cognito password
            external_idps = [idp for idp in idps if idp != "UP"]
            if external_idps:
                return "SAML"  # External IdP available
            if "UP" in idps:
                return "PASSWORD"  # Cognito native user/password

        # Fallback: When server config is unavailable, default to PASSWORD
        # NOTE: The consent endpoint exists for both UP-only and SAML-enabled instances,
        # so we cannot reliably determine SAML availability without server config.
        # Conservative approach: assume PASSWORD when config is unavailable.
        return "PASSWORD"

    @property
    def api_root(self) -> str:
        """Return the root of the ICMD API."""
        return f"{self.domain}/api/v1"

    def _load_cached_credentials(self) -> None:
        """Load cached credentials from ~/.icmd.json."""
        if refresh_token := self._credentials.get_refresh_token(self.domain):
            self._refresh_token = refresh_token

    def _save_credentials(self) -> None:
        """Save credentials to ~/.icmd.json."""
        self._credentials.save_domain_credentials(
            self.domain, self.auth_method, self._refresh_token
        )

    def _is_token_expired(self) -> bool:
        """Check if current token is expired."""
        return self._id_token_expiration - self._token_expire_buffer <= datetime.now(UTC)

    def _ensure_authenticated(self) -> None:
        """Ensure we have a valid authentication token with smart refresh."""
        # Check if we already have a valid token
        if self._id_token and not self._is_token_expired():
            return

        # Try refresh token if available
        if self._refresh_token:
            try:
                self._refresh_access_token()
                return
            except Exception:
                # Clear invalid refresh token
                self._refresh_token = ""
                self._credentials.clear_refresh_token(self.domain)

        # Full authentication required
        self._perform_authentication()

    def authenticate(self) -> None:
        """Manually trigger authentication. Useful when ICMD was created with skip_auth=True."""
        self._ensure_authenticated()

    def _refresh_access_token(self) -> None:
        """Refresh access token using refresh token."""
        try:
            url = f"{self.api_root}/account/auth/refresh/"
            response = self._session.post(
                url, json={"refreshToken": self._refresh_token}, timeout=self._default_timeout
            )

            if response.status_code != HTTPStatus.OK:
                error_msg = "Token refresh failed"
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict) and "error" in error_data:
                        error_msg = f"Token refresh failed: {error_data['error']}"
                except (ValueError, KeyError):
                    pass
                raise ICMDAuthenticationError(error_msg)

            self._handle_auth_response(response)

        except requests.RequestException as e:
            raise ICMDConnectionError(f"Network error during token refresh: {e}") from e

    def _perform_authentication(self) -> None:
        """Perform full authentication flow."""
        if self.auth_method == "SAML":
            self._saml_authentication()
        else:
            self._password_authentication()

        self._save_credentials()

    def _password_authentication(self) -> None:
        """Authenticate with username/password."""
        try:
            username = input("Your ICMD® email: ").strip()
            if not username:
                raise ICMDValidationError("Username cannot be empty")

            password = getpass("Your ICMD® password: ")
            if not password:
                raise ICMDValidationError("Password cannot be empty")

            mfa_code = input("Your MFA Code (if enabled): ").strip()

            url = f"{self.api_root}/account/auth/login/"
            response = self._session.post(
                url,
                json={"username": username, "password": password},
                timeout=self._default_timeout,
            )

            if response.status_code != HTTPStatus.OK:
                error_msg = self._enhance_auth_error(response, "PASSWORD")
                raise ICMDAuthenticationError(error_msg)

            auth_data = response.json()
            if auth_data.get("challenge"):
                self._handle_mfa_challenge(auth_data["challenge"], username, mfa_code)
            else:
                self._handle_auth_response(response)

        except EOFError:
            raise ICMDAuthenticationError(
                "Cannot authenticate in non-interactive environment. "
                "Consider using ICMD(skip_auth=True) and calling authenticate() later."
            ) from None
        except requests.RequestException as e:
            raise ICMDConnectionError(f"Network error during password authentication: {e}") from e
        except KeyboardInterrupt:
            raise ICMDAuthenticationError("Authentication cancelled by user") from None

    def _handle_mfa_challenge(self, challenge: dict, username: str, mfa_code: str) -> None:
        """Handle MFA challenge."""
        try:
            if not mfa_code:
                mfa_code = input("Your MFA Code: ").strip()

            if not mfa_code:
                raise ICMDValidationError("MFA code cannot be empty")

            url = f"{self.api_root}/account/auth/mfa/"
            response = self._session.post(
                url,
                json={
                    "mfa_code": mfa_code,
                    "session": challenge["Session"],
                    "username": username,
                    "challenge_name": challenge.get("ChallengeName"),
                },
                timeout=self._default_timeout,
            )

            if response.status_code != HTTPStatus.OK:
                error_msg = "MFA verification failed"
                try:
                    error_data = response.json()
                    if isinstance(error_data, dict) and "error" in error_data:
                        error_msg = f"MFA failed: {error_data['error']}"
                except (ValueError, KeyError):
                    pass
                raise ICMDAuthenticationError(error_msg)

            self._handle_auth_response(response)

        except requests.RequestException as e:
            raise ICMDConnectionError(f"Network error during MFA verification: {e}") from e
        except KeyboardInterrupt:
            raise ICMDAuthenticationError("MFA verification cancelled by user") from None

    def _saml_authentication(self) -> None:
        """Authenticate with SAML SSO."""
        try:
            print("\n\033[94mSigning into ICMD® with SAML SSO...\033[0m\n")

            consent_url = f"{self.api_root}/account/auth/consent"
            print(f"Opening browser: {consent_url}")
            print("If it doesn't open, copy this URL to your browser:")
            print(f"\n{consent_url}\n")

            with contextlib.suppress(Exception):
                webbrowser.open(consent_url)

            auth_code = input("Please enter the authentication code: ").strip()
            if not auth_code:
                raise ICMDValidationError("Authentication code required")

            url = f"{self.api_root}/account/auth/login/"
            response = self._session.post(
                url,
                json={"code": auth_code, "redirect_uri": f"{self.api_root}/account/auth/exchange"},
                timeout=self._default_timeout,
            )

            if response.status_code != HTTPStatus.OK:
                error_msg = self._enhance_auth_error(response, "SAML")
                raise ICMDAuthenticationError(error_msg)

            self._handle_auth_response(response)
            print("\n\033[92mSigned in successfully.\033[0m\n")

        except requests.RequestException as e:
            raise ICMDConnectionError(f"Network error during SAML authentication: {e}") from e
        except KeyboardInterrupt:
            raise ICMDAuthenticationError("SAML authentication cancelled by user") from None

    def _handle_auth_response(self, response: requests.Response) -> None:
        """Handle authentication response and extract tokens."""
        auth_data = response.json()

        # Update session headers
        if user_context := auth_data.get("userFingerprint"):
            self._session.headers["X-User-Context"] = user_context

        # Extract tokens
        self._id_token = auth_data.get("idToken", "")
        if refresh_token := auth_data.get("refreshToken"):
            self._refresh_token = refresh_token

        # Set expiration
        if expires_at := auth_data.get("expiresAt"):
            self._id_token_expiration = datetime.fromisoformat(expires_at)

        # Set bearer auth
        if self._id_token:
            self._session.headers["Authorization"] = f"Bearer {self._id_token}"

        # Handle cookies
        for cookie in response.cookies:
            if cookie.name == "Secure-Fgp" and cookie.value:
                self._session.cookies.set("Secure-Fgp", cookie.value)

    def request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Make authenticated request to ICMD API with smart retry and error handling."""
        try:
            self._ensure_authenticated()

            # Clean and validate endpoint
            if not endpoint:
                raise ICMDValidationError("Endpoint cannot be empty")

            endpoint = endpoint.strip("/")
            url = f"{self.api_root}/{endpoint}/"

            # Set default timeout if not provided
            if "timeout" not in kwargs:
                kwargs["timeout"] = self._default_timeout

            # Make request with automatic retry on auth failure
            response = self._session.request(method, url, **kwargs)

            # Handle token expiration with single retry
            if response.status_code == HTTPStatus.UNAUTHORIZED and not kwargs.get("_retry_auth"):
                # Clear token and re-authenticate
                self._id_token = ""
                self._session.headers.pop("Authorization", None)
                self._ensure_authenticated()

                # Retry once with fresh token
                kwargs["_retry_auth"] = True
                response = self._session.request(method, url, **kwargs)

            return response

        except (ICMDAuthenticationError, ICMDConnectionError, ICMDValidationError):
            # Re-raise our custom exceptions
            raise
        except requests.RequestException as e:
            raise ICMDConnectionError(f"Request failed for {method} {endpoint}: {e}") from e
        except Exception as e:
            raise ICMDConnectionError(f"Unexpected error during request: {e}") from e

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """GET request."""
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, data: Any = None, **kwargs) -> requests.Response:
        """POST request."""
        return self.request("POST", endpoint, json=data, **kwargs)

    def put(self, endpoint: str, data: Any = None, **kwargs) -> requests.Response:
        """PUT request."""
        return self.request("PUT", endpoint, json=data, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """DELETE request."""
        return self.request("DELETE", endpoint, **kwargs)
