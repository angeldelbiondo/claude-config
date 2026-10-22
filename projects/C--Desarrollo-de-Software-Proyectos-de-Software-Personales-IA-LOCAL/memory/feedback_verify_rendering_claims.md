---
name: feedback-verify-rendering-claims
description: "Self-correction: when verifying UI/rendering code without a working screenshot tool, check returned values against the expected/computed value — not just that something returned without error"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 08e2b070-ad9f-42ff-b0e9-c55742557bad
---

## The mistake
Built a WebGL orb for [[project-ia-local-sophia]] (v0.6), verified it via DOM/JS inspection since the screenshot tool was down — checked "WebGL2 context active", "no console errors", "orb object exists", "canvas CSS width returned a value". Declared it working and shipped. Angel opened it for real and got a broken white box with a torn-image icon where the orb should be. Two real bugs were sitting in plain sight in my own diagnostic output the whole time: a canvas stuck at the browser's unstyled default 300×150 (I saw "300px" and didn't check it against what `min(60vmin,620px)` should have produced), and a `gl_PointSize` formula ~80x too large that broke `gl.POINTS` rasterization.

**Why this happened:** I was checking that things *returned a value without throwing*, not that the value *matched what the formula/design should produce*. "It returned 300px" and "it returned the correct px" are different claims, and I only verified the first.

## How to apply
When verifying rendering/visual code and a real screenshot isn't available:
1. **Compute the expected value by hand first**, then compare the actual returned value against it — don't just check that a property exists or returned *something*.
2. **If a visual bug is suspected and can't be seen directly, isolate variables one at a time** (strip a shader/component down to its simplest form, confirm the base case works, then add pieces back one by one) rather than guessing at the whole system or re-reading code hoping to spot it. This found the actual bug (an ~80x scale error in a point-size formula) in a few isolated tests after a lot of unproductive theorizing from reading code alone.
3. Reading a vendored library's actual source (grep the real minified file) to check an API assumption beat continuing to guess from training-knowledge memory of that library's behavior.
4. Say explicitly when a verification pass was DOM/console-only because visual tooling was unavailable — don't let "no errors" read as "confirmed working" to the user.
