# MIxS Schema Version Comparison

## Overview

This document describes the approach and tooling for comparing different versions of the MIxS (Minimum Information about any Sequence) schema to understand changes between releases.

## Current Diffing Script

### Location and Status
- **Script**: `diff_two_linkml_mixs_releases.py`
- **Repository**: Available in `compare-mixs` clone at `/Users/MAM/Documents/gitrepos/compare-mixs/main/mixs/src/scripts/`
- **Branch**: `845-what-are-our-options-for-diffing-schema-changes`
- **Status**: Committed but has uncommitted local modifications
- **Missing**: No Poetry CLI alias or Makefile target (doesn't follow current modernization standards)

### Functionality

**Core Capabilities:**
- Fetches schemas from GitHub releases or commits
- Performs deep structural comparison using LinkML SchemaView
- Generates YAML diff reports with detailed change analysis
- Handles schema evolution patterns (renamed elements, structural changes)
- Supports caching for performance optimization

**Architecture:**
- Dataclass-based comparison framework (`ValueComparison`, `KeyComparison`, `CollectionComparison`, `SchemaComparison`)
- Cascading comparison pattern: schema → collections → individual definitions → nested attributes
- Systematic LinkML introspection using `SchemaView` for materialization and pattern expansion

**Dependencies:**
- `linkml_runtime.utils.schemaview.SchemaView` - Core LinkML schema processing
- `click` - CLI interface  
- `requests` - GitHub API interactions
- `yaml` - Configuration and output serialization
- `dotenv` - Environment variable management

### Current Use Case

**Release Comparison Project:**
- Comparing MIxS 6.0.0 against current main branch (future 7.0.0)
- Command: `poetry run python src/scripts/diff_two_linkml_mixs_releases.py`
- Supporting release documentation: [Making a MIXS major release in GitHub](https://docs.google.com/document/d/1feY0K_ftmW2lcEFS55KviNQTTap1TlBpaWbqIpCGhwM/edit?tab=t.0)

## Technical Limitations

**Current Issues:**
- **File size**: 2700+ lines requiring modular decomposition
- **Global state**: Configuration should be encapsulated in classes
- **Performance**: Repeated SchemaView operations could be memoized
- **Memory usage**: Large schema objects kept in memory throughout comparison
- **Error handling**: Generic exception handling needs improvement

**Missing Capabilities:**
- Cross-repository comparisons (partially supported)
- Interactive diff navigation (only static YAML output)
- Semantic change detection (structural only)
- Multiple export formats (YAML only)
- Change impact analysis
- Migration guide generation

## Integration Needs

**Modernization Requirements:**
Per project standards, this script needs:
1. **Poetry CLI alias** in `pyproject.toml`
2. **Makefile target** for integration with build system
3. **Click CLI standardization** (if not already implemented)
4. **Documentation** in `src/scripts/README.md`

**Proposed Integration:**
- Add to `contrib/` directory as analysis tool
- Create target that outputs to `contrib/schema-diffs/` or similar
- Include in `all-contrib` target for comprehensive analysis

## Multi-Repository Context

**Repository Structure:**
Multiple local MIxS clones exist for different releases and forks:
- Main development repo: `/Users/MAM/Documents/gitrepos/turbomam/mixs/`
- Comparison repo: `/Users/MAM/Documents/gitrepos/compare-mixs/main/mixs/`
- Others for specific releases/branches

This explains the separation of the diffing tool from the main development repository.

## Future Enhancements

**Architectural Improvements:**
- Extract comparison engine into separate module
- Separate GitHub operations utility
- Add comprehensive type annotations
- Implement structured logging
- Optimize schema loading with lazy evaluation

**Functional Enhancements:**
- Visual diff interface (web-based)
- Change classification (breaking vs non-breaking)
- Batch comparison capabilities
- Schema complexity metrics and trend analysis
- Integration with release workflow automation

## Schema Transformation Pipeline Context

The diffing tool complements the existing schema transformation pipeline in `contrib/`:
1. **Original Schema** (`src/mixs/schema/mixs.yaml`)
2. **Structured Patterns Preferred** (`contrib/mixs_structured_patterns_preferred.yaml`)
3. **Normalized-Minimized** (`contrib/mixs-normalized-minimized.yaml`)
4. **Patterns-Materialized** (`contrib/mixs-patterns-materialized.yaml`)

Version comparison helps understand how this pipeline evolves between releases and validates transformation consistency.