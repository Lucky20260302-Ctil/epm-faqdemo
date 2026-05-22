---
project: FE
title: "FE-1634: Data Unavailable in Datamart for 15-21 Jan"
issue_key: FE-1634
issue_type: Change Request
status: Closed
faq_score: 7.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, front-end-v720.02]
jira_url: "https://ctil.atlassian.net/browse/FE-1634"
created: 2025-02-28
resolved: 2025-04-08
resolution: Done
has_images: False
---

# FE-1634: Data Unavailable in Datamart for 15-21 Jan

## 問題描述

**Change Request for HKJC BJ RTM**

 

**Title: Implementation of "isConsentToHK" Indicator in POS and Datamart Processes**

 

**Date: 28/02/2025**

**Prepared By: Bobby Chu**

 

**Purpose**

To comply with legal requirements regarding the import of non-China member records, this change request outlines the necessary modifications to the POS system and associated Datamart processes to include the "isConsentToHK" indicator in Sales Journal.

 

**Background**

Due to legal constraints, the import of non-China member records into the BJ database is prohibited. To address this, we need to capture the consent of members regarding data sharing with Hong Kong and store this information in the Sales Journal and Datamart.

 

**Application**

Front End: **HKJC RTM BJ POS v720.02R05**

Back End: **HKJC RTM BJ BE v7.0**

 

**Scope of Change**

1. **POS System Modifications:(@Sang)**

- Add an "isConsentToHK" indicator (Yes/No) to each transaction in the POS system.

- Ensure that the indicator is captured during the transaction process.

2. **Database Modifications: @Jerry)**

- Utilize the orphan field jouinv_class char(10), joudep_class char(5), and jouser_class in the **pcd** record to store the "isConsentToHK" value.

- Update backend processes to ensure proper handling of this field.

3. **Sales Journal Adjustments: (@Jerry)**

- Modify the Sales Journal to include the "isConsentToHK" value with each transaction record.

4. **Datamart Process Adjustments: (@Jerry)**

- Update the **interim Datamart process** (HKJC_FASC.exe) to check the jouinv_cust_attr field for the "isConsentToHK" value before exporting data.

- Modify the **End-Stage Datamart interface** (HKJC_DM.exe) to rely on the jouinv_cust_attr field instead of the vipdef table.

**Timeline**

- **Development: 03/03/2025 - 6/03/2025**

- **Testing: 7/03/2025 - 13/03/2025**



## 相關資訊

- **Jira:** [FE-1634](https://ctil.atlassian.net/browse/FE-1634)
- **解決方式:** Done