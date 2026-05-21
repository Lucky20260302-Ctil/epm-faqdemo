---
tags: [bug, production]
component: MPOS
symptom: "MPOS does not restart or update POS date after Front End POS Day End when MPOS is idle on login page"
root-cause: "MPOS UI stays on login page with cached POS date and does not detect that the Front End POS has completed Day End and changed system date"
solution: "MPOS detects POS date change and pops error message, then forces MPOS restart to reload shop config and latest POS date"
jira: MP-499
resolved: 2021-09-21
---

# MP-499: MPOS Doesn't Restart After POS Day End

## 問題

When a staff member stays on the MPOS **login page** (idle, not logged in) and the Front End POS completes Day End, the MPOS UI does not update to reflect the new POS date and till number. This causes:

- Incorrect date shown in MPOS
- Shop config not refreshed
- Potential transaction date mismatches

**Reproduce steps:**
1. FE POS date = 2021-01-01
2. MPOS starts and stays on login page (no login)
3. FE POS processes Day End → system date changes to 2021-01-02
4. MPOS logs in → still shows date = 2021-01-01 (incorrect)

## 根因

MPOS only loads POS date and shop config at **initial startup**. While the app is idle on the login page, it does not monitor for system date changes or POS Day End events. The FE POS date changes after Day End, but MPOS has no mechanism to detect this change and reload its configuration.

## 解法

Enhanced MPOS to:
1. **Detect** when the Front End POS date has changed (compared to cached value)
2. **Pop an error message** informing the user
3. **Force restart** MPOS to reload the shop config and latest POS date

**Fix Version**: `3.13.0`

## 相關問題

- [[FE-1225-dotnet-dayend-missing-transaction-count|FE-1225]] — Related Day End issues (FE side)
- [[FE-1646-v75-dayend-cs2kconnect-missing|FE-1646]] — Day End cs2kconnect schedule
