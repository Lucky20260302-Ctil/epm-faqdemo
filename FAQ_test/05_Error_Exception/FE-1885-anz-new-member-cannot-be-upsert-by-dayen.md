---
project: FE
title: "FE-1885: [ANZ] New Member cannot be upsert by Dayend or transaction"
issue_key: FE-1885
issue_type: Bug QA
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, day-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1885"
created: 2026-02-11
resolved: 2026-05-05
resolution: Done
has_images: True
---

# FE-1885: [ANZ] New Member cannot be upsert by Dayend or transaction

## 問題描述

Here is the normal created flow:

The config：

> 📎 **image-20260211-082720.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/5a6e80a8-48c3-4acf-b1d8-d7ececadc536)（需 Jira 登入）

> 📎 **image-20260211-083419.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d2e91b59-df30-4361-903c-b6b334d90564)（需 Jira 登入）

MPOS has created the new Member

> 📎 **image-20260211-083116.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d5000d91-7027-46b9-8548-a87dcd13b5ea)（需 Jira 登入）
BE has no this record even once the “Day-end” is proceed.

> 📎 **image-20260211-083734.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9d1c7a87-847d-43ce-bde7-97cca896f6cc)（需 Jira 登入）
Here is the log

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a8878c03-a799-46d5-ae73-fbac5a4e665d)（需 Jira 登入）



## 附件截圖

1. 📎 **image-20260211-082720.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/5a6e80a8-48c3-4acf-b1d8-d7ececadc536)
2. 📎 **image-20260211-083419.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d2e91b59-df30-4361-903c-b6b334d90564)
3. 📎 **image-20260211-083116.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d5000d91-7027-46b9-8548-a87dcd13b5ea)
4. 📎 **image-20260211-083734.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9d1c7a87-847d-43ce-bde7-97cca896f6cc)
5. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a8878c03-a799-46d5-ae73-fbac5a4e665d)

## 相關資訊

- **Jira:** [FE-1885](https://ctil.atlassian.net/browse/FE-1885)
- **解決方式:** Done