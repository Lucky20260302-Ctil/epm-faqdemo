---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Env: [https://172.16.138.55/ChainStorePlus_AIGLE/home](https://172.16.138.55/ChainStorePlus_AIGLE/ho"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-666
resolved: 2023-02-15
fix-version: ""
---

# BE-666: Issue of Pop an API error after enter into some Tabs

## 問題

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

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-02-15
### Jira Comments (2 則)
**Sherman tse** (2022-11-04):
Case1 Updated
**Thomas** (2023-02-15):
No error found in this environment, please try again

## 相關資訊

- Jira: [BE-666](https://ctil.atlassian.net/browse/BE-666)
- Fix Version: 未記錄
- 解決日期: 2023-02-15
