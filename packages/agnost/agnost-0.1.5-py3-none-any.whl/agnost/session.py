"""
Session management for Agnost Analytics.

This module handles analytics sessions with caching and client info management.
"""

import uuid
import logging
from typing import Dict, Optional

import requests

from .adapters import SessionInfo

logger = logging.getLogger("agnost.analytics.session")


class SessionManager:
    """Manages analytics sessions with caching and client info."""

    def __init__(self, endpoint: str, org_id: str, session: requests.Session):
        self.endpoint = endpoint
        self.org_id = org_id
        self.session = session
        self._sessions: Dict[str, str] = {}
        logger.debug(f"SessionManager initialized for org: {org_id}")

    def get_or_create_session(self, session_info: Optional[SessionInfo]) -> str:
        """Get existing session or create new one."""
        if not session_info:
            logger.debug("No session info provided, using default")
            return self._sessions.get('default', '')

        session_id = self._sessions.get(session_info.session_key)
        if session_id:
            logger.debug(f"Using existing session: {session_id}")
            return session_id

        logger.debug(f"Creating new session for client: {session_info.client_name}")
        return self._create_session(session_info.session_key, session_info.client_name)

    def _create_session(self, session_key: str, client_name: str) -> str:
        """Create a new session."""
        try:
            session_id = str(uuid.uuid4())
            response = self.session.post(
                f"{self.endpoint}/api/v1/capture-session",
                headers={
                    "Content-Type": "application/json",
                    "X-Org-Id": self.org_id,
                },
                json={
                    "session_id": session_id,
                    "client_config": client_name,
                    "connection_type": "",
                    "ip": "",
                },
                timeout=10
            )
            response.raise_for_status()
            self._sessions[session_key] = session_id
            logger.info(f"New session created: {session_id} for client: {client_name}")
            return session_id
        except Exception as e:
            logger.error(f"Failed to create session: {e}")
            return ""