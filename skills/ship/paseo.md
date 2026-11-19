# Paseo

Load the `paseo` skill.

**Start.** `create_agent` starts the reviewer as a subagent tab in this workspace, launched from the `<reviewer>-reviewer` profile (`codex-reviewer` or `claude-reviewer`), with round 1's `Read and follow <path>` as `initialPrompt`.

**Send.** `send_agent_prompt` to the same `agentId`.

**Wait.** Paseo notifies you when the round finishes: end your turn and wait for it.
