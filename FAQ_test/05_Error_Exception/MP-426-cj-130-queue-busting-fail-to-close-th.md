---
project: MP
issue_key: MP-426
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-426"
created: 2021-05-03
resolved: 2021-05-17
resolution: Done
has_images: False
---

# MP-426: CJ #130 - Queue Busting – Fail to Close the order in Queue Busting after complete transaction

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.0
> **解決日期:** 2021-05-17
> **負責人:** Joy Li
> **組件:** MPOS

## 問題描述

- CJ Queue Busting – Fail to Close the order in Queue Busting after complete transaction

- Reproduce Steps:

- J805 use MPOS to create an order in queue questing with ref "Order_A" and "Order_B"

- POS retrieve order "Order_A" and issue sales memo. >> Order_A will disappear after payment >> Normal response

- MPOS retrieve order "Order_B" and issue sales memo. >> Order_B was keep after payment << Fix in this release
 *



## 相關資訊

- **Jira:** [MP-426](https://ctil.atlassian.net/browse/MP-426)
- **解決方式:** Done