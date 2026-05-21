---
tags: [bug, production, uat]
component: Front End
symptom: "Wrong member discount applied to VIPs with the same VIP type when both VIP discount and Mix & Match discount are 20% off"
root-cause: "Price calculation incorrectly uses local DB member type instead of API-returned online member type when both exist with different values"
solution: "Force online member type from API over local DB type; handle API return without PCard No by assigning Betting No.; enhance JC LM Auto Update on POS startup"
jira: FE-1476
resolved: 2024-09-04
---

# FE-1476: HKJC REMS MVP1 — Offline/Online Member Type Mismatch

## 問題

HKJC REMS CWL MVP1 — Multiple issues found in member profile and discount application:

1. **Wrong member discount** applied to VIP with same VIP type when both VIP discount and Mix & Match discount are 20% off
2. **Sensitive fields unprotected** — Betting A/C No., Email, Phone No. in Member Profile search screen
3. **Offline member data** (`dbmas`) contains dummy data not aligned with JC online data

## 根因

**Core issue (Scenario 4)**: When a member exists in both local DB and online API:
- API returns Member Type **'03'**
- Local DB has the same member with a **different** Member Type (e.g., 'S' or '05')
- Price calculation incorrectly uses the **local DB Member Type** instead of the **online API Member Type**
- This causes the wrong discount to apply when both VIP discount and Mix & Match discount share the same rate (20% off)

**Test Scenarios analyzed**:

| Scenario | API Type | Local DB | Effective MM | Expected Behavior | Actual (before fix) |
|----------|----------|----------|-------------|-------------------|---------------------|
| 1 | '03' | No record | No | Apply Member disc 20% | ✅ Correct |
| 2 | '03' | '05' (diff) | No | Apply Member disc 20% ('03') | ❌ Used local '05' |
| 3 | '03' | No record | Yes | Apply MM disc | ✅ Correct |
| 4 | '03' | '05' (diff) | No | Apply Member disc 20% ('03') | ❌ Used local '05' |

**Example member `PS07770915`**: API returned '03', local DB had type 'S'. System used local DB type 'S' (bug) — no effective MM, should apply Member disc 20% ('03').

## 解法

**Fixes included in v750.01R02N and v750.01R021:**

1. **Use Online Member Type** — Force price calculation to use API-returned member type instead of local DB type
2. **Handle API Return Without PCard No** — Assign Betting Account No. to PCard No. field when API does not return a PCard number
3. **Enhance JC LM Auto Update** — Update `Vipmas_ID_no` and `Vipmas_Staff_Code` on POS startup and Z-file update
4. **Member Search Restriction** — JC RM Member Panel only allows Member No. Input Box for member search
5. **Data recommendation** — For offline mode testing, truncate `vipmas` table on local DB and import one set of updated data aligned with online testing data

## 相關問題

- [[FE-1476-hkjc-rems-member-type-offline-online-mismatch|FE-1476]] — HKJC REMS CWL MVP1
