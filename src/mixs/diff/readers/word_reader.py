"""Word document reader for pre-2009 MIxS schemas (.docx).

This reader handles the earliest MIxS specifications that were distributed
as Word documents with embedded tables.

Note: Only 2 files in the legacy corpus use this format (pre-2009/).
"""

import logging
from pathlib import Path
from typing import Dict, List, Optional, Any

from mixs.diff.models import NormalizedSchema, NormalizedTerm
from mixs.diff.readers.base import BaseReader, detect_format

logger = logging.getLogger(__name__)


class WordReader(BaseReader):
    """Reader for Word-based MIxS schemas (.docx).

    Parses tables from Word documents to extract term definitions.
    """

    @classmethod
    def can_read(cls, path: str) -> bool:
        """Check if this reader can handle the given path."""
        fmt = detect_format(path)
        return fmt == "docx"

    def read(self, path: str, version: Optional[str] = None) -> NormalizedSchema:
        """Read Word document and return normalized representation.

        Args:
            path: Path to the .docx file.
            version: Optional version string. Defaults to "v1.x" for pre-2009 files.

        Returns:
            NormalizedSchema with terms extracted from document tables.
        """
        try:
            from docx import Document
        except ImportError:
            raise ImportError(
                "python-docx is required for reading .docx files. "
                "Install with: poetry install --with legacy-diff"
            )

        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"Word file not found: {path}")

        if version is None:
            version = self._detect_version(path)

        logger.info(f"Reading Word document: {path} (version: {version})")

        doc = Document(path)

        schema = NormalizedSchema(
            version=version,
            source_path=str(file_path),
            source_format="docx",
        )

        # Extract terms from tables
        self._extract_from_tables(doc, schema)

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

    def _extract_from_tables(self, doc, schema: NormalizedSchema) -> None:
        """Extract term definitions from document tables.

        Pre-2009 Word documents typically have terms in tables with
        columns like: Item, Definition, Expected Value, etc.
        """
        for table in doc.tables:
            if len(table.rows) < 2:
                continue

            # Try to identify header row
            header_row = table.rows[0]
            headers = [cell.text.strip().lower() for cell in header_row.cells]

            # Check if this looks like a term definition table
            if not self._is_term_table(headers):
                continue

            # Build column mapping
            col_map = self._build_column_map(headers)

            # Process data rows
            for row in table.rows[1:]:
                cells = [cell.text.strip() for cell in row.cells]
                term = self._row_to_term(cells, col_map)
                if term and term.name:
                    schema.terms[term.name] = term

    def _is_term_table(self, headers: List[str]) -> bool:
        """Check if headers indicate a term definition table."""
        term_indicators = ["item", "definition", "expected value", "example", "occurrence"]
        matches = sum(1 for h in headers if any(ind in h for ind in term_indicators))
        return matches >= 2

    def _build_column_map(self, headers: List[str]) -> Dict[str, int]:
        """Build mapping from field names to column indices."""
        col_map = {}

        mappings = {
            "name": ["structured comment name", "item name", "item", "name"],
            "item": ["item", "item name"],
            "definition": ["definition", "description"],
            "example": ["example", "examples"],
            "expected_value": ["expected value", "value", "expected"],
            "occurrence": ["occurrence", "occurence", "requirement"],
            "section": ["section", "category"],
        }

        for field_name, variations in mappings.items():
            for i, header in enumerate(headers):
                if any(var in header for var in variations):
                    col_map[field_name] = i
                    break

        return col_map

    def _row_to_term(self, cells: List[str], col_map: Dict[str, int]) -> Optional[NormalizedTerm]:
        """Convert a table row to a NormalizedTerm."""
        def get_val(field: str) -> str:
            idx = col_map.get(field)
            if idx is not None and idx < len(cells):
                return cells[idx]
            return ""

        # Use 'item' as name if no explicit name column
        name = get_val("name")
        if not name:
            name = get_val("item")

        if not name:
            return None

        # Normalize name to structured comment format
        name = self._normalize_term_name(name)

        return NormalizedTerm(
            name=name,
            item=get_val("item"),
            definition=get_val("definition"),
            example=get_val("example"),
            expected_value=get_val("expected_value"),
            occurrence=get_val("occurrence"),
            section=get_val("section"),
        )

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
