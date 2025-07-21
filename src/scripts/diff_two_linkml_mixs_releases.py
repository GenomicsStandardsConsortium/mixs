"""
Script to compare MIxS schema releases using GitHub API.

Fetches release information from GitHub, identifies mixs.yaml files across releases,
and saves structured data for analysis. Supports GitHub API authentication via
local/.env file for higher rate limits.

Usage:
    python diff_two_linkml_mixs_releases.py

Output:
    - Console output showing releases and YAML files
    - local/mixs_releases.yaml with structured release data
"""

import requests
from datetime import datetime
import pprint
import os
from pathlib import Path
from dotenv import load_dotenv
import yaml
from linkml_runtime.utils.schemaview import SchemaView
from typing import List, Tuple, Dict, Optional, Any, Set
import re

APPROVED_DIRS = ['src', 'model']
DEFAULT_OLD_COMMIT = '74744ee'  # mixs6.0.0 - comparing from this version
DEFAULT_NEW_COMMIT = '994c745'  # main branch as of 2025-07-14 - comparing to this version

# Global configuration
SHOW_YAML_FILES = False  # Set to True to print discovered YAML files
VERBOSE_AUTH = False     # Set to True to print auth message every time
SHOW_ALL_CLASS_NAMES = True  # Set to True to print all class names in diffs
SHOW_ALL_ENUM_NAMES = True  # Set to True to print all enum names in diffs
SHOW_ALL_SLOT_NAMES = True  # Set to True to print all slot names in diffs
API_CALL_COUNT = 0       # Track number of API calls made
AUTH_MESSAGE_PRINTED = False  # Track if auth message was already shown

# Load name mappings
CLASS_NAME_MAPPINGS = {}  # Will be loaded from TSV file
ENUM_NAME_MAPPINGS = {}   # Will be loaded from TSV file
SLOT_NAME_MAPPINGS = {}   # Will be loaded from TSV file
SUBSET_NAME_MAPPINGS = {}  # Will be loaded from TSV file
INTER_TYPE_REFACTORING = []  # Will be loaded from TSV file


