"""Base loading result types and helpers.

This module defines BaseLoadingResult, an immutable, slotted dataclass
that tracks the number of items successfully loaded or failed to load.
It also provides pure functions for incrementing counts and merging results.

Key design points::

    Immutable: all helpers return a new instance; original objects are never mutated.
    Slots: low memory overhead and faster attribute access.
    Type-preserving: helpers use PEP 695 generics so subclasses keep their own type.
    Convenience: boolean properties such as has_errors and truthiness
      (if result:) make common conditions easy to check.

Typical usage::

    from ci.transparency.cwe.types.base_loading_result import (
        BaseLoadingResult,
        increment_loaded,
    )

    r = BaseLoadingResult()
    r = increment_loaded(r)
    bool(r)               # True if no errors
    attempted = r.total_attempted
"""

from dataclasses import dataclass, replace
from typing import Self

from ci.transparency.cwe.types.base_result import BaseResult


@dataclass(frozen=True, slots=True)
class BaseLoadingResult(BaseResult):
    """Base for all loading operations."""

    loaded_count: int = 0
    failed_count: int = 0

    @property
    def success_rate(self) -> float:
        """Calculate loading success rate."""
        total = self.total_attempted
        return self.loaded_count / total if total else 1.0

    @property
    def failure_rate(self) -> float:
        """Calculate loading failure rate."""
        total = self.total_attempted
        return self.failed_count / total if total else 0.0

    @property
    def total_attempted(self) -> int:
        """Total number of items attempted to load."""
        return self.loaded_count + self.failed_count

    @classmethod
    def from_counts(cls, loaded: int = 0, failed: int = 0) -> Self:
        """Create a new result from counts."""
        if loaded < 0 or failed < 0:
            raise ValueError("Counts must be non-negative.")
        return cls(loaded_count=loaded, failed_count=failed)

    def __post_init__(self) -> None:
        """Validate that counts are non-negative after initialization."""
        if self.loaded_count < 0 or self.failed_count < 0:
            raise ValueError("Counts must be non-negative.")


def increment_loaded[R: BaseLoadingResult](result: R) -> R:
    """Return a copy with loaded_count += 1."""
    return replace(result, loaded_count=result.loaded_count + 1)


def increment_failed[R: BaseLoadingResult](result: R) -> R:
    """Return a copy with failed_count += 1."""
    return replace(result, failed_count=result.failed_count + 1)


def add_loading_counts[R: BaseLoadingResult](result: R, loaded: int, failed: int) -> R:
    """Return a copy with both counts increased."""
    if loaded < 0 or failed < 0:
        raise ValueError("Counts must be non-negative.")
    return replace(
        result,
        loaded_count=result.loaded_count + loaded,
        failed_count=result.failed_count + failed,
    )


def merge_loading[R: BaseLoadingResult](a: R, b: R) -> R:
    """Return `a` with counts/messages merged from `b`."""
    return replace(
        a,
        loaded_count=a.loaded_count + b.loaded_count,
        failed_count=a.failed_count + b.failed_count,
        errors=a.errors + b.errors,
        warnings=a.warnings + b.warnings,
        infos=a.infos + b.infos,
    )


def merge_many_loading[R: BaseLoadingResult](first: R, *rest: R) -> R:
    """Variadic merge; returns a single result of the same concrete type."""
    out = first
    for r in rest:
        out = merge_loading(out, r)
    return out
