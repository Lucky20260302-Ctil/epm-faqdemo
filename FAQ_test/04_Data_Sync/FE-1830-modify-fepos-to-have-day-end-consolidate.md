---
project: FE
issue_key: FE-1830
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1830
created: '2025-12-11'
resolved: '2026-02-26'
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1830: Modify FEPOS to have Day-end consolidated report if 3rd party (Omni) is enabled'
---
# FE-1830: Modify FEPOS to have Day-end consolidated report if 3rd party (Omni) is enabled

## 問題描述

Modify FEPOS to have Day-end consolidated report if 3rd party (Omni) is enabled

- current design, if maintill is single till, no consolidated report will be generated.

- to be: 

- if maintill is single till but 3rd party (Omni) has dayend data, consolidated report will be generated.

- re-do consolidated report also.




## Jira Comments

> **Automation for Jira** (2025-12-11):
> Issue has been created since Days since: 0 Week since : 0 Issue due date difference Days since :  Weeks since: 

> **Sang** (2025-12-11):
> revised program uploaded to \\ds411\share\POS_FE_Release_64\2025121 Coach v750.04R18 – Omni

## 相關資訊

- **Jira:** [FE-1830](https://ctil.atlassian.net/browse/FE-1830)
- **解決方式:** Done
- **標籤:** OmniHub