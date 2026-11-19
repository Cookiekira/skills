#!/bin/sh
# Usage: link-env.sh
# Run inside a linked worktree. Symlink the main checkout's gitignored .env
# files into it, skipping any already present.
set -eu
main=$(dirname "$(git rev-parse --path-format=absolute --git-common-dir)")
here=$(git rev-parse --show-toplevel)
git -C "$main" ls-files --others --ignored --exclude-standard --directory |
  grep -E '(^|/)\.env[^/]*$' |
  while IFS= read -r f; do [ -e "$here/$f" ] || ln -s "$main/$f" "$here/$f"; done
