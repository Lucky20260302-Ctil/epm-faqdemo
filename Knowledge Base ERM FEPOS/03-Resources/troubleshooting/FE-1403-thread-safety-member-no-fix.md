---
tags: [bug, production, hotfix]
component: Front End
symptom: "Incorrect member number applied in J431 discount variance incident — fixed by data correction but underlying thread safety issue remains"
root-cause: "Thread safety issue in conditional check — if-condition not properly isolated for concurrent access, potentially allowing incorrect vip type (empty string) to be processed"
solution: "Separated the if-condition into a thread-safe block with exception throwing for edge cases; further investigation needed for viptype = '' scenario"
jira: FE-1403
resolved: 2024-09-08
---

# FE-1403: Thread Safety Issue in Member Number Assignment

## 問題

A discount variance incident (J431, 2024-06-01) was initially fixed by correcting the Member No. in the database (`J431-00024115`). However, subsequent investigation revealed the underlying code issue is a **thread safety problem** that can cause incorrect member data to be processed under concurrent access.

**Incident data**: `\\172.16.183.201\localuser\support\^^DiscountVariance_2024\20240531_JP_J431_00024115_IncorrectMember.zip`

The issue was identified as part of the V72 discount variance investigation series.

## 根因

The root cause is a **thread safety deficiency** in the member number assignment logic:

1. The if-condition check is not properly isolated for concurrent thread access
2. Under specific race conditions, a thread can pass the validation check but then operate on stale/wrong data
3. A related edge case where `viptype = ""` (empty string) exists and may be contributing to the incorrect assignment
4. When the invalid state is detected, the code throws an exception — but this should be caught earlier

The fix in `v750.04R04I` separates the if-condition into a thread-safe structure.

**Note**: More investigation is recommended about whether `viptype = ""` should exist as a valid state.

## 解法

**Fix in v750.04R04I:**
- Separated the if-condition logic to ensure thread safety
- Added proper exception throwing when invalid state is detected
- Isolated the conditional check so concurrent threads cannot interfere

**Remaining investigation needed:**
- Determine whether `viptype = ""` (empty string) is a valid state
- If not, add validation to prevent empty viptype from being processed

## 相關問題

- [[FE-1402-sales-associate-code-case-sensitivity|FE-1402]] — Related discount variance issue (J804)
