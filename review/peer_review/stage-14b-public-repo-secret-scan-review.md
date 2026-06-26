# Stage 14B Public Repo Secret-Scan Review

Status: simulated review with conditions.
Date: 2026-06-26.
Review roles: Public Release Review Agent, Evidence Librarian, Red Team.

## Review Question

Does the repository now have a controlled current-tree response to the GitGuardian Grafana-token-pattern alert without overstating what has been remediated?

## Findings

1. The current-tree token-pattern hit was traced to public Bristol committee-pack evidence, not a local credentials file.
2. The matched pattern is consistent with public Power BI report identifiers that collide with legacy Grafana-token detection.
3. The current tree must still be cleaned because hosted public-repo secret scanners will continue to flag the pattern regardless of whether it is a false positive.
4. The remediation removes the three raw PDFs from the current tree and redacts extracted text where the pattern appears.
5. The source register keeps the official URLs, hashes and omission rationale, so the evidence trail is not silently erased.
6. `scripts/scan_secrets.py` avoids printing secret values and is now part of validation.
7. Git history still contains prior blobs until a separate, explicitly approved history rewrite is performed.

## Conditions

- Do not describe this as token revocation, token safety or GitGuardian closure.
- Do not re-add the omitted raw PDFs to the public repository.
- Do not run a history rewrite or force push without explicit user approval.
- Re-run `make secrets-qa` before future public pushes or source acquisition refreshes.

## Simulated Sign-Off

The Stage 14B current-tree remediation and controls are fit for simulation use. They do not replace external secret revocation, hosted-alert triage, legal review or any real-world security assurance.
