---
project: FE
issue_key: FE-1898
issue_type: Task
status: Test in Progress
tags:
- 01_install_deploy
- faq
- fe
- front-end
- install_deploy
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1898
created: '2026-03-10'
resolved: ''
fix_version: ''
components: []
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'FE-1898: [Coach] Dtutil testing'
---
# FE-1898: [Coach] Dtutil testing

## 問題描述

[Coach] Dtutil testing

Compontents:

POSDN & .ini & dtutil program

Dtutil POSDN

\\172.16.183.201\localuser\coach\POSPATCH\Dtutil2\

Dtutil program:

original program from IMX: WIN11, with 72 library

Testing VM:

172.16.138.51
.\sxd
Yan20201104@

---

DTUT Enable Upload Delivery Note setting:

 

Call AddLog(mLastLog, "Ver 8.3.34 (CS2000 v661.11R19) (2016-10-03, 161110 .Net Updated)", True)

    Call AddLog(mLastLog, "Support online Batch Upload TN & Print Transfer Note (DN)", True)

    Call AddLog(mLastLog, "1. Set DTUT.ini", True)

    Call AddLog(mLastLog, "  a. BatchUploadTransferFile=Y (Default 'N')")

    Call AddLog(mLastLog, "  b. CompanyCode ( use to Connect backend GL Data) ")

    Call AddLog(mLastLog, "  c. BackendGLData ( use to Connect backend GL Data - case sensitive")

    Call AddLog(mLastLog, "  d. BackendUser ( backend user - case sensitive to Post DN, must have access right of module 'TF6009'")

    Call AddLog(mLastLog, "2. Support CS2000 POS v662.11R17 +")

    Call AddLog(mLastLog, "3. Post DN Program Folder : \PostDN\")

    Call AddLog(mLastLog, "4. Request to install Barcode Font Free 3 of 9 Extended True Type front (FRE3OF9X)")

    Call AddLog(mLastLog, "5. Support Single PickNo Multi DN (Must Enable Bin Header)")

    Call AddLog(mLastLog, "6. For Coach SIngleBatchPerPickNo Operation, One Batch/Pick - One fr-To Location Only (161110 updated)")



## 相關資訊

- **Jira:** [FE-1898](https://ctil.atlassian.net/browse/FE-1898)