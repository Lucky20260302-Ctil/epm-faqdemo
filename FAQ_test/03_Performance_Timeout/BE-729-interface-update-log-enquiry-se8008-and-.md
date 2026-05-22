---
project: BE
title: "BE-729: Interface Update Log Enquiry (SE8008) and Interface Posting Error Enquiry (AS2000) changes for Lands Project"
issue_key: BE-729
issue_type: Task
status: Closed
faq_score: 7.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-729"
created: 2023-03-23
resolved: 2023-07-26
resolution: Done
has_images: False
---

# BE-729: Interface Update Log Enquiry (SE8008) and Interface Posting Error Enquiry (AS2000) changes for Lands Project

## 問題描述

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

 



## 相關資訊

- **Jira:** [BE-729](https://ctil.atlassian.net/browse/BE-729)
- **解決方式:** Done