---
project: FE
issue_key: FE-1263
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end-v760.02]
jira_url: "https://ctil.atlassian.net/browse/FE-1263"
created: 2023-06-08
resolved: 2023-11-16
resolution: Done
has_images: True
---

# FE-1263: [Lands] Pop an error after select get HKMS Shop Cart

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2023-11-16
> **負責人:** Sang
> **組件:** front end v760.02

## 問題描述

Reproduce steps:

1. More >click on HKMS 2.0 Order

2. Click on Cancel to clear items from HKMS 2.0

3. Click on HKMS Shop Cart

Existing result:

Pop up an error: DialogResult cna be set only after window is created and shown as dialog

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bb5524f7-a5e6-4f08-9937-cdc9305e10f5)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/bb5524f7-a5e6-4f08-9937-cdc9305e10f5)

## 相關資訊

- **Jira:** [FE-1263](https://ctil.atlassian.net/browse/FE-1263)
- **解決方式:** Done