---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "Currently in CAR interface for transaction posting, POS will send data file to CAR and the posting d"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1055
resolved: 2025-06-11
fix-version: ""
---

# BE-1055: SOW of changing CAR Interface posting date time

## 問題

Currently in CAR interface for transaction posting, POS will send data file to CAR and the posting datetime is using backend server datetime in Hong Kong time zone.
It causes a symptom that data datetime is not reflecting the corresponding region datetime especially for Japan and Korea since there is 1 hour time difference between Hong Kong time zones.
To resolve this issue, this solution is introduced that putting the transaction date and time into posting date and time fields inside the interface file for sending to CAR. The change will apply to Coach Japan, Coach Korea and Kate Spade Japan.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-06-11
### Jira Comments (1 則)
**Sherman tse** (2025-05-12):
Verified on QA
test case attached

## 相關資訊

- Jira: [BE-1055](https://ctil.atlassian.net/browse/BE-1055)
- Fix Version: 未記錄
- 解決日期: 2025-06-11
