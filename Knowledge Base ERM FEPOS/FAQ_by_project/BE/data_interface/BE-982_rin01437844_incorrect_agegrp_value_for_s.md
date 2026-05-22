---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "1.SOG call out MY区域有32 个OCE member的Age group不对，正确应该是'01'，'02'，而DB这些OCE48的member，为'1'， ''2'。"
root-cause: "待提取"
solution: "### Jira Comments (3 則)"
jira: BE-982
resolved: 
fix-version: ""
---

# BE-982: [RIN01437844] - Incorrect agegrp value for some MY OCE member data

## 問題

1.SOG call out MY区域有32 个OCE member的Age group不对，正确应该是"01"，"02"，而DB这些OCE48的member，为"1"， "'2"。
2.sample OCE480C00202371
查询change log ，此会员在 2023-12-28 08:46:12 由原来的 '02' 变成 'NULL',但是没有找到从什么时候又从 'NUll' 变成了现在的 '2'.Could you help to check the root cause?

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (3 則)
**Tovi Wang** (2025-01-13):
@@Cy Lau Just need check the root cause.I has corrected the data in DB now.
**Cy Lau** (2025-01-15):
Hold by @@Tovi Wang
**Tovi Wang** (2025-01-16):
@@pierre.shi has corrected the data in DB and resend them to CRM.closed this case first.

## 相關資訊

- Jira: [BE-982](https://ctil.atlassian.net/browse/BE-982)
- Fix Version: 未記錄
- 解決日期: 未記錄
