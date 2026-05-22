---
project: FE
issue_key: FE-1669
issue_type: Improvement
status: Closed
tags:
- 01_install_deploy
- faq
- fe
- install_deploy
- install_package
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1669
created: '2025-04-11'
resolved: '2026-05-05'
fix_version: ''
components: []
has_images: true
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'FE-1669: [CS-1389]J429 printing issue after upgrade to v75.004.1100.0008'
---
# FE-1669: [CS-1389]J429 printing issue after upgrade to v75.004.1100.0008

## 問題描述

encountering printing issue after upgrade to v75.004.1100.0008.

Previous ADK saved Devices would be inherted to [OPOS.net](http://OPOS.net) 

> 📎 **image-20250411-035209.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/20882e40-b0c9-4be4-843b-ca5b3c5b6270)（需 Jira 登入）
### After checking record, ADK270JR4 should be given out on 25/12/2012 and ADK270ER5 on 25/11/2017 which would be UPOS 1.13.

### ADK280ER8, UPOS 1.14, should be given out since 26/11/2019.

### From 1.13 or previous , ModelName is not included in the configurations :

> 📎 **image-20250411-035254.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d55f29bc-1cd3-4d0d-8a72-7332dcbaf34e)（需 Jira 登入）

### Solutions : 

Using DeviceName for matching ModelName if ModelName does not exist,

The configurations from OPSON : 

> 📎 **image-20250411-035320.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3c9e6e7e-86d6-4cbc-a7e3-14a15b6f9df2)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250411-035209.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/20882e40-b0c9-4be4-843b-ca5b3c5b6270)
2. 📎 **image-20250411-035254.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d55f29bc-1cd3-4d0d-8a72-7332dcbaf34e)
3. 📎 **image-20250411-035320.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3c9e6e7e-86d6-4cbc-a7e3-14a15b6f9df2)

## 相關資訊

- **Jira:** [FE-1669](https://ctil.atlassian.net/browse/FE-1669)
- **解決方式:** Done