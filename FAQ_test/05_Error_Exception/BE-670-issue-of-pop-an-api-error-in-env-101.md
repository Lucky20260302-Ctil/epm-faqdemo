---
project: BE
issue_key: BE-670
issue_type: Bug QA
status: Closed
faq_score: 10.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-670"
created: 2022-11-04
resolved: 2023-03-03
resolution: Done
has_images: False
---

# BE-670: Issue of Pop an API error in Env 101

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 10.0
> **解決日期:** 2023-03-03
> **負責人:** Sherman tse
> **組件:** Backend (Web)

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/home](https://172.16.138.101/chainstoreplus/home)

~~ACC: P01  PW:P01~~

Case 1:

~~Location: Data Interface > POS Oriented Polling Control (IC8002)~~

~~API error: API Error [Request ID : 2022110411325154]~~

~~API Error [Request ID : 2022110411325154] (Ref: Case-1.png)~~

 

Case 2: 

~~Location: Administration > POS Data Posting Process > POS Data Posting Control (IC8004)~~

~~API Error [Request ID : 2022110409592836]~~
~~Invalid object name 'status'.    (Ref: Case-2.png)~~

 

Case3: 

~~Location: Location Item Information (SE1004)~~

~~Reproduce steps:~~

1. ~~Click into one of the records in Location Item Information (SE1004)~~

2. ~~Select one of the items, then pop an api error~~

~~API Error: API Error [Request ID : 2022110416482915]~~

~~API Error [Request ID : 2022110416482915]  (Ref: Case 3.png)~~

 

Case 4:

~~Location: Stock on hand > Stock on hand by item(se1001)~~

~~Reproduce steps:~~

~~1. Click into one of the records in Stock on hand by item(se1001)~~

~~2. Select quantuty status inquiry~~
 –  
~~API Error [Request ID : 2022110714032257]~~
 –  
~~Conversion from type 'DBNull' to type 'String' is not valid.  (Ref: Case 4.1.png)~~
 

 Case5:

~~Location: Membership Management Information (MF3005)~~

~~Reproduce steps:~~

1. ~~To Membership Management Information~~

2. ~~Click Create~~

3. ~~To primiay > Click Accessible~~

4. ~~Select some Location~~

5. ~~Click "X" & select Save~~

6. ~~Click "Yes"~~

 – 

~~API Error [Request ID : 2022110809403166]~~
 ~~Index was outside the bounds of the array.  (Ref: Case 5.png)~~

 

Case6:

~~Location:  POS On-Line Sales Information (SE6005)~~

~~Reproduce steps:~~

1. ~~To POS On-Line Sales Information (SE6005) > Click one of the records~~

~~API Error [Request ID : 2022110814420148]~~

~~Incorrect syntax near the keyword 'UNION'. (Ref: Case 6.png)~~

 

~~Case7:~~

~~Location: User Group Information (GL0006)~~

~~Reporduce steps:~~

1. ~~To User Group Information (GL0006)~~

2. ~~Click Create & insert user group & description~~

3. ~~Click Save~~

~~Pop API Error [Request ID : 2022110910523453]~~
~~Invalid object name 'dbusergrph'. (Ref: Case7.png)~~

 

Case8: 

~~Location: On Sale Price Maintenance (On-Line Mode) (MF3001) (Page mode) (MF2003)/ (On-Line Mode) (MF3001)/~~

~~Reproduce steps:~~

~~1. To On Sale Price Maintenance~~

~~2. Click "Create'~~

~~3. Click on "Save"~~
 –  
~~API Error [Request ID : 2022110917141045]~~
~~Object reference not set to an instance of an object. (Ref: Case8.png)~~

 

Case 9:

~~Location:  Process > Stock receive inforamtion (rc1000) / Stock transfer batch information(TF6000)~~

~~API Error [Request ID : 2022111117212907]~~

~~Value cannot be null. (Parameter 'array')~~



## 相關資訊

- **Jira:** [BE-670](https://ctil.atlassian.net/browse/BE-670)
- **解決方式:** Done