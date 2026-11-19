# Paseo

Load the `paseo` skill.

**Start.** Start the reviewer as a subagent with `create_agent`, which opens it as a tab in this workspace: round 1's `Read and follow <path>` as `initialPrompt`, and the reviewer's unattended mode: `provider: "codex/<model>"` with `settings.modeId: "full-access"`, or `provider: "claude/<model>"` with `settings.modeId: "bypassPermissions"`.

**Send.** Send later rounds to the same `agentId` with `send_agent_prompt`.

**Wait.** Paseo notifies you when it finishes, whichever harness you are: end your turn and wait for that notification.
