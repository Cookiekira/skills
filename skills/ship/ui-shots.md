# UI screenshot prompt

Write this prompt to `<scratchpad>/ui-shots-prompt.md` and send the reviewer `Read and follow <that path>`. Fill in the placeholders.

---

Take before/after screenshots of the UI change on branch `<branch>`. This is not a code review.

**What changed:** <for each changed screen: its route, the state that shows the change (loading, after a click, after creating a record), and what should look different>.

1. **Worktrees.** Create one throwaway worktree at `origin/main` for the "before" shots and one at `<branch>` (or its pushed HEAD) for the "after" shots, both under `<scratchpad>/wt-*`. Run the repo's install command in each. Leave the shared checkout untouched: another agent is working in it.
2. **Harness.** Drive a real browser through the app's own browser test harness. Find it from the app's e2e README; it runs against synthetic data and fake external services. Where a fake fails by default, make it return realistic sample data that reaches the changed state. Delay a fake to capture a loading state. Add one temporary spec that captures the shots, and wait for the changed element to be visible before each capture.
3. **Shots.** Capture the same screen and state in both worktrees. Save PNGs to `<scratchpad>/ui-shots/`, named `<pr-or-topic>-{before,after}-<screen>.png`. Crop to the element when the change is small, and capture the full page when the change is about placement.
4. **Clean up.** Remove both worktrees with `git worktree remove --force`, and remove nothing else.

Reply with one line per shot pair: its path stem and what changed. Name any shot you could not take, and why. Do not open the files; the caller opens them.
