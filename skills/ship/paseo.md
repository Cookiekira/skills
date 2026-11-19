# Paseo

Load the `paseo` skill.

## Worktree

Paseo creates the worktree itself: the user starts `/ship` in a workspace opened with **New worktree**, so step 1 is skipped. If this session runs in the main checkout instead, stop and ask the user to start `/ship` from a **New worktree** workspace.

## Reviewer

**Start or reuse.** Reuse the Codex agent labelled `role: reviewer` in this workspace (`list_agents` with `cwd` set to this worktree). If there is none, call `create_agent` in this workspace with `provider: "codex/<model>"`, `settings.modeId: "full-access"`, `labels: { "role": "reviewer" }`, and the round's `Read and follow <path>` as `initialPrompt`. Full access lets it read the ticket, write its report into the scratchpad, and drive a browser without stopping on approvals.

To reset a reviewer that last reviewed a different ticket, archive it with `archive_agent` and start a new one.

**Send.** Send later rounds to the same `agentId` with `send_agent_prompt`.

**Wait.** End your turn and wait for its finish notification, then read the report file.
