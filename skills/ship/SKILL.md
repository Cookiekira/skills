---
name: ship
description: "Implement a ticket in its own worktree, ablate speculative defenses and shallow abstractions, loop a cross-model thermo-nuclear review in Herdr, Rex, or Paseo until PASS, show before/after UI screenshots, then open the PR."
disable-model-invocation: true
---

# Ship

Start in a worktree for the ticket or short task the user gave you.

## 1. Open the worktree

If this checkout is a linked worktree, go to step 2. Otherwise, open one below and do every later step in it.

For a new worktree, read the ticket with `gh issue view <n>` and state its title. Use `<ticket number>-<two-word slug>` as the label. For a short task, use a two to four word slug. Name the branch using the repo's convention.

- **Paseo.** If `PASEO_AGENT_ID` is set, follow [Paseo workspace setup](paseo.md#workspace).
- **Other environments.** Run `<skill dir>/worktree.sh <label> <branch>` and enter the worktree it prints.

## 2. Implement

1. If the user gave a ticket and you have yet to read it, run `gh issue view <n>` and state its title.
2. In a new worktree, run `<skill dir>/link-env.sh`, install dependencies with the repo's package manager, and run the generation steps the repo's CI runs before its checks.
3. Implement the ticket under the repo's `AGENTS.md`. Check the acceptance criteria, validate, and commit. To **validate**, run the repo's validation commands over every file the branch changes (`git diff --name-only origin/main...HEAD`), so callers and tests outside the latest edit run too.

## 3. Ablate

1. Read `git diff origin/main...HEAD`. Remove speculative defenses for states that types, callers, a database constraint, or the owning module already rule out. Inline or delete shallow abstractions that have one caller or value and hide no decision.
2. Keep guards at untrusted inputs and external integrations. Preserve distinct observable outcomes, such as a status, stored row, webhook result, or message. Remove tests that only cover deleted code or mirror the implementation.
3. Name the caller or reachable state that needs each remaining guard and new abstraction. Validate and commit.

## 4. Review

### Start the reviewer

Start one unattended reviewer for the ticket with its bypass-approvals flag or mode. Use Codex when Claude implements and Claude when Codex implements. Keep the same reviewer for every round.

- **Herdr.** If `HERDR_ENV=1`, follow [Herdr reviewer setup](herdr.md).
- **Rex.** If `REX_SESSION` is set, follow [Rex reviewer setup](rex.md).
- **Paseo.** If `PASEO_AGENT_ID` is set, follow [Paseo reviewer setup](paseo.md#reviewer).

### Run a round

1. Write `<scratchpad>/review-<n>-prompt.md` using the instructions below.
2. Send only `Read and follow <prompt path>` and wait using the reviewer recipe.
3. Read `<scratchpad>/review-<n>.md`. Move to step 5 when the report for the current HEAD ends with `VERDICT: PASS`.
4. Weigh each finding as a peer's argument and own the call. Fix it, or decline it with a concrete reason: the ADR, ticket requirement, or user instruction it contradicts, or the cost that outweighs what it protects. Keep a declined finding declined unless the reviewer brings new evidence. If the reviewer repeats it across two rounds, pause the loop and ask the user, stating both positions.
5. Ablate any fixes, validate, commit, and run the next round.

### Write the review prompt

Give the reviewer the worktree path, HEAD SHA, ticket number if available, and one paragraph on the design. After round 1, list the fix commit or reason for declining each finding from the last round. Include these instructions for the reviewer.

1. Read the ticket with `gh issue view` if given a number. Follow `~/.agents/skills/thermo-nuclear-code-quality-review/SKILL.md` and apply `AGENTS.md` and `CODING_STANDARDS.md`.
2. Review `git diff origin/main...HEAD` and any untracked files. Flag speculative defenses and shallow abstractions. Leave the checkout untouched.
3. Write the report to `<scratchpad>/review-<n>.md` and end it with `VERDICT: PASS` or `VERDICT: FAIL`. Reply with the report path only.

## 5. Show UI changes

Continue at step 6 if the diff changes no rendered UI.

1. Send the reviewer [the screenshot prompt](ui-shots.md) using the same send and wait steps as a review round.
2. Verify that each changed screen has a before and after shot and that the after shot shows the intended change.
3. Open all shots for the user with one `open` call.

## 6. Open the PR

1. Write the body with the `pr` skill, push the branch, and run `gh pr create`.
2. Run `gh pr checks --watch` and fix failures until CI passes.
3. Report the PR URL, review round count, and any declined findings with reasons.

Merge only when the user asks.
