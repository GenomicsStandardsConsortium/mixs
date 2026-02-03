"""Word document reader for pre-2009 MIxS schemas (.docx).

This reader handles the earliest MIxS specifications that were distributed
as Word documents with embedded tables.

Note: Only 2 files in the legacy corpus use this format (pre-2009/).

The Word documents use a complex table structure. Terms are loaded from
a pre-extracted cache file (word_extracted_terms.json) since the original
documents require manual interpretation.
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any

from mixs.diff.models import NormalizedSchema, NormalizedTerm
from mixs.diff.readers.base import BaseReader, detect_format

logger = logging.getLogger(__name__)

# Default location for pre-extracted terms cache
DEFAULT_CACHE_PATH = Path(__file__).parent.parent.parent.parent.parent / "assets" / "legacy_format_profiles" / "word_extracted_terms.json"


class WordReader(BaseReader):
    """Reader for Word-based MIxS schemas (.docx).

    Loads term data from pre-extracted cache file since the original Word
    documents have complex table structures that require manual interpretation.
    """

    def __init__(self, cache_path: Optional[Path] = None):
        """Initialize the Word reader.

        Args:
            cache_path: Path to the pre-extracted terms JSON file.
                       Defaults to assets/legacy_format_profiles/word_extracted_terms.json
        """
        self.cache_path = cache_path or DEFAULT_CACHE_PATH
        self._cache: Optional[Dict] = None

    @classmethod
    def can_read(cls, path: str) -> bool:
        """Check if this reader can handle the given path."""
        fmt = detect_format(path)
        return fmt == "docx"

    def _load_cache(self) -> Dict:
        """Load the pre-extracted terms cache."""
        if self._cache is None:
            if not self.cache_path.exists():
                logger.warning(f"Cache file not found: {self.cache_path}")
                self._cache = {}
            else:
                with open(self.cache_path) as f:
                    self._cache = json.load(f)
                logger.info(f"Loaded pre-extracted terms from {self.cache_path}")
        return self._cache

    def read(self, path: str, version: Optional[str] = None) -> NormalizedSchema:
        """Read Word document and return normalized representation.

        Args:
            path: Path to the .docx file.
            version: Optional version string. Defaults to auto-detect from filename.

        Returns:
            NormalizedSchema with terms loaded from pre-extracted cache.
        """
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"Word file not found: {path}")

        filename = file_path.name

        if version is None:
            version = self._detect_version(path)

        logger.info(f"Reading Word document: {path} (version: {version})")

        schema = NormalizedSchema(
            version=version,
            source_path=str(file_path),
            source_format="docx",
        )

        # Load from pre-extracted cache
        cache = self._load_cache()

        if filename in cache:
            self._load_from_cache(cache[filename], schema)
        else:
            logger.warning(
                f"No pre-extracted data found for {filename}. "
                f"Available files: {[k for k in cache.keys() if not k.startswith('_')]}"
            )

        logger.info(f"Loaded {len(schema.terms)} terms from {file_path.name}")

        return schema

    def _detect_version(self, path: str) -> str:
        """Detect version from filename."""
        path_lower = path.lower()
        if "1.1" in path_lower:
            return "v1.1"
        elif "1.2" in path_lower:
            return "v1.2"
        elif "pre-2009" in path_lower or "pre2009" in path_lower:
            return "v1.x"
        return "v1.x"

    def _load_from_cache(self, file_data: Dict, schema: NormalizedSchema) -> None:
        """Load terms from cached extraction data."""
        # Override version if specified in cache
        if "version" in file_data:
            schema.version = file_data["version"]

        # Load checklists
        if "checklists" in file_data:
            for checklist_name in file_data["checklists"]:
                schema.checklists[checklist_name] = []

        # Load terms
        for term_data in file_data.get("terms", []):
            term = NormalizedTerm(
                name=term_data.get("term_name", ""),
                item=term_data.get("item", ""),
                definition=term_data.get("definition", ""),
                section=term_data.get("section", ""),
            )

            # Add checklist membership
            requirements = term_data.get("checklist_requirements", {})
            for checklist, req in requirements.items():
                if req and req not in ("-", ""):
                    term.checklist_membership[checklist] = req
                    # Add term to checklist's term list
                    if checklist in schema.checklists:
                        schema.checklists[checklist].append(term.name)

            if term.name:
                schema.terms[term.name] = term

    def _normalize_term_name(self, name: str) -> str:
        """Normalize term name to structured comment format.

        Converts names like "Project Name" to "project_name".
        """
        # Convert to lowercase and replace spaces/special chars with underscores
        normalized = name.lower()
        normalized = normalized.replace(" ", "_")
        normalized = normalized.replace("-", "_")
        normalized = "".join(c if c.isalnum() or c == "_" else "_" for c in normalized)
        # Remove multiple consecutive underscores
        while "__" in normalized:
            normalized = normalized.replace("__", "_")
        return normalized.strip("_")
