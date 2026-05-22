---
tags: [faq, mp, 交易流程]
component: "MPOSPrint.exe"
symptom: "we got callout from J317 & J328 which did v3.29.5 MPOS Pilot, have printing issue ~~on~~ since Apr-5"
root-cause: "待提取"
solution: "### Jira Comments (3 則)"
jira: MP-772
resolved: 
fix-version: ""
---

# MP-772: [MPOS-90]MPOS 3.29.5 - JP Cloud IIS PRD store printing issue

## 問題

we got callout from J317 & J328 which did v3.29.5 MPOS Pilot, have printing issue ~~on~~ since Apr-5th, kindly help to further check. thanks

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (3 則)
**Cy Lau** (2025-05-21):
**Cy Lau** (2025-05-26):
Owing to the uncertain network, MPOSPrint enhanced with HeartBeat to handle reconnecting beside the native mechanism from websocket message.
\\ds411\share\POS_FE_Release_64\20250526 Coach v750.04 MPOSPrint
WIth TBLConfig
'CY 250526
'HealthCheck of the connection:
Integer.TryParse(posShop.ThisTill.GetConfigValue("<span style="color:#ff991f">**MPOSPrintHeatBeat**</span>", "30000"), heartbeatInterval)
Integer.TryParse(posShop.ThisTill.GetConfigValue("<span style="color:#ff991f">**MPOSPrintHeatBeatRetryCnt**</span>", "3"), maxRetries)
**Andrew_Au** (2025-06-05):
@@Sherman tse Please update the ticket status

## 相關資訊

- Jira: [MP-772](https://ctil.atlassian.net/browse/MP-772)
- Fix Version: 未記錄
- 解決日期: 未記錄
