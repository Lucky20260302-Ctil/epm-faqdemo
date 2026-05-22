---
tags: [faq, fe, 列印]
component: "report"
symptom: "Symptom:"
root-cause: "待提取"
solution: "### Jira Comments (8 則)"
jira: FE-1850
resolved: 
fix-version: ""
---

# FE-1850: INC3381142 Till 0 Dayend Report Format Issue

## 問題

Symptom:
Till 0 Dayend Report Issue
Troubleshooting:
1. 
2. 
3. 
1.@@Sang 查到Till0 的RP file一共有74行，留白了9行。Till1 的RP file一共有65行，留白了6行。
请查看确认为什么till0 留白比till1 留白多了3行？
CC @@Joy Li @@pierre.shi FYI.
2.Till1 的RP file一共有65行，留白了6行。
3.
till0 POS version:75.004.1305.0001
till1 POS version:75.004.1100.0010

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (8 則)
**Tovi Wang** (2026-01-09):
@@Sang RP file here.
**pierre.shi** (2026-01-09):
Hi @@Joy Li @@Tovi Wang  below copy is from OC198, have the same pos version.
**Automation for Jira** (2026-01-12):
Issue has been created since
Days since: 2
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2026-01-12):
@@Tovi Wang @@Joy Li  Please verify Coach CN need to enable service module or not
OC198 disable service module ,
OC287 enable service module
**pierre.shi** (2026-01-12):
Hi @@Sang  Please help to provide the xconfig enable/disable the module on the report.
**Sang** (2026-01-12):
Dear Pierre,
Set syscon_alter_mod=0 to disable service module
KO, Tin Sang | Team Head, ChainStorePlus ERM
Sanyo Extended System Services Limited
Subsidiary of Computer And Technologies Holdings Limited (SEHK: 46)
T (852) 25038166
F (852) 25038100
18th Floor of Viva Place, No.36 Heung Yip Road, Wong Chuk Hang, Hong Kong
www.chainstoreplus.com<[https://apc01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.chainstoreplus.com%2F&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261580752&sdata=zDB%2BRdRUJo17qjnWxP8lRLkjllcd35JyPb6wdydJqsY%3D&reserved=0](https://apc01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.chainstoreplus.com%2F&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261580752&sdata=zDB%2BRdRUJo17qjnWxP8lRLkjllcd35JyPb6wdydJqsY%3D&reserved=0)> | www.ctil.com<[https://apc01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.ctil.com%2F&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261590747&sdata=%2FrJQdKNdgCvFrPIvS6KJhy%2B80x4FZPsIiznDxQNz2s4%3D&reserved=0](https://apc01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.ctil.com%2F&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261590747&sdata=%2FrJQdKNdgCvFrPIvS6KJhy%2B80x4FZPsIiznDxQNz2s4%3D&reserved=0)>
LinkedIn<[https://apc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Fcomputer-and-technologies-holdings-limited%2F&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261590747&sdata=fcQNHiV5C5%2BK10lTfONu1UGgXF9IRbZKe8VHxRjVf5o%3D&reserved=0](https://apc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Fcomputer-and-technologies-holdings-limited%2F&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261590747&sdata=fcQNHiV5C5%2BK10lTfONu1UGgXF9IRbZKe8VHxRjVf5o%3D&reserved=0)> | Twitter<[https://apc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Ftwitter.com%2FCNT00046&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261600740&sdata=XX7SXxctAEr4mxkyG8b3%2BNfhr5i8X44Et0uNmldb53U%3D&reserved=0](https://apc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Ftwitter.com%2FCNT00046&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261600740&sdata=XX7SXxctAEr4mxkyG8b3%2BNfhr5i8X44Et0uNmldb53U%3D&reserved=0)> | WeChat<[https://apc01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.ctil.com%2Fsites%2Fdefault%2Ffiles%2FwechatQR.jpg&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261600740&sdata=mBK8VOXzwob1g1F7F10KuqlFfXqT7hEe3gAhIi5r8NU%3D&reserved=0](https://apc01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.ctil.com%2Fsites%2Fdefault%2Ffiles%2FwechatQR.jpg&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261600740&sdata=mBK8VOXzwob1g1F7F10KuqlFfXqT7hEe3gAhIi5r8NU%3D&reserved=0)> | YouTube<[https://apc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.youtube.com%2Fchannel%2FUCFQgmjIFRyNRwNhJ0cnmHQg%2Ffeatured&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261610736&sdata=aCP6S6g8BJkCvvPS0p4HXe%2BDdwjEo8HmqXaiaJasrwk%3D&reserved=0](https://apc01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.youtube.com%2Fchannel%2FUCFQgmjIFRyNRwNhJ0cnmHQg%2Ffeatured&data=02%7C01%7Ctomchong%40imaginex.com%7Cb9513a009aa24fc7874108d810ce00d1%7C23f77f7405c140e1940be17f2c5cd3b8%7C1%7C0%7C637277824261610736&sdata=aCP6S6g8BJkCvvPS0p4HXe%2BDdwjEo8HmqXaiaJasrwk%3D&reserved=0)>
#10Years+CaringCompany #HKGreenOrg #PartnerEmployer
**Tovi Wang** (2026-01-16):
Disable the service section,issue fixed.
**Tovi Wang** (2026-01-21):
Import up xconfig,issue fixed.

## 相關資訊

- Jira: [FE-1850](https://ctil.atlassian.net/browse/FE-1850)
- Fix Version: 未記錄
- 解決日期: 未記錄
