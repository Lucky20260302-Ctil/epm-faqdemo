---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Location: [https://172.16.138.55/ChainStorePlus_AIGLE/home](https://172.16.138.55/ChainStorePlus_AIG"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-725
resolved: 2023-03-02
fix-version: ""
---

# BE-725: Purchase Order would duplicate a set of same items after Item Receive more than 1 time

## 問題

Location: [https://172.16.138.55/ChainStorePlus_AIGLE/home](https://172.16.138.55/ChainStorePlus_AIGLE/home)
Reproduce steps:
**Create a Purchase Order**
1. 
2. 
*insert:
PO no.: 2023030203
Supplier: 1003032
Item: 00 1 20000007 Quantity: 10
Item: 00 1 20000006 Quantity: 10 Color: #1  Size: D
**Make a Stock Receive**
3. To Stock Receive Input Against PO/DRV (RC2000)
4. Find PO no. 2023030203 & tick it for Confirm
5. You are redirected to Stock Receive Confirmation Process (RC1000)
6. Receipt No. select a location e.g.: A007 灣仔
8. Click tab: Item information > With P.O.
9. Insert item for receive
Item: 00 1 20000007 Quantity: 1
Item: 00 1 20000006 Quantity: 1  Color: #1  Size: D
10. Click Validate & Save
**Confirm Stock Receive**
11. To Stock Receive Information (RC1000)
12. Double Click on the PO no. you just create (2023030203 > A007 - XXXXXX)
13. Select Batch Validation & Confirm OK
14. Select Batch Posting & Confirm OK
**Make a Stock Receive again**
15. To Stock Receive Information (RC1000)
16. Click Create
17. Receipt No. select a location e.g.: A008 西灣河
18. Click tab: Item information > With P.O.
19. Insert item for receive
Item: 00 1 20000007 Quantity: 2
Item: 00 1 20000006 Quantity: 2
20. Click Validate & Save
**Confirm Stock Receive again**
21. Repeat steps: 11-14
**Check items in Purchase Order**
22. To Purchase Order Information (PO3000)
23. Click on PO no.: 2023030203
24. To manage item
Existing result:
Purchase Order would duplicate a set of same items after Item Receive more than time
Remark:
- 
-

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-03-02
### Jira Comments (1 則)
**Sherman tse** (2023-03-02):
Verified on 172.16.138.55
Close Case

## 相關資訊

- Jira: [BE-725](https://ctil.atlassian.net/browse/BE-725)
- Fix Version: 未記錄
- 解決日期: 2023-03-02
