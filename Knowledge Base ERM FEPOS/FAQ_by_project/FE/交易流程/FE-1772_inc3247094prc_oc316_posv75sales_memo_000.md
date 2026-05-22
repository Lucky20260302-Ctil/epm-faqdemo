---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "[INC3247094]PRC OC316 POSv75,Sales memo 00004891 invoice QR code can't be printed out."
root-cause: "待提取"
solution: "### Jira Comments (6 則)"
jira: FE-1772
resolved: 
fix-version: ""
---

# FE-1772: [INC3247094]PRC OC316 POSv75,Sales memo 00004891 invoice QR code can't be printed out

## 問題

[INC3247094]PRC OC316 POSv75,Sales memo 00004891 invoice QR code can't be printed out.
Have 5 sales memos, only 00004891 invoice QR code can't be printed out.
import xconfig, issue still
checked the vip info in db, missed vip name, update the vip name, issue still, please kindly help to check

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (6 則)
**Automation for Jira** (2025-10-22):
Issue has been created since
Days since: 1
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2025-10-22):
@@pierre.shi Memo#00004891 was selected not print out e_invoice QR-code
u
**pierre.shi** (2025-10-22):
Hi@@Sang这个选择项是在哪个页面选择的？
**pierre.shi** (2025-10-22):
@@Sang Hi Sang，4891这个单子是打印的时候，没有下图中这个qrcode，更新invtrx_prt_einv这个字段值以后，重新打印，还是不能打印出qrcode
**Sang** (2025-10-22):
@@pierre.shi change dbhist.[jouinvh].invtrx_prt_einv='Y', can print qr code
**pierre.shi** (2025-10-24):
@@Sang ok. thanks

## 相關資訊

- Jira: [FE-1772](https://ctil.atlassian.net/browse/FE-1772)
- Fix Version: 未記錄
- 解決日期: 未記錄
