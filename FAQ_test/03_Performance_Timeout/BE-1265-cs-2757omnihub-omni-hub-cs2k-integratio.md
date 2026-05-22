---
project: BE
issue_key: BE-1265
issue_type: Improvement
status: Selected for Development (migrated)
faq_score: 5.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, api]
jira_url: "https://ctil.atlassian.net/browse/BE-1265"
created: 2026-05-19
resolved: 
resolution: 
has_images: False
---

# BE-1265: [CS-2757][OmniHub] Omni hub & CS2K Integration - Add Email Alert for Promotion Engine Job Failure

> **類型:** Improvement | **狀態:** Selected for Development (migrated)
> **分類:** 效能與逾時 | **FAQ 分數:** 5.5
> **負責人:** Jerry Wong
> **組件:** API

## 問題描述

# Proposed Approach (Execution-Level Monitoring)

We can implement a **lightweight background monitoring job** (e.g. NET service or PowerShell script) that runs **once per day** or **in certain time interval within a day.**

This job will:

- Read the MMTableVersionHistory table

- Check Target suffix (_1 /_2) , last created date time / update date time.  

- Send out alert email only in extraction not executed:  “No VersionHistory Record is found” during job run.

# Alert Logic:

- ✅ If the suffix is switched,

- → the extraction job is completed

- ❌ If the last suffix is not today / no today's history record,

- → the extraction job is **not** completed

**Benefit:** 

- This suggestion requires no current MM extraction program change as we will build standalone service to check the MM extraction version history from backend DB directly.

- **Easiest way** to capture status of MM extraction not completed with the minimum resource.

 

**Limitation:** 

- This background can only capture the status of program execution not completed; no extra failure status or information can be provided.

- Dependence of the SMTP server and the job schedule itself. **Potential failure point** on SMTP server or the scheduler which use to trigger the job.

- If DB connection failure, it will not be able to query the last version history from backend DB. But it can still send alert email to notify this type of error.

- If the extraction is still running without failure, the alert will still send email as no completion record in MMTableVersionHistory.

 



## 相關資訊

- **Jira:** [BE-1265](https://ctil.atlassian.net/browse/BE-1265)
- **標籤:** OmniHub