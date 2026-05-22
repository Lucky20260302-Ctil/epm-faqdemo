---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "Currently Kate Spade SEA CRM sales registration interface, promotion code is not included in the JSO"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1034
resolved: 2025-05-12
fix-version: ""
---

# BE-1034: [CS-1359]SOW of KS SEA CRM Sales Registration Enhancement

## 問題

Currently Kate Spade SEA CRM sales registration interface, promotion code is not included in the JSON payload thus causing the issues of miscalculation for VIP upgrading in Loyalty system.
To overcome the issue, we need to enhance the Sales Registration Interface by including the promotion code in the payload sending to Memberson’s “Register Transaction” API. This change will be implemented on Kate Spade Singapore and Malaysia regions only.
Please refer to Teams Group: KS SEA CRM Memberson

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-12
### Jira Comments (4 則)
**Bobby** (2025-03-20):
Timeline:
SOW: 12/03 - 18/03
Sign Off: 19/03
Development: 20/03 - 25/03
QC Testing: 26/03 - 31/03
Release: 01/04
**Andrew_Au** (2025-03-20):
@@Sherman tse testing completed ?
**Bobby** (2025-03-20):
Please refer to Teams Group: KS SEA CRM Memberson for more information.
**Cy Lau** (2025-04-10):
[Bobby Chu: \\ds411\csms60\delivery\coach_ks\add_promotions_to_api_20250324](https://teams.microsoft.com/l/message/19:2c8053d0-c619-4c5c-8111-762831247516_b580a21e-c7da-4537-a574-fea9ee0bd55c@unq.gbl.spaces/1744277158975?context=%7B%22contextType%22%3A%22chat%22%7D)

## 相關資訊

- Jira: [BE-1034](https://ctil.atlassian.net/browse/BE-1034)
- Fix Version: 未記錄
- 解決日期: 2025-05-12
