---
project: WEB
issue_key: WEB-335
issue_type: Change Request
status: Closed
faq_score: 4.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, web, performance_timeout, beapi]
jira_url: "https://ctil.atlassian.net/browse/WEB-335"
created: 2023-08-22
resolved: 2024-05-16
resolution: Done
has_images: False
---

# WEB-335: change C360 getCustomerDetail call source code

> **類型:** Change Request | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 4.5
> **解決日期:** 2024-05-16
> **負責人:** Anson Cheung
> **組件:** BEAPI

## 問題描述

Modify the C360 API call getCustomerDetails, the “source” value to “SFCC” in GetCustomerRequest JSON object.

This is for KSJ only

As C360 Mercury project, C360 will generate NEAR real time GCID. so the Alternate ID search will not work for source code = 'KSCS2K', but it will work for source code='SFCC'

 

please change customer search API call getCustomerDetails, source code to 'SFCC' like below:
{
    "GetCustomerRequest": [
        {
            "brand": "KS",
            "source": "SFCC",
            "customerid": "11002000000573859",
            "addressId": "",
            "phoneId": "",
            "emailId": ""
        }
    ]
}
 



## 相關資訊

- **Jira:** [WEB-335](https://ctil.atlassian.net/browse/WEB-335)
- **解決方式:** Done