---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "The issue of pre-scan VIP barcode before submitting eName registration , VIP date can not be queried"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1318
resolved: 2024-05-07
fix-version: ""
---

# FE-1318: HK eName follow up - pre-scan vip barcode before submit

## 問題

The issue of pre-scan VIP barcode before submitting eName registration , VIP date can not be queried during transaction.
For JP eName: query VIP when creating new VIP, it directly query from FE to BE and no data then.  When do payment in POS(this time registration submitted), and it will query again from FE to BE, then it can be queried VIP.
For HK eName: because of CBDT, it will first call ‘online member API’ from FE to CDP to check if any customer from region ‘11’, then check the privacy policy to decide whether this customer can be queried, and this query action will finally goes to BE and call only once.(this design is based on the VIP is already exist).  Then now, eName join,  for FE to query VIP, it still goes to call API to query VIP, but only query one time.  That’s why HK can not scan bar code before registration submitted.
Got solution from Sanyo, they will do enhancement on the program to add one more time API query after payment while printing.  In this case, there will be 2 conditions:
1. 
2. 
Have aligned with business that they will scan barcode or QR code only after eName registration is submitted, and currently for eName registration there is no impact to business.
HK will have EFT payment SOW, this enhancement plan to go with EFT payment deployment together .

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-05-07
### Jira Comments (1 則)
**Sang** (2023-11-30):
10. Enhance Coach DotNet Print Out Performance - re-get member name thru web api (KTS 220627 JIra [🔗](https://ctil.atlassian.net/browse/FE-1126#icft=FE-1126) & [🔗](https://ctil.atlassian.net/browse/FE-1318#icft=FE-1318), v750.04, 231130 v720.01R26A )
a. Only Coach (CompanyCode or prtCompany - start with 'COACH') use eName
b. Only customized region print out which show member Name need to re-get member name 2nd time if member's first name and last name is '-' or is ''      (Exclude Company 'COACHJP' and 'KS_JP')

## 相關資訊

- Jira: [FE-1318](https://ctil.atlassian.net/browse/FE-1318)
- Fix Version: 未記錄
- 解決日期: 2024-05-07
