"""LinkML reader for MIxS v6+ YAML schemas.

Wraps SchemaView to produce NormalizedSchema for comparison with legacy formats.
"""

import logging
import os
import re
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Any

import requests
import yaml as pyyaml
from linkml_runtime.utils.schemaview import SchemaView

from mixs.diff.models import NormalizedSchema, NormalizedTerm
from mixs.diff.readers.base import BaseReader, detect_format

logger = logging.getLogger(__name__)


class LinkMLReader(BaseReader):
    """Reader for LinkML-based MIxS schemas (v6+)."""

    @classmethod
    def can_read(cls, path: str) -> bool:
        """Check if this reader can handle the given path."""
        fmt = detect_format(path)
        return fmt == "linkml"

    def read(self, path: str, version: Optional[str] = None) -> NormalizedSchema:
        """Read LinkML schema and return normalized representation.

        Args:
            path: Path to YAML file or GitHub specification
                  (e.g., "GenomicsStandardsConsortium/mixs@v6.2.3:src/mixs/schema/mixs.yaml").
            version: Optional version string. If not provided, attempts to detect.

        Returns:
            NormalizedSchema with terms extracted from the LinkML schema.
        """
        # Check if this is a GitHub specification
        if "@" in path and ":" in path:
            schema_view, version = self._load_from_github(path, version)
        else:
            schema_view = self._load_from_file(path)
            if version is None:
                version = self._detect_version(path, schema_view)

        logger.info(f"Reading LinkML schema: {path} (version: {version})")

        schema = NormalizedSchema(
            version=version,
            source_path=path,
            source_format="linkml",
        )

        # Extract schema metadata
        if schema_view.schema:
            schema.metadata["name"] = schema_view.schema.name
            schema.metadata["title"] = schema_view.schema.title
            schema.metadata["id"] = schema_view.schema.id

        # Process all slots as terms
        self._extract_terms(schema_view, schema)

        # Process classes to build checklist and package membership
        self._extract_checklists_and_packages(schema_view, schema)

        logger.info(f"Loaded {len(schema.terms)} terms, {len(schema.packages)} packages, "
                   f"{len(schema.checklists)} checklists from {path}")

        return schema

    def _load_from_file(self, path: str) -> SchemaView:
        """Load SchemaView from local file."""
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"Schema file not found: {path}")
        return SchemaView(str(file_path))

    def _load_from_github(self, spec: str, version: Optional[str] = None) -> tuple:
        """Load SchemaView from GitHub specification.

        Handles both single-file schemas (v6.2.0+) and multi-file schemas (v6.0.0, v6.1.x)
        by downloading imported files to a temp directory.

        Args:
            spec: GitHub specification in format "owner/repo@commit:path"
            version: Optional version override

        Returns:
            Tuple of (SchemaView, version_string)
        """
        # Parse specification
        owner, repo, commit, file_path = self._parse_github_spec(spec)
        base_dir = str(Path(file_path).parent)

        # Construct raw file URL
        base_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{commit}"
        raw_url = f"{base_url}/{file_path}"

        logger.info(f"Fetching schema from: {raw_url}")

        # Download main file
        response = requests.get(raw_url, timeout=30)
        response.raise_for_status()
        main_content = response.text

        # Create temp directory and download schema files
        temp_dir = tempfile.mkdtemp(prefix="mixs_schema_")
        main_filename = Path(file_path).name
        main_path = Path(temp_dir) / main_filename

        try:
            # Write main file
            with open(main_path, 'w') as f:
                f.write(main_content)

            # Parse imports from the main file and download them
            self._download_imports(main_content, base_url, base_dir, temp_dir)

            schema_view = SchemaView(str(main_path))
        except Exception:
            # Clean up temp directory on error
            shutil.rmtree(temp_dir, ignore_errors=True)
            raise

        # Note: We intentionally don't delete the temp directory here
        # because SchemaView may need to access imported files lazily.
        # The OS will clean it up eventually, or we could add cleanup later.

        # Use commit/tag as version if not provided
        if version is None:
            version = commit

        return schema_view, version

    def _download_imports(self, yaml_content: str, base_url: str, base_dir: str, temp_dir: str) -> None:
        """Download imported schema files to temp directory.

        Parses the 'imports:' section of a YAML file and recursively downloads
        any local imports (not linkml: prefixed).

        Args:
            yaml_content: Content of the main YAML file
            base_url: Base GitHub raw URL (e.g., https://raw.githubusercontent.com/owner/repo/commit)
            base_dir: Directory containing the schema files in the repo
            temp_dir: Local temp directory to save files
        """
        try:
            data = pyyaml.safe_load(yaml_content)
        except Exception as e:
            logger.warning(f"Could not parse YAML for imports: {e}")
            return

        imports = data.get('imports', [])
        if not imports:
            return

        for imp in imports:
            # Skip linkml built-in imports
            if imp.startswith('linkml:'):
                continue

            # Construct import file path
            import_filename = f"{imp}.yaml" if not imp.endswith('.yaml') else imp
            import_url = f"{base_url}/{base_dir}/{import_filename}"
            local_path = Path(temp_dir) / import_filename

            # Skip if already downloaded
            if local_path.exists():
                continue

            logger.debug(f"Downloading import: {import_filename}")

            try:
                response = requests.get(import_url, timeout=30)
                response.raise_for_status()

                with open(local_path, 'w') as f:
                    f.write(response.text)

                # Recursively download imports from this file
                self._download_imports(response.text, base_url, base_dir, temp_dir)

            except requests.RequestException as e:
                logger.warning(f"Could not download import {import_filename}: {e}")

    def _parse_github_spec(self, spec: str) -> tuple:
        """Parse GitHub specification string.

        Args:
            spec: Format "owner/repo@commit:path"

        Returns:
            Tuple of (owner, repo, commit, path)
        """
        if "@" not in spec or ":" not in spec:
            raise ValueError(f"Invalid GitHub spec format: {spec}")

        owner_repo, commit_path = spec.split("@", 1)
        owner, repo = owner_repo.split("/", 1)
        commit, path = commit_path.split(":", 1)

        return owner, repo, commit, path

    def _detect_version(self, path: str, schema_view: SchemaView) -> str:
        """Attempt to detect version from path or schema metadata."""
        # Try to extract from path
        match = re.search(r'v?(\d+\.\d+(?:\.\d+)?)', path)
        if match:
            return f"v{match.group(1)}"

        # Try schema metadata
        if schema_view.schema and schema_view.schema.version:
            return str(schema_view.schema.version)

        return "unknown"

    def _extract_terms(self, schema_view: SchemaView, schema: NormalizedSchema) -> None:
        """Extract terms from LinkML slots."""
        all_slots = schema_view.all_slots(imports=True)

        for slot_name, slot_def in all_slots.items():
            term = NormalizedTerm(
                name=slot_name,
                item=slot_def.title or "",
                definition=slot_def.description or "",
                expected_value=str(slot_def.range) if slot_def.range else "",
                occurrence="M" if slot_def.required else "",
            )

            # Extract examples
            if slot_def.examples:
                examples = []
                for ex in slot_def.examples:
                    if hasattr(ex, 'value') and ex.value:
                        examples.append(str(ex.value))
                term.example = "; ".join(examples)

            # Extract structured pattern as value_syntax
            if hasattr(slot_def, 'structured_pattern') and slot_def.structured_pattern:
                if hasattr(slot_def.structured_pattern, 'syntax'):
                    term.value_syntax = slot_def.structured_pattern.syntax or ""
            elif slot_def.pattern:
                term.value_syntax = slot_def.pattern

            # Extract preferred unit from annotations or unit slot
            if hasattr(slot_def, 'unit') and slot_def.unit:
                term.preferred_unit = str(slot_def.unit)

            # Extract MIXS ID from slot_uri or annotations
            if slot_def.slot_uri:
                term.mixs_id = str(slot_def.slot_uri)

            # Store in annotations for additional metadata
            if slot_def.annotations:
                for ann_name, ann_val in slot_def.annotations.items():
                    term.extra[str(ann_name)] = str(ann_val)

            # Extract multivalued info
            if slot_def.multivalued:
                term.extra["multivalued"] = True

            schema.terms[slot_name] = term

    def _extract_checklists_and_packages(self, schema_view: SchemaView, schema: NormalizedSchema) -> None:
        """Extract checklist and package information from classes."""
        all_classes = schema_view.all_classes(imports=True)

        # Known checklist class prefixes
        checklist_prefixes = ["Migs", "Mims", "Mimarks", "Misag", "Mimag", "Miuvig", "Me"]

        # Known environmental package names (extensions)
        package_names = [
            "Agriculture", "Air", "BuiltEnvironment", "HostAssociated",
            "HumanAssociated", "HumanGut", "HumanOral", "HumanSkin", "HumanVaginal",
            "HydrocarbonResourcesCores", "HydrocarbonResourcesFluidsSwabs",
            "MicrobialMatBiofilm", "MiscellaneousNaturalOrArtificialEnvironment",
            "PlantAssociated", "Sediment", "Soil", "SymbiontAssociated",
            "WastewaterSludge", "Water", "FoodAnimalAndAnimalFeed", "FoodFarmEnvironment",
            "FoodFoodProductionFacility", "FoodHumanFoods",
        ]

        for class_name, class_def in all_classes.items():
            # Skip abstract classes and mixins
            if class_def.abstract or class_def.mixin:
                continue

            # Determine if this is a checklist or package
            is_checklist = any(class_name.startswith(prefix) for prefix in checklist_prefixes)
            is_package = class_name in package_names

            if is_checklist or is_package:
                # Get slots for this class
                try:
                    class_slots = list(schema_view.class_slots(class_name))
                except Exception:
                    class_slots = []

                if is_checklist:
                    # Normalize checklist name
                    checklist_normalized = self._normalize_checklist_name(class_name)
                    schema.checklists[checklist_normalized] = class_slots

                    # Update term membership
                    for slot_name in class_slots:
                        if slot_name in schema.terms:
                            # Try to get requirement from induced slot
                            try:
                                induced = schema_view.induced_slot(slot_name, class_name)
                                req = "M" if induced.required else "X"
                            except Exception:
                                req = ""
                            schema.terms[slot_name].checklist_membership[checklist_normalized] = req

                if is_package:
                    # Normalize package name
                    package_normalized = self._normalize_package_name(class_name)
                    schema.packages[package_normalized] = class_slots

                    # Update term membership
                    for slot_name in class_slots:
                        if slot_name in schema.terms:
                            try:
                                induced = schema_view.induced_slot(slot_name, class_name)
                                req = "M" if induced.required else "X"
                            except Exception:
                                req = ""
                            schema.terms[slot_name].package_membership[package_normalized] = req

    def _normalize_checklist_name(self, class_name: str) -> str:
        """Normalize checklist class name to standard format."""
        # Convert CamelCase to lowercase with underscores
        name = re.sub(r'([A-Z])', r'_\1', class_name).lower().strip('_')

        # Map common names to standard abbreviations
        mappings = {
            "migs_ba": "migs_ba",
            "migs_eu": "migs_eu",
            "migs_pl": "migs_pl",
            "migs_vi": "migs_vi",
            "migs_org": "migs_org",
            "mims": "mims",
            "mimarks_s": "mimarks_s",
            "mimarks_c": "mimarks_c",
            "misag": "misag",
            "mimag": "mimag",
            "miuvig": "miuvig",
            "me": "me",
        }

        for standard, normalized in mappings.items():
            if standard in name:
                return normalized

        return name

    def _normalize_package_name(self, class_name: str) -> str:
        """Normalize package class name to standard format."""
        # Convert CamelCase to snake_case
        name = re.sub(r'([A-Z])', r'_\1', class_name).lower().strip('_')
        return name
