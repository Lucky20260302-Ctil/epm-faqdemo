---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "When pay code is GIC in one transaction, the payment will be double."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1235
resolved: 2026-05-05
fix-version: ""
---

# BE-1235: [CS-1412] Issue_OC555 Landlord sales interface logic is wrong

## 問題

When pay code is GIC in one transaction, the payment will be double.
In bellow case.
Total 20 GIC in this transaction, each one is 50 and total should be 1000.
But system will send 20000 to Landlord.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-05-05
### Jira Comments (9 則)
**Tovi Wang** (2026-03-11):
@@Sang For this issue.When pay code = ‘GIC',We should send sum(joupay_vhr_amount)=1000 to CAR instead of sum(joupay_pay_amt_fx)=’20000'.Please help to correct the GIC paycode send landlord interface logic for all region。
CC @@Joy Li
**Automation for Jira** (2026-03-12):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2026-03-12):
@@Tovi Wang this is last year 2025-3-20 transaction.  Any problem in recent transaction interface file ?
**Tovi Wang** (2026-03-12):
@@Sang Yes,如果Paycode='GIC' 的话就会有这个issue.
如果paycode='GIC',就会sum(joupay_pay_amt_fx)=’20000' 发 interface.
实际应该发sum(joupay_vhr_amount)=1000 或者只发一个 joupay_pay_amt_fx=1000 给 interface.
请检查确认发interface 的逻辑并且优化 paycode='GIC' 时的发 interface.
**Sang** (2026-03-12):
@@Jerry Wong @@Cy Lau Please follow up.
**Cy Lau** (2026-03-12):
@@Tovi Wang  which LandLord is that ? CoachSG ? 
@@Joy Li
**Tovi Wang** (2026-03-12):
@@Cy Lau @@Jerry Wong Let me double confirm the interface exe and got the interface file to you.
**Jerry Wong** (2026-03-12):
# Release:
\\DS411\csms60\delivery\coach\VivoGTOSalesUpload_2026-03-12
# Notes:
if paycode is 'GIC' then SUM(joupay_vhr_amt), Otherwise sum(joupay_pay_amt_fx)
Source:
\\DS411\public\anson\Project.A\Sales Amount Uploader\VivoGTO File SubmissionReceipt Level (HQ QR)
# Testing config:
Data Source=172.16.138.8,40000;Initial Catalog=csdata10_70;User ID=csuser;Password=csuser
Date = 2019-11-28
jouinv_loc = 'J999'
jouinv_no = '00000559'
# Result:
Before changes:
8008008_20191128_172749_BEFORE_CHANGE.txt
After changes:
8008008_20191128_172928_AFTER_CHANGE.txt
**Sherman tse** (2026-03-19):
Verified ok on QA with below release
\\DS411\csms60\delivery\coach\VivoGTOSalesUpload_2026-03-12\VivoGTOSalesUpload_2026-03-19

## 相關資訊

- Jira: [BE-1235](https://ctil.atlassian.net/browse/BE-1235)
- Fix Version: 未記錄
- 解決日期: 2026-05-05
