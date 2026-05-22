---
project: MP
issue_key: MP-565
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-565
created: '2022-10-03'
resolved: '2022-10-19'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-565: enable generate the vip number when create the vip'
---
# MP-565: enable generate the vip number when create the vip

## 問題描述

unable assign the new vip no.

- NVIPAUTOGEN =Y

- NVIPAUTOGENFORMAT= default value = "LTCS" ( 'L'-Location, 'T'-Till, 'C'-Customer Add, 'S'-Sequence No. ,new vip number format)

- NVIPPERSEQ  (Running Sequence No. if using auto generate Member Code)

- NVIPSEQFIXEDLEN = default value "8"

- NVIPCODELEN_PERM default value "0,="



## 相關資訊

- **Jira:** [MP-565](https://ctil.atlassian.net/browse/MP-565)
- **解決方式:** Done