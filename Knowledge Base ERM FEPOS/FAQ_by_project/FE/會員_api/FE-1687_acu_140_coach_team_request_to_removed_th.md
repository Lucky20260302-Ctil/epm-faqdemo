---
tags: [faq, fe, 會員_api]
component: "API"
symptom: "@@Anson Cheung @@Cy Lau  Coach Team request to removed the Email alert for the 'ERROR|CDP-CUST-404|C"
root-cause: "待提取"
solution: "### Jira Comments (10 則)"
jira: FE-1687
resolved: 
fix-version: ""
---

# FE-1687: [ACU-140] Coach Team request to removed the Email alert for the CRM return "ERROR|CDP-CUST-404|Customer not found"

## 問題

@@Anson Cheung @@Cy Lau  Coach Team request to removed the Email alert for the "ERROR|CDP-CUST-404|Customer not found",Please help to removed the Email alert for this section. If anything other question please ping me.Thanks!
CC @@Joy Li @@Bobby
Details workflow:
1.When user input Member code OCQA1TC00000085 in FE POS.
2.Then use member code call CRM API,
API url:/api/v1/acxiom/purchaseHistory,
Input data as bellow:
3.But CRM API return:
"ResponseCode": 200,
"result": "{"successful":false,"data":"ERROR|CDP-CUST-404|Customer not found"
4.Coach team request removed bellow Email alert of “200 Customer Not Found“.Because it is normal workflow.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (10 則)
**Cy Lau** (2025-05-08):
@@Anson Cheung  Please help to confirm the logic thanks
**Anson Cheung** (2025-05-08):
@@Tovi Wang email alert of 404 customer not found has been removed in BEAPI ver1.17.17 (build no. dd1948a1), also I cannot reproduce this case in my environment, can you please help to confirm the BEAPICRM version?
**Tovi Wang** (2025-05-08):
@@Anson Cheung
**Anson Cheung** (2025-05-08):
@@Tovi Wang this version does not include the changes, please update the program to latest version and test again.
**Tovi Wang** (2025-05-08):
@@Anson Cheung You mean update the BEAPI program to latest version,Right?
**Anson Cheung** (2025-05-08):
@@Tovi Wang update BEAPICRM
**Tovi Wang** (2025-05-08):
@@Joy Li @@Jason Wu@@Bobby  Could you help to this.How to update BEAPICRM?Thanks!
**Andrew_Au** (2025-06-05):
@@Tovi Wang @@pierre.shi Please update the ticket status
**Tovi Wang** (2025-09-04):
和Lein确认现在已经没有收到此类的Email alert.BEAPI ver1.17.17 (build no. dd1948a1) 已经发布到生产，fixed and closed.
**Automation for Jira** (2025-09-04):
Issue has been created since
Days since: 119
Week since : 17
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1687](https://ctil.atlassian.net/browse/FE-1687)
- Fix Version: 未記錄
- 解決日期: 未記錄
