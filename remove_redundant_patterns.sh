#!/bin/bash

# Script to remove pattern values when structured_pattern exists
# Usage: ./remove_redundant_patterns.sh [input_file] [output_file]

INPUT_FILE="${1:-src/mixs/schema/mixs.yaml}"
OUTPUT_FILE="${2:-src/mixs/schema/mixs_no_redundant_patterns.yaml}"

echo "Removing redundant patterns from: $INPUT_FILE"
echo "Saving results to: $OUTPUT_FILE"

# Use yq to remove pattern field when structured_pattern exists
yq eval '.slots |= with_entries(if .value.pattern and .value.structured_pattern then .value |= del(.pattern) else . end)' "$INPUT_FILE" > "$OUTPUT_FILE"

# Count how many slots were modified
MODIFIED_COUNT=$(yq eval '.slots | to_entries | map(select(.value.structured_pattern and (.value.pattern | not))) | length' "$OUTPUT_FILE")
ORIGINAL_COUNT=$(yq eval '.slots | to_entries | map(select(.value.pattern and .value.structured_pattern)) | length' "$INPUT_FILE")

echo "Successfully processed $INPUT_FILE"
echo "Removed 'pattern' field from $ORIGINAL_COUNT slots that had both 'pattern' and 'structured_pattern'"
echo "Output saved to: $OUTPUT_FILE"

# Verify the result
echo ""
echo "Verification:"
echo "- Slots with both pattern and structured_pattern in original: $ORIGINAL_COUNT"
echo "- Slots with structured_pattern but no pattern in output: $MODIFIED_COUNT"

if [ "$ORIGINAL_COUNT" -eq "$MODIFIED_COUNT" ]; then
    echo "✅ Success: All redundant patterns removed correctly"
else
    echo "❌ Warning: Counts don't match - please review the output"
fi