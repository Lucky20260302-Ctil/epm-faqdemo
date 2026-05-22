---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Neil callout that create MPOS transaction for AU region but unable post to DB. Testing store: OCA213"
root-cause: "待提取"
solution: "### Jira Comments (1 則)"
jira: MP-805
resolved: 
fix-version: ""
---

# MP-805: [PPR-94]MPOS Transaction unable to post to DB

## 問題

Neil callout that create MPOS transaction for AU region but unable post to DB. Testing store: OCA213(IP: 10.34.103.17), transaction no: MA000001. kindly help to check
Troubleshooting:
1.From MPOS API log,We can see the memo MA000001 was created in 2025-12-19 15:51:09
2.And can find the memo in MPOS PC file
3.Upload PCD file：
2025/12/19 15:51:11.203 Create MSMQ to apawiqwposmqs21\PRIVATE$\Server20a
2025/12/19 15:51:11.219 Upload PCD file D:\www\apawiqwposweb24\SanyoService.API.FE_20\App_Data\Shops\oca213\Retdata6\UploadPCD\ACP2025121915511120.OCA213_M Successful
4.@@Cy Lau @@Daniel Leung But I can’t find the MPOS ACP file in polling posting log:
A. 2025-12-19 MQ log not have any MPOS data:
B. 2025-12-19 posting log not have any MPOS ACP file.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (1 則)
**Tovi Wang** (2025-12-22):
@@Daniel Leung @@Cy Lau  2025-12-19 ALL mpos log,Polling posting log here.Please help to further checking if anything other setting for MPOS?
CC @@Joy Li @@Bobby

## 相關資訊

- Jira: [MP-805](https://ctil.atlassian.net/browse/MP-805)
- Fix Version: 未記錄
- 解決日期: 未記錄
