---
project: BE
title: "BE-1066: [INC2961835] SG store OC554 Retrieve 04-17 sales records to Landlord have error"
issue_key: BE-1066
issue_type: Bug PRD
status: Closed
faq_score: 9.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1066"
created: 2025-05-09
resolved: 
resolution: 
has_images: True
---

# BE-1066: [INC2961835] SG store OC554 Retrieve 04-17 sales records to Landlord have error

## 問題描述

Tried to generate 04-17 sales file to landlord.
showing error: Object reference not set to an instance of an object.
Please help to check and advise
Thanks!

> 📎 **image-20250509-095836.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d65f20fc-435f-41fb-a795-543172cca22b)（需 Jira 登入）

1.

查看interface log发现retrieve 04-17的 sales records有error.

Log details:

Sales Data Export / MBSS v1.2 By Sanyo Exteneded -=2025-04-18 01:30:05

Parameter Used
-- config : sample.ini
-- business date : 2025-04-17
-- output path : D:\DCS_OC554\
-- loc code : OC554

Retrieve sales records on 04/17/2025

Escape on following error
Object reference not set to an instance of an object.

Done!

> 📎 **image-20250509-091409.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ba9defc0-ed60-460b-b9dd-b320cb8f4d55)（需 Jira 登入）
2.retrieve 04-16的 sales records正常，没有error

> 📎 **image-20250509-091601.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9de651ea-9fc7-4dfd-80bf-da0c640f611f)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250509-095836.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d65f20fc-435f-41fb-a795-543172cca22b)
2. 📎 **image-20250509-091409.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ba9defc0-ed60-460b-b9dd-b320cb8f4d55)
3. 📎 **image-20250509-091601.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9de651ea-9fc7-4dfd-80bf-da0c640f611f)

## 相關資訊

- **Jira:** [BE-1066](https://ctil.atlassian.net/browse/BE-1066)