---
tags: [improvement, production]
component: Backend
symptom: "CRM member upsert process during transaction takes ~6 seconds out of ~10 seconds total, causing severe performance degradation"
root-cause: "Synchronous CRM Acxiom member upsert blocks the transaction completion flow, consuming 60% of total processing time"
solution: "Offload the member upsert process to a separate async background service; add config flags to control sync vs async behavior"
jira: BE-1039
resolved: 2025-10-06
---

# BE-1039: Offloading the Upsert Process to a Separate Async Service

## 問題

The CRM Acxiom member upsert process runs synchronously during transaction completion, consuming approximately **6 seconds out of ~10 seconds** total processing time. This causes significant performance degradation for stores, especially CN Tapestry stores already experiencing API bottlenecks.

**Pros of async approach:** Member search operation will no longer depend on the upsert process
**Cons:** Caching version may not align with search results due to asynchronous updates

## 根因

The synchronous upsert design requires the transaction to wait for the CRM Acxiom API call to complete before the transaction can finish. Isolated debugging sessions confirmed that removing the upsert process can save **6 out of ~10 seconds** of processing time.

**Temporary solution** (V1.07.08+): Configuration to disable ACIXOM member upsert.

## 解法

**Solution**: Offload member upsert to a separate **async background service**.

**Architecture:**
- Sync-Member-Upsert → replaced with Async-Member-Upsert
- A background service handles the upsert queue
- Frontend transaction no longer waits for CRM API call

**Config settings** (`appsettings.json`):
```json
"AcxiomCRM_enableUpsert": "N"
"AcxiomCRM_asyncUpsertApiUrl": "https://{web server BEAPICRM URL}/api/v1/member/upsert"
"AcxiomCRM_bgUpsertInterval": "1000"
```

**Releases:**
- `v1.7.14_20250328` — Initial async service
- `v1.7.16_20250408` — Updated release

## 相關問題

- [[ACU-127]] — Original story reference
- [[FE-1654]] — Related member API config (FE side)
