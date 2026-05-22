---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "Till 1 pos failed to scan the payment code of Alipay from customer and shows invalid amount"
root-cause: "待提取"
solution: "### Jira Comments (7 則)"
jira: FE-1738
resolved: 
fix-version: ""
---

# FE-1738: [INC3113670]HK OCF583 Till 1 pos failed to scan the payment code of Alipay from customer and shows invalid amount 

## 問題

Till 1 pos failed to scan the payment code of Alipay from customer and shows invalid amount

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (7 則)
**Tovi Wang** (2025-07-29):
@Sang Please help to double check and confirm the error “Invalid Amount“ is come from CMB return response or not?FE T9 logs on attachment for your reference.Thanks!
CC @@Joy Li @@Cy Lau
**Sang** (2025-07-29):
@@Tovi Wang Yes. That error message is come from CMD return response.
**Tovi Wang** (2025-07-29):
@@Sang Many Thanks for your double confirm.
只有HK OCF583 Till 1从07-25下午突然有这个error（Till0 用此支付方式没有error）,早上用QAP支付方式还可以正常使用且没有error.我们前台有QAP payment支付方式相关的setting嘛？谢谢！
**Sang** (2025-07-29):
@12:15@@Tovi Wang Last successful respsonse returned from CMB APLI Pay occured  @12:45, afterward all response is fail.
**Tovi Wang** (2025-07-29):
@@Sang Yes,Right.I also found this situation.我先让Coach Team去问下CMB side.但是只有这一个till突然有这个error也很奇怪。我们前台是否有QAP 支付方式相关的setting呀?
**Automation for Jira** (2025-07-31):
Issue has been created since
Days since: 2
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Tovi Wang** (2025-08-08):
Dear ALL,
Issue caused by incorrect EFT setting.EFT team re-set the till code,then issue fixed.Thanks!

## 相關資訊

- Jira: [FE-1738](https://ctil.atlassian.net/browse/FE-1738)
- Fix Version: 未記錄
- 解決日期: 未記錄
