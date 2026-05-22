---
project: MP
issue_key: MP-531
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, mposprint.exe]
jira_url: "https://ctil.atlassian.net/browse/MP-531"
created: 2022-06-14
resolved: 2024-03-01
resolution: Done
has_images: True
---

# MP-531: MPOSPrint.exe fail to print

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.0
> **解決日期:** 2024-03-01
> **負責人:** Cy Lau
> **組件:** MPOSPrint.exe

## 問題描述

Log path in FE: 

C:\CS2000POS\MPOSPrint_YYYYMMDD.log
C:\retdata6\T9YYMMDD.dat
C:\retdata6\DALYYYYMMDD.log

 

**Case 1: User start FE. auto recovery.**

2022-06-15 J421 &J487

J421 and J487 call out that they fail to print MPOS memo at 1400. But reported can print without any remote at 1600.

 

**Case 2: Sanyo kill MPOSprint.exe and start. then work**

2022-06-15 J486

J486 call out at 2pm too. I remote at 14:55 and found that the MPOSprint.exe in task manager but fail to found in notice bar. fail to open.

Therefore i kill MPOSprint.exe in task manager and start MPOSprint.exe manually. User reported that mpos print back to normal after i restart mposprint.exe
***No server IIS reset on 2022-06-14 ***

 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/670f1a35-39b6-48b7-8ed2-d8fab853482f)（需 Jira 登入）
 

**Case 3: MPOS IIS fail call print Hub >> Restart IIS then work**

2022-06-16 J368

 

 



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/670f1a35-39b6-48b7-8ed2-d8fab853482f)

## 相關資訊

- **Jira:** [MP-531](https://ctil.atlassian.net/browse/MP-531)
- **解決方式:** Done