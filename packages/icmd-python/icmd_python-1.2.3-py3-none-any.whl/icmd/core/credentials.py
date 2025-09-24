"""Credential management for ICMD client."""

import json
import logging
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class CredentialManager:
    """Handles domain-keyed credential persistence for multiple ICMD instances."""

    def __init__(self, credential_file: str | None = None):
        """Initialize credential manager.

        Args:
            credential_file: Optional custom path to credential file.
                           Defaults to ~/.icmd.json
        """
        self.credential_file = Path(credential_file or Path.home() / ".icmd.json")

    def load_domain_credentials(self, domain: str) -> dict[str, Any]:
        """Load cached credentials for specific domain.

        Args:
            domain: Domain to load credentials for

        Returns
        -------
            Dictionary containing auth_method, refresh_token, etc.
            Empty dict if file doesn't exist or domain not found.
        """
        all_credentials = self._load_all_credentials()
        return all_credentials.get(domain, {})

    def _load_all_credentials(self) -> dict[str, dict[str, Any]]:
        """Load all domain-keyed credentials from file.

        Returns
        -------
            Dictionary with domain keys and credential values.
            Empty dict if file doesn't exist or can't be read.
        """
        if not self.credential_file.exists():
            return {}

        try:
            with open(self.credential_file) as f:
                data = json.load(f)

            # Validate domain-keyed structure
            if not isinstance(data, dict):
                logger.warning("Credential file contains invalid data structure")
                return {}

            return data

        except (json.JSONDecodeError, OSError) as e:
            logger.warning(f"Failed to load credential file: {e}")
            return {}

    def save_domain_credentials(
        self, domain: str, auth_method: str, refresh_token: str, **additional_data: Any
    ) -> None:
        """Save credentials for specific domain, preserving other domains.

        Args:
            domain: ICMD domain
            auth_method: Authentication method (SAML/PASSWORD)
            refresh_token: Refresh token for subsequent sessions
            **additional_data: Additional data to store
        """
        # Load existing credentials
        all_credentials = self._load_all_credentials()

        # Update credentials for this domain
        all_credentials[domain] = {
            "auth_method": auth_method,
            "refresh_token": refresh_token,
            "saved_at": datetime.now(UTC).isoformat(),
            **additional_data,
        }

        self._save_all_credentials(all_credentials)

    def _save_all_credentials(self, all_credentials: dict[str, dict[str, Any]]) -> None:
        """Save all domain-keyed credentials to file.

        Args:
            all_credentials: Dictionary with domain keys and credential values
        """
        try:
            # Ensure parent directory exists
            self.credential_file.parent.mkdir(parents=True, exist_ok=True)

            # Save with proper permissions (readable only by user)
            with open(self.credential_file, "w") as f:
                json.dump(all_credentials, f, indent=2)

            # Set file permissions to be readable only by user
            self.credential_file.chmod(0o600)

            logger.debug(f"Saved credentials to {self.credential_file}")

        except OSError as e:
            logger.error(f"Failed to save credentials: {e}")
            # Don't raise - failing to save credentials shouldn't break the session

    def clear_session_data(self) -> None:
        """Clear cached session data by removing the credential file."""
        try:
            if self.credential_file.exists():
                self.credential_file.unlink()
                logger.info("Cleared cached credentials")
        except OSError as e:
            logger.warning(f"Failed to clear credentials: {e}")

    def get_auth_method(self, domain: str) -> str | None:
        """Get cached authentication method for domain."""
        data = self.load_domain_credentials(domain)
        return data.get("auth_method")

    def get_refresh_token(self, domain: str) -> str | None:
        """Get cached refresh token for domain."""
        data = self.load_domain_credentials(domain)
        return data.get("refresh_token")

    def clear_refresh_token(self, domain: str) -> None:
        """Clear only the refresh token for domain, keeping other session data."""
        all_credentials = self._load_all_credentials()
        if domain in all_credentials and "refresh_token" in all_credentials[domain]:
            all_credentials[domain].pop("refresh_token")
            self._save_all_credentials(all_credentials)
            logger.debug(f"Cleared invalid refresh token for domain {domain}")

    def clear_domain_credentials(self, domain: str) -> None:
        """Clear all credentials for specific domain."""
        all_credentials = self._load_all_credentials()
        if domain in all_credentials:
            del all_credentials[domain]
            self._save_all_credentials(all_credentials)
            logger.info(f"Cleared credentials for domain {domain}")
