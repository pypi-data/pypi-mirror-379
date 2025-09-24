"""Schema freeze operation error types."""

from pathlib import Path


class SchemaFreezeError(Exception):
    """Base exception for schema freeze operations."""

    __slots__ = ("file_path", "operation")

    def __init__(self, message: str, file_path: Path | None = None, operation: str | None = None):
        """Initialize SchemaFreezeError with a message, optional file path, and operation.

        Args:
            message (str): Description of the error.
            file_path (Path | None): Path to the related file, if applicable.
            operation (str | None): Name of the operation being performed, if applicable.

        """
        super().__init__(message)
        self.file_path = file_path
        self.operation = operation

    def __str__(self) -> str:
        """Return a string representation of the schema freeze error."""
        parts: list[str] = [self.args[0]]
        if self.operation:
            parts.append(f"Operation: {self.operation}")
        if self.file_path:
            parts.append(f"File: {self.file_path}")
        return " | ".join(parts)


class SchemaHashError(SchemaFreezeError):
    """Error computing schema file hash."""


class SchemaSourceValidationError(SchemaFreezeError):
    """Schema source validation failed."""


class SchemaRepoDetectionError(SchemaFreezeError):
    """Could not detect repository root."""


class SchemaFileNotFoundError(SchemaFreezeError):
    """Schema file not found during freeze operation."""


class SchemaPermissionError(SchemaFreezeError):
    """Permission denied during schema freeze operation."""


class SchemaIntegrityError(SchemaFreezeError):
    """Schema file integrity check failed."""
