# mixs-legacy-diff

Compare MIxS schemas across formats and versions (v4 onward).

## Install

```bash
poetry install --with legacy-diff
```

This installs `openpyxl` (for .xlsx) and `xlrd` (for .xls) alongside the base project.

## Supported formats

| Version | Format | File extension |
|---------|--------|----------------|
| v4 (2014) | Excel | `.xls` |
| v5 (2018) | Excel | `.xlsx` |
| v6.0+ (2022+) | LinkML YAML | `.yaml` / `.yml` |

Any combination of old/new formats works: v4 vs v5, v5 vs v6, v4 vs v6, v6 vs v6.

## Basic usage

```bash
# Local files
mixs-legacy-diff \
  --old ../mixs-legacy/mixs4/MIxS_210514.xls \
  --new ../mixs-legacy/mixs5/mixs_v5.xlsx

# GitHub spec: owner/repo@ref:path
mixs-legacy-diff \
  --old "GenomicsStandardsConsortium/mixs@v6.2.0:src/mixs/schema/mixs.yaml" \
  --new "GenomicsStandardsConsortium/mixs@v6.3.0:src/mixs/schema/mixs.yaml"
```

## GitHub spec format

Remote schemas are fetched from GitHub using this format:

```
owner/repo@ref:path/to/schema.yaml
```

- `ref` can be a tag, branch, or commit SHA
- `path` is the file path within the repo at that ref

## MIxS release tags and schema paths

The schema file path changed between releases. Use this table when constructing GitHub specs:

| Tag | Schema path | Notes |
|-----|-------------|-------|
| `mixs6.0.0` | `model/schema/mixs.yaml` | First LinkML release |
| `mixs6.1.0` | `model/schema/mixs.yaml` | |
| `mixs6.1.1` | `model/schema/mixs.yaml` | Last `model/` path |
| `v6.2.0` | `src/mixs/schema/mixs.yaml` | Path changed here |
| `v6.2.2` | `src/mixs/schema/mixs.yaml` | |
| `v6.2.3` | `src/mixs/schema/mixs.yaml` | |
| `v6.3.0` | `src/mixs/schema/mixs.yaml` | |
| `main` | `src/mixs/schema/mixs.yaml` | Current development |

Note: tag naming also changed from `mixs6.x.x` to `v6.x.x` at v6.2.0.

### Examples using the table above

```bash
# v6.0.0 → current main (note different paths)
mixs-legacy-diff \
  --old "GenomicsStandardsConsortium/mixs@mixs6.0.0:model/schema/mixs.yaml" \
  --new "GenomicsStandardsConsortium/mixs@main:src/mixs/schema/mixs.yaml"

# v6.2.0 → v6.3.0 (same path)
mixs-legacy-diff \
  --old "GenomicsStandardsConsortium/mixs@v6.2.0:src/mixs/schema/mixs.yaml" \
  --new "GenomicsStandardsConsortium/mixs@v6.3.0:src/mixs/schema/mixs.yaml"
```

## Mapping hints

For comparisons where you know about expected renames, splits, merges, or deletions,
provide a mappings directory:

```bash
mixs-legacy-diff --old ... --new ... \
  --mappings-dir assets/between_diff_mappings/6_to_pre_7
```

The mapping config (`mapping_config.yaml`) uses this structure:

```yaml
renames:
  slots:
    old_slot_name: new_slot_name
  classes:
    OldClassName: NewClassName
  enums:
    OldEnumName: NewEnumName

deletions:
  slots:
    removed_slot: "Reason for removal"
```

Pre-built mapping configs are in `assets/between_diff_mappings/`.

## Output

The tool writes two files to the output directory:

- `schema_comparison_results.yaml` — structured YAML with full comparison data
- `comparison_summary.txt` — human-readable summary with diffs

## Release workflow integration

The `create-release-pr.yaml` GitHub Actions workflow uses this tool to generate
a schema diff as part of every release PR. The workflow inputs accept full GitHub
specs (see table above for correct paths per tag).

## Tests

```bash
# Run all 30 tests (downloads Excel files from GitHub if needed)
poetry run python -m pytest tests/test_legacy_diff.py -v
```

Tests run automatically in CI on PRs that touch `src/mixs/diff/` or test files.
