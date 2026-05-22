---
project: MP
issue_key: MP-509
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-509
created: '2021-10-08'
resolved: '2021-12-08'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-509: MPOS Fails to Retrieve Device ID after iOS 14.5'
---
# MP-509: MPOS Fails to Retrieve Device ID after iOS 14.5

## 問題描述

Since April 26^th^ ,2021, Apple has released iOS 14.5, which removed the limit Ad Tracking feature but included a new feature - App Tracking Transparency. App Tracking Transparency provides similar functionality as limit Ad Tracking does, but it has “Allow Apps to Request to Track” setting instead of the old “limit Ad Tracking” setting. The major difference between the “limit Ad Tracking” setting and the App Tracking Transparency feature is that even the users enable “Allow Apps to Request to Track” setting, apps have to ask the users to request the permission in order to retrieve IDFA. By disabling “Allow Apps to Request to Track” setting, it not only denies all apps to track and receive the IDFA from the users but also prevents all apps to bring it up to the users.



## 相關資訊

- **Jira:** [MP-509](https://ctil.atlassian.net/browse/MP-509)
- **解決方式:** Done