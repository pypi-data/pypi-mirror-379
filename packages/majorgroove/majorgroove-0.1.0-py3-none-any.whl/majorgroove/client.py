from __future__ import annotations

from typing import Any, Dict, List, Optional

# pyright: reportMissingTypeStubs=false
import requests


class MajorGroove:
    """
    Simple client for the MajorGroove API.

    Example:
        mg = MajorGroove(base_url="https://your-host", token="...")
        rows = mg.get_sequences(name="M13", project="SDC")
    """

    def __init__(
        self,
        host: str = "127.0.0.1",  # hostname or full URL
        port: int = 5002,
        scheme: str = "http",
        session: requests.Session | None = None,
    ):
        self.base_url = host if "://" else f"{scheme}://{host.rstrip('/')}:{port}"
        self.port = port
        self._session = session or requests.Session()

    def _headers(self) -> Dict[str, str]:
        # Token auth removed; keep method for potential future headers
        headers: Dict[str, str] = {}
        return headers

    def get_sequences(
        self,
        *,
        name: Optional[str] = None,
        project: Optional[str] = None,
        group: Optional[str] = None,
        timeout: float = 10.0,
        only_sequences=True,
        ensure_unique=False,
    ) -> List[Dict[str, Any]] | List[str]:
        """
        Fetch sequences filtered by optional name, project, group.
        Returns a list of dict rows as provided by the server.
        """
        params: Dict[str, str] = {}
        if name:
            params["name"] = name
        if project:
            params["project"] = project
        if group:
            params["group"] = group

        url = f"{self.base_url}/api/sequences"
        resp = self._session.get(
            url, headers=self._headers(), params=params, timeout=timeout
        )
        resp.raise_for_status()
        data = resp.json()
        if not isinstance(data, list):
            raise ValueError(
                "Unexpected response shape from /api/sequences; expected a JSON list"
            )

        if ensure_unique and len(data) != 1:
            raise ValueError("Expected exactly one sequence, but got %s", len(data))

        if not only_sequences:
            return data
        return [d["sequence"] for d in data]

    def get_sequence(
        self,
        *,
        name: Optional[str] = None,
        project: Optional[str] = None,
        group: Optional[str] = None,
        timeout: float = 10.0,
        only_sequence=True,
    ) -> List[Dict[str, Any]] | List[str]:
        return self.get_sequences(
            name=name,
            project=project,
            group=group,
            timeout=timeout,
            only_sequences=only_sequence,
            ensure_unique=True,
        )
