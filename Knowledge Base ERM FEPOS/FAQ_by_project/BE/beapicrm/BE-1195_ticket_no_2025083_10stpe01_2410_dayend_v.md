---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "IMX"
root-cause: "待提取"
solution: "### Jira Comments (7 則)"
jira: BE-1195
resolved: 
fix-version: ""
---

# BE-1195: Ticket No. 2025083 10STPE01 24/10 dayend validation , error in sales and payment 

## 問題

IMX
Operation :03
Location code : 10STPE01-0
POS version : v71
Please help to check and repost the transaction  10STPE03-00003633 on 24/10.
Alec has tried to repost it but it is failed . Member M10T0002629 is existed in CSP backend after check .

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (7 則)
**Angela Chan** (2025-11-03):
the posting is done after removing **# **on the line (pls refer to image file: remove # in pc file), pls help to check why it can’t be post before as the formatting looks OK, thank you!
**Jerry Wong** (2025-11-03):
can I have the log for checking?
**Angela Chan** (2025-11-03):
T9 log is uploaded, DAL needed? I need to ask user  if needed, thank you
**Jerry Wong** (2025-11-03):
I would like to have the backend posting log, file name should be fomatted as 'log-ic8006-xxxxxxxxxxxxxx.03', xxx is date time, 03 is company. Thanks!
**Angela Chan** (2025-11-03):
2 files uploaded, thanks
**Angela Chan** (2025-11-05):
user replied nothing updated on the member details, attached as the screen capture
**Angela Chan** (2025-11-11):
@@Jerry Wong 
do you have any finding based on nothing done by user side?

## 相關資訊

- Jira: [BE-1195](https://ctil.atlassian.net/browse/BE-1195)
- Fix Version: 未記錄
- 解決日期: 未記錄
