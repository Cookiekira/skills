# Reviewer in Herdr

Load the `herdr` skill.

**Start or reuse.** Reuse a live Codex agent from `herdr agent list`. If there is none, split a pane to the right and start one with `--kind codex`, named `reviewer`.

**Send.** A prompt sent while `/new` is still resetting is dropped, even after `/new --wait` returns. After every prompt, check that `herdr agent get <reviewer>` reports `working`, and resend it if the agent is still `idle`.

**Wait.** Run `herdr agent prompt <reviewer> "Read and follow <path>" --wait --timeout 1800000` as a background Bash command, and wait for its notification.
