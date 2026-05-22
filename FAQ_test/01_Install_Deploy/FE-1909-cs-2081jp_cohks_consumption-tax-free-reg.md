---
project: FE
issue_key: FE-1909
issue_type: Bug PRD
status: SOW Send
faq_score: 9.5
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, fe, install_deploy, front-end, mpos, mpos_api]
jira_url: "https://ctil.atlassian.net/browse/FE-1909"
created: 2026-03-27
resolved: 
resolution: 
has_images: False
---

# FE-1909: [CS-2081]JP_COH&KS_Consumption Tax Free regulation change

> **類型:** Bug PRD | **狀態:** SOW Send
> **分類:** 安裝與部署 | **FAQ 分數:** 9.5
> **負責人:** Cy Lau
> **組件:** Front End, MPOS, MPOS_API

## 問題描述

Due to JP tax free regulation change, POS need to have enhancement/change.

but from operation team point of view, they don't want to change any store operation. 

TLDR;Coverage : 

- [ ] FEPOS
- [ ] Fast Tax free switchingPCD for tax free = Y / N
- [ ] MPOS 
- [ ] Fast Tax free switching
- [ ] MPOS API
- [ ] PCD(sqlPCD) for tax free = Y/NDistinguish tax free item eligible
- [ ] SalesHub 
- [ ] PCD(sqlPCD) for tax free = Y/NDistinguish tax free item eligible
- [ ] CAR
- [ ] follow up for the Export

---

# **JIRA Proposal – Japan Consumption Tax‑Free Regulation 2026 (Nov) Adaptation**

**Scope:** CSPLUS (FEPOS, MPOS) & Tapestry (CAR)
 

---

# **Objective**

Enable CSPLUS to comply with Japan’s 2026 November Consumption Tax‑Free regulatory changes.

---

# **Targets**

- **CSPLUS**

- FEPOS

- MPOS

- **Tapestry**

- CAR

---

# **Goals**

1. Mark Tax‑Free sales with a **TaxFree flag**.

2. Ensure **GST is excluded** from all price and transaction calculations.

3. Trigger the existing **Tax‑Free survey workflow** (nationality prompt) with no changes to UX.

4. Support **instant Tax‑Free switching** during checkout (optional but achievable with new logic).

---

# **Preliminary Design / Key Assumptions**

1. **Item pricing from SAP remains tax‑inclusive** (unchanged from current design).

2. **All customer transactions remain unified**; no distinction (local vs tourist) in stored data schemas.

3. **Receipt amounts must always match DB‑stored values** (data integrity requirement).

4. **CAR export continues to use the same dataset**, no additional transformation required.

---

# **Enhancement Highlights**

# **1. SOP for Tax‑Free (UI/UX)**

- Maintain the **current SOP** and UI/UX behavior.

- The **Tax‑Free button** remains visible and functionally triggers the nationality survey as it does today.

- No UI workflow change is introduced except behind‑the‑scenes calculation logic (controlled by config).

---

# **2. New Configuration Flag**

A new configuration parameter will be introduced:

`TaxFreeSkipGSTInCalculation = Y / N`

# **Config Behaviour**

- **N (default)**

- Retains the **original Tax‑Free flow** (existing implementation).

- **Y (new flow enabled)**

- The Tax‑Free button behaviour is updated.

- Upon activation:

- Sets the **TaxFree flag** on the sale.

- **GST is excluded** from:

- Item amount

- All calculations

- Any GST‑related totals

- System proceeds with a **normal sales flow but without GST**.

*****This configuration enables instant switching between “Normal Sale” and “Tax‑Free Sale” during checkout.**

---

# **3. Dataset Changes (PCD / BEDB)**

- Only the **GST Amount** will be stored (as per current design).

- PCD and BEDB datasets will mirror the **exact values printed on the receipt** to maintain consistency.

- CAR will receive **unchanged dataset format**, ensuring backward compatibility with CAR processing pipelines.

---

# **4. Receipt Output**

- Receipt layout remains unchanged.

- Value presentation will reflect:

- Item price excluding GST

- GST = 0 for Tax‑Free transactions

- Totals consistent with DB‑stored values

---

# **Summary**

This enhancement introduces a configuration‑driven approach to support Japan’s 2026 Tax‑Free regulation without requiring UI/UX redesign. The system can instantly switch between Tax‑Free and normal flows while keeping pricing integrity, receipt consistency, and CAR export compatibility.

SOW : 
 [📎附件](https://ctil.atlassian.net/rest/api/3/attachment/content/cad3365d-213b-48d4-ba54-0d68dc26ca18) 



## 相關資訊

- **Jira:** [FE-1909](https://ctil.atlassian.net/browse/FE-1909)