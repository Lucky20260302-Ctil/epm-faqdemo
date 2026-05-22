---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Env: LANDS UAT"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-783
resolved: 2023-08-14
fix-version: ""
---

# BE-783: [Lands] Wordings change & add a column for display Credit / Debit

## 問題

Env: LANDS UAT
Involved section: Blokc Vote Account (BV0001)
1) Wordings change
Please change wordings in the button "Deposit" & "Withdraw" as "Credit" & "Debit"
2) Add a column for display Credit / Debit
Sample:

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-08-14
### Jira Comments (3 則)
**Jerry Wong** (2023-07-27):
update [dbo].[multivar] set multivar_msg = 'Credit' where multivar_progid = 'BV0001' and multivar_msg = 'Deposit'
update [dbo].[multivar] set multivar_msg = 'Debit' where multivar_progid = 'BV0001' and multivar_msg = 'Withdraw'
Update [dbo].[multimsg] set multimsg_label = 'Block Vote Account	Block Vote Account 	Block Vote Account Code	Balance	Credit	Debit	Amount	Active	Inactive'
where multimsg_progid = 'BV0001'
**Hans Wong** (2023-07-28):
@@Jerry Wong
remember use CHAR(9) instead of tab
update [dbo].[multivar] set multivar_msg = 'Credit' where multivar_progid = 'BV0001' and multivar_msg = 'Deposit'
update [dbo].[multivar] set multivar_msg = 'Debit' where multivar_progid = 'BV0001' and multivar_msg = 'Withdraw'
Update [dbo].[multimsg] set multimsg_label = 'Block Vote Account'<u>CHAR(9)</u>'Block Vote Account '<u>CHAR(9)</u>'Block Vote Account Code'<u>CHAR(9)</u>'Balance'<u>CHAR(9)</u>'Credit'<u>CHAR(9)</u>'Debit'<u>CHAR(9)</u>'Amount'<u>CHAR(9)</u>'Active'<u>CHAR(9)</u>'Inactive'
where multimsg_progid = 'BV0001'
**Sherman tse** (2023-08-14):
Verified on Lands UAT env, Close case

## 相關資訊

- Jira: [BE-783](https://ctil.atlassian.net/browse/BE-783)
- Fix Version: 未記錄
- 解決日期: 2023-08-14
