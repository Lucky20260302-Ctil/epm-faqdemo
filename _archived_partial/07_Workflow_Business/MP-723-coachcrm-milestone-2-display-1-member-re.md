---
project: MP
issue_key: MP-723
issue_type: Bug QA
status: Closed
tags:
- 07_workflow_business
- faq
- mp
- mpos
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-723
created: '2024-11-11'
resolved: '2024-11-14'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'MP-723: [Coach][CRM milestone 2] Display 1 member result only but Backend Db has more than 1 same tel records'
---
# MP-723: [Coach][CRM milestone 2] Display 1 member result only but Backend Db has more than 1 same tel records

## 問題描述

[Coach][CRM milestone 2] Display 1 member result only but Backend Db has more than 1 same tel records

Reproduce steps:

1. Disconnect CRM

2. Scan QR code that Backend db has no this member, then search by tel

Existing result:

Display 1 member result only but Backend Db has more than 1 same tel records

Expected result:

Display multiple results



## 相關資訊

- **Jira:** [MP-723](https://ctil.atlassian.net/browse/MP-723)
- **解決方式:** Done