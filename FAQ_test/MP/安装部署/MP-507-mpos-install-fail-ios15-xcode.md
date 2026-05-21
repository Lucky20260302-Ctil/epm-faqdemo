---
tags: [faq, MP, bug, ios]
component: "MPOS"
symptom: "After upgrading devices to iOS 15, MPOS cannot be installed — deployment/installation fails entirely"
root-cause: "The deployment machine was running macOS Catalina with Xcode 12, which lacks code signing support for iOS 15. IPA cannot be signed for iOS 15 targets."
solution: "Upgraded deployment machine to macOS Big Sur with Xcode 13 and recompiled MPOS. Fixed in v3.13.2."
jira: MP-507
resolved: 2021-12-08
fix-version: "v3.13.2"
---

# MP-507: MPOS Fails to Install on iOS 15 Devices

## 問題

After upgrading devices to iOS 15, MPOS cannot be installed — deployment/installation fails entirely

## 根因

The deployment machine was running macOS Catalina with Xcode 12, which lacks code signing support for iOS 15. IPA cannot be signed for iOS 15 targets.

## 解法

Upgraded deployment machine to macOS Big Sur with Xcode 13 and recompiled MPOS. Fixed in v3.13.2.

## 相關資訊

- Jira: [MP-507](https://ctil.atlassian.net/browse/MP-507)
- Fix Version: v3.13.2
- 解決日期: 2021-12-08
