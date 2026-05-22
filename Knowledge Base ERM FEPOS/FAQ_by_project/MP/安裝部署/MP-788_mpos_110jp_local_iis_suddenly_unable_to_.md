---
tags: [faq, mp, 安裝部署]
component: "LocalIIS, MPOS"
symptom: "When Coach QA did testing in QA for JP Local IIS, it will pop-up below error message after scan the "
root-cause: "待提取"
solution: "### Jira Comments (15 則)"
jira: MP-788
resolved: 
fix-version: ""
---

# MP-788: 【MPOS-110】JP Local IIS suddenly unable to Use

## 問題

When Coach QA did testing in QA for JP Local IIS, it will pop-up below error message after scan the QR code, could you please help to check? I've tried v3.29.5 and v3.30.3 both get this error message.
Testing machine IP: 172.24.253.16

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (15 則)
**Tovi Wang** (2025-07-30):
@@Cy Lau @@Daniel LeungFollow MPOS log for your further checking.If need other logs please let me know.
CC @@Joy Li
**Automation for Jira** (2025-07-30):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Daniel Leung** (2025-07-30):
Can you also upload the UI log please? @@Tovi Wang
**Cy Lau** (2025-07-30):
It is reported by Dev Team @@Daniel Leung  that the ApiModule hasn’t been changed and no handling for bypass the SSL error
Please help to verify the SSL settings and SSL cert for that testing machine.
@@Joy Li  @@Tovi Wang
**Cy Lau** (2025-07-30):
@@Daniel Leung there would be no UI log, since the connection cannot be established
the ui log cannot be uploaded.
**Tovi Wang** (2025-07-30):
@@Cy Lau Local IIS logs.
Log path: C:\inetpub\logs\LogFiles\W3SVC1
**Cy Lau** (2025-07-30):
@@Tovi Wang  would be mind checking the dbTrans config ? 
when it is working , it is using port80 which is http
**Tovi Wang** (2025-07-30):
@@Cy Lau Let me double check and compare the dbtrans config.Thanks!
**Tovi Wang** (2025-07-30):
@@Cy Lau 我和之前的dbtrans config setting 对比发现 SALESHUBPORT setting之前是 8080 现在是 9001.所以这个config setting正常应该是什么值呀？
**Cy Lau** (2025-07-30):
@@Tovi Wang 先不管saleshub
**Cy Lau** (2025-07-30):
with the QR Code, the mpos connection settings as below:
{"LOC":"J406","IP":"172.24.253.16","TILL":"0","DESC":"Yokkaichi Kintetsu", "ISSECURE":"True","PORT":"80","DATASERVERIP":"172.24.253.16","RegionCode":"18","LocalSalesHubEncryptionKey":"G4Emd115kDrwJAGR"}
**Daniel Leung** (2025-07-30):
Coach QA setting QR Code: 
{"LOC":"J406","IP":"172.24.253.16","TILL":"0","DESC":"Yokkaichi Kintetsu", "ISSECURE":"True","PORT":"80","DATASERVERIP":"172.24.253.16","RegionCode":"18","LocalSalesHubEncryptionKey":"G4Emd115kDrwJAGR"}
our testing env qr code:
{"LOC":"C318","IP":"[HTTPS://172.16.138.7/SANYOSERVICE.API.FE_38","TILL":"0","DESC":"O.K.Sanda"](HTTPS://172.16.138.7/SANYOSERVICE.API.FE_38%22,%22TILL%22:%220%22,%22DESC%22:%22O.K.Sanda%22), "ISSECURE":"True","PORT":"443","DATASERVERIP":"172.16.138.34","RegionCode":"38"}
The IP part is different. 
If NO http at the beginning of IP, MPOS will auto add https/http at the front depends on ISSECURE (true will add https, false will add http).
If no ‘sanyoservice.api’ part in IP , MPOS will also add the port after the IP.
So in this case, https is used but the link refer to 80 port. And this will cause the problem. 
 @@Tovi WangPlease try set MOBILESERVERISSECURE to N, and please check 80 port is available.
**Cy Lau** (2025-07-30):
@@Daniel Leung please update ur findings
**Tovi Wang** (2025-07-30):
@@Daniel Leung @@Cy Lau  Many Thanks for your details update.
I has set MOBILESERVERISSECURE config setting from Y to N.Let Nei rescan the MPS QR code to double confirm the error gone or not.
**Tovi Wang** (2025-07-30):
@@Cy Lau @@Daniel Leung  Neil double confirmed issue fixed after set the config to N.

## 相關資訊

- Jira: [MP-788](https://ctil.atlassian.net/browse/MP-788)
- Fix Version: 未記錄
- 解決日期: 未記錄
