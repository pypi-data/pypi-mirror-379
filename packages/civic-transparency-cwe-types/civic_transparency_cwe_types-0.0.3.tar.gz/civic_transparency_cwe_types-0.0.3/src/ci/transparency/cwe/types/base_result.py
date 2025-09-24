"""Base result types and immutable helpers for transparency operations.

This module defines BaseResult, an immutable, slotted abstract class
representing the outcome of an operation. It captures three message
categories: errors, warnings, and infos, and provides helper functions
for safe, functional-style manipulation.

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
    bool(r)              # False
    issues = r.total_issues   # 1

Subclasses implement success_rate to define their own notion of success
while inheriting all immutable message-handling utilities.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, replace


@dataclass(frozen=True, slots=True)
class BaseResult(ABC):
    """Immutable base result for operations.

    Notes:
        - `total_issues` includes `errors` and `warnings`, and excludes `infos`.

    """

    errors: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()
    infos: tuple[str, ...] = ()

    @property
    def has_errors(self) -> bool:
        """True if any errors are present."""
        return bool(self.errors)

    @property
    def has_warnings(self) -> bool:
        """True if any warnings are present."""
        return bool(self.warnings)

    @property
    def has_infos(self) -> bool:
        """True if any informational messages are present."""
        return bool(self.infos)

    @property
    def success(self) -> bool:
        """True if no errors occurred."""
        return not self.has_errors

    @property
    @abstractmethod
    def success_rate(self) -> float:
        """Ratio in [0, 1] indicating operation success (defined by subclasses)."""
        raise NotImplementedError

    @property
    def error_count(self) -> int:
        """Number of errors."""
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        """Number of warnings."""
        return len(self.warnings)

    @property
    def info_count(self) -> int:
        """Number of infos."""
        return len(self.infos)

    @property
    def total_issues(self) -> int:
        """Errors + warnings."""
        return self.error_count + self.warning_count

    @property
    def total_messages(self) -> int:
        """Errors + warnings + infos."""
        return self.error_count + self.warning_count + self.info_count

    @classmethod
    def ok(cls) -> "BaseResult":
        """Return a successful result."""
        return cls()

    def __bool__(self) -> bool:
        """Truthiness reflects success (True iff no errors)."""
        return self.success


# ---- Immutable helpers (PEP 695 generics satisfy UP047) ----
def add_error[R: BaseResult](result: R, error: str) -> R:
    """Return a copy of `result` with `error` appended."""
    return replace(result, errors=result.errors + (error,))


def add_warning[R: BaseResult](result: R, warning: str) -> R:
    """Return a copy of `result` with `warning` appended."""
    return replace(result, warnings=result.warnings + (warning,))


def add_info[R: BaseResult](result: R, info: str) -> R:
    """Return a copy of `result` with `info` appended."""
    return replace(result, infos=result.infos + (info,))


def extend_errors[R: BaseResult](result: R, *errors: str) -> R:
    """Return a copy with all `errors` appended."""
    return replace(result, errors=result.errors + tuple(errors))


def extend_warnings[R: BaseResult](result: R, *warnings: str) -> R:
    """Return a copy with all `warnings` appended."""
    return replace(result, warnings=result.warnings + tuple(warnings))


def extend_infos[R: BaseResult](result: R, *infos: str) -> R:
    """Return a copy with all `infos` appended."""
    return replace(result, infos=result.infos + tuple(infos))


def merge_results[R: BaseResult](r1: R, r2: R) -> R:
    """Return `r1` with messages merged from `r2`."""
    return replace(
        r1,
        errors=r1.errors + r2.errors,
        warnings=r1.warnings + r2.warnings,
        infos=r1.infos + r2.infos,
    )


def merge_many[R: BaseResult](first: R, *rest: R) -> R:
    """Variadic merge; returns a single result of the same concrete type."""
    out = first
    for r in rest:
        out = merge_results(out, r)
    return out
