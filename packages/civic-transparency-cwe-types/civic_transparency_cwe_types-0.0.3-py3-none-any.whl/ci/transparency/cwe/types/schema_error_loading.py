"""Schema loading error types."""

from pathlib import Path


class SchemaLoadingError(Exception):
    """Base exception for schema loading operations."""

    __slots__ = ("schema_name", "file_path")

    def __init__(self, message: str, schema_name: str | None = None, file_path: Path | None = None):
        """Initialize SchemaLoadingError.

        Args:
            message (str): The error message.
            schema_name (str | None, optional): The name of the schema. Defaults to None.
            file_path (Path | None, optional): The path to the schema file. Defaults to None.

        """
        super().__init__(message)
        self.schema_name = schema_name
        self.file_path = file_path

    def __str__(self) -> str:
        """Return a string representation of the schema loading error."""
        parts: list[str] = [self.args[0]]
        if self.schema_name:
            parts.append(f"Schema: {self.schema_name}")
        if self.file_path:
            parts.append(f"File: {self.file_path}")
        return " | ".join(parts)


class SchemaNotFoundError(SchemaLoadingError):
    """Schema file could not be found."""


class SchemaParsingError(SchemaLoadingError):
    """Schema file could not be parsed as JSON."""


class SchemaVersionError(SchemaLoadingError):
    """Schema version not supported or invalid."""


class SchemaBundleError(SchemaLoadingError):
    """Error working with schema bundle."""


class SchemaSearchError(SchemaLoadingError):
    """Error during schema file search."""


class SchemaConfigurationError(SchemaLoadingError):
    """Schema configuration is invalid."""
