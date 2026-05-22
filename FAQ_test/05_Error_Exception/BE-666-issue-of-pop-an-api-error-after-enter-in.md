---
project: BE
title: "BE-666: Issue of Pop an API error after enter into some Tabs"
issue_key: BE-666
issue_type: Bug QA
status: Closed
faq_score: 9.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-666"
created: 2022-11-03
resolved: 2023-02-15
resolution: Done
has_images: False
---

# BE-666: Issue of Pop an API error after enter into some Tabs

## 問題描述

Env: [https://172.16.138.55/ChainStorePlus_AIGLE/home](https://172.16.138.55/ChainStorePlus_AIGLE/home)

Case 1:

~~Location: Administration > POS Data Posting Process > POS Data Posting Control (IC8004)~~

~~API error: API Error [Request ID : 2022110309462817]~~

~~Invalid object name 'status'. (Ref: Case-1.png)~~

~~Update(04/11):~~

~~*Issue also occurs in env: ~~~~[https://172.16.138.101/chainstoreplus/home](https://172.16.138.101/chainstoreplus/home)~~
 
API Error [Request ID : 2022110409592836]
Invalid object name 'status'.
 
~~Case 2:~~

~~Location: Stock Receive Confirmation Process  RC1000 > select Modify Receive > Click Item information~~

~~API error: API Error [Request ID : 2022110312121796]~~

~~object reference not to an instance an object (Ref: Case 2.png)~~

~~Case 3:~~

~~Location: Stock Receive Confirmation Process  RC1000 > select Batch Validation > Click OK~~

~~API error: Incorrect syntax near 'A' (Ref: Case 3.png)~~

~~Case 4:~~

~~Location: Stock Receive Confirmation Process  RC1000 > select Batch Posting > Click OK~~

~~API error: Error : Incorrect syntax near 'A' (Ref: Case 4. png)~~

 ~~Case 5:~~ 

~~Location: Process > Stock Controls > Physical Count Process IC0005 > Click  Batch Validation >  Click OK~~

~~API error:~~ 
~~Http failure response for ~~~~[https://172.16.138.55/CSBN_API_AIGLE/api/checkAsyncTaskStat2/T2022110313142806:](https://172.16.138.55/CSBN_API_AIGLE/api/checkAsyncTaskStat2/T2022110313142806:)~~~~ 404 OK  (Ref: Case 5. png)~~

 
 



## 相關資訊

- **Jira:** [BE-666](https://ctil.atlassian.net/browse/BE-666)
- **解決方式:** Done