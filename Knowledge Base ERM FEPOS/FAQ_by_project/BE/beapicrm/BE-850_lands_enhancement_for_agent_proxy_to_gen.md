---
tags: [faq, be, beapicrm]
component: "Backend (V66)"
symptom: "[Lands] Enhancement for Agent proxy to generate CSR image for work ledger"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-850
resolved: 2024-05-03
fix-version: ""
---

# BE-850: [Lands] Enhancement for Agent proxy to generate CSR image for work ledger

## 問題

[Lands] Enhancement for Agent proxy to generate CSR image for work ledger
Expected result:
- 
- 
- 
"RequestDataFromHKMSAsync - payloadJsonStr":{
"user":"[salestaff_UAT@landsd.gov.hk](mailto:salestaff_UAT@landsd.gov.hk)",
"orderId":"LHQ-02400178",
"orderDate":"2024-01-16 18:08:57",
"dispatchMethod":"C",
"orderFolderPath":"",
"aoiList":[
{
"itemNum":"7",
"aoiFile":"af6e9045-413e-433f-9ac9-8113fe0286e6.png"
}
],
"lipList":[
{
"itemNum":"6",
"itemId":"LIPPO2",
"collectionOffice":"LHQ",
"lipNo":"LIP320193P"
}
],
"csrList":[
{
"itemNum":"1",
"itemId":"LBPLSOP",
"sheetNo":"LBP/DN/014/1176/D1"
},
{
"itemNum":"2",
"itemId":"SRPLSOP",
"sheetNo":"SRP/DN/007/0551/D1(R)"
},
{
"itemNum":"3",
"itemId":"SRPALS",
"sheetNo":"SRP/DN/047/2514/76/1492-S"
},
{
"itemNum":"4",
"itemId":"LBP",
"sheetNo":"LBP/YL/UL3073/D1_SHT1OF2"
},
{
"itemNum":"5",
"itemId":"SRP",
"sheetNo":"DN9061"
}
]
}

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-05-03
### Jira Comments (1 則)
**Sherman tse** (2024-05-03):
Verified on UAT & deployed to Production

## 相關資訊

- Jira: [BE-850](https://ctil.atlassian.net/browse/BE-850)
- Fix Version: 未記錄
- 解決日期: 2024-05-03
