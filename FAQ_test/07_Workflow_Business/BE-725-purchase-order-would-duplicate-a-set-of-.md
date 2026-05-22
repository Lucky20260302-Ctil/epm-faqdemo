---
project: BE
issue_key: BE-725
issue_type: Bug QA
status: Closed
tags:
- 07_workflow_business
- backend-(web)
- be
- faq
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-725
created: '2023-03-02'
resolved: '2023-03-02'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'BE-725: Purchase Order would duplicate a set of same items after Item Receive more than 1 time'
---
# BE-725: Purchase Order would duplicate a set of same items after Item Receive more than 1 time

## 問題描述

Location: [https://172.16.138.55/ChainStorePlus_AIGLE/home](https://172.16.138.55/ChainStorePlus_AIGLE/home)

Reproduce steps:

**Create a Purchase Order**

1. To Purchase Order Information (PO3000)

2. Create a Purchase Order

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

- Prorunner version has same issue (Ref: image-2023-03-02-11-26-10-430.png)

- Applied same location for stock receive more than 1 time also has the issue



## 相關資訊

- **Jira:** [BE-725](https://ctil.atlassian.net/browse/BE-725)
- **解決方式:** Done