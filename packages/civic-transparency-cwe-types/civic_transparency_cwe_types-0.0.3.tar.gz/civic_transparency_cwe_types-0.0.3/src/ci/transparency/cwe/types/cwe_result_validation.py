"""CWE validation result type."""

from dataclasses import dataclass, replace

from ci.transparency.cwe.types.base_result_validation import BaseValidationResult


@dataclass(frozen=True, slots=True)
class CweValidationResult(BaseValidationResult):
    """Results from CWE definition validation operations."""

    validated_cwes: tuple[str, ...] = ()
    invalid_cwes: tuple[str, ...] = ()
    schema_errors: tuple[str, ...] = ()
    integrity_errors: tuple[str, ...] = ()
    validation_details: dict[str, str] | None = None

    def __post_init__(self) -> None:
        """Ensure validation_details is a dict."""
        if self.validation_details is None:
            object.__setattr__(self, "validation_details", {})

    @property
    def has_schema_errors(self) -> bool:
        """True if schema validation errors occurred."""
        return bool(self.schema_errors)

    @property
    def has_integrity_errors(self) -> bool:
        """True if integrity errors occurred."""
        return bool(self.integrity_errors)


def add_validated_cwe[R: CweValidationResult](result: R, cwe_id: str) -> R:
    """Return a copy with a successfully validated CWE added."""
    return replace(
        result,
        validated_cwes=result.validated_cwes + (cwe_id,),
        passed_count=result.passed_count + 1,
    )


def add_invalid_cwe[R: CweValidationResult](result: R, cwe_id: str, error: str) -> R:
    """Return a copy with an invalid CWE and error details recorded."""
    details = result.validation_details or {}
    new_details = {**details, cwe_id: error}
    return replace(
        result,
        invalid_cwes=result.invalid_cwes + (cwe_id,),
        validation_details=new_details,
        failed_count=result.failed_count + 1,
    )


def add_schema_error[R: CweValidationResult](result: R, error: str) -> R:
    """Return a copy with a schema validation error recorded."""
    return replace(result, schema_errors=result.schema_errors + (error,))


def add_integrity_error[R: CweValidationResult](result: R, error: str) -> R:
    """Return a copy with an integrity validation error recorded."""
    return replace(result, integrity_errors=result.integrity_errors + (error,))


def get_validation_summary(result: CweValidationResult) -> dict[str, int | float]:
    """Summary of validation statistics."""
    return {
        "total_processed": result.total_processed,
        "validation_passed": result.passed_count,
        "validation_failed": result.failed_count,
        "schema_errors": len(result.schema_errors),
        "integrity_errors": len(result.integrity_errors),
        "success_rate_percent": round(result.success_rate * 100, 2),
    }
