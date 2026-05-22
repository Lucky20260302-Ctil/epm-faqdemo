---
project: WEB
issue_key: WEB-200
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- ename
- error_exception
- faq
- web
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/WEB-200
created: '2021-07-12'
resolved: '2021-07-12'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'WEB-200: Fix SG Birthday Verification error + disable CJ Loyalty'
---
# WEB-200: Fix SG Birthday Verification error + disable CJ Loyalty

## 問題描述

ChainStorePlus WEB Server

- eName Program [17185/17188]

- Add config to disable the additional field from CJ Loyalty SOW

- No DB config change in this release (will NOT show if config = N or cannot found)

- Fix edit member (not created by ename interface) issue

- Since vip (NOT created by ename interface) do not have related record in ename table, therefore ename program will auto create a dummy record with vip information to record the ename_validate value.

- Fix “Next” button disable issue while input postal in CJ new customer creation.



## 相關資訊

- **Jira:** [WEB-200](https://ctil.atlassian.net/browse/WEB-200)
- **解決方式:** Done