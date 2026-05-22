---
project: MP
issue_key: MP-791
issue_type: Task
status: Closed
tags:
- 01_install_deploy
- faq
- install_deploy
- mp
- mpos-api
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-791
created: '2025-08-13'
resolved: '2025-08-13'
fix_version: ''
components: []
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'MP-791: MPOS-113: Request set eReceipt function as disabled for JP MPOS config'
---
# MP-791: MPOS-113: Request set eReceipt function as disabled for JP MPOS config

## 問題描述

Hi [Joy Li](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Joy_Li) (CC:[CY Lau](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Lau_Ching_Yeung%40ctil.com) [^cs2kapipatch_v3.0030.0301.zip][Shie Saito](https://jira.tapestry.support/secure/ViewProfile.jspa?name=ssaito%40tapestry.com)) kindly set the eReceipt disabled as default in MPOS config file for **JP region**, and add below store as eReceipt Enabled.

J101
J111
J207
J507
J805
J868

After reset the config file. kindly also update it in attached Local IIS package. Thanks

Kindly find Local IIS package with link:

[cs2kapipatch_v3.0030.0301.zip](https://ourtapestry-my.sharepoint.com/:u:/g/personal/nliu2_tapestry_com/EUFeCW9pxQFDtqTYbMyFq-oBLIcT87uXsCiPY8QGdVmE_A?e=Gewxmu)



## 相關資訊

- **Jira:** [MP-791](https://ctil.atlassian.net/browse/MP-791)
- **解決方式:** Done