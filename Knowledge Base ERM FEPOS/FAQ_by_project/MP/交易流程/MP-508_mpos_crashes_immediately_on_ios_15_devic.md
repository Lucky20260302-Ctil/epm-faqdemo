---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "After installing MPOS on iOS 15, it crashes immediately. During the investigation, we found out the "
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-508
resolved: 2021-12-08
fix-version: ""
---

# MP-508: MPOS Crashes Immediately on iOS 15 Device 

## 問題

After installing MPOS on iOS 15, it crashes immediately. During the investigation, we found out the current development environment is using Flutter 2.0.6, which might be the reason why it crashes on iOS 15.
Solution: we have upgraded the dev env to use Flutter 2.2.0 to make MPOS working on iOS 15.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2021-12-08

## 相關資訊

- Jira: [MP-508](https://ctil.atlassian.net/browse/MP-508)
- Fix Version: 未記錄
- 解決日期: 2021-12-08
