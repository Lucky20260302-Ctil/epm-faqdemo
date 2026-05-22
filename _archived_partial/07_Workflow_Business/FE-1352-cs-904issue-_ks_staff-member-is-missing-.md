---
project: FE
issue_key: FE-1352
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
jira_url: https://ctil.atlassian.net/browse/FE-1352
created: '2024-02-27'
resolved: '2024-05-06'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1352: CS-904:Issue _KS_staff member is missing from FE DB RIN01293371 RIN01300770'
---
# FE-1352: CS-904:Issue _KS_staff member is missing from FE DB RIN01293371 RIN01300770

## 問題描述

KSG and KMY Memberson case:

Reproduce Step:

1. select Staff member in staff panel

- table tblvipmas , VipTemp both have such member

2. issue a sale memo with staff member

3. process day end

>> Member in tblvipmas , VipTemp is deleted after day end



## 相關資訊

- **Jira:** [FE-1352](https://ctil.atlassian.net/browse/FE-1352)
- **解決方式:** Done