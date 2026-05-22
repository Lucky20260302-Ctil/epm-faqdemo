---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "FE user can receive a transfer when it was already received in BE."
root-cause: "待提取"
solution: "### Jira Comments (4 則)"
jira: FE-1656
resolved: 
fix-version: ""
---

# FE-1656: IMX refresh transfer receive record everytime when user enter the transfer receive page on FE

## 問題

FE user can receive a transfer when it was already received in BE.
@@Sang  Please help to add a config to control user can refresh the transfer status to avoid this issue.
**FE Record** – Received on 2025/03/03 at 17:29
Be Record – receive on 2025/03/03  15:50 by user 230324

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (4 則)
**Sang** (2025-03-31):
@@Jason Wu
Patch uploaded to \\ds411\share\POS_FE_Release\20250331 MX V710.02R14ZY Patch
'v710.02R14ZY
1.
**Andrew_Au** (2025-08-28):
@@Joy Li @@Sherman tse  Please arrange some test the bug fix. Still not release to IMX
**Andrew_Au** (2025-09-30):
@@Sherman tse
**Andrew_Au** (2025-10-03):
@@Sherman tse Please update status

## 相關資訊

- Jira: [FE-1656](https://ctil.atlassian.net/browse/FE-1656)
- Fix Version: 未記錄
- 解決日期: 未記錄
