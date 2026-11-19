# Paseo

Load the `paseo` skill.

**Start.** Start the reviewer as a subagent with `create_agent`, which opens it as a tab in this workspace: `provider: "codex/<model>"`, `settings.modeId: "full-access"`, and round 1's `Read and follow <path>` as `initialPrompt`. Full access lets it read the ticket, write its report into the scratchpad, and drive a browser without stopping on approvals.

**Send.** Send later rounds to the same `agentId` with `send_agent_prompt`.

**Wait.** End your turn and wait for its finish notification.