def load_class_name_mappings() -> Dict[str, str]:
    """Load class name mappings from TSV file."""
    mappings = {}
    mapping_file = Path(__file__).parent.parent.parent / 'class_name_mappings.tsv'
    
    if not mapping_file.exists():
        print(f"Warning: Class name mapping file not found: {mapping_file}")
        return mappings
    
    try:
        with open(mapping_file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:  # Skip header
                    continue
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    old_name, new_name = parts
                    mappings[old_name] = new_name
        print(f"Loaded {len(mappings)} class name mappings")
    except Exception as e:
        print(f"Warning: Could not load class name mappings: {e}")
    
    return mappings


def load_enum_name_mappings() -> Dict[str, str]:
    """Load enum name mappings from TSV file."""
    mappings = {}
    mapping_file = Path(__file__).parent.parent.parent / 'enum_name_mappings.tsv'
    
    if not mapping_file.exists():
        print(f"Warning: Enum name mapping file not found: {mapping_file}")
        return mappings
    
    try:
        with open(mapping_file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:  # Skip header
                    continue
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    old_name, new_name = parts
                    mappings[old_name] = new_name
        print(f"Loaded {len(mappings)} enum name mappings")
    except Exception as e:
        print(f"Warning: Could not load enum name mappings: {e}")
    
    return mappings


def load_slot_name_mappings() -> Dict[str, str]:
    """Load slot name mappings from TSV file."""
    mappings = {}
    mapping_file = Path(__file__).parent.parent.parent / 'slot_name_mappings.tsv'
    
    if not mapping_file.exists():
        print(f"Warning: Slot name mapping file not found: {mapping_file}")
        return mappings
    
    try:
        with open(mapping_file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:  # Skip header
                    continue
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    old_name, new_name = parts
                    mappings[old_name] = new_name
        print(f"Loaded {len(mappings)} slot name mappings")
    except Exception as e:
        print(f"Warning: Could not load slot name mappings: {e}")
    
    return mappings


def load_subset_name_mappings() -> Dict[str, str]:
    """Load subset name mappings from TSV file."""
    mappings = {}
    mapping_file = Path(__file__).parent.parent.parent / 'subset_name_mappings.tsv'
    
    if not mapping_file.exists():
        print(f"Warning: Subset name mapping file not found: {mapping_file}")
        return mappings
    
    try:
        with open(mapping_file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:  # Skip header
                    continue
                parts = line.strip().split('\t')
                if len(parts) == 2:
                    old_name, new_name = parts
                    mappings[old_name] = new_name
        print(f"Loaded {len(mappings)} subset name mappings")
    except Exception as e:
        print(f"Warning: Could not load subset name mappings: {e}")
    
    return mappings


def load_inter_type_refactoring() -> List[Tuple[str, str, str, str]]:
    """Load inter-type refactoring mappings from TSV file."""
    mappings = []
    mapping_file = Path(__file__).parent.parent.parent / 'inter_type_refactoring.tsv'
    
    if not mapping_file.exists():
        print(f"Warning: Inter-type refactoring file not found: {mapping_file}")
        return mappings
    
    try:
        with open(mapping_file, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:  # Skip header
                    continue
                parts = line.strip().split('\t')
                if len(parts) >= 4:
                    old_type, old_name, new_type, new_name = parts[0], parts[1], parts[2], parts[3]
                    if old_type and old_name and new_type and new_name:
                        mappings.append((old_type, old_name, new_type, new_name))
        print(f"Loaded {len(mappings)} inter-type refactoring mappings")
    except Exception as e:
        print(f"Warning: Could not load inter-type refactoring mappings: {e}")
    
    return mappings


def filter_expected_name_changes(old_keys: Set[str], new_keys: Set[str], mappings: Dict[str, str]) -> Tuple[Set[str], Set[str], Set[str]]:
    """Filter out expected name changes based on mappings.
    
    Returns:
        Tuple of (unique_old, unique_new, expected_mappings)
    """
    unique_old = set()
    unique_new = set()
    expected_mappings = set()
    
    # Track which new keys have been accounted for
    accounted_new_keys = set()
    
    for old_key in old_keys:
        if old_key in mappings:
            expected_new_key = mappings[old_key]
            if expected_new_key in new_keys:
                # This is an expected mapping
                expected_mappings.add(f"{old_key} -> {expected_new_key}")
                accounted_new_keys.add(expected_new_key)
            else:
                # Expected mapping but new key not found
                unique_old.add(old_key)
        else:
            # No mapping for this old key - check if it exists unchanged in new keys
            if old_key in new_keys:
                # Key exists unchanged in both schemas
                accounted_new_keys.add(old_key)
            else:
                # Key only exists in old schema
                unique_old.add(old_key)
    
    # Any new keys not accounted for are unique
    unique_new = new_keys - accounted_new_keys
    
    return unique_old, unique_new, expected_mappings


def filter_inter_type_refactoring(element_type: str, only_in_old: Set[str], only_in_new: Set[str], 
                                 inter_type_mappings: List[Tuple[str, str, str, str]]) -> Tuple[Set[str], Set[str], Set[str]]:
    """Filter out expected inter-type refactoring from unique element lists.
    
    Args:
        element_type: Type of element being checked ('slot', 'subset', 'class', 'enum')
        only_in_old: Set of elements only found in old schema
        only_in_new: Set of elements only found in new schema
        inter_type_mappings: List of (old_type, old_name, new_type, new_name) tuples
        
    Returns:
        Tuple of (filtered_old, filtered_new, refactoring_found)
    """
    filtered_old = only_in_old.copy()
    filtered_new = only_in_new.copy()
    refactoring_found = set()
    
    for old_type, old_name, new_type, new_name in inter_type_mappings:
        # If this element type appears as old_type in refactoring, remove from only_in_old
        if old_type == element_type and old_name in only_in_old:
            filtered_old.discard(old_name)
            refactoring_found.add(f"{old_type}:{old_name} -> {new_type}:{new_name}")
        
        # If this element type appears as new_type in refactoring, remove from only_in_new  
        if new_type == element_type and new_name in only_in_new:
            filtered_new.discard(new_name)
            refactoring_found.add(f"{old_type}:{old_name} -> {new_type}:{new_name}")
    
    return filtered_old, filtered_new, refactoring_found


def is_populated(value: Any) -> bool:
    """Check if a value is populated using recursive analysis.
    
    This function performs robust checking of scalars, lists, dicts, and LinkML objects
    to determine if they contain meaningful content.
    
    Args:
        value: Value to check for populated status.
        
    Returns:
        True if value is populated, False if it's None, empty, or effectively empty.
    """
    if value is None:
        return False
    if isinstance(value, str) and value.strip() == "":
        return False
    if isinstance(value, (list, tuple)):
        return any(is_populated(v) for v in value)
    if isinstance(value, dict):
        return any(is_populated(v) for v in value.values())
    return True  # number, bool, LinkML objects, etc.


def populated_top_level_keys(schema_view: SchemaView) -> Set[str]:
    """Extract top-level keys from a SchemaView that have populated values.
    
    This function checks both the raw schema attributes and the merged/resolved
    collections accessible via all_* methods to get a complete picture.
    
    Args:
        schema_view: SchemaView instance to analyze.
        
    Returns:
        Set of top-level keys whose values are populated.
    """
    keys = set()
    
    # Check raw schema attributes first
    schema_dict = schema_view.schema._as_dict
    for k, v in schema_dict.items():
        if is_populated(v):
            keys.add(k)
    
    # Check merged/resolved collections via all_* methods
    schema_collections = {
        'classes': lambda: schema_view.all_classes(imports=True),
        'slots': lambda: schema_view.all_slots(imports=True),
        'enums': lambda: schema_view.all_enums(imports=True),
        'types': lambda: schema_view.all_types(imports=True),
        'subsets': lambda: schema_view.all_subsets(imports=True),
    }
    
    for key_name, method in schema_collections.items():
        try:
            result = method()
            if is_populated(result):
                keys.add(key_name)
        except (AttributeError, TypeError):
            # Skip if method doesn't exist or fails
            pass
    
    return keys


def find_element_differences(old_element, new_element, element_type: str) -> List[str]:
    """Find differences between two LinkML elements (enum, class, slot) and return as list of strings."""
    differences = []
    
    # Dynamically discover all attributes from both objects
    old_attrs = set(dir(old_element)) if old_element else set()
    new_attrs = set(dir(new_element)) if new_element else set()
    
    # Element-specific attributes to exclude (complex objects we'll handle separately)
    element_specific_exclusions = {
        'enum': {'permissible_values', 'values'},
        'class': {'slots', 'slot_usage', 'attributes'},
        'slot': {'structured_pattern', 'annotations'}
    }
    
    # Filter out private/internal attributes, methods, and known complex attributes
    excluded_attrs = {
        # Private/internal
        attr for attr in (old_attrs | new_attrs) if attr.startswith('_')
    } | {
        # Obvious differences we don't need to report
        'name', 'from_schema'  # These are expected to differ in mappings
    } | element_specific_exclusions.get(element_type, set())
    
    all_attrs = (old_attrs | new_attrs) - excluded_attrs
    
    # Further filter out callable methods
    all_attrs = {
        attr for attr in all_attrs 
        if not (callable(getattr(old_element, attr, None)) or callable(getattr(new_element, attr, None)))
    }
    
    for attr in sorted(all_attrs):
        old_val = getattr(old_element, attr, None)
        new_val = getattr(new_element, attr, None)
        
        # Only report scalar/simple values that differ and at least one is non-empty
        if old_val != new_val and (old_val or new_val):
            # Skip complex objects like dicts, lists for now (we'll handle those separately)
            if not isinstance(old_val, (dict, list)) and not isinstance(new_val, (dict, list)):
                old_display = repr(old_val) if old_val else "None"
                new_display = repr(new_val) if new_val else "None"
                differences.append(f"{attr}: {old_display} vs {new_display}")
    
    return differences


def find_enum_differences(old_enum, new_enum) -> List[str]:
    """Find differences between two enum definitions and return as list of strings."""
    return find_element_differences(old_enum, new_enum, 'enum')


def find_class_differences(old_class, new_class) -> List[str]:
    """Find differences between two class definitions and return as list of strings."""
    return find_element_differences(old_class, new_class, 'class')


def find_slot_differences(old_slot, new_slot) -> List[str]:
    """Find differences between two slot definitions and return as list of strings."""
    return find_element_differences(old_slot, new_slot, 'slot')


def compare_enum_metadata(enum_name: str, old_enum, new_enum, old_info: Dict[str, Any], new_info: Dict[str, Any]) -> None:
    """Compare scalar metadata between two enum definitions."""
    print(f"        {enum_name}: comparing metadata")
    
    differences = find_enum_differences(old_enum, new_enum)
    if differences:
        for diff in differences:
            print(f"          {diff}")
    else:
        print(f"          No scalar metadata differences found")


def analyze_slot_settings_usage(schema_view: SchemaView) -> Dict[str, any]:
    """Analyze which slots use which settings in structured_pattern.syntax.
    
    Returns:
        Dict with keys:
        - 'settings_usage': Dict mapping setting names to lists of slot names that use them
        - 'pattern_usage': Dict mapping full patterns to lists of slot names that use them  
        - 'undefined_settings': Set of setting names used but not defined
        - 'unused_settings': Set of setting names defined but not used
    """
    import re
    
    settings_usage = {}  # setting_name -> [slot_names]
    pattern_usage = {}   # full_pattern -> [slot_names]
    all_referenced_settings = set()
    
    try:
        # Get all defined settings
        defined_settings = set()
        try:
            all_settings = schema_view.schema.settings
            if all_settings:
                defined_settings = set(all_settings.keys())
        except (AttributeError, TypeError):
            pass
        
        # Parse all slots for structured patterns
        all_slots = schema_view.all_slots(imports=True)
        for slot_name, slot_def in all_slots.items():
            if hasattr(slot_def, 'structured_pattern') and slot_def.structured_pattern:
                if hasattr(slot_def.structured_pattern, 'syntax') and slot_def.structured_pattern.syntax:
                    syntax_value = slot_def.structured_pattern.syntax
                    
                    # Track full pattern usage
                    if syntax_value not in pattern_usage:
                        pattern_usage[syntax_value] = []
                    pattern_usage[syntax_value].append(slot_name)
                    
                    # Extract setting names from {setting_name} patterns
                    setting_references = re.findall(r'\{([^}]+)\}', syntax_value)
                    for setting_name in setting_references:
                        all_referenced_settings.add(setting_name)
                        if setting_name not in settings_usage:
                            settings_usage[setting_name] = []
                        if slot_name not in settings_usage[setting_name]:  # Avoid duplicates
                            settings_usage[setting_name].append(slot_name)
        
        # Convert lists to sets to remove duplicates, then back to sorted lists
        for setting_name in settings_usage:
            settings_usage[setting_name] = sorted(list(set(settings_usage[setting_name])))
        
        for pattern in pattern_usage:
            pattern_usage[pattern] = sorted(list(set(pattern_usage[pattern])))
        
        # Find undefined and unused settings
        undefined_settings = all_referenced_settings - defined_settings
        unused_settings = defined_settings - all_referenced_settings
        
    except Exception as e:
        print(f"Error analyzing slot settings usage: {e}")
        return {
            'settings_usage': {},
            'pattern_usage': {},
            'undefined_settings': set(),
            'unused_settings': set()
        }
    
    return {
        'settings_usage': settings_usage,
        'pattern_usage': pattern_usage,
        'undefined_settings': undefined_settings,
        'unused_settings': unused_settings
    }


def diff_top_keys(schema1_view: SchemaView, schema2_view: SchemaView) -> Tuple[Set[str], Set[str]]:
    """Compare top-level keys between two schemas.
    
    Args:
        schema1_view: First SchemaView to compare.
        schema2_view: Second SchemaView to compare.
        
    Returns:
        Tuple of (only_in_1, only_in_2) where each is a set of keys that are
        populated in one schema but missing or empty in the other.
    """
    s1_keys = populated_top_level_keys(schema1_view)
    s2_keys = populated_top_level_keys(schema2_view)
    only_in_1 = s1_keys - s2_keys
    only_in_2 = s2_keys - s1_keys
    return only_in_1, only_in_2



def validate_github_token(token: str) -> bool:
    """Validate GitHub token format.
    
    Args:
        token: GitHub token to validate.
        
    Returns:
        True if token format is valid, False otherwise.
    """
    # GitHub personal access tokens patterns
    patterns = [
        r'^ghp_[a-zA-Z0-9]{36}$',  # Personal access token
        r'^gho_[a-zA-Z0-9]{36}$',  # OAuth token
        r'^ghu_[a-zA-Z0-9]{36}$',  # User token
        r'^ghs_[a-zA-Z0-9]{36}$',  # Server token
        r'^github_pat_[a-zA-Z0-9_]{82}$',  # Fine-grained personal access token
    ]

    return any(re.match(pattern, token) for pattern in patterns)


def get_github_headers() -> Dict[str, str]:
    """Get GitHub API headers with authentication if available.
    
    Returns:
        Dict containing Authorization header if token is available, empty dict otherwise.
    """
    global AUTH_MESSAGE_PRINTED
    
    env_file = Path(__file__).parent.parent.parent / 'local' / '.env'
    if env_file.exists():
        load_dotenv(env_file)

    headers = {}
    if token := os.getenv('GITHUB_TOKEN'):
        if validate_github_token(token):
            headers['Authorization'] = f'token {token}'
            if VERBOSE_AUTH or not AUTH_MESSAGE_PRINTED:
                print("Using authenticated GitHub API")
                AUTH_MESSAGE_PRINTED = True
        else:
            if VERBOSE_AUTH or not AUTH_MESSAGE_PRINTED:
                print("WARNING: Invalid GitHub token format detected, using unauthenticated API")
                print("Using unauthenticated GitHub API (rate limited)")
                AUTH_MESSAGE_PRINTED = True
    else:
        if VERBOSE_AUTH or not AUTH_MESSAGE_PRINTED:
            print("Using unauthenticated GitHub API (rate limited)")
            AUTH_MESSAGE_PRINTED = True
    return headers


def fetch_tree(commit_sha: str) -> List[str]:
    """Fetch recursive tree from GitHub API and return YAML files.
    
    Args:
        commit_sha: Git commit SHA to fetch tree for.
        
    Returns:
        List of paths to YAML files in the repository at the given commit.
    """
    global API_CALL_COUNT
    headers = get_github_headers()
    url = f"https://api.github.com/repos/GenomicsStandardsConsortium/mixs/git/trees/{commit_sha}?recursive=1"
    response = requests.get(url, headers=headers, timeout=10)
    API_CALL_COUNT += 1
    response.raise_for_status()
    tree = response.json()

    yaml_files = [item['path'] for item in tree['tree']
                  if item['path'].endswith(('.yaml', '.yml'))]
    return yaml_files


def find_mixs_yaml_path(yaml_files: List[str], approved_dirs: Optional[List[str]] = None) -> Optional[str]:
    """Find mixs.yaml file in approved directories.
    
    Args:
        yaml_files: List of YAML file paths to search through.
        approved_dirs: List of approved directory names to search in. 
                      Defaults to APPROVED_DIRS constant.
                      
    Returns:
        Path to mixs.yaml file if found in approved directories, None otherwise.
    """
    if approved_dirs is None:
        approved_dirs = APPROVED_DIRS

    for yaml_file in yaml_files:
        if yaml_file.endswith('mixs.yaml'):
            for approved_dir in approved_dirs:
                if yaml_file.startswith(f'{approved_dir}/'):
                    return yaml_file
    return None


def get_releases() -> List[Tuple[str, datetime]]:
    """Get releases from GitHub API with pagination support.
    
    Returns:
        List of tuples containing (tag_name, published_date) for each release.
    """
    global API_CALL_COUNT
    headers = get_github_headers()
    url = "https://api.github.com/repos/GenomicsStandardsConsortium/mixs/releases"

    release_info = []
    page = 1

    while True:
        paginated_url = f"{url}?page={page}&per_page=100"
        response = requests.get(paginated_url, headers=headers, timeout=10)
        API_CALL_COUNT += 1
        response.raise_for_status()
        releases = response.json()

        # If no releases returned, we've reached the end
        if not releases:
            break

        for release in releases:
            tag = release['tag_name']
            date = datetime.fromisoformat(release['published_at'].replace('Z', '+00:00'))
            release_info.append((tag, date))

        page += 1

    return release_info


def get_yaml_files_from_release(tag: str) -> Tuple[List[str], str]:
    """Get list of YAML files and commit SHA from a specific release tag.
    
    Args:
        tag: Release tag name to fetch files for.
        
    Returns:
        Tuple of (yaml_files, commit_sha) where yaml_files is a list of YAML file paths
        and commit_sha is the full commit hash for the tag.
    """
    global API_CALL_COUNT
    headers = get_github_headers()
    # Get commit SHA for the tag
    url = f"https://api.github.com/repos/GenomicsStandardsConsortium/mixs/git/refs/tags/{tag}"
    response = requests.get(url, headers=headers, timeout=10)
    API_CALL_COUNT += 1
    response.raise_for_status()
    commit_sha = response.json()['object']['sha']

    yaml_files = fetch_tree(commit_sha)
    return yaml_files, commit_sha


def get_main_branch_info() -> Tuple[List[str], str, datetime]:
    """Get YAML files and commit info from main branch.
    
    Returns:
        Tuple of (yaml_files, commit_sha, commit_date) where yaml_files is a list
        of YAML file paths, commit_sha is the full commit hash, and commit_date
        is the datetime of the commit.
    """
    global API_CALL_COUNT
    headers = get_github_headers()
    # Get main branch commit
    url = "https://api.github.com/repos/GenomicsStandardsConsortium/mixs/branches/main"
    response = requests.get(url, headers=headers, timeout=10)
    API_CALL_COUNT += 1
    response.raise_for_status()
    branch_info = response.json()

    commit_sha = branch_info['commit']['sha']
    commit_date = datetime.fromisoformat(branch_info['commit']['commit']['author']['date'].replace('Z', '+00:00'))

    yaml_files = fetch_tree(commit_sha)
    return yaml_files, commit_sha, commit_date


def get_raw_schema_url(commit_hash: str, mixs_yaml_path: Optional[str]) -> Optional[str]:
    """Get raw GitHub URL for a mixs.yaml file at a specific commit.
    
    Args:
        commit_hash: Git commit hash.
        mixs_yaml_path: Path to mixs.yaml file within the repository.
        
    Returns:
        Raw GitHub URL to the schema file, or None if no path provided.
    """
    if not mixs_yaml_path:
        return None
    return f"https://raw.githubusercontent.com/GenomicsStandardsConsortium/mixs/{commit_hash}/{mixs_yaml_path}"


def build_full_release_info() -> Dict[str, Dict[str, Any]]:
    """Build comprehensive release info dictionary for all releases and main branch.
    
    Returns:
        Dict mapping short commit hashes to release metadata with commit_sha included.
    """
    releases = get_releases()
    release_info = {}

    # Build release info dict
    for tag, date in releases:
        yaml_files, commit_sha = get_yaml_files_from_release(tag)
        short_hash = commit_sha[:7]
        mixs_yaml_path = find_mixs_yaml_path(yaml_files)

        release_info[short_hash] = {
            'tag': tag,
            'date': date.strftime('%Y-%m-%d'),
            'mixs_yaml_path': mixs_yaml_path,
            'commit_sha': commit_sha
        }

    # Add main branch info
    yaml_files, commit_sha, commit_date = get_main_branch_info()
    short_hash = commit_sha[:7]
    mixs_yaml_path = find_mixs_yaml_path(yaml_files)

    release_info[short_hash] = {
        'tag': 'main',
        'date': commit_date.strftime('%Y-%m-%d'),
        'mixs_yaml_path': mixs_yaml_path,
        'commit_sha': commit_sha
    }

    return release_info


def load_schema_views(old_commit: str = DEFAULT_OLD_COMMIT,
                      new_commit: str = DEFAULT_NEW_COMMIT) -> Tuple[
    SchemaView, SchemaView, Dict[str, Any], Dict[str, Any]]:
    """Load SchemaView objects for old and new commits.
    
    Args:
        old_commit: Short commit hash for the old schema version.
        new_commit: Short commit hash for the new schema version.
        
    Returns:
        Tuple of (old_schema, new_schema, old_info, new_info) where:
        - old_schema, new_schema: SchemaView objects for the schemas
        - old_info, new_info: Dict with release metadata (tag, date, etc.)
        
    Raises:
        ValueError: If specified commits are not found or have no mixs.yaml file.
    """
    release_info = build_full_release_info()

    # Get schema info for specified commits
    old_info = release_info.get(old_commit)
    new_info = release_info.get(new_commit)

    if not old_info:
        raise ValueError(f"Old commit {old_commit} not found in releases")
    if not new_info:
        raise ValueError(f"New commit {new_commit} not found in releases")

    # Get raw URLs
    old_url = get_raw_schema_url(old_info['commit_sha'], old_info['mixs_yaml_path'])
    new_url = get_raw_schema_url(new_info['commit_sha'], new_info['mixs_yaml_path'])

    if not old_url:
        raise ValueError(f"No mixs.yaml found for old commit {old_commit} ({old_info['tag']})")
    if not new_url:
        raise ValueError(f"No mixs.yaml found for new commit {new_commit} ({new_info['tag']})")

    print(f"Loading old schema: {old_info['tag']} ({old_commit})")
    print(f"  URL: {old_url}")
    old_schema = SchemaView(old_url)

    print(f"Loading new schema: {new_info['tag']} ({new_commit})")
    print(f"  URL: {new_url}")
    new_schema = SchemaView(new_url)

    return old_schema, new_schema, old_info, new_info


def print_releases() -> None:
    """Print all releases with tag and date."""
    releases = get_releases()
    for tag, date in releases:
        print(f"{tag}: {date.strftime('%Y-%m-%d')}")


def build_release_info_dict() -> Dict[str, Dict[str, Any]]:
    """Build release info dictionary with all releases and main branch info (with optional display output).
    
    Returns:
        Dict mapping short commit hashes to release metadata.
    """
    release_info = build_full_release_info()

    if SHOW_YAML_FILES:
        # Print output for each release (excluding main for now)
        releases = get_releases()
        for tag, date in releases:
            yaml_files, commit_sha = get_yaml_files_from_release(tag)
            short_hash = commit_sha[:7]

            print(f"\n{tag}: {date.strftime('%Y-%m-%d')} ({short_hash})")
            for yaml_file in yaml_files:
                print(f"  {yaml_file}")

        # Add main branch info display
        yaml_files, commit_sha, commit_date = get_main_branch_info()
        short_hash = commit_sha[:7]

        print(f"\nmain: {commit_date.strftime('%Y-%m-%d')} ({short_hash})")
        for yaml_file in yaml_files:
            print(f"  {yaml_file}")

    # Return the simplified dict (without commit_sha for backward compatibility)
    return {k: {key: val for key, val in v.items() if key != 'commit_sha'}
            for k, v in release_info.items()}


def compare_scalar_values(key: str, old_value, new_value, old_info: Dict[str, Any], new_info: Dict[str, Any]) -> None:
    """Compare and print scalar values."""
    print(f"    {key}:")
    print(f"      {old_info['tag']}: {old_value}")
    print(f"      {new_info['tag']}: {new_value}")


def compare_list_values(key: str, old_value, new_value, old_info: Dict[str, Any], new_info: Dict[str, Any]) -> None:
    """Compare and print list/tuple values as sets."""
    # Keys that should never be truncated
    no_truncate_keys = {'imports', 'settings'}
    
    try:
        old_set = set(old_value)
        new_set = set(new_value)
        only_in_old = old_set - new_set
        only_in_new = new_set - old_set
        
        print(f"    {key}:")
        if only_in_old:
            print(f"      Only in {old_info['tag']} ({len(only_in_old)} items):")
            if key in no_truncate_keys or len(only_in_old) <= 20:
                for item in sorted(only_in_old):
                    print(f"        {item}")
            else:
                for item in list(sorted(only_in_old))[:20]:
                    print(f"        {item}")
                print(f"        ... and {len(only_in_old) - 20} more")
                
        if only_in_new:
            print(f"      Only in {new_info['tag']} ({len(only_in_new)} items):")
            if key in no_truncate_keys or len(only_in_new) <= 20:
                for item in sorted(only_in_new):
                    print(f"        {item}")
            else:
                for item in list(sorted(only_in_new))[:20]:
                    print(f"        {item}")
                print(f"        ... and {len(only_in_new) - 20} more")
    except TypeError:
        # Items not hashable, fall back to showing type/size info
        print(f"    {key}:")
        print(f"      {old_info['tag']}: {type(old_value).__name__} (size: {len(old_value)})")
        print(f"      {new_info['tag']}: {type(new_value).__name__} (size: {len(new_value)})")


def filter_mixs_compliant_slots(schema_view: SchemaView, slot_dict: Dict) -> Tuple[Dict, int]:
    """Filter out slots with domain 'MixsCompliantData' and return filtered dict and count."""
    filtered_slots = {}
    mixs_compliant_count = 0
    
    for slot_name, slot_def in slot_dict.items():
        try:
            # Get the slot definition from SchemaView to check domain
            slot_obj = schema_view.get_slot(slot_name)
            if slot_obj and hasattr(slot_obj, 'domain') and slot_obj.domain == 'MixsCompliantData':
                mixs_compliant_count += 1
            else:
                filtered_slots[slot_name] = slot_def
        except:
            # If we can't get slot info, include it in the comparison
            filtered_slots[slot_name] = slot_def
    
    return filtered_slots, mixs_compliant_count


def compare_schema_elements(key: str, old_value: Dict, new_value: Dict, old_info: Dict[str, Any], new_info: Dict[str, Any], 
                          mappings: Dict[str, str] = None, show_all_flag: bool = False, 
                          old_schema: SchemaView = None, new_schema: SchemaView = None) -> None:
    """Unified comparison function for classes, enums, and slots."""
    
    old_keys = set(old_value.keys())
    new_keys = set(new_value.keys())
    
    print(f"      Total old {key}: {len(old_keys)}, Total new {key}: {len(new_keys)}")
    
    # Apply mappings if available
    if mappings:
        unique_old, unique_new, expected_mappings = filter_expected_name_changes(
            old_keys, new_keys, mappings
        )
        
        print(f"      Expected {key} name changes ({len(expected_mappings)} mappings):")
        if show_all_flag and len(expected_mappings) <= 50:
            for mapping in sorted(expected_mappings):
                print(f"        {mapping}")
        elif len(expected_mappings) <= 10:
            for mapping in sorted(expected_mappings):
                print(f"        {mapping}")
        else:
            print(f"        [Many expected mappings: showing first 10]")
            for mapping in list(sorted(expected_mappings))[:10]:
                print(f"        {mapping}")
            print(f"        ... and {len(expected_mappings) - 10} more expected mappings")
        
        # Compare mapped elements for detailed differences
        if key in ['enums', 'classes', 'slots']:
            print(f"      Comparing mapped {key} definitions:")
            mapped_differences = []
            
            # Choose the appropriate comparison function
            if key == 'enums':
                diff_func = find_enum_differences
            elif key == 'classes':
                diff_func = find_class_differences
            else:  # slots
                diff_func = find_slot_differences
            
            # Compare ALL mapped elements
            for old_name, new_name in sorted(mappings.items()):
                if old_name in old_value and new_name in new_value:
                    # Capture differences without printing immediately
                    old_element = old_value[old_name]
                    new_element = new_value[new_name]
                    differences = diff_func(old_element, new_element)
                    if differences:
                        mapped_differences.append((f"{old_name} -> {new_name}", differences))
            
            # Display results with limits
            if mapped_differences:
                display_limit = 10
                for i, (mapping_name, differences) in enumerate(mapped_differences):
                    if i < display_limit:
                        print(f"        {mapping_name}: has differences")
                        for diff in differences:
                            print(f"          {diff}")
                    else:
                        break
                
                if len(mapped_differences) > display_limit:
                    print(f"        ... and {len(mapped_differences) - display_limit} more mapped {key} with differences")
                print(f"        Total mapped {key} compared: {len(mappings)}, with differences: {len(mapped_differences)}")
            else:
                print(f"        All {len(mappings)} mapped {key} have identical metadata")
        
        only_in_old_keys = unique_old
        only_in_new_keys = unique_new
    else:
        only_in_old_keys = old_keys - new_keys
        only_in_new_keys = new_keys - old_keys
    
    # Apply inter-type refactoring filtering
    element_type_map = {'classes': 'class', 'enums': 'enum', 'slots': 'slot', 'subsets': 'subset'}
    if key in element_type_map and INTER_TYPE_REFACTORING:
        element_type = element_type_map[key]
        filtered_old, filtered_new, refactoring_found = filter_inter_type_refactoring(
            element_type, only_in_old_keys, only_in_new_keys, INTER_TYPE_REFACTORING
        )
        
        if refactoring_found:
            print(f"      Expected inter-type refactoring ({len(refactoring_found)} transformations):")
            for refactoring in sorted(refactoring_found):
                print(f"        {refactoring}")
        
        only_in_old_keys = filtered_old
        only_in_new_keys = filtered_new
    
    shared_keys = old_keys & new_keys
    
    # Show unique differences
    print(f"      Unique {key} only in {old_info['tag']}: {len(only_in_old_keys)}")
    if only_in_old_keys:
        if key == 'enums' and old_schema:
            show_enum_slot_associations(only_in_old_keys, old_schema, old_info['tag'])
        elif key == 'slots' and old_schema:
            show_slot_class_associations(only_in_old_keys, old_schema, old_info['tag'])
        else:
            show_all = show_all_flag or len(only_in_old_keys) <= 50
            if show_all:
                for k in sorted(only_in_old_keys):
                    print(f"        {k}")
            else:
                print(f"        [LARGE DIFF: {len(only_in_old_keys)} {key} - showing sample]")
                for k in list(sorted(only_in_old_keys))[:10]:
                    print(f"        {k}")
                print(f"        ... and {len(only_in_old_keys) - 10} more")
        
    print(f"      Unique {key} only in {new_info['tag']}: {len(only_in_new_keys)}")
    if only_in_new_keys:
        if key == 'enums' and new_schema:
            show_enum_slot_associations(only_in_new_keys, new_schema, new_info['tag'])
        elif key == 'slots' and new_schema:
            show_slot_class_associations(only_in_new_keys, new_schema, new_info['tag'])
        else:
            show_all = show_all_flag or len(only_in_new_keys) <= 50
            if show_all:
                for k in sorted(only_in_new_keys):
                    print(f"        {k}")
            else:
                print(f"        [LARGE DIFF: {len(only_in_new_keys)} {key} - showing sample]")
                for k in list(sorted(only_in_new_keys))[:10]:
                    print(f"        {k}")
                print(f"        ... and {len(only_in_new_keys) - 10} more")
    
    # Show shared elements with different definitions
    if shared_keys:
        changed_keys = [k for k in shared_keys if old_value[k] != new_value[k]]
        if changed_keys and len(changed_keys) <= 10:
            definition_word = "definitions" if key in ['classes', 'enums', 'slots'] else "values"
            print(f"      Shared {key} with different {definition_word} ({len(changed_keys)} {key}):")
            for k in sorted(changed_keys):
                if key == 'enums':
                    # Detailed enum comparison
                    differences = find_enum_differences(old_value[k], new_value[k])
                    if differences:
                        print(f"        {k}: has differences")
                        for diff in differences:
                            print(f"          {diff}")
                    else:
                        print(f"        {k}: no scalar metadata differences")
                elif key == 'classes':
                    # Detailed class comparison
                    differences = find_class_differences(old_value[k], new_value[k])
                    if differences:
                        print(f"        {k}: has differences")
                        for diff in differences:
                            print(f"          {diff}")
                    else:
                        print(f"        {k}: no scalar metadata differences")
                elif key == 'slots':
                    # Detailed slot comparison
                    differences = find_slot_differences(old_value[k], new_value[k])
                    if differences:
                        print(f"        {k}: has differences")
                        for diff in differences:
                            print(f"          {diff}")
                    else:
                        print(f"        {k}: no scalar metadata differences")
                elif key == 'prefixes':
                    # Special formatting for prefix objects
                    old_prefix = old_value[k]
                    new_prefix = new_value[k]
                    
                    # Extract meaningful parts from Prefix objects
                    old_ref = getattr(old_prefix, 'prefix_reference', old_prefix)
                    new_ref = getattr(new_prefix, 'prefix_reference', new_prefix)
                    
                    print(f"        {k}: {old_info['tag']}='{old_ref}' vs {new_info['tag']}='{new_ref}'")
                else:
                    print(f"        {k}: {old_info['tag']}={old_value[k]!r} vs {new_info['tag']}={new_value[k]!r}")
        elif changed_keys:
            definition_word = "definitions" if key in ['classes', 'enums', 'slots'] else "values"
            print(f"      {len(changed_keys)} shared {key} have different {definition_word} (too many to show)")


def compare_dict_values(key: str, old_value, new_value, old_info: Dict[str, Any], new_info: Dict[str, Any], old_schema: SchemaView = None, new_schema: SchemaView = None) -> None:
    """Compare and print dictionary values by comparing keys."""
    # Special handling for slots - filter out MixsCompliantData domain slots
    if key == 'slots':
        # We need access to the schema views, but they're not passed here
        # For now, just note this in the output and handle normally
        print(f"    {key} (Note: MixsCompliantData domain slots not filtered in this view):")
    else:
        print(f"    {key}:")
    
    # Use unified comparison for schema elements
    if key == 'classes':
        compare_schema_elements(key, old_value, new_value, old_info, new_info, 
                              CLASS_NAME_MAPPINGS, SHOW_ALL_CLASS_NAMES, old_schema, new_schema)
    elif key == 'enums':
        compare_schema_elements(key, old_value, new_value, old_info, new_info,
                              ENUM_NAME_MAPPINGS, SHOW_ALL_ENUM_NAMES, old_schema, new_schema)
    elif key == 'slots':
        # Note: Slots have special filtering that happens in compare_slots_with_filtering
        # This branch shouldn't be reached for slots in normal operation
        compare_schema_elements(key, old_value, new_value, old_info, new_info,
                              SLOT_NAME_MAPPINGS, SHOW_ALL_SLOT_NAMES, old_schema, new_schema)
    elif key == 'subsets':
        compare_schema_elements(key, old_value, new_value, old_info, new_info,
                              SUBSET_NAME_MAPPINGS, True, old_schema, new_schema)
    else:
        # Original logic for non-schema element keys
        old_keys = set(old_value.keys())
        new_keys = set(new_value.keys())
        only_in_old_keys = old_keys - new_keys
        only_in_new_keys = new_keys - old_keys
        shared_keys = old_keys & new_keys
        
        show_all_keys = len(only_in_old_keys) <= 50
        
        if only_in_old_keys:
            print(f"      Keys only in {old_info['tag']} ({len(only_in_old_keys)} keys):")
            if show_all_keys:
                for k in sorted(only_in_old_keys):
                    print(f"        {k}")
            else:
                print(f"        [LARGE DIFF: {len(only_in_old_keys)} keys - showing sample]")
                for k in list(sorted(only_in_old_keys))[:10]:
                    print(f"        {k}")
                print(f"        ... and {len(only_in_old_keys) - 10} more")
        
        show_all_new_keys = len(only_in_new_keys) <= 50
                
        if only_in_new_keys:
            print(f"      Keys only in {new_info['tag']} ({len(only_in_new_keys)} keys):")
            if show_all_new_keys:
                for k in sorted(only_in_new_keys):
                    print(f"        {k}")
            else:
                print(f"        [LARGE DIFF: {len(only_in_new_keys)} keys - showing sample]")
                for k in list(sorted(only_in_new_keys))[:10]:
                    print(f"        {k}")
                print(f"        ... and {len(only_in_new_keys) - 10} more")
        
        if shared_keys:
            changed_keys = [k for k in shared_keys if old_value[k] != new_value[k]]
            if changed_keys and len(changed_keys) <= 10:
                print(f"      Shared keys with different values ({len(changed_keys)} keys):")
                for k in sorted(changed_keys):
                    if key == 'prefixes':
                        # Special formatting for prefix objects
                        old_prefix = old_value[k]
                        new_prefix = new_value[k]
                        
                        # Extract meaningful parts from Prefix objects
                        old_ref = getattr(old_prefix, 'prefix_reference', old_prefix)
                        new_ref = getattr(new_prefix, 'prefix_reference', new_prefix)
                        
                        print(f"        {k}: {old_info['tag']}='{old_ref}' vs {new_info['tag']}='{new_ref}'")
                    else:
                        print(f"        {k}: {old_info['tag']}={old_value[k]!r} vs {new_info['tag']}={new_value[k]!r}")
            elif changed_keys:
                print(f"      {len(changed_keys)} shared keys have different values (too many to show)")


def show_enum_slot_associations(enum_names: Set[str], schema_view: SchemaView, schema_tag: str) -> None:
    """Show which slots use the given enums."""
    for enum_name in sorted(enum_names):
        try:
            slots_using_enum = schema_view.get_slots_by_enum(enum_name)
            if slots_using_enum:
                slot_names = [slot.name for slot in slots_using_enum]
                print(f"        {enum_name} (used by {len(slot_names)} slots: {', '.join(sorted(slot_names))})")
            else:
                print(f"        {enum_name} (no slots use this enum)")
        except Exception as e:
            print(f"        {enum_name} (error checking slot associations: {e})")


def show_slot_class_associations(slot_names: Set[str], schema_view: SchemaView, schema_tag: str) -> None:
    """Show which classes use the given slots."""
    for slot_name in sorted(slot_names):
        try:
            slot_obj = schema_view.get_slot(slot_name)
            if slot_obj:
                classes_using_slot = schema_view.get_classes_by_slot(slot_obj)
                
                # Check if slot is abstract
                is_abstract = getattr(slot_obj, 'abstract', False)
                abstract_note = " [ABSTRACT]" if is_abstract else ""
                
                if classes_using_slot:
                    # classes_using_slot is already a list of class name strings
                    print(f"        {slot_name}{abstract_note} (used by {len(classes_using_slot)} classes: {', '.join(sorted(classes_using_slot))})")
                else:
                    print(f"        {slot_name}{abstract_note} (no classes use this slot)")
            else:
                print(f"        {slot_name} (slot not found)")
        except Exception as e:
            print(f"        {slot_name} (error checking class usage: {e})")


def compare_slots_with_filtering(old_value, new_value, old_schema: SchemaView, new_schema: SchemaView, old_info: Dict[str, Any], new_info: Dict[str, Any]) -> None:
    """Compare slot dictionaries with MixsCompliantData domain filtering."""
    # Filter out MixsCompliantData domain slots
    old_filtered, old_mixs_count = filter_mixs_compliant_slots(old_schema, old_value)
    new_filtered, new_mixs_count = filter_mixs_compliant_slots(new_schema, new_value)
    
    print(f"    slots:")
    print(f"      Filtered out {old_mixs_count} MixsCompliantData domain slots from {old_info['tag']}")
    print(f"      Filtered out {new_mixs_count} MixsCompliantData domain slots from {new_info['tag']}")
    
    # Use the unified comparison function for consistency
    compare_schema_elements('slots', old_filtered, new_filtered, old_info, new_info,
                          SLOT_NAME_MAPPINGS, SHOW_ALL_SLOT_NAMES, old_schema, new_schema)


def compare_key_values(key: str, old_value, new_value, old_info: Dict[str, Any], new_info: Dict[str, Any], old_schema: SchemaView = None, new_schema: SchemaView = None) -> None:
    """Compare two values for a given key and print differences."""
    # Special handling for slots with domain filtering
    if key == 'slots' and old_schema and new_schema and isinstance(old_value, dict) and isinstance(new_value, dict):
        compare_slots_with_filtering(old_value, new_value, old_schema, new_schema, old_info, new_info)
        return
    
    # Handle scalars
    if not isinstance(old_value, (dict, list, tuple)) and not isinstance(new_value, (dict, list, tuple)):
        compare_scalar_values(key, old_value, new_value, old_info, new_info)
        return
    
    # Handle lists/tuples
    if isinstance(old_value, (list, tuple)) and isinstance(new_value, (list, tuple)):
        compare_list_values(key, old_value, new_value, old_info, new_info)
        return
    
    # Handle dictionaries
    if isinstance(old_value, dict) and isinstance(new_value, dict):
        compare_dict_values(key, old_value, new_value, old_info, new_info, old_schema, new_schema)
        return
    
    # Fallback for mixed types
    print(f"    {key}:")
    print(f"      {old_info['tag']}: {type(old_value).__name__} (size: {len(old_value) if hasattr(old_value, '__len__') else 'N/A'})")
    print(f"      {new_info['tag']}: {type(new_value).__name__} (size: {len(new_value) if hasattr(new_value, '__len__') else 'N/A'})")


def compare_schema_values(old_schema: SchemaView, new_schema: SchemaView,
                          old_info: Dict[str, Any], new_info: Dict[str, Any]) -> None:
    """Compare values that are populated in one schema but not in the other.

    Args:
        old_schema: SchemaView for the old schema version
        new_schema: SchemaView for the new schema version
        old_info: Metadata about the old schema
        new_info: Metadata about the new schema
    """
    print("\n" + "=" * 50)
    print("Schema Value Comparison (Populated in one, empty in other)")
    print("=" * 50)

    # Track keys that have different population status
    old_populated_new_empty = []
    new_populated_old_empty = []

    # Check method-based attributes (all_* methods) - these access the merged schema
    all_methods = set()
    for method_name in dir(old_schema):
        if method_name.startswith('all_') and callable(getattr(old_schema, method_name)):
            all_methods.add(method_name)

    for method_name in dir(new_schema):
        if method_name.startswith('all_') and callable(getattr(new_schema, method_name)):
            all_methods.add(method_name)

    # Process all discovered methods across both schemas
    for method_name in sorted(all_methods):
        key_name = method_name[4:]  # Remove 'all_' prefix

        try:
            old_value = getattr(old_schema, method_name)() if hasattr(old_schema, method_name) else None
            new_value = getattr(new_schema, method_name)() if hasattr(new_schema, method_name) else None

            old_populated = is_populated(old_value)
            new_populated = is_populated(new_value)

            if old_populated and not new_populated:
                old_populated_new_empty.append((key_name, old_value))
            elif new_populated and not old_populated:
                new_populated_old_empty.append((key_name, new_value))
        except:
            # Skip methods that fail to call
            pass

    # Also check direct attributes from both schemas
    all_attrs = set()
    for attr_name in dir(old_schema.schema):
        if not attr_name.startswith('_') and not callable(getattr(old_schema.schema, attr_name)):
            all_attrs.add(attr_name)

    for attr_name in dir(new_schema.schema):
        if not attr_name.startswith('_') and not callable(getattr(new_schema.schema, attr_name)):
            all_attrs.add(attr_name)

    for attr_name in sorted(all_attrs):
        old_value = getattr(old_schema.schema, attr_name, None)
        new_value = getattr(new_schema.schema, attr_name, None)

        old_populated = is_populated(old_value)
        new_populated = is_populated(new_value)

        if old_populated and not new_populated:
            old_populated_new_empty.append((attr_name, old_value))
        elif new_populated and not old_populated:
            new_populated_old_empty.append((attr_name, new_value))

    # Print results
    print(f"\nKeys populated in {old_info['tag']} but empty in {new_info['tag']}: {len(old_populated_new_empty)}")
    for key, value in sorted(old_populated_new_empty, key=lambda x: x[0]):
        print(f"  {key}:")
        if isinstance(value, dict) and len(value) > 5:
            print(f"    {len(value)} items")
        elif isinstance(value, (list, tuple)) and len(value) > 5:
            print(f"    {len(value)} items")
        else:
            pprint.pprint(value, indent=4, depth=1, width=80)

    print(f"\nKeys populated in {new_info['tag']} but empty in {old_info['tag']}: {len(new_populated_old_empty)}")
    for key, value in sorted(new_populated_old_empty, key=lambda x: x[0]):
        print(f"  {key}:")
        if isinstance(value, dict) and len(value) > 5:
            print(f"    {len(value)} items")
        elif isinstance(value, (list, tuple)) and len(value) > 5:
            print(f"    {len(value)} items")
        else:
            pprint.pprint(value, indent=4, depth=1, width=80)


if __name__ == "__main__":
    # Load name mappings
    CLASS_NAME_MAPPINGS = load_class_name_mappings()
    ENUM_NAME_MAPPINGS = load_enum_name_mappings()
    SLOT_NAME_MAPPINGS = load_slot_name_mappings()
    SUBSET_NAME_MAPPINGS = load_subset_name_mappings()
    INTER_TYPE_REFACTORING = load_inter_type_refactoring()
    
    # Build and display release info
    release_info = build_release_info_dict()

    # Print the dictionary
    separator = "=" * 50
    print(f"\n{separator}")
    print("Release Info Dictionary:")
    print(separator)
    pprint.pprint(release_info)

    # Save as YAML file
    output_file = Path(__file__).parent.parent.parent / "local" / "mixs_releases.yaml"
    with open(output_file, 'w') as f:
        yaml.dump(release_info, f, default_flow_style=False, sort_keys=False)
    print(f"\nSaved release info to: {output_file}")

    # Load and compare schemas
    print("\n" + "=" * 50)
    print("Loading schemas for comparison...")
    print("=" * 50)

    old_schema, new_schema, old_info, new_info = load_schema_views(DEFAULT_OLD_COMMIT, DEFAULT_NEW_COMMIT)

    print("\nOld schema info:")
    pprint.pprint(old_info)

    print("\nNew schema info:")
    pprint.pprint(new_info)

    # Test the new top-level key diffing functionality
    print("\n" + "=" * 50)
    print("Top-Level Key Diff Analysis (Using SchemaView)")
    print("=" * 50)
    
    # Get populated top-level keys for each schema
    old_top_keys = populated_top_level_keys(old_schema)
    new_top_keys = populated_top_level_keys(new_schema)
    
    print(f"\nOld schema ({old_info['tag']}) populated top-level keys ({len(old_top_keys)}):")
    for key in sorted(old_top_keys):
        print(f"  {key}")
    
    print(f"\nNew schema ({new_info['tag']}) populated top-level keys ({len(new_top_keys)}):")
    for key in sorted(new_top_keys):
        print(f"  {key}")
    
    # Perform the diff
    only_in_old, only_in_new = diff_top_keys(old_schema, new_schema)
    
    def get_key_value(schema_view: SchemaView, key: str):
        """Get the value for a specific key from schema."""
        # First try raw schema
        schema_dict = schema_view.schema._as_dict
        if key in schema_dict and is_populated(schema_dict[key]):
            return schema_dict[key]
        
        # Then try all_* methods for collections
        collection_methods = {
            'classes': lambda: schema_view.all_classes(imports=True),
            'slots': lambda: schema_view.all_slots(imports=True),
            'enums': lambda: schema_view.all_enums(imports=True),
            'types': lambda: schema_view.all_types(imports=True),
            'subsets': lambda: schema_view.all_subsets(imports=True),
        }
        
        if key in collection_methods:
            try:
                return collection_methods[key]()
            except (AttributeError, TypeError):
                return None
        
        return None
    
    def print_key_value(key: str, value, max_items: int = 10):
        """Print key value with size warnings if needed."""
        # Keys that should never be truncated
        no_truncate_keys = {'imports', 'settings'}
        
        if value is None:
            print(f"    {key}: None")
            return
            
        # Special formatting for settings
        if key == 'settings' and isinstance(value, dict):
            print(f"    {key}:")
            
            # Analyze which slots use which settings (we need the schema view for this)
            # For now, we'll just show the settings - we'll enhance this in the calling context
            for setting_key, setting_obj in sorted(value.items()):
                if hasattr(setting_obj, 'setting_value'):
                    regex_value = setting_obj.setting_value
                    # Check if regex has anchors
                    has_start_anchor = regex_value.startswith('^')
                    has_end_anchor = regex_value.endswith('$')
                    
                    if has_start_anchor and has_end_anchor:
                        anchor_status = "[ANCHORED]"
                    elif has_start_anchor:
                        anchor_status = "[START ANCHOR]"
                    elif has_end_anchor:
                        anchor_status = "[END ANCHOR]"
                    else:
                        anchor_status = "[NO ANCHORS]"
                    
                    print(f"      {setting_key}: {regex_value} {anchor_status}")
                else:
                    print(f"      {setting_key}: {setting_obj}")
            return
            
        if isinstance(value, dict):
            if len(value) > max_items and key not in no_truncate_keys:
                print(f"    {key}: [LARGE DICT with {len(value)} items - showing first {max_items}]")
                items = list(value.items())[:max_items]
                for k, v in items:
                    print(f"      {k}: {type(v).__name__}")
                print(f"      ... and {len(value) - max_items} more items")
            else:
                print(f"    {key}:")
                pprint.pprint(value, indent=6, depth=2, width=100)
        elif isinstance(value, (list, tuple)):
            if len(value) > max_items and key not in no_truncate_keys:
                print(f"    {key}: [LARGE LIST with {len(value)} items - showing first {max_items}]")
                for i, item in enumerate(value[:max_items]):
                    print(f"      [{i}]: {type(item).__name__}")
                print(f"      ... and {len(value) - max_items} more items")
            else:
                print(f"    {key}:")
                pprint.pprint(value, indent=6, depth=2, width=100)
        else:
            print(f"    {key}:")
            pprint.pprint(value, indent=6, depth=1, width=100)

    print(f"\nTop-level key differences:")
    print(f"  Keys populated in {old_info['tag']} but missing/empty in {new_info['tag']}: {len(only_in_old)}")
    for key in sorted(only_in_old):
        value = get_key_value(old_schema, key)
        print_key_value(key, value)
    
    print(f"\n  Keys populated in {new_info['tag']} but missing/empty in {old_info['tag']}: {len(only_in_new)}")
    for key in sorted(only_in_new):
        value = get_key_value(new_schema, key)
        print_key_value(key, value)
        
        # If we just printed settings, also show which slots use which settings
        if key == 'settings':
            print(f"\n    Settings usage in slot structured_patterns:")
            analysis = analyze_slot_settings_usage(new_schema)
            settings_usage = analysis['settings_usage']
            pattern_usage = analysis['pattern_usage']
            undefined_settings = analysis['undefined_settings']
            unused_settings = analysis['unused_settings']
            
            if settings_usage:
                for setting_name in sorted(settings_usage.keys()):
                    slot_list = settings_usage[setting_name]
                    print(f"      {setting_name}: used by {len(slot_list)} slots")
                    for slot_name in sorted(slot_list):
                        print(f"        - {slot_name}")
                
                if undefined_settings:
                    print(f"\n      ⚠️  UNDEFINED SETTINGS (used but not defined): {len(undefined_settings)}")
                    for setting_name in sorted(undefined_settings):
                        slots_using = settings_usage.get(setting_name, [])
                        print(f"        {setting_name}: used by {len(slots_using)} slots")
                        for slot_name in sorted(slots_using):
                            print(f"          - {slot_name}")
                
                if unused_settings:
                    print(f"\n      📝 UNUSED SETTINGS (defined but not used): {len(unused_settings)}")
                    for setting_name in sorted(unused_settings):
                        print(f"        {setting_name}")
            else:
                print(f"      No slots found using structured_pattern.syntax references")
    
    # Compare shared keys for differences
    shared_keys = old_top_keys & new_top_keys
    print(f"\n  Shared keys with potential differences: {len(shared_keys)}")
    
    differences_found = 0
    for key in sorted(shared_keys):
        old_value = get_key_value(old_schema, key)
        new_value = get_key_value(new_schema, key)
        
        if old_value != new_value:
            compare_key_values(key, old_value, new_value, old_info, new_info, old_schema, new_schema)
            differences_found += 1
    
    if differences_found == 0:
        print("      No differences found in shared keys")
    
    # Report API usage
    print(f"\n" + "=" * 50)
    print(f"API Usage Summary: {API_CALL_COUNT} GitHub API calls made")
    print("=" * 50)
