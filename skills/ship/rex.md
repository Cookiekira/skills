# Rex

Load the `rex` skill.

**Start.** Start the reviewer beside your pane, rooted in the worktree, and save the returned `.block_ids[0]` as the reviewer block:

```sh
rex split -s "$REX_SESSION" -b "$REX_BLOCK" --split=right --label reviewer-<label> --focus=false \
  -c "<worktree>" --json -- <reviewer command>
```

**Send.** An agent TUI reads an Enter that arrives right after typed text as part of a paste, and inserts a newline. Type the prompt, pause a few seconds, then press Enter:

```sh
rex send -s "$REX_SESSION" -b <reviewer> "Read and follow <path>"
# pause, then:
rex send-key -s "$REX_SESSION" -b <reviewer> enter
```

Then capture the pane with `rex capture -s "$REX_SESSION" -b <reviewer> --trim`. It is submitted once the input box is empty and the agent shows it is working; if the prompt still sits there, press Enter again.

**Wait.** The round is done when its report file exists. Run `until [ -f <report> ]; do sleep 10; done` with a 1800000 ms timeout.
