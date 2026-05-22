---
project: FE
issue_key: FE-1600
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, interface]
jira_url: "https://ctil.atlassian.net/browse/FE-1600"
created: 2024-12-31
resolved: 2025-02-12
resolution: Done
has_images: True
---

# FE-1600: [CS-1309] Issue-MY-INC2772129- CAR Error - MY-A130-Unknown Sales item type code 9999 12/20

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.0
> **解決日期:** 2025-02-12
> **負責人:** Andrew_Au
> **組件:** interface

## 問題描述

Below transaction having unknown sales item type code 9999 error in CAR.

Raise this ticket to request for a Program enhance.

> 📎 **image001 (1).png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e10e5929-bfa3-4ff3-8f65-f0ab2b4047c5)（需 Jira 登入）
**Transaction Nuber:**

MY-OC602-40060402 of 12/20

**Root Cause:**

Normally,CAR interface file separate by ' | '.The issue caused by user input remarks which contain ' | '.

> 📎 **pastedImage.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8d262e5b-211d-4a6e-bb23-473b465beab3)（需 Jira 登入）
Details in Bellow Email:

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/5441b2d7-0d56-4bb4-81ab-6859a8ccb70a)（需 Jira 登入）



## 附件截圖

1. 📎 **image001 (1).png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e10e5929-bfa3-4ff3-8f65-f0ab2b4047c5)
2. 📎 **pastedImage.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8d262e5b-211d-4a6e-bb23-473b465beab3)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/5441b2d7-0d56-4bb4-81ab-6859a8ccb70a)

## 相關資訊

- **Jira:** [FE-1600](https://ctil.atlassian.net/browse/FE-1600)
- **解決方式:** Done