from typing import Optional, Any


class SLBaseError(Exception):
    """
    Base exception class for all pyb1slayer-related errors.
    """
    pass


class SLAuthError(SLBaseError):
    """
    Raised when authentication fails due to invalid credentials,
    incorrect company database name, or missing permissions.
    Typically corresponds to HTTP 401 or Service Layer error code -1001.
    """
    def __init__(self, message: str = "Authentication failed in SAP Business One Service Layer"):
        self.message = message
        super().__init__(self.message)


class SLSessionError(SLBaseError):
    """
    Raised when the session is invalid, expired, or missing.
    Usually occurs when B1SESSION cookie is not provided or has expired.
    Corresponds to Service Layer error code -1001 with message 'Invalid session'.
    """
    def __init__(self, message: str = "Invalid or expired session"):
        self.message = message
        super().__init__(self.message)


class SLConnectionError(SLBaseError):
    """
    Raised when a network-level error occurs (e.g., timeout, DNS failure, SSL error).
    Wraps exceptions from the underlying HTTP client (e.g., httpx.RequestError).
    """
    def __init__(self, message: str = "Failed to connect to Service Layer"):
        self.message = message
        super().__init__(self.message)


class SLRequestError(SLBaseError):
    """
    Raised when a business logic error occurs during a request.
    Examples include:
      - Duplicate key (-10)
      - Unsupported operation (-5006)
      - Validation failure
      - Missing required field
    Typically corresponds to HTTP 400, 403, 409, etc.
    """
    def __init__(
        self,
        message: str = "Service Layer request failed",
        *,
        code: Optional[int] = None,
        raw_response: Optional[Any] = None
    ):
        self.code = code
        self.raw_response = raw_response
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        if self.code is not None:
            return f"[SL-{self.code}] {self.message}"
        return self.message


class SLBatchError(SLBaseError):
    """
    Raised when an error occurs during a batch request.
    May wrap a specific SLRequestError from one of the sub-requests.
    """
    def __init__(
        self,
        message: str = "Batch request failed",
        *,
        failed_request_index: Optional[int] = None,
        sub_error: Optional[SLRequestError] = None
    ):
        self.failed_request_index = failed_request_index
        self.sub_error = sub_error
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        base = self.message
        if self.failed_request_index is not None:
            base += f" (failed at request index: {self.failed_request_index})"
        if self.sub_error:
            base += f": {self.sub_error}"
        return base


class SLUnsupportedOperationError(SLBaseError):
    """
    Raised when attempting an unsupported operation on a Service Layer entity.
    For example, DELETE on Orders (error code -5006).
    """
    def __init__(self, message: str = "The requested action is not supported for this object"):
        self.message = message
        super().__init__(self.message)