"""Test suite for Schema errors and results."""

from pathlib import Path
from typing import Any


from ci.transparency.cwe.types.schema_error_freeze import (
    SchemaFileNotFoundError,
    SchemaFreezeError,
    SchemaHashError,
    SchemaIntegrityError,
    SchemaPermissionError,
    SchemaRepoDetectionError,
    SchemaSourceValidationError,
)
from ci.transparency.cwe.types.schema_error_validation import (
    BatchValidationError,
    DocumentValidationError,
    SchemaCompilationError,
    SchemaMetaValidationError,
    SchemaUnavailableError,
    SchemaValidationError,
    ValidationContextError,
)
from ci.transparency.cwe.types.schema_result_validation import (
    SchemaValidationResult,
    add_invalid_document,
    add_schema_error,
    add_validated_document,
    get_schema_validation_statistics,
    set_schema_name,
)
from ci.transparency.cwe.types.schema_error_loading import (
    SchemaBundleError,
    SchemaConfigurationError,
    SchemaLoadingError,
    SchemaNotFoundError,
    SchemaParsingError,
    SchemaSearchError,
    SchemaVersionError,
)
from ci.transparency.cwe.types.schema_result_loading import (
    SchemaLoadingResult,
    add_failed_schema,
    add_loaded_schema,
    add_search_path,
    get_schema_loading_summary,
    set_catalog_version,
)

class TestSchemaDomain:
    def test_freeze_errors(self):
        errs = [
            SchemaFreezeError("freeze base", Path("/s.json"), "hash"),
            SchemaHashError("hash fail"),
            SchemaSourceValidationError("source invalid"),
            SchemaRepoDetectionError("no repo"),
            SchemaFileNotFoundError("missing"),
            SchemaPermissionError("perm"),
            SchemaIntegrityError("integrity"),
        ]
        for e in errs:
            assert isinstance(e, SchemaFreezeError)
            assert str(e)

    def test_validation_errors(self):
        errs = [
            SchemaValidationError("base"),
            SchemaUnavailableError("unavailable"),
            DocumentValidationError("doc invalid"),
            SchemaCompilationError("compile"),
            ValidationContextError("context"),
            BatchValidationError("batch"),
            SchemaMetaValidationError("meta invalid"),
        ]
        for e in errs:
            assert isinstance(e, SchemaValidationError)

    def test_schema_validation_result(self):
        res = SchemaValidationResult()
        res = set_schema_name(res, "cwe_schema")
        res = add_validated_document(res, "/ok.json")
        res = add_invalid_document(res, "/bad.json", "missing field")
        res = add_schema_error(res, "invalid enum")

        stats = get_schema_validation_statistics(res)
        assert stats["total_documents"] == 1  # only validated counted here
        assert stats["validation_failed"] == 1
        assert stats["schema_errors"] == 1
        assert "success_rate_percent" in stats





class TestSchemaLoadingErrors:
    """Test schema loading error hierarchy."""

    def test_base_schema_loading_error(self):
        """Test base SchemaLoadingError functionality."""
        # Basic error
        error = SchemaLoadingError("Basic error")
        assert str(error) == "Basic error"

        # With schema name
        error_with_schema = SchemaLoadingError("Error", schema_name="cwe_schema")
        assert "Schema: cwe_schema" in str(error_with_schema)

        # With file path
        error_with_path = SchemaLoadingError("Error", file_path=Path("/schema.json"))
        assert "schema.json" in str(error_with_path)



        # With both
        full_error = SchemaLoadingError("Error", schema_name="cwe", file_path=Path("/cwe.json"))
        error_str = str(full_error)
        assert "Schema: cwe" in error_str
        assert "cwe.json" in error_str

    def test_schema_loading_error_subclasses(self):
        """Test all SchemaLoadingError subclasses."""
        errors = [
            SchemaNotFoundError("Not found"),
            SchemaParsingError("Parse error"),
            SchemaVersionError("Version error"),
            SchemaBundleError("Bundle error"),
            SchemaSearchError("Search error"),
            SchemaConfigurationError("Config error"),
        ]

        for error in errors:
            assert isinstance(error, SchemaLoadingError)
            assert str(error)  # Should not raise


