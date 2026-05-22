---
tags: [faq, fe, 交易流程]
component: "Front End, Payment"
symptom: "@@Sang SOG checked till5 on 02 Oct, still failed to click '完成' when purchase 3 pieces with one item."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1520
resolved: 2024-12-27
fix-version: ""
---

# FE-1520: RIN01399092 - PRC - OCF7  - CS2000 - FE : All Till cannot finish selling 

## 問題

@@Sang SOG checked till5 on 02 Oct, still failed to click "完成" when purchase 3 pieces with one item.
I can’t reproduce the issue in QA,But can re-produce the issue in Production.So could you help to check the root cause and give some advice?
@@Jason Wu Please help to send the logs to sang,I  send the log to you by zoom.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-12-27
### Jira Comments (8 則)
**Jason Wu** (2024-10-08):
@@Sang logs sent to you in Teams
**Tovi Wang** (2024-10-08):
POS payment screenshot
**Tovi Wang** (2024-10-08):
Dear All,
Another store callout the same issue.
RIN01402692,CN-OCF3
**Sang** (2024-10-09):
**Sang** (2024-10-09):
1.
**Tovi Wang** (2024-10-16):
Dear @@Sang @@Jason Wu ,
Many thanks for your confirmation.I has updated the details to Coach Jira [CS-1171](https://jira.tapestry.support/browse/CS-1171).
**Andrew_Au** (2024-12-24):
@@Tovi Wang Please update the ticket status
**Tovi Wang** (2024-12-24):
@@Andrew_Au  Since @@Sang said this issue was containd in Fix Round Calc Cpn Disc Amt base on NetNetAmt (KTS 241009 Jira FE-1520 v750.04R07+, v750.05).So I think we can closed this issue first.Waiting released v750.04R07+ to fixed this issue.Thanks!

## 相關資訊

- Jira: [FE-1520](https://ctil.atlassian.net/browse/FE-1520)
- Fix Version: 未記錄
- 解決日期: 2024-12-27
