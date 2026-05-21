---
tags: [bug, production]
component: MPOS
symptom: "MPOS cannot be installed on iOS 15 devices — deployment machine macOS Catalina with Xcode 12 doesn't support iOS 15 code signing"
root-cause: "macOS Catalina (Xcode 12) does not support code signing for iOS 15 apps; Apple requires Xcode 13+ for iOS 15 deployment"
solution: "Upgrade deployment machine to macOS Big Sur with Xcode 13 and re-compile MPOS for iOS 15 support"
jira: MP-507
resolved: 2021-12-08
---

# MP-507: MPOS Fails Installation on iOS 15 — Xcode Code Signing

## 問題

After upgrading to iOS 15, MPOS cannot be installed on devices. The deployment/build pipeline fails because the development machine cannot produce code-signed binaries compatible with iOS 15.

## 根因

The deployment machine was running **macOS Catalina** with **Xcode 12**, which does not support code signing for iOS 15 apps. Apple requires **Xcode 13+** (running on macOS Big Sur or later) to generate apps compatible with iOS 15's updated code signing requirements.

Reference: [Apple Developer — Xcode Support](https://developer.apple.com/support/xcode/)

## 解法

1. Upgraded the deployment machine from **macOS Catalina** to **macOS Big Sur**
2. Upgraded **Xcode from 12 to 13**
3. Re-compiled MPOS with the new toolchain
4. The new build successfully installs on iOS 15 devices

**Fix Version**: `3.13.2`

## 相關問題

- [[MP-508-mpos-crash-ios15-flutter-upgrade|MP-508]] — Related iOS 15 crash issue (Flutter compatibility)
