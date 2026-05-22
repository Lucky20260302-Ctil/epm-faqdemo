---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "refer to INC3180836， kindly provide the RCA."
root-cause: "待提取"
solution: "### Jira Comments (5 則)"
jira: MP-798
resolved: 
fix-version: ""
---

# MP-798: [MPOS-123] JP MPOS has started experiencing situations where scanning product A brings up product B's information

## 問題

refer to INC3180836， kindly provide the RCA.
The scanned SKU is not the same as the displayed SKU on Mpos
Version:75.004.1305.0001
Mpos: Local iis
Mpos version:3.30.3
Troubleshooting：
1.All Mpos have the same issue
2.After restarting IIS, it returned to normal, but after a period of time, the same problem occurred again
3.For example, the scanned SKU is CAL17, but the Mpos displays CW329

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (5 則)
**Tovi Wang** (2025-09-08):
Waiting SOG team double confirm the issue details with store in TMR.
CC @@Joy Li
**Joy Li** (2025-09-09):
Log copied from J804 till 0 IIS folder on 2025-09-09
**Cy Lau** (2025-09-09):
Scanned 4 times 196395775941
**Cy Lau** (2025-09-09):
5-Sept : 
Only 1 time
**Tovi Wang** (2025-09-18):
User mis-operation and mis-understanding.Closed ticket.

## 相關資訊

- Jira: [MP-798](https://ctil.atlassian.net/browse/MP-798)
- Fix Version: 未記錄
- 解決日期: 未記錄
