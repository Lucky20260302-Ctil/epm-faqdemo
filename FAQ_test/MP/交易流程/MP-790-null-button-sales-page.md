---
tags: [faq, MP, bug, ios]
component: "MPOS"
symptom: "A white, non-responsive button appears on MPOS sales screen after the app sits idle on item select screen. Blocks navigation until app is force-killed. Occurs on iOS 18.6."
root-cause: "iOS session-related UI rendering issue in Flutter v3.30.3. After idle timeout on item select screen, a floating null button renders and persists in the UI layer."
solution: "Fixed in MPOS IPA 3.30.3-20250801.1 and 3.29.6-20250801.1."
jira: MP-790
resolved: 2025-08-20
fix-version: "3.30.3-20250801.1"
---

# MP-790: CJ MPOS: White/Null Button Appears on Sales Page After Idle (iOS 18.6)

## 問題

A white, non-responsive button appears on MPOS sales screen after the app sits idle on item select screen. Blocks navigation until app is force-killed. Occurs on iOS 18.6.

## 根因

iOS session-related UI rendering issue in Flutter v3.30.3. After idle timeout on item select screen, a floating null button renders and persists in the UI layer.

## 解法

Fixed in MPOS IPA 3.30.3-20250801.1 and 3.29.6-20250801.1.

## 相關資訊

- Jira: [MP-790](https://ctil.atlassian.net/browse/MP-790)
- Fix Version: 3.30.3-20250801.1
- 解決日期: 2025-08-20
