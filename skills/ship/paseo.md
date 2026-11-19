# Paseo

Load the `paseo` skill.

## Workspace

1. Get your `workspaceId` with `get_agent_status` and find it in `list_workspaces`. If it is a worktree workspace on the ticket branch, go to step 2 in [Ship](SKILL.md#2-implement).
2. Choose the ticket label and branch as in [Ship step 1](SKILL.md#1-open-the-worktree). Fetch `origin`. Call `create_workspace` with the current workspace's `projectId` and checkout path, plus these fields.

   | Field | Value |
   | --- | --- |
   | `isolation` | `worktree` |
   | `mode` | `branch-off` |
   | `baseBranch` | `origin/main` |
   | `branchName` | Ticket branch |
   | `worktreeSlug` | Ticket label |
   | `title` | Ticket title or short task description |
   | `background` | `false` |

3. Call `create_agent` with the new `workspaceId`, your `provider/model`, and your mode, thinking option, and feature values in `settings`. Use this plain-text `initialPrompt`.

   > Read `<absolute path to ship/SKILL.md>`. For `<original ticket or task>`, verify that this workspace is on `<branch>`, then follow Ship from step 2.

4. Report the new workspace and branch. The new agent continues the run.

## Reviewer

1. Resolve the `<reviewer>-reviewer` profile using the `paseo` skill. Call `create_agent` in the implementing workspace with round 1's `Read and follow <path>` as `initialPrompt`.
2. Use `send_agent_prompt` with the same `agentId` for later rounds.
3. End the turn after each dispatch and wait for Paseo's completion notification.
