from typing import List, Optional, Any, Dict, Union
from datetime import date

try:
    from pydantic import BaseModel, Field
except ImportError:
   # Fallback: minimal base class if Pydantic is not installed
    class BaseModel:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

        @classmethod
        def model_validate(cls, data: dict):
            return cls(**data)


# === 1. Login / Session ===
class SLLoginResponse(BaseModel):
    SessionId: str
    Version: Optional[str] = None
    SessionTimeout: Optional[int] = None  # in minutes


# === 2. Ping Pong API ===
class SLPingResponse(BaseModel):
    message: str = Field(..., alias="message")
    sender: str = Field(..., alias="sender")
    timestamp: str = Field(..., alias="timestamp")  # can be parsed as a float if desired

    @property
    def is_pong(self) -> bool:
        return self.message == "pong"


# === 3. Attachments ===
class SLAttachmentLine(BaseModel):
    SourcePath: Optional[str] = None
    FileName: Optional[str] = None
    FileExtension: Optional[str] = None
    AttachmentDate: Optional[date] = None
    UserID: Optional[str] = None
    Override: Optional[str] = None  # 'tYES' / 'tNO'


class SLAttachment(BaseModel):
    AbsoluteEntry: str
    Attachments2_Lines: List[SLAttachmentLine]


# === 4. Errors ===
class SLErrorDetails(BaseModel):
    code: int
    message: dict  # {"lang": "en-us", "value": "..."}

    @property
    def text(self) -> str:
        return self.message.get("value", "")


class SLErrorResponse(BaseModel):
    error: SLErrorDetails

    def raise_exception(self):
        from .exceptions import SLRequestError
        raise SLRequestError(f"[{self.error.code}] {self.error.text}")


# === 5. Queries with $inlinecount ===
class SLInlineCountResponse(BaseModel):
    odata_count: int = Field(..., alias="odata.count")
    value: List[Any]


# === 6. Individual Properties ===
class SLPropertyResponse(BaseModel):
    value: Any


class SLPropertyNullResponse(BaseModel):
    odata_null: bool = Field(..., alias="odata.null")


# === 7. Batch (basic structure for typing) ===
class SLBatchResponse(BaseModel):
    status: int
    headers: Dict[str, str]
    body: Optional[Union[Dict[str, Any], str]] = None
    error: Optional[SLErrorResponse] = None


# === 8. UDF / UDT / UDO Metadata ===
class UserFieldMD(BaseModel):
    Name: str
    Type: str  # ej: "db_Alpha", "db_Float"
    Size: Optional[int] = None
    Description: Optional[str] = None
    SubType: Optional[str] = None
    TableName: str
    FieldID: int
    EditSize: Optional[int] = None
    Mandatory: str  # "tYES" / "tNO"
    DefaultValue: Optional[str] = None
    LinkedTable: Optional[str] = None
    LinkedUDO: Optional[str] = None
    ValidValuesMD: List[Any]


class UserTableMD(BaseModel):
    TableName: str
    TableDescription: str
    TableType: str  # ej: "bott_Document", "bott_NoObject"
    Archivable: Optional[str] = None


class UserObjectMD(BaseModel):
    Code: str
    Name: str
    TableName: str
    ObjectType: str  # ej: "boud_Document"
    CanCancel: Optional[str] = None  # "tYES" / "tNO"
    CanClose: Optional[str] = None


# === 9. Semantic Layer (generic model) ===
class SemanticLayerResponse(BaseModel):
    odata_context: str = Field(..., alias="@odata.context")
    value: List[Dict[str, Any]]


# === 10. Count ===
class SLCountResponse(BaseModel):
    count: int