---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "[BASH] Incorrect Day End print out not fit in the A4 size paper"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1761
resolved: 2025-11-03
fix-version: ""
---

# FE-1761: [BASH] Incorrect Day End print out not fit in the A4 size paper

## 問題

[BASH] Incorrect Day End print out not fit in the A4 size paper
Version: 7.5.0.05 (build250918)
**VM:**
172.16.138.4
acc:  .\sxd
pw:   AOtesting..
**POS Login:**
acc: 99999
pw: 9999
**Existing result:**

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-11-03
### Jira Comments (5 則)
**Sang** (2025-10-02):
@@Sherman tseRevised program uploaded to \\ds411\share\POS_FE_Release_64\20251002 BASH v750.05 Beta and 172.16.138.4
|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
**Sherman tse** (2025-10-03):
@@Sang  tested with the new release, the day end print out can fit in the A4 size paper now, but some places are not align as below:
**Sang** (2025-10-06):
@@Sherman tse RP file show Qty column proper alignment.
**Sang** (2025-10-06):
@@Sherman tse v75 layout align the memo Qty / Sales Qty in same Qty column.
**Automation for Jira** (2025-11-03):
Issue has been created since
Days since: 33
Week since : 4
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1761](https://ctil.atlassian.net/browse/FE-1761)
- Fix Version: 未記錄
- 解決日期: 2025-11-03
