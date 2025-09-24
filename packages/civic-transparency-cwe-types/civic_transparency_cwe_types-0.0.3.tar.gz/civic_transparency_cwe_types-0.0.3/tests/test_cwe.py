"""Test suite for CWE types."""

from pathlib import Path

from ci.transparency.cwe.types.cwe_error_loading import (
    CweDuplicateIdError,
    CweFileNotFoundError,
    CweInvalidIdError,
    CweLoadingError,
    CweParsingError,
    CweSchemaError,
)
from ci.transparency.cwe.types.cwe_error_validation import (
    CweCircularReferenceError,
    CweIntegrityError,
    CweMissingReferenceError,
    CweOrphanedError,
    CweRelationshipError,
    CweSchemaValidationError,
    CweValidationError,
)
from ci.transparency.cwe.types.cwe_result_loading import (
    CweLoadingResult,
    add_cwe,
    add_duplicate_id,
    add_invalid_file,
    get_loading_summary,
)
from ci.transparency.cwe.types.cwe_result_validation import (
    CweValidationResult,
    add_invalid_cwe,
    add_schema_error,
    add_validated_cwe,
    get_validation_summary,
)
from ci.transparency.cwe.types.cwe_result_validation_relationship import (
    CweRelationshipValidationResult,
    add_broken_reference,
    add_circular_reference,
    add_orphaned_cwe,
    add_validated_relationship,
    get_relationship_summary,
    update_relationship_stats,
)


class TestCWEDomain:
    """Test suite for CWE domain types and related functionality."""

    def test_cwe_loading_errors(self):
        """CWE loading error classes construct and stringify."""
        errors = [
            CweLoadingError("Base error", "CWE-123", Path("/path/file.json")),
            CweFileNotFoundError("File not found", "CWE-456"),
            CweParsingError("Parse failed", file_path=Path("/test.json")),
            CweDuplicateIdError("Duplicate", "CWE-789"),
            CweInvalidIdError("Invalid format"),
            CweSchemaError("Schema mismatch"),
        ]
        for err in errors:
            assert isinstance(err, CweLoadingError)
            s = str(err)
            assert " | " in s or s  # at least stringifies

    def test_cwe_validation_errors(self):
        """CWE validation error classes construct and subclass correctly."""
        errors = [
            CweValidationError("Base validation error"),
            CweSchemaValidationError("Schema validation failed"),
            CweRelationshipError("Relationship error"),
            CweCircularReferenceError("Circular reference"),
            CweMissingReferenceError("Missing reference"),
            CweOrphanedError("Orphaned CWE"),
            CweIntegrityError("Integrity violation"),
        ]
        for err in errors:
            assert isinstance(err, CweValidationError)

    def test_cwe_loading_result(self):
        """CweLoadingResult helpers behave immutably and compute summary."""
        result = CweLoadingResult()
        cwe_data = {"name": "Test CWE", "description": "Test"}

        r2 = add_cwe(result, "CWE-123", cwe_data)
        assert result.cwe_count == 0  # original unchanged
        assert r2.cwe_count == 1 and "CWE-123" in r2.cwes

        r3 = add_duplicate_id(r2, "CWE-123")
        r4 = add_invalid_file(r3, Path("/bad.json"))
        summary = get_loading_summary(r4)
        assert summary["total_cwes"] == 1
        assert summary["failed_to_load"] == 2  # duplicate + invalid file

    def test_cwe_validation_result(self):
        """CweValidationResult accumulates pass/fail and summarizes."""
        result = CweValidationResult()
        result = add_validated_cwe(result, "CWE-100")
        result = add_invalid_cwe(result, "CWE-200", "Invalid structure")
        result = add_schema_error(result, "schema: required missing")

        assert result.passed_count == 1
        assert result.failed_count == 1
        summary = get_validation_summary(result)
        assert "schema_errors" in summary and summary["schema_errors"] == 1

    def test_cwe_relationship_validation_result(self):
        """CweRelationshipValidationResult tracks relations and stats."""
        result = CweRelationshipValidationResult()
        result = add_validated_relationship(result, "CWE-1", "CWE-2")
        result = add_circular_reference(result, "CWE-3", "CWE-3")
        result = add_broken_reference(result, "CWE-4", "CWE-999")
        result = add_orphaned_cwe(result, "CWE-5")
        result = update_relationship_stats(result, {"total_relationships": 10, "cycles_detected": 1})

        summary = get_relationship_summary(result)
        assert isinstance(summary, dict)
        assert summary["validation_failed"] == 2
        assert summary["orphaned_cwes"] == 1
