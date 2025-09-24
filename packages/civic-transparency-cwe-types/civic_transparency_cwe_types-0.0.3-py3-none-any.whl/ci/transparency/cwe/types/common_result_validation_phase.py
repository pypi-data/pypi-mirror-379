"""Common single phase validation result type."""

from dataclasses import dataclass, field, replace
from typing import Any

from ci.transparency.cwe.types.base_result_validation import BaseValidationResult


def _new_phase_details() -> dict[str, Any]:
    """Typed default factory to satisfy static type checkers."""
    return {}


@dataclass(frozen=True, slots=True)
class PhaseValidationResult(BaseValidationResult):
    """Results from a single validation phase."""

    phase_name: str = ""
    validation_type: str = ""
    items_processed: tuple[str, ...] = ()
    phase_details: dict[str, Any] = field(default_factory=_new_phase_details)

    @property
    def items_count(self) -> int:
        """Number of items processed in this phase."""
        return len(self.items_processed)


def set_phase_info[R: PhaseValidationResult](
    result: R, phase_name: str, validation_type: str = ""
) -> R:
    """Return a copy with phase identification information set."""
    return replace(result, phase_name=phase_name, validation_type=validation_type)


def add_processed_item[R: PhaseValidationResult](result: R, item_id: str) -> R:
    """Return a copy with an item that was processed in this phase added."""
    return replace(result, items_processed=result.items_processed + (item_id,))


def update_phase_details[R: PhaseValidationResult](result: R, details: dict[str, Any]) -> R:
    """Return a copy with phase-specific details updated."""
    new_details = {**result.phase_details, **details}
    return replace(result, phase_details=new_details)


def set_phase_detail[R: PhaseValidationResult](result: R, key: str, value: Any) -> R:
    """Return a copy with a specific phase detail set."""
    new_details = {**result.phase_details, key: value}
    return replace(result, phase_details=new_details)


def get_phase_summary(result: PhaseValidationResult) -> dict[str, Any]:
    """Summary of single-phase validation statistics."""
    return {
        "phase_name": result.phase_name,
        "validation_type": result.validation_type,
        "items_processed": result.items_count,
        "validation_passed": result.passed_count,
        "validation_failed": result.failed_count,
        "success_rate_percent": round(result.success_rate * 100, 2),
        "phase_details": dict(result.phase_details),
    }
