---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "FE staff login by 'AAA'."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-918
resolved: 2021-03-01
fix-version: ""
---

# FE-918: MPOS-CN#29: Some singed in staff couldn't be found on MPOS

## 問題

FE staff login by "AAA".
Not shown in MPOS .
---
MPOS from Kingsley:
Please check this flag in DBTrans.MDF
Also Run the following SQL in DBTrans.mdf amd DBHist.mdf
Select H1.Salesman_code, A.salesman_sec_code, H1.attend_date+' '<u>H1.attend_Time as Attend_dateTime, H1.attend_In_out  from [Salady attendance history] As H1 Right Join (Select Salesman_code, Max(attend_date</u>' '<u>attend_Time) As attend_DateTime from [Salady attendance history]  where attend_pos_Date ='2021/02/08' Group by Salesman_code) as H2 On H1.Salesman_code=H2.Salesman_code And (H1.attend_date</u>' '+H1.attend_Time)=H2.attend_dateTime Left Join [Salady attendance] As A On H1.Salesman_code = A.Salesman_code

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2021-03-01
### Jira Comments (1 則)
**Sang** (2021-02-23):
1. Enhance Sync Multi-Till Salady Attendance History and Get Sign in Staff for different Process (KTS 210209 v750.01R01 720.02R06B Jira [🔗](https://ctil.atlassian.net/browse/FE-918#icft=FE-918))
-

## 相關資訊

- Jira: [FE-918](https://ctil.atlassian.net/browse/FE-918)
- Fix Version: 未記錄
- 解決日期: 2021-03-01
