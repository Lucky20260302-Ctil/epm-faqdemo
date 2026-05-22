---
project: FE
issue_key: FE-1393
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, fe, install_deploy, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1393"
created: 2024-05-17
resolved: 2024-05-24
resolution: Done
has_images: False
---

# FE-1393: [CS-1034] Issue_JP_RIN01339795 A barcode was splited up when printed out.

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 安裝與部署 | **FAQ 分數:** 7.5
> **解決日期:** 2024-05-24
> **負責人:** Joy Li
> **組件:** Front End

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