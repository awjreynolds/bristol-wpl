# Bristol WPL Codex authoring pack

1. Create or open a blank local repository.
2. Place `CODEX_MASTER_PROMPT.md` in the repository root.
3. Place your source CSV at `inputs/bristol_wpl_codex_sources.csv` or leave it in the root; the prompt tells Codex to move or copy it.
4. Start Codex from the repository root and instruct it:

   `Read CODEX_MASTER_PROMPT.md in full and execute Section 26. Treat the file as the governing full-simulation programme instruction. Use bounded subagent context packets and agentic simulation sign-offs.`

The prompt requires Markdown and editable DOCX/XLSX outputs. It prohibits authored PDFs and PDFs for officer review/distribution. Raw official PDF source documents may be retained only as immutable evidence when no better official format exists.

All sign-offs produced by the repo are simulation sign-offs only. They are not legal advice, officer approval, financial certification, statutory confirmation, or approval by Bristol City Council, the West of England MCA/WECA, DfT or the Secretary of State.
