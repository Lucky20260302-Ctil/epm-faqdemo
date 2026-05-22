---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "@@Bobby @@Anson Cheung @@Cy Lau TW也有电话号码不一致的情况，导致会员同步到CRM失败，重发仍然失败。"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1013
resolved: 2025-05-21
fix-version: ""
---

# BE-1013: email - If there is similar error in TW (vip number does not match the customer)

## 問題

@@Bobby @@Anson Cheung @@Cy Lau TW也有电话号码不一致的情况，导致会员同步到CRM失败，重发仍然失败。
Tovi:TW 之前失败的会员已经重传，但是还有部分会员重传也失败。请看下下面会员重传仍然被拒的原因。OCF841T00008010
ACX: OCF841T00008010 CRM 侧手机号为 0971250730 ，接口传过来的手机号是 0938811730
1.member OCF841T00008010 issue data:2020-11-11,DB Tel no 0938811730 .
2.dbtmnlogd table for your reference.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-21
### Jira Comments (6 則)
**Bobby** (2025-02-28):
Firstly, I recommend adding a record change log to track each update made to the record. This will allow us to easily trace the time, location, and user responsible for the changes. Without this log, identifying the root cause of issues becomes challenging.
@@Anson Cheung, please list out of all functions that update the VIP table and indicate where we should incorporate the change log.
@@Cy Lau, any other suggestions you may have on this matter?
**Anson Cheung** (2025-02-28):
function will update vip table:
1. 
2. 
3.
**Andrew_Au** (2025-04-07):
@bobby Please update the ticket status
**Bobby** (2025-04-07):
@@Anson Cheung Have you started the development yet? If yes, please let me know the change in which release.
**Andrew_Au** (2025-05-21):
@tovi Please update the ticket status
**Tovi Wang** (2025-05-21):
@@Andrew_Au - closed first.

## 相關資訊

- Jira: [BE-1013](https://ctil.atlassian.net/browse/BE-1013)
- Fix Version: 未記錄
- 解決日期: 2025-05-21
