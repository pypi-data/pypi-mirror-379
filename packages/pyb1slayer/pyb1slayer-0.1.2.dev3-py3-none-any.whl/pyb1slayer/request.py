from typing import Optional, Union, Dict, Any, TypeVar, Type
import httpx
from urllib.parse import urlencode, quote

T = TypeVar("T")


class SLRequest:
    """
    Fluent Builder for building and executing requests against the Service Layer.
    It is instantiated from SLConnection.request().
    """

    def __init__(self, connection: "SLConnection", resource: str, key: Optional[Union[str, int]] = None):
        self._connection = connection
        self._resource = resource
        self._key = key

        # Query options
        self._select: Optional[str] = None
        self._filter: Optional[str] = None
        self._orderby: Optional[str] = None
        self._top: Optional[int] = None
        self._skip: Optional[int] = None
        self._inlinecount: Optional[str] = None
        self._apply: Optional[str] = None

        # Custom headers per request
        self._headers: Dict[str, str] = {}

        # Special options
        self._prefer_no_content: bool = False
        self._page_size: Optional[int] = None
        self._case_insensitive: bool = False

    def select(self, fields: str) -> "SLRequest":
        """Specifies the fields to return ($select)."""
        self._select = fields
        return self

    def filter(self, condition: str) -> "SLRequest":
        """Applies an OData filter ($filter)."""
        self._filter = condition
        return self

    def orderby(self, order: str) -> "SLRequest":
        """Orders the results ($orderby)."""
        self._orderby = order
        return self

    def top(self, n: int) -> "SLRequest":
        """Limits the number of results ($top)."""
        self._top = n
        return self

    def skip(self, n: int) -> "SLRequest":
        """Skip the first n results ($skip)."""
        self._skip = n
        return self

    def inlinecount(self, mode: str = "allpages") -> "SLRequest":
        """Include the total count in the response ($inlinecount)."""
        if mode not in ("allpages", "none"):
            raise ValueError("inlinecount must be 'allpages' or 'none'")
        self._inlinecount = mode
        return self

    def apply(self, aggregation: str) -> "SLRequest":
        """Applies grouping/aggregation operations ($apply)."""
        self._apply = aggregation
        return self

    def with_page_size(self, size: int) -> "SLRequest":
        """Set the page size via header B1S-PageSize."""
        self._page_size = size
        return self

    def case_insensitive(self, enabled: bool = True) -> "SLRequest":
        """Enables case-insensitive searching via header B1S-CaseInsensitive."""
        self._case_insensitive = enabled
        return self

    def prefer_no_content(self) -> "SLRequest":
        """Indicates that no body is returned in POST responses (Location only)."""
        self._prefer_no_content = True
        return self

    def _build_query_string(self) -> str:
        """Builds the OData query string from the options."""
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
        if self._inlinecount:
            params["$inlinecount"] = self._inlinecount
        if self._apply:
            params["$apply"] = self._apply

        if not params:
            return ""
        return "?" + urlencode(params, safe="(),/:$' ")

    def _build_headers(self) -> Dict[str, str]:
        """Build headers specific to this request."""
        headers = {}

        if self._page_size is not None:
            headers["B1S-PageSize"] = str(self._page_size)
        if self._case_insensitive:
            headers["B1S-CaseInsensitive"] = "true"
        if self._prefer_no_content:
            headers["Prefer"] = "return-no-content"

        return headers

    def _build_path(self) -> str:
        """Build the resource path, with key if applicable."""
        base = self._resource

        if self._key is not None:
           # Supports string (in single quotes) or int (without quotes) keys
            if isinstance(self._key, str):
                key_part = f"('{quote(self._key)}')"
            else:
                key_part = f"({self._key})"
            return base + key_part
        return base

    async def get(self, model: Optional[Type[T]] = None) -> Union[Dict[str, Any], T, None]:
        """Executes a GET request."""
        path = self._build_path() + self._build_query_string()
        headers = self._build_headers()

        data = await self._connection._make_request("GET", path, headers=headers)

        if model and data is not None:
            # If using Pydantic
            if hasattr(model, "model_validate"):
                return model.model_validate(data)
            # Whether to use dataclass or dict-like constructor
            elif callable(model):
                return model(**data)
        return data

    async def post(self, body: Any, model: Optional[Type[T]] = None) -> Union[Dict[str, Any], T, None]:
        """Executes a POST request."""
        path = self._build_path()
        headers = self._build_headers()

        data = await self._connection._make_request("POST", path, json=body, headers=headers)

        if model and data is not None:
            if hasattr(model, "model_validate"):
                return model.model_validate(data)
            elif callable(model):
                return model(**data)
        return data

    async def patch(self, body: Any) -> None:
        """Executes a PATCH request."""
        path = self._build_path()
        headers = self._build_headers()
        await self._connection._make_request("PATCH", path, json=body, headers=headers)

    async def delete(self) -> None:
        """Executes a DELETE request."""
        path = self._build_path()
        headers = self._build_headers()
        await self._connection._make_request("DELETE", path, headers=headers)

    # Alias ​​for .NET style support (optional)
    get_async = get
    post_async = post
    patch_async = patch
    delete_async = delete