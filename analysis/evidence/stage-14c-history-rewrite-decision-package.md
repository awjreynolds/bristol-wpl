# Stage 14C History Rewrite Decision Package

Status: dry run complete; destructive remote action not approved.
Date: 2026-06-26.

## Purpose

Stage 14B cleaned the current public tree after the GitGuardian Grafana-token-pattern alert. Stage 14C tests whether the same collision can be removed from reachable git history without acting on the real remote.

This is a decision package only. It does not rewrite the live repository.

## Dry-Run Scope

The dry run used a temporary local mirror clone:

```text
/private/tmp/bristol-wpl-history-test.nj3SaW/bristol-wpl.git
```

The rewrite helper was:

```text
scripts/stage14b_history_redact.py
```

The helper removes these paths from every rewritten commit:

```text
evidence/raw/bristol-city-council/src-bcc-0005_public-reports-pack-transport-connectivity-policy-committee-2024-09-12.pdf
evidence/raw/bristol-city-council/src-bcc-0011_public-reports-pack-transport-connectivity-policy-committee-2025-10-23.pdf
evidence/raw/bristol-city-council/src-bcc-0015_public-reports-pack-transport-connectivity-policy-committee-2026-03-19.pdf
```

It also redacts token-detector collision payloads in:

```text
evidence/processed/text/SRC-BCC-0011.txt
```

## Dry-Run Result

- Original live `main` head before rewrite action: `306cf0688726e6f8b4b2a5532b035cbc42bdcfc6`.
- Rewritten temp `main` head: `7e4c01f1ed0aa3cdbcf3ee33cab5d951aa6dca5a`.
- Rewritten temp commit count: 31.
- Rewritten temp reachable-history detector scan: no matches.

## Tested Commands

The successful dry-run rewrite used:

```bash
git clone --mirror /Users/awjre/Work/transport/bristol-wpl /private/tmp/bristol-wpl-history-test.nj3SaW/bristol-wpl.git
cd /private/tmp/bristol-wpl-history-test.nj3SaW/bristol-wpl.git
FILTER_BRANCH_SQUELCH_WARNING=1 git filter-branch --force --tree-filter 'python3 /Users/awjre/Work/transport/bristol-wpl/scripts/stage14b_history_redact.py' -- refs/heads/main refs/remotes/origin/main
git update-ref -d refs/original/refs/heads/main
git update-ref -d refs/original/refs/remotes/origin/main
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

The successful dry-run scan used a redacted path-only pattern scan over reachable rewritten refs. It did not print token values.

## Approval Boundary

A live history rewrite would require replacing `origin/main` with rewritten history. That is disruptive:

- existing clones will need to fetch and reset or reclone;
- open PRs and branch references may need repair;
- GitHub-hosted secret scanning may take time to re-evaluate;
- any forks can still retain the old objects;
- a real issued Grafana token must still be revoked or rotated outside git.

Do not force-push on a vague instruction such as "continue". Require explicit approval naming the repo and the force-push risk.

## Current Recommendation

If the GitGuardian alert remains open after the Stage 14B current-tree cleanup, proceed only after explicit approval to perform the Stage 14C history rewrite and force-push.
