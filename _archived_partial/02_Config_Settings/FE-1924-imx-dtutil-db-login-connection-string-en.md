---
project: FE
issue_key: FE-1924
issue_type: Task
status: Closed
tags:
- 02_config_settings
- config_settings
- dtutil
- faq
- fe
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1924
created: '2026-04-13'
resolved: '2026-04-16'
fix_version: ''
components: []
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: partial
title: 'FE-1924: IMX Dtutil DB login connection string enhance'
---
# FE-1924: IMX Dtutil DB login connection string enhance

## 問題描述

Enhance **VBRETAIL.ini for IMX** to allow the connection string to use `$CSUSER$` and `$PASSWORD$`, dynamically retrieving their values from the local `TBLSALADY` table where `SALADY_POSACC = 'DBLOGIN'`, instead of using hardcoded credentials.



## 相關資訊

- **Jira:** [FE-1924](https://ctil.atlassian.net/browse/FE-1924)
- **解決方式:** Done