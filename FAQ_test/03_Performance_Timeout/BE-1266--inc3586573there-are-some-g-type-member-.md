---
project: BE
title: "BE-1266:  [INC3586573]There are some G type member data in KS NZ & KS AU DB"
issue_key: BE-1266
issue_type: Bug PRD
status: Open
faq_score: 7.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, api]
jira_url: "https://ctil.atlassian.net/browse/BE-1266"
created: 2026-05-20
resolved: 
resolution: 
has_images: True
---

# BE-1266:  [INC3586573]There are some G type member data in KS NZ & KS AU DB

## 問題描述



1.We found some G type member in DB

> 📎 **image-20260520-094411.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ac39aa37-f736-4aad-bd41-e4c985b7a4b5)（需 Jira 登入）
2.POS API will insert one default data to DB first.

> 📎 **image-20260520-094642.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c1f086fc-87bb-40c9-aeb3-8620a980b0a2)（需 Jira 登入）
3.

KSFN6481S001021

Event ID:72a87d358a0345aba1562c183048f7a3 

Update the actual member data to DB,But connect DB occured  timeout error.

> 📎 **image-20260520-094526.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/1e40e445-fb08-4262-9d30-0257742a5084)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260520-094411.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ac39aa37-f736-4aad-bd41-e4c985b7a4b5)
2. 📎 **image-20260520-094642.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c1f086fc-87bb-40c9-aeb3-8620a980b0a2)
3. 📎 **image-20260520-094526.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/1e40e445-fb08-4262-9d30-0257742a5084)

## 相關資訊

- **Jira:** [BE-1266](https://ctil.atlassian.net/browse/BE-1266)