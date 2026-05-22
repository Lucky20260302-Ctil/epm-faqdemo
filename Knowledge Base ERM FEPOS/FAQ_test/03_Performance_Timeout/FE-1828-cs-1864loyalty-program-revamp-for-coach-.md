---
project: FE
issue_key: FE-1828
issue_type: Change Request
status: Selected for Development (migrated)
faq_score: 7.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1828"
created: 2025-12-08
resolved: 
resolution: 
has_images: False
---

# FE-1828: [CS-1864]Loyalty Program Revamp for Coach Japan

> **類型:** Change Request | **狀態:** Selected for Development (migrated)
> **分類:** 效能與逾時 | **FAQ 分數:** 7.5
> **負責人:** Sang
> **組件:** Front End

## 問題描述

Coach Japan would also like to have the **Loyalty Program Revamp**

**Background:**

- Current system displays detailed VIP customer information, group membership, stage information, and coupon points across mobile POS, CS2000, and EM Capture systems

- Business requirement: Hide certain loyalty details from UI while preserving backend data and functionality

**Proposed Changes:**

- Hide VIP customer detail information from UI

- Hide group and stage information from UI

- Remove coupon point display from CLM (Customer Loyalty Management) system integration to CS2000

- Maintain data availability in backend for future use

**Technical Implementation Uncertainty:**

- **Critical Blocker:** Unknown if loyalty data flows via API or direct database linkage

- **If API:** Configuration-based removal of loyalty program data fields at API level; no database or deployment changes needed; minimal QA regression testing required

- **If Database Direct:** Front-end UI changes required; more extensive testing and deployment needed; affects database relationships

**Data Source Investigation Required:**

- Confirm whether loyalty binding data comes from API or direct database access

- Determine treatment of additional customer information fields

- Verify data origin (API vs. direct DBSS access) for member and coupon information



## 相關資訊

- **Jira:** [FE-1828](https://ctil.atlassian.net/browse/FE-1828)