---
tags: [bug, production]
component: Front End
symptom: "Promo Code CLE062A not reflected on JP store POS J433 and J378, fixed by re-saving promo code in BE"
root-cause: "Zfile z241226.06 update failed on 2024-12-26 — MASTCONV.DAT request failure caused promo data to not sync to POS"
solution: "Added PCD '81' write on zupdate failure to log DB table update errors for diagnostics; re-saving promo code in BE triggers fresh sync"
jira: FE-1611
resolved: 2025-05-21
---

# FE-1611: Promo Code Not Reflected in POS — Zfile Update Failure

## 問題

JP stores J433 and J378 reported that clearance event sales amounts were not reflected in reports. Investigation found that Promo Code `CLE062A` was not showing in POS, even though the promo setting in BE appeared normal.

**Affected period**: 2024-12-26 to 2025-01-08
**Control comparison**: J425 could reflect the promo code correctly

**Fix action**: Re-saving the promo code in CS2K BE on 2025-01-09 resolved the issue for both stores.

## 根因

The root cause was a **Zfile update failure** on 2024-12-26:

```
[26/12/2024 09:24:43] Error Log: z24122604
[26/12/2024 09:24:43] ******* RESEND ZUPDATE LOG (z24122604) FAILURE, 
           REQUEST FOR MASTCONV.DAT ******
```

The Zfile update failed because `TblItmast` (item master table) could not be updated. Since the promo code data is distributed via Zfile, the failure meant store J433 and J378 never received the updated promo configuration.

Re-saving the promo code in BE triggered a fresh Zfile generation, which then synced successfully to the affected stores.

## 解法

**Fix in v750.04R10, v750.05:**
- Added Zupdate failure write **PCD '81'** to log DB table update errors
- Format: `81 P01 z22100301 0 Update DB Table ERROR - TblItmast 0/1`
- This allows proactive monitoring of Zfile update failures

**Patch reference**: `KTS 250127 FE-1611 v750.04R10, v750.05`

## 相關問題

- [CS-1319](https://hktdc.atlassian.net/browse/CS-1319) — Coach Jira reference
- [[FE-1646-v75-dayend-cs2kconnect-missing|FE-1646]] — Related V75 dayend/cs2kconnect schedule fix
