# Herdr

Load the `herdr` skill.

**Start.** Split a pane to the right and start the reviewer there with `herdr agent start reviewer-<label> --kind <reviewer> --pane <pane> -- <bypass flag>`.

**Send and wait.** `herdr agent prompt <reviewer> "Read and follow <path>" --wait --timeout 1800000`. A prompt sent while the agent is still starting is dropped: check that `herdr agent get <reviewer>` reports `working`, and resend while it is `idle`.
