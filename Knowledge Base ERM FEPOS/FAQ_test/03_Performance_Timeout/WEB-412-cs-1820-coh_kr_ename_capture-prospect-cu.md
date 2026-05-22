---
project: WEB
issue_key: WEB-412
issue_type: Change Request
status: HOLD
faq_score: 6.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, web, performance_timeout, ename]
jira_url: "https://ctil.atlassian.net/browse/WEB-412"
created: 2025-11-04
resolved: 
resolution: 
has_images: False
---

# WEB-412: [CS-1820] COH_KR_eName_Capture prospect customer

> **類型:** Change Request | **狀態:** HOLD
> **分類:** 效能與逾時 | **FAQ 分數:** 6.0
> **負責人:** Cy Lau
> **組件:** eName

## 問題描述

in Korea, we got request from CRM/MKT team how can capture prospect customer data. 

and put something Memo in these customer data.

Especially Popup Event store, customer will NOT purchase but having strong interesting Coach product.  for communicate customer later, we want to get something flag/remark function in eNameCapture

 

#1. in eNameCapture side, can we add 1-2 new memo field for input remark?

#2-1. in VIP table, can we re-use "vip_title" (nvarchar(10)) column for store this remark?

#2-2.  maybe can we extend size of this vip_title db definition? (extend to nvarchar(30), etc)

#3. can you give us rough estimation how long it need to spend for this change?



## 相關資訊

- **Jira:** [WEB-412](https://ctil.atlassian.net/browse/WEB-412)