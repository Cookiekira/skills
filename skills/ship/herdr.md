# Herdr

Load the `herdr` skill.

**Start.** Split a pane to the right and start the reviewer there with `herdr agent start reviewer-<label> --kind codex --pane <pane> -- --dangerously-bypass-approvals-and-sandbox`. The bypass lets it read the ticket, write its report into the scratchpad, and drive a browser without stopping on approvals.

**Send and wait.** Run `herdr agent prompt <reviewer> "Read and follow <path>" --wait --timeout 1800000` as a background Bash command, and wait for its notification. A prompt sent while the agent is still starting is dropped, so check that `herdr agent get <reviewer>` reports `working`, and resend if it is still `idle`.
