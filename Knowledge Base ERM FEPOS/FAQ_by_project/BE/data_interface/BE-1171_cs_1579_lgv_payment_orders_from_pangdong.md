---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "Upon request, modify the sales export interfaces to remove LGV payment amount ( sum(joupay_pay_amt_b"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1171
resolved: 2025-09-22
fix-version: ""
---

# BE-1171: [CS-1579]  LGV payment orders from PangdongLai API

## 問題

Upon request, modify the sales export interfaces to remove LGV payment amount ( sum(joupay_pay_amt_bx) where payment_code = 'LGV') in the export amount “c_amount” and “c_pay_type”.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-09-22
### Jira Comments (3 則)
**Cy Lau** (2025-08-29):
\\ds411\public\anson\Coach_Pangdonglai\Coach_Pangdonglai_v0.0.2_20250829
＋add config “excludeLGV“
+ calculate the LGV for exclusion
[http://172.16.138.42:3000/ERM/Coach_Pangdonglai](http://172.16.138.42:3000/ERM/Coach_Pangdonglai)
d98afd2
**Ken Wang** (2025-09-22):
QA passed and released to Coach on 10 Sep2025.
**Automation for Jira** (2025-09-22):
Issue has been created since
Days since: 23
Week since : 3
Issue due date difference
Days since : 17
Weeks since: 2

## 相關資訊

- Jira: [BE-1171](https://ctil.atlassian.net/browse/BE-1171)
- Fix Version: 未記錄
- 解決日期: 2025-09-22
