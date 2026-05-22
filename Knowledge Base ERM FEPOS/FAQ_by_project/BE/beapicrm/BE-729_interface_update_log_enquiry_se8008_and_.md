---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Please provide the changed SQL script on enqdic"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-729
resolved: 2023-07-26
fix-version: ""
---

# BE-729: Interface Update Log Enquiry (SE8008) and Interface Posting Error Enquiry (AS2000) changes for Lands Project

## 問題

Please provide the changed SQL script on enqdic
DB
ip:172.16.138.128, login: csuser, pw: csuser
New display data:
for Interface Posting Error Enquiry (AS2000)
```sql
SELECT asperr.asperr_date,
asperr.asperr_file_date,
asperr.asperr_line_no, 
asperr.asperr_err_msg,
asperr_file_name
FROM asperr 
order by 1 desc
```
for Interface Update Log Enquiry (SE8008)
```sql
select interlog_comp_date, interlog_file_date, interlog_file_name, interlog_total, interlog_success, interlog_fail, interlog_err_msg from interlog order by A4GLIdentity desc
```
Other sql reference
```java
SELECT enqsql_select, 
    enqsql_join, 
    enqsql_where, 
    enqsql_group, 
    enqsql_having 
FROM enqsql 
WHERE enqsql_progid = 'AS2000' 
    AND  ISNULL(enqsql_company, ' ')  = ''
SELECT * 
FROM enqdic
WHERE enqdic_progid = 'AS2000' 
    AND  ISNULL(enqdic_company, ' ')  = '' 
ORDER BY enqdic_disp_seq 
SELECT enqsql_select, 
    enqsql_join, 
    enqsql_where, 
    enqsql_group, 
    enqsql_having 
FROM enqsql 
WHERE enqsql_progid = 'SE8008' 
    AND  ISNULL(enqsql_company, ' ')  = '' 
SELECT * 
FROM enqdic
WHERE enqdic_progid = 'SE8008' 
    AND  ISNULL(enqdic_company, ' ')  = '' 
ORDER BY enqdic_disp_seq
```

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-07-26
### Jira Comments (6 則)
**Andy Ko** (2023-06-13):
@@Hans Wong
**Hans Wong** (2023-06-13):
@@Jerry Wong Please help to see what's the problem.
**Sherman tse** (2023-06-23):
tested on .55 QA env
**Andy Ko** (2023-06-23):
OK now
environment: 172.16.138.55/ChainStorePlus_LandsD_QA
**Sherman tse** (2023-07-05):
Retested on LANDS DEV 10.77.227.31 (SMO-PMSSAPP-D1)
*system may have 2 record incorrect will pop up error, we should apply 2 new sql command (Ref:\\172.16.183.201\localuser\support\20230705) find sqlenq.sql
**Sherman tse** (2023-07-07):
Tested on UAT LANDS

## 相關資訊

- Jira: [BE-729](https://ctil.atlassian.net/browse/BE-729)
- Fix Version: 未記錄
- 解決日期: 2023-07-26
