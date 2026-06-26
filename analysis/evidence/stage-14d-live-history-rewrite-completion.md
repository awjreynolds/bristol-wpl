# Stage 14D Live History Rewrite Completion

Status: live history rewrite completed and verified; hosted alert disposition still external.
Date: 2026-06-26.

## Purpose

Stage 14D records the approved live execution of the Stage 14C history-rewrite plan.

This stage removes the Stage 14B detector-collision blobs from reachable `main` history on GitHub. It does not revoke or rotate any external token and does not guarantee that GitGuardian has closed its hosted alert.

## Approval Basis

The user approved the live history rewrite after Stage 14C documented the dry-run method and force-push boundary.

## Execution Summary

The live rewrite was run from a fresh mirror clone of:

```text
https://github.com/awjreynolds/bristol-wpl.git
```

The protected force push used an exact lease against the pre-rewrite remote head:

```text
20f48c2cf815ab635051a7fb78b69f80c78ee508
```

The remote forced update moved `main` to:

```text
8a407b9f0e4b48fd6fc0939eb1ead3706e10b9de
```

## Verification Evidence

Verification after the force push:

- `git ls-remote origin refs/heads/main` returned `8a407b9f0e4b48fd6fc0939eb1ead3706e10b9de`.
- Local `HEAD` was reset to match rewritten `origin/main`.
- `python3 scripts/scan_secrets.py` passed in the local working tree.
- `python3 scripts/scan_secrets.py --all-history` passed locally.
- A fresh post-rewrite remote mirror clone returned `8a407b9f0e4b48fd6fc0939eb1ead3706e10b9de` for `refs/heads/main`.
- The fresh remote mirror reachable-history detector scan returned no matches.
- The fresh remote mirror retained 32 commits on `main`.

## Residual Caveats

- GitGuardian hosted alert disposition is outside this repository and must be checked in GitGuardian.
- Old local clones, forks, GitHub caches or third-party mirrors can retain old objects.
- Any genuinely issued Grafana token must be revoked or rotated outside git.
- Contributors with old clones should reclone or reset to the rewritten `origin/main`.
