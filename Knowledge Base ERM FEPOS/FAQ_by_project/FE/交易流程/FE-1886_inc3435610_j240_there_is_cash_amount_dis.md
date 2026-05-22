---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Morning sang ko,Store callout that there is cash amount 173,300 discrepancy in RC report."
root-cause: "待提取"
solution: "### Jira Comments (5 則)"
jira: FE-1886
resolved: 
fix-version: ""
---

# FE-1886: [INC3435610] J240 There is cash amount discrepancy in dayend report.

## 問題

Morning sang ko,Store callout that there is cash amount 173,300 discrepancy in RC report.
I have one quick question,May I confirm that under what circumstances would such a discrepancy occur in the RC report?
INC3435610
1.RC report:
2.The cash flow 173,300 is come from Till0 which entered by store user.
Till0 RP:
3.From T9 log we can see that cashier id 488188 entered the cash flow amount 173,300

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (5 則)
**Tovi Wang** (2026-02-12):
@@Sang SOG team provided All the logs and files.Please further checking.
CC @@Joy Li @@pierre.shi
**Sang** (2026-02-12):
@@Tovi Wang @@Joy Li J240 have 3 tills. Please copy Till 1 and Till 2 dbtrans (Dbtbk08.1.sdf and Dbtbk08.2.sdf) and Dbtbk09.sdf from Till 0.
**Sang** (2026-02-12):
@@Tovi Wang Please copy Till 1 (Dbtbk08.1.sdf) and Till 2 (Dbtbk08.2.sdf if available)  dbtrans and Dbtbk09.sdf from Till 0.
**pierre.shi** (2026-02-12):
Hi @@Sang  dbtbk has been uploaded as attachment. Please help to check.
**Sang** (2026-02-12):
@@Tovi Wang @@pierre.shi @@Joy Li  J240 has Till 0-2, in Till 0 found till 2026.02.08 dbtrans (dbtbk02.02.sdf),  Total Cash Flow show in RC report is 173300+93300+173300 = 439,900.
<span style="color:#ff991f">**But Till 2 backup dbtrans (dbtbk08.2.sdf) actually is a copy of Till 0 2026.02.08 dbtrans.  Please find out why ?**</span>

## 相關資訊

- Jira: [FE-1886](https://ctil.atlassian.net/browse/FE-1886)
- Fix Version: 未記錄
- 解決日期: 未記錄
