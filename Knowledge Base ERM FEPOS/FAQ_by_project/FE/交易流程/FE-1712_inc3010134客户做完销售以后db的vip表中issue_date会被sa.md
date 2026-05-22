---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "以OC3000C00002005为例，6.2做了销售以后，VIP issue date就被同步成6.2了，并且在dbtmnlogd表中是没有这个被同步的记录的。"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1712
resolved: 2025-09-08
fix-version: ""
---

# FE-1712: [INC3010134]客户做完销售以后，db的vip表中issue date会被sales memo日期同步，实际上，issue date是不应该被sales memo的销售日期同步的。目前，issue date被同步的逻辑是什么？

## 問題

以OC3000C00002005为例，6.2做了销售以后，VIP issue date就被同步成6.2了，并且在dbtmnlogd表中是没有这个被同步的记录的。

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-09-08
### Jira Comments (6 則)
**Sang** (2025-06-12):
@@pierre.shi Which report is showing 30283.19? Backend/Web or FE ?
**pierre.shi** (2025-06-12):
Hi @@Sang 他们这个报告是根据issue date来查询的。sql查出来的issue date变动有2次，一次是在5.6，另外一次是6.5，从图中可以看到5.6将ussue date变更为2024-08-04以后，在6.5这一天从变动历史看到，issue date已经不是2024-08-04，而是2025-06-02，那这个issue date是否为产生销售的日期，产生销售的时候，销售日期会同步会更新这个issue date。
1为什么做销售会更新这个issue date
2issue date被销售日期更新，这里并没有记录。
具体日志以及查询进度，需要Joy帮忙更新下。
Hi @@Joy Li 我这边描述有什么遗漏或者不正确的，麻烦帮忙一并更新下
CC: @@Joy Li
**Andrew_Au** (2025-09-08):
@@pierre.shi @@Tovi Wang @@Joy Li  Please update the ticket status
**Tovi Wang** (2025-09-08):
@@pierre.shi Please update.
**pierre.shi** (2025-09-08):
@@Andrew_Au
SOG Jira [CS-1470](https://jira.tapestry.support/browse/CS-1470) . please help to close here
**Automation for Jira** (2025-09-08):
Issue has been created since
Days since: 89
Week since : 12
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1712](https://ctil.atlassian.net/browse/FE-1712)
- Fix Version: 未記錄
- 解決日期: 2025-09-08
