---
project: FE
issue_key: FE-1158
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1158
created: '2022-10-08'
resolved: '2023-11-16'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1158: MPOS cannot complete the sales transactions when set the prtcompany=''PROJECT'
---
# FE-1158: MPOS cannot complete the sales transactions when set the prtcompany='PROJECT

## 問題描述

update the program \\ds411\share\POS_FE_Release_64\20220930 CSPlus v750.02  to testing Machine still cannot completed the sales transactions.

I follow the instruction set the below config 

- copied the CSPLUSeReceipt.rpt file to c:\retdata6

- set PRINTOUTFILESUBDIR = printlog

- EnableEReceipt='Y'



## 相關資訊

- **Jira:** [FE-1158](https://ctil.atlassian.net/browse/FE-1158)
- **解決方式:** Done