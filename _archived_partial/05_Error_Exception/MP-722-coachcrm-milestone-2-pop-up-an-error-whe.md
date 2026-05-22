---
project: MP
issue_key: MP-722
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-722
created: '2024-11-11'
resolved: '2024-11-14'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-722: [Coach][CRM milestone 2] Pop up an error when MPOS scan a QR code that has no Member ID in backend DB'
---
# MP-722: [Coach][CRM milestone 2] Pop up an error when MPOS scan a QR code that has no Member ID in backend DB

## 問題描述

Reproduce steps:

1. Fail to connect CRM

2. Scan QR code (no member no.)

Existing result:

Pop up an error “Object reference not set to an instance of an object“

Expected result:

Direct to member creation screen

> 📎 **image-20241111-023740.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bd0d29ac-5c0c-406e-97fc-712c7842fed7)（需 Jira 登入）
YVhaQWRYTmxaRFIwWVhCemRISjVQUT09bFRXRy9XMVg1cFYzaUROQlgveFU4bFpYZ1RqVVhURWs2aWNjSkdNKy8vc3ZGNnBQajFTYmI0WTNWWmlEQkd3L3hpV0lIWU42NUdVbngrY25ibTdQQ3R5aURKejAwWXVrakkvaU04bnNmdkhUeWZQY25uTmhVWUVYdWZGOEFoT3ZGK3Jma21xMnAvOG1oZGk5MzVyV2RtUE52a0x3WWxGcTgvV2lpMjg5R0dVVjcwYUJ2WjI5SUM5dnNZM3J2c1Rlb1pEY0hIREhMK3NwVmhMSXNMaU9lR0hhbzlsU3R5U0N0TUIyRngrRGVUWT0=

> 📎 **image-20241111-025032.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ce7a1abb-be18-42b1-b768-93b08da6fbf3)（需 Jira 登入）
YVhaQWRYTmxaRFIwWVhCemRISjVQUT09bFRXRy9XMVg1cFYzaUROQlgveFU4bFpYZ1RqVVhURWs2aWNjSkdNKy8vc3ZGNnBQajFTYmI0WTNWWmlEQkd3L3hpV0lIWU42NUdVbngrY25ibTdQQ3R5aURKejAwWXVrakkvaU04bnNmdkhUeWZQY25uTmhVWUVYdWZGOEFoT3ZGK3Jma21xMnAvOG1oZGk5MzVyV2RtUE52a0x3WWxGcTgvV2lpMjg5R0dVVjcwYUJ2WjI5SUM5dnNZM3J2c1RlRkpCdHlJQndYSmFFY1FxYkpuL2JvbEtaVmpUOXRCOTl2amZFaDJYK0kwQT0=

> 📎 **image-20241111-023805.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/dd1958a2-e50d-4cf6-a8b8-de6dd68ce473)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20241111-023740.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/bd0d29ac-5c0c-406e-97fc-712c7842fed7)
2. 📎 **image-20241111-025032.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ce7a1abb-be18-42b1-b768-93b08da6fbf3)
3. 📎 **image-20241111-023805.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/dd1958a2-e50d-4cf6-a8b8-de6dd68ce473)

## 相關資訊

- **Jira:** [MP-722](https://ctil.atlassian.net/browse/MP-722)
- **解決方式:** Done