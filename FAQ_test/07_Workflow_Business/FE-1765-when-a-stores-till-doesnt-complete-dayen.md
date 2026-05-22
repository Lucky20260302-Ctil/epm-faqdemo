---
project: FE
issue_key: FE-1765
issue_type: Bug PRD
status: DEV Done
tags:
- 07_workflow_business
- faq
- fe
- front-end
- workflow_business
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1765
created: '2025-10-03'
resolved: ''
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1765: When a store''s Till doesn''t complete Dayend, there is no prompt on Till 0 (INC3227274)'
---
# FE-1765: When a store's Till doesn't complete Dayend, there is no prompt on Till 0 (INC3227274)

## 問題描述

Symptom:

When a store's Till doesn't complete Dayend, there is no prompt on Till 0

 

Troubleshooting:

When upgrading to V75 in the Outlet store, it was found that when the dayend of a certain Tile is not completed, there will be no prompt on Tile 0 indicating that the Tile has not completed its dayend. The store will only discover the missing sales of a certain Tile when it needs to complete the total dayend of Tile 0 and print the total dayend report



## 相關資訊

- **Jira:** [FE-1765](https://ctil.atlassian.net/browse/FE-1765)