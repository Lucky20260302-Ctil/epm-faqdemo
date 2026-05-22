---
project: BE
issue_key: BE-870
issue_type: Bug QA
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-870"
created: 2024-07-09
resolved: 2024-07-10
resolution: Done
has_images: True
---

# BE-870: [Lands] Masconv function fail to overwrite encrypted masconv

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.5
> **解決日期:** 2024-07-10
> **負責人:** Jerry Wong
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

[Lands] Masconv function fail to overwrite encrypted masconv

Reproduce steps:

1. Execute Masconv to export encrypted Masconv file

2. Execute Masconv again to overwrite encrypted Masconv file

Existing result:

Got stuck in Item Master during Masconv

> 📎 **image-20240709-061102.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/635fe286-126e-4ed6-a50c-9700b67b100a)（需 Jira 登入）
I tried to close the Export POS master data & execute again, it will pop up an error:

> 📎 **image-20240709-061309.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/539c9449-1bd4-4e5b-9111-cdae9057d6c7)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240709-061102.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/635fe286-126e-4ed6-a50c-9700b67b100a)
2. 📎 **image-20240709-061309.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/539c9449-1bd4-4e5b-9111-cdae9057d6c7)

## 相關資訊

- **Jira:** [BE-870](https://ctil.atlassian.net/browse/BE-870)
- **解決方式:** Done