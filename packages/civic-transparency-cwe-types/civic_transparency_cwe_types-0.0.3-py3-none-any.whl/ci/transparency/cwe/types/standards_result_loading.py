"""Standards loading result type."""

from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any

from ci.transparency.cwe.types.base_result_loading import BaseLoadingResult


# --- typed default factories to satisfy Pyright ---
def _new_mappings() -> dict[str, dict[str, Any]]:
    return {}


def _new_framework_coverage() -> dict[str, int]:
    return {}


def _new_format_distribution() -> dict[str, int]:
    return {}


@dataclass(frozen=True, slots=True)
class StandardsLoadingResult(BaseLoadingResult):
    """Results from standards mapping loading operations."""

    mappings: dict[str, dict[str, Any]] = field(default_factory=_new_mappings)
    framework_coverage: dict[str, int] = field(default_factory=_new_framework_coverage)
    format_distribution: dict[str, int] = field(default_factory=_new_format_distribution)
    loaded_files: tuple[Path, ...] = ()
    failed_files: tuple[Path, ...] = ()

    @property
    def mapping_count(self) -> int:
        """Number of mappings successfully loaded."""
        return len(self.mappings)

    @property
    def framework_count(self) -> int:
        """Number of frameworks with mappings."""
        return len(self.framework_coverage)

    @property
    def total_framework_mappings(self) -> int:
        """Total number of framework mappings across all frameworks."""
        return sum(self.framework_coverage.values())


def add_mapping[R: StandardsLoadingResult](
    result: R, mapping_name: str, mapping_data: dict[str, Any], file_path: Path
) -> R:
    """Return a copy with a successfully loaded mapping added."""
    new_mappings = {**result.mappings, mapping_name: mapping_data}
    return replace(
        result,
        mappings=new_mappings,
        loaded_files=result.loaded_files + (file_path,),
        loaded_count=result.loaded_count + 1,
    )


def add_failed_file[R: StandardsLoadingResult](result: R, file_path: Path, error: str) -> R:
    """Return a copy with a failed file load recorded."""
    new_errors = result.errors + (f"{file_path}: {error}",)
    return replace(
        result,
        errors=new_errors,
        failed_files=result.failed_files + (file_path,),
        failed_count=result.failed_count + 1,
    )


def update_framework_coverage[R: StandardsLoadingResult](
    result: R, framework: str, count: int
) -> R:
    """Return a copy with framework coverage updated."""
    new_coverage = {**result.framework_coverage, framework: count}
    return replace(result, framework_coverage=new_coverage)


def update_format_distribution[R: StandardsLoadingResult](
    result: R, format_name: str, count: int
) -> R:
    """Return a copy with format distribution updated."""
    new_distribution = {**result.format_distribution, format_name: count}
    return replace(result, format_distribution=new_distribution)


def get_mapping_statistics(result: StandardsLoadingResult) -> dict[str, Any]:
    """Return mapping loading statistics."""
    return {
        "total_mappings": result.mapping_count,
        "loaded_successfully": result.loaded_count,
        "failed_to_load": result.failed_count,
        "framework_count": result.framework_count,
        "total_framework_mappings": result.total_framework_mappings,
        "framework_coverage": dict(result.framework_coverage),
        "format_distribution": dict(result.format_distribution),
        "success_rate_percent": round(result.success_rate * 100, 2),
    }


def get_standards_loading_summary(result: StandardsLoadingResult) -> str:
    """Human-readable summary of loading results."""
    stats = get_mapping_statistics(result)
    return (
        f"Loaded {stats['total_mappings']} mappings "
        f"({stats['success_rate_percent']}% success rate) "
        f"across {stats['framework_count']} frameworks"
    )
