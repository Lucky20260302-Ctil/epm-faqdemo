---
project: FE
issue_key: FE-1107
issue_type: SOW
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1107
created: '2022-04-04'
resolved: '2022-06-01'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1107: A920 - Octopus & PayMe'
---
# FE-1107: A920 - Octopus & PayMe

## 問題描述

3. A920 Otopus + Payme (Coach sow) (KTS 220331 v72.02R16B, v720.01R01A Jira FE-1107)

A. A920-Octoupus

a. ChangeType='0' [EPM], 900_TX_TRype='A920_OCTO'

b. No Support refund, Pop Up Message remain to refund manually  

B. A920-Payme 

a. ChangeType='0' [EPM], 900_TX_TRype='A920_PAYME' 

b. Void UI - Show PayINfo.Description 

c. Enter password in A920 (000000) 

d. Store Payme Txn Ref in Trace_no field, POS Receipt and A920 Receipt both show this reference 

e. Void Store Diff Trace No - Sales / Deposit / Gift Cert / Service  

f. Extend [Invtrx File Payment].[invtrx_Trace], [Payment File].[Pay_TRACE]  nchar*6-> 50, store Payme Refund  

g. Add tblconfig.A920PayMeTermID A920 payMe Terminal ID Ex.'99010011' 

h. Add tblconfig.A920PayMeStoreID A920 payMe Store ID Ex.'000017734410'  

i. A920 - Payment / Void Exception - Show Failure + A920 Response Message



## 相關資訊

- **Jira:** [FE-1107](https://ctil.atlassian.net/browse/FE-1107)
- **解決方式:** Done