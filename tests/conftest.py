"""Shared test fixtures for MIxS legacy diff tests.

Downloads Excel test files from the public GenomicsStandardsConsortium/mixs-legacy
repo on GitHub if they aren't available locally (e.g. in CI).
"""

import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
MIXS_LEGACY_LOCAL = ROOT.parent / "mixs-legacy"
MIXS_LEGACY_CACHE = ROOT / ".test_cache" / "mixs-legacy"

# Raw GitHub URLs for the two Excel files we need
_GITHUB_RAW = "https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs-legacy/master"
_EXCEL_FILES = {
    "mixs4/MIxS_210514.xls": f"{_GITHUB_RAW}/mixs4/MIxS_210514.xls",
    "mixs5/mixs_v5.xlsx": f"{_GITHUB_RAW}/mixs5/mixs_v5.xlsx",
}


def _download_file(url: str, dest: Path) -> None:
    """Download a file from URL to dest, creating parent dirs."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(url, dest)


def get_legacy_file(relative_path: str) -> Path:
    """Get path to a legacy Excel file, downloading if needed.

    Checks in order:
    1. Local mixs-legacy repo (sibling directory)
    2. .test_cache directory (downloaded from GitHub)
    3. Downloads from GitHub to .test_cache
    """
    # Try local repo first
    local = MIXS_LEGACY_LOCAL / relative_path
    if local.exists():
        return local

    # Try cache
    cached = MIXS_LEGACY_CACHE / relative_path
    if cached.exists():
        return cached

    # Download from GitHub
    url = _EXCEL_FILES.get(relative_path)
    if url is None:
        raise FileNotFoundError(
            f"No download URL configured for {relative_path}. "
            f"Available: {list(_EXCEL_FILES.keys())}"
        )

    _download_file(url, cached)
    return cached


def ensure_legacy_files() -> tuple[Path, Path]:
    """Ensure both v4 and v5 Excel files are available. Returns (v4_path, v5_path)."""
    v4 = get_legacy_file("mixs4/MIxS_210514.xls")
    v5 = get_legacy_file("mixs5/mixs_v5.xlsx")
    return v4, v5
