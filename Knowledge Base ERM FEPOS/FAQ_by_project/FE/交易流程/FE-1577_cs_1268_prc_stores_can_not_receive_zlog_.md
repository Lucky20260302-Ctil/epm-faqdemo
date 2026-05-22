---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "all PRC stores can not receive zlog files on Nov 27th by timeout.   HK & MC works well."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1577
resolved: 2025-01-20
fix-version: ""
---

# FE-1577: [CS-1268] PRC stores can not receive zlog since Nov. 27th - RIN01424205)

## 問題

all PRC stores can not receive zlog files on Nov 27th by timeout.   HK & MC works well.
deployed OSS on BE on Nov.25 night, and the issue happened on Nov.27th and happened again on Dec.2nd.
Besides, PRC zlog files volumes are bigger than HK and MC, so please make sure if anything related with OSS deployment.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-01-20
### Jira Comments (7 則)
**Cy Lau** (2024-12-06):
CY 241206
Release of SanyoCloud v 1.2.0.7
\\ds411\share\CYLau\SanyoCloud\241206_1.2.0.7
Release Notes:
1. 
2.
**Cy Lau** (2024-12-06):
@@Joy Li  Please help to arrange for the testing
in case not enough time, putting negative value for OSS Upload Retry would disable the function and just give one shot testing on that
**Joy Li** (2024-12-10):
@@Joseph_Hu  Please update status
**Joy Li** (2024-12-10):
BE-V70R3.75 is released to COACH Team by @@Joy Li  on 2024-12-10.
@@Joseph_Hu  Please update Jira for testing result.
**Joseph_Hu** (2024-12-10):
It’s passed in our internal environment.
**Cy Lau** (2024-12-12):
From. TP QA :
**Joseph_Hu** (2025-01-20):
Closed

## 相關資訊

- Jira: [FE-1577](https://ctil.atlassian.net/browse/FE-1577)
- Fix Version: 未記錄
- 解決日期: 2025-01-20
