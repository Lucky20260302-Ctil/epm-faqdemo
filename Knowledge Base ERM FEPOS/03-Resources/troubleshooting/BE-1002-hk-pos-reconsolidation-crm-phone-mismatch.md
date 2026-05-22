---
tags: [bug, production]
component: Backend
symptom: "HK POS reconsolidation failed for 61 records — VIP synchronization error due to phone number mismatch between POS and CRM"
root-cause: "POS captured correct phone number (96430785) and stored in PC file, but BE DB recorded wrong phone number (96430185) — CRM sync then fails with 'Vip number does not match the customer'"
solution: "Under investigation; temporary fix by correcting phone number in CRM to match POS data"
jira: BE-1002
resolved: 2025-05-02
---

# BE-1002: HK POS Reconsolidation Discrepancy — CRM Phone Number Mismatch

## 問題

HK POS reconsolidation found 61 records that failed to send sales data from CS2000 to Acxiom CRM. The error originated from VIP synchronization failure.

**Sample affected record:**
- VIP No: `OCF12H00230077`
- Sales Memo: `OCF1-20285439`
- Date: 2025-02-11
- CRM error: "fail to send member in member sync process: OCF12H00230077"
- CRM returned **400 error**: "Vip number does not match the customer"

## 根因

Investigation revealed a phone number inconsistency:

- **POS/PC file**: Customer entered correct phone `96430785`
- **T9 log**: Shows correct phone `96430785`
- **BE DB**: Phone number stored as `96430185` (wrong)
- **CRM**: `96430185` doesn't match the customer record

The correct phone number should be `96430785`, but somewhere between POS input and DB storage, the number was corrupted from `96430785` to `96430185` (digit 7 changed to 1).

The exact point of data corruption is still under investigation — BEAPI logs may provide further clues.

## 解法

The root cause of the data corruption (how `96430785` became `96430185` in DB) requires further investigation through BEAPI logs. The immediate fix was correcting the phone number in CRM to enable the sync to proceed.

_See Jira ticket for resolution details._

## 相關問題

- [[CS-1351]] — Coach Jira reference
- [[BE-944]] — Related CRM data sync issue
