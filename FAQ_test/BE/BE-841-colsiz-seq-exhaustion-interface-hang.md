---
tags: [faq, BE, bug, config]
component: "Backend / Data Import"
symptom: "The ITMEAN (Item Master) data import interface hangs because the color/size sequence (colsiz_seq) reached its maximum value of 999,999"
root-cause: "The colsiz_seq column in the database was configured with only 6 digits (max 999,999). Over years of operation, it exhausted its available sequence space."
solution: "Extended sequence to 8 digits (max 99,999,999) for Tapestry brand. Added max_colsiz_seq config parameter. Modified AS0003 and MF0001 to support extended range."
jira: BE-841
resolved: 2023-10-15
fix-version: ""
---

# BE-841: ITMEAN Interface Hangs — colsiz_seq Exhausted at 999,999

## 問題

The ITMEAN (Item Master) data import interface hangs because the color/size sequence (colsiz_seq) reached its maximum value of 999,999

## 根因

The colsiz_seq column in the database was configured with only 6 digits (max 999,999). Over years of operation, it exhausted its available sequence space.

## 解法

Extended sequence to 8 digits (max 99,999,999) for Tapestry brand. Added max_colsiz_seq config parameter. Modified AS0003 and MF0001 to support extended range.

## 相關資訊

- Jira: [BE-841](https://ctil.atlassian.net/browse/BE-841)
- Fix Version: 未記錄
- 解決日期: 2023-10-15
