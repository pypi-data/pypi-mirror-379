import asyncio
import httpx
from typing import Optional, Dict, Any, Union, List
from urllib.parse import urljoin

from .exceptions import (
    SLAuthError,
    SLConnectionError,
    SLRequestError,
)
from .models import SLAttachment, SLPingResponse
from .request import SLRequest
from .batch import SLBatchRequest, build_batch_request


class SLConnection:
    """
    Represents a persistent connection to SAP Business One Service Layer.
    Manages session lifecycle, automatic re-authentication, retries, headers,
    and special operations like attachments, ping, batch, semantic layer, and query service.
    """

    def __init__(
        self,
        url: str,
        company_db: str,
        username: str,
        password: str,
        *,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_backoff_factor: float = 0.5,
        verify_ssl: bool = True,
    ):
        """
        Initializes a new Service Layer connection.

        Args:
            url (str): Base URL of Service Layer (e.g., "https://myb1:50000/b1s/v1/").
            company_db (str): SAP Business One company database name.
            username (str): Username for authentication.
            password (str): Password for authentication.
            extra_headers (dict, optional): Additional headers (e.g., for API Gateway).
            timeout (float): HTTP request timeout in seconds.
            max_retries (int): Maximum number of retry attempts on transient failures.
            retry_backoff_factor (float): Exponential backoff multiplier for retries.
            verify_ssl (bool): Whether to verify SSL certificates.
        """
        if not url.endswith("/"):
            url += "/"
        self._base_url = url
        self._company_db = company_db
        self._username = username
        self._password = password

        self._extra_headers = extra_headers or {}
        self._timeout = timeout
        self._max_retries = max_retries
        self._backoff_factor = retry_backoff_factor
        self._verify_ssl = verify_ssl

        # Session managed internally
        self._session_id: Optional[str] = None
        self._route_id: Optional[str] = None
        self._client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        """Async context manager entry."""
        await self.open()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()

    async def open(self):
        """Initializes the underlying HTTP client."""
        if self._client is None:
            self._client = httpx.AsyncClient(
                timeout=self._timeout,
                verify=self._verify_ssl,
                follow_redirects=True,
            )

    async def close(self):
        """Closes the HTTP client and logs out from Service Layer."""
        if self._client:
            await self.logout()
            await self._client.aclose()
            self._client = None

    def _build_headers(self) -> Dict[str, str]:
        """Builds request headers, including session cookies if available."""
        headers = {"Content-Type": "application/json"}
        headers.update(self._extra_headers)

        if self._session_id:
            headers["Cookie"] = f"B1SESSION={self._session_id}; ROUTEID={self._route_id}"
        return headers

    async def login(self):
        """
        Performs manual login to Service Layer.
        Usually not needed—login is handled automatically on first request.
        """
        if self._client is None:
            await self.open()

        login_payload = {
            "CompanyDB": self._company_db,
            "UserName": self._username,
            "Password": self._password,
        }

        try:
            response = await self._client.post(
                urljoin(self._base_url, "Login"),
                json=login_payload,
                headers={"Content-Type": "application/json"},
            )
            response.raise_for_status()

            session_id = response.json().get("SessionId")
            if not session_id:
                raise SLAuthError("Login succeeded but no SessionId returned")

            b1session = response.cookies.get("B1SESSION")
            routeid = response.cookies.get("ROUTEID")

            if not b1session:
                raise SLAuthError("Login succeeded but B1SESSION cookie missing")

            self._session_id = b1session
            self._route_id = routeid or ".node0"

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise SLAuthError(f"Authentication failed: {e.response.text}")
            raise SLConnectionError(f"Login error: {e}")

    async def logout(self):
        """Logs out and invalidates the current session."""
        if self._session_id and self._client:
            try:
                await self._client.post(
                    urljoin(self._base_url, "Logout"),
                    headers=self._build_headers(),
                )
            except Exception:
                pass  # Ignore errors during logout
            finally:
                self._session_id = None
                self._route_id = None

    async def _make_request(
        self,
        method: str,
        path: str,
        *,
        json: Any = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        raw_response: bool = False,
    ):
        """
        Executes an HTTP request with automatic session renewal and retry logic.
        """
        if self._client is None:
            await self.open()

        full_url = urljoin(self._base_url, path.lstrip("/"))
        merged_headers = {**self._build_headers(), **(headers or {})}

        for attempt in range(self._max_retries + 1):
            try:
                response = await self._client.request(
                    method=method,
                    url=full_url,
                    json=json,
                    params=params,
                    headers=merged_headers,
                )

                if response.status_code == 401 and attempt < self._max_retries:
                    await self.login()
                    merged_headers = {**self._build_headers(), **(headers or {})}
                    await asyncio.sleep(self._backoff_factor * (2 ** attempt))
                    continue

                response.raise_for_status()
                return response if raw_response else response.json()

            except httpx.HTTPStatusError as e:
                if e.response.status_code == 401 and attempt < self._max_retries:
                    await self.login()
                    merged_headers = {**self._build_headers(), **(headers or {})}
                    await asyncio.sleep(self._backoff_factor * (2 ** attempt))
                    continue
                raise SLRequestError(f"Request failed: {e.response.text}") from e
            except httpx.RequestError as e:
                if attempt < self._max_retries:
                    await asyncio.sleep(self._backoff_factor * (2 ** attempt))
                    continue
                raise SLConnectionError(f"Network error: {e}") from e

        raise SLConnectionError("Max retries exceeded")

    def request(self, resource: str, key: Optional[Union[str, int]] = None) -> SLRequest:
        """
        Starts a fluent request builder for a given resource.

        Example:
            await sl.request("BusinessPartners", "C0001").get()
        """
        return SLRequest(self, resource, key)

    # === Special Operations ===

    async def ping(self) -> SLPingResponse:
        """Pings the load balancer (available since 9.3 PL10)."""
        from .ping import ping_load_balancer
        return await ping_load_balancer(self._client, self._base_url)

    async def ping_node(self, node_id: Optional[int] = None) -> SLPingResponse:
        """Pings a specific Service Layer node."""
        from .ping import ping_node
        return await ping_node(self._client, self._base_url, node_id)

    async def post_attachment(self, file_path: str) -> SLAttachment:
        """Uploads a file as an attachment (must exist on Service Layer server filesystem)."""
        from .attachments import build_attachment_payload_from_path
        payload = build_attachment_payload_from_path(file_path)
        data = await self._make_request("POST", "Attachments2", json=payload)
        return SLAttachment.model_validate(data)

    async def get_attachment(self, attachment_entry: int, filename: Optional[str] = None) -> bytes:
        """Downloads an attachment as raw bytes."""
        url = f"Attachments2({attachment_entry})/$value"
        if filename:
            url += f"?filename='{filename}'"
        response = await self._make_request("GET", url, raw_response=True)
        return response.content

    async def post_batch(self, *requests: SLBatchRequest) -> List[httpx.Response]:
        """
        Sends multiple operations in a single batch request.
        Note: Full multipart response parsing is not yet implemented.
        """
        batch_body, boundary = build_batch_request(requests, self._base_url)
        headers = {
            "Content-Type": f"multipart/mixed; boundary={boundary}",
        }
        response = await self._make_request(
            "POST", "$batch", raw_response=True, headers=headers
        )
        return [response]

    # === Lazy-loaded modules ===

    @property
    def query_service(self) -> "QueryService":
        """Access to Query Service for row-level filtering."""
        if not hasattr(self, "_query_service"):
            from .query_service import QueryService
            self._query_service = QueryService(self)
        return self._query_service

    @property
    def semantic(self) -> "SemanticLayerClient":
        """Access to Semantic Layer (HANA views exposed as OData)."""
        if not hasattr(self, "_semantic_client"):
            from .semantic import SemanticLayerClient
            self._semantic_client = SemanticLayerClient(self)
        return self._semantic_client