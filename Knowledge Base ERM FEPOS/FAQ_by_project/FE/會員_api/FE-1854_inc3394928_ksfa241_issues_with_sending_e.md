---
tags: [faq, fe, 會員_api]
component: "interface"
symptom: "Symptom:"
root-cause: "待提取"
solution: "### Jira Comments (5 則)"
jira: FE-1854
resolved: 
fix-version: ""
---

# FE-1854: INC3394928 -KSFA241  Issues with sending email receipt to the customer 

## 問題

Symptom:
POS show error "send e-receipt fail, allow re-send later"
1.
查询log发现在 Call API: api/v1/cloud/ereceipt_v2 发送 20000044 e-receipt时，API response follow error,
只有这一张sales memo 的e-receipt 有这个error,后面重新发送成功。其它小票比如43，45 的e-receipt都可以正常发送。
@@Sang @@Cy Lau PLease help to check what’s mean of the error?what’s the RCA?How to avoid this error?Thanks!
CC @@Bobby @@Joy Li @@pierre.shi
2026/01/16 11:15:39.069 [20260116 11:15:39] Response:{"successful":false,"data":{"errorType":"Sanyo Error","errorCode":400,"errorMessage":"Error occurred when call eReceiptRestfulService API.","errorDetails":"No such host is known. (d:443)","errorDisplayMessage":"Error occurred when call eReceiptRestfulService API.","errorDesc":"Error occurred when call eReceiptRestfulService API.","message":"Error occurred when call eReceiptRestfulService API."}}
2026/01/16 11:15:39.074 [20260116 11:15:39] Send_eReceipt.Error: Error occurred when call eReceiptRestfulService API.
2.查询 ereceipt log没有发现20000044 的record,也没有error.有正常单20000045的record.
3.查询 ereceipt api log没有发现20000044 的record,也没有error.有正常单20000045的record.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (5 則)
**Tovi Wang** (2026-01-16):
@@Sangall log here.Please further checking.Thanks!
**Cy Lau** (2026-01-19):
@@Tovi Wang  Error by : 
No such host is known. (d:443)
d:443 ???
**Tovi Wang** (2026-01-19):
[FEPOS]->[LB]-><span style="color:#ff5630">[Webxx - BEAPI] / [Webyy-BEAPI]</span> ->eReceiptRestfulService
highlight as error coming from
**Tovi Wang** (2026-01-26):
Incorrect config setting in web sever.Issue gone after Coach support correct the config setting.
**Automation for Jira** (2026-01-26):
Issue has been created since
Days since: 9
Week since : 1
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1854](https://ctil.atlassian.net/browse/FE-1854)
- Fix Version: 未記錄
- 解決日期: 未記錄
