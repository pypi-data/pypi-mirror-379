"""Test suite for Standards results (loading, validation, extraction)."""

from pathlib import Path

from ci.transparency.cwe.types.standards_result_loading import (
    StandardsLoadingResult,
    add_failed_file,
    add_mapping,
    get_mapping_statistics,
    get_standards_loading_summary,
    update_format_distribution,
    update_framework_coverage,
)
from ci.transparency.cwe.types.standards_result_validation import (
    StandardsValidationResult,
    add_cross_reference_error,
    add_coverage_gap,
    add_invalid_code,
    add_invalid_framework,
    add_validated_code,
    add_validated_framework,
    get_standards_coverage_statistics,
    get_validation_summary_report,
)
from ci.transparency.cwe.types.standards_result_extraction import (
    ExtractionResult,
    add_extracted_codes,
    detect_data_format,
    detect_framework_type,
    increment_extraction_stat,
    update_extraction_stats,
    get_extraction_summary,
)
from ci.transparency.cwe.types.standards_result_analysis_mapping import (
    MappingAnalysisResult,
    add_framework_with_lists,
    add_framework_with_nonempty_lists,
    get_analysis_summary,
    get_frameworks_with_lists,
    get_frameworks_with_nonempty_lists,
    increment_analysis_stat,
    update_analysis_stats,
    update_consistency_results,
    update_mapping_structure_analysis,
)


class TestStandardsResults:
    def test_loading_result_flow(self):
        res = StandardsLoadingResult()
        res = add_mapping(res, "nist", {"CWE-1": {"x": 1}}, Path("/nist.json"))
        res = add_failed_file(res, Path("/bad.json"), "parse error")
        res = update_framework_coverage(res, "NIST", 10)
        res = update_format_distribution(res, "json", 1)

        stats = get_mapping_statistics(res)
        assert stats["total_mappings"] == 1
        assert stats["failed_to_load"] == 1
        assert "framework_coverage" in stats

        summary = get_standards_loading_summary(res)
        assert "Loaded" in summary

    def test_validation_result_flow(self):
        res = StandardsValidationResult()
        res = add_validated_framework(res, "NIST")
        res = add_validated_code(res, "NIST.AC-1")
        res = add_invalid_code(res, "NIST.BAD")
        res = add_invalid_framework(res, "ISO", "missing sections")
        res = add_coverage_gap(res, "NIST", ["AC-2", "AC-3"])
        res = add_cross_reference_error(res, "NIST.AC-1 -> ISO.1 missing")

        stats = get_standards_coverage_statistics(res)
        assert stats["frameworks_validated"] == 1
        assert stats["invalid_codes"] == 1
        assert stats["coverage_gaps"] == 2

        summary = get_validation_summary_report(res)
        assert "Validated" in summary

    def test_extraction_result_flow(self):
        res = ExtractionResult()
        res = add_extracted_codes(res, "NIST", ["AC-1", "AC-2"], framework_type="control", data_format="json")
        res = detect_framework_type(res, "ISO", "control")
        res = detect_data_format(res, "ISO", "yaml")
        res = update_extraction_stats(res, {"total_attempted": 3})
        res = increment_extraction_stat(res, "successful_extractions", 2)

        summary = get_extraction_summary(res)
        assert summary["frameworks_processed"] == 1
        assert summary["total_codes_extracted"] == 2
        assert summary["success_rate_percent"] == 66.67






