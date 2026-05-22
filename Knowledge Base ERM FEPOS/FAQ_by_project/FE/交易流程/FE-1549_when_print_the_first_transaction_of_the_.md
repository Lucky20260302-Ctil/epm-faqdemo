---
tags: [faq, fe, 交易流程]
component: "Front End v720.02"
symptom: "RIN01414263,PRC - OCF3 - CS2000 - FE :when print the first transaction of the day, POS will take a l"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1549
resolved: 2025-02-24
fix-version: ""
---

# FE-1549: when print the first transaction of the day, POS will take a long time

## 問題

RIN01414263,PRC - OCF3 - CS2000 - FE :when print the first transaction of the day, POS will take a long time

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-02-24
### Jira Comments (10 則)
**pierre.shi** (2024-11-06):
每天POS打印的第一单都很慢，无论是出票还是重印都会loading很久
用于做销售的Till2, till5, till6, till7都有这个问题.
以上till均使用TMU printer。
**Sang** (2024-11-07):
Please advise tblconfig.DotNetPrint Value ?
**Sang** (2024-11-07):
v72 use VB6 print library (tblconfig.dotnetprint='N'), 1st time use print function will take longer time due to construct and initialize VB6 COM object . When upgrade to v75 (tblconfig.dotnetprint='Y') which use dotnet print library has not this issue.
**pierre.shi** (2024-11-12):
Hi@@Sang Coach want to know below inform to analy this issue .
Why OCF3Till0till1 or other stores Not have this issue? This issue occurred only on OCF3 till2,till5,till6,till7.
1CN dotnetprint config setting 应该是 'N' 还是 'Y'.
2下面两条T9 log分别是在什么情况下才会写进 T9 log?
[05/11/2024 10:45:16 -4954]: Before Print - After Prepare MDB : Avail V. Memory : 974.426
[05/11/2024 10:45:23 -8835]: After Print : Avail V. Memory : 956.985
**Sang** (2024-11-14):
@@pierre.shi  please get till 1  & till 3 dbtrans and 3 days logs for analysis.
**pierre.shi** (2024-11-14):
Hi@@Sang as till3 is PCE, I copied the dbtrans and logs on till1 and till2 for your reference.
They have been uploaded onto onedrive.
**Sang** (2024-11-14):
@@pierre.shi 20241114_FE-1549.zip contains till# 1 11/Nov - 13/Nov logs file, but haven’t any print out action within these 3 days.
**pierre.shi** (2024-11-15):
@@Sang I had uploaded the logs and dbtbk on till0 and till2 from 9th Nov to 11th Nov. They had sales memos printed on the three days.
**Andrew_Au** (2025-02-24):
@@pierre.shi Can I close the ticket ?
**pierre.shi** (2025-02-24):
Hi @@Andrew_Au please help to close. thanks

## 相關資訊

- Jira: [FE-1549](https://ctil.atlassian.net/browse/FE-1549)
- Fix Version: 未記錄
- 解決日期: 2025-02-24
