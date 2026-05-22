---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "Till0 sales cannot be uploaded to HKMR timely"
root-cause: "待提取"
solution: "### Jira Comments (1 則)"
jira: FE-1952
resolved: 
fix-version: ""
---

# FE-1952: [CS-2672] Issue_PRC_INC3520233_OCF516 till0 sales cannot be uploaded to HKMR timely

## 問題

Till0 sales cannot be uploaded to HKMR timely
Worknote from Jira ticket:
我查了下05-14新建的2笔Till0销售可以自动生成ACP file并且正常上传到DB...我没有做任何变更.
请继续监测 OCF516 till0 的销售上传情况。下面截图供参考。
1. 
05-14 做了2笔销售
2.
select * from sqlpcdossb
where sqlpcd_post_ref like 'acp20260514124006.OCF516__0%'
---sales memo: 00002795
select * from sqlpcdossb
where sqlpcd_post_ref like 'acp20260514164006.OCF516__0%'
---sales memo: 00002796

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (1 則)
**Automation for Jira** (2026-05-18):
Issue has been created since
Days since: 4
Week since : 0
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1952](https://ctil.atlassian.net/browse/FE-1952)
- Fix Version: 未記錄
- 解決日期: 未記錄
