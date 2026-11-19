# Paseo

Load the `paseo` skill. Pick each agent's launch settings from its profiles as that skill describes. The modes below are the ones each agent needs.

## Hand off

Adopt the worktree as its own workspace with `create_workspace` (`isolation: "local"`, `path: <worktree>`, `title: <label>`). Then start Claude there with `create_agent`:

- `workspaceId`: the new workspace
- `provider`: `claude/<model>`
- `settings.modeId`: `bypassPermissions`
- `title`: `<label>`
- `initialPrompt`: `/ship <argument>`
- `notifyOnFinish`: `false`

The new agent stays in your subagent track until the user detaches it.

## Reviewer

**Start or reuse.** Reuse a live Codex agent from `list_agents` (filtered by `cwd: <worktree>`) that is labelled `role: reviewer`. Another worktree's reviewer sees another checkout. If there is none, start one in your workspace with `create_agent`: `provider` `codex/<model>`, `settings.modeId` `full-access`, `labels` `{ "role": "reviewer" }`, and the round's `Read and follow <path>` as `initialPrompt`. Full access lets it read the ticket, write its report into the scratchpad, and drive a browser without stopping on approvals.

To reset a reviewer that last reviewed a different ticket, archive it with `archive_agent` and start a fresh one. Do not send it `/new`.

**Send.** Send later rounds with `send_agent_prompt` to the same `agentId`, with `prompt: "Read and follow <path>"` and `activeTurnBehavior: "interrupt"`.

**Wait.** `notifyOnFinish` defaults to `true`, so end your turn and wait for the finish notification. Do not poll. Then read the report file.
