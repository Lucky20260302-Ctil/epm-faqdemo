---
project: BE
issue_key: BE-1153
issue_type: Task
status: Closed
faq_score: 6.0
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, be, install_deploy, backend-(chainstoreplus-7.0), table]
jira_url: "https://ctil.atlassian.net/browse/BE-1153"
created: 2025-08-04
resolved: 2026-05-05
resolution: Done
has_images: False
---

# BE-1153: [CS-1371] Testing schedule for SQL Server Upgrade from 2016 to 2022

> **類型:** Task | **狀態:** Closed
> **分類:** 安裝與部署 | **FAQ 分數:** 6.0
> **解決日期:** 2026-05-05
> **負責人:** Sherman tse
> **組件:** Backend (ChainStorePlus 7.0), Table

## 問題描述

Background : 

> **info:** Due to SQL 2016 is EOL, we need to upgrade our POS SQL to ~~2019 or~~ 2022.

please kindly help to evaluate the new SQL capacity, system impact and effort to switch the SQL. 

> Estiamtions for checking from Aug to Sept would be practical for Sanyo Side.

For the upgrade to SQL Server 2022, we would like to propose into 2 phrases: #1 Security update  

#2 Performance wise by levelaging the features of SQL server 2022  

We suggest to implement #1 first which involves following :

1. Indexes checking

2. DB functions checking  

1. Table-valued Functions

2. Scalar-valued Functions

3. StoredProcedures

 

| Type | Count | 
| SQL_SCALAR_FUNCTION | 33 | 
| SQL_STORED_PROCEDURE | 693 | 
| SQL_TABLE_VALUED_FUNCTION | 58 | 

***will be variant according to regions 
 
The tests would be conducted on QA for ensuring avaliable on SQL server 2022

The checking would be excuted by CSPLUS Backend , BE web enquiry and DataInterface modules or standalone programs.



## 相關資訊

- **Jira:** [BE-1153](https://ctil.atlassian.net/browse/BE-1153)
- **解決方式:** Done