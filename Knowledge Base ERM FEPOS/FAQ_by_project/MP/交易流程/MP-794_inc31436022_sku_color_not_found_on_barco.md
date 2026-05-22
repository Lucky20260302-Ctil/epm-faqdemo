---
tags: [faq, mp, 交易流程]
component: "Frontend"
symptom: "[INC3143602]SG region,OC554 POS v75,2 SKU Color Not Found on Barcode print"
root-cause: "待提取"
solution: "### Jira Comments (15 則)"
jira: MP-794
resolved: 
fix-version: ""
---

# MP-794: [INC3143602]2 SKU Color Not Found on Barcode print

## 問題

[INC3143602]SG region,OC554 POS v75,2 SKU Color Not Found on Barcode print
CY200 B4/N4
CI032 B4/N4
can be found in DB and BE, but FE still cannot find these color
OCF61till1 can use normally, compare the two item in dbmas, it looks like the same.
I remoted to store and check the two item in barcode print mode and can’t find
below are the logs:

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (15 則)
**pierre.shi** (2025-08-21):
Hi @@Joy Li item search from fe, can find the col b4/n4
but cannot find in barcode printing
**Sang** (2025-08-25):
@@pierre.shi @@Joy Li  Please check is SKU available in FE dbmas.tblitmean table
**Sang** (2025-08-25):
@@pierre.shi Please copy back dbmas.mdf
**Joy Li** (2025-08-25):
@@Sang Yes. the item can be select in FE with EAN code
**pierre.shi** (2025-08-26):
@@Sang please help to confirm whether you need dbmas.bak or dbmas.mdf
I checked in POS folder, no dbmas.mdf found.
**pierre.shi** (2025-08-27):
Hi @@Sang ,as the attachment size limitted in Jira ticket, dbmas has been uploaded into onedrive. [OC5542.zip](https://ctil00046-my.sharepoint.com/:u:/g/personal/jason_wu_ctil00046_onmicrosoft_com/EdHMxPM_JRJPq-SdwvDFf6gBX_GyihCSau841DOpHaaXBg?e=BFEnYb)
please help to check.
**pierre.shi** (2025-08-28):
Hi@@Sang  have we got any progress?
**Sang** (2025-08-28):
@@pierre.shi Please send me the link to get dbmas
**pierre.shi** (2025-08-28):
@@Sang this is a superlink of dbmas. can you open it?
**Sang** (2025-08-28):
@@pierre.shi please resend this link to me
**Sang** (2025-08-28):
@@Sang Got dbmas.bak from link. Thanks.
**Sang** (2025-08-28):
@@pierre.shi @@Joy Li @@Cy Lau @@Bobby
Item ‘CY200’ has color w/o Size. Color/Size should has a record in tblcolsiz, is no size then colsiz_siz=''. I can find colsize_col='BE/NE' and ‘Colsiz_siz’='' in other SG dbmas database but is is not exist in OC554 dbmas. Please update FE tblcolSiz table (Zupdate record ‘03’).
**Sang** (2025-08-28):
@@pierre.shi @@Joy Li @@Cy Lau @@Bobby
1. 
Program uploaded to \\ds411\share\POS_FE_Release_64\20250828 Label Printing v750.04R14
**Automation for Jira** (2025-10-08):
Issue has been created since
Days since: 49
Week since : 7
Issue due date difference
Days since : 
Weeks since:
**Andrew_Au** (2025-10-08):
@@Sherman tse Please confime the current status

## 相關資訊

- Jira: [MP-794](https://ctil.atlassian.net/browse/MP-794)
- Fix Version: 未記錄
- 解決日期: 未記錄
