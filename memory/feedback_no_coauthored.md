---
name: No Co-Authored-By in commits
description: User does not want the Co-Authored-By Claude signature in git commit messages
type: feedback
---

Never include `Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>` in git commit messages.

**Why:** User explicitly requested this — they don't want Claude's signature appearing in their commit history.

**How to apply:** When creating any git commit for this user, write only the commit message itself with no Co-Authored-By trailer.
