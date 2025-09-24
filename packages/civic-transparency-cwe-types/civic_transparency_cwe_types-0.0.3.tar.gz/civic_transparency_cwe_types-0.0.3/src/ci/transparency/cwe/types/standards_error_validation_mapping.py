"""Standards mapping validation error types."""

from pathlib import Path

from ci.transparency.cwe.types.standards_error_validation import StandardsValidationError


class MappingValidationError(StandardsValidationError):
    """Base exception for mapping validation operations."""

    __slots__ = ("mapping_file",)

    def __init__(
        self,
        message: str,
        cwe_id: str | None = None,
        framework: str | None = None,
        mapping_file: Path | None = None,
    ):
        """Initialize MappingValidationError with message, CWE ID, framework, and mapping file.

        Args:
            message (str): Error message.
            cwe_id (str | None): CWE identifier.
            framework (str | None): Framework name.
            mapping_file (Path | None): Path to the mapping file related to the error.

        """
        # Call parent with validation_type fixed as "mapping"
        super().__init__(message, cwe_id, framework, "mapping")
        self.mapping_file = mapping_file

    def __str__(self) -> str:
        """Return a string representation of the mapping validation error."""
        parts: list[str] = [super().__str__()]
        if self.mapping_file:
            parts.append(f"File: {self.mapping_file}")
        return " | ".join(parts)


class MappingStructureError(MappingValidationError):
    """Mapping structure is invalid."""


class MappingDataConsistencyError(MappingValidationError):
    """Mapping consistency check failed."""


class FrameworkNameError(MappingValidationError):
    """Framework name validation failed."""


class MappingFormatError(MappingValidationError):
    """Mapping format validation failed."""


class ListValidationError(MappingValidationError):
    """List-based mapping validation failed."""


class MappingAnalysisError(MappingValidationError):
    """Mapping analysis operation failed."""
