"""Standards loading error types."""

from pathlib import Path


class StandardsLoadingError(Exception):
    """Base exception for standards loading operations."""

    __slots__ = ("file_path", "framework")

    def __init__(self, message: str, file_path: Path | None = None, framework: str | None = None):
        """Initialize StandardsLoadingError with an error message, optional file path, and framework.

        Args:
            message (str): The error message.
            file_path (Path | None, optional): The path to the related file, if any.
            framework (str | None, optional): The name of the related framework, if any.

        """
        super().__init__(message)
        self.file_path = file_path
        self.framework = framework

    def __str__(self) -> str:
        """Return a string representation of the error, including message, framework, and file path."""
        parts: list[str] = [self.args[0]]
        if self.framework:
            parts.append(f"Framework: {self.framework}")
        if self.file_path:
            parts.append(f"File: {self.file_path}")
        return " | ".join(parts)


class MappingFileNotFoundError(StandardsLoadingError):
    """Standards mapping file could not be found."""


class MappingParsingError(StandardsLoadingError):
    """Standards mapping file could not be parsed."""


class InvalidMappingStructureError(StandardsLoadingError):
    """Standards mapping has invalid structure."""


class MappingValidationError(StandardsLoadingError):
    """Standards mapping validation failed."""


class FrameworkNotFoundError(StandardsLoadingError):
    """Required standards framework not found."""


class MappingMetadataError(StandardsLoadingError):
    """Error with standards mapping metadata."""
