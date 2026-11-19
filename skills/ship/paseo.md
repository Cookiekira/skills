# Paseo

Load the `paseo` skill.

## Workspace

Open the worktree as a Paseo workspace in your current project, and keep working in it yourself.

1. Find your workspace in `list_workspaces` (its `cwd` is your checkout) and fetch `origin`.
2. Call `create_workspace` with these fields. `path` names the source checkout; a worktree path there registers a separate project.

   | Field | Value |
   | --- | --- |
   | `isolation` | `worktree` |
   | `mode` | `branch-off`, or `checkout-branch` with `branch` to reuse a branch |
   | `projectId` | Your workspace's `projectId` |
   | `path` | Your workspace's `cwd` |
   | `baseBranch` | `origin/main` |
   | `branchName` | Ticket branch |
   | `worktreeSlug` | Ticket label |
   | `title` | Ticket title or short task description |
   | `background` | `false` |

3. Do steps 2–6 in the returned `cwd`, and start the reviewer in the returned `workspaceId`.

## Reviewer

1. Resolve the `<reviewer>-reviewer` profile using the `paseo` skill. Call `create_agent` in the implementing workspace with round 1's `Read and follow <path>` as `initialPrompt`.
2. Use `send_agent_prompt` with the same `agentId` for later rounds.
3. End the turn after each dispatch and wait for Paseo's completion notification.
