---
project: BE
title: "BE-776: CS-595:Chinese Character in store address"
issue_key: BE-776
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, be, workflow_business, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-776"
created: 2023-06-29
resolved: 2024-09-04
resolution: Done
has_images: True
---

# BE-776: CS-595:Chinese Character in store address

## 問題描述

Brand: Coach

Region: PRC/TW/JP

**Issue Detail:**

We have 40 characters limit on BE store address.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b2317db6-f4ee-4916-bd2b-ba9fbea5df8b)（需 Jira 登入）
   

All Chinese, Korea and Japan character will count 1 in BE, BUT it will count as 2 characters when we printer receipt.

if we have Chinese character in address, it may over 40 when we print receipt. like below

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/da161302-441b-4ff0-855b-2a7a4c7f0649)（需 Jira 登入）
it is allowed in BE, but it is not allowed in FE, it will has printing issue and no store information and no payment line.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/70d3c166-a3cb-4bd2-b1ac-bb41f45c3f62)（需 Jira 登入）
 



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b2317db6-f4ee-4916-bd2b-ba9fbea5df8b)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/da161302-441b-4ff0-855b-2a7a4c7f0649)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/70d3c166-a3cb-4bd2-b1ac-bb41f45c3f62)

## 相關資訊

- **Jira:** [BE-776](https://ctil.atlassian.net/browse/BE-776)
- **解決方式:** Done