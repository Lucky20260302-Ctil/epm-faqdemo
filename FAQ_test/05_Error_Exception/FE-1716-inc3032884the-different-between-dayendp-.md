---
project: FE
issue_key: FE-1716
issue_type: Bug DEV
status: Closed
faq_score: 5.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end-v750.01r01a]
jira_url: "https://ctil.atlassian.net/browse/FE-1716"
created: 2025-06-23
resolved: 2025-09-08
resolution: Done
has_images: True
---

# FE-1716: [INC3032884]the different between dayendp and joupay caused the dayend issue

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 5.5
> **解決日期:** 2025-09-08
> **負責人:** Cy Lau
> **組件:** Front End v750.01R01A

## 問題描述

POS V75 PRC OCF539

We checked FE, the amount is the same as that in joupay.

But it has dayend issue on 14th Jun.

While running dayend check sql, it shew error payment and the difference between joupay and dayendp.

> 📎 **111.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/75e51576-2a21-45ae-9afa-8e987694d18b)（需 Jira 登入）
cheched in db between ‘joupay’ and ‘jouinv’, the total amount in jouinv is equal to that in joupay without D.

Checked in db between ‘joupay’ and ‘dayendp’, the total amount in joupay is equal to that in dayendp.

> 📎 **222.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/10e3120f-9b8f-45dd-96ac-932a55e40c8b)（需 Jira 登入）

> 📎 **333.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0d2e9f90-603c-4837-b8e3-d505b2ca14be)（需 Jira 登入）


## 附件截圖

1. 📎 **111.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/75e51576-2a21-45ae-9afa-8e987694d18b)
2. 📎 **222.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/10e3120f-9b8f-45dd-96ac-932a55e40c8b)
3. 📎 **333.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0d2e9f90-603c-4837-b8e3-d505b2ca14be)

## 相關資訊

- **Jira:** [FE-1716](https://ctil.atlassian.net/browse/FE-1716)
- **解決方式:** Done