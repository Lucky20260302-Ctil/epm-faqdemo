---
tags: [bug, production]
component: Backend
symptom: "CRM API returns correct vip_name1 = 'Yoyo' and vip_last_name = 'Yoyo', but BE DB stores vip_name1 = 'BEAPI' and vip_last_name = NULL"
root-cause: "BEAPI overwrites CRM API response name fields with default/fallback values instead of using the CRM-provided name data"
solution: "Fix BEAPI logic to properly pass through CRM API response name values instead of overwriting with defaults"
jira: BE-944
resolved: 2025-02-24
---

# BE-944: CRM VIP Name Cannot Sync with CRM API Response

## 問題

When CRM API responds with correct member name data, the Backend DB stores incorrect default values instead.

**Affected store**: OC182 (V75 pilot store)

**Observed behavior:**
- CRM API response: `vip_name1 = 'Yoyo'`, `vip_last_name = 'Yoyo'`
- BE DB stored: `vip_name1 = 'BEAPI'`, `vip_last_name = NULL`

This caused member names to display as "BEAPI" in POS, which is clearly a fallback/default value rather than the actual member name.

## 根因

The BEAPI (Backend API) has a logic path where it overwrites the CRM API response name fields with default/fallback values instead of properly passing through the CRM-provided name data. When the CRM returns valid name values, the BEAPI should use those values, but instead it substitutes them with a hardcoded or internal default.

The exact condition that triggers this overwrite is still under investigation but is related to how BEAPI processes the CRM upsert response before writing to the member database.

## 解法

Fix the BEAPI logic to properly pass through CRM API response name fields (`vip_name1`, `vip_last_name`) instead of overwriting them with default values when the CRM returns valid name data.

_See Jira ticket for resolution details._

## 相關問題

- [[ACU-106]] — Original story reference
- [[BE-987]] — Related CRM data sync issue
- [[BE-1002]] — Related CRM data sync (phone number)
