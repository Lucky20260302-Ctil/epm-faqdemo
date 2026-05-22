---
project: FE
title: "FE-1556: [Coach][CRM milestone 2] Need to send tel no.  to beapi when use QR code find member"
issue_key: FE-1556
issue_type: Bug QA
status: Closed
faq_score: 7.5
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, fe, workflow_business, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1556"
created: 2024-11-08
resolved: 2024-11-22
resolution: Done
has_images: True
---

# FE-1556: [Coach][CRM milestone 2] Need to send tel no.  to beapi when use QR code find member

## 問題描述

[Coach][CRM milestone 2] Send tel no.  to beapi when use QR code find member

Existing result:

Sent member no. to beapi when use QR code find member, then beapi won’t run qr code member searching flow

> 📎 **image-20241108-084328.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bee41597-2d6d-4b49-ae09-94653bd38eb4)（需 Jira 登入）
QR code string:

YVhaQWRYTmxaRFIwWVhCemRISjVQUT09bFRXRy9XMVg1cFYzaUROQlgveFU4bFpYZ1RqVVhURWs2aWNjSkdNKy8vc3ZGNnBQajFTYmI0WTNWWmlEQkd3L3hpV0lIWU42NUdVbngrY25ibTdQQ3R5aURKejAwWXVrakkvaU04bnNmdkhUeWZQY25uTmhVWUVYdWZGOEFoT3ZGK3Jma21xMnAvOG1oZGk5MzVyV2RtUE52a0x3WWxGcTgvV2lpMjg5R0dVVjcwYUJ2WjI5SUM5dnNZM3J2c1Rlb1pEY0hIREhMK3NwVmhMSXNMaU9lR0hhbzlsU3R5U0N0TUIyRngrRGVUWT0=

Content:

{"CustomerID":"OC11018230203002","Name":"周测试","Mobile":"18230203002","DOB(Year)":"1992","DOB(Mon)":"10","DOB(Day)":"06","Gender":"M","DynamicToken":"QsjzFsBO9JOHryDf"}



## 附件截圖

1. 📎 **image-20241108-084328.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/bee41597-2d6d-4b49-ae09-94653bd38eb4)

## 相關資訊

- **Jira:** [FE-1556](https://ctil.atlassian.net/browse/FE-1556)
- **解決方式:** Done