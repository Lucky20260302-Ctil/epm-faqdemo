---
tags: [bug, production]
component: Front End
symptom: "HK eName registration cannot pre-scan VIP barcode before submitting registration because VIP data is not yet queryable during transaction"
root-cause: "HK eName uses CBDT online member API which only queries VIP once (design assumes VIP already exists), unlike JP eName which queries FE→BE twice (registration and payment)"
solution: "Enhance DotNet print-out to make a second API call after payment for new VIPs where the first query returned no name"
jira: FE-1318
resolved: 2024-05-07
---

# FE-1318: HK eName VIP Barcode Pre-Scan — CBDT Single-Query Limitation

## 問題

When processing eName registration in Hong Kong stores, VIP barcode cannot be pre-scanned before the eName registration is submitted. The VIP date cannot be queried during the transaction, preventing the cashier from scanning the barcode/QR code upfront.

## 根因

The root cause is a fundamental design difference between JP and HK eName VIP query flows:

**JP eName flow:**
1. Query VIP when creating new VIP — directly from FE to BE → no data yet
2. During payment (registration submitted), query again from FE to BE → VIP data becomes available
3. ✅ VIP is queryable by the time barcode is needed

**HK eName flow (CBDT):**
1. Call 'online member API' from FE → CDP to check customer from region '11'
2. Check privacy policy to determine if customer can be queried
3. Query goes to BE and calls **only once** (design assumes VIP already exists)
4. For eName join, FE still queries only one time
5. ❌ Since the VIP is newly created, the single query returns no data, making barcode pre-scan impossible

## 解法

Sanyo team enhanced the DotNet print-out program to add **one more API query** after payment during printing:

- **Existing VIP** queried in the first call → second query is skipped
- **First-time VIP** where `vip_name = '-'` (empty) from first query → execute second query to retrieve the newly created VIP data

**Business alignment**: Business agreed to scan barcode/QR code **only after eName registration is submitted**. Currently there is no business impact for eName registration.

**Deployment**: This enhancement is planned to go together with the HK EFT payment SOW deployment.

**Implementation detail** (v720.02R26A / v750.04):
- Only Coach companies (`CompanyCode` or `prtCompany` starts with 'COACH') use eName
- Only customized region print-outs showing member name need re-query if first/last name is `'-'` or `''`
- Excludes `COACHJP` and `KS_JP`

## 相關問題

- [[FE-???|EFT Payment SOW]] — HK EFT payment deployment
