---
project: FE
issue_key: FE-1569
issue_type: Bug PRD
status: Closed
tags:
- 07_workflow_business
- faq
- fe
- front-end
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1569
created: '2024-11-25'
resolved: '2025-02-12'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1569: [CS-1148] Issue_KR_not able to return items sold from other store RIN01369752 RIN01390154 RIN01388455 CS-1119'
---
# FE-1569: [CS-1148] Issue_KR_not able to return items sold from other store RIN01369752 RIN01390154 RIN01388455 CS-1119

## 問題描述

**Issue Detail**

not able to return item （**this item was not sold in same store**）in KR region

e.g.

OC825 try to return item C3916 B4/BK, original sales memo is OC807 00038691.

after we input qty and return sales memo OC807 00038691, it will show not able to find item C3916 B4/BK in this sales memo. 



## 相關資訊

- **Jira:** [FE-1569](https://ctil.atlassian.net/browse/FE-1569)
- **解決方式:** Done