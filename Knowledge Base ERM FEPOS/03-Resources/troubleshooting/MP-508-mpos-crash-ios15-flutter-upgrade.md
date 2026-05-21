---
tags: [bug, production]
component: MPOS
symptom: "MPOS crashes immediately after installation on iOS 15 devices"
root-cause: "Development environment uses Flutter 2.0.6 which is incompatible with iOS 15"
solution: "Upgrade Flutter development environment from 2.0.6 to 2.2.0 to restore iOS 15 compatibility"
jira: MP-508
resolved: 2021-12-08
---

# MP-508: MPOS Crashes Immediately on iOS 15 — Flutter Compatibility

## 問題

After installing MPOS on iOS 15 devices, the app crashes immediately upon launch. The app is non-functional on iOS 15 devices.

## 根因

The MPOS development environment was using **Flutter 2.0.6**, which is incompatible with **iOS 15**. Flutter 2.0.6 does not have the necessary iOS 15 runtime support, causing the app to crash on startup.

## 解法

Upgraded the development environment from **Flutter 2.0.6 to Flutter 2.2.0**, which includes proper support for iOS 15 runtime.

**Fix Version**: `3.13.2`

## 相關問題

- [[MP-507-mpos-install-fail-ios15-xcode-upgrade|MP-507]] — Related iOS 15 installation issue
