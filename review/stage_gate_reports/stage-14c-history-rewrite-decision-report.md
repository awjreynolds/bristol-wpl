# Stage 14C History Rewrite Decision Report

Status: dry run complete; live rewrite blocked pending explicit approval.
Date: 2026-06-26.

## Gate Decision

Stage 14C passes only as a dry-run and decision-control stage.

It does not rewrite the live GitHub repository, close GitGuardian, revoke or rotate any token, or change the no-go position for WPL approval, OBC, FBC, consultation or statutory submission.

## Evidence Checked

- `scripts/stage14b_history_redact.py`.
- Temporary mirror clone dry run.
- Successful `git filter-branch` run over `refs/heads/main` and `refs/remotes/origin/main`.
- Deletion of temp `refs/original/*` backup refs.
- Temp reflog expiry and aggressive garbage collection.
- Redacted reachable-history scan of the rewritten temp mirror.

## Dry-Run Result

The temp rewritten `main` head was:

```text
7e4c01f1ed0aa3cdbcf3ee33cab5d951aa6dca5a
```

The rewritten temp mirror retained 31 commits and returned no detector-pattern matches in reachable rewritten history.

## Residual Position

- Live `origin/main` remains at `306cf0688726e6f8b4b2a5532b035cbc42bdcfc6` until an approved force-push changes it.
- GitHub/GitGuardian alert disposition is still external to this repo.
- Any real Grafana token must be revoked or rotated outside git.
- Forks, caches and old clones may retain old objects even after a force push.

## Approval Required

Do not proceed to a live history rewrite without explicit user approval that names the repository and acknowledges that `main` history will be replaced and force-pushed.

## Simulated Gate Sign-Off

The dry-run rewrite path is accepted for simulation purposes. Live history rewrite remains blocked pending explicit approval.
