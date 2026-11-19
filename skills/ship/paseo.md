# Paseo

Load the `paseo` skill.

## Reviewer

1. Resolve the `<reviewer>-reviewer` profile using the `paseo` skill. Call `create_agent` in the implementing workspace with round 1's `Read and follow <path>` as `initialPrompt`.
2. Use `send_agent_prompt` with the same `agentId` for later rounds.
3. End the turn after each dispatch and wait for Paseo's completion notification.
