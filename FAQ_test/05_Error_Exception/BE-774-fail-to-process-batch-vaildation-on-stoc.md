---
project: BE
issue_key: BE-774
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-774"
created: 2023-06-21
resolved: 2023-06-23
resolution: Done
has_images: True
---

# BE-774: Fail to process batch vaildation on Stock Receive (TF6000)

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2023-06-23
> **負責人:** Sherman tse
> **組件:** Backend (Web)

## 問題描述

Reproduce steps:

1. Go to Stock Receive (TF6000)

2. Create a new batch

3. Put item into the batch

4. Make a batch vaildation

Existing reuslt:

Pop up error (screenshot as below) & Fail to make a batch vaildation

Testing Env: [https://172.16.138.55/ChainStorePlus_LandsD_QA](https://172.16.138.55/ChainStorePlus_LandsD_QA)

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c3c19a0b-37bc-4af2-a50a-3c7d329813e4)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c3c19a0b-37bc-4af2-a50a-3c7d329813e4)

## 相關資訊

- **Jira:** [BE-774](https://ctil.atlassian.net/browse/BE-774)
- **解決方式:** Done