---
project: WEB
issue_key: WEB-200
issue_type: Bug PRD
status: Closed
faq_score: 9.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, web, error_exception, ename]
jira_url: "https://ctil.atlassian.net/browse/WEB-200"
created: 2021-07-12
resolved: 2021-07-12
resolution: Done
has_images: False
---

# WEB-200: Fix SG Birthday Verification error + disable CJ Loyalty

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 9.5
> **解決日期:** 2021-07-12
> **負責人:** Joy Li
> **組件:** eName

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