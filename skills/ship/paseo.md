# Paseo

Load the `paseo` skill.

## Worktree

Paseo owns worktrees natively, so this session opens one and works in it directly. Run `git fetch origin`, then call `create_workspace` with `isolation: "worktree"`, `mode: "branch-off"`, `branchName: <branch>`, `baseBranch: "origin/main"`, and `worktreeSlug: <label>`. It lands under this project. From the main checkout, run `<skill dir>/link-env.sh <worktree path>` to symlink the gitignored `.env*` files.

Then continue here. Your shell resets to the main checkout after each call, so start every command with `cd <worktree> &&` and give file tools absolute worktree paths.

## Reviewer

**Start or reuse.** Reuse the Codex agent labelled `role: reviewer` in the worktree's workspace (`list_agents` with `cwd: <worktree>`). If there is none, call `create_agent` with `workspaceId` set to the worktree's workspace, `provider: "codex/<model>"`, `settings.modeId: "full-access"`, `labels: { "role": "reviewer" }`, and the round's `Read and follow <path>` as `initialPrompt`. Full access lets it read the ticket, write its report into the scratchpad, and drive a browser without stopping on approvals.

To reset a reviewer that last reviewed a different ticket, archive it with `archive_agent` and start a new one.

**Send.** Send later rounds to the same `agentId` with `send_agent_prompt`.

**Wait.** End your turn and wait for its finish notification, then read the report file.
