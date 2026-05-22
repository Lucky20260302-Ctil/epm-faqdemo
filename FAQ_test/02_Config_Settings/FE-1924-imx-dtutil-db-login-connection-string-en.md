---
project: FE
title: "FE-1924: IMX Dtutil DB login connection string enhance"
issue_key: FE-1924
issue_type: Task
status: Closed
faq_score: 4.0
faq_category: 02_Config_Settings
faq_category_label: 設定與配置
tags: [faq, fe, config_settings, dtutil]
jira_url: "https://ctil.atlassian.net/browse/FE-1924"
created: 2026-04-13
resolved: 2026-04-16
resolution: Done
has_images: False
---

# FE-1924: IMX Dtutil DB login connection string enhance

## 問題描述

Enhance **VBRETAIL.ini for IMX** to allow the connection string to use `$CSUSER$` and `$PASSWORD$`, dynamically retrieving their values from the local `TBLSALADY` table where `SALADY_POSACC = 'DBLOGIN'`, instead of using hardcoded credentials.



## 相關資訊

- **Jira:** [FE-1924](https://ctil.atlassian.net/browse/FE-1924)
- **解決方式:** Done