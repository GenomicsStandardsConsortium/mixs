#!/bin/bash
set -euo pipefail

echo "Starting cumulative merge of all feature branches..."
echo "Current branch: $(git branch --show-current)"
echo ""

for branch in $(git branch -r | grep -v HEAD | grep -v main | grep -v 23-make-a-cumulative-branch | sed 's/origin\///'); do
  echo "Attempting to merge $branch..."
  if ! git merge --no-edit origin/$branch; then
    echo ""
    echo "CONFLICT in $branch - stopping here"
    echo "You're now in merge state for $branch"
    echo ""
    echo "To resume after resolving conflicts:"
    echo "1. Resolve conflicts in files"
    echo "2. git add <resolved-files>"
    echo "3. git commit"
    echo "4. Run this script again to continue with remaining branches"
    echo ""
    exit 1
  fi
  echo "✓ Successfully merged $branch"
  echo ""
done

echo "All branches merged successfully!"