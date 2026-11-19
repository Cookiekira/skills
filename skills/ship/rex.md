# Rex

Load the `rex` skill.

**Start.** Split beside your pane, rooted in the worktree, and keep the returned `.block_ids[0]` as the reviewer block:

```sh
rex split -s "$REX_SESSION" -b "$REX_BLOCK" --split=right --label reviewer-<label> --focus=false \
  -c "<worktree>" --json -- <reviewer> <bypass flag>
```

**Send.** An agent TUI reads an Enter that arrives right after typed text as part of a paste, and inserts a newline. Type the prompt, pause a few seconds, then press Enter:

```sh
rex send -s "$REX_SESSION" -b <reviewer> "Read and follow <path>"
# pause, then:
rex send-key -s "$REX_SESSION" -b <reviewer> enter
```

It is submitted once `rex capture -s "$REX_SESSION" -b <reviewer> --trim` shows an empty input box; otherwise press Enter again.

**Wait.** A pane gives no finish signal, so the round is done when its report file exists: `until [ -f <report> ]; do sleep 10; done`.
