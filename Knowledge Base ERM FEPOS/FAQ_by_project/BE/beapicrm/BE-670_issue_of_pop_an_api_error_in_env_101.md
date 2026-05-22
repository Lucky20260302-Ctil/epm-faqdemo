---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Env: [https://172.16.138.101/chainstoreplus/home](https://172.16.138.101/chainstoreplus/home)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-670
resolved: 2023-03-03
fix-version: ""
---

# BE-670: Issue of Pop an API error in Env 101

## 問題

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
1. 
2. 
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
1. 
2. 
3. 
4. 
5. 
6. 
–
~~API Error [Request ID : 2022110809403166]~~
 ~~Index was outside the bounds of the array.  (Ref: Case 5.png)~~
Case6:
~~Location:  POS On-Line Sales Information (SE6005)~~
~~Reproduce steps:~~
1. 
~~API Error [Request ID : 2022110814420148]~~
~~Incorrect syntax near the keyword 'UNION'. (Ref: Case 6.png)~~
~~Case7:~~
~~Location: User Group Information (GL0006)~~
~~Reporduce steps:~~
1. 
2. 
3. 
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

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-03-03
### Jira Comments (2 則)
**Thomas** (2023-02-17):
Program GL0006 fixed in our development environment, need to check after program updated
**Sherman tse** (2023-03-03):
Verified on 172.16.138.55
Close case

## 相關資訊

- Jira: [BE-670](https://ctil.atlassian.net/browse/BE-670)
- Fix Version: 未記錄
- 解決日期: 2023-03-03
