---
project: BE
issue_key: BE-107
issue_type: Task
status: Closed
tags:
- 05_error_exception
- backend-(web)
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-107
created: '2020-06-18'
resolved: '2024-04-27'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-107: CR0006 - General Point Calculation (WEB based)'
---
# BE-107: CR0006 - General Point Calculation (WEB based)

## 問題描述

1) special effective period must within header period when saving, same issue found in .net version already fixed (9/7/2020) fixed

2) No checking on From Date & To Date when saving (runtime error - Operator '>' is not defined for type 'Date' and type 'DBNULL' (28/9/2020) fixed

3) No checking on Disc. Item Ctrl when saving (9/7/2020) fixed

4) Always return 'Please enter From Amount' and 'Amt$ <= will be cleared (28/9/2020) fixed

5) Validation sequence - Reference No, Remarks, Disc. Item Ctrl, From Date, To Date Bonus Points Control (09/10/2020) fixed

 



## 相關資訊

- **Jira:** [BE-107](https://ctil.atlassian.net/browse/BE-107)
- **解決方式:** Done