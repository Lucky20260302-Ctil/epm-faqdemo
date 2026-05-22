---
project: FE
title: "FE-1658: [CS-1387] .net OPOS not support Korean"
issue_key: FE-1658
issue_type: Bug PRD
status: Closed
faq_score: 6.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1658"
created: 2025-03-24
resolved: 2025-05-30
resolution: Done
has_images: True
---

# FE-1658: [CS-1387] .net OPOS not support Korean

## 問題描述

During v75 pilot for KR region, we found that .net OPOS not supporting Korean language, could you please help to check how could resolve it in the future release? thanks 

> 📎 **image-20250324-170639.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f5ef71ab-4fb9-426d-b73f-077f02710e6f)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250324-170639.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f5ef71ab-4fb9-426d-b73f-077f02710e6f)


## Jira Comments

> **Tovi Wang** (2025-03-24):
>  log拿到后帮忙贴到这里。Thanks! CC     

> **Cy Lau** (2025-03-25):
> Hi all, for the tracing of RCA, with device of TM-T88IV Brief: The logic of printing a TMU : v75 [CSPLUS](Create the printing content script) >[Microft Point of Service]>[ OPOS.net ]>[PrinterFirmware]>[Printing] v72 [CS2000](Create the printing content script) >[Microft Point of Service]>[OPOS ADK]>[PrinterFirmware]>[Printing] v72 using 32bits of OPOS ADK (COM object wise) - OPOS ADK Version for KR For  OPOS.net  64-bits (.Net wise) CharacterSet '949' is specific for Korean. SY Dev team after received the incidient ticket, performed as following : Check release notes of OPOS .net Result : No specfic mentions about Korean handling Comparing the Release notes of OPOS ADK and OPOS .net Results : Mentioned about Korean handling with setting 949 and supported Devices Try to hijack with Configur

> **pierre.shi** (2025-03-25):
> Hi teams, below logs for your reference.

> **Sang** (2025-05-05):
> v750.04R13 uploaded to svn://sanyosvn.ctil.com/svn/SvnPepository/branches/PosNetFE/7.5.0.04 Compiled Program uploaded to \\ds411\share\POS_FE_Release_64\20250505 Coach v750.04R13 Sample DB & log uploaded to Jira FE-1658 Add PrintAgent to use X86 X32TMUPrint.exe (KTS 250505 Jira FE-1658 v750.04R13, v750.05)  a. PosReportCenter - Add Support PrintAgent  b. Add PrintAgent Class + SanyoPos.PrintAgent.dll (Refactor from x32TMUPrint Project) - Need System.Data.SQLite.dll (DB ver 3) + SQLite.Interop.dll (v1.0.117 x64)  c. add PrintAgent Log (retData6\PAyymmdd.dat) - HouseKeeping  d. add tblconfig.EnablePrintAgent  'Y' - use x32TMUPrint.exe 32bit program call TMU Driver to Print TMU Receipt/Report  	- POS Startup auto call x32TMUPrint.exe  	- need deploy to ProgramFolder\PrintAgent\x32TMUPrint.exe

> **Cy Lau** (2025-05-07):
>  x32TMUPrint.exe set PosReportCenter.EnablePrintAgent = False Updated

> **Cy Lau** (2025-05-12):
> X32TMUPrint.exe updates : Scanning timeframe : \\ds411\share\POS_FE_Release_64\20250512 Coach v750.04R13\PrintAgent 5mins: <add key="FetchTimeFrame" value="300000" /> 

## 相關資訊

- **Jira:** [FE-1658](https://ctil.atlassian.net/browse/FE-1658)
- **解決方式:** Done