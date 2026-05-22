---
project: FE
issue_key: FE-1433
issue_type: Bug QA
status: Closed
tags:
- 07_workflow_business
- faq
- fe
- front-end
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1433
created: '2024-06-26'
resolved: '2024-09-03'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1433: SQ0343-106 [MVP 1] The spending value did not update after using spending value to settle payment in REMS'
---
# FE-1433: SQ0343-106 [MVP 1] The spending value did not update after using spending value to settle payment in REMS

## 問題描述

Hi Andy,

 

As discussed, the burn action missing member account type and account number. Below is Deloitte provide information, please help fix and provide update later today. Thanks.

 

Please find the log file that we found when Sanyo send to us, we expecting accountType & accountNo should have value. While accountType should be "Wagering" ,accountNo should be the betting account number.

 

{"accountType":"","accountNo":"","txnNo":"SST1.00050046","txnDate":"0001-01-01 00:00:00.000","txnVenue":"Gift at Races ST shop 1","txnOutlet":"","txnDesc":"","txnType":"","totalAmount":0.0,"earnTxnAmount":68.6,"couponUsed":0.0,"burnDollars":1.0,"remarks":"0.0","handledBy":"QCTEST11","channel":"CPOS"}



## 相關資訊

- **Jira:** [FE-1433](https://ctil.atlassian.net/browse/FE-1433)
- **解決方式:** Done