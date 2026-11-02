# Reviewer in Rex

Load the `rex` skill.

**Start or reuse.** Reuse the pane labelled `reviewer` from `rex block ls -s "$REX_SESSION"` while it still runs Codex. Otherwise start one beside your pane, and save the returned `.block_ids[0]` as the reviewer block:

```sh
rex split -s "$REX_SESSION" -b "$REX_BLOCK" --split=right --label reviewer --focus=false \
  -c "<repo>" --json -- codex -s workspace-write --add-dir "<scratchpad>"
```

`--add-dir` lets the reviewer write its report into the scratchpad.

**Send.** Codex reads an Enter that arrives right after typed text as part of a paste, and inserts a newline. Type the prompt, pause a few seconds, then press Enter:

```sh
rex send -s "$REX_SESSION" -b <reviewer> "Read and follow <path>"
# pause, then:
rex send-key -s "$REX_SESSION" -b <reviewer> enter
```

Then capture the pane with `rex capture -s "$REX_SESSION" -b <reviewer> --trim`. It is submitted once it shows `Working`. If the prompt still sits in the input box, press Enter again. Send `/new` the same way.

**Wait.** The round is done when its report file exists. Run `until [ -f <report> ]; do sleep 10; done` as a background Bash command with a 1800000 ms timeout, and wait for its notification.
