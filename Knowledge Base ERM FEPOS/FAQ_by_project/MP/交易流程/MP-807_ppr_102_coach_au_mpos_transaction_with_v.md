---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Neil callout during testing we found that if MPOS transaction with member without transaction before"
root-cause: "待提取"
solution: "### Jira Comments (3 則)"
jira: MP-807
resolved: 
fix-version: ""
---

# MP-807: [PPR-102] Coach AU MPOS Transaction with VIP post to DB failed

## 問題

Neil callout during testing we found that if MPOS transaction with member without transaction before, then posted DB failed. Testing machine IP: 10.34.103.18(OCFA218 till 0), transaction no#: MA000004, testing VIP no#: 2035535201. MPOS UI log was uploaded to apawiqwposweb24. Kindly help to check, thanks!

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (3 則)
**Cy Lau** (2026-01-09):
After first investigation, the API log doesn’t indicate completetransaction 
Log contains :
Search member from C360 member
certain calcWithMMCoupon at paymentmethod controller.
@@Joy Li  we do need MPOS app log to see when and how the transaction completed at
**Automation for Jira** (2026-01-19):
Issue has been created since
Days since: 11
Week since : 1
Issue due date difference
Days since : 
Weeks since:
**Cy Lau** (2026-01-19):
It is owing to members ain’t being created before the transaction completed by PCD 34 , FEPOS has acomplished the enhancement.
MPOS would follow the enhancement for
1. 
2. 
DEV schedule :
[🔗](https://ctil.atlassian.net/browse/MP-808)

## 相關資訊

- Jira: [MP-807](https://ctil.atlassian.net/browse/MP-807)
- Fix Version: 未記錄
- 解決日期: 未記錄
