"""Standards validation error types."""


class StandardsValidationError(Exception):
    """Base exception for standards validation operations."""

    __slots__ = ("cwe_id", "framework", "validation_type")

    def __init__(
        self,
        message: str,
        cwe_id: str | None = None,
        framework: str | None = None,
        validation_type: str | None = None,
    ):
        """Initialize a StandardsValidationError.

        Args:
            message (str): The error message.
            cwe_id (str | None, optional): The CWE identifier.
            framework (str | None, optional): The framework name.
            validation_type (str | None, optional): The type of validation.

        """
        super().__init__(message)
        self.cwe_id = cwe_id
        self.framework = framework
        self.validation_type = validation_type

    def __str__(self) -> str:
        """Return a string representation of the validation error."""
        parts: list[str] = [self.args[0]]
        if self.cwe_id:
            parts.append(f"CWE: {self.cwe_id}")
        if self.framework:
            parts.append(f"Framework: {self.framework}")
        if self.validation_type:
            parts.append(f"Validation: {self.validation_type}")
        return " | ".join(parts)


class FrameworkValidationError(StandardsValidationError):
    """Standards framework validation error."""


class CodeValidationError(StandardsValidationError):
    """Standards code format validation error."""


class CrossReferenceError(StandardsValidationError):
    """Standards cross-reference validation error."""


class CompletenessError(StandardsValidationError):
    """Standards completeness check failed."""


class MappingConsistencyError(StandardsValidationError):
    """Standards mapping consistency error."""


class CoverageError(StandardsValidationError):
    """Standards coverage validation error."""
