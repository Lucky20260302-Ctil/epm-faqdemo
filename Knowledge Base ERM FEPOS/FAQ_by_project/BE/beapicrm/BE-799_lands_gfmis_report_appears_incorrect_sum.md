---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "GFMIS report appears incorrect sum of total price:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-799
resolved: 2023-09-07
fix-version: ""
---

# BE-799: [Lands] GFMIS report appears incorrect sum of total price

## 問題

GFMIS report appears incorrect sum of total price:
Total price of Receipt Details displayed as 10980.8
It seems sum by colunm of joinv_tot_amt_fx- 1372.6*8 = 10980.8, instead, joupay_pay_amt_fx- 872.6+100+200+200 = 1372.6
Seems purchased specific items causing the issue
Items pusrchased in this order:
PHOTOCGEODA3
PHOTOCSVY
PHOTOCSVYA3
PHOTOCSVYCOLOR
PHOTOCSVYLSO
PHOTOCSVYLSOA3
100001
233575

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-09-07
### Jira Comments (2 則)
**Sherman tse** (2023-09-07):
Verified on 172.16.138.55 QA
REF: RR_DCBBATCH_74_0001_20230907_verified.txt
**Sherman tse** (2023-09-07):
Verified on 10.77.227.28 UAT

## 相關資訊

- Jira: [BE-799](https://ctil.atlassian.net/browse/BE-799)
- Fix Version: 未記錄
- 解決日期: 2023-09-07
