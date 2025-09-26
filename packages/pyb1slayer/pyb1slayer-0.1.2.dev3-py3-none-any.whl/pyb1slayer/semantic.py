from typing import Optional, Dict, Any, TypeVar, Type
from urllib.parse import urljoin

T = TypeVar("T")


class SemanticLayerClient:
    """
    Client for interacting with the SAP Business One Semantic Layer (HANA views exposed as OData).
    The Semantic Layer service root is: /b1s/v1/sml.svc/
    It supports OData v4 and requires proper authorization in SAP Business One.
    """

    def __init__(self, connection: "SLConnection"):
        """
        Initializes the Semantic Layer client with a reference to an active SLConnection.

        Args:
            connection (SLConnection): An active Service Layer connection.
        """
        self._connection = connection
        # Build semantic layer base URL from the main Service Layer URL
        base = self._connection._base_url.rstrip("/")
        if base.endswith("/b1s/v1"):
            self._semantic_base_url = base.replace("/b1s/v1", "/b1s/v1/sml.svc/")
        else:
            # Fallback: append sml.svc to base
            self._semantic_base_url = urljoin(base, "sml.svc/")

    def _build_headers(self) -> Dict[str, str]:
        """Reuses session headers from the parent connection."""
        return self._connection._build_headers()

    async def query(
        self,
        view_name: str,
        key: Optional[str] = None
    ) -> "SemanticLayerRequest":
        """
        Starts a fluent request builder for a Semantic Layer view.

        Example:
            result = await sl.semantic.query("AveragePurchasingPriceQuery") \\
                .select("PostingYear,BusinessPartnerCode") \\
                .filter("PostingYear eq '2023'") \\
                .get()

        Args:
            view_name (str): Name of the exposed HANA view (e.g., "AveragePurchasingPriceQuery").
            key (str, optional): Entity key (e.g., "1" or composite key like "P_FinancialPeriod='2023',P_AddVoucher='N'").

        Returns:
            SemanticLayerRequest: Fluent builder for the query.
        """
        return SemanticLayerRequest(self, view_name, key)


class SemanticLayerRequest:
    """
    Fluent builder for Semantic Layer view queries.
    Mirrors the OData query syntax supported by Service Layer.
    """

    def __init__(self, client: SemanticLayerClient, view_name: str, key: Optional[str] = None):
        self._client = client
        self._view_name = view_name
        self._key = key

        # Query options
        self._select: Optional[str] = None
        self._filter: Optional[str] = None
        self._orderby: Optional[str] = None
        self._top: Optional[int] = None
        self._skip: Optional[int] = None
        self._apply: Optional[str] = None

    def select(self, fields: str) -> "SemanticLayerRequest":
        """Specifies the fields to return ($select)."""
        self._select = fields
        return self

    def filter(self, condition: str) -> "SemanticLayerRequest":
        """Applies an OData filter ($filter)."""
        self._filter = condition
        return self

    def orderby(self, order: str) -> "SemanticLayerRequest":
        """Orders the results ($orderby)."""
        self._orderby = order
        return self

    def top(self, n: int) -> "SemanticLayerRequest":
        """Limits the number of results ($top)."""
        self._top = n
        return self

    def skip(self, n: int) -> "SemanticLayerRequest":
        """Skips the first n results ($skip)."""
        self._skip = n
        return self

    def apply(self, aggregation: str) -> "SemanticLayerRequest":
        """Applies aggregation or grouping ($apply)."""
        self._apply = aggregation
        return self

    def _build_query_string(self) -> str:
        """Builds the OData query string."""
        from urllib.parse import urlencode

        params = {}
        if self._select:
            params["$select"] = self._select
        if self._filter:
            params["$filter"] = self._filter
        if self._orderby:
            params["$orderby"] = self._orderby
        if self._top is not None:
            params["$top"] = str(self._top)
        if self._skip is not None:
            params["$skip"] = str(self._skip)
        if self._apply:
            params["$apply"] = self._apply

        if not params:
            return ""
        return "?" + urlencode(params, safe="(),/:$' ")

    def _build_path(self) -> str:
        """Builds the full resource path for the Semantic Layer view."""
        base = self._view_name
        if self._key is not None:
            # Support both simple keys ("1") and composite keys ("P1='a',P2='b'")
            if "," in self._key or "=" in self._key:
                # Composite key: wrap in parentheses
                key_part = f"({self._key})"
            else:
                # Simple key: quote if string-like
                try:
                    int(self._key)
                    key_part = f"({self._key})"
                except ValueError:
                    key_part = f"('{self._key}')"
            return base + key_part
        return base

    async def get(self, model: Optional[Type[T]] = None) -> Any:
        """
        Executes a GET request against the Semantic Layer view.

        Args:
            model (Type[T], optional): Pydantic or dataclass model for response parsing.

        Returns:
            dict, list, or model instance: Parsed response from Semantic Layer.
        """
        from urllib.parse import urljoin

        path = self._build_path() + self._build_query_string()
        full_url = urljoin(self._client._semantic_base_url, path)

        # Reuse the connection's HTTP client and retry logic
        response = await self._client._connection._client.get(
            full_url,
            headers=self._client._build_headers()
        )
        response.raise_for_status()
        data = response.json()

        if model and data is not None:
            if hasattr(model, "model_validate"):
                return model.model_validate(data)
            elif callable(model):
                return model(**data)
        return data