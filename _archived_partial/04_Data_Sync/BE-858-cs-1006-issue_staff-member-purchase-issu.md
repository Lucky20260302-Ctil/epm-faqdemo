---
project: BE
issue_key: BE-858
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- backend-(chainstoreplus-7.0)
- be
- data_sync
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-858
created: '2024-05-24'
resolved: '2024-06-17'
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-858: [CS-1006] Issue_Staff member purchase issue in HKMO'
---
# BE-858: [CS-1006] Issue_Staff member purchase issue in HKMO

## 問題描述

Tapestry team request to exclude vip_type=E or T from the sync job for VIP data.

Program exe: \Obj\csplus_syncmember.exe

Request:

1. Add config in csplus_syncmember.exe.config

2. member sync with exclude the member type which marked in config.

3. Check if Member sync select SQL with (nolock) 




## Jira Comments

> **Joy Li** (2024-05-27):
>   Please provide ETA:

## 相關資訊

- **Jira:** [BE-858](https://ctil.atlassian.net/browse/BE-858)
- **解決方式:** Done