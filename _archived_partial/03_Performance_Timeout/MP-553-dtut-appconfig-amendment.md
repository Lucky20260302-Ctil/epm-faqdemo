---
project: MP
issue_key: MP-553
issue_type: Improvement
status: Closed
tags:
- 03_performance_timeout
- dtut-app
- faq
- mp
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-553
created: '2022-09-25'
resolved: '2024-05-27'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'MP-553: [DTUT] AppConfig Amendment'
---
# MP-553: [DTUT] AppConfig Amendment

## 問題描述

AFW{ 

   "Name":"default", // non editable 

   "Type":"DEV", // non editable 

   "Company":"COACH",// non editable 

   "EnableBarcodeValidation":true, // editable 

   "DefaultQtyInput":1, // editable 

   "EnableModuleStockTake":true, // editable 

   "EnableModuleStockTransfer":false,// editable 

   "EnableModuleActualReceive":false,//editable 

   "EnableModulePOSTransfer":false,// editable 

   "EnableModuleTransferACK":false,// editable 

   "ServerPath":"[https://172.16.138.42:7101/](https://172.16.138.42:7101/)",// editable 

   "ServerTimeout":60,// non editable 

   "EnableBin":true,// non editable 

   "EnableManualQtyInput":false,// editable 

   "pageSize":10000,// non editable 

   "WarnDuplicateScan":true,// non editable 

   "HouseKeepLogsDays":30// non editable 

} 

 

1) Please advise the red items usage

2) Change the Yellow items to be editable



## 相關資訊

- **Jira:** [MP-553](https://ctil.atlassian.net/browse/MP-553)
- **解決方式:** Done