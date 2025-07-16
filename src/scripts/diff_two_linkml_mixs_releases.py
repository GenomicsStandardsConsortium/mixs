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
from typing import List, Tuple, Dict, Optional, Any


APPROVED_DIRS = ['src', 'model']
DEFAULT_OLD_COMMIT = '74744ee'  # mixs6.0.0
DEFAULT_NEW_COMMIT = '994c745'  # main


def get_github_headers() -> Dict[str, str]:
    """Get GitHub API headers with authentication if available.
    
    Returns:
        Dict containing Authorization header if token is available, empty dict otherwise.
    """
    env_file = Path(__file__).parent.parent.parent / 'local' / '.env'
    if env_file.exists():
        load_dotenv(env_file)
    
    headers = {}
    if token := os.getenv('GITHUB_TOKEN'):
        headers['Authorization'] = f'token {token}'
        print("Using authenticated GitHub API")
    else:
        print("Using unauthenticated GitHub API (rate limited)")
    return headers


def fetch_tree(commit_sha: str) -> List[str]:
    """Fetch recursive tree from GitHub API and return YAML files.
    
    Args:
        commit_sha: Git commit SHA to fetch tree for.
        
    Returns:
        List of paths to YAML files in the repository at the given commit.
    """
    headers = get_github_headers()
    url = f"https://api.github.com/repos/GenomicsStandardsConsortium/mixs/git/trees/{commit_sha}?recursive=1"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    tree = response.json()
    
    yaml_files = [item['path'] for item in tree['tree'] 
                  if item['path'].endswith('.yaml')]
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
    """Get releases from GitHub API and return list of (tag, date) tuples.
    
    Returns:
        List of tuples containing (tag_name, published_date) for each release.
    """
    headers = get_github_headers()
    url = "https://api.github.com/repos/GenomicsStandardsConsortium/mixs/releases"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    releases = response.json()
    
    release_info = []
    for release in releases:
        tag = release['tag_name']
        date = datetime.fromisoformat(release['published_at'].replace('Z', '+00:00'))
        release_info.append((tag, date))
    
    return release_info


def get_yaml_files_from_release(tag: str) -> Tuple[List[str], str]:
    """Get list of YAML files and commit SHA from a specific release tag.
    
    Args:
        tag: Release tag name to fetch files for.
        
    Returns:
        Tuple of (yaml_files, commit_sha) where yaml_files is a list of YAML file paths
        and commit_sha is the full commit hash for the tag.
    """
    headers = get_github_headers()
    # Get commit SHA for the tag
    url = f"https://api.github.com/repos/GenomicsStandardsConsortium/mixs/git/refs/tags/{tag}"
    response = requests.get(url, headers=headers)
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
    headers = get_github_headers()
    # Get main branch commit
    url = "https://api.github.com/repos/GenomicsStandardsConsortium/mixs/branches/main"
    response = requests.get(url, headers=headers)
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


def load_schema_views(old_commit: str = DEFAULT_OLD_COMMIT, 
                     new_commit: str = DEFAULT_NEW_COMMIT) -> Tuple[SchemaView, SchemaView, Dict[str, Any], Dict[str, Any]]:
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


if __name__ == "__main__":
    releases = get_releases()
    release_info = {}
    
    for tag, date in releases:
        yaml_files, commit_sha = get_yaml_files_from_release(tag)
        short_hash = commit_sha[:7]
        
        mixs_yaml_path = find_mixs_yaml_path(yaml_files)
        
        release_info[short_hash] = {
            'tag': tag,
            'date': date.strftime('%Y-%m-%d'),
            'mixs_yaml_path': mixs_yaml_path
        }
        
        print(f"\n{tag}: {date.strftime('%Y-%m-%d')} ({short_hash})")
        for yaml_file in yaml_files:
            print(f"  {yaml_file}")
    
    # Add main branch info
    yaml_files, commit_sha, commit_date = get_main_branch_info()
    short_hash = commit_sha[:7]
    
    mixs_yaml_path = find_mixs_yaml_path(yaml_files)
    
    release_info[short_hash] = {
        'tag': 'main',
        'date': commit_date.strftime('%Y-%m-%d'),
        'mixs_yaml_path': mixs_yaml_path
    }
    
    print(f"\nmain: {commit_date.strftime('%Y-%m-%d')} ({short_hash})")
    for yaml_file in yaml_files:
        print(f"  {yaml_file}")
    
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
    print("\n" + "="*50)
    print("Loading schemas for comparison...")
    print("="*50)
    
    old_schema, new_schema, old_info, new_info = load_schema_views('e7ffaea', '994c745')
    
    print("\nOld schema info:")
    pprint.pprint(old_info)
    
    print("\nNew schema info:")
    pprint.pprint(new_info)
    
    # Identify populated keys in each schema
    print("\n" + "="*50)
    print("Schema Key Analysis")
    print("="*50)
    
    old_schema_keys = set(key for key, value in old_schema.schema.__dict__.items() if value is not None)
    new_schema_keys = set(key for key, value in new_schema.schema.__dict__.items() if value is not None)
    
    print(f"\nOld schema ({old_info['tag']}) populated keys ({len(old_schema_keys)}):")
    for key in sorted(old_schema_keys):
        print(f"  {key}")
    
    print(f"\nNew schema ({new_info['tag']}) populated keys ({len(new_schema_keys)}):")
    for key in sorted(new_schema_keys):
        print(f"  {key}")
    
    # Compare keys
    keys_only_in_old = old_schema_keys - new_schema_keys
    keys_only_in_new = new_schema_keys - old_schema_keys
    common_keys = old_schema_keys & new_schema_keys
    
    print(f"\nKey comparison:")
    print(f"  Keys only in old schema: {len(keys_only_in_old)}")
    if keys_only_in_old:
        for key in sorted(keys_only_in_old):
            print(f"    {key}")
    
    print(f"  Keys only in new schema: {len(keys_only_in_new)}")
    if keys_only_in_new:
        for key in sorted(keys_only_in_new):
            print(f"    {key}")
    
    print(f"  Common keys: {len(common_keys)}")
    for key in sorted(common_keys):
        print(f"    {key}")