---
tags: [faq, BE, bug]
component: "BEAPI / CRM"
symptom: "CRM API returns correct vip_name (e.g., “Yoyo“) for a member, but the database stores “BEAPI“ in last_name and NULL in other name fields"
root-cause: "BEAPI was overwriting the CRM API response name field with its own internal value (“BEAPI“) instead of passing through the CRM-provided name."
solution: "Fixed in R3.80 release — BEAPI now correctly passes through CRM-provided name values."
jira: BE-944
resolved: 2024-11-14
fix-version: "R3.80"
---

# BE-944: BEAPI Overwrites CRM API Response Name Fields with Internal Default

## 問題

CRM API returns correct vip_name (e.g., "Yoyo") for a member, but the database stores "BEAPI" in last_name and NULL in other name fields

## 根因

BEAPI was overwriting the CRM API response name field with its own internal value ("BEAPI") instead of passing through the CRM-provided name.

## 解法

Fixed in R3.80 release — BEAPI now correctly passes through CRM-provided name values.

## 相關資訊

- Jira: [BE-944](https://ctil.atlassian.net/browse/BE-944)
- Fix Version: R3.80
- 解決日期: 2024-11-14
