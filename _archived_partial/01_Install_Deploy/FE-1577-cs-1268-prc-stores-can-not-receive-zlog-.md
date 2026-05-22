---
project: FE
issue_key: FE-1577
issue_type: Bug PRD
status: Closed
tags:
- 01_install_deploy
- faq
- fe
- front-end
- install_deploy
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1577
created: '2024-12-06'
resolved: '2025-01-20'
fix_version: ''
components: []
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'FE-1577: [CS-1268] PRC stores can not receive zlog since Nov. 27th - RIN01424205)'
---
# FE-1577: [CS-1268] PRC stores can not receive zlog since Nov. 27th - RIN01424205)

## 問題描述

all PRC stores can not receive zlog files on Nov 27th by timeout.   HK & MC works well.

deployed OSS on BE on Nov.25 night, and the issue happened on Nov.27th and happened again on Dec.2nd.

Besides, PRC zlog files volumes are bigger than HK and MC, so please make sure if anything related with OSS deployment.



## 相關資訊

- **Jira:** [FE-1577](https://ctil.atlassian.net/browse/FE-1577)
- **解決方式:** Done