---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Since April 26^th^ ,2021, Apple has released iOS 14.5, which removed the limit Ad Tracking feature b"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-509
resolved: 2021-12-08
fix-version: ""
---

# MP-509: MPOS Fails to Retrieve Device ID after iOS 14.5

## 問題

Since April 26^th^ ,2021, Apple has released iOS 14.5, which removed the limit Ad Tracking feature but included a new feature - App Tracking Transparency. App Tracking Transparency provides similar functionality as limit Ad Tracking does, but it has “Allow Apps to Request to Track” setting instead of the old “limit Ad Tracking” setting. The major difference between the “limit Ad Tracking” setting and the App Tracking Transparency feature is that even the users enable “Allow Apps to Request to Track” setting, apps have to ask the users to request the permission in order to retrieve IDFA. By disabling “Allow Apps to Request to Track” setting, it not only denies all apps to track and receive the IDFA from the users but also prevents all apps to bring it up to the users.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2021-12-08
### Jira Comments (1 則)
**Nathan Chan** (2021-10-18):
Added a checking point when registering the device or initialize MPOS.

## 相關資訊

- Jira: [MP-509](https://ctil.atlassian.net/browse/MP-509)
- Fix Version: 未記錄
- 解決日期: 2021-12-08
