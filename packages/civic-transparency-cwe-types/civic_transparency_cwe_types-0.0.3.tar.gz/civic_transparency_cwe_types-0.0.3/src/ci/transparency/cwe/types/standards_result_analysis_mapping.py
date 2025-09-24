"""Standards mapping analysis result type."""

from dataclasses import dataclass, field, replace
from typing import Any

from ci.transparency.cwe.types.base_result import BaseResult


# --- typed default factories to satisfy static checkers ---
def _new_mapping_structure_analysis() -> dict[str, dict[str, Any]]:
    return {}


def _new_consistency_results() -> dict[str, bool]:
    return {}


def _new_analysis_stats() -> dict[str, int]:
    return {}


@dataclass(frozen=True, slots=True)
class MappingAnalysisResult(BaseResult):
    """Results from standards mapping analysis operations."""

    frameworks_with_lists: tuple[str, ...] = ()
    frameworks_with_nonempty_lists: tuple[str, ...] = ()
    mapping_structure_analysis: dict[str, dict[str, Any]] = field(
        default_factory=_new_mapping_structure_analysis
    )
    consistency_results: dict[str, bool] = field(default_factory=_new_consistency_results)
    analysis_stats: dict[str, int] = field(default_factory=_new_analysis_stats)

    @property
    def success_rate(self) -> float:
        """Calculate analysis success rate."""
        total = self.analysis_stats.get("total_analyzed", 0)
        successful = self.analysis_stats.get("successful_analysis", 0)
        return successful / total if total > 0 else 1.0

    @property
    def framework_count(self) -> int:
        """Number of frameworks analyzed."""
        return len(self.frameworks_with_lists)

    @property
    def has_inconsistencies(self) -> bool:
        """True if mapping inconsistencies were found."""
        return any(not consistent for consistent in self.consistency_results.values())


def add_framework_with_lists[R: MappingAnalysisResult](result: R, framework: str) -> R:
    """Return a copy with a framework that has list-based mappings added."""
    return replace(result, frameworks_with_lists=result.frameworks_with_lists + (framework,))


def add_framework_with_nonempty_lists[R: MappingAnalysisResult](result: R, framework: str) -> R:
    """Return a copy with a framework that has non-empty list-based mappings added."""
    return replace(
        result,
        frameworks_with_nonempty_lists=result.frameworks_with_nonempty_lists + (framework,),
    )


def update_mapping_structure_analysis[R: MappingAnalysisResult](
    result: R, cwe_id: str, analysis: dict[str, Any]
) -> R:
    """Return a copy with mapping structure analysis updated for a CWE."""
    new_analysis = {**result.mapping_structure_analysis, cwe_id: analysis}
    return replace(result, mapping_structure_analysis=new_analysis)


def update_consistency_results[R: MappingAnalysisResult](
    result: R, cwe_id: str, is_consistent: bool
) -> R:
    """Return a copy with consistency results updated for a CWE mapping."""
    new_results = {**result.consistency_results, cwe_id: is_consistent}
    return replace(result, consistency_results=new_results)


def update_analysis_stats[R: MappingAnalysisResult](result: R, stats: dict[str, int]) -> R:
    """Return a copy with analysis statistics updated."""
    new_stats = {**result.analysis_stats, **stats}
    return replace(result, analysis_stats=new_stats)


def increment_analysis_stat[R: MappingAnalysisResult](
    result: R, stat_name: str, increment: int = 1
) -> R:
    """Return a copy with a specific analysis statistic incremented."""
    current_value = result.analysis_stats.get(stat_name, 0)
    new_stats = {**result.analysis_stats, stat_name: current_value + increment}
    return replace(result, analysis_stats=new_stats)


def get_frameworks_with_lists(result: MappingAnalysisResult) -> tuple[str, ...]:
    """Frameworks that have list-based mappings."""
    return result.frameworks_with_lists


def get_frameworks_with_nonempty_lists(result: MappingAnalysisResult) -> tuple[str, ...]:
    """Frameworks that have non-empty list-based mappings."""
    return result.frameworks_with_nonempty_lists


def get_analysis_summary(result: MappingAnalysisResult) -> dict[str, Any]:
    """Summary of mapping analysis statistics."""
    inconsistent_count = sum(
        1 for consistent in result.consistency_results.values() if not consistent
    )
    return {
        "frameworks_analyzed": result.framework_count,
        "frameworks_with_lists": len(result.frameworks_with_lists),
        "frameworks_with_nonempty_lists": len(result.frameworks_with_nonempty_lists),
        "total_consistency_checks": len(result.consistency_results),
        "inconsistent_mappings": inconsistent_count,
        "analysis_stats": dict(result.analysis_stats),
        "success_rate_percent": round(result.success_rate * 100, 2),
    }
