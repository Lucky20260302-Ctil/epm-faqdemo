---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Please reference the member have 2 sales & 1 void, but in the vipmovent dont have the void BP record"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1662
resolved: 2025-09-30
fix-version: ""
---

# FE-1662: IMX void memo didnt return BP to member

## 問題

Please reference the member have 2 sales & 1 void, but in the vipmovent dont have the void BP record,
Log copied in 
\\172.16.183.201\localuser\support\20250328\IMX_BP.zip

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-09-30
### Jira Comments (6 則)
**Jason Wu** (2025-04-01):
I added the BE posting error; it likely looks like the void discount record can not be posted to BE.
**Jason Wu** (2025-04-01):
@@Sang  seems like the void memo missed the line 24/25,attetchd the PC file & the Dbtrans, please help to have a look
**Sang** (2025-04-02):
@@Jason Wu please get 2025.03.01 dbtrans, PC file and log from BPSHKG35
**Sang** (2025-04-02):
@@Jason Wu Void Memo does not write 24/25. Return Redeem Pts write adjusted as PCD ‘36’ .
Please compare with 25.03.31 Void Memo #00042704
**Andrew_Au** (2025-08-28):
@@Joy Li @@Bobby  Did you know the ticket status ? Could we change the ticket status to close
**Automation for Jira** (2025-09-30):
Issue has been created since
Days since: 185
Week since : 26
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1662](https://ctil.atlassian.net/browse/FE-1662)
- Fix Version: 未記錄
- 解決日期: 2025-09-30