class TestSchemaLoadingResult:
    """Test SchemaLoadingResult class and helper functions."""

    def test_empty_result_initialization(self):
        """Test creating an empty SchemaLoadingResult."""
        result = SchemaLoadingResult()

        assert result.schema_count == 0
        assert result.available_schemas == ()
        assert not result.has_cwe_schema
        assert not result.has_mapping_schema
        assert result.loaded_count == 0
        assert result.failed_count == 0
        assert result.loaded_schemas == ()
        assert result.failed_schemas == ()
        assert result.search_paths == ()
        assert result.catalog_version == ""

    def test_properties_with_loaded_schemas(self):
        """Test properties when schemas are loaded."""
        schemas = {
            "cwe_schema": {"type": "object"},
            "mapping_schema": {"type": "array"},
            "other_schema": None  # Not loaded
        }

        result = SchemaLoadingResult(
            schemas=schemas,
            loaded_schemas=("cwe_schema", "mapping_schema"),
            loaded_count=2
        )

        assert result.schema_count == 2
        assert result.has_cwe_schema
        assert result.has_mapping_schema
        assert set(result.available_schemas) == {"cwe_schema", "mapping_schema"}

    def test_add_loaded_schema(self):
        """Test adding a successfully loaded schema."""
        result = SchemaLoadingResult()
        from typing import Dict, Any
        schema_data: Dict[str, Any] = {"type": "object", "properties": {}}
        source_path = Path("/schemas/cwe.json")

        updated = add_loaded_schema(result, "cwe_schema", schema_data, source_path)

        assert updated.has_cwe_schema
        assert updated.schema_count == 1
        assert updated.loaded_count == 1
        assert "cwe_schema" in updated.loaded_schemas
        assert updated.schemas["cwe_schema"] == schema_data

    def test_add_failed_schema(self):
        """Test adding a failed schema load."""
        result = SchemaLoadingResult()

        updated = add_failed_schema(result, "bad_schema", "File not found")

        assert updated.failed_count == 1
        assert "bad_schema" in updated.failed_schemas
        assert len(updated.errors) == 1
        assert "bad_schema: File not found" in updated.errors[0]

    def test_add_search_path(self):
        """Test adding a search path."""
        result = SchemaLoadingResult()
        search_path = Path("/usr/share/schemas")

        updated = add_search_path(result, search_path)

        assert search_path in updated.search_paths
        assert len(updated.search_paths) == 1

    def test_set_catalog_version(self):
        """Test setting catalog version."""
        result = SchemaLoadingResult()

        updated = set_catalog_version(result, "v2.1.0")

        assert updated.catalog_version == "v2.1.0"

    def test_get_schema_loading_summary(self):
        """Test getting schema loading summary."""
        schemas: dict[str, dict[str, Any] | None] = {"cwe_schema": {"type": "object"}}
        result = SchemaLoadingResult(
            schemas=schemas,
            loaded_schemas=("cwe_schema",),
            failed_schemas=("bad_schema",),
            search_paths=(Path("/schemas"),),
            catalog_version="v1.0",
            loaded_count=1,
            failed_count=1
        )

        summary = get_schema_loading_summary(result)

        assert summary["catalog_version"] == "v1.0"
        assert summary["total_schemas"] == 1
        assert summary["loaded_successfully"] == 1
        assert summary["failed_to_load"] == 1
        assert summary["available_schemas"] == ["cwe_schema"]
        assert summary["failed_schemas"] == ["bad_schema"]
        assert summary["search_paths_count"] == 1
        assert "success_rate_percent" in summary

    def test_immutability(self):
        """Test that helper functions don't mutate the original result."""
        original = SchemaLoadingResult()

        # Add a schema
        updated = add_loaded_schema(original, "test", {"data": True}, Path("/test.json"))

        # Original should be unchanged
        assert original.schema_count == 0
        assert not original.has_cwe_schema

        # Updated should have the schema
        assert updated.schema_count == 1
        assert "test" in updated.available_schemas
