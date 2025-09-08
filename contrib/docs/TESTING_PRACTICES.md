# LinkML Community Testing Best Practices

## Framework Recommendation

The LinkML project has **transitioned to pytest** as their standard testing framework. The official documentation states:

> *"It is recommended that you always use pytest to run tests. New tests in any directory should be written using pytest."*

## Current MIxS Testing Status

**Current Implementation:**
- Uses Python `unittest` framework (older approach)
- Single test in `tests/test_data.py`
- Validates YAML example files against generated Python dataclasses
- Run via: `poetry run python -m unittest discover`

**Test Coverage:**
- Loads example YAML files from `src/data/examples/valid/`
- Validates against `MixsCompliantData` Python dataclass
- Ensures LinkML-generated Python datamodel works with example data

## LinkML-Specific Testing Patterns

### 1. Schema Validation Testing
```python
from linkml.validator import validate

# Basic validation pattern
instance = {"id": "example", "field": "value"}
report = validate(instance, "schema.yaml", "ClassName")
```

**Best Practices:**
- Test with both valid and invalid data examples
- Use `linkml_runtime.loaders` for YAML/JSON loading
- Validate against generated Python dataclasses

### 2. Generator Testing
**Organization:**
- Generator tests go in `tests/test_generators/` subdirectory
- Use model LinkML schemas from test suite as fixtures
- Test generated artifacts (JSON Schema, Python classes, OWL, etc.)

### 3. Command-Line Integration Testing
```bash
# CLI validation testing
linkml-validator --inputs examples/data.json \
  --schema examples/schema.yaml \
  --output validation_report.json
```

### 4. Multi-Layer Validation Approach
LinkML supports multiple validation backends:
- **JSON Schema**: Generated artifacts validation
- **Python dataclasses**: Lightweight object validation  
- **RDF/SPARQL**: Triplestore data validation
- **Pydantic models**: Type-safe validation with rich error reporting

## Testing Architecture

### Plugin-Based Validation
LinkML uses a plugin architecture where the validator:
- Does not perform validation itself
- Orchestrates validation through plugins
- Supports custom validation plugin development
- Uses `JsonSchemaValidationPlugin` for JSON Schema validation

### Project Structure
```
tests/
├── test_generators/     # Generator-specific tests
├── test_validators/     # Validation logic tests
└── test_datamodel/      # Generated dataclass tests
```

## Migration Strategy

### From unittest to pytest
**Compatibility:**
- pytest can run existing unittest-based tests
- Gradual migration approach supported
- Leverage existing test infrastructure during transition

**Benefits of Migration:**
- Less boilerplate code
- More readable test output
- Rich fixture management
- Parameterized testing capabilities
- Extensive plugin ecosystem
- Better integration with LinkML testing patterns

### Recommended Migration Path
1. **Phase 1**: Run existing unittest tests with pytest
2. **Phase 2**: Add new tests using pytest patterns
3. **Phase 3**: Gradually convert existing tests to pytest style
4. **Phase 4**: Adopt LinkML-specific testing patterns

## Current vs. Recommended Testing

### Current MIxS Approach
```python
class TestData(unittest.TestCase):
    def test_data(self):
        for path in EXAMPLE_FILES:
            obj = yaml_loader.load(path, target_class=MixsCompliantData)
            assert obj
```

### Recommended LinkML Pytest Approach
```python
import pytest
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader

@pytest.mark.parametrize("example_file", EXAMPLE_FILES)
def test_schema_validation(example_file):
    """Test schema validation using LinkML validator."""
    # Load and validate using LinkML patterns
    obj = yaml_loader.load(example_file, target_class=MixsCompliantData)
    assert obj
    
    # Additional validation using LinkML validator
    with open(example_file) as f:
        data = yaml.safe_load(f)
    report = validate(data, "src/mixs/schema/mixs.yaml", "MixsCompliantData")
    assert report.valid

def test_generated_datamodel():
    """Test generated Python datamodel functionality."""
    # Test dataclass instantiation and validation
    
def test_schema_consistency():
    """Test schema internal consistency."""
    # Test slot definitions, class hierarchies, etc.
```

## Community Standards

### Testing Organization
- **Unit tests**: Test individual components (slots, classes, enums)
- **Integration tests**: Test complete workflows (schema → datamodel → validation)
- **Generator tests**: Test LinkML output generation (JSON Schema, OWL, etc.)
- **CLI tests**: Test command-line tools and scripts

### Documentation Testing
- Include validation examples in tutorials
- Test schema examples in documentation
- Validate generated documentation artifacts

## Recommendations for MIxS

### Immediate Improvements
1. **Add pytest dependency** to development requirements
2. **Expand test coverage** beyond single datamodel test
3. **Add generator tests** for schema transformation pipeline
4. **Test CLI scripts** with various input scenarios

### Future Enhancements
1. **Parameterized testing** for multiple schema variants
2. **Property-based testing** for schema edge cases
3. **Performance testing** for large schema operations
4. **Integration testing** with external tools (validators, generators)

### Specific MIxS Test Scenarios
Given the project's complexity, consider testing:
- Schema transformation pipeline validation
- Extension combination compatibility
- Excel template generation accuracy
- Cross-version schema compatibility
- Generated artifact consistency across formats