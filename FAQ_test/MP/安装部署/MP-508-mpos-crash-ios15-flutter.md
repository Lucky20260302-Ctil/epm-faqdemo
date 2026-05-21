---
tags: [faq, MP, bug, ios]
component: "MPOS"
symptom: "After installing MPOS on iOS 15 devices, the app crashes immediately on launch with no error message"
root-cause: "The MPOS development environment used Flutter 2.0.6, which is incompatible with iOS 15. The Flutter engine crashes on initialization under iOS 15."
solution: "Upgraded Flutter development environment to 2.2.0 and recompiled MPOS. Fixed in v3.13.2."
jira: MP-508
resolved: 2021-12-08
fix-version: "v3.13.2"
---

# MP-508: MPOS Crashes Immediately on iOS 15 Devices

## 問題

After installing MPOS on iOS 15 devices, the app crashes immediately on launch with no error message

## 根因

The MPOS development environment used Flutter 2.0.6, which is incompatible with iOS 15. The Flutter engine crashes on initialization under iOS 15.

## 解法

Upgraded Flutter development environment to 2.2.0 and recompiled MPOS. Fixed in v3.13.2.

## 相關資訊

- Jira: [MP-508](https://ctil.atlassian.net/browse/MP-508)
- Fix Version: v3.13.2
- 解決日期: 2021-12-08
