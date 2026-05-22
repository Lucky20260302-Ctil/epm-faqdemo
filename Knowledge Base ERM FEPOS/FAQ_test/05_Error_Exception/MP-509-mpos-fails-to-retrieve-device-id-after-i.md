---
project: MP
issue_key: MP-509
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-509"
created: 2021-10-08
resolved: 2021-12-08
resolution: Done
has_images: False
---

# MP-509: MPOS Fails to Retrieve Device ID after iOS 14.5

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.0
> **解決日期:** 2021-12-08
> **負責人:** Nathan Chan
> **組件:** MPOS

## 問題描述

Since April 26^th^ ,2021, Apple has released iOS 14.5, which removed the limit Ad Tracking feature but included a new feature - App Tracking Transparency. App Tracking Transparency provides similar functionality as limit Ad Tracking does, but it has “Allow Apps to Request to Track” setting instead of the old “limit Ad Tracking” setting. The major difference between the “limit Ad Tracking” setting and the App Tracking Transparency feature is that even the users enable “Allow Apps to Request to Track” setting, apps have to ask the users to request the permission in order to retrieve IDFA. By disabling “Allow Apps to Request to Track” setting, it not only denies all apps to track and receive the IDFA from the users but also prevents all apps to bring it up to the users.



## 相關資訊

- **Jira:** [MP-509](https://ctil.atlassian.net/browse/MP-509)
- **解決方式:** Done