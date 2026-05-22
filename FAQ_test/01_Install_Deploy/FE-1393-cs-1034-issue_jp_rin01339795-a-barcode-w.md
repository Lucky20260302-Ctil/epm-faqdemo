---
project: FE
issue_key: FE-1393
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
jira_url: https://ctil.atlassian.net/browse/FE-1393
created: '2024-05-17'
resolved: '2024-05-24'
fix_version: ''
components: []
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'FE-1393: [CS-1034] Issue_JP_RIN01339795 A barcode was splited up when printed out.'
---
# FE-1393: [CS-1034] Issue_JP_RIN01339795 A barcode was splited up when printed out.

## 問題描述

Barcode Print ini folder:

Background:

Need to AUTO copy ini from \CS2000POS\Layout folder before uninstall.

Suggestion:

1. prepare v72 adminUpdate.bat to copy all files in \CS2000POS\Layout to \Retdata6\layout folder. (create a new folder for layout)

2. Update v75 adminUpdate.bat to copy the ini files from \Retdata6\layout folder to \CSPLUS\layout folder.

3. Downgrade from V75 to V72 will restore the ini files from \Retdata6\layout folder to c:\cs2000pos\layout.



## 相關資訊

- **Jira:** [FE-1393](https://ctil.atlassian.net/browse/FE-1393)
- **解決方式:** Done