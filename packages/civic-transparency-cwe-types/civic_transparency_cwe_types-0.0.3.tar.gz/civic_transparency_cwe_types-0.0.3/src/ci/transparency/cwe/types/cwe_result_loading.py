"""CWE loading result type."""

from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any

from ci.transparency.cwe.types.base_result_loading import BaseLoadingResult


def _new_cwe_dict() -> dict[str, dict[str, Any]]:
    """Typed default factory for the CWE dictionary to satisfy static checkers."""
    return {}


@dataclass(frozen=True, slots=True)
class CweLoadingResult(BaseLoadingResult):
    """Results from CWE definition loading operations."""

    cwes: dict[str, dict[str, Any]] = field(default_factory=_new_cwe_dict)
    duplicate_ids: tuple[str, ...] = ()
    invalid_files: tuple[Path, ...] = ()
    skipped_files: tuple[Path, ...] = ()

    @property
    def loaded_cwe_ids(self) -> tuple[str, ...]:
        """All loaded CWE IDs."""
        return tuple(self.cwes.keys())

    @property
    def cwe_count(self) -> int:
        """Number of CWEs successfully loaded."""
        return len(self.cwes)

    @property
    def has_duplicates(self) -> bool:
        """True if duplicate CWE IDs were found."""
        return bool(self.duplicate_ids)


def add_cwe[R: CweLoadingResult](result: R, cwe_id: str, cwe_data: dict[str, Any]) -> R:
    """Return a copy with a successfully loaded CWE added."""
    new_cwes = {**result.cwes, cwe_id: cwe_data}
    return replace(result, cwes=new_cwes, loaded_count=result.loaded_count + 1)


def add_duplicate_id[R: CweLoadingResult](result: R, cwe_id: str) -> R:
    """Return a copy with a duplicate CWE ID recorded."""
    return replace(
        result,
        duplicate_ids=result.duplicate_ids + (cwe_id,),
        failed_count=result.failed_count + 1,
    )


def add_invalid_file[R: CweLoadingResult](result: R, file_path: Path) -> R:
    """Return a copy with an invalid file recorded."""
    return replace(
        result,
        invalid_files=result.invalid_files + (file_path,),
        failed_count=result.failed_count + 1,
    )


def add_skipped_file[R: CweLoadingResult](result: R, file_path: Path) -> R:
    """Return a copy with a skipped file recorded."""
    return replace(result, skipped_files=result.skipped_files + (file_path,))


def get_loading_summary(result: CweLoadingResult) -> dict[str, int | float]:
    """Summary of CWE loading statistics."""
    return {
        "total_cwes": result.cwe_count,
        "loaded_successfully": result.loaded_count,
        "failed_to_load": result.failed_count,
        "duplicate_ids": len(result.duplicate_ids),
        "invalid_files": len(result.invalid_files),
        "skipped_files": len(result.skipped_files),
        "success_rate_percent": round(result.success_rate * 100, 2),
    }
