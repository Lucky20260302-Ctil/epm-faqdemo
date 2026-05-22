---
project: BE
issue_key: BE-741
issue_type: SOW
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-741"
created: 2023-05-30
resolved: 2023-07-20
resolution: Done
has_images: False
---

# BE-741: Data Cleansing for MY and SG coach

> **類型:** SOW | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2023-07-20
> **負責人:** Joy Li
> **組件:** Backend (Web)

## 問題描述

**VIP Table Data Cleansing**

 ** 

**This is a one-off tool to help KS SEA to purge the duplicate VIP master data for data migration to CDP. So, this program does not require annual software maintenance.** 

 ** 

- Develop a program to follow the rules in the ‘Memebership Cleansing Guide’ to list out the potential cleansing VIP records in a report for users to verify and confirm. It will also return a list of potential cleansing VIP No. in a text file. User can edit this ‘Cleansing VIP No.’ file to confirm which VIP record to be cleansing.

 

Membership Cleansing Guide:

- Guide for Membership cleansing MY v1.0.docx

- Guide for Membership cleansing SG v1.0.docx

 

- Develop a cleansing program to follow the ‘Cleansing VIP No.’ file to do the data cleansing. The cleansing includes the following actions:

- Remove the invalid phone no.

- Fixing the incorrect email address.

- Filter out the duplicate VIP record by email and phone number.

- Populate and merge the fields.

- Update the VIP historical transactions.

- Purge the duplicate VIP records.

- Update the VIP records to POS front end.

 

This program will generate a report to list out the VIP records which have been changed for audit trial. The changed VIP records will be updated in POS front end.

 ** 

**NOTE: As the changed VIP records will be updated in the POS front end. To minimize the impact on front-end operations, it is recommended to limit the process VIP record to no more than 10,000 per daily batch.**



## 相關資訊

- **Jira:** [BE-741](https://ctil.atlassian.net/browse/BE-741)
- **解決方式:** Done