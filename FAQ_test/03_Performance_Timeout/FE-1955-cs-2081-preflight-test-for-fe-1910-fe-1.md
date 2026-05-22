---
project: FE
issue_key: FE-1955
issue_type: Task
status: Design
faq_score: 6.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1955"
created: 2026-05-21
resolved: 
resolution: 
has_images: False
---

# FE-1955: [CS-2081] Preflight Test for [FE-1910] , [FE-1912] with no additional configurations

> **類型:** Task | **狀態:** Design
> **分類:** 效能與逾時 | **FAQ 分數:** 6.5
> **負責人:** Andrew_Au
> **組件:** Front End

## 問題描述

**Background:**
The development team has performed early development work for a forthcoming SOW. However, there are two intermediate SOWs scheduled for release before this enhancement goes live. To ensure no impact on these releases, the enhancement has been designed to be fully controllable—specifically, it can be disabled via empty, missing, or configuration-based settings.

**Testing Scope:**
Please validate that when the enhancement is **disabled**, the system behavior remains consistent with the current production behavior (i.e., prior to enhancement implementation).

Testing should include the following scenarios under the disabled configuration:

1. **Tax Mode** – Sales issuing should function as per existing logic(Pricing, Exclude Items , Printing, PCD).

2. **Non-Tax Mode** – Sales issuing should function as per existing logic(Pricing, Exclude Items , Printing, PCD).

**Expected Result:**
System behavior should remain unchanged from the current baseline when the enhancement is disabled.

Successful validation will allow the development team to proceed with the intermediate SOW releases without risk of regression from this enhancement.



## 相關資訊

- **Jira:** [FE-1955](https://ctil.atlassian.net/browse/FE-1955)