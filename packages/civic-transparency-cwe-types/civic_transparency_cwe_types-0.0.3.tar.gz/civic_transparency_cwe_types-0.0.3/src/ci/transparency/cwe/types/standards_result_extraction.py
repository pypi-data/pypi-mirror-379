"""Standards extraction result type."""

from dataclasses import dataclass, field, replace
from typing import Any

from ci.transparency.cwe.types.base_result import BaseResult


# --- typed default factories to satisfy static checkers ---
def _new_extracted_codes() -> dict[str, list[str]]:
    return {}


def _new_framework_types() -> dict[str, str]:
    return {}


def _new_data_formats() -> dict[str, str]:
    return {}


def _new_extraction_stats() -> dict[str, int]:
    return {}


@dataclass(frozen=True, slots=True)
class ExtractionResult(BaseResult):
    """Results from standards code extraction operations."""

    extracted_codes: dict[str, list[str]] = field(default_factory=_new_extracted_codes)
    framework_types: dict[str, str] = field(default_factory=_new_framework_types)
    data_formats: dict[str, str] = field(default_factory=_new_data_formats)
    extraction_stats: dict[str, int] = field(default_factory=_new_extraction_stats)

    @property
    def success_rate(self) -> float:
        """Calculate extraction success rate."""
        total = self.extraction_stats.get("total_attempted", 0)
        successful = self.extraction_stats.get("successful_extractions", 0)
        return successful / total if total > 0 else 1.0

    @property
    def total_codes_extracted(self) -> int:
        """Total number of codes extracted across all frameworks."""
        return sum(len(codes) for codes in self.extracted_codes.values())

    @property
    def framework_count(self) -> int:
        """Number of frameworks processed."""
        return len(self.extracted_codes)


def add_extracted_codes[R: ExtractionResult](
    result: R,
    framework: str,
    codes: list[str],
    framework_type: str | None = None,
    data_format: str | None = None,
) -> R:
    """Return a copy with extracted codes for a framework added."""
    new_codes = {**result.extracted_codes, framework: codes}
    new_types = {**result.framework_types}
    new_formats = {**result.data_formats}

    if framework_type:
        new_types[framework] = framework_type
    if data_format:
        new_formats[framework] = data_format

    return replace(
        result, extracted_codes=new_codes, framework_types=new_types, data_formats=new_formats
    )


def update_extraction_stats[R: ExtractionResult](result: R, stats: dict[str, int]) -> R:
    """Return a copy with extraction statistics updated."""
    new_stats = {**result.extraction_stats, **stats}
    return replace(result, extraction_stats=new_stats)


def increment_extraction_stat[R: ExtractionResult](
    result: R, stat_name: str, increment: int = 1
) -> R:
    """Return a copy with a specific extraction statistic incremented."""
    current_value = result.extraction_stats.get(stat_name, 0)
    new_stats = {**result.extraction_stats, stat_name: current_value + increment}
    return replace(result, extraction_stats=new_stats)


def detect_framework_type[R: ExtractionResult](result: R, framework: str, framework_type: str) -> R:
    """Return a copy with the detected framework type recorded."""
    new_types = {**result.framework_types, framework: framework_type}
    return replace(result, framework_types=new_types)


def detect_data_format[R: ExtractionResult](result: R, framework: str, data_format: str) -> R:
    """Return a copy with the detected data format recorded."""
    new_formats = {**result.data_formats, framework: data_format}
    return replace(result, data_formats=new_formats)


def get_extraction_summary(result: ExtractionResult) -> dict[str, Any]:
    """Summary of extraction operation statistics."""
    return {
        "frameworks_processed": result.framework_count,
        "total_codes_extracted": result.total_codes_extracted,
        "framework_types": dict(result.framework_types),
        "data_formats": dict(result.data_formats),
        "extraction_stats": dict(result.extraction_stats),
        "success_rate_percent": round(result.success_rate * 100, 2),
    }
