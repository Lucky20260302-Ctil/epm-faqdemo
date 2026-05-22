---
project: FE
title: "FE-1895: DTUTIL - Add a configuration to get the POS_API URL from DTUTIL.INI"
issue_key: FE-1895
issue_type: Improvement
status: Selected for Development (migrated)
faq_score: 7.5
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, fe, install_deploy, dtutil]
jira_url: "https://ctil.atlassian.net/browse/FE-1895"
created: 2026-03-04
resolved: 
resolution: 
has_images: False
---

# FE-1895: DTUTIL - Add a configuration to get the POS_API URL from DTUTIL.INI

## 問題描述

Since the current DTUTIL logic reads the POS_API URL from tblConfig within dbtrans.sdf. However, we now provide an independent DTUTIL setup package for Windows 11, which is no longer bound to the POS installation. Because of this separation, I’m unable to update the xconfig file into *dbtrans.sdf* on these machines.

To support the new deployment approach, could you please help modify the DTUTIL program so that it reads the **POS_API URL** and related configuration directly from **DTUTIL.ini**, instead of relying on **dbtrans.sdf**?

This change will ensure the new DTUTIL package can be deployed smoothly without tying it to the POS environment.

 



## 相關資訊

- **Jira:** [FE-1895](https://ctil.atlassian.net/browse/FE-1895)