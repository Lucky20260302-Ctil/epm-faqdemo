---
project: FE
issue_key: FE-918
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-918"
created: 2021-02-09
resolved: 2021-03-01
resolution: Done
has_images: False
---

# FE-918: MPOS-CN#29: Some singed in staff couldn't be found on MPOS

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 7.0
> **解決日期:** 2021-03-01
> **負責人:** Joy Li
> **組件:** Front End

## 問題描述

FE staff login by "AAA".
Not shown in MPOS .

 

 

---

MPOS from Kingsley:

Please check this flag in DBTrans.MDF

   >>   TblConfig! ALLOWSTAFFUSEINOTHERTILL = 'Y'

Also Run the following SQL in DBTrans.mdf amd DBHist.mdf

Select H1.Salesman_code, A.salesman_sec_code, H1.attend_date+' '<u>H1.attend_Time as Attend_dateTime, H1.attend_In_out  from [Salady attendance history] As H1 Right Join (Select Salesman_code, Max(attend_date</u>' '<u>attend_Time) As attend_DateTime from [Salady attendance history]  where attend_pos_Date ='2021/02/08' Group by Salesman_code) as H2 On H1.Salesman_code=H2.Salesman_code And (H1.attend_date</u>' '+H1.attend_Time)=H2.attend_dateTime Left Join [Salady attendance] As A On H1.Salesman_code = A.Salesman_code



## 相關資訊

- **Jira:** [FE-918](https://ctil.atlassian.net/browse/FE-918)
- **解決方式:** Done