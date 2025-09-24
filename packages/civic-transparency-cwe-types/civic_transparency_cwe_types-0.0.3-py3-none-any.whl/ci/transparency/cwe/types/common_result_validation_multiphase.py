"""Common multi-phase validation result type."""

from dataclasses import dataclass, field, replace
from typing import Any

from ci.transparency.cwe.types.base_result_validation import BaseValidationResult
from ci.transparency.cwe.types.common_result_validation_phase import PhaseValidationResult


# --- typed default factory to satisfy static checkers ---
def _new_overall_stats() -> dict[str, int]:
    return {}


@dataclass(frozen=True, slots=True)
class MultiPhaseValidationResult(BaseValidationResult):
    """Results from multi-phase validation operations."""

    phase_results: tuple[PhaseValidationResult, ...] = ()
    phase_names: tuple[str, ...] = ()
    overall_stats: dict[str, int] = field(default_factory=_new_overall_stats)

    @property
    def phase_count(self) -> int:
        """Number of validation phases executed."""
        return len(self.phase_results)

    @property
    def failed_phases(self) -> tuple[str, ...]:
        """Names of phases that had failures."""
        return tuple(
            name
            for name, result in zip(self.phase_names, self.phase_results, strict=False)
            if result.has_errors
        )

    @property
    def successful_phases(self) -> tuple[str, ...]:
        """Names of phases that completed successfully."""
        return tuple(
            name
            for name, result in zip(self.phase_names, self.phase_results, strict=False)
            if not result.has_errors
        )


def add_phase_result[R: MultiPhaseValidationResult](
    result: R, phase_result: PhaseValidationResult, phase_name: str = ""
) -> R:
    """Return a copy with a phase validation result added."""
    name = phase_name or phase_result.phase_name
    return replace(
        result,
        phase_results=result.phase_results + (phase_result,),
        phase_names=result.phase_names + (name,),
        passed_count=result.passed_count + phase_result.passed_count,
        failed_count=result.failed_count + phase_result.failed_count,
        errors=result.errors + phase_result.errors,
        warnings=result.warnings + phase_result.warnings,
        infos=result.infos + phase_result.infos,
    )


def update_overall_stats[R: MultiPhaseValidationResult](result: R, stats: dict[str, int]) -> R:
    """Return a copy with overall validation statistics updated."""
    new_stats = {**result.overall_stats, **stats}
    return replace(result, overall_stats=new_stats)


def set_overall_stat[R: MultiPhaseValidationResult](result: R, key: str, value: int) -> R:
    """Return a copy with a specific overall statistic set."""
    new_stats = {**result.overall_stats, key: value}
    return replace(result, overall_stats=new_stats)


def get_phase_by_name(
    result: MultiPhaseValidationResult, phase_name: str
) -> PhaseValidationResult | None:
    """Get a specific phase result by name."""
    for name, phase_result in zip(result.phase_names, result.phase_results, strict=False):
        if name == phase_name:
            return phase_result
    return None


def get_multi_phase_summary(result: MultiPhaseValidationResult) -> dict[str, Any]:
    """Summary of multi-phase validation statistics."""
    return {
        "total_phases": result.phase_count,
        "successful_phases": len(result.successful_phases),
        "failed_phases": len(result.failed_phases),
        "overall_validated": result.passed_count,
        "overall_failed": result.failed_count,
        "overall_success_rate_percent": round(result.success_rate * 100, 2),
        "phase_names": list(result.phase_names),
        "failed_phase_names": list(result.failed_phases),
        "overall_stats": dict(result.overall_stats),
    }
