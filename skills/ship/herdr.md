# Herdr

Load the `herdr` skill.

**Start.** Split a pane to the right and start the reviewer there with `herdr agent start reviewer-<label> --kind <codex|claude> --pane <pane> -- <reviewer bypass flag>`, the flag from the harness table.

**Send and wait.** Run `herdr agent prompt <reviewer> "Read and follow <path>" --wait --timeout 1800000`. A prompt sent while the agent is still starting is dropped, so check that `herdr agent get <reviewer>` reports `working`, and resend if it is still `idle`.
