# Stage 14C History Rewrite Dry-Run Review

Status: simulated review with conditions.
Date: 2026-06-26.
Review roles: Public Release Review Agent, Evidence Librarian, Red Team.

## Review Question

Is there a tested, bounded and reviewable method for removing the Stage 14B detector-collision payloads from reachable git history if the user explicitly approves a force push?

## Findings

1. A non-destructive local mirror dry run was performed under `/private/tmp`.
2. The first failed attempt showed fragile inline Python quoting. The root cause was literal newline escapes and shell regex expansion.
3. The successful attempt moved the rewrite logic into `scripts/stage14b_history_redact.py`.
4. The successful dry run rewrote 31 commits and produced temp rewritten head `7e4c01f1ed0aa3cdbcf3ee33cab5d951aa6dca5a`.
5. The post-rewrite temp scan found no reachable-history matches for the detector patterns.
6. No live remote rewrite or force push was performed.

## Conditions

- Get explicit approval before any live history rewrite or force push.
- Re-run the dry-run or live rewrite from the current `origin/main`, not from stale assumptions.
- Push with a lease, not a blind force push.
- Record the new remote head and post-push GitGuardian disposition.
- Tell downstream users to reclone or hard-reset only after they understand the rewrite.

## Simulated Sign-Off

The Stage 14C dry-run method is fit for a future explicitly approved live history rewrite. It does not itself clean the remote history.
