---
tags: [faq, fe, 會員_api]
component: "API"
symptom: "we're doing testing for CJ eReceipt enhancement, encounter below error message, could you please hel"
root-cause: "待提取"
solution: "### Jira Comments (14 則)"
jira: FE-1670
resolved: 
fix-version: ""
---

# FE-1670: [CS-1403] Unable to send eReceipt - JP CS2K v75.004.1200.0001

## 問題

we're doing testing for CJ eReceipt enhancement, encounter below error message, could you please help to check?
Testing machine IP:172.24.253.20(J805), BE patch already deploy to apawiqwposweb21 & apawiqwposweb22.
1.
2.WA log response error:
```
Response:<!DOCTYPE html>
<html lang="en-US" xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta charset="utf-8" />
        <title> HTTP Error 500.31 - Failed to load ASP.NET Core runtime </title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Arial, Helvetica, sans-serif;
                font-size: .813em;
                color: #222;
                background-color: #fff;
            }
            h1, h2, h3, h4, h5 {
                /*font-family: 'Segoe UI',Tahoma,Arial,Helvetica,sans-serif;*/
                font-weight: 100;
            }
            h1 {
                color: #44525e;
                margin: 15px 0 15px 0;
            }
            h2 {
                margin: 10px 5px 0 0;
            }
            h3 {
                color: #363636;
                margin: 5px 5px 0 0;
            }
            code {
                font-family: Consolas, "Courier New", courier, monospace;
            }
            body .titleerror {
                padding: 3px 3px 6px 3px;
                display: block;
                font-size: 1.5em;
                font-weight: 100;
            }
            a {
                color: #1ba1e2;
                text-decoration: none;
            }
                a:hover {
                    color: #13709e;
                    text-decoration: underline;
                }
            li {
                margin: 5px;
            }
        </style>
    </head>
    <body>
        <h1> HTTP Error 500.31 - Failed to load ASP.NET Core runtime </h1>
        <h2> Common solutions to this issue: </h2>The specified version of Microsoft.NetCore.App or Microsoft.AspNetCore.App was not found.
        <h2> Troubleshooting steps: </h2>
        <ul>
            <li> Check the system event log for error messages </li>
            <li> Enable logging the application process' stdout messages </li>
            <li> Attach a debugger to the application process and inspect </li>
        </ul>
        <h2>
            For more information visit:
             <a href="https://go.microsoft.com/fwlink/?LinkID=2028526"> <cite> https://go.microsoft.com/fwlink/?LinkID=2028526 </cite> </a>
        </h2>
    </body>
</html>
```
3.BEAPI appsettings.json config setting for your reference:

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (14 則)
**Tovi Wang** (2025-04-17):
@@Cy Lau Log details for your further checking.Thanks!
**Cy Lau** (2025-04-22):
@@Anson Cheung  I do believe it would be the IIS setting issue or .net core installation missing,
Please help to align the requirements
**Anson Cheung** (2025-04-22):
@@Tovi WangeReceiptRestfulService is using .net 8, please install the .net hosting bundle in \\ds411\public\anson\eReceiptRestfulService
**Tovi Wang** (2025-04-22):
@@Anson Cheung How do I access \\ds411\public\anson\eReceiptRestfulService?
Could you directly share the .net hosting bundle to me and advice next action?
**Anson Cheung** (2025-04-22):
@@Tovi Wang   install it in both 21 22 web server and restart the application pool
**Joy Li** (2025-04-23):
@@Cy Lau  @@Anson Cheung
For Local IIS package update, only file replace. No program install.
May I confirm if you need all local IIS till 0 install .net 8 ?
Need to discuss how to deploy.
**Cy Lau** (2025-05-16):
Update testing at 16:18
**Cy Lau** (2025-05-16):
But seems the log showing …old flow ????
**Cy Lau** (2025-05-16):
After checking , 
From FEPOS → BEAPI (passed)
BEAPI handles request (passed)
BEAPI calls eReceiptRestfulservice (failed as 404 )
Config is not aligned with deployment :
**Cy Lau** (2025-05-16):
And please also align the FEPOS version
@@Joy Li  @@Tovi Wang
172.24.253.20
**Tovi Wang** (2025-08-29):
Still under align with Coach QA.Please hold on.
**Andrew_Au** (2025-09-30):
@@Tovi Wang This ticket pending for a long time. Please update the ticket status
**Tovi Wang** (2025-09-30):
Testing passed.Waiting deployment.Please closed.
**Automation for Jira** (2025-09-30):
Issue has been created since
Days since: 165
Week since : 23
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1670](https://ctil.atlassian.net/browse/FE-1670)
- Fix Version: 未記錄
- 解決日期: 未記錄