class TestMappingAnalysisResult:
    """Test MappingAnalysisResult class and helper functions."""

    def test_empty_result_initialization(self):
        """Test creating an empty MappingAnalysisResult."""
        result = MappingAnalysisResult()

        assert result.success_rate == 1.0  # Default when no data
        assert result.framework_count == 0
        assert not result.has_inconsistencies
        assert result.frameworks_with_lists == ()
        assert result.frameworks_with_nonempty_lists == ()
        assert result.mapping_structure_analysis == {}
        assert result.consistency_results == {}
        assert result.analysis_stats == {}

    def test_properties_with_data(self):
        """Test properties when MappingAnalysisResult has data."""
        consistency = {"CWE-1": True, "CWE-2": False}
        stats = {"total_analyzed": 10, "successful_analysis": 8}
        frameworks = ("NIST", "ISO")

        result = MappingAnalysisResult(
            frameworks_with_lists=frameworks,
            consistency_results=consistency,
            analysis_stats=stats
        )

        assert result.framework_count == 2
        assert result.has_inconsistencies  # CWE-2 is False
        assert result.success_rate == 0.8  # 8/10

    def test_success_rate_calculation(self):
        """Test success rate calculation with different scenarios."""
        # No data - should be 1.0
        empty_result = MappingAnalysisResult()
        assert empty_result.success_rate == 1.0

        # With data
        result_with_data = MappingAnalysisResult(
            analysis_stats={"total_analyzed": 5, "successful_analysis": 3}
        )
        assert result_with_data.success_rate == 0.6

    def test_add_framework_with_lists(self):
        """Test adding a framework with lists."""
        result = MappingAnalysisResult()

        updated = add_framework_with_lists(result, "NIST")

        assert "NIST" in updated.frameworks_with_lists
        assert updated.framework_count == 1

    def test_add_framework_with_nonempty_lists(self):
        """Test adding a framework with non-empty lists."""
        result = MappingAnalysisResult()

        updated = add_framework_with_nonempty_lists(result, "ISO")

        assert "ISO" in updated.frameworks_with_nonempty_lists

    def test_update_mapping_structure_analysis(self):
        """Test updating mapping structure analysis."""
        result = MappingAnalysisResult()
        analysis_data = {"frameworks": ["NIST", "ISO"], "complexity": "high"}

        updated = update_mapping_structure_analysis(result, "CWE-123", analysis_data)

        assert updated.mapping_structure_analysis["CWE-123"] == analysis_data

    def test_update_consistency_results(self):
        """Test updating consistency results."""
        result = MappingAnalysisResult()

        # Add consistent mapping
        updated1 = update_consistency_results(result, "CWE-1", True)
        assert not updated1.has_inconsistencies

        # Add inconsistent mapping
        updated2 = update_consistency_results(updated1, "CWE-2", False)
        assert updated2.has_inconsistencies

    def test_update_analysis_stats(self):
        """Test updating analysis statistics."""
        result = MappingAnalysisResult()
        stats = {"total_analyzed": 5, "successful_analysis": 4}

        updated = update_analysis_stats(result, stats)

        assert updated.analysis_stats == stats
        assert updated.success_rate == 0.8

    def test_increment_analysis_stat(self):
        """Test incrementing specific analysis statistics."""
        result = MappingAnalysisResult(analysis_stats={"processed": 3})

        # Increment existing stat
        updated1 = increment_analysis_stat(result, "processed", 2)
        assert updated1.analysis_stats["processed"] == 5

        # Increment new stat (default increment of 1)
        updated2 = increment_analysis_stat(updated1, "new_stat")
        assert updated2.analysis_stats["new_stat"] == 1

    def test_get_frameworks_functions(self):
        """Test getter functions for frameworks."""
        frameworks_with_lists = ("NIST", "ISO")
        frameworks_with_nonempty = ("NIST",)

        result = MappingAnalysisResult(
            frameworks_with_lists=frameworks_with_lists,
            frameworks_with_nonempty_lists=frameworks_with_nonempty
        )

        assert get_frameworks_with_lists(result) == frameworks_with_lists
        assert get_frameworks_with_nonempty_lists(result) == frameworks_with_nonempty

    def test_get_analysis_summary(self):
        """Test getting analysis summary."""
        result = MappingAnalysisResult(
            frameworks_with_lists=("NIST", "ISO"),
            frameworks_with_nonempty_lists=("NIST",),
            consistency_results={"CWE-1": True, "CWE-2": False, "CWE-3": True},
            analysis_stats={"total_analyzed": 10, "successful_analysis": 8}
        )

        summary = get_analysis_summary(result)

        assert summary["frameworks_analyzed"] == 2
        assert summary["frameworks_with_lists"] == 2
        assert summary["frameworks_with_nonempty_lists"] == 1
        assert summary["total_consistency_checks"] == 3
        assert summary["inconsistent_mappings"] == 1  # CWE-2 is False
        assert summary["analysis_stats"] == {"total_analyzed": 10, "successful_analysis": 8}
        assert summary["success_rate_percent"] == 80.0

    def test_immutability(self):
        """Test that helper functions don't mutate the original result."""
        original = MappingAnalysisResult(frameworks_with_lists=("NIST",))

        # Add a framework
        updated = add_framework_with_lists(original, "ISO")

        # Original should be unchanged
        assert len(original.frameworks_with_lists) == 1
        assert "ISO" not in original.frameworks_with_lists

        # Updated should have both
        assert len(updated.frameworks_with_lists) == 2
        assert "ISO" in updated.frameworks_with_lists
