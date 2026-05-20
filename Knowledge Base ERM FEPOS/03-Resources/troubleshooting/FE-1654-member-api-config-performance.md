---
tags: [change-request, production]
component: Front End
symptom: "CRM member API bottleneck during complete transaction causes serious performance issue in CN Tapestry stores"
root-cause: "Calling MemberSearch/Upsert API during CompleteTransaction creates a round-trip bottleneck — BEGW API retrieves from CRM and upserts member to BE DB on every transaction"
solution: "Add tblconfig.WEBAPIUPDATENEWMEMBER to control Acxiom call upsert Member API per transaction; add WEBAPIUpdateNewMemberatDayEnd for batch upsert at day end; write new member PCD '34' for posting integrity"
jira: FE-1654
resolved: 2025-09-30
---

# FE-1654: Add Config to Disable Member API During Complete Transaction

## 問題

CN Tapestry stores experienced serious performance issues due to the CRM API bottleneck during transaction completion. The `CreateInvoice` flow triggers multiple member API calls (query/upsert) that cause significant latency.

**Discovery**: Long time taken when completing a transaction — the API round-trip to CRM via BEGW creates a bottleneck.

**Trigger flow**: When `CreateInvoice` is called, the following member operations are triggered:
- Query of VIP when completing transactions
- Upsert member via Acxiom API

## 根因

The root cause is that every transaction completion calls the **BEGW member API** which:
1. Retrieves member data from CRM
2. Upserts member directly to BE DB
3. This round-trip is slow, especially for CN Tapestry stores

The existing design lacked a way to **disable or defer** these API calls for stores where the API is a bottleneck. The PCD data alone would be sufficient for posting integrity, but there was concern about missing Acxiom essential member data.

## 解法

**Fix in v750.04R11A, R12, v750.05:**

Added **two new config flags** to control member API behavior:

1. **`tblconfig.WEBAPIUPDATENEWMEMBER`**
   - `'Y'` — Call Web API to Upsert Member when creating transaction (default/current behavior)
   - `'N'` — Skip API call; write member data via PCD only

2. **`tblconfig.WEBAPIUPDATENEWMEMBERATDAYEND`**
   - `'Y'` — Call Web API to Upsert all outstanding members at Day End
   - Allows deferring API updates to batch processing

3. **PCD '34'** — All new member transactions write PCD '34' to ensure BE posting has member data even without the API call

**Performance consideration**: If the bottleneck is on the FE side, consider changing to FE background API call. If it's on the BEGW API side, this config-based approach allows deferring to Day End batch.

**Patch reference**: `KTS 250324 Jira FE-1654 v750.04R11A, R12, v750.05`

## 相關問題

- [[ACU-130]] — Original story reference
- [[FE-1476]] — Related member type/API handling fix
