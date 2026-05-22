---
project: FE
title: "FE-1158: MPOS cannot complete the sales transactions when set the prtcompany='PROJECT"
issue_key: FE-1158
issue_type: Bug QA
status: Closed
faq_score: 8.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1158"
created: 2022-10-08
resolved: 2023-11-16
resolution: Done
has_images: False
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