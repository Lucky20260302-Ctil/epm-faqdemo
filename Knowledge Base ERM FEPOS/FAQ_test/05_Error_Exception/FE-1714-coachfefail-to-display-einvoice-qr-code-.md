---
project: FE
issue_key: FE-1714
issue_type: Bug QA
status: Closed
faq_score: 9.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1714"
created: 2025-06-19
resolved: 
resolution: 
has_images: True
---

# FE-1714: [Coach][FE]Fail to display einvoice qr code on the receipt

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 9.0
> **負責人:** Sherman tse
> **組件:** Front End

## 問題描述

[Coach][FE]Fail to display einvoice qr code 

Config:

EINV_QRCODE_ENABLE_DEFAULTY='Y'

EINV_QRCODE_ENABLE='Y'

Testing VM:

172.16.138.131

Reproduce steps:

1. Issue an order

2. Add an item

3. Select payment method

4. Process to complete transaction

5. Skip pop up of einvoice

6. Print out receipt directly

7. Check the print out

> 📎 **image-20250619-085646.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d6ff0253-c550-441b-ab59-6e03bf51f120)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250619-085646.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d6ff0253-c550-441b-ab59-6e03bf51f120)

## 相關資訊

- **Jira:** [FE-1714](https://ctil.atlassian.net/browse/FE-1714)