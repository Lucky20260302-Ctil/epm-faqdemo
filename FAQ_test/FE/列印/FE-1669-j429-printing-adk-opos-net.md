---
tags: [faq, FE, bug, upgrade]
component: "Printing"
symptom: "After upgrading to v75.004.1100.0008, J429 store printer settings are lost. Printers previously configured with ADK need to be migrated to OPOS.net."
root-cause: "The upgrade process does not migrate ADK printer configuration to OPOS.net. The ModelName field required by OPOS.net is missing from the migrated configuration, causing printer detection failure."
solution: "Manually re-configure printer settings in OPOS.net after upgrade. Ensure ModelName is set correctly. Fix in v75.004.1100.0008+."
jira: FE-1669
resolved: 2026-05-05
fix-version: "v75.004.1100.0008+"
---

# FE-1669: J429 Printing Issue After Upgrade — ADK to OPOS.net Printer Config Missing ModelName

## 問題

After upgrading to v75.004.1100.0008, J429 store printer settings are lost. Printers previously configured with ADK need to be migrated to OPOS.net.

## 根因

The upgrade process does not migrate ADK printer configuration to OPOS.net. The ModelName field required by OPOS.net is missing from the migrated configuration, causing printer detection failure.

## 解法

Manually re-configure printer settings in OPOS.net after upgrade. Ensure ModelName is set correctly. Fix in v75.004.1100.0008+.

## 相關資訊

- Jira: [FE-1669](https://ctil.atlassian.net/browse/FE-1669)
- Fix Version: v75.004.1100.0008+
- 解決日期: 2026-05-05
