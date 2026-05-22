---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "1.)  POS never timeout and display negative time remain"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-903
resolved: 2021-02-22
fix-version: ""
---

# FE-903: Payment Module - A920 Integration issue - EPM payment time remain keep loading

## 問題

1.)  POS never timeout and display negative time remain
2.) Staff cannot cannel from POS even click and and pass security check.
After confirm, POS time remain screen display again.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2021-02-22
### Jira Comments (3 則)
**Sang** (2021-01-19):
-
**howard** (2021-01-20):
@@@Sang can reproduce by following steps:
1) POS online connected to send EPM-payment amount
2) A920 displayed amount equal to POS online sale
3) A920 wifi disconnected (e.g. walk out of wifi area)
4) After 60s, A920 display timeout
5) POS still keep remain countdown without end
**howard** (2021-02-22):
Retest in 7.5.0.01R01(Build210218) EPM counter screen can be closed while time remain is 0.

## 相關資訊

- Jira: [FE-903](https://ctil.atlassian.net/browse/FE-903)
- Fix Version: 未記錄
- 解決日期: 2021-02-22
