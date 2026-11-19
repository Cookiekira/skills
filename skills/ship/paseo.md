# Paseo

Load the `paseo` skill.

## Worktree

Create it with `<skill dir>/worktree.sh <label> <branch>`; it prints the worktree path. Carry on in this session. The shell returns to the main checkout after each call, so start every command with `cd <worktree> &&` and give file tools absolute worktree paths.

## Reviewer

**Start.** For the first round, start one Codex subagent with `create_agent` in this workspace, where it opens as a tab. Give it `provider: "codex/<model>"`, `settings.modeId: "full-access"`, and the round's `Read and follow <path>` as `initialPrompt`. Keep its `agentId` for every later round of this ticket. Full access lets it read the ticket, write its report into the scratchpad, and drive a browser without stopping on approvals.

Its shell starts in the main checkout, so every prompt you write for it names the worktree path and tells it to work there.

**Send.** Send later rounds to the same `agentId` with `send_agent_prompt`.

**Wait.** End your turn and wait for its finish notification, then read the report file.
