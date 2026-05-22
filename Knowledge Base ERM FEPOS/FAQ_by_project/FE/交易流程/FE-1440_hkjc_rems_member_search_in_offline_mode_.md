---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "In offline mode, the resulting exception message will be displayed when inputting QR code to search "
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1440
resolved: 2024-07-09
fix-version: ""
---

# FE-1440: [HKJC] REMS - Member search in offline mode will result in execption

## 問題

In offline mode, the resulting exception message will be displayed when inputting QR code to search for a member:
to clarify, “offline mode” is this:
TBLCONFIG.ENABLEDASEC = 'N'
TBLCONFIG.ENABLEDASECROLE = 'N'
network is disabled

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-07-09
### Jira Comments (8 則)
**Sang** (2024-07-01):
**Sang** (2024-07-01):
'v750.01R02H
1.
**Andy Ko** (2024-07-02):
@sang after testing, we found that the search will stop after submitting the QR code. No error messages, no search results. Please see the video for details. also included the logs for details.
**Sang** (2024-07-02):
**Sang** (2024-07-02):
**Sang** (2024-07-03):
**Sang** (2024-07-03):
**Sang** (2024-07-03):
'v750.01R02J
1. 
2.

## 相關資訊

- Jira: [FE-1440](https://ctil.atlassian.net/browse/FE-1440)
- Fix Version: 未記錄
- 解決日期: 2024-07-09
