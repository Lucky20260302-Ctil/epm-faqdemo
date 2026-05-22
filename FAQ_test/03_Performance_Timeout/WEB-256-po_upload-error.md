---
project: WEB
issue_key: WEB-256
issue_type: Bug QA
status: Closed
faq_score: 7.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, web, performance_timeout, web-(csplus)]
jira_url: "https://ctil.atlassian.net/browse/WEB-256"
created: 2022-11-30
resolved: 2023-11-16
resolution: Done
has_images: False
---

# WEB-256: PO_Upload Error

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 7.0
> **解決日期:** 2023-11-16
> **負責人:** Ken Lam
> **組件:** Web (CSPlus)

## 問題描述

Environment: Prorunner UAT

ACC: sx1                        PW: sx1

Location: Purchase Order > Purchase Order Maintenance 

Reproduce step

~~Case 1 (Solved because some columns is not allowed to input)~~

1. ~~Click Create~~

2. ~~Manage item~~

3. ~~Upload files and Unit Column disappear~~

 

Case 2 

1. Click Create

2. Manage item

3. Upload attached files **(testing 29)** and **Import view is correct (Attached-Import View Correct)**

4. Press 'Confirm'

5. **The unit cost change "0"(Attached-Unit Cost Error)****

6.  **Can Validate but not allow save even change (show Error - Attached Insert Error)**

 

Enhancement 

1. Plz remove column "*"

 

*Users don't know which column is mandatory.



## 相關資訊

- **Jira:** [WEB-256](https://ctil.atlassian.net/browse/WEB-256)
- **解決方式:** Done