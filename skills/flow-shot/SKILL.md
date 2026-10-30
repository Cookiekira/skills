---
name: flow-shot
description: Stitch screenshots into one annotated flow image, with numbered steps and arrows showing the order of operations.
disable-model-invocation: true
---

# Flow shot

Turn a sequence of screenshots into one image that walks a reader through an operation: each panel captioned, each click target boxed and numbered, arrows joining the steps in order. The screenshots are the user's pasted images or shots you took.

1. **Panels.** List the screenshots in operation order and read each one's pixel size. When an image is shown to you scaled, multiply what you read by the stated factor to get source pixels.
2. **Targets.** For each step, find the rect of the element the reader acts on (button, tab, field), in that panel's source pixels. Group steps per panel; each panel gets a caption naming its steps in the user's language, with UI labels kept verbatim.
3. **Spec.** Write `<scratchpad>/flow/spec.json` in the format at the top of [`compose.py`](compose.py). Route each arrow from one target to the next through empty space: within a panel along blank rows and columns, and between panels via the `"lane"` column and the next panel's `"gap"` strip.
4. **Render and look.** Run `python3 -I <this skill directory>/compose.py <spec> <scratchpad>/flow/<topic>-flow.png`, then Read the output. Fix every arrow, box, or badge that covers text (move a badge with `"badge": "below"` or `"right"`, reroute an arrow) and render again. Done when no annotation covers any text and every step number follows its arrow.
5. **Privacy.** Look for names, emails, and customer details in the panels. Blur them with `"redact"` when the user says the image is going to others; otherwise name what is visible and offer to blur it.
6. **Open** the image with `open <path>` and give its full path.
