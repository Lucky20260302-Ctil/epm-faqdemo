---
tags: [faq, fe, 交易流程]
component: "Day End"
symptom: "tested on 172.16.138.99"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1387
resolved: 2024-05-24
fix-version: ""
---

# FE-1387: [CS-1033] day end error by incorrect cash flow record

## 問題

tested on 172.16.138.99

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-05-24
### Jira Comments (5 則)
**Joy Li** (2024-05-10):
@@Sang Could we have a clear error message for this case in V75?
Also why there are different behavior for v72 and v75 day end? even the record is exisy in J317 long time ago.
**Joy Li** (2024-05-13):
Suggestion:
Program update to filter and use valid payment type's cash flow only
@@Andy Ko
<span style="color:#4c9aff">***Test case:***</span>
1. 
2. 
3.
**Andy Ko** (2024-05-14):
case 1 and case 2
**Joy Li** (2024-05-16):
@@Andy KoPlease provide me the testing case and result for below case in single excel.
**Joy Li** (2024-05-23):
test report checked

## 相關資訊

- Jira: [FE-1387](https://ctil.atlassian.net/browse/FE-1387)
- Fix Version: 未記錄
- 解決日期: 2024-05-24
