---
tags: [faq, be, beapicrm]
component: "API"
symptom: "1.CRM API responsed the vip_name1 and vip_last_name all are 'Yoyo'."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-944
resolved: 2025-02-24
fix-version: ""
---

# BE-944: [ACU-106]CRM - vip name can't sync with CRM API response

## 問題

1.CRM API responsed the vip_name1 and vip_last_name all are 'Yoyo'.
2.But in DB vip table, vip_name1 is ‘BEAPI’ and vip_last_name is NULL.Please double check and confirm the logic and fixed it in hot fix.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-02-24
### Jira Comments (7 則)
**Tovi Wang** (2024-11-14):
QA WEB21 2024-11-14 API log for your reference.
**Tovi Wang** (2024-11-14):
@@Anson CheungCould you help to double check and confirm this issue and fixed it in new released?
CC @@Sherman tse @@Joy Li @@Cy Lau FYI.
**Andrew_Au** (2024-12-24):
@@Tovi Wang  Please update the ticket status
**Andrew_Au** (2025-01-03):
@@Joy Li @@Tovi Wang Please update the ticket status
**Tovi Wang** (2025-01-03):
@@Joy Li  这个issue就是V75 pilot store OC182 会员名是 ‘BEAPI’的问题，请确认是否可以closed这个Jira?
@@Andrew_Au Joy & Bobby are double checking the SOW and discussing with Coach team for the details.
**Andrew_Au** (2025-02-24):
@@Bobby I close the ticket ?
**Bobby** (2025-02-24):
Yes, please close this ticket because they have deployed to PRD and confirmed the bug has been fixed by R3.80.

## 相關資訊

- Jira: [BE-944](https://ctil.atlassian.net/browse/BE-944)
- Fix Version: 未記錄
- 解決日期: 2025-02-24
