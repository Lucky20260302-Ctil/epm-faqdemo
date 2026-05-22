---
tags: [faq, fe, 列印]
component: "report"
symptom: "Test POS: 10.33.248.5 and 10.33.248.6"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1724
resolved: 2025-07-15
fix-version: ""
---

# FE-1724: [CS-1487] No Qty for Void and return deposit listed on Till1 dayend report

## 問題

Test POS: 10.33.248.5 and 10.33.248.6
FE Version: V75.004.1303.0001
Steps:
1. 
1. 
There are two issues:
<span style="color:#ff5630">**1.Till1 is laser printer.Till1 dayend report NOT display follow 2 line.**</span>
<span style="color:#ff5630">**'取消定金单数量'**</span>
<span style="color:#ff5630">**‘退回定金单数量’**</span>
<span style="color:#ff5630">**2.Consolidation 按金单数量 ！=Till0 按金单数量 + Till1 按金单数量**</span>
@@Cy Lau @@Sang Could you help to double check and confirm the deposit display logic?Thanks!
CC @@Joy Li
1.
2.Till0 is TMU printer.
3.Till1 is laser printer.Till1 dayend report NOT have
'取消定金单数量'
‘退回定金单数量’
4.Consolidation 按金单数量 ！=Till0 按金单数量 + Till1 按金单数量
Consolidation 按金单数量:7
Consolidation 按金结算数量:2
Till0 按金单数量 ：3
Till0 按金结算数量：1
Till1 按金单数量 ：5
Till1 按金结算数量：1

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-15
### Jira Comments (11 則)
**Cy Lau** (2025-07-09):
@@Sang
Correct me if im wrong, the alignment on the definition would be on **Coach/Kate** **Spade** all region *except JP* on <span style="color:#ff991f">**TMU**</span> only but *not* the <u><span style="color:#ff5630">laser</span></u> right ?
**Tovi Wang** (2025-07-09):
@@Sang @@Cy Lau  Please help to further checking.
**Sang** (2025-07-10):
@@Tovi Wang These two file is 8-Jul db. Please re-get 6-Jul Till 0 and Till 1 dbtrans.sdf; Till 0 6-Jul log and PC file. Thanks
**Sang** (2025-07-10):
@@Tovi Wang @@Cy Lau
A4 Day-end report ‘No of Deposit section’ - Deposit Memo Qty include Void deposit Qty, and miss ‘Deposit Return Memo Qty’ line. Will align A4 ‘deposit memo Qty’ section to same as TMU. And Add control print 'deposit memo Qty’ section by Deposit Module Flag.
**Cy Lau** (2025-07-10):
@@Sang so what’s ur testing result for both TMU and A4 laser?
@@Tovi Wang  please help to get the
Please re-get 6-Jul Till 0 and Till 1 dbtrans.sdf; Till 0 6-Jul log and PC file.
**Tovi Wang** (2025-07-10):
@@Sang @@Cy Lau  All files here.Please help to check.
**Sang** (2025-07-10):
v750.04R13E
1. 
2. 
Use OCQ91 6-Jul dbtrans.sdf (Till 1)
Consolidated Day End
Disable Deposit(Syscon_Dep_mod=0)
**Cy Lau** (2025-07-11):
\\ds411\share\POS_FE_Release_64\20250710 Coach v750.04R13E\PrintAgent
**Sherman tse** (2025-07-15):
Issue has been created since
Days since: 6
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Joy Li** (2025-07-15):
Issue has been created since
Days since: 7
Week since : 1
Issue due date difference
Days since : 
Weeks since:
**Joy Li** (2025-07-15):
FE package V75.004.1503.0000 is released on 2025-07-15
-

## 相關資訊

- Jira: [FE-1724](https://ctil.atlassian.net/browse/FE-1724)
- Fix Version: 未記錄
- 解決日期: 2025-07-15
