from typing import Optional, Dict, Any
import json


class QueryService:
    """
    Provides access to the Query Service endpoint for advanced row-level filtering.
    This service is available since SAP Business One 9.2 PL11.
    
    The Query Service allows complex queries that combine $crossjoin, $expand, and $filter
    across document headers and lines in a single request.
    
    Reference: Section 3.7.10 "Row-Level Filter" in the Service Layer manual.
    """

    def __init__(self, connection: "SLConnection"):
        """
        Initializes the Query Service with a reference to an active SLConnection.
        
        Args:
            connection (SLConnection): An active Service Layer connection.
        """
        self._connection = connection

    async def post_query(
        self,
        query_path: str,
        query_option: str
    ) -> Dict[str, Any]:
        """
        Executes a POST request to /QueryService_PostQuery with the given query path and options.
        
        This method is typically used for row-level filtering scenarios, such as:
          - Joining Orders and Orders/DocumentLines
          - Filtering document lines while retrieving header data
        
        Example:
            result = await sl.query_service.post_query(
                query_path="$crossjoin(Orders,Orders/DocumentLines)",
                query_option="$expand=Orders($select=DocEntry),Orders/DocumentLines($select=ItemCode)&$filter=Orders/DocEntry eq Orders/DocumentLines/DocEntry and Orders/DocumentLines/LineNum eq 0"
            )
        
        Args:
            query_path (str): The resource path (e.g., "$crossjoin(Orders,Orders/DocumentLines)").
            query_option (str): OData query options (e.g., "$filter=...", "$expand=...").
        
        Returns:
            dict: The raw JSON response from Service Layer (as a dictionary).
        
        Raises:
            SLRequestError: If the query fails (e.g., invalid syntax, unsupported operation).
        """
        payload = {
            "QueryPath": query_path,
            "QueryOption": query_option
        }

        # Use the internal _make_request method of SLConnection
        response = await self._connection._make_request(
            method="POST",
            path="QueryService_PostQuery",
            json=payload
        )

        # The response is a raw JSON string in text/plain format (per manual, p.55)
        # But Service Layer often returns it as a JSON object directly.
        # If it's a string, parse it.
        if isinstance(response, str):
            try:
                return json.loads(response)
            except json.JSONDecodeError:
                raise ValueError("QueryService returned invalid JSON response.")
        elif isinstance(response, dict):
            return response
        else:
            raise TypeError(f"Unexpected response type from QueryService: {type(response)}")