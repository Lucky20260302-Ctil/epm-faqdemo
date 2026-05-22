---
project: BE
issue_key: BE-982
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-982"
created: 2025-01-13
resolved: 
resolution: 
has_images: True
---

# BE-982: [RIN01437844] - Incorrect agegrp value for some MY OCE member data

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 7.0
> **負責人:** Cy Lau
> **組件:** Data Interface

## 問題描述

1.SOG call out MY区域有32 个OCE member的Age group不对，正确应该是"01"，"02"，而DB这些OCE48的member，为"1"， "'2"。

> 📎 **image-20250113-144742.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7727a362-4fbc-4b40-9d53-e2a9ddd944c0)（需 Jira 登入）
2.sample OCE480C00202371
查询change log ，此会员在 2023-12-28 08:46:12 由原来的 '02' 变成 'NULL',但是没有找到从什么时候又从 'NUll' 变成了现在的 '2'.Could you help to check the root cause?

> 📎 **image-20250113-144946.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ae7b62bd-1d98-4f23-b138-5849a1544b2d)（需 Jira 登入）



## 附件截圖

1. 📎 **image-20250113-144742.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7727a362-4fbc-4b40-9d53-e2a9ddd944c0)
2. 📎 **image-20250113-144946.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ae7b62bd-1d98-4f23-b138-5849a1544b2d)

## 相關資訊

- **Jira:** [BE-982](https://ctil.atlassian.net/browse/BE-982)