import uuid
from typing import List, Optional
from urllib.parse import urljoin

from .exceptions import SLBatchError


class SLBatchRequest:
    """
    Represents a single operation within a Service Layer batch request.
    
    Supports:
      - HTTP methods: GET, POST, PATCH, DELETE
      - Resource paths (e.g., "BusinessPartners", "Orders(123)")
      - Optional JSON body (for POST/PATCH)
      - Optional Content-ID (required for referencing in change sets)
    """

    def __init__(
        self,
        method: str,
        resource: str,
        body: Optional[dict] = None,
        content_id: Optional[str] = None
    ):
        method = method.upper()
        if method not in {"GET", "POST", "PATCH", "DELETE"}:
            raise ValueError(f"Unsupported HTTP method: {method}")
        self.method = method
        self.resource = resource
        self.body = body
        self.content_id = content_id


def _serialize_subrequest(req: SLBatchRequest, base_url: str) -> str:
    """
    Serializes a single batch sub-request into the HTTP format expected by Service Layer.
    
    Format per sub-request:
        Content-Type: application/http
        Content-Transfer-Encoding: binary
        [Content-ID: <id>]
        
        <METHOD> <full_path> HTTP/1.1
        [Content-Type: application/json]
        [body]
    """
    lines = []
    lines.append("Content-Type: application/http")
    lines.append("Content-Transfer-Encoding: binary")
    if req.content_id:
        lines.append(f"Content-ID: {req.content_id}")
    lines.append("")  # blank line before HTTP request

    full_path = urljoin(base_url.rstrip("/") + "/", req.resource.lstrip("/"))
    lines.append(f"{req.method} {full_path} HTTP/1.1")

    if req.method in {"POST", "PATCH"} and req.body is not None:
        lines.append("Content-Type: application/json")
        lines.append("")  # blank line before body
        import json
        lines.append(json.dumps(req.body))
    else:
        # GET/DELETE or no body: empty body (but still need two newlines)
        lines.append("")  # end of headers
        lines.append("")  # empty body

    return "\r\n".join(lines)


def _build_changeset(requests: List[SLBatchRequest], base_url: str, changeset_boundary: str) -> str:
    """
    Builds a change set (atomic group of non-GET operations) within a batch request.
    
    Change sets:
      - Must not contain GET requests
      - Are executed atomically (all or nothing)
      - Use a nested multipart boundary
    """
    if any(req.method == "GET" for req in requests):
        raise SLBatchError("Change sets cannot contain GET requests.")

    parts = []
    for req in requests:
        parts.append(f"--{changeset_boundary}")
        parts.append(_serialize_subrequest(req, base_url))
    parts.append(f"--{changeset_boundary}--")
    return "\r\n".join(parts)


def build_batch_request(
    requests: List[SLBatchRequest],
    base_url: str
) -> tuple[str, str]:
    """
    Builds a full multipart/mixed batch request body for Service Layer's $batch endpoint.
    
    This version treats all requests as top-level (no automatic change set grouping).
    For atomic operations, use `build_batch_with_changeset` instead.

    Args:
        requests: List of SLBatchRequest objects.
        base_url: Service Layer base URL (e.g., "https://myb1:50000/b1s/v1/").

    Returns:
        tuple[str, str]: (batch_body, batch_boundary)
    """
    batch_boundary = f"batch_{uuid.uuid4().hex}"
    parts = []

    for req in requests:
        parts.append(f"--{batch_boundary}")
        parts.append(_serialize_subrequest(req, base_url))

    parts.append(f"--{batch_boundary}--")
    body = "\r\n".join(parts)
    return body, batch_boundary


def build_batch_with_changeset(
    standalone_requests: List[SLBatchRequest],
    atomic_requests: List[SLBatchRequest],
    base_url: str
) -> tuple[str, str]:
    """
    Builds a batch request that includes both standalone requests (e.g., GET)
    and one atomic change set (e.g., POST + PATCH).

    Args:
        standalone_requests: Typically GET requests (outside change sets).
        atomic_requests: POST/PATCH/DELETE requests to be executed atomically.
        base_url: Service Layer base URL.

    Returns:
        tuple[str, str]: (batch_body, batch_boundary)
    """
    if not atomic_requests and not standalone_requests:
        raise SLBatchError("Batch request must contain at least one operation.")

    batch_boundary = f"batch_{uuid.uuid4().hex}"
    changeset_boundary = f"changeset_{uuid.uuid4().hex}"
    parts = []

    # Add standalone requests
    for req in standalone_requests:
        parts.append(f"--{batch_boundary}")
        parts.append(_serialize_subrequest(req, base_url))

    # Add change set (if any)
    if atomic_requests:
        parts.append(f"--{batch_boundary}")
        parts.append(f"Content-Type: multipart/mixed; boundary={changeset_boundary}")
        parts.append("")  # blank line before nested body
        parts.append(_build_changeset(atomic_requests, base_url, changeset_boundary))

    parts.append(f"--{batch_boundary}--")
    body = "\r\n".join(parts)
    return body, batch_boundary