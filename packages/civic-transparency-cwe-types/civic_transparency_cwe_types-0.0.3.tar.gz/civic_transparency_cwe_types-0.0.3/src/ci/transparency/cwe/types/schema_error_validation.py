"""Schema validation error types."""


class SchemaValidationError(Exception):
    """Base exception for schema validation operations."""

    __slots__ = ("schema_name", "document_path", "validation_path")

    def __init__(
        self,
        message: str,
        schema_name: str | None = None,
        document_path: str | None = None,
        validation_path: str | None = None,
    ):
        """Initialize SchemaValidationError.

        Args:
            message (str): The error message.
            schema_name (str | None): Name of the schema involved.
            document_path (str | None): Path to the document being validated.
            validation_path (str | None): Path within the schema or document where the error occurred.

        """
        super().__init__(message)
        self.schema_name = schema_name
        self.document_path = document_path
        self.validation_path = validation_path

    def __str__(self) -> str:
        """Return a string representation of the schema validation error."""
        parts: list[str] = [self.args[0]]
        if self.schema_name:
            parts.append(f"Schema: {self.schema_name}")
        if self.document_path:
            parts.append(f"Document: {self.document_path}")
        if self.validation_path:
            parts.append(f"Path: {self.validation_path}")
        return " | ".join(parts)


class SchemaUnavailableError(SchemaValidationError):
    """Required schema is not available."""


class DocumentValidationError(SchemaValidationError):
    """Document fails schema validation."""


class SchemaCompilationError(SchemaValidationError):
    """Schema could not be compiled for validation."""


class ValidationContextError(SchemaValidationError):
    """Error setting up validation context."""


class BatchValidationError(SchemaValidationError):
    """Error during batch validation operation."""


class SchemaMetaValidationError(SchemaValidationError):
    """Schema itself is invalid (meta-validation failed)."""
