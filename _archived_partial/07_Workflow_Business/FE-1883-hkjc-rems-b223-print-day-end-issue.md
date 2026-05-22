---
project: FE
issue_key: FE-1883
issue_type: Bug PRD
status: Selected for Development (migrated)
tags:
- 07_workflow_business
- faq
- fe
- front-end-v750.01r01a
- workflow_business
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1883
created: '2026-02-10'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1883: HKJC REMS B223 Print Day End Issue'
---
# FE-1883: HKJC REMS B223 Print Day End Issue

## 問題描述

As B223 reported EWIN223PC1 got print day end issue - print to EPSON TM-L90 Label printer. But the correct print queue should be OCB223MFD01. Tried to reprint day end, it seems only set OCB223MFD01 as default printer, then system able to print it in this print queue.

> 📎 **image-20260210-021729.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/afe82bd2-d943-4fca-90e6-b0a469d8780d)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260210-021729.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/afe82bd2-d943-4fca-90e6-b0a469d8780d)

## 相關資訊

- **Jira:** [FE-1883](https://ctil.atlassian.net/browse/FE-1883)
- **標籤:** DAYEND