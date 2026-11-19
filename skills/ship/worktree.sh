#!/bin/sh
# Usage: worktree.sh <label> <branch>
# Create <main checkout>.<label> on a new <branch> from a fresh origin default
# branch, and print the worktree path.
set -eu
main=$(git rev-parse --show-toplevel)
path="$main.$1"

git -C "$main" fetch --quiet origin
base=$(git -C "$main" symbolic-ref --quiet --short refs/remotes/origin/HEAD || echo origin/main)
git -C "$main" worktree add --quiet --no-track -b "$2" "$path" "$base"

echo "$path"
