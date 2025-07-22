# GitHub Actions Setup Requirements

This document outlines the repository configuration requirements for the GitHub Actions workflows in this project.

## Repository Settings

### Workflow Permissions

**Location**: Settings > Actions > General > Workflow permissions

**Required Setting**: ✅ **Read and write permissions**

This setting is required for:
- `test_pages_build.yaml`: The PR preview deployment action (`rossjrw/pr-preview-action`) needs write access to push to the `gh-pages` branch
- `deploy-docs.yaml`: Documentation deployment via `mkdocs gh-deploy`

### GitHub Pages Configuration

**Location**: Settings > Pages

**Required Settings**:
- **Source**: Deploy from a branch
- **Branch**: `gh-pages` (or your preferred deployment branch)
- **Folder**: `/ (root)`

This configuration enables:
- Main documentation deployment from `deploy-docs.yaml` workflow
- PR preview deployments from `test_pages_build.yaml` workflow

## Workflow Permissions Summary

| Workflow | Permissions | Purpose |
|----------|-------------|---------|
| `deploy-docs.yaml` | `contents: read`<br>`pages: write`<br>`id-token: write` | Deploy documentation to GitHub Pages using `mkdocs gh-deploy` |
| `test_pages_build.yaml` | `contents: write`<br>`pull-requests: write` | Deploy PR previews using `rossjrw/pr-preview-action` and post preview links |
| `lint-linkml.yml` | `contents: read`<br>`pull-requests: write` | Read schema files and post linting results as PR comments |
| `main.yaml` | Default (no explicit permissions) | Run tests and builds |
| `lint-yaml.yaml` | Default (no explicit permissions) | YAML linting |
| `pypi-publish.yaml` | Default (no explicit permissions) | PyPI package publishing |

## Troubleshooting

### PR Preview Deployment Fails
- Check that "Read and write permissions" is enabled in workflow permissions
- Verify GitHub Pages is configured to deploy from a branch
- Ensure the `gh-pages` branch exists (it will be created automatically on first deployment)

### Documentation Deployment Fails
- Verify GitHub Pages configuration
- Check that the repository has Pages enabled
- Ensure the workflow has appropriate permissions (see table above)

---

*Last updated: 2025-01-22*
*Generated during GitHub Actions alignment (Issue #56)*