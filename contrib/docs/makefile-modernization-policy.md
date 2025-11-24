# MIxS Makefile Modernization and Directory Organization Policy

## Executive Summary

This document outlines the modernization of the MIxS project's build system, focusing on improved organization, consistent tooling, and clear separation between official artifacts and contributor analysis files.

## Key Changes Implemented

### 1. Directory Reorganization

**Problem**: The `assets/` directory mixed official artifacts with contributor analysis files, creating confusion about authoritative vs. developmental content.

**Solution**: Renamed `assets/` to `contrib/` with clear purpose distinction:
- `project/` and `release/` - Official GSC-approved schema artifacts
- `contrib/` - Contributor analysis and quality control files (subject to GSC approval)
- `contrib/templates/` - Input templates preserved during cleanup
- Generated outputs in `contrib/` root can be safely cleaned and regenerated

### 2. Build Target Organization

**Linting Strategy**:
- Moved linting targets (`linkml-lint`, `yaml-lint`) to end of build pipeline
- Implemented non-failing mode with `|| true` for warnings-only feedback
- Distinguished between `qc` (deptry - can fail) and schema linters (non-failing)
- Maintained GitHub Actions for PR feedback without blocking builds

**Target Consolidation**:
- Renamed `all-assets` to `all-contrib` for clarity
- Updated `clean-assets` to `clean-contrib`
- Integrated contrib generation into main `all` target workflow
- Separated `project.Makefile` into `contrib.Makefile` for focused concerns

### 3. CLI Standardization

**Script Modernization**:
- Converted all scripts from legacy `sys.argv` to Click CLI framework
- Standardized option names: `--output-file`, `--schema-file`, `--source-file`
- Added Poetry script aliases for all utility scripts
- Updated Makefile targets to use Poetry aliases instead of direct Python calls

**Benefits**:
- Consistent command-line interface across all tools
- Automatic help generation and argument validation
- Better integration with Poetry package management
- Reduced coupling between Makefiles and script internals

### 4. Documentation Enhancement

**Comprehensive Help System**:
- Created detailed help target showing complete dependency graph
- Documented what each target outputs to which directory  
- Showed relationships between local targets and GitHub Actions
- Clarified schema transformation pipeline with numbered steps
- Distinguished between targets that can fail vs. warning-only

**Script Documentation**:
- Consolidated scattered script documentation into single `src/scripts/README.md`
- Removed redundant individual markdown files
- Documented CLI interfaces and Poetry aliases
- Explained integration with build system

## Schema Transformation Pipeline

The contributor analysis includes a clear transformation pipeline:

1. **Original Schema** (`src/mixs/schema/mixs.yaml`)
2. **Structured Patterns Preferred** (`contrib/mixs_structured_patterns_preferred.yaml`)
   - Removes `pattern` field from slots with `structured_pattern`
3. **Normalized-Minimized** (`contrib/mixs-normalized-minimized.yaml`) 
   - Extensive yq cleanup: removes imports, normalizes annotations, removes metadata
4. **Patterns-Materialized** (`contrib/mixs-patterns-materialized.yaml`)
   - Expands structured patterns into concrete validation rules

## GitHub Actions Integration

**Alignment with CI/CD**:
- Updated main workflow to use correct target names (`all-contrib`)
- Added `make clean` to docs workflows to prevent stale files
- Documented which targets are replicated by dedicated GitHub Actions
- Maintained separation between local development and CI execution

**Quality Assurance**:
- LinkML and YAML linting provide PR feedback without blocking merges
- Dependency checking (`deptry`) can fail builds for serious dependency issues
- Full build pipeline tested on every PR through main GitHub Action

## Governance and Approval

**Contributor vs. Official Content**:
- Clear distinction between GSC-approved official artifacts and contributor analysis
- All `contrib/` files explicitly marked as "subject to GSC approval"
- Maintained authoritative content in `project/` and `release/` directories
- Contributors can iterate on analysis tools without affecting official releases

## Implementation Benefits

1. **Consistency**: Unified CLI interface and build patterns across all tools
2. **Clarity**: Clear separation of concerns between directories and target purposes  
3. **Reliability**: Non-failing linters provide feedback without disrupting workflows
4. **Maintainability**: Reduced code duplication and improved documentation
5. **Governance**: Clear boundaries between official and developmental content

## Future Considerations

**Potential Enhancements**:
- Add `ruff` Python linting for code quality (Issue #103)
- Further consolidation of docs workflow targets
- Additional Poetry aliases for developer convenience
- Enhanced schema validation reporting

## Migration Path

The changes maintain backward compatibility while providing clearer organization:
- Legacy workflows continue to function
- New standardized interfaces available for all tools
- Gradual migration path from old to new patterns
- Comprehensive documentation for both approaches

This modernization establishes a foundation for continued development while maintaining the stability and governance requirements of the GSC-managed MIxS standard.