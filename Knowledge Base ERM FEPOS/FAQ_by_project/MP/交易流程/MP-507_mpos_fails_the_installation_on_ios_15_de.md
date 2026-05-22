---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "After upgrade to iOS 15, MPOS is prevented to install because the deploy machine was running macOS C"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-507
resolved: 2021-12-08
fix-version: ""
---

# MP-507: MPOS Fails the Installation on iOS 15 Devices

## 問題

After upgrade to iOS 15, MPOS is prevented to install because the deploy machine was running macOS Catalina (with Xcode 12), which doesn't support code signing for iOS 15.
Solution: we have upgraded our machine to macOS Big Sur (with Xcode 13) and re-compiled MPOS in order to install it on iOS 15 device successfully.
More details:
[https://developer.apple.com/support/xcode/](https://developer.apple.com/support/xcode/)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2021-12-08

## 相關資訊

- Jira: [MP-507](https://ctil.atlassian.net/browse/MP-507)
- Fix Version: 未記錄
- 解決日期: 2021-12-08
