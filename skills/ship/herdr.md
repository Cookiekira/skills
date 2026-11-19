# Herdr

Load the `herdr` skill.

## Hand off

Open the worktree as its own workspace with `herdr worktree open --path <worktree> --label <label> --focus --json`, then start Claude in that workspace's pane with `herdr agent start ship --kind claude --pane <pane> -- --dangerously-skip-permissions "/ship <argument>"`.

## Reviewer

**Start or reuse.** Reuse a live Codex agent from `herdr agent list` that runs in this workspace; another workspace's reviewer sees another worktree. If there is none, split a pane to the right and start one there with `herdr agent start reviewer --kind codex --pane <pane> -- --dangerously-bypass-approvals-and-sandbox`, so it reads the ticket, writes its report into the scratchpad, and drives a browser without stopping on approvals.

**Send.** A prompt sent while `/new` is still resetting is dropped, even after `/new --wait` returns. After every prompt, check that `herdr agent get <reviewer>` reports `working`, and resend it if the agent is still `idle`.

**Wait.** Run `herdr agent prompt <reviewer> "Read and follow <path>" --wait --timeout 1800000` as a background Bash command, and wait for its notification.
