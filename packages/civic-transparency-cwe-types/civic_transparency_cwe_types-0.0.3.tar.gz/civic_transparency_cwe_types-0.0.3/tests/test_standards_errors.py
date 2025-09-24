"""Test suite for Standards error families."""

from pathlib import Path

from ci.transparency.cwe.types.standards_error_format import (
    FormatCompatibilityError,
    FormatDetectionError,
    FormatNormalizationError,
    FormatStructureError,
    FormatValidationError,
    StandardsFormatError,
    UnsupportedFormatError,
)
from ci.transparency.cwe.types.standards_error_loading import (
    FrameworkNotFoundError,
    InvalidMappingStructureError,
    MappingFileNotFoundError,
    MappingMetadataError,
    MappingParsingError,
    MappingValidationError,
    StandardsLoadingError,
)
from ci.transparency.cwe.types.standards_error_validation_mapping import (
    MappingAnalysisError,
    MappingDataConsistencyError,
    MappingFormatError,
    MappingStructureError,
    MappingValidationError,
)
from ci.transparency.cwe.types.standards_error_validation import (
    CodeValidationError,
    CompletenessError,
    CoverageError,
    CrossReferenceError,
    FrameworkValidationError,
    MappingConsistencyError,
    StandardsValidationError,
)

class TestStandardsErrors:
    def test_format_errors(self):
        errs = [
            StandardsFormatError("format base", "json", Path("/f.json")),
            UnsupportedFormatError("unsupported"),
            FormatDetectionError("detect"),
            FormatValidationError("validate"),
            FormatStructureError("structure"),
            FormatCompatibilityError("compat"),
            FormatNormalizationError("normalize"),
        ]
        for e in errs:
            assert isinstance(e, StandardsFormatError)
            assert str(e)

    def test_validation_errors(self):
        errs = [
            StandardsValidationError("base", "CWE-1", "NIST", "framework"),
            FrameworkValidationError("framework"),
            CodeValidationError("code"),
            CrossReferenceError("xref"),
            CompletenessError("complete"),
            MappingConsistencyError("map consistency"),
            CoverageError("coverage"),
        ]
        for e in errs:
            assert isinstance(e, StandardsValidationError)

    def test_mapping_validation_errors(self):
        errs = [
            MappingValidationError("base", cwe_id="CWE-1", framework="NIST", mapping_file=Path("/m.json")),
            MappingStructureError("structure"),
            MappingDataConsistencyError("consistency"),
            MappingFormatError("format"),
            MappingAnalysisError("analysis"),
        ]
        for e in errs:
            assert isinstance(e, MappingValidationError)
            assert "mapping" in str(e).lower()




class TestStandardsLoadingErrors:
    """Test standards loading error hierarchy."""

    def test_base_standards_loading_error(self):
        """Test base StandardsLoadingError functionality."""
        # Basic error
        error = StandardsLoadingError("Basic error")
        assert str(error) == "Basic error"

        # With file path
        error_with_file = StandardsLoadingError("Error", file_path=Path("/mapping.json"))
        assert "mapping.json" in str(error_with_file)

        # With framework
        error_with_framework = StandardsLoadingError("Error", framework="NIST")
        assert "Framework: NIST" in str(error_with_framework)

        # With both
        full_error = StandardsLoadingError("Error", file_path=Path("/nist.json"), framework="NIST")
        error_str = str(full_error)
        assert "Framework: NIST" in error_str
        assert "nist.json" in error_str

    def test_standards_loading_error_subclasses(self):
        """Test all StandardsLoadingError subclasses."""
        errors = [
            MappingFileNotFoundError("File not found"),
            MappingParsingError("Parse error"),
            InvalidMappingStructureError("Invalid structure"),
            FrameworkNotFoundError("Framework missing"),
            MappingMetadataError("Metadata error"),
        ]

        for error in errors:
            assert isinstance(error, StandardsLoadingError)
            assert str(error)  # Should not raise

    def test_standards_loading_error_with_context(self):
        """Test StandardsLoadingError with file and framework context."""
        file_path = Path("/standards/nist_mappings.json")
        framework = "NIST SP 800-53"

        error = MappingFileNotFoundError(
            "Could not locate mapping file",
            file_path=file_path,
            framework=framework
        )

        error_str = str(error)
        assert "Could not locate mapping file" in error_str
        assert "Framework: NIST SP 800-53" in error_str
        assert "nist_mappings.json" in error_str
