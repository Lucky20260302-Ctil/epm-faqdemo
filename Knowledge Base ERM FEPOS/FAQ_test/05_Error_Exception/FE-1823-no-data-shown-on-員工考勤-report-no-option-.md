---
project: FE
issue_key: FE-1823
issue_type: Bug PRD
status: Selected for Development (migrated)
faq_score: 6.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1823"
created: 2025-11-28
resolved: 
resolution: 
has_images: False
---

# FE-1823: No data shown on 員工考勤 report & no option of location selection when doing transfer memo

> **類型:** Bug PRD | **狀態:** Selected for Development (migrated)
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.0
> **負責人:** Sang
> **組件:** Front End

## 問題描述

there' are 2 issues on Prorunner (store: P10) on 27 Nov 2025:

1. Store found the  員工考勤 report data is incorrect, nothing shown on the report before 14:34, and only the record on sign in at 14:34 (Staff: 1195) is shown, checked the dbhist, staff 1033 also sign in at 10:37am, and from T9, staff 1095 is a sales lady of a sales memo, there should be sign in record of both of them in the morning, however, the report cannot shown anything 

2. Store found no location can be selected from the drop down list when doing transfer at 16:00

please have a look, logs and related files provided, thank you.



## 相關資訊

- **Jira:** [FE-1823](https://ctil.atlassian.net/browse/FE-1823)