---
project: MP
issue_key: MP-768
issue_type: Bug PRD
status: Closed
faq_score: 8.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-768"
created: 2025-04-22
resolved: 
resolution: 
has_images: True
---

# MP-768: 【MPOS-92】MPOS 3.29.5e - HK Region, EFT function is unavailable

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 8.5
> **負責人:** Daniel Leung
> **組件:** MPOS

## 問題描述

We're testing with MPOS IPA "v3.29.5 0325.3", "COACH_MPOSWebAPI_R3.29.5f" for HK region, when paid with "EFT Wechat Online" payment, it will pop-up below error message, kindly help to check. Thanks

Testing machine IP: 10.33.254.14(OCQ10), HK region, with SalesHub enabled, connect to apabiqwposweb23, log already uploaded

> 📎 **image-20250422-040615.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/271459bd-3af7-42c5-ba61-0a53e7c68490)（需 Jira 登入）

1.Neil confirmed the issue was come from MPOS program, He paid with CS2K without any issues. Kindly help to further check, thanks

> 📎 **image-20250422-052009.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/5c60ea5b-3bd2-4ba6-8a52-85476ea58850)（需 Jira 登入）
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

> 📎 **image-20250422-053635.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a7bcdaf4-e455-4bf9-b840-5cdbd606faf8)（需 Jira 登入）
3.Checked MPOS UI log found bellow error:

> 📎 **image-20250422-053820.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e01fdc62-261d-400e-ab45-4a925be42b8f)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250422-040615.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/271459bd-3af7-42c5-ba61-0a53e7c68490)
2. 📎 **image-20250422-052009.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/5c60ea5b-3bd2-4ba6-8a52-85476ea58850)
3. 📎 **image-20250422-053635.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a7bcdaf4-e455-4bf9-b840-5cdbd606faf8)
4. 📎 **image-20250422-053820.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e01fdc62-261d-400e-ab45-4a925be42b8f)

## 相關資訊

- **Jira:** [MP-768](https://ctil.atlassian.net/browse/MP-768)