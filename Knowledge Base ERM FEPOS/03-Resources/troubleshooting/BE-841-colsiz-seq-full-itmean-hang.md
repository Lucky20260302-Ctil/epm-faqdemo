---
tags: [improvement, production]
component: Backend
symptom: "ITMEAN import data interface process hangs because colsiz_seq sequence is fully occupied"
root-cause: "The colsiz_seq auto-increment sequence reached its maximum value (99999), preventing creation of new color/size records and causing the ITMEAN interface to hang"
solution: "Add dbconfig max_colsiz_seq setting (default 99999, Tapestry set to 9999999) and modify programs that create colsiz records to respect the new limit"
jira: BE-841
resolved: 2024-05-24
---

# BE-841: Colsiz_seq Fully Occupied Causes ITMEAN Interface Hang

## 問題

Coach reported that the ITMEAN import data interface process hangs. Investigation found the root cause is that the `colsiz_seq` sequence (color/size sequence) has reached its maximum capacity.

**Workaround**: Delete unused color & size records to free up sequence space.

Tapestry requested a **long-term solution** to prevent recurrence.

## 根因

The `colsiz_seq` auto-increment sequence is configured with a maximum value of **99999** (5 digits). Over time, as new color and size combinations are created, the sequence exhausts all available values. When no more sequence numbers can be allocated, any program that needs to create a new color/size record fails, causing the ITMEAN interface to hang.

Since Tapestry does not use the ChainStorePlus barcode sequence, increasing the sequence limit should have no negative impact on their operations.

## 解法

**Solution**: Added a configuration setting `max_colsiz_seq` in the `dbconfig` table.

- **Default**: `99999` (existing behavior, unchanged)
- **Tapestry/Coach setting**: `9999999` (7 digits)

**Modified programs**: All programs that create `colsiz` records were updated:
- Standard Data Import Interface (AS0003)
- Other relevant size/color creation programs

**Note**: No formal release — the issue was handled via SQL update only.

## 相關問題

- [[BE-1012]] — Related data integrity issue (size category carry-forward)
