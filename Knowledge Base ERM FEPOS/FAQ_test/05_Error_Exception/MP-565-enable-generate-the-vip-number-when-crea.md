---
project: MP
issue_key: MP-565
issue_type: Bug QA
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-565"
created: 2022-10-03
resolved: 2022-10-19
resolution: Done
has_images: False
---

# MP-565: enable generate the vip number when create the vip

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.5
> **解決日期:** 2022-10-19
> **負責人:** Sang
> **組件:** MPOS

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