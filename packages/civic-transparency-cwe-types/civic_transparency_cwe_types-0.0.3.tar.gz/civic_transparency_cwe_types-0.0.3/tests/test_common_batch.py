"""Tests for common batch loading result type."""

from pathlib import Path


from ci.transparency.cwe.types.common_result_loading_batch import (
    BatchLoadingResult,
    add_mapping,
    add_processed_file,
    add_skipped_file,
    get_batch_loading_summary,
    increment_file_type,
    update_file_type_stats,
)


class TestBatchLoadingResult:
    """Test BatchLoadingResult class and its properties."""

    def test_empty_result_initialization(self):
        """Test creating an empty BatchLoadingResult."""
        result = BatchLoadingResult()

        assert result.mapping_count == 0
        assert result.total_files_processed == 0
        assert result.loaded_count == 0
        assert result.failed_count == 0
        assert result.mappings == {}
        assert result.processed_files == ()
        assert result.skipped_files == ()
        assert result.file_types == {}

    def test_properties_with_data(self):
        """Test properties when BatchLoadingResult has data."""
        processed = (Path("file1.yaml"), Path("file2.yaml"))
        skipped = (Path("bad.yaml"),)
        mappings = {"cwe-1": {"name": "Test"}, "cwe-2": {"name": "Another"}}

        result = BatchLoadingResult(
            mappings=mappings,
            processed_files=processed,
            skipped_files=skipped,
            loaded_count=2,
        )

        assert result.mapping_count == 2
        assert result.total_files_processed == 3  # 2 processed + 1 skipped
        assert result.loaded_count == 2


class TestBatchLoadingHelpers:
    """Test helper functions for BatchLoadingResult."""

    def test_add_mapping(self):
        """Test adding a mapping to the result."""
        result = BatchLoadingResult()
        file_path = Path("test.yaml")

        updated = add_mapping(result, "key1", {"data": "value"}, file_path)

        assert updated.mapping_count == 1
        assert "key1" in updated.mappings
        assert updated.mappings["key1"] == {"data": "value"}
        assert updated.loaded_count == 1
        assert file_path in updated.processed_files

    def test_add_mapping_without_file_path(self):
        """Test adding a mapping without specifying a file path."""
        result = BatchLoadingResult()

        updated = add_mapping(result, "key1", {"data": "value"})

        assert updated.mapping_count == 1
        assert updated.loaded_count == 1
        assert len(updated.processed_files) == 0

    def test_add_skipped_file(self):
        """Test adding a skipped file with reason."""
        result = BatchLoadingResult()
        file_path = Path("invalid.yaml")

        updated = add_skipped_file(result, file_path, "Invalid format")

        assert file_path in updated.skipped_files
        assert len(updated.skipped_files) == 1
        # Should also add a warning
        assert len(updated.warnings) == 1
        assert "Skipped" in updated.warnings[0]

    def test_add_processed_file(self):
        """Test adding a processed file."""
        result = BatchLoadingResult()
        file_path = Path("processed.yaml")

        updated = add_processed_file(result, file_path)

        assert file_path in updated.processed_files
        assert len(updated.processed_files) == 1

    def test_update_file_type_stats(self):
        """Test updating file type statistics."""
        result = BatchLoadingResult()

        updated = update_file_type_stats(result, "yaml", 5)

        assert updated.file_types["yaml"] == 5

    def test_increment_file_type(self):
        """Test incrementing file type count."""
        result = BatchLoadingResult(file_types={"yaml": 3})

        # Increment existing type
        updated = increment_file_type(result, "yaml")
        assert updated.file_types["yaml"] == 4

        # Increment new type
        updated2 = increment_file_type(updated, "json")
        assert updated2.file_types["json"] == 1
        assert updated2.file_types["yaml"] == 4

    def test_get_batch_loading_summary(self):
        """Test getting a summary of batch loading results."""
        processed = (Path("file1.yaml"), Path("file2.yaml"))
        skipped = (Path("bad.yaml"),)
        mappings = {"key1": {"data": "value"}}
        file_types = {"yaml": 3, "json": 1}

        result = BatchLoadingResult(
            mappings=mappings,
            processed_files=processed,
            skipped_files=skipped,
            file_types=file_types,
            loaded_count=1,
            failed_count=1,
        )

        summary = get_batch_loading_summary(result)

        assert summary["total_mappings"] == 1
        assert summary["loaded_successfully"] == 1
        assert summary["failed_to_load"] == 1
        assert summary["files_processed"] == 2
        assert summary["files_skipped"] == 1
        assert summary["file_types"] == {"yaml": 3, "json": 1}
        assert "success_rate_percent" in summary

    def test_immutability(self):
        """Test that helper functions don't mutate the original result."""
        original = BatchLoadingResult(mappings={"key1": {"data": "value"}})

        # Add a mapping
        updated = add_mapping(original, "key2", {"data": "value2"})

        # Original should be unchanged
        assert len(original.mappings) == 1
        assert "key2" not in original.mappings

        # Updated should have both
        assert len(updated.mappings) == 2
        assert "key2" in updated.mappings
