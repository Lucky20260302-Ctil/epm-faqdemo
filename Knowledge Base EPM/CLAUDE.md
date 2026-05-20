# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project context

A knowledge base linked to Jira tickets, stored as an Obsidian vault. Notes use
Obsidian-flavored Markdown with `[[wiki-links]]`, frontmatter, and backlinks.

## Vault structure

```
├── 01-Inbox/           # Raw, unsorted notes — draft before filing elsewhere
├── 02-Projects/        # Active project notes (one subfolder per project)
├── 03-Resources/       # Permanent reference knowledge
│   └── jira-knowledge/ # Wiki-style knowledge distilled from Jira tickets
├── 04-Templates/       # Note templates for new notes
└── .obsidian/          # Obsidian plugin/config — NEVER modify
```

## Safety rules

- NEVER modify files in `.obsidian/` unless explicitly asked
- Ask before moving or deleting files
- Default to read-only analysis first — examine context before proposing changes

## Knowledge base patterns

- Use `[[wikilinks]]` to connect related notes; `[[note|alias]]` for display text
- Tag Jira-linked notes with `#jira/PROJ-123` to connect notes to tickets
- Frontmatter example:

  ```yaml
  ---
  tags: [jira, resolved]
  related-ticket: PROJ-123
  resolved-date: 2025-01-15
  ---
  ```

- Inbox items should be moved to the appropriate folder once they mature
- `04-Templates/` notes are used via Obsidian's "Insert template" — keep placeholders generic

## How Claude should interact

- Create new notes in `01-Inbox/` unless the user specifies a destination
- When the user asks to "file" or "organize" a note, move it to `02-Projects/` or `03-Resources/`
- When creating notes from Jira tickets, distill technical decisions, rationale, and outcome — skip transient status updates. File in `03-Resources/jira-knowledge/`
