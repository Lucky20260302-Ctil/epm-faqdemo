---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "cannot open AS2000 and SE8008"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-760
resolved: 2023-06-23
fix-version: ""
---

# BE-760: error when trying to open AS2000 and SE8008

## 問題

cannot open AS2000 and SE8008
Updated db by below sql script
DELETE FROM gldata.dbo.enqdic WHERE enqdic_progid = 'AS2000' and enqdic_seq > 5;
update gldata.dbo.enqdic set enqdic_field = 'interlog_comp_date' , enqdic_unique_key = 'interlog_comp_date' WHERE enqdic_progid = 'SE8008' and enqdic_seq = 1;
DELETE FROM gldata.dbo.enqdic WHERE enqdic_progid = 'SE8008' and enqdic_seq > 7;

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-06-23
### Jira Comments (2 則)
**Sherman tse** (2023-06-20):
Will be retested on QA env .55
**Sherman tse** (2023-06-23):
Tested on QA .55 env. Close case

## 相關資訊

- Jira: [BE-760](https://ctil.atlassian.net/browse/BE-760)
- Fix Version: 未記錄
- 解決日期: 2023-06-23
