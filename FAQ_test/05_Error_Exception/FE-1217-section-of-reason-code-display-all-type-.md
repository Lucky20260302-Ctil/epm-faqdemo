---
project: FE
issue_key: FE-1217
issue_type: Bug QA
status: Closed
faq_score: 5.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1217"
created: 2023-02-22
resolved: 2023-02-23
resolution: Done
has_images: False
---

# FE-1217: Section of reason code display ALL type in Physical In/Out Information (IC6000)

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 5.5
> **解決日期:** 2023-02-23
> **負責人:** Jerry Wong
> **組件:** Front End

## 問題描述

Reproduce steps:

1. To Physical In/Out Batch Information (IC6000)

2. Click on one of the record & Select "Batch maintenance"

3. Click on one of the items in the batch & Select "Modify"

4. Click on "..." in the Reason field

Existing result:

Section of reason code display ALL type

Expected result:

Only display reason code with type null/P in Physical In/Out Information (IC6000)



## 相關資訊

- **Jira:** [FE-1217](https://ctil.atlassian.net/browse/FE-1217)
- **解決方式:** Done