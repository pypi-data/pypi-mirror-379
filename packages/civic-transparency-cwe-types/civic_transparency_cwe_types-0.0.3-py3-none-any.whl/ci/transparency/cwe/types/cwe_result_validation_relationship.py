"""CWE relationship validation result type."""

from dataclasses import dataclass, replace

from ci.transparency.cwe.types.base_result_validation import BaseValidationResult


@dataclass(frozen=True, slots=True)
class CweRelationshipValidationResult(BaseValidationResult):
    """Results from CWE relationship validation operations."""

    validated_relationships: tuple[tuple[str, str], ...] = ()
    circular_references: tuple[tuple[str, str], ...] = ()
    broken_references: tuple[tuple[str, str], ...] = ()
    orphaned_cwes: tuple[str, ...] = ()
    relationship_stats: dict[str, int] | None = None

    def __post_init__(self) -> None:
        """Ensure relationship_stats is a dict."""
        if self.relationship_stats is None:
            object.__setattr__(self, "relationship_stats", {})

    @property
    def has_circular_refs(self) -> bool:
        """True if circular references were found."""
        return bool(self.circular_references)

    @property
    def has_broken_refs(self) -> bool:
        """True if broken references were found."""
        return bool(self.broken_references)

    @property
    def has_orphaned_cwes(self) -> bool:
        """True if orphaned CWEs were found."""
        return bool(self.orphaned_cwes)

    @property
    def total_relationships(self) -> int:
        """Total number of relationships validated."""
        return len(self.validated_relationships)


def add_validated_relationship[R: CweRelationshipValidationResult](
    result: R, parent_id: str, child_id: str
) -> R:
    """Return a copy with a successfully validated relationship added."""
    relationship = (parent_id, child_id)
    return replace(
        result,
        validated_relationships=result.validated_relationships + (relationship,),
        passed_count=result.passed_count + 1,
    )


def add_circular_reference[R: CweRelationshipValidationResult](
    result: R, cwe_id1: str, cwe_id2: str
) -> R:
    """Return a copy with a circular reference recorded."""
    circular_ref = (cwe_id1, cwe_id2)
    return replace(
        result,
        circular_references=result.circular_references + (circular_ref,),
        failed_count=result.failed_count + 1,
    )


def add_broken_reference[R: CweRelationshipValidationResult](
    result: R, parent_id: str, missing_child_id: str
) -> R:
    """Return a copy with a broken reference recorded."""
    broken_ref = (parent_id, missing_child_id)
    return replace(
        result,
        broken_references=result.broken_references + (broken_ref,),
        failed_count=result.failed_count + 1,
    )


def add_orphaned_cwe[R: CweRelationshipValidationResult](result: R, cwe_id: str) -> R:
    """Return a copy with an orphaned CWE recorded."""
    return replace(result, orphaned_cwes=result.orphaned_cwes + (cwe_id,))


def update_relationship_stats[R: CweRelationshipValidationResult](
    result: R, stats: dict[str, int]
) -> R:
    """Return a copy with relationship statistics updated."""
    base_stats = result.relationship_stats or {}
    new_stats = {**base_stats, **stats}
    return replace(result, relationship_stats=new_stats)


def get_relationship_summary(result: CweRelationshipValidationResult) -> dict[str, int | float]:
    """Summary of relationship validation statistics."""
    return {
        "total_relationships": result.total_relationships,
        "validated_successfully": result.passed_count,
        "validation_failed": result.failed_count,
        "circular_references": len(result.circular_references),
        "broken_references": len(result.broken_references),
        "orphaned_cwes": len(result.orphaned_cwes),
        "success_rate_percent": round(result.success_rate * 100, 2),
    }
