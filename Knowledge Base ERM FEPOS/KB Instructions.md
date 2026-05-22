You are helping create a structured troubleshooting note from a Jira ticket.

## Instructions

1. Read the Jira ticket carefully (problem, root cause, solution, comments)
2. Create a Markdown note following the exact format below

## Output Format
---
tags: [bug, jira, production]  # Add: production, uat, hotfix, change-request if applicable
component: [inferred component]
symptom: "[brief symptom description in 1 sentence]"
root-cause: "[root cause in 1-2 sentences, or empty if unknown]"
solution: "[solution in 1-2 sentences, or empty if unknown]"
jira: [TICKET-KEY]
resolved: [YYYY-MM-DD]
---

# [TICKET-KEY]: [Ticket Summary]

## 問題

[Full problem description — paste key details, link references, capture images]

## 根因

[Root cause explanation, investigation findings, or diagnosis steps]

## 解法

[Solution/fix description, code snippets if applicable]
_See Jira ticket for resolution details._  (use this if solution is unknown)

## 相關問題

- [[RELATED-TICKET-1]]
- [[RELATED-TICKET-2]]
markdown
Rules
Root cause section: extract from "root cause" or investigation comments
Solution section: extract from "solution" or "fix" sections
Keep Chinese section headers (問題, 根因, 解法)
Skip transient status updates — only document real technical content
Tag with #jira/ TICKET -KEY for cross-referencing