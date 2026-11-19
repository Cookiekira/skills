#!/bin/sh
# Usage: link-env.sh <worktree>
# Run from the main checkout. Symlink its gitignored .env files into <worktree>.
set -eu
main=$(git rev-parse --show-toplevel)
git -C "$main" ls-files --others --ignored --exclude-standard --directory |
  grep -E '(^|/)\.env[^/]*$' |
  while IFS= read -r f; do ln -s "$main/$f" "$1/$f"; done
