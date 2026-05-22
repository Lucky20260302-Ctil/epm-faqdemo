---
project: FE
issue_key: FE-1683
issue_type: Bug DEV
status: Closed
faq_score: 5.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end-v750.01r01a]
jira_url: "https://ctil.atlassian.net/browse/FE-1683"
created: 2025-04-29
resolved: 
resolution: 
has_images: True
---

# FE-1683: [CS-1430][INC2933217]PRC region POSV75 扫描顾CDP礼券的核销码,显示"parse coupon QR code error"

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 5.5
> **負責人:** Sang
> **組件:** Front End v750.01R01A

## 問題描述

PRC region POSV75 

升级之前，POSV72在支付页面点击会员电子优惠券之后可以扫描顾客手机上CDP礼券的核销码选中优惠券，但现在升级到V75以后，扫描核销码会显示"parse coupon QR code error"，无法通过扫描选中，只能手动选择优惠券。

检查日志，扫描核销码以后，生成的是一大串字符，并不是对应的coupon核销码，并且有error：parse coupon QR code error。

对应当天的日志已经上传。

> 📎 **2.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3a1c7160-51e9-4170-b391-abc539c8174f)（需 Jira 登入）

> 📎 **4.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3b89b101-78a3-400b-a520-57787776b9e0)（需 Jira 登入）

> 📎 **1.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f4f58ee2-931d-4b35-ad95-f70e464568cf)（需 Jira 登入）

> 📎 **3.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ff12eccf-e90b-4334-91df-95af0558cb39)（需 Jira 登入）


## 附件截圖

1. 📎 **2.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3a1c7160-51e9-4170-b391-abc539c8174f)
2. 📎 **4.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3b89b101-78a3-400b-a520-57787776b9e0)
3. 📎 **1.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f4f58ee2-931d-4b35-ad95-f70e464568cf)
4. 📎 **3.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ff12eccf-e90b-4334-91df-95af0558cb39)

## 相關資訊

- **Jira:** [FE-1683](https://ctil.atlassian.net/browse/FE-1683)