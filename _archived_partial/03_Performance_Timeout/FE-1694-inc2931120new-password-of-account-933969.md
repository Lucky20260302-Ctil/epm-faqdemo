---
project: FE
issue_key: FE-1694
issue_type: Bug DEV
status: Closed
tags:
- 03_performance_timeout
- faq
- fe
- front-end-v750.01r01a
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1694
created: '2025-05-15'
resolved: '2025-09-10'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1694: [INC2931120]new password of account 933969changed in FE can''t be sync to SRC/HHT/namecapture'
---
# FE-1694: [INC2931120]new password of account 933969changed in FE can't be sync to SRC/HHT/namecapture   

## 問題描述

[INC2931120]AWS JP J317 POS v75,

new password of account 933969 changed in FE can't be sync to SRC/HHT/namecapture. 

If the password changed in BE , it can be sync to SRC/HHT/namecapture and FE normally. only this account has the issue.

User changed the password to Aa123456 in FE , but the password in ename is still Www0213. Sync password failed.



## 相關資訊

- **Jira:** [FE-1694](https://ctil.atlassian.net/browse/FE-1694)
- **解決方式:** Done