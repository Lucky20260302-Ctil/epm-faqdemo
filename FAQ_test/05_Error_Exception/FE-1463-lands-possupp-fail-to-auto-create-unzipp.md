---
project: FE
issue_key: FE-1463
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1463"
created: 2024-07-18
resolved: 2024-09-03
resolution: Done
has_images: True
---

# FE-1463: [Lands] POSSUPP fail to auto create Unzipped_temp folder in retdata6

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2024-09-03
> **負責人:** Sang
> **組件:** Front End

## 問題描述

[Lands] POSSUPP fail to auto create Unzipped_temp folder in retdata6

Reproduce steps:

1. Open CSPLUS

2. Execute POSSUPP automatically

3. Wait until POS directed to login page

4. Check the retdata6 folder

Existing result:

- retdata6 folder has no Unzipped_temp folder after executed POSSUPP 

Modified date of the POSSUPP in CSPLUS is 11/07/2024 5:00 pm

> 📎 **image-20240718-080301.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/70232c62-036d-41d0-a364-4da9c90e7ca4)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240718-080301.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/70232c62-036d-41d0-a364-4da9c90e7ca4)

## 相關資訊

- **Jira:** [FE-1463](https://ctil.atlassian.net/browse/FE-1463)
- **解決方式:** Done