---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "During v75 pilot for KR region, we found that .net OPOS not supporting Korean language, could you pl"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1658
resolved: 2025-05-30
fix-version: ""
---

# FE-1658: [CS-1387] .net OPOS not support Korean

## 問題

During v75 pilot for KR region, we found that .net OPOS not supporting Korean language, could you please help to check how could resolve it in the future release? thanks

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-30
### Jira Comments (6 則)
**Tovi Wang** (2025-03-24):
@@pierre.shi log拿到后帮忙贴到这里。Thanks!
CC @@Cy Lau @@Sang
**Cy Lau** (2025-03-25):
Hi all, for the tracing of RCA, with device of TM-T88IV
Brief:
The logic of printing a TMU :
v75
[CSPLUS](Create the printing content script) >[Microft Point of Service]>[[OPOS.net](http://OPOS.net)]>[PrinterFirmware]>[Printing]
v72
[CS2000](Create the printing content script) >[Microft Point of Service]>[OPOS ADK]>[PrinterFirmware]>[Printing]
v72 using 32bits of OPOS ADK (COM object wise) - OPOS ADK Version for KR
For [OPOS.net](http://OPOS.net) 64-bits (.Net wise)
CharacterSet '949' is specific for Korean.
---
SY Dev team after received the incidient ticket, performed as following :
1. 
Result : No specfic mentions about Korean handling
1. 
2. 
Result: Print still with ???
1. 
Result: PrinterError, Invalid Paramter(Would reason of rejected by [OPOS.net](http://OPOS.net)) .
---
Findings:
choosing TM-T88VII(WIth multi language front):
offers 949
Conclusion: Only those models with _MltFront allow choosing 949 for korean
*Japanese character has been mentioned in the release notes in **[OPOS.net](http://OPOS.net)*
Suggestions
1. 
2.
**pierre.shi** (2025-03-25):
Hi teams, below logs for your reference.
**Sang** (2025-05-05):
v750.04R13 uploaded to svn://sanyosvn.ctil.com/svn/SvnPepository/branches/PosNetFE/7.5.0.04
Compiled Program uploaded to \\ds411\share\POS_FE_Release_64\20250505 Coach v750.04R13
Sample DB & log uploaded to Jira FE-1658
1.
**Cy Lau** (2025-05-07):
** x32TMUPrint.exe set PosReportCenter.EnablePrintAgent = False Updated**
**Cy Lau** (2025-05-12):
X32TMUPrint.exe updates :
Scanning timeframe :
\\ds411\share\POS_FE_Release_64\20250512 Coach v750.04R13\PrintAgent
5mins:
<add key="FetchTimeFrame" value="300000" />

## 相關資訊

- Jira: [FE-1658](https://ctil.atlassian.net/browse/FE-1658)
- Fix Version: 未記錄
- 解決日期: 2025-05-30
