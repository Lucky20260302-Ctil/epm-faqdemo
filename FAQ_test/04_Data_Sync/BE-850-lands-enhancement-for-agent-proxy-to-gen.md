---
project: BE
issue_key: BE-850
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, backend-(v66)]
jira_url: "https://ctil.atlassian.net/browse/BE-850"
created: 2024-05-03
resolved: 2024-05-03
resolution: Done
has_images: False
---

# BE-850: [Lands] Enhancement for Agent proxy to generate CSR image for work ledger

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 7.0
> **解決日期:** 2024-05-03
> **負責人:** Sherman tse
> **組件:** Backend (V66)

## 問題描述

[Lands] Enhancement for Agent proxy to generate CSR image for work ledger

Expected result:

- issued shopping cart order with CS, LIP & AOI items 

- Correct itemNum for Agent proxy

- Acom side can get correct details of our paid shop cart orders 

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




## Jira Comments

> **Sherman tse** (2024-05-03):
> Verified on UAT & deployed to Production

## 相關資訊

- **Jira:** [BE-850](https://ctil.atlassian.net/browse/BE-850)
- **解決方式:** Done