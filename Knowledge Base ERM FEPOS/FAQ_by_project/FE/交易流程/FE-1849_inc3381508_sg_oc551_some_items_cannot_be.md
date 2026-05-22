---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "**Mastconv Data: /ds411/share/JIRA/FE-1849/mastconv_SG_20260111.zip**"
root-cause: "待提取"
solution: "### Jira Comments (6 則)"
jira: FE-1849
resolved: 
fix-version: ""
---

# FE-1849: [INC3381508] SG OC551 Some items cannot be printed from POS system

## 問題

**Mastconv Data: \\ds411\share\JIRA\FE-1849\mastconv_SG_20260111.zip**
dbtrans Data:
Symptom:
Some items cannot be found and printed from POS system.
Troubleshooting:
1.The items able to find in Sales Page, but cannot find in label printing page.
2.User provided the list.
3.Resaved all issue items on BE,Issue still.
Device information:
Till 2
Issue items:
CCC23 B4MPL
CCM57 B4MPL
CCU00 B4MPL
CCX06 B4/N4
CCX07 B4MPL
CDG71 B4S0M
CDZ64 B4MPL
CR652 B4MPL
CU044 B4MPL
CW616 B4MPL
CCC42 B4/N4
1.Search by item CCC23,But NOT found the bar code 196395963683 in search result page.
@@Sang @@Cy Lau Could you help to further checking and find the RCA?
CC @@Joy Li @@pierre.shi
2.We can find the item searching by bar code 196395963683.
3.The items able to find in Sales Page

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (6 則)
**Automation for Jira** (2026-01-12):
Issue has been created since
Days since: 2
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2026-01-12):
@@Tovi Wang Please try to search barcode ' 196395963683' in other till, if POS cannot find it, then copy back SG mastconv for testing
**Tovi Wang** (2026-01-12):
@@Sang 用barcode ' 196395963683'可以正常搜索到这个item。现在问题是用Item 搜索不到这个barcode ' 196395963683'.详细截图如上图所示。It’s so strange.
@@Joy Li As we talked before.Could you help to copy the SG mastconv to Sang for further checking?Thanks!
**pierre.shi** (2026-01-12):
Hi @@Sang @@Joy Li @@Tovi Wang  dbtrans uploaded.
**Sang** (2026-01-12):
@@Tovi Wang @@Joy Li IN new dbmas created by  mastconv.dat, can’t find item no ‘CC23’, ‘CCM57’, ‘CCU00’; so can’t sell  in POS. But EAN table ca' find records.
**Tovi Wang** (2026-01-26):
Apply Mastconv for user till2 confirm issue fixed

## 相關資訊

- Jira: [FE-1849](https://ctil.atlassian.net/browse/FE-1849)
- Fix Version: 未記錄
- 解決日期: 未記錄
