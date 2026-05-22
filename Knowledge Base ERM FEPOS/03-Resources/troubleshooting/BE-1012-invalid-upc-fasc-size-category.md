---
tags: [bug, production]
component: Backend
symptom: "HKJC_FASC.exe exported invalid size to FASC for item 1APKTS25KDM001 — wrong size category SML instead of KDS"
root-cause: "Item Master Maintenance carries forward previous item's size category; user created SML-size item first, then KDS-size item which incorrectly inherited SML sizes in edisku table"
solution: "Fix Item Master Maintenance to properly handle size category when creating items with different size types"
jira: BE-1012
resolved: 2025-03-21
---

# BE-1012: Invalid UPC Code to FASC — Wrong Size Category

## 問題

HKJC RTM reported that `HKJC_FASC.exe gen_link1_skumaster` interface sent an invalid size to FASC for item `1APKTS25KDM001 Mem Bdg K-Tee plain`.

The output file `HSRTM_ITEMMASTER` contained incorrect size information. The correct size category should be **"KDS"** but the file contained **"SML"** sizes.

## 根因

The investigation found the following sequence of events:

1. User created item `1APLTS25KDM002` which has size category **SML**
2. User then created item `1APKTS25DM001` which has size category **KDS**
3. The Item Master Maintenance system **carried forward** the SML sizes from the previous item into the `edisku` table for the new item
4. This caused the `HSRTM_ITEMMASTER` interface to export the wrong size to FASC

The root cause is that the Item Master Maintenance does not properly reset the size category data when creating a new item with a different size type from the previously created item.

## 解
Fix applied to **Item Master Maintenance** to properly handle size category initialization when creating items, ensuring that sizes from a previous item are not incorrectly carried forward to a new item with a different size category.

**Status**: Fix delivered to HKJC for testing; ticket closed.

## 相關問題

- [[BE-841]] — Related data integrity fix (colsiz_seq)
