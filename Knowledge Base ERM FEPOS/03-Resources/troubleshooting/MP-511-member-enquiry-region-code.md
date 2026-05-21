---
tags: [bug, qa]
component: MPOS API
symptom: "MPOS member enquiry returns 'Record Not Found' for valid members due to incorrect region code"
root-cause: "MPOS API does not read its own region code from vbretai.ini, causing it to query the wrong region's member database"
solution: "Program update for API to get own region code from vbretai.ini configuration"
jira: MP-511
resolved: 2021-12-08
---

# MP-511: MPOS Member Enquiry Returns 'Record Not Found'

## 問題

MPOS member enquiry returns "Record Not Found" for members that are valid and exist in the system. This prevents MPOS from looking up member information and processing member transactions.

## 根因

The MPOS API was not reading its **own region code** from the `vbretai.ini` configuration file. When the API performs a member search, it uses the region code to determine which database to query. Without the correct region code, the API queries the wrong region's member database and returns "Record Not Found."

## 解法

Program update for the API to **read its own region code** from `vbretai.ini` before performing member enquiries. This ensures the API queries the correct regional member database.

**Fix Versions**: `3.14.0`, `3.13.2`

## 相關問題

- [MP-510](https://ctil.atlassian.net/browse/MP-510) — Same fix (duplicate ticket)
