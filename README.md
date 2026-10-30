# skills

Agent skills by [@Cookiekira](https://github.com/Cookiekira), installable with the [`skills`](https://github.com/vercel-labs/skills) CLI.

```sh
npx skills add Cookiekira/skills            # pick from the list
npx skills add Cookiekira/skills -s ship -g # one skill, user-level
```

| Skill | What it does | Needs |
| --- | --- | --- |
| [`ship`](skills/ship) | Takes one ticket to an open, green PR: implement, ablate speculative defenses, loop a Codex review in Herdr until it passes, show before/after UI screenshots, open the PR. Invoke with `/ship #123`. | `gh`, [Herdr](https://github.com/herdrdev/herdr) with Codex, the `herdr`, `pr` and `thermo-nuclear-code-quality-review` skills |
| [`flow-shot`](skills/flow-shot) | Stitches screenshots into one image with captioned panels, numbered click targets, and arrows showing the order of operations. Invoke with `/flow-shot`. | macOS, Python 3 with Pillow |

Both skills are user-invoked (`disable-model-invocation: true`): the agent runs them only when you type their name.
