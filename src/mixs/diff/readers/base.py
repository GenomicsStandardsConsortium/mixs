"""Abstract base reader interface for MIxS schema formats."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional

from mixs.diff.models import NormalizedSchema


def detect_format(path: str) -> str:
    """Detect schema format from file path or specification.

    Args:
        path: File path or GitHub specification string.

    Returns:
        Format string: 'xlsx', 'xls', 'docx', 'xsd', 'linkml', or 'unknown'.
    """
    path_lower = path.lower()

    # Check for GitHub specification format (owner/repo@commit:path)
    if "@" in path and ":" in path:
        # Extract the actual file path from the spec
        _, file_path = path.split(":", 1)
        path_lower = file_path.lower()

    if path_lower.endswith(".xlsx"):
        return "xlsx"
    elif path_lower.endswith(".xls"):
        return "xls"
    elif path_lower.endswith(".docx"):
        return "docx"
    elif path_lower.endswith(".xsd"):
        return "xsd"
    elif path_lower.endswith((".yaml", ".yml")):
        return "linkml"
    else:
        return "unknown"


class BaseReader(ABC):
    """Abstract base class for schema readers."""

    @abstractmethod
    def read(self, path: str, version: Optional[str] = None) -> NormalizedSchema:
        """Read schema file and return normalized representation.

        Args:
            path: Path to the schema file (local path or GitHub spec).
            version: Optional version string to use. If not provided,
                    the reader will attempt to detect it.

        Returns:
            NormalizedSchema with all terms and metadata extracted.
        """
        pass

    @classmethod
    def can_read(cls, path: str) -> bool:
        """Check if this reader can handle the given path.

        Args:
            path: File path or specification to check.

        Returns:
            True if this reader can handle the file format.
        """
        return False


def get_reader(path: str, profiles_dir: Optional[Path] = None) -> BaseReader:
    """Get appropriate reader for the given path.

    Args:
        path: File path or GitHub specification.
        profiles_dir: Optional custom directory for format profiles (Excel only).

    Returns:
        Appropriate reader instance.

    Raises:
        ValueError: If no reader can handle the format.
    """
    from mixs.diff.readers.excel_reader import ExcelReader
    from mixs.diff.readers.linkml_reader import LinkMLReader

    fmt = detect_format(path)

    if fmt in ("xlsx", "xls"):
        return ExcelReader(profiles_dir=profiles_dir)
    elif fmt == "linkml":
        return LinkMLReader()
    elif fmt == "docx":
        # Import lazily to avoid dependency issues
        from mixs.diff.readers.word_reader import WordReader
        return WordReader()
    elif fmt == "xsd":
        # Import lazily to avoid dependency issues
        from mixs.diff.readers.xsd_reader import XsdReader
        return XsdReader()
    else:
        raise ValueError(f"No reader available for format '{fmt}' (path: {path})")
