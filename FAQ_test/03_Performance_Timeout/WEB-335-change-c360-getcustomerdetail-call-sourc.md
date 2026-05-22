---
project: WEB
issue_key: WEB-335
issue_type: Change Request
status: Closed
tags:
- 03_performance_timeout
- beapi
- faq
- performance_timeout
- web
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/WEB-335
created: '2023-08-22'
resolved: '2024-05-16'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'WEB-335: change C360 getCustomerDetail call source code'
---
# WEB-335: change C360 getCustomerDetail call source code

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