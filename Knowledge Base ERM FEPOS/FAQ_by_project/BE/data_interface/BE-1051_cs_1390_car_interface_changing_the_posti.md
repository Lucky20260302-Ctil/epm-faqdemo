---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "Currently, CAR Interface file, the posting date time is using the server time which is HKT. Tapestry"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1051
resolved: 2025-05-12
fix-version: ""
---

# BE-1051: [CS-1390] CAR Interface Changing the posting date time to transaction hour-min

## 問題

Currently, CAR Interface file, the posting date time is using the server time which is HKT. Tapestry would like to get the regional date time especially for JP and KR since they have 1 hour advance to HKT. The solution is to put the transaction date and time to the posting date & time fields.
Changing the posting date time to **transaction hour-min**
P|J801|00207838|20250223|D|1|196395660940|CY698|IMXXA|||01|3|1|0.00|JXXXX0003641186|<span style="color:#ff5630">**20250223|hhmm00**</span>
a) hh = jouinv_hour, joudep_hour, jouser_hh, jougic_hour
b) mm = jouinv_mn, joudep_mn, jouser_mn, jougic_min
c) date = jouinv_date, joudep_date, jouser_date, jougic_date
The change will apply to Sales Memo - Item Layout, Sales Memo - Item Discount Layout, Payment Detail Layout, Deposit Memo - Item Layout, Service Memo - Item Layout, Gift Cert Memo - Header Layout.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-12
### Jira Comments (5 則)
**Ken Wang** (2025-04-11):
attached the 1st Draft of SOW - Q2025-xxx-ERM- Coach JP&KR- SOW of Enhancement of changing CAR Interface posting datetime to transaction datetime v1.0.docx
for review.
**Cy Lau** (2025-04-22):
Additional requirement on 21-Apr :
# yes, we confirmed reportinig team.  based on their request, **we want to applythis change to COH Japan, COH KR and Kate JP.**
# **so we want to have setting in BE side for enable/disable this change.**
CAR_Trx_AS_PostingDatetime = Y
**Cy Lau** (2025-04-28):
2025/04/24
Dear all,
Release:
<u>[\\ds411\csms60\delivery\coach\CAR.2024-04-24](file://ds411/csms60/delivery/coach/CAR.2024-04-24)</u>
Note:
- 
- 
Source:
svn://sanyosvn.ctil.com/svn/cs2000/Trunk/BackEnd.Net(VS2017 FW 4.5.2 NEW)/Coach_CAR
Regards,
Jerry
**Sherman tse** (2025-04-29):
Verifeid on QA
test caes attached
**Joy Li** (2025-07-04):
released on 2025-04-29 with BE V70R3.102

## 相關資訊

- Jira: [BE-1051](https://ctil.atlassian.net/browse/BE-1051)
- Fix Version: 未記錄
- 解決日期: 2025-05-12
