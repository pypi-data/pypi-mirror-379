"""Base validation result types and helpers.

This module defines `BaseValidationResult`, an immutable, slotted dataclass
that tracks the number of items that passed or failed validation.  It also
provides pure functions for incrementing counts and merging results.

Key design points::

    Immutable: all helpers return a new instance; original objects are never mutated.
    Slots: low memory overhead and faster attribute access.
    Type-preserving: helpers use PEP 695 generics so subclasses keep their own type.
    Convenience: boolean properties such as has_errors and truthiness
      (if result:) make common conditions easy to check.

Typical usage::

    from ci.transparency.cwe.types.base_result import BaseResult, add_error

    class MyResult(BaseResult):
        @property
        def success_rate(self) -> float:
            return 1.0 if not self.errors else 0.0

    r = MyResult.ok()
    r = add_error(r, "missing field")
    bool(r)            # False
    issues = r.total_issues   # 1

Subclasses implement success_rate to define their own notion of success
while inheriting all immutable message-handling utilities.
"""

from collections.abc import Sequence
from dataclasses import dataclass, replace
from typing import Self

from .base_result import BaseResult


@dataclass(frozen=True, slots=True)
class BaseValidationResult(BaseResult):
    """Base for all validation operations."""

    passed_count: int = 0
    failed_count: int = 0

    @property
    def failure_rate(self) -> float:
        """Calculate validation failure rate."""
        total = self.total_processed
        return self.failed_count / total if total else 0.0

    @property
    def pass_rate(self) -> float:
        """Alias of success_rate."""
        return self.success_rate

    @property
    def success_rate(self) -> float:
        """Calculate validation success rate."""
        total = self.total_processed
        return self.passed_count / total if total else 1.0

    @property
    def total_processed(self) -> int:
        """Total number of items processed (passed and failed)."""
        return self.passed_count + self.failed_count

    @classmethod
    def from_bools(cls, outcomes: Sequence[bool]) -> Self:
        """Create a new result from boolean outcomes."""
        passed = sum(outcomes)  # fast path for bools
        failed = len(outcomes) - passed
        return cls(passed_count=passed, failed_count=failed)

    @classmethod
    def from_counts(cls, passed: int = 0, failed: int = 0) -> Self:
        """Create a new result from counts."""
        if passed < 0 or failed < 0:
            raise ValueError("Counts must be non-negative.")
        return cls(passed_count=passed, failed_count=failed)

    def __post_init__(self) -> None:
        """Validate that counts are non-negative after initialization."""
        if self.passed_count < 0 or self.failed_count < 0:
            raise ValueError("Counts must be non-negative.")


def increment_validation_passed[R: BaseValidationResult](result: R) -> R:
    """Return a copy with passed_count += 1."""
    return replace(result, passed_count=result.passed_count + 1)


def increment_validation_failed[R: BaseValidationResult](result: R) -> R:
    """Return a copy with failed_count += 1."""
    return replace(result, failed_count=result.failed_count + 1)


def add_validation_counts[R: BaseValidationResult](result: R, passed: int, failed: int) -> R:
    """Return a copy with both counts increased."""
    if passed < 0 or failed < 0:
        raise ValueError("Counts must be non-negative.")
    return replace(
        result,
        passed_count=result.passed_count + passed,
        failed_count=result.failed_count + failed,
    )


def merge_validation[R: BaseValidationResult](a: R, b: R) -> R:
    """Return `a` with counts/messages merged from `b`."""
    return replace(
        a,
        passed_count=a.passed_count + b.passed_count,
        failed_count=a.failed_count + b.failed_count,
        errors=a.errors + b.errors,
        warnings=a.warnings + b.warnings,
        infos=a.infos + b.infos,
    )
