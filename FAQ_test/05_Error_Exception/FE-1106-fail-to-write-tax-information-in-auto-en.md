---
project: FE
title: "FE-1106: Fail to write tax information in auto enable tax Rate POS instance."
issue_key: FE-1106
issue_type: Bug PRD
status: Closed
faq_score: 10.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1106"
created: 2022-03-28
resolved: 2022-07-12
resolution: Done
has_images: False
---

# FE-1106: Fail to write tax information in auto enable tax Rate POS instance. 

## 問題描述

It can be re-produced by Initial Configuration setup disable Tax function (syscon_Gst_Function=0) and effective tax rate was setup in dbmas.[tblVatRate]. When POS startup and detect effective tax rate in [tblvatRate], it will auto enable tax feature and set DB syscon_Gst_Function=-1. But when write complete transaction to database, POS have not get new gst function enable status and write 0 Gst to DB. This problem remains until POS Re-start.



## 相關資訊

- **Jira:** [FE-1106](https://ctil.atlassian.net/browse/FE-1106)
- **解決方式:** Done