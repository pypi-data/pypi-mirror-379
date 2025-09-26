"""
pyb1slayer - A clean and fluent Python client for SAP Business One Service Layer.
Created by [peddiaznicolas].
"""

__version__ = "0.1.2.dev3"

# Core classes (lo único que el usuario necesita instanciar)
from .connection import SLConnection

# Modelos útiles para tipado y respuestas
from .models import SLAttachment, SLPingResponse

# Excepciones comunes (para manejo de errores)
from .exceptions import (
    SLAuthError,
    SLRequestError,
    SLBatchError,
    SLConnectionError,
)

# API pública
__all__ = [
    "SLConnection",
    "SLAttachment",
    "SLPingResponse",
    "SLAuthError",
    "SLRequestError",
    "SLBatchError",
    "SLConnectionError",
    "__version__",
]