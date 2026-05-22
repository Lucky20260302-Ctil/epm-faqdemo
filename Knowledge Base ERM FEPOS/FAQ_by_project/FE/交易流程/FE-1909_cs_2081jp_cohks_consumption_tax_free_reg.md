---
tags: [faq, fe, 交易流程]
component: "Front End, MPOS, MPOS_API"
symptom: "Due to JP tax free regulation change, POS need to have enhancement/change."
root-cause: "待提取"
solution: "### Jira Comments (7 則)"
jira: FE-1909
resolved: 
fix-version: ""
---

# FE-1909: [CS-2081]JP_COH&KS_Consumption Tax Free regulation change

## 問題

Due to JP tax free regulation change, POS need to have enhancement/change.
but from operation team point of view, they don't want to change any store operation.
TLDR;Coverage :
- [x] FEPOS
- [x] 
- [x] MPOS
- [x] 
- [x] MPOS API
- [x] 
- [x] SalesHub
- [x] 
- [x] CAR
- [x] 
---
# **JIRA Proposal – Japan Consumption Tax‑Free Regulation 2026 (Nov) Adaptation**
**Scope:** CSPLUS (FEPOS, MPOS) & Tapestry (CAR)
---
# **Objective**
Enable CSPLUS to comply with Japan’s 2026 November Consumption Tax‑Free regulatory changes.
---
# **Targets**
- 
- 
---
# **Goals**
1. 
2. 
3. 
4. 
---
# **Preliminary Design / Key Assumptions**
1. 
2. 
3. 
4. 
---
# **Enhancement Highlights**
# **1. SOP for Tax‑Free (UI/UX)**
- 
- 
- 
---
# **2. New Configuration Flag**
A new configuration parameter will be introduced:
`TaxFreeSkipGSTInCalculation = Y / N`
# **Config Behaviour**
- 
- 
*****This configuration enables instant switching between “Normal Sale” and “Tax‑Free Sale” during checkout.**
---
# **3. Dataset Changes (PCD / BEDB)**
- 
- 
- 
---
# **4. Receipt Output**
- 
- 
---
# **Summary**
This enhancement introduces a configuration‑driven approach to support Japan’s 2026 Tax‑Free regulation without requiring UI/UX redesign. The system can instantly switch between Tax‑Free and normal flows while keeping pricing integrity, receipt consistency, and CAR export compatibility.
SOW :

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (7 則)
**Automation for Jira** (2026-03-27):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Cy Lau** (2026-03-27):
Todo :
Estimation for each component
@@Sang  @@Daniel Leung @@Jerry Wong 
@@Jerry Wong  may also involve in MPOS API
|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
---
@@Ken Wang  @@Joy Li  @@Bobby  for visibility
@@Andrew_Au  @@Sherman tse  for QAQC test case estimation
**Sang** (2026-03-27):
@@Cy Lau @@Ken Wang please upload SOW to Jira
**Cy Lau** (2026-03-29):
@@Sang
**Sang** (2026-03-30):
@@Cy Lau With refer to SOW. please clarify following requirement under new flow enable,
1. 
2. 
3. 
4.
**Daniel Leung** (2026-03-30):
@@Cy Lau 
Fast Switching MPOS - 3
Fast Switching Calc - MPOSAPI - 4
New TaxFree handling - MPOS API - 4
Fast Switching Calc - SalesHub - 4
New TaxFree handling - SalesHub - 4
**Cy Lau** (2026-05-21):
From @@Sang 
Updated Program  v750.04R26 uploaded to \\ds411\share\POS_FE_Release_64\20260520 Coach v750.04R26
1. 
a. tblconfig.TaxFreeSkipGSTInCalculation='Y' (Default 'N', 'Y'-Tax Free Flag only)
  b. Runtime Instant switch from Normal sales to 'marked Tax Free'and reverse
  c. switch from Normal sales to 'marked Tax Free' - remove tax Free Exclude Items, Add log and show message (Resource)
  d. Marked Tax Free Mode – Validate Item is not tax Free Exclusive Item – Select/barcode/Sku Input
  e. Retrieve Queue Basting
     – handle MarkTaxFree and auto Marked Tax Free on taxExempted
  f. Cancel Payment - Retain Original 'Mark Tax Free Status' (? AUTOTAXFREEMODE)
  g. Complete/Cancel Sale memo - Init Memo - Resume Default 'Marked Tax Free' Status (? AUTOTAXFREEMODE)
  h. Marked Tax Free - Input Nationality
  i. Local DB invtrx_tax_Exempted='X'
  j. PCD invtrx_tax_Exempted='X' --> 'Y'
  k. View Marked Tax Free SM

## 相關資訊

- Jira: [FE-1909](https://ctil.atlassian.net/browse/FE-1909)
- Fix Version: 未記錄
- 解決日期: 未記錄
