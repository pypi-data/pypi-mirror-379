"""Common batch loading result type."""

from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any

from ci.transparency.cwe.types.base_result import add_warning
from ci.transparency.cwe.types.base_result_loading import BaseLoadingResult


# --- typed default factories to satisfy static checkers ---
def _new_mappings() -> dict[str, dict[str, Any]]:
    return {}


def _new_file_types() -> dict[str, int]:
    return {}


@dataclass(frozen=True, slots=True)
class BatchLoadingResult(BaseLoadingResult):
    """Results from generic batch file loading operations."""

    mappings: dict[str, dict[str, Any]] = field(default_factory=_new_mappings)
    processed_files: tuple[Path, ...] = ()
    skipped_files: tuple[Path, ...] = ()
    file_types: dict[str, int] = field(default_factory=_new_file_types)

    @property
    def mapping_count(self) -> int:
        """Number of mappings successfully loaded."""
        return len(self.mappings)

    @property
    def total_files_processed(self) -> int:
        """Total number of files processed (loaded + skipped)."""
        return len(self.processed_files) + len(self.skipped_files)


def add_mapping[R: BatchLoadingResult](
    result: R, name: str, data: dict[str, Any], file_path: Path | None = None
) -> R:
    """Return a copy with a successfully loaded mapping added."""
    new_mappings = {**result.mappings, name: data}
    new_processed = result.processed_files + ((file_path,) if file_path else ())
    return replace(
        result,
        mappings=new_mappings,
        processed_files=new_processed,
        loaded_count=result.loaded_count + 1,
    )


def add_skipped_file[R: BatchLoadingResult](result: R, file_path: Path, reason: str) -> R:
    """Return a copy with a skipped file recorded and a warning appended."""
    # Preserve subclass type via generic helper composition
    result_with_warning = add_warning(result, f"Skipped {file_path}: {reason}")
    return replace(
        result_with_warning,
        skipped_files=result.skipped_files + (file_path,),
    )


def add_processed_file[R: BatchLoadingResult](result: R, file_path: Path) -> R:
    """Return a copy with a processed file recorded (success or skip)."""
    return replace(result, processed_files=result.processed_files + (file_path,))


def update_file_type_stats[R: BatchLoadingResult](result: R, file_type: str, count: int) -> R:
    """Return a copy with file type statistics updated."""
    new_types = {**result.file_types, file_type: count}
    return replace(result, file_types=new_types)


def increment_file_type[R: BatchLoadingResult](result: R, file_type: str) -> R:
    """Return a copy with the count for a specific file type incremented."""
    current_count = result.file_types.get(file_type, 0)
    new_types = {**result.file_types, file_type: current_count + 1}
    return replace(result, file_types=new_types)


def get_batch_loading_summary(result: BatchLoadingResult) -> dict[str, Any]:
    """Summary of batch loading operation statistics."""
    return {
        "total_mappings": result.mapping_count,
        "loaded_successfully": result.loaded_count,
        "failed_to_load": result.failed_count,
        "files_processed": len(result.processed_files),
        "files_skipped": len(result.skipped_files),
        "file_types": dict(result.file_types),
        "success_rate_percent": round(result.success_rate * 100, 2),
    }
