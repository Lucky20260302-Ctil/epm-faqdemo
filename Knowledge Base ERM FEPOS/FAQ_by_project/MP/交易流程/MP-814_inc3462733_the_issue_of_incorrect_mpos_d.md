---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "@@Sang J364 店铺反馈 2026-02-23创建三笔MPOS销售，但是MPOS date 却显示 2026-02-22。请帮忙查询RCA.什么情况下会发生这种情况？谢谢！"
root-cause: "待提取"
solution: "### Jira Comments (3 則)"
jira: MP-814
resolved: 
fix-version: ""
---

# MP-814: [INC3462733] The issue of incorrect MPOS date on MPOS memo

## 問題

@@Sang J364 店铺反馈 2026-02-23创建三笔MPOS销售，但是MPOS date 却显示 2026-02-22。请帮忙查询RCA.什么情况下会发生这种情况？谢谢！
根据我的理解，MPOS的销售日期是根据 Till0 POS date走的。说明店铺2026-02-23创建这三笔MPOS销售的时候，POS date当时显示是 2026-02-22。但我查询2026-02-22 日结已正常完成.
J364-MB002725，create time: 2026-02-23 12:35
J364-MA003745，create time: 2026-02-23 12:04
J364-MC002018，create time: 2026-02-23 14:34
[1.BE](http://1.BE) capture
2.查询T9 log如下图：

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (3 則)
**Tovi Wang** (2026-02-27):
@@Sang 22 Feb & 23 Feb till0 logs for your further checking.
CC @@Joy Li @@Cy Lau @@pierre.shi
**Automation for Jira** (2026-03-03):
Issue has been created since
Days since: 3
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Tovi Wang** (2026-03-04):
Store not open cs2000 on 02-23 morning.update the details to SOG & Coach team.Can be closed first.

## 相關資訊

- Jira: [MP-814](https://ctil.atlassian.net/browse/MP-814)
- Fix Version: 未記錄
- 解決日期: 未記錄
