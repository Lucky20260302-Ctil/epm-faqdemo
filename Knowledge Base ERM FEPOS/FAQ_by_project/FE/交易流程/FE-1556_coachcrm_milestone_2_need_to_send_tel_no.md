---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "[Coach][CRM milestone 2] Send tel no.  to beapi when use QR code find member"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1556
resolved: 2024-11-22
fix-version: ""
---

# FE-1556: [Coach][CRM milestone 2] Need to send tel no.  to beapi when use QR code find member

## 問題

[Coach][CRM milestone 2] Send tel no.  to beapi when use QR code find member
Existing result:
Sent member no. to beapi when use QR code find member, then beapi won’t run qr code member searching flow
QR code string:
YVhaQWRYTmxaRFIwWVhCemRISjVQUT09bFRXRy9XMVg1cFYzaUROQlgveFU4bFpYZ1RqVVhURWs2aWNjSkdNKy8vc3ZGNnBQajFTYmI0WTNWWmlEQkd3L3hpV0lIWU42NUdVbngrY25ibTdQQ3R5aURKejAwWXVrakkvaU04bnNmdkhUeWZQY25uTmhVWUVYdWZGOEFoT3ZGK3Jma21xMnAvOG1oZGk5MzVyV2RtUE52a0x3WWxGcTgvV2lpMjg5R0dVVjcwYUJ2WjI5SUM5dnNZM3J2c1Rlb1pEY0hIREhMK3NwVmhMSXNMaU9lR0hhbzlsU3R5U0N0TUIyRngrRGVUWT0=
Content:
{"CustomerID":"OC11018230203002","Name":"周测试","Mobile":"18230203002","DOB(Year)":"1992","DOB(Mon)":"10","DOB(Day)":"06","Gender":"M","DynamicToken":"QsjzFsBO9JOHryDf"}

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-11-22
### Jira Comments (2 則)
**Sang** (2024-11-14):
v750.04R09A
**Sherman tse** (2024-11-18):
Verified on QA
POS send tel no. to beapi when users use QR　code to find member

## 相關資訊

- Jira: [FE-1556](https://ctil.atlassian.net/browse/FE-1556)
- Fix Version: 未記錄
- 解決日期: 2024-11-22
