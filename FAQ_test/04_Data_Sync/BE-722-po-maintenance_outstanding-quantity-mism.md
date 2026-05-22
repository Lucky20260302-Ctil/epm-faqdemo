---
project: BE
title: "BE-722: PO Maintenance_Outstanding Quantity Mismatch"
issue_key: BE-722
issue_type: Bug PRD
status: Closed
faq_score: 6.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-722"
created: 2023-02-27
resolved: 2023-03-02
resolution: Done
has_images: False
---

# BE-722: PO Maintenance_Outstanding Quantity Mismatch

## 問題描述

55 site environemnt 

Reproduce Steps (As an example):

Need to create PO first

1. Click Process

2. Click Purchase Order

3. Purchase Oder Maintenance

4. Click 'Create' 

5. Click PO date, Supplier >1003032, Currency> HKD in 'Header Info'  - Attachment 1

6. Select '<PAGEAGE> & input Quantity - Attachment 2

7. Click 'Save'

 Check PO outstanding 

1. Click Inquiry

2. Click Purchase Order

3. Select inputed PO

4. Double Click 'Create' 

5. Click Manage and update Outstanding Quantity - Attachment 3 is correct

 Stock Receive

1. Click Process

2. Click Stock Receive

3. Select Stock Receive Confirmation Process

4. Click Create, supplier as same, Input PO number in <With PO> & input Rec Quatity - Attachment 4

5. Right click <Batch Validation> - Attachemnt 5

6. Right click <Batch Posting>

Repeat Check PO outstanding 

1. Click Inquiry

2. Click Purchase Order

3. Select inputed PO

4. Double Click 'Create' 

5. Click Manage and update Outstanding Quantity - Attachment 6 is correct

6. Click Header Info and update Outstanding Quantity - **Attachment 7 is incorrect**

 

- You can find PO#20230226 for your information




## Jira Comments

> **Jacky Lam** (2023-02-27):
> Prorunner has same issue to be fixed, plz deploy on their Production site afterwards. For   note, here're othe ways (not only above example) to do Stock Receive, Plz fix this oustanding issue by other ways for Stock Receive at the same time.

> **Jacky Lam** (2023-02-27):
> CC: 

> **Sherman tse** (2023-03-02):
> Verified on 172.16.138.55 Close Case  

## 相關資訊

- **Jira:** [BE-722](https://ctil.atlassian.net/browse/BE-722)
- **解決方式:** Done