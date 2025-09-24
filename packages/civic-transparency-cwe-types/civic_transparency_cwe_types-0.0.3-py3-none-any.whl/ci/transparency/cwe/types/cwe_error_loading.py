"""CWE loading error types."""

from pathlib import Path


class CweLoadingError(Exception):
    """Base exception for CWE loading operations."""

    __slots__ = ("cwe_id", "file_path")

    def __init__(self, message: str, cwe_id: str | None = None, file_path: Path | None = None):
        """Initialize a CweLoadingError.

        Args:
            message (str): The error message.
            cwe_id (str | None, optional): The CWE ID associated with the error.
            file_path (Path | None, optional): The file path related to the error.

        """
        super().__init__(message)
        self.cwe_id = cwe_id
        self.file_path = file_path

    def __str__(self) -> str:
        """Return a string representation of the error, including message, CWE ID, and file path if available."""
        parts: list[str] = [self.args[0]]
        if self.cwe_id:
            parts.append(f"CWE: {self.cwe_id}")
        if self.file_path:
            parts.append(f"File: {self.file_path}")
        return " | ".join(parts)


class CweFileNotFoundError(CweLoadingError):
    """CWE file could not be found."""


class CweParsingError(CweLoadingError):
    """CWE file could not be parsed."""


class CweDuplicateIdError(CweLoadingError):
    """Duplicate CWE ID found."""


class CweInvalidIdError(CweLoadingError):
    """Invalid CWE ID format."""


class CweSchemaError(CweLoadingError):
    """CWE data does not match the expected schema."""
