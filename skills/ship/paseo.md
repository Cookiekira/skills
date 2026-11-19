# Paseo

Load the `paseo` skill.

## Workspace

Resolve the calling agent's `workspaceId` via `get_agent_status` and look it up with `list_workspaces`. If it is already a `worktree` workspace on the ticket branch, continue at step 2.

Otherwise, choose the ticket label and branch as in step 1. Fetch `origin`, then call `create_workspace` with `isolation: "worktree"`, `mode: "branch-off"`, `baseBranch: "origin/main"`, `background: false`, the chosen `branchName`, the label as `worktreeSlug`, and the ticket title. Use the current workspace's `projectId` and checkout path so the ticket appears under that project.

Call `create_agent` with the new `workspaceId` and the calling agent's `provider/model`. Carry over its mode, thinking option, and feature values through `settings`. Give the implementing agent a plain-text `initialPrompt`:

> Read and follow `<absolute path to ship/SKILL.md>` from step 2 for `<original ticket or task>`. Step 1 created this workspace for branch `<branch>`. Verify the checked-out branch before implementing.

Once the agent starts, report the workspace and branch and let it own the rest of the run.

## Reviewer

**Start.** `create_agent` starts the reviewer as a subagent tab in the implementing agent's workspace. Resolve the `<reviewer>-reviewer` profile as described in the `paseo` skill and pass round 1's `Read and follow <path>` as `initialPrompt`.

**Send.** `send_agent_prompt` to the same `agentId`.

**Wait.** Paseo notifies you when the round finishes: end your turn and wait for it.
