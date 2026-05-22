---
tags: [change-request, production]
component: Backend
symptom: "CAR interface posting datetime uses Hong Kong server time instead of regional transaction datetime for Japan and Korea stores"
root-cause: "CAR interface file posting datetime is set to Backend server time (HKT), causing JP and KR transactions to appear 1 hour off their actual transaction time"
solution: "Put transaction date and time (jouinv_hour/jouinv_mn) into CAR interface posting date and time fields instead of server time; add dbconfig flag to control enable/disable per region"
jira: BE-1055
resolved: 2025-06-11
---

# BE-1055/BE-1051: CAR Interface Posting Datetime — Timezone Handling

## 問題

The CAR interface for transaction posting uses the Backend server datetime (Hong Kong Time, HKT) for posting date and time fields. This causes a **1-hour discrepancy** for stores in Japan and Korea, where the local transaction time is ahead of HKT.

The data datetime in CAR does not reflect the corresponding region's actual transaction time.

**Affected regions**: Coach Japan, Coach Korea, Kate Spade Japan

## 根因

Currently, when POS sends data to CAR, the posting datetime is populated using the **Backend server's system clock** (HKT). Since JP and KR are 1 hour ahead of HKT, transactions from these regions appear in CAR with incorrect timestamps.

The CAR interface file format uses a fixed datetime field that was not designed to accept per-transaction datetime values.

## 解法

**Solution**: Put the **transaction date and time** into the posting date and time fields inside the CAR interface file, replacing the server-time approach.

**Field mapping:**
- `hh` = `jouinv_hour`, `joudep_hour`, `jouser_hh`, `jougic_hour`
- `mm` = `jouinv_mn`, `joudep_mn`, `jouser_mn`, `jougic_min`
- `date` = `jouinv_date`, `joudep_date`, `jougic_date`

**Configuration**: Added `dbconfig` setting to enable/disable this change per region, allowing targeted application to Coach Japan, Coach KR, and Kate JP only.

**Release**: `BE-V70R3.102` / `\\ds411\csms60\delivery\coach\CAR.2024-04-24`

## 相關問題

- [[CS-1390]] — Coach Jira reference
- [[FE-1600]] — Related CAR interface fix (pipe character handling)
