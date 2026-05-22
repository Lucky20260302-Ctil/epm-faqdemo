---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "We're testing with MPOS IPA 'v3.29.5 0325.3', 'COACH_MPOSWebAPI_R3.29.5f' for HK region, when paid w"
root-cause: "待提取"
solution: "### Jira Comments (4 則)"
jira: MP-768
resolved: 
fix-version: ""
---

# MP-768: 【MPOS-92】MPOS 3.29.5e - HK Region, EFT function is unavailable

## 問題

We're testing with MPOS IPA "v3.29.5 0325.3", "COACH_MPOSWebAPI_R3.29.5f" for HK region, when paid with "EFT Wechat Online" payment, it will pop-up below error message, kindly help to check. Thanks
Testing machine IP: 10.33.254.14(OCQ10), HK region, with SalesHub enabled, connect to apabiqwposweb23, log already uploaded
1.Neil confirmed the issue was come from MPOS program, He paid with CS2K without any issues. Kindly help to further check, thanks
2.Checked API log found bellow errr:
2025-04-14 15:02:17.539 +08:00 [INF] PaymentsController.SendEFTAPIPaymentRequest?moduleId:0.Start()
2025-04-14 15:02:17.539 +08:00 [ERR] Index and length must refer to a location within the string.
Parameter name: length
2025-04-14 15:02:20.930 +08:00 [INF] PaymentsController.SendEFTAPIPaymentCancelRequest?moduleId:0.Start()
2025-04-14 15:02:21.000 +08:00 [INF] [Thread(96)] sendMessage:ReqeuestJobID:32c70702-OCQ10-MC;PrinterClient:ocq10
2025-04-14 15:02:21.023 +08:00 [INF] [Thread(21)] Message Sent
2025-04-14 15:02:21.026 +08:00 [INF] PaymentsController.SendEFTAPIPaymentCancelRequest?moduleId:0.Start()
2025-04-14 15:02:34.911 +08:00 [INF] PaymentsController.SendEFTAPIPaymentRequest?moduleId:0.Start()
2025-04-14 15:02:34.911 +08:00 [ERR] Index and length must refer to a location within the string.
Parameter name: length
2025-04-14 15:02:39.781 +08:00 [INF] PaymentsController.SendEFTAPIPaymentCancelRequest?moduleId:0.Start()
2025-04-14 15:02:39.842 +08:00 [ERR] The parameterized query '(@RequestJobId nvarchar(17),@Till nvarchar(2),@PayCode nvarchar(' expects the parameter '@PayRequestID', which was not supplied.
3.Checked MPOS UI log found bellow error:

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (4 則)
**Tovi Wang** (2025-04-22):
@@Daniel Leung @@Cy Lau
Details updated in description.bellow logs for your further checking.
**Daniel Leung** (2025-04-22):
@@Tovi Wang Please check [Dbhist].[dbo].[PaymentJob] and find the record where PayRequestID = 'cb66676a-OCQ10-MC', thank you
**Tovi Wang** (2025-04-22):
@@Daniel Leung I can find the PayRequestID from [Dbhist].[dbo].[PaymentJob],Follow details for your further checking.
.
PayRequestID:
|  |
| --- |
Req:
|  |
| --- |
Res:
|  |
| --- |
**Tovi Wang** (2025-04-23):
Confirmed issue was gone after we config the EFT payment for Till MC.

## 相關資訊

- Jira: [MP-768](https://ctil.atlassian.net/browse/MP-768)
- Fix Version: 未記錄
- 解決日期: 未記錄
