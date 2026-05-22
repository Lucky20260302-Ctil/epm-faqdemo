---
tags: [faq, fe, 系統服務]
component: "BackEnd"
symptom: "中国以下五个coupon遇到了无法邮件approve的问题。"
root-cause: "待提取"
solution: "### Jira Comments (8 則)"
jira: FE-1628
resolved: 
fix-version: ""
---

# FE-1628: CN Epromo 邮件approve失败

## 問題

中国以下五个coupon遇到了无法邮件approve的问题。
COACHXY200
COACHXY300
COACHXY400
COACHXY500
COACHXY600
1.从DB看，Retail 这边（Caroline Zhang ）已经批了，现在等待Finance的批复。
2.但是昨天Finance确认已经通过邮件批复，且能找到对应发出的邮件。
请帮忙查一下原因并修复这五个coupon。

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (8 則)
**Tovi Wang** (2025-02-19):
@@Anson Cheung Mail approve log for your reference.Please help to double check and advice the temp work around.Thanks!
CC :@bobby @@Cy Lau @@Jason Wu FYI.
**Tovi Wang** (2025-02-19):
select * from appath where appath_id like '%COACHXY600%'
select * from appath where appath_id like '%COUPN0221%'
select top 10 * from appath where appath_stage = '2' and appath_actiontaken_date is not NULL order by appath_actiontaken_date DESC
**Anson Cheung** (2025-02-20):
@@Tovi Wang can you check if these 5 emails subject exist in backend table “o365email“ in gldata?
if yes, please provide the details of records.
**Tovi Wang** (2025-02-20):
@@Anson Cheung  these 5 emails subject NOT exist in backend table “o365email“ in gldata.Please further checking.Thanks!
**Tovi Wang** (2025-02-20):
@@Anson Cheung 我们是否有temp workaround先手动把那几个Epromo approved?因为User今天要用那几个Epromo.谢谢！
**Anson Cheung** (2025-02-20):
@@Tovi Wang  應該可以在Epromo的protal找到那幾個coupon再手動approve
**Tovi Wang** (2025-02-20):
@@Anson Cheung Lein问我们是否可以在DB data patch或者script 来approved？Please advice.Thanks!
**Tovi Wang** (2025-02-24):
Dear ALL,
已建议客户重新手动approved.如果没有其它问题先closed.

## 相關資訊

- Jira: [FE-1628](https://ctil.atlassian.net/browse/FE-1628)
- Fix Version: 未記錄
- 解決日期: 未記錄
