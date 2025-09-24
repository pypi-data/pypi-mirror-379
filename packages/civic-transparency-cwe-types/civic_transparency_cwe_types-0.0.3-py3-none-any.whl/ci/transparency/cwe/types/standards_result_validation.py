"""Standards validation result type."""

from dataclasses import dataclass, field, replace

from ci.transparency.cwe.types.base_result_validation import BaseValidationResult


# --- typed default factories to satisfy static checkers ---
def _new_coverage_gaps() -> dict[str, tuple[str, ...]]:
    return {}


def _new_validation_details() -> dict[str, str]:
    return {}


@dataclass(frozen=True, slots=True)
class StandardsValidationResult(BaseValidationResult):
    """Results from standards mapping validation operations."""

    validated_frameworks: tuple[str, ...] = ()
    invalid_frameworks: tuple[str, ...] = ()
    validated_codes: tuple[str, ...] = ()
    invalid_codes: tuple[str, ...] = ()
    coverage_gaps: dict[str, tuple[str, ...]] = field(default_factory=_new_coverage_gaps)
    cross_reference_errors: tuple[str, ...] = ()
    validation_details: dict[str, str] = field(default_factory=_new_validation_details)

    @property
    def framework_count(self) -> int:
        """Number of frameworks validated."""
        return len(self.validated_frameworks)

    @property
    def has_coverage_gaps(self) -> bool:
        """True if coverage gaps were found."""
        return bool(self.coverage_gaps)

    @property
    def has_cross_reference_errors(self) -> bool:
        """True if cross-reference errors were found."""
        return bool(self.cross_reference_errors)


def add_validated_framework[R: StandardsValidationResult](result: R, framework: str) -> R:
    """Return a copy with a successfully validated framework added."""
    return replace(
        result,
        validated_frameworks=result.validated_frameworks + (framework,),
        passed_count=result.passed_count + 1,
    )


def add_invalid_framework[R: StandardsValidationResult](result: R, framework: str, error: str) -> R:
    """Return a copy with an invalid framework and error details recorded."""
    new_details = {**result.validation_details, framework: error}
    return replace(
        result,
        invalid_frameworks=result.invalid_frameworks + (framework,),
        validation_details=new_details,
        failed_count=result.failed_count + 1,
    )


def add_validated_code[R: StandardsValidationResult](result: R, code: str) -> R:
    """Return a copy with a successfully validated code added."""
    return replace(result, validated_codes=result.validated_codes + (code,))


def add_invalid_code[R: StandardsValidationResult](result: R, code: str) -> R:
    """Return a copy with an invalid code added."""
    return replace(result, invalid_codes=result.invalid_codes + (code,))


def add_coverage_gap[R: StandardsValidationResult](
    result: R, framework: str, missing_codes: list[str]
) -> R:
    """Return a copy with a coverage gap for a framework recorded."""
    new_gaps = {**result.coverage_gaps, framework: tuple(missing_codes)}
    return replace(result, coverage_gaps=new_gaps)


def add_cross_reference_error[R: StandardsValidationResult](result: R, error: str) -> R:
    """Return a copy with a cross-reference error recorded."""
    return replace(result, cross_reference_errors=result.cross_reference_errors + (error,))


def get_standards_coverage_statistics(result: StandardsValidationResult) -> dict[str, int]:
    """Standards coverage statistics."""
    total_gaps = sum(len(gaps) for gaps in result.coverage_gaps.values())
    return {
        "frameworks_validated": result.framework_count,
        "validation_passed": result.passed_count,
        "validation_failed": result.failed_count,
        "valid_codes": len(result.validated_codes),
        "invalid_codes": len(result.invalid_codes),
        "coverage_gaps": total_gaps,
        "cross_reference_errors": len(result.cross_reference_errors),
        "success_rate_percent": int(round(result.success_rate * 100)),
    }


def get_validation_summary_report(result: StandardsValidationResult) -> str:
    """Human-readable validation summary."""
    stats = get_standards_coverage_statistics(result)
    return (
        f"Validated {stats['frameworks_validated']} frameworks "
        f"({stats['success_rate_percent']}% success rate) "
        f"with {stats['coverage_gaps']} coverage gaps and "
        f"{stats['cross_reference_errors']} cross-reference errors"
    )
