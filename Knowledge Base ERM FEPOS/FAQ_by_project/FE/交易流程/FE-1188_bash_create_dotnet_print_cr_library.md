---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "POS have created DotNetPrint TMU Layout for BASH Oct-2021. However, BASH finally decide to use Imagi"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1188
resolved: 2022-12-16
fix-version: ""
---

# FE-1188: BASH - Create DotNet Print CR Library

## 問題

POS have created DotNetPrint TMU Layout for BASH Oct-2021. However, BASH finally decide to use ImagineX CR layout, therefore, finally BASH configured ti use IMX CR layout.   We need to separate BASH CR layout from ImagineX, and customized CR layout for BASH.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-12-16
### Jira Comments (1 則)
**Sang** (2022-12-07):
Merge IMX CR To BASH (TMU) - (KTS 221206 v720.02R07ZB, v750.03 Jira [🔗](https://ctil.atlassian.net/browse/FE-1188#icft=FE-1188)) BASH DotNetPrint CR Setting : tblconfig.PrtCompany ='BASH'
+ BASH_Receipt.rpt,  BASH_AccSales.rpt, BASH_GiftCertificate.rpt + BASH_GiftReceipt.rpt, BASH_GiftRedeemReceipt.Rpt, BASH)REplenish.rpt, BASH_transferOut.rpt. BASH_TransferReceive.rpt

## 相關資訊

- Jira: [FE-1188](https://ctil.atlassian.net/browse/FE-1188)
- Fix Version: 未記錄
- 解決日期: 2022-12-16
