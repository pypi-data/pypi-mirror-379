"""Standards format error types."""

from pathlib import Path


class StandardsFormatError(Exception):
    """Base exception for standards format operations."""

    __slots__ = ("format_name", "file_path")

    def __init__(self, message: str, format_name: str | None = None, file_path: Path | None = None):
        """Initialize StandardsFormatError with an error message, format name, and file path.

        Args:
            message (str): The error message.
            format_name (str | None, optional): The name of the format. Defaults to None.
            file_path (Path | None, optional): The path to the file. Defaults to None.

        """
        super().__init__(message)
        self.format_name = format_name
        self.file_path = file_path

    def __str__(self) -> str:
        """Return a string representation of the error with format and file details."""
        parts: list[str] = [self.args[0]]
        if self.format_name:
            parts.append(f"Format: {self.format_name}")
        if self.file_path:
            parts.append(f"File: {self.file_path}")
        return " | ".join(parts)


class UnsupportedFormatError(StandardsFormatError):
    """Standards mapping format is not supported."""


class FormatDetectionError(StandardsFormatError):
    """Could not detect standards mapping format."""


class FormatValidationError(StandardsFormatError):
    """Standards mapping format validation failed."""


class FormatStructureError(StandardsFormatError):
    """Standards mapping has invalid structure for format."""


class FormatCompatibilityError(StandardsFormatError):
    """Format compatibility check failed."""


class FormatNormalizationError(StandardsFormatError):
    """Error normalizing standards format."""
