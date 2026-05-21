---
tags: [faq, FE, bug, production]
component: "SQL Express / System"
symptom: "After V75 upgrade, stores frequently enter standalone mode with error 'not able to connect to main till, please change to standalone mode'. SQL Express service timeout causes heartbeat failure."
root-cause: "SQL Express has a default timeout that can be exceeded under load (large databases, slow hardware). When the heartbeat query times out, the system incorrectly assumes the main till is unavailable and switches to standalone mode."
solution: "Extended SQL Express heartbeat timeout and added retry logic. The heartbeat monitor now tolerates brief SQL Express delays before switching to standalone. Fix in FE-V75.04R13A."
jira: FE-1696
resolved: 2025-05-30
fix-version: "FE-V75.04R13A"
---

# FE-1696: SQL Express Timeout Causes Standalone Mode — Heartbeat Monitor Fix

## 問題

After V75 upgrade, stores frequently enter standalone mode with error 'not able to connect to main till, please change to standalone mode'. SQL Express service timeout causes heartbeat failure.

## 根因

SQL Express has a default timeout that can be exceeded under load (large databases, slow hardware). When the heartbeat query times out, the system incorrectly assumes the main till is unavailable and switches to standalone mode.

## 解法

Extended SQL Express heartbeat timeout and added retry logic. The heartbeat monitor now tolerates brief SQL Express delays before switching to standalone. Fix in FE-V75.04R13A.

## 相關資訊

- Jira: [FE-1696](https://ctil.atlassian.net/browse/FE-1696)
- Fix Version: FE-V75.04R13A
- 解決日期: 2025-05-30
