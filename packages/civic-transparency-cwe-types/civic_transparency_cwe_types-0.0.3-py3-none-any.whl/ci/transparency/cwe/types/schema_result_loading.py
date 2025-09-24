"""Schema loading result type."""

from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any

from ci.transparency.cwe.types.base_result_loading import BaseLoadingResult


@dataclass(frozen=True, slots=True)
class SchemaLoadingResult(BaseLoadingResult):
    """Results from schema loading operations."""

    schemas: dict[str, dict[str, Any] | None] = field(
        default_factory=lambda: {
            "cwe_schema": None,
            "mapping_schema": None,
        }
    )
    loaded_schemas: tuple[str, ...] = ()
    failed_schemas: tuple[str, ...] = ()
    search_paths: tuple[Path, ...] = ()
    catalog_version: str = ""

    @property
    def available_schemas(self) -> tuple[str, ...]:
        """Names of successfully loaded schemas."""
        return tuple(name for name, schema in self.schemas.items() if schema is not None)

    @property
    def schema_count(self) -> int:
        """Number of schemas successfully loaded."""
        return len(self.available_schemas)

    @property
    def has_cwe_schema(self) -> bool:
        """True if the CWE schema was loaded."""
        return self.schemas.get("cwe_schema") is not None

    @property
    def has_mapping_schema(self) -> bool:
        """True if the mapping schema was loaded."""
        return self.schemas.get("mapping_schema") is not None


def add_loaded_schema[R: SchemaLoadingResult](
    result: R, schema_name: str, schema_data: dict[str, Any], source_path: Path
) -> R:
    """Return a copy with a successfully loaded schema added."""
    new_schemas = {**result.schemas, schema_name: schema_data}
    return replace(
        result,
        schemas=new_schemas,
        loaded_schemas=result.loaded_schemas + (schema_name,),
        loaded_count=result.loaded_count + 1,
    )


def add_failed_schema[R: SchemaLoadingResult](result: R, schema_name: str, error: str) -> R:
    """Return a copy with a failed schema load recorded."""
    new_errors = result.errors + (f"{schema_name}: {error}",)
    return replace(
        result,
        errors=new_errors,
        failed_schemas=result.failed_schemas + (schema_name,),
        failed_count=result.failed_count + 1,
    )


def add_search_path[R: SchemaLoadingResult](result: R, path: Path) -> R:
    """Return a copy with a searched path recorded."""
    return replace(result, search_paths=result.search_paths + (path,))


def set_catalog_version[R: SchemaLoadingResult](result: R, version: str) -> R:
    """Return a copy with the catalog version set."""
    return replace(result, catalog_version=version)


def get_schema_loading_summary(result: SchemaLoadingResult) -> dict[str, Any]:
    """Summary of schema loading statistics."""
    return {
        "catalog_version": result.catalog_version,
        "total_schemas": result.schema_count,
        "loaded_successfully": result.loaded_count,
        "failed_to_load": result.failed_count,
        "available_schemas": list(result.available_schemas),
        "failed_schemas": list(result.failed_schemas),
        "search_paths_count": len(result.search_paths),
        "success_rate_percent": round(result.success_rate * 100, 2),
    }
