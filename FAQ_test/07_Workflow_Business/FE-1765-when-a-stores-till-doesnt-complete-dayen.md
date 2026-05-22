---
project: FE
title: "FE-1765: When a store's Till doesn't complete Dayend, there is no prompt on Till 0 (INC3227274)"
issue_key: FE-1765
issue_type: Bug PRD
status: DEV Done
faq_score: 5.5
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, fe, workflow_business, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1765"
created: 2025-10-03
resolved: 
resolution: 
has_images: False
---

# FE-1765: When a store's Till doesn't complete Dayend, there is no prompt on Till 0 (INC3227274)

## 問題描述

Symptom:

When a store's Till doesn't complete Dayend, there is no prompt on Till 0

 

Troubleshooting:

When upgrading to V75 in the Outlet store, it was found that when the dayend of a certain Tile is not completed, there will be no prompt on Tile 0 indicating that the Tile has not completed its dayend. The store will only discover the missing sales of a certain Tile when it needs to complete the total dayend of Tile 0 and print the total dayend report



## 相關資訊

- **Jira:** [FE-1765](https://ctil.atlassian.net/browse/FE-1765)