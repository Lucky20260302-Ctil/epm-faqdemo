---
tags: [bug, production, improvement]
component: Install_Package
symptom: "J429 printer configuration lost after upgrading to v75.004.1100.0008 — old ADK device settings not inherited by OPOS.net"
root-cause: "Old ADK (UPOS 1.13 or earlier) does not include ModelName in printer configurations; OPOS.net requires ModelName for device matching"
solution: "Use DeviceName as fallback for ModelName matching when ModelName is missing in inherited ADK configurations"
jira: FE-1669
resolved: 2026-05-05
---

# FE-1669: J429 Printing Issue — ADK to OPOS.net Upgrade Device Config Loss

## 問題

After upgrading to v75.004.1100.0008, stores encountered printing issues. Previous ADK-saved printer devices were not inherited correctly by OPOS.net.

**Timeline of ADK versions:**
- `ADK270JR4` — issued 25/12/2012 (UPOS 1.13)
- `ADK270ER5` — issued 25/11/2017 (UPOS 1.13)
- `ADK280ER8` — issued 26/11/2019 (UPOS 1.14)

## 根因

The ADK versions **UPOS 1.13 and earlier** do not include `ModelName` in their printer configurations. When the system upgrades to OPOS.net (which uses `Configuration.xml`), it expects `ModelName` to match printer devices. Since the old ADK configurations lack this field, the printers are not recognized and the settings are lost.

**Tested scenario**: ADK270 (UPOS 1.13) with TM-T88IV printer — Configuration.xml failed to retrieve ModelName.

## 解法

**Solution**: When `ModelName` is missing in inherited ADK configurations, use **DeviceName** as the fallback for `ModelName` matching.

This allows OPOS.net to correctly identify and inherit printer settings from old ADK configurations even when `ModelName` was not stored.

## 相關問題

- [[CS-1389]] — Coach Jira reference
