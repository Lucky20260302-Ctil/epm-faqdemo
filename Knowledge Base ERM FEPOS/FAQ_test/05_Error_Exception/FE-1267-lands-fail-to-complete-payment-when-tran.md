---
project: FE
issue_key: FE-1267
issue_type: Bug QA
status: Closed
faq_score: 8.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end-v760.02]
jira_url: "https://ctil.atlassian.net/browse/FE-1267"
created: 2023-06-16
resolved: 2023-08-08
resolution: Done
has_images: False
---

# FE-1267: [Lands] Fail to complete payment when transaction paid by BlockVote & send E-receipt

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 8.0
> **解決日期:** 2023-08-08
> **負責人:** Sang
> **組件:** front end v760.02

## 問題描述

Reproduce steps:

1. Create a transaction 

2. Apply GOV memebr with BV account (GOV00002)

3. Payment method select: BlockVote

4. Select send E-receipt & confirm

5. Pop up BV acc balance & confirm

Existing result:

1. Pop up an error: Your transaction has not been saved. Please try again later. & Click on OK

2. Stay at payment method page, fail to completed the payment

 

Remark:

VM: 172.16.138.111   /   P@ssw0rd@09

DAL log: 

2023/06/16 09:52:26.312 FillData.End PosShop
2023/06/16 09:52:26.313 PreparePayments.Start
2023/06/16 09:52:26.314 PreparePayments.End :
2023/06/16 09:52:26.976 [S] CreateInvoice 9999
Err: Object reference not set to an instance of an object.

 

T9 log:

[20230616 09:52:27 -0062]: CompleteTransaction.End()
[20230616 09:52:27 -0072]: Save Memo End:S.BF0.02300172 : Avail V. Memory : 140732097.294
[20230616 09:52:27 -0072]: Save Memo [02300172]: Faliure
[20230616 09:52:27 -0082]: Transaction is not completed!



## 相關資訊

- **Jira:** [FE-1267](https://ctil.atlassian.net/browse/FE-1267)
- **解決方式:** Done