---
name: sync-jira-kb
description: Sync closed Jira bugs into Obsidian troubleshooting KB. Fetches resolved bugs with root cause/solution/fix mentions, distills into structured notes, and rebuilds the MOC index.
---

# Sync Jira KB

Synchronizes closed Jira bugs (EPMTDCPROT project) into `03-Resources/troubleshooting/` as structured troubleshooting notes.

## Workflow

1. **Search** — JQL: `project = EPMTDCPROT AND status = Closed AND resolution IS NOT NULL AND (text ~ "root cause" OR text ~ "solution" OR text ~ "fix")`
2. **Filter** — Parse ADF description locally; keep only tickets where description contains `root cause`, `solution`, or `fix`
3. **Fetch comments** — Get resolution notes for each ticket via API
4. **Distill** — Extract symptom, component, root-cause, solution into frontmatter + sections
5. **Write files** — `03-Resources/troubleshooting/{KEY}-troubleshooting.md`
6. **Build MOC** — Regenerate `index.md` grouped by symptom type and component

## Usage

```bash
# Full refresh (all time)
python3 scripts/distill_jira_kb.py

# Last 7 days only (daily cron use)
python3 scripts/distill_jira_kb.py --days 7

# Quiet mode (no console output, for cron)
python3 scripts/distill_jira_kb.py --days 7 --quiet
```

## File Output

```
03-Resources/troubleshooting/
├── index.md                              # MOC (依症狀 / 依元件 / 完整列表)
├── EPMTDCPROT-3389-troubleshooting.md     # one note per ticket
├── EPMTDCPROT-3450-troubleshooting.md
└── ...
```

## Note Template

```yaml
---
tags: bug, production, ...
component: Tender & RFQ
symptom: "一句話現象"
root-cause: "一句話根因"
solution: "一句話解法"
jira: EPMTDCPROT-XXXX
resolved: 2026-05-13
---
```

## Scheduling

Already configured to run daily at 10:00 AM via cron.
