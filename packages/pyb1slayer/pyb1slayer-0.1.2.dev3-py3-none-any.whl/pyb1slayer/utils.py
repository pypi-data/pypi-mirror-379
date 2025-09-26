import re
from typing import Union, Optional
from urllib.parse import quote


def build_entity_key(key: Union[str, int, dict]) -> str:
    """
    Builds a properly formatted entity key for OData URLs.
    
    Supports:
      - Simple keys: "C0001" → "('C0001')"
      - Integer keys: 123 → "(123)"
      - Composite keys: {"P1": "2023", "P2": "N"} → "(P1='2023',P2='N')"

    Args:
        key (str, int, or dict): Entity key value.

    Returns:
        str: Formatted key string for use in OData paths.

    Raises:
        ValueError: If the key format is unsupported.
    """
    if isinstance(key, int):
        return f"({key})"
    elif isinstance(key, str):
        # Escape single quotes by doubling them (OData standard)
        safe_key = key.replace("'", "''")
        return f"('{safe_key}')"
    elif isinstance(key, dict):
        parts = []
        for k, v in key.items():
            if isinstance(v, str):
                safe_v = v.replace("'", "''")
                parts.append(f"{k}='{safe_v}'")
            elif isinstance(v, (int, float)):
                parts.append(f"{k}={v}")
            else:
                raise ValueError(f"Unsupported value type in composite key: {type(v)}")
        return f"({','.join(parts)})"
    else:
        raise ValueError(f"Unsupported key type: {type(key)}")


def safe_odata_identifier(name: str) -> str:
    """
    Ensures an identifier is safe for use in OData query strings.
    Currently a passthrough, but can be extended for escaping if needed.
    """
    # OData identifiers are generally safe if they match CSDL rules
    if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name):
        raise ValueError(f"Invalid OData identifier: {name}")
    return name


def merge_headers(base: dict, extra: Optional[dict]) -> dict:
    """
    Merges two header dictionaries, with `extra` taking precedence.
    """
    if extra is None:
        return base.copy()
    return {**base, **extra}


def is_retryable_error(status_code: int) -> bool:
    """
    Determines if an HTTP status code is retryable.
    Typically includes 401 (session expired), 429 (rate limit), and 5xx errors.
    """
    return status_code == 401 or status_code == 429 or 500 <= status_code < 600


def normalize_base_url(url: str) -> str:
    """
    Ensures the base URL ends with a single slash.
    """
    return url.rstrip("/") + "/"


def build_semantic_base_url(service_layer_url: str) -> str:
    """
    Derives the Semantic Layer base URL from the Service Layer URL.
    
    Example:
        Input:  "https://myb1:50000/b1s/v1/"
        Output: "https://myb1:50000/b1s/v1/sml.svc/"
    """
    base = normalize_base_url(service_layer_url)
    if base.endswith("/b1s/v1/"):
        return base.replace("/b1s/v1/", "/b1s/v1/sml.svc/")
    else:
        # Fallback: append sml.svc
        return base.rstrip("/") + "/sml.svc/"