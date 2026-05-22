---
tags: [improvement, production]
component: Backend
symptom: "CRM upsert cannot update vip_no_edm, vip_no_dm, vip_no_phone, vip_no_sms when CRM expiry_date differs from BE DB"
root-cause: "Backend DB rejects updates to vip_no_edm/dm/phone/sms flag fields when the incoming CRM expiry_date does not match the existing DB value"
solution: "Add dbconfig flag beapi_allow_update_vip_expiry_date = 'Y' to allow direct update of vip_expiry_date from CRM"
jira: BE-987
resolved: 2025-02-25
---

# BE-987: CRM vip_no_edm/dm/phone/sms Cannot Be Updated Due to Expiry Date Mismatch

## 問題

When CRM upserts a member whose `expiry_date` differs from the Backend DB value, the system rejects updates to the following member preference fields:
- `vip_no_edm` (no EDM)
- `vip_no_dm` (no direct mail)
- `vip_no_phone` (no phone contact)
- `vip_no_sms` (no SMS)

This prevents CRM from properly synchronizing member communication preferences to the Backend.

## 根因

The Backend DB has a validation rule that blocks updates to these preference fields when the incoming `vip_expiry_date` from CRM does not match the existing value in the database. The expiry date mismatch is treated as a data inconsistency and the entire update is rejected, including the preference flags.

## 解法

Added a configuration flag to control this behavior:

**`dbconfig.beapi_allow_update_vip_expiry_date = 'Y'`**

When set to `'Y'`, the Backend API allows direct updates to `vip_expiry_date` from CRM, which resolves the mismatch and allows the preference flag updates to proceed.

**Release**: `\\ds411\public\samuel\beapi\v1.6.20_20250115`

**Tested with**: Member `OC135TC00000028` on QA

## 相關問題

- [[BE-944]] — Related CRM data sync issue (vip name sync)
- [[BE-1039]] — Related CRM upsert performance improvement
