---
tags: [faq, fe, 列印]
component: "Receipt Printing"
symptom: "ANZ (Australia and New Zealand) will adopt the SG (Singapore) printing layout. However, during testi"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1770
resolved: 2026-02-11
fix-version: ""
---

# FE-1770: ANZ TMU Receipt printing(Tax Exemption & Footer

## 問題

ANZ (Australia and New Zealand) will adopt the SG (Singapore) printing layout. However, during testing of the SG layout with tax exemption applied, it was observed that **tax details such as tax amount and percentage are not displayed** in the printed output.
Given that:
- 
- 
Both regions will be set to **tax-exempt** status. However, for transparency and audit purposes, the printed documents should still **display the tax exemption details**, including:
- 
- 
- 
**Expected Outcome:**
- 
- 
- 
**Acceptance Criteria:**
- 
- 
-

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-02-11
### Jira Comments (6 則)
**Sang** (2025-10-22):
@@Joy LiSG / ANZ Tax Layout
ANZ Tax Exempted Layout
**Automation for Jira** (2025-11-03):
Issue has been created since
Days since: 17
Week since : 2
Issue due date difference
Days since : 
Weeks since:
**Sang** (2025-11-04):
Revised Tax Exempted Memo Print Out
**Sang** (2025-11-04):
1.
**Sang** (2025-11-04):
Please find updated program for Coach ANZ in \\ds411\share\POS_FE_Release_64\20251105 Coach AZN v750.04R14F
**Joy Li** (2025-12-15):
FE tested and released.

## 相關資訊

- Jira: [FE-1770](https://ctil.atlassian.net/browse/FE-1770)
- Fix Version: 未記錄
- 解決日期: 2026-02-11
