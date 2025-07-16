import requests
from datetime import datetime
import pprint
import os
from pathlib import Path
from dotenv import load_dotenv


APPROVED_DIRS = ['src', 'model']


def get_github_headers():
    """Get GitHub API headers with authentication if available."""
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


def find_mixs_yaml_path(yaml_files, approved_dirs=None):
    """Find mixs.yaml file in approved directories."""
    if approved_dirs is None:
        approved_dirs = APPROVED_DIRS
    
    for yaml_file in yaml_files:
        if yaml_file.endswith('mixs.yaml'):
            for approved_dir in approved_dirs:
                if yaml_file.startswith(f'{approved_dir}/'):
                    return yaml_file
    return None


def get_releases():
    """Get releases from GitHub API and return list of (tag, date) tuples."""
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


def get_yaml_files_from_release(tag):
    """Get list of YAML files and commit SHA from a specific release tag."""
    headers = get_github_headers()
    # Get commit SHA for the tag
    url = f"https://api.github.com/repos/GenomicsStandardsConsortium/mixs/git/refs/tags/{tag}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    commit_sha = response.json()['object']['sha']
    
    # Get recursive tree
    url = f"https://api.github.com/repos/GenomicsStandardsConsortium/mixs/git/trees/{commit_sha}?recursive=1"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    tree = response.json()
    
    yaml_files = [item['path'] for item in tree['tree'] 
                  if item['path'].endswith('.yaml')]
    return yaml_files, commit_sha


def get_main_branch_info():
    """Get YAML files and commit info from main branch."""
    headers = get_github_headers()
    # Get main branch commit
    url = "https://api.github.com/repos/GenomicsStandardsConsortium/mixs/branches/main"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    branch_info = response.json()
    
    commit_sha = branch_info['commit']['sha']
    commit_date = datetime.fromisoformat(branch_info['commit']['commit']['author']['date'].replace('Z', '+00:00'))
    
    # Get recursive tree
    url = f"https://api.github.com/repos/GenomicsStandardsConsortium/mixs/git/trees/{commit_sha}?recursive=1"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    tree = response.json()
    
    yaml_files = [item['path'] for item in tree['tree'] 
                  if item['path'].endswith('.yaml')]
    
    return yaml_files, commit_sha, commit_date


def print_releases():
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