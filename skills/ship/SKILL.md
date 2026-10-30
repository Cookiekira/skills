---
name: ship
description: "Implement a ticket, ablate speculative defenses and shallow abstractions, loop a Codex thermo-nuclear review in Herdr until PASS, then open the PR."
disable-model-invocation: true
---

# Ship

Take one ticket from implementation to an open, green PR. The argument is a ticket reference (`#926`) or a short task description.

## 1. Implement

1. If given a ticket, run `gh issue view <n>` and state its title. Branch from a fresh `origin/main`.
2. Implement it, following the repo's `AGENTS.md`.
3. Validate with the repo's commands, then commit.

Done when the ticket's acceptance criteria are met, validation passes, and the work is committed.

## 2. Ablate

Ablation deletes two things from `git diff origin/main...HEAD`:

- **Speculative defense**: a guard, fallback, retry, re-validation, `die`, or optional field for a state that the types, the callers, a database constraint, or the owning module already rule out.
- **Shallow abstraction**: a helper, wrapper, type alias, option, or parameter that has one caller or one value, and that adds a name without hiding a decision.

Inline or delete each one. Delete the tests that only covered the deleted pieces, and the tests that mirror the implementation.

Keep **behaviour**: a branch that produces a distinct observable outcome (a status, a stored row, a webhook result, a message) is not a defense, even when it looks like one. Keep guards at untrusted seams, such as request input, webhooks, and external services.

Done when every guard and every newly named abstraction in the diff is either deleted, or you can name the real caller or reachable state that needs it. Then validate and commit.

## 3. Review loop

Load the `herdr` skill.

### Reviewer

Reuse a live Codex agent with `herdr agent list`, and send it `/new` if it reviewed earlier work. If there is none, split a pane to the right and start one with `--kind codex`, named `reviewer`.

A prompt sent while `/new` is still resetting is dropped, even after `/new --wait` returns. After every prompt, check that `herdr agent get <reviewer>` reports `working`, and resend it if the agent is still `idle`.

### Prompt

For round `n`, write the prompt to `<scratchpad>/review-<n>-prompt.md`. Then send only `Read and follow <that path>`. This keeps quoting out of the shell. The prompt says:

- `$thermo-nuclear-code-quality-review` on `git diff origin/main...HEAD`, at HEAD `<sha>`. Include untracked files if any.
- The intent: the ticket number (read it with `gh issue view`) and one paragraph on the design.
- Apply `AGENTS.md` and `CODING_STANDARDS.md`, and flag speculative defenses and shallow abstractions.
- From round 2 on: what each previous finding became (fixed in `<sha>`, or declined and why).
- Do not edit files.
- Write the report to `<scratchpad>/review-<n>.md`, ending with `VERDICT: PASS` or `VERDICT: FAIL`. Reply with only that path.

### Running a round

Run `herdr agent prompt <reviewer> "Read and follow <path>" --wait --timeout 1800000` as a background Bash command, and wait for its notification. Read the report file, not the pane.

### Handling findings

For each finding, either fix it or decline it with a reason. A finding is declined when it contradicts an ADR, the ticket, or the user's instructions. Ablate the fixes as in step 2, validate, and commit. Then start round `n+1`.

If the reviewer repeats a finding you declined across two rounds, stop and ask the user to decide.

Done when the report for the current HEAD ends with `VERDICT: PASS`.

## 4. Show the UI change

Skip this step when the diff changes no rendered UI.

Ask the reviewer for before/after screenshots, using the prompt in [`ui-shots.md`](ui-shots.md), run like a review round. When it reports back, look at the "after" shots yourself and check that each one shows the intended change. Then open every shot for the user with one `open` call, so they appear together as before/after pairs.

Done when every changed screen has a "before" and an "after" shot, you have checked each "after" shot, and all of them are open on the user's screen.

## 5. Open the PR

Write the body with the `pr` skill, push, and run `gh pr create`. Then watch CI with `gh pr checks --watch`, and fix any failures.

Done when CI is green. Report:

- the PR URL
- the number of review rounds
- the findings you declined, with reasons

Merge only when the user asks.
