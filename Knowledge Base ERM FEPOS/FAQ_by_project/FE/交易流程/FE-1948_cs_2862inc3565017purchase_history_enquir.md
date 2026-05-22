---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "Email Subject: TW Members info in CS2K are not synced with CRM"
root-cause: "待提取"
solution: "### Jira Comments (2 則)"
jira: FE-1948
resolved: 
fix-version: ""
---

# FE-1948: [CS-2862][INC3565017]Purchase History enquire only display last 5 transaction 

## 問題

Email Subject: TW Members info in CS2K are not synced with CRM
Symptom:
For example, customer owns 10 transactions in 2025/06/30-2026/04/17, but Purchase History enquire only able to view the last 5 transaction
想詢問筆數上限是五單，是有辦法優化的嗎? 因為現在的呈現狀態不是分成很多頁，但一頁5筆，而是不管選擇什麼區間，都只會顯示間最新的5筆，這樣對於前線來說查詢極為不便
舉例：假如有位顧客於2025/06/30-2026/04/17整年總共消費了10單，但SA事先並無法得知，所以用這個區間去查詢的時候，就永遠只會顯示最後的那5單，會需要不斷來回調整時間區段
1.
Member code: OC7170T00016428
Member phone: 0932345204
search time:2026-04-26 16:18:25
2.Member code: OC7170T00016428 have
3.request info
4.response info

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (2 則)
**Tovi Wang** (2026-05-11):
@@Joy Li API log here for your further checking.
**Tovi Wang** (2026-05-21):
Hi @@Joy Li@@Sang  As talked in before.Please double check and confirm this issue if need to program enhancemnet.
In the Purchase History page.I had confirmed There are all NOT 'Next Page' button on both of PRC & TW region.

## 相關資訊

- Jira: [FE-1948](https://ctil.atlassian.net/browse/FE-1948)
- Fix Version: 未記錄
- 解決日期: 未記錄
