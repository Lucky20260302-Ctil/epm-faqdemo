---
tags: [bug, production]
component: Front End
symptom: "Sales associate code 'aa' (lowercase) stored in V72 is not recognized — system expects uppercase 'AA'"
root-cause: "Legacy sales associate code stored in lowercase ('aa') in V72 database does not match the expected uppercase format ('AA') in V72 processing"
solution: "Data fix — corrected sales associate code from 'aa' to 'AA' in the database for J804-20242729"
jira: FE-1402
resolved: 2024-09-23
---

# FE-1402: Sales Associate Code Case Sensitivity — 'aa' vs 'AA'

## 問題

A discount variance incident (J804, 2024-05-31) was traced to a sales associate code mismatch. The sales associate code `'aa'` (lowercase) was stored in the database and could not be properly matched by the system.

**Incident data**: `\\172.16.183.201\localuser\support\^^DiscountVariance_2024\20240601_JP_J804-20242729_AA.zip`

**Reproduce steps:**
1. Issue three items
2. Select sales associate for item 3 as "aa"
3. Issue memo
4. "aa" is marked in V72 but not recognized by the processing system

## 根因

The sales associate code `'aa'` was stored in lowercase in the V72 database. The V72 processing expects the sales associate code in uppercase format `'AA'`. This case sensitivity mismatch causes the system to not recognize the sales associate assignment, resulting in discount variance.

## 解法

Data fix — corrected `'aa'` to `'AA'` in the database for transaction `J804-20242729`.

This is a **data-level fix** rather than a code change. For a permanent solution, the system should consider case-insensitive handling or input validation for sales associate codes.

**Fix Version**: `v750.04R02B`

## 相關問題

- [[FE-1403]] — Related discount variance issue (J431) with thread safety fix
