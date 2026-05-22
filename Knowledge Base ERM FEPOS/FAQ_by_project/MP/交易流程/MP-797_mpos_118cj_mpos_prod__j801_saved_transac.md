---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "After upgraded the version, retrieve the temporary saving transaction from POS. The Casher ID remain"
root-cause: "待提取"
solution: "### Jira Comments (4 則)"
jira: MP-797
resolved: 
fix-version: ""
---

# MP-797: [MPOS-118]CJ mPOS Prod_ J801 Saved transaction retains old cashier ID after upgrade

## 問題

After upgraded the version, retrieve the temporary saving transaction from POS. The Casher ID remained as the associate who saved the transaction so Casher at the POS need to input again.
Reproduce steps(v75.004.1305.0001)
1. 
2. 
3. 
4.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (4 則)
**Tovi Wang** (2025-08-29):
@@Sang Please help to take a look this issue.Thanks!
CC @@Cy Lau @@Joy Li FYI.
**Automation for Jira** (2025-09-02):
Issue has been created since
Days since: 4
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2025-09-02):
@@sherman @@Tovi Wang cc @@Joy Li @@Bobby@@Cy Lau
v750.04R14B
1.
**Sherman tse** (2025-09-15):
Testing result: pass
Cashier ID feature would follow back V72
Test case attached

## 相關資訊

- Jira: [MP-797](https://ctil.atlassian.net/browse/MP-797)
- Fix Version: 未記錄
- 解決日期: 未記錄
