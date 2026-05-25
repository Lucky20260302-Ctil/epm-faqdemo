---
project: FEPOS
issue_key: FE-1713
issue_type: Bug PRD
status: Closed
tags:
- 01_install_deploy
- faq
- fepos
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1713
created: '2025-06-11'
resolved: '2025-07-11'
fix_version: FE-75.004.1303.0002
components:
- Front End
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: complete
title: 'FE-1713: Cash drawer can not be opened after upgrade to V75 - MC region'
---
# FE-1713: Cash drawer can not be opened after upgrade to V75 - MC region

## Problem

After upgrading to V75, all POS cash drawers cannot open due to cah.ini COM port setting being auto-changed from '1' to '7' during the upgrade process. This affected all upgraded POS tills in the MC region.

## Root Cause

During the V75 upgrade, the cah.ini configuration file was overwritten by two sources:
1. InstallationShield during major updates uses `Z:\Tapestry\COMMON\cah.ini` (default COM Port=7)
2. AdminUpdate.bat copies cah.ini from `Retdata6\inibak` backup folder
When the backup folder does not exist or has incorrect settings, the COM port defaults to 7.

## Solution

1. **Workaround:** Manually change the COM port in cah.ini back to the correct value (e.g., 1)
2. **Fix:** Released in **FE-75.004.1303.0002** — Enhanced AdminUpdate.bat logic to preserve existing cah.ini in CSPLUS folder when backup folder has no ini file, and restore from backup when available.

## Related Info

- **Jira:** [FE-1713](https://ctil.atlassian.net/browse/FE-1713)
- **Fix Version:** FE-75.004.1303.0002
- **Resolved:** 2025-07-11
- **Components:** Front End
- **Attachments:** [image-20250611-072631.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59389) | [image-20250611-072816.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59388) | [image-20250611-072936.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59386) | [image-20250611-073007.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59391) | [image-20250612-063415.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59454) | [image-20250612-095859.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59494) | [AdminUpdate.bat](https://ctil.atlassian.net/rest/api/3/attachment/content/59387) | [cah.ini.bak](https://ctil.atlassian.net/rest/api/3/attachment/content/59390)


## 相關截圖

![[../attachments/FE-1713/ac222b97-ef25-489b-b535-916a01f5fcdd.png]]

![[../attachments/FE-1713/image-20250611-072631.png]]

![[../attachments/FE-1713/image-20250611-072816.png]]

![[../attachments/FE-1713/image-20250611-072936.png]]

![[../attachments/FE-1713/image-20250611-073007.png]]

> 共 8 張截圖，[查看全部](../attachments/FE-1713/)
