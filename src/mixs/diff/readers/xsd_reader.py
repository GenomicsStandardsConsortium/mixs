"""XSD reader for 2006 MIGS XML Schema (.xsd).

This reader handles the earliest machine-readable MIxS specification
from the 2006 Migs.xsd XML Schema file.

Note: Only 1 file in the legacy corpus uses this format (pre-2009/Migs.xsd).
"""

import logging
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Any

from mixs.diff.models import NormalizedSchema, NormalizedTerm
from mixs.diff.readers.base import BaseReader, detect_format

logger = logging.getLogger(__name__)

# XML Schema namespace
XS_NS = "{http://www.w3.org/2001/XMLSchema}"


class XsdReader(BaseReader):
    """Reader for XSD-based MIxS schemas.

    Parses XML Schema definitions to extract type and element information.
    """

    @classmethod
    def can_read(cls, path: str) -> bool:
        """Check if this reader can handle the given path."""
        fmt = detect_format(path)
        return fmt == "xsd"

    def read(self, path: str, version: Optional[str] = None) -> NormalizedSchema:
        """Read XSD file and return normalized representation.

        Args:
            path: Path to the .xsd file.
            version: Optional version string. Defaults to "v1.0" for XSD files.

        Returns:
            NormalizedSchema with terms extracted from the XSD.
        """
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"XSD file not found: {path}")

        if version is None:
            version = "v1.0"  # 2006 XSD is earliest version

        logger.info(f"Reading XSD schema: {path} (version: {version})")

        tree = ET.parse(path)
        root = tree.getroot()

        schema = NormalizedSchema(
            version=version,
            source_path=str(file_path),
            source_format="xsd",
        )

        # Extract schema metadata
        schema.metadata["target_namespace"] = root.get("targetNamespace", "")
        schema.metadata["element_form_default"] = root.get("elementFormDefault", "")

        # Extract elements and complex types
        self._extract_elements(root, schema)
        self._extract_complex_types(root, schema)

        logger.info(f"Loaded {len(schema.terms)} terms from {file_path.name}")

        return schema

    def _extract_elements(self, root: ET.Element, schema: NormalizedSchema) -> None:
        """Extract top-level elements from XSD."""
        for elem in root.findall(f"{XS_NS}element"):
            name = elem.get("name")
            if not name:
                continue

            term = self._element_to_term(elem)
            if term:
                schema.terms[term.name] = term

    def _extract_complex_types(self, root: ET.Element, schema: NormalizedSchema) -> None:
        """Extract complex type definitions from XSD."""
        for complex_type in root.findall(f"{XS_NS}complexType"):
            type_name = complex_type.get("name")
            if not type_name:
                continue

            # Extract elements within the complex type
            for sequence in complex_type.findall(f".//{XS_NS}sequence"):
                for elem in sequence.findall(f"{XS_NS}element"):
                    term = self._element_to_term(elem, parent_type=type_name)
                    if term and term.name not in schema.terms:
                        schema.terms[term.name] = term

            # Also check for all/choice constructs
            for container in complex_type.findall(f".//{XS_NS}all") + complex_type.findall(f".//{XS_NS}choice"):
                for elem in container.findall(f"{XS_NS}element"):
                    term = self._element_to_term(elem, parent_type=type_name)
                    if term and term.name not in schema.terms:
                        schema.terms[term.name] = term

    def _element_to_term(self, elem: ET.Element, parent_type: str = "") -> Optional[NormalizedTerm]:
        """Convert an XSD element to a NormalizedTerm."""
        name = elem.get("name")
        if not name:
            return None

        # Normalize name
        normalized_name = self._normalize_term_name(name)

        # Extract type information
        elem_type = elem.get("type", "")

        # Extract occurrence info
        min_occurs = elem.get("minOccurs", "1")
        max_occurs = elem.get("maxOccurs", "1")
        occurrence = "M" if min_occurs != "0" else "X"

        # Extract documentation/annotation
        definition = ""
        annotation = elem.find(f"{XS_NS}annotation")
        if annotation is not None:
            doc = annotation.find(f"{XS_NS}documentation")
            if doc is not None and doc.text:
                definition = doc.text.strip()

        # Extract restriction patterns if present
        value_syntax = ""
        simple_type = elem.find(f"{XS_NS}simpleType")
        if simple_type is not None:
            restriction = simple_type.find(f"{XS_NS}restriction")
            if restriction is not None:
                pattern = restriction.find(f"{XS_NS}pattern")
                if pattern is not None:
                    value_syntax = pattern.get("value", "")

        term = NormalizedTerm(
            name=normalized_name,
            item=name,  # Original name as item
            definition=definition,
            expected_value=elem_type,
            value_syntax=value_syntax,
            occurrence=occurrence,
        )

        # Store additional XSD-specific info
        term.extra["xsd_type"] = elem_type
        term.extra["min_occurs"] = min_occurs
        term.extra["max_occurs"] = max_occurs
        if parent_type:
            term.extra["parent_type"] = parent_type

        return term

    def _normalize_term_name(self, name: str) -> str:
        """Normalize XSD element name to structured comment format."""
        # Convert camelCase to snake_case
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        normalized = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
        return normalized
