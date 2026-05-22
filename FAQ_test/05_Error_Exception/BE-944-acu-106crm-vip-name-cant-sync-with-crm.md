---
project: BE
issue_key: BE-944
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, api]
jira_url: "https://ctil.atlassian.net/browse/BE-944"
created: 2024-11-14
resolved: 2025-02-24
resolution: Done
has_images: True
---

# BE-944: [ACU-106]CRM - vip name can't sync with CRM API response

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.5
> **解決日期:** 2025-02-24
> **負責人:** Joy Li
> **組件:** API

## 問題描述

1.CRM API responsed the vip_name1 and vip_last_name all are 'Yoyo'.

> 📎 **image-20241114-070110.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/434dc146-4ff9-4792-9534-190699cbaad6)（需 Jira 登入）
2.But in DB vip table, vip_name1 is ‘BEAPI’ and vip_last_name is NULL.Please double check and confirm the logic and fixed it in hot fix.

> 📎 **image-20241114-070959.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/db52a30d-f33a-421e-8dab-6559794af70c)（需 Jira 登入）

> 📎 **image-20241114-070605.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/2413402b-62d1-4e28-be6e-754be63f73ba)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20241114-070110.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/434dc146-4ff9-4792-9534-190699cbaad6)
2. 📎 **image-20241114-070959.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/db52a30d-f33a-421e-8dab-6559794af70c)
3. 📎 **image-20241114-070605.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2413402b-62d1-4e28-be6e-754be63f73ba)

## 相關資訊

- **Jira:** [BE-944](https://ctil.atlassian.net/browse/BE-944)
- **解決方式:** Done