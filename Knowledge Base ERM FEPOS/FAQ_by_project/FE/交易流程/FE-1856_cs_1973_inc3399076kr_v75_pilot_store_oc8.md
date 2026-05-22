---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "KR store callout that After upgrading to V75, some parts become Japanese and English."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1856
resolved: 2026-02-26
fix-version: ""
---

# FE-1856: [CS-1973] INC3399076,KR V75 pilot store  OC825 CS2000  UI daiplay issue 

## 問題

KR store callout that After upgrading to V75, some parts become Japanese and English.
Confirmed with two other pilot stores OC807 and OC860 that they also have the same issues.
Normal all should display as Korean.
@@Sang @@Cy Lau @@Joy Li I suspect it's a problem with the language pack file settings.Please help to further checking and confirming the language pack file.
Troubleshooting:
1.repaired cs2000 program,issue still.
2.change windows system language from 'English' to  'Korean.'Issue still.
1. 
2.会员页面显示英文 Purchase History，应该显示韩文。
LL coupon notes can only input English after upgrade (previously supported Korean).
COACH say 72 can support Korean. but V75 fail (75.004.1404.0000)
Could you please help to check and confirm?

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-02-26
### Jira Comments (6 則)
**Sang** (2026-01-19):
@@Tovi Wang @@Joy Li @@Cy Lau Need to update KR language package. To be update in next release
**Automation for Jira** (2026-01-20):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2026-01-26):
Fixed in v750.04R21
**Tovi Wang** (2026-01-26):
@@Sang Thanks!
@@Joy Li Please help to arrange the released ETA.
**Joy Li** (2026-02-05):
@@Sang LL coupon notes can only input English after upgrade (previously supported Korean).
COACH say 72 can support Korean. but V75 fail (75.004.1404.0000)
Could you please help to check and confirm?
**Sang** (2026-02-05):
Dear Joy,
KR 75.004.1404.0000 mapped to v750.04R14D.  Please confirm hot fix [🔗](https://ctil.atlassian.net/browse/FE-1856#icft=FE-1856) apply to which version R14E, R14G ?
v750.04R14D
1. Print DayEnd (Laser) - Simplified Chinese Font Setting fixed (KTS 251002 [🔗](https://ctil.atlassian.net/browse/FE-1761#icft=FE-1761) v750.04R14D, v750.05)
2. Process consolidated day end before sub till complete day end, POS fail to alert missing till message fixed, add log (KTS 251006 [🔗](https://ctil.atlassian.net/browse/FE-1766#icft=FE-1766) v750.04R14D, v750.05)
[20251006 12:10:35 -0511]: The day-end file cannot be found from the following sub-tills, tills number are [ 1 ]. Do you want to continue with consolidated report?
3. Enhance Day End backup/copy Dbtrans (CYL 251008 [🔗](https://ctil.atlassian.net/browse/FE-1766#icft=FE-1766) v750.04R14D, v750.05
a) RemoveFile - adding 30s timeout to check the exist
b CopyFile - adding 120s with checking exist, length and checksum
c) BackupTillData - adding log and exceptions
'-------
v750.04R14E
1. Add DBVer 007.001.003.074A (MPOS) - Ext dbtrans.MDF tblSysconfig_Bak,tblConfig.config_value to 400 nchar - override 007.001.003.063B (KTS 251020 [🔗](https://ctil.atlassian.net/browse/MP-802#icft=MP-802) v750.04R14E, v750.05)
v750.04R14F
1. Support Coach AU/NZ region (tblconfig.PrtCompany='COACHANZ') Tax Exempted TMU Print Out (KTS 251104 [🔗](https://ctil.atlassian.net/browse/FE-1770#icft=FE-1770) v750.04R14F, v750.05)
2. Coach ANZ Allow Tax Free Shop Operation  (loctab_tax_exempt='Y') - Default Tax Free Mode (add tblconfig.AutoTaxFreeMode ='Y') (KTS 251104 [🔗](https://ctil.atlassian.net/browse/FE-1785#icft=FE-1785) v750.04R14F, v750.05)
v750.04R14G
1. Zupdate Itmast (01) - add UE Message of not include Brand item (tblconfig.itemBrand) (KTS 251105 [🔗](https://ctil.atlassian.net/browse/FE-1793#icft=FE-1793) v750.04R14G, v750.05R03)
KO, Tin Sang | Team Head, ChainStorePlus ERM
Sanyo Extended System Services Limited
Subsidiary of Computer And Technologies Holdings Limited (SEHK: 46)
T (852) 25038166
F (852) 25038100
18th Floor of Viva Place, No.36 Heung Yip Road, Wong Chuk Hang, Hong Kong
www.chainstoreplus.com<[https://apc01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.chainstoreplus.com%2F&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261580752&sdata=zDB%2BRdRUJo17qjnWxP8lRLkjllcd35JyPb6wdydJqsY%3D&reserved=0](https://apc01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.chainstoreplus.com%2F&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261580752&sdata=zDB%2BRdRUJo17qjnWxP8lRLkjllcd35JyPb6wdydJqsY%3D&reserved=0)> | www.ctil.com<[https://apc01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.ctil.com%2F&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261590747&sdata=%2FrJQdKNdgCvFrPIvS6KJhy%2B80x4FZPsIiznDxQNz2s4%3D&reserved=0](https://apc01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.ctil.com%2F&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261590747&sdata=%2FrJQdKNdgCvFrPIvS6KJhy%2B80x4FZPsIiznDxQNz2s4%3D&reserved=0)>
LinkedIn<[https://apc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Fcomputer-and-technologies-holdings-limited%2F&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261590747&sdata=fcQNHiV5C5%2BK10lTfONu1UGgXF9IRbZKe8VHxRjVf5o%3D&reserved=0](https://apc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Fcomputer-and-technologies-holdings-limited%2F&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261590747&sdata=fcQNHiV5C5%2BK10lTfONu1UGgXF9IRbZKe8VHxRjVf5o%3D&reserved=0)> | Twitter<[https://apc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Ftwitter.com%2FCNT00046&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261600740&sdata=XX7SXxctAEr4mxkyG8b3%2BNfhr5i8X44Et0uNmldb53U%3D&reserved=0](https://apc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Ftwitter.com%2FCNT00046&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261600740&sdata=XX7SXxctAEr4mxkyG8b3%2BNfhr5i8X44Et0uNmldb53U%3D&reserved=0)> | WeChat<[https://apc01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.ctil.com%2Fsites%2Fdefault%2Ffiles%2FwechatQR.jpg&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261600740&sdata=mBK8VOXzwob1g1F7F10KuqlFfXqT7hEe3gAhIi5r8NU%3D&reserved=0](https://apc01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.ctil.com%2Fsites%2Fdefault%2Ffiles%2FwechatQR.jpg&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261600740&sdata=mBK8VOXzwob1g1F7F10KuqlFfXqT7hEe3gAhIi5r8NU%3D&reserved=0)> | YouTube<[https://apc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.youtube.com%2Fchannel%2FUCFQgmjIFRyNRwNhJ0cnmHQg%2Ffeatured&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261610736&sdata=aCP6S6g8BJkCvvPS0p4HXe%2BDdwjEo8HmqXaiaJasrwk%3D&reserved=0](https://apc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.youtube.com%2Fchannel%2FUCFQgmjIFRyNRwNhJ0cnmHQg%2Ffeatured&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261610736&sdata=aCP6S6g8BJkCvvPS0p4HXe%2BDdwjEo8HmqXaiaJasrwk%3D&reserved=0)>
#10Years+CaringCompany #HKGreenOrg #PartnerEmployer

## 相關資訊

- Jira: [FE-1856](https://ctil.atlassian.net/browse/FE-1856)
- Fix Version: 未記錄
- 解決日期: 2026-02-26
