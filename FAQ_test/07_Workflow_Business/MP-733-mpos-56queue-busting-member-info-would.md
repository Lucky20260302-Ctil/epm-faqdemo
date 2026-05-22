---
project: MP
title: "MP-733: [MPOS-56]Queue Busting - Member Info would be cleared out after update on MPOS"
issue_key: MP-733
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, mp, workflow_business, mpos, mpos-api]
jira_url: "https://ctil.atlassian.net/browse/MP-733"
created: 2024-12-01
resolved: 2025-02-24
resolution: Done
has_images: False
---

# MP-733: [MPOS-56]Queue Busting - Member Info would be cleared out after update on MPOS

## 問題描述

Issue - JP - Memo＆Customer Info will be cleaned up when call out transaction in MPOS

Reproduce steps:

Issue sales in MPOS >>Send to POS >> call out transaction in MPOS to modify items>>Send to POS once again(Memo & customer info became blank)



## 相關資訊

- **Jira:** [MP-733](https://ctil.atlassian.net/browse/MP-733)
- **解決方式:** Done