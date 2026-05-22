---
project: MP
issue_key: MP-619
issue_type: Bug QA
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-619"
created: 2022-12-20
resolved: 2023-06-27
resolution: Done
has_images: False
---

# MP-619: Back to sales main page after Tab "Confirm" in time out error

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.5
> **解決日期:** 2023-06-27
> **負責人:** Cy Lau
> **組件:** MPOS

## 問題描述

Location: Stock Check page

Users may meet time out issue when searching item's stock, it would pop up an error: 

Exception: Fail to get Stock Data

 

Existing situation: 

Back to sales main page automatically after Tab "Confirm" in time out error (ref: image-2022-12-20-11-28-43-008.png)

 

Expected situation:

Suggest to stay in Stock Check page after  tab "Confirm" in time out error



## 相關資訊

- **Jira:** [MP-619](https://ctil.atlassian.net/browse/MP-619)
- **解決方式:** Done