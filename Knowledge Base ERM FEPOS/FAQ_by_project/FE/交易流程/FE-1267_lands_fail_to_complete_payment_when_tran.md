---
tags: [faq, fe, 交易流程]
component: "front end v760.02"
symptom: "Reproduce steps:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1267
resolved: 2023-08-08
fix-version: ""
---

# FE-1267: [Lands] Fail to complete payment when transaction paid by BlockVote & send E-receipt

## 問題

Reproduce steps:
1. 
2. 
3. 
4. 
5. 
Existing result:
1. 
2. 
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

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-08-08
### Jira Comments (1 則)
**Sherman tse** (2023-07-27):
Verified on .111 local desktop/ LANDS UAT, close case

## 相關資訊

- Jira: [FE-1267](https://ctil.atlassian.net/browse/FE-1267)
- Fix Version: 未記錄
- 解決日期: 2023-08-08
