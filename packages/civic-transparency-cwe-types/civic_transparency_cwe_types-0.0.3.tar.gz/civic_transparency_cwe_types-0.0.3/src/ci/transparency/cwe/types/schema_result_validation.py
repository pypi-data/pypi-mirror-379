"""Schema validation result type."""

from dataclasses import dataclass, field, replace

from ci.transparency.cwe.types.base_result_validation import BaseValidationResult


def _new_validation_details() -> dict[str, str]:
    """Typed default factory to satisfy static checkers."""
    return {}


@dataclass(frozen=True, slots=True)
class SchemaValidationResult(BaseValidationResult):
    """Results from schema validation operations."""

    validated_documents: tuple[str, ...] = ()
    invalid_documents: tuple[str, ...] = ()
    schema_errors: tuple[str, ...] = ()
    validation_details: dict[str, str] = field(default_factory=_new_validation_details)
    schema_name: str = ""

    @property
    def document_count(self) -> int:
        """Total number of documents validated."""
        return len(self.validated_documents)

    @property
    def has_schema_errors(self) -> bool:
        """True if schema-level errors occurred."""
        return bool(self.schema_errors)


def add_validated_document[R: SchemaValidationResult](result: R, document_path: str) -> R:
    """Return a copy with a successfully validated document added."""
    return replace(
        result,
        validated_documents=result.validated_documents + (document_path,),
        passed_count=result.passed_count + 1,
    )


def add_invalid_document[R: SchemaValidationResult](result: R, document_path: str, error: str) -> R:
    """Return a copy with an invalid document and error details recorded."""
    new_details = {**result.validation_details, document_path: error}
    return replace(
        result,
        invalid_documents=result.invalid_documents + (document_path,),
        validation_details=new_details,
        failed_count=result.failed_count + 1,
    )


def add_schema_error[R: SchemaValidationResult](result: R, error: str) -> R:
    """Return a copy with a schema-level error recorded."""
    return replace(result, schema_errors=result.schema_errors + (error,))


def set_schema_name[R: SchemaValidationResult](result: R, schema_name: str) -> R:
    """Return a copy with the schema name set."""
    return replace(result, schema_name=schema_name)


def get_schema_validation_statistics(result: SchemaValidationResult) -> dict[str, int | float]:
    """Summary of schema validation statistics."""
    return {
        "total_documents": result.document_count,
        "validation_passed": result.passed_count,
        "validation_failed": result.failed_count,
        "schema_errors": len(result.schema_errors),
        "success_rate_percent": round(result.success_rate * 100, 2),
    }
