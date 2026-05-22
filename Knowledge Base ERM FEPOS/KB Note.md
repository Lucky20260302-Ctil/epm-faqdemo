# CLAUDE.md

This file provides guidance to Claude Code when working in this vault.

## Project context

A knowledge base for the FEPOS project. This vault tracks [describe your project]. Notes use Obsidian-flavored Markdown with `[[wiki-links]]`, frontmatter, and backlinks.

## Vault structure

```
├── 01-Inbox/           # Raw, unsorted notes — draft before filing elsewhere
├── 02-Projects/        # Active project notes (project phases, milestones)
│   └── your-project/   # Core project documentation
├── 03-Resources/       # Permanent reference knowledge
│   ├── standards/      # Industry standards, compliance requirements
│   ├── troubleshooting/ # KB notes distilled from resolved Jira bugs
│   ├── jira-knowledge/ # Wiki-style knowledge distilled from Jira tickets
│   └── references/     # External reference materials
├── 04-Templates/       # Note templates for new notes
└── .obsidian/          # Obsidian plugin/config — NEVER modify
```

## Safety rules

- NEVER modify files in `.obsidian/` unless explicitly asked
- Ask before moving or deleting files
- Default to read-only analysis first — examine context before proposing changes

## Knowledge base patterns

- Use `[[wikilinks]]` to connect related notes; `[[note|alias]]` for display text
    
- Tag notes with relevant tags: `#your-tag`, `#project`
    
- Tag Jira-linked notes with `#jira/PROJ-123` to connect notes to tickets
    
- Frontmatter example:
    
    ```yaml
    ---
    tags: [project, submission]
    related-ticket: PROJ-123
    status: draft|submitted|in-review|completed
    date: 2026-05-18
    ---
    ```
    
    yaml
    
- Inbox items should be moved to the appropriate folder once they mature
    
- `04-Templates/` notes are used via Obsidian's "Insert template" — keep placeholders generic
    

Thought

I see the CLAUDE.md instructions for working in this vault. I'm ready to help!

What would you like me to work on? I can help with:

- **Reading and organizing notes** in your vault
- **Creating or editing notes** following your vault's conventions
- **Searching across your knowledge base** for specific topics
- **Code analysis** using external context paths you provide
- **Jira knowledge management** following your folder structure
- Any specific questions you have about the FEPOS project or your vault content

Just let me know what you need!

Step 1：從 Jira 找到已解決的問題

我可以幫你用 Jira JQL 搜尋已解決的 ticket，只篩選「有技術決策、有根因分析」的：

project =  
Frontend AND status = Closed AND release IS NOT NULL  
AND (description ~ "root cause" OR description ~ "solution" OR description ~ "fix")

Step 2：output format as below

---

tags:  
component:  
symptom:  
root-cause: "  
jira Ticket no:  
date-resolved:

---

## 問題

## 診斷方法

## 解決方案

## 預防措施

## 相關問題ticket no

Step 3：建立索引（MOC）

03-Resources/troubleshooting/index.md 用 MOC 模式組織所有問題：

---

---

---

---

# 解決手冊

## 依症狀

## 依元件