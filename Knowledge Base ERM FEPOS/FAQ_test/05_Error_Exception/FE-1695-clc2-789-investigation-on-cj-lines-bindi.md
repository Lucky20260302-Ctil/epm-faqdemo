---
project: FE
issue_key: FE-1695
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, api]
jira_url: "https://ctil.atlassian.net/browse/FE-1695"
created: 2025-05-15
resolved: 
resolution: 
has_images: True
---

# FE-1695: [CLC2-789] Investigation on CJ LINE's Binding Issue of the POS API Create Member Failure

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **負責人:** Cy Lau
> **組件:** API

## 問題描述

Coach team callout there are so many  400,500,503 on 2025-04-06

While binding with an SA on Production, our attempts failed by receiving the **POS API Create Member Failure (503 Error)** at the following times. Some screenshots are provided below.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4038ed8f-538f-48dc-a1fd-20028f6cd1b0)（需 Jira 登入）

| [2025-04-06 12:08:48] | Ud4016be355546f39c1935c8cde9d5576 | 400 | 
| [2025-04-06 14:28:27] | U4b202c05acaad18d506c8387cf82eb25 | 400 | 
| [2025-04-06 14:29:57] | U03da6f6179b4eb06ba9cd4185caa31c2 | 500 | 
| [2025-04-06 14:31:07] | Ue630c3f2ba4a7049a7a8fe26dc619b8a | 503 | 
| [2025-04-06 14:31:07] | Uf23eca3848d0d8a06d3baffe32e0c377 | 500 | 
| [2025-04-06 14:31:11] | U2ae7a5bb40108eb2ddcf368c6f40dfe3 | 503 | 
| [2025-04-06 14:31:25] | Ub9d7eef888bf0fc3b53588291ec042e7 | 400 | 
| [2025-04-06 14:31:36] | U334a843045c4364e869a4f1ae561eeac | 503 | 
| [2025-04-06 14:31:49] | Uab0cb516ca36c42a35fb183054e35a1a | 503 | 
| [2025-04-06 14:32:23] | U8a0fdac85f3f5f772d0ca033710b57da | 503 | 
| [2025-04-06 14:33:06] | U79a91b944b433961ba6d5c1dfc3d2ac7 | 503 | 
| [2025-04-06 14:33:34] | U9ee1a1140f20e073c0a73ee40d384887 | 500 | 
| [2025-04-06 14:34:12] | U4d3b9f01e52ae1b0347e5db330f9a8c8 | 503 | 
| [2025-04-06 14:35:11] | U97f956e366874a3aba613407d60380d7 | 503 | 
| [2025-04-06 14:35:14] | U5f7dddcdb5f0301b9b4e01363d64ea32 | 503 | 
| [2025-04-06 14:35:19] | Ucba32e98326d24334f4d69435e2fce59 | 503 | 

> 📎 **image-20250515-061416.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/923bc672-fe18-49b7-a66a-ebb8d3e4a284)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4038ed8f-538f-48dc-a1fd-20028f6cd1b0)
2. 📎 **image-20250515-061416.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/923bc672-fe18-49b7-a66a-ebb8d3e4a284)

## 相關資訊

- **Jira:** [FE-1695](https://ctil.atlassian.net/browse/FE-1695)