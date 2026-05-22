---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "[LCX] Redeem Qty=0 of gift code can be comfirmed when Gift Redeem items summary has other gift code "
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1911
resolved: 2026-04-21
fix-version: ""
---

# FE-1911: [LCX] Redeem Qty=0 of gift code can be comfirmed when Gift Redeem items summary has other gift code Redeem Qty=1

## 問題

[LCX] Redeem Qty=0 of gift code can be comfirmed when Gift Redeem items summary has other gift code Redeem Qty=1
Specific condition:
Gift Redeem items summary has  gift code A Redeem Qty=1 and gift code B Redeem Qty=0
Existing result:
Still able to complete the redeem process cauing pc file has one more 19 line with 0 amount
PC file content:

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-04-21
### Jira Comments (4 則)
**Automation for Jira** (2026-03-30):
Issue has been created since
Days since: 2
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2026-03-30):
@@Sherman tse
Gift Redeem - Gift redeem Rule set gift item qty =0 and Multi Gift Set Write PCD Fixed (KTS 260330 FE-1911 v750.05R11). Program uploaded to \\ds411\share\POS_FE_Release_64\20260330 LCX v750.05R11
**Andrew_Au** (2026-04-16):
Please update the ticket status
**Sherman tse** (2026-04-21):
Verifed on QA
Close case

## 相關資訊

- Jira: [FE-1911](https://ctil.atlassian.net/browse/FE-1911)
- Fix Version: 未記錄
- 解決日期: 2026-04-21
