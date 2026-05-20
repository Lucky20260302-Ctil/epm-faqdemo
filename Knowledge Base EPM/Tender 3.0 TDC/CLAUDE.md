# CLAUDE.md

This file provides guidance to Claude Code when working in this vault.

## Project context

A knowledge base for the **Tender 3.0 TDC** project. This vault tracks tender documentation, requirements, submissions, evaluations, and decisions related to the Tender 3.0 technology/development project. Notes use Obsidian-flavored Markdown with `[[wiki-links]]`, frontmatter, and backlinks.

## Vault structure

```
├── 01-Inbox/           # Raw, unsorted notes — draft before filing elsewhere
├── 02-Projects/        # Active project notes (project phases, milestones)
│   └── tender-3.0-tdc/ # Core Tender 3.0 TDC project documentation
├── 03-Resources/        # Permanent reference knowledge
│   ├── standards/       # Industry standards, compliance requirements
│   ├── troubleshooting/ # KB notes distilled from resolved Jira bugs
│   ├── jira-knowledge/  # Wiki-style knowledge distilled from Jira tickets
│   └── references/      # External reference materials
├── 04-Templates/       # Note templates for new notes
│   ├── tender-note.md  # Template for tender-related notes
│   └── meeting-note.md # Template for meeting minutes
└── .obsidian/          # Obsidian plugin/config — NEVER modify
```

## Safety rules

- NEVER modify files in `.obsidian/` unless explicitly asked
- Ask before moving or deleting files
- Default to read-only analysis first — examine context before proposing changes

## Knowledge base patterns

- Use `[[wikilinks]]` to connect related notes; `[[note|alias]]` for display text
- Tag notes with relevant tags: `#tender`, `#tdc`, `#submission`, `#evaluation`, `#compliance`
- Tag Jira-linked notes with `#jira/PROJ-123` to connect notes to tickets
- Frontmatter example:

  ```yaml
  ---
  tags: [tender, tdc, submission]
  related-ticket: PROJ-123
  status: draft|submitted|evaluated|awarded
  date: 2026-05-18
  ---
  ```

- Inbox items should be moved to the appropriate folder once they mature
- `04-Templates/` notes are used via Obsidian's "Insert template" — keep placeholders generic

## How Claude should interact

- Create new notes in `01-Inbox/` unless the user specifies a destination
- When the user asks to "file" or "organize" a note, move it to `02-Projects/` or `03-Resources/`
- When creating notes from Jira tickets, distill technical decisions, rationale, and outcome — skip transient status updates. File in `03-Resources/jira-knowledge/`
- For tender-specific content (RFP responses, submission docs, evaluations), use `02-Projects/tender-3.0-tdc/`
