import os
from pathlib import Path
from typing import List, Union, Dict, Any, Optional
from .exceptions import SLRequestError


# Supported file extensions for attachments (as per Service Layer documentation, section 3.16)
SUPPORTED_EXTENSIONS = {
    "pdf", "doc", "docx", "jpg", "jpeg", "png", "txt", "xls", "ppt"
}


def _validate_extension(file_path: Union[str, Path]) -> str:
    """
    Validates that the file extension is supported by SAP Business One Service Layer.
    
    Args:
        file_path (str or Path): Path to the file.
        
    Returns:
        str: The lowercase file extension without the dot.
        
    Raises:
        SLRequestError: If the extension is not supported.
    """
    file_path = Path(file_path)
    ext = file_path.suffix.lower().lstrip(".")
    if ext not in SUPPORTED_EXTENSIONS:
        raise SLRequestError(
            f"Unsupported file extension: '{ext}'. "
            f"Allowed extensions: {sorted(SUPPORTED_EXTENSIONS)}"
        )
    return ext


def build_attachment_payload_from_path(file_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Builds a JSON payload for uploading a file as an attachment via /Attachments2.
    This method assumes the file is already present on the Service Layer server's filesystem
    (e.g., mounted via CIFS), as required by the "Attach source file from Linux" approach.

    Example usage:
        payload = build_attachment_payload_from_path("/mnt/attachments/invoice.pdf")
        # Result:
        # {
        #   "Attachments2_Lines": [
        #     {
        #       "SourcePath": "/mnt/attachments",
        #       "FileName": "invoice",
        #       "FileExtension": "pdf"
        #     }
        #   ]
        # }

    Args:
        file_path (str or Path): Absolute path to the file on the Service Layer server.

    Returns:
        dict: Valid JSON payload for POST /Attachments2.

    Raises:
        FileNotFoundError: If the file does not exist.
        SLRequestError: If the file extension is not supported.
    """
    file_path = Path(file_path).resolve()
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    ext = _validate_extension(file_path)
    source_dir = str(file_path.parent)
    file_name = file_path.stem  # without extension

    return {
        "Attachments2_Lines": [
            {
                "SourcePath": source_dir,
                "FileName": file_name,
                "FileExtension": ext,
            }
        ]
    }


def build_attachment_payload_from_paths(file_paths: List[Union[str, Path]]) -> Dict[str, Any]:
    """
    Builds a payload for uploading multiple files as a single attachment.

    Args:
        file_paths (List[str or Path]): List of absolute file paths.

    Returns:
        dict: Valid JSON payload for POST /Attachments2 with multiple lines.

    Raises:
        FileNotFoundError: If any file does not exist.
        SLRequestError: If any file has an unsupported extension.
    """
    lines = []
    for fp in file_paths:
        file_path = Path(fp).resolve()
        if not file_path.is_file():
            raise FileNotFoundError(f"File not found: {file_path}")
        ext = _validate_extension(file_path)
        lines.append({
            "SourcePath": str(file_path.parent),
            "FileName": file_path.stem,
            "FileExtension": ext,
        })
    return {"Attachments2_Lines": lines}


def build_attachment_payload_from_bytes(
    filename: str,
    content: bytes,
    *,
    temp_dir: str = "/tmp/pyb1slayer_uploads"
) -> Dict[str, Any]:
    """
    [Advanced] Saves binary content to a temporary file and builds an attachment payload.
    Useful when the file originates from memory (e.g., web upload).

    ⚠️ The temporary directory must be accessible by the Service Layer server (e.g., via CIFS mount).

    Args:
        filename (str): Full filename with extension (e.g., "report.pdf").
        content (bytes): Binary content of the file.
        temp_dir (str): Temporary directory path on the Service Layer server.

    Returns:
        dict: Valid JSON payload for /Attachments2.

    Raises:
        SLRequestError: If the extension is unsupported.
        OSError: If the file cannot be written.
    """
    path = Path(temp_dir)
    path.mkdir(parents=True, exist_ok=True)

    full_path = path / filename
    full_path.write_bytes(content)

    return build_attachment_payload_from_path(full_path)


def get_full_filename(attachment_line: Dict[str, Any]) -> str:
    """
    Reconstructs the full filename (name + extension) from an attachment line.

    Args:
        attachment_line (dict): A single line from Attachments2_Lines.

    Returns:
        str: Full filename (e.g., "invoice.pdf").
    """
    name = attachment_line.get("FileName", "")
    ext = attachment_line.get("FileExtension", "")
    if ext:
        return f"{name}.{ext}"
    return name