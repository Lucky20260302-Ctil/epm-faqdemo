---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Store user has some problem with  CS2000 - FE"
root-cause: "待提取"
solution: "### Jira Comments (4 則)"
jira: FE-1576
resolved: 
fix-version: ""
---

# FE-1576: RIN01424961 - MY - KMY720  - CS2000 - FE : after update pos, everything gets longer

## 問題

Store user has some problem with  CS2000 - FE
Symptom:
1. 
Long loading  when clicked follow button.
Such as- ‘Cash Drawer Balance', 'Sales Perf by Staff’.
From T9 log,We can see follow that
[20241130 21:11:30 -4233]: doEnq_CashDrawBalance- Start 
[20241130 21:20:46 -5343]: doEnq_CashDrawBalance- End
From Npos log,We can see follow long SQL.
@@Cy Lau<span style="color:#ff991f"> </span><span style="color:#ff5630">So could we optimize and improve the performance of SQL execution statements to shorten search time？</span>
CC: @@Joy Li @@Jason Wu @@pierre.shi  FYI.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (4 則)
**Tovi Wang** (2024-12-09):
@@Cy Lau @@Sang KMY720 Till1 logs and search Sales Performance long loading video for your reference.
**Cy Lau** (2024-12-09):
Thanks for the heads-up especially the investigation on NPOS log which almost nailed down in SQL issue
before talking about” could we optimize the sql execute statement”
DevTeam would like to know :
1. 
2. 
3.
**Andrew_Au** (2025-02-24):
@tovi Can I the ticket ?
**Tovi Wang** (2025-02-24):
@@Andrew_Au User confirmed issue gone now.We can closed the ticket first.I will keep monitoring with SOG team.Thanks!

## 相關資訊

- Jira: [FE-1576](https://ctil.atlassian.net/browse/FE-1576)
- Fix Version: 未記錄
- 解決日期: 未記錄
