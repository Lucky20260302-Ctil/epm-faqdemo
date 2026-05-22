---
project: BE
title: "BE-761: ChainStorePlus - (Prorunner disk full)"
issue_key: BE-761
issue_type: Task
status: Closed
faq_score: 4.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-761"
created: 2023-06-14
resolved: 2023-09-19
resolution: Done
has_images: True
---

# BE-761: ChainStorePlus - (Prorunner disk full)

## 問題描述

log.sqlite  file over 50 GB size (delete file on 2023-06-14)

 

 

- Suggest add housekeeping logic in appsettings.json like as csplus web enquiry application.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d6b3a92c-cdd0-4b36-8ad2-4ae56a1b74ae)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d6b3a92c-cdd0-4b36-8ad2-4ae56a1b74ae)


## Jira Comments

> **Hans Wong** (2023-07-28):
> Added branch on gitlab named  Change-to-Serilog  for switching project to new log library, with rollover capability on size and daily. with compress and backup program, this issue should be solved. [\\ds411\csms70\delivery\CompressBackup]  

> **Hans Wong** (2023-08-02):
> Please use the latest CSBN_API which is merged with  Change-to-Serilog  to produce the new branch  LandsDev-With-Serilog-Update \\ds411\csms70\delivery\lands\UAT\Backend (Web)\2023-08-01 ChainStorePlus-v1.5-2023-08-01.zip  

> **Hans Wong** (2023-08-02):
> Please test the new API   

> **Hans Wong** (2023-08-02):
> sample powershell script to delete files older than 2 years   $limit = (Get-Date).AddYears(-2)
> $path = "C:\Path\To\Folder"
> Get-ChildItem -Path $path -Recurse | Where-Object { !$_.PSIsContainer -and $_.CreationTime -lt $limit } | Remove-Item   You can use the Windows Task Scheduler to run a PowerShell script on a schedule. Here are the steps to schedule a PowerShell script using the Task Scheduler: Open the Task Scheduler by searching for it in the Start menu. Click on the “Create Basic Task” option on the right panel. Follow the wizard to name your task and select when you want it to run. When prompted for the action, select “Start a program”. In the “Program/script” field, enter  powershell.exe . In the “Add arguments” field, enter  -File "C:\Path\To\YourScript.ps1" , replacing  C:\Path

> **Hans Wong** (2023-08-02):
> CompressBackup Config file: This config describes, the program will process files from each location in LoadSettings at SourcePath and backup to TargetPath. The program will pack files within 1 month into same zip. The program will backup files more than 2 months old. log-path is the program's own log path. LoadSettings can accept multiple entries to process multiple destinations.

> **Andrew_Au** (2023-09-19):
>   Tested the compress program is working normal.  I used the dos batch file to purge the files, insteat of use power shell script.

## 相關資訊

- **Jira:** [BE-761](https://ctil.atlassian.net/browse/BE-761)
- **解決方式:** Done