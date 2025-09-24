"""CWE validation error types."""


class CweValidationError(Exception):
    """Base exception for CWE validation operations."""

    __slots__ = ("cwe_id", "validation_type")

    def __init__(self, message: str, cwe_id: str | None = None, validation_type: str | None = None):
        """Initialize a CweValidationError.

        Args:
            message (str): The error message.
            cwe_id (str | None, optional): The CWE identifier related to the error.
            validation_type (str | None, optional): The type of validation that failed.

        """
        super().__init__(message)
        self.cwe_id = cwe_id
        self.validation_type = validation_type

    def __str__(self) -> str:
        """Return a string representation of the validation error."""
        parts: list[str] = [self.args[0]]
        if self.cwe_id:
            parts.append(f"CWE: {self.cwe_id}")
        if self.validation_type:
            parts.append(f"Validation: {self.validation_type}")
        return " | ".join(parts)


class CweSchemaValidationError(CweValidationError):
    """CWE data fails schema validation."""


class CweRelationshipError(CweValidationError):
    """CWE relationship validation error."""


class CweCircularReferenceError(CweValidationError):
    """Circular reference detected in CWE relationships."""


class CweMissingReferenceError(CweValidationError):
    """Referenced CWE does not exist."""


class CweOrphanedError(CweValidationError):
    """CWE has no parent relationships."""


class CweIntegrityError(CweValidationError):
    """CWE data integrity violation."""
