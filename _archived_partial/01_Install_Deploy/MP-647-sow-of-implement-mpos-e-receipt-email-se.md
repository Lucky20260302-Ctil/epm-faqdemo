---
project: MP
issue_key: MP-647
issue_type: SOW
status: Closed
tags:
- 01_install_deploy
- faq
- install_deploy
- mp
- mpos
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-647
created: '2023-04-04'
resolved: '2023-06-12'
fix_version: ''
components: []
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'MP-647: SOW of Implement MPOS e-Receipt Email sending in Coach SG and MY'
---
# MP-647: SOW of Implement MPOS e-Receipt Email sending in Coach SG and MY

## 問題描述

1. . New tblconfig.eReceiptDisablePrint ='Y' (Default 'N') 'Y" - if select Send E-receipt, disable Print Hardcopy" (tblconfig)

2. . tblconfig.ENABLEERECEIPT='Y' (This setting can be ignored. It is for POS eRecipt only.)

3. . tblconfig.PolicyImageFileName ='' (Get from License DB)

4.  tblconfig.LOGO_FILENAME (Get from License DB)

5.  tblconfig.PRINTOUTFILESUBDIR  - Share Folder store e-receipt copy (can be ignored) 



## 相關資訊

- **Jira:** [MP-647](https://ctil.atlassian.net/browse/MP-647)
- **解決方式:** Done