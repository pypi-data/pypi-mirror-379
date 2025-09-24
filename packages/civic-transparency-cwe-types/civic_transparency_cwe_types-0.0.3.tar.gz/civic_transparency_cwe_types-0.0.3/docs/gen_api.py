"""Generate API documentation pages for the civic-transparency-cwe-types package.

Walks the source tree, generates one page per (public) module or package,
and writes a literate nav so MkDocs picks up a nested API tree.
"""

from __future__ import annotations

from pathlib import Path
import pkgutil

import mkdocs_gen_files

PKG_IMPORT = "ci.transparency.cwe.types"
PKG_SRC = Path("src") / Path(*PKG_IMPORT.split("."))

nav = mkdocs_gen_files.Nav()


def is_public(modname: str) -> bool:
    """Hide anything with a private path component (e.g., ci._internal.foo)."""
    return all(part and not part.startswith("_") for part in modname.split("."))


# Sort for stable output across platforms/CI
for mod in sorted(
    pkgutil.walk_packages([str(PKG_SRC)], prefix=f"{PKG_IMPORT}."), key=lambda m: m.name
):
    if not is_public(mod.name):
        continue

    # One page per module (or package); include packages too so __init__.py is documented.
    module_path = Path("api", *mod.name.split(".")).with_suffix(".md")
    nav[tuple(mod.name.split("."))] = module_path.as_posix()

    with mkdocs_gen_files.open(module_path, "w") as f:
        print(f"# {mod.name}", file=f)
        print("", file=f)
        print(f"::: {mod.name}", file=f)
        print("    options:", file=f)
        print("      members_order: source", file=f)

    # Map "Edit this page" to the correct source file
    src_py = Path("src") / Path(*mod.name.split(".")).with_suffix(".py")
    init_py = Path("src") / Path(*mod.name.split(".")) / "__init__.py"
    if src_py.exists():
        mkdocs_gen_files.set_edit_path(module_path, src_py.as_posix())
    elif init_py.exists():
        mkdocs_gen_files.set_edit_path(module_path, init_py.as_posix())

# Write the literate nav file that the 'literate-nav' plugin will consume
with mkdocs_gen_files.open("api/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
