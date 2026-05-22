---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "Program hardcore exclude member type = E."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1231
resolved: 2026-04-22
fix-version: ""
---

# BE-1231: [CS-1881] Issue_KSMY_Missing Transactions from POS to Memberson (Selected MY stores)

## 問題

Program hardcore exclude member type = E.
i would like to control the exclude member type by config in config file.
multi exclude member type is request

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-04-22
### Jira Comments (3 則)
**Jerry Wong** (2026-02-24):
Release:
\\DS411\csms60\delivery\coach_ks\add_config_exclude_viptype_2026-02-24
Notes:
add config in app.config, split by comma ‘,'
<add key="exclude_vip_type" value="E,A"/>
if set empty value <add key="exclude_vip_type" value=""/> ISNULL(vip_type, ‘') NOT IN (’’)
**Automation for Jira** (2026-04-21):
Issue has been created since
Days since: 55
Week since : 7
Issue due date difference
Days since : 
Weeks since:
**Sherman tse** (2026-04-21):
Verified on QA env with release:
\\DS411\csms60\delivery\coach_ks\add_config_exclude_viptype_2026-02-24\2026-04-20

## 相關資訊

- Jira: [BE-1231](https://ctil.atlassian.net/browse/BE-1231)
- Fix Version: 未記錄
- 解決日期: 2026-04-22
