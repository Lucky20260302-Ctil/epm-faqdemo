---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "[INC2996330]PRC V75 OC254till0 sales memo 00009176 missed vip gender in pcd file"
root-cause: "待提取"
solution: "### Jira Comments (8 則)"
jira: FE-1704
resolved: 
fix-version: ""
---

# FE-1704: [INC2996330]PRC V75 OC254till0 sales memo 00009176 missed vip gender

## 問題

[INC2996330]PRC V75 OC254till0 sales memo 00009176 missed vip gender in pcd file

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (8 則)
**Sang** (2025-05-29):
@@pierre.shi Member information returned from web API without gender data
**Andrew_Au** (2025-06-05):
@@pierre.shi @@Tovi Wang Please update the ticket status
**pierre.shi** (2025-06-05):
Hi @@Andrew_Au  Please help to close this ticket.
**pierre.shi** (2025-08-27):
dayend issue on 26th Aug:
**Tovi Wang** (2025-08-30):
@@Sang 我明白那空的会员名和空的gender code是CRMAPI return过来的。但是我们为什么要让没有姓名和gender code的会员能在前台搜索出来并且写到PCD file里面呀？因为在BE里面会员名和gender code 是必填项，如果PCD file里面没有会员名和gender code的话，post PCD file会报错。
我记得在CRMBEAPI中，如果CRM return null member name ,API program会分配一个默认会员名 ‘BEAPI' 给到此会员然后upsert到DB.
1.当时我们和CRM做这一块的对接时，双方align好的SOW是否有对这两个字段做规定，比如CRM不能传Null member name 和 Null gender code给我们？
2.我们是否可以考虑在在前台加一个会员名和gender code等必填字段的校验，比如CRM return data没有会员名或者gender code时，POS前台提示此会员没有会员名或者没有gender code，请新建会员,并且不给在POS前台显示。
3.或者前台POS和API upsert逻辑保持一致，如果CRM return会员没有会员名和gender code,前台自动分配一个默认会员名 ‘BEAPI’ 和默认gender code 'F’ 给到此会员，同时写到PCD file.
@@Joy Li @@Cy Lau If I’m wrong please correct me.Let me know your ideas for this issue.Thanks!
**Andrew_Au** (2025-10-08):
@@pierre.shi @@Tovi Wang  Please the status
**pierre.shi** (2025-10-09):
@@Andrew_Au Please help to close this ticket
**Automation for Jira** (2025-10-09):
Issue has been created since
Days since: 135
Week since : 19
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1704](https://ctil.atlassian.net/browse/FE-1704)
- Fix Version: 未記錄
- 解決日期: 未記錄
