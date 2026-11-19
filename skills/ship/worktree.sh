#!/bin/sh
# Usage: worktree.sh <label> <branch>
# Create <main checkout>.<label> on a new <branch> from a fresh origin default
# branch, symlink the main checkout's gitignored .env files into it, and print
# the worktree path.
set -eu
label=$1
branch=$2
main=$(git rev-parse --show-toplevel)
path="$main.$label"

git -C "$main" fetch --quiet origin
base=$(git -C "$main" symbolic-ref --quiet --short refs/remotes/origin/HEAD || echo origin/main)
git -C "$main" worktree add --quiet --no-track -b "$branch" "$path" "$base"

git -C "$main" ls-files --others --ignored --exclude-standard --directory |
  grep -E '(^|/)\.env[^/]*$' |
  while IFS= read -r f; do ln -s "$main/$f" "$path/$f"; done

echo "$path"
