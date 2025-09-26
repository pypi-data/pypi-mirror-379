from typing import Optional
from urllib.parse import urljoin
import httpx

from .models import SLPingResponse


async def ping_load_balancer(
    client: httpx.AsyncClient,
    base_url: str
) -> SLPingResponse:
    """
    Pings the Service Layer load balancer directly.
    
    This endpoint is available since SAP Business One 9.3 PL10.
    It returns a simple "pong" response directly from the Apache server,
    bypassing SAP Business One internal processing.
    
    Endpoint: GET /ping/
    
    Args:
        client (httpx.AsyncClient): The HTTP client to use.
        base_url (str): Service Layer base URL (e.g., "https://myb1:50000/b1s/v1/").
        
    Returns:
        SLPingResponse: Response with message="pong", sender="load balancer", and timestamp.
        
    Raises:
        httpx.HTTPError: If the request fails (e.g., 503 if node is down).
    """
    url = urljoin(base_url.rstrip("b1s/v1/"), "ping/")
    response = await client.get(url)
    response.raise_for_status()
    return SLPingResponse.model_validate(response.json())


async def ping_node(
    client: httpx.AsyncClient,
    base_url: str,
    node_id: Optional[int] = None
) -> SLPingResponse:
    """
    Pings a specific Service Layer node.
    
    If node_id is None, defaults to node 1.
    If the node is down or does not exist, the load balancer returns a 503 error.
    
    Endpoints:
        - /ping/node      → node 1
        - /ping/node/{n}  → node n
        
    Args:
        client (httpx.AsyncClient): The HTTP client to use.
        base_url (str): Service Layer base URL.
        node_id (int, optional): Node ID to ping. Defaults to 1 if None.
        
    Returns:
        SLPingResponse: Response from the specified node or load balancer.
        
    Raises:
        httpx.HTTPError: On network error or 503 (node unavailable).
    """
    if node_id is None:
        path = "ping/node"
    else:
        path = f"ping/node/{node_id}"
    
    url = urljoin(base_url.rstrip("b1s/v1/"), path)
    response = await client.get(url)
    response.raise_for_status()
    return SLPingResponse.model_validate(response.json())