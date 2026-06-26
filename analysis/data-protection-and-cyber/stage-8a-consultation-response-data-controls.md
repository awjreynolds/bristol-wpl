# Stage 8A Consultation Response Data Controls

Status: simulation control note.  
Date: 2026-06-26.  
Owner: Data Protection Review Agent.

Stage 8A does not collect consultation responses and does not create raw response data.

## Data Separation Rule

Normal repo paths may contain only processed, sanitised, pseudonymous response records after a later launch gate has passed. Raw response exports, direct identifiers, correspondence, free-text files with personal data, accessibility-request details and survey-platform exports must stay in restricted storage outside normal repo paths.

The allowed processed-record shape is controlled by `schemas/consultation-response.schema.json`. The schema requires a pseudonymous response ID, response channel, stakeholder category, response item references, coding status, representativeness metadata, publication-consent control, raw external reference and `personal_data_in_repo=false`.

## Stage 8A Required Controls

- Complete DPIA and lawful-basis assessment before launch.
- Define restricted storage location, access control and audit log outside the public repo.
- Define retention, deletion and publication-redaction rules.
- Define processor, survey-platform and transfer controls.
- Define incident, subject-rights and complaints route controls.
- Check that aggregate consultation reporting does not disclose small-cell or identifiable responses.

## No-Go Position

Consultation launch remains blocked until response-data controls are complete, reviewed and linked to the launch-readiness register.
