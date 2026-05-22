---
project: BE
issue_key: BE-1152
issue_type: Bug PRD
status: Open
faq_score: 7.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-1152"
created: 2025-07-29
resolved: 
resolution: 
has_images: False
---

# BE-1152: Ticket no. 2025059 v67 pos cannot use mastconv files to update pos data

> **類型:** Bug PRD | **狀態:** Open
> **分類:** 效能與逾時 | **FAQ 分數:** 7.0
> **負責人:** Jerry Wong
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

V67 and V7 both can be worked this format like mastconv.dat.01 , mastconv,dat.02 , mastconv.dat.03….and so on  as those data are exported from cs2000 backend .

But after migration ,  using CSP , the file format is changed like mastconv.dat.1 , mastconv.2 , mastconv.3 ….. mastconv.dat.100 , mastconv.dat.101 ….. ,

**>> Please check and confirm if we can generate the mastconv with mastconv.dat.01 , mastconv,dat.02 , mastconv.dat.03**



## 相關資訊

- **Jira:** [BE-1152](https://ctil.atlassian.net/browse/BE-1152)