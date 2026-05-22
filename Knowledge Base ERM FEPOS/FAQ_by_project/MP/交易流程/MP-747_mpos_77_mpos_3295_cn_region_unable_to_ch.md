---
tags: [faq, mp, 交易流程]
component: "Frontend"
symptom: "@@Daniel Leung @@Cy Lau  This is the Jira [MPOS-77] issue.Let us follow the issue in this internal J"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-747
resolved: 2025-05-02
fix-version: ""
---

# MP-747: [MPOS-77] MPOS 3.29.5 - CN Region, unable to check the purchase history for CRM Member

## 問題

@@Daniel Leung @@Cy Lau  This is the Jira [MPOS-77] issue.Let us follow the issue in this internal Jira.Thanks!
For COACH_MPOSWebAPI_R3.29.5d, if Saleshub was enabled, for CN region then we unable to check the purchase history for the member we selected.
Testing info:
CS2K Testing machine ip: 10.33.254.15(OCQ311) - CN region
IPA Version: 3.29.5-20250108.2
API: COACH_MPOSWebAPI_R3.29.5d ( connect to apabiqwposweb24)
Testing vip phone no: 15008476947
![](https://jira.tapestry.support/images/icons/link_attachment_7.gif)
Log already uploaded, for the more details kindly check the attached video.[202502141410590000.mp4](https://jira.tapestry.support/secure/attachment/912829/912829_202502141410590000.mp4)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (37 則)
**Daniel Leung** (2025-02-17):
Seems member purchase history could be found in MPOS
@@Tovi Wang Please get the backend api log for further investigation
**Tovi Wang** (2025-02-17):
@@Daniel Leung  This is CN region,And it is not same region with [MP-746].Let me re-copy CN apabiqwposweb24 MPOS logs to you for further checking.Thanks!
**Tovi Wang** (2025-02-17):
@@Daniel Leung CN 02-14 ALL MPOS logs to you for further checking.Thanks!
**Daniel Leung** (2025-02-17):
Accroding to the logs , seems purchase history can be found in MPOS
@@Tovi Wang Please also get the CRMBEAPI for further investigation .
**Tovi Wang** (2025-02-17):
@@Daniel Leung 02-14 WEB22 CRM BEAPI log for your further checking
**Daniel Leung** (2025-02-17):
@@Tovi Wang Can you also get 02-11 CRM BEAPI log? Thanks
**Tovi Wang** (2025-02-17):
@@Daniel Leung 02-11 CRM BEAPI log
**Daniel Leung** (2025-02-17):
The fail case is later then the logs. Do you have any more logs  before 11 February 2025 03:22:35 PM?
**Tovi Wang** (2025-02-17):
@@Daniel Leung Sorry,I don’t got your point.Neil提供的测试 Vedio是在 02-14.我们为什么需要查02-11的log呀？Please help to double check and confirm.
**Daniel Leung** (2025-02-18):
@@Tovi Wang I don’t have right to access the video.::sweat_smile:: . Anyway, I have check all 02-14 mpos log and it shows positive result, purchase data return normally.
 Did the member profile can be open and display correctly?
Both profile and purchase history will open a webview. Just want to make sure its not a webview issue.
**Tovi Wang** (2025-02-18):
@@Daniel Leung As talked in teams meeting.Per the vedio,The issue happend in 14:06 02-14.Please help to double check the logs of the time.If anything other question please ping me.Thanks!
**Tovi Wang** (2025-02-18):
@@Daniel Leung apabiqwposweb24 server MPOS API web.config for your further checking
**Tovi Wang** (2025-02-18):
@@Daniel Leung APABIQWPOSWEB21 & APABIQWPOSWEB22 IIS log for your further checking.
**Tovi Wang** (2025-02-19):
@@Daniel Leung 把MPOS API 的 web.config 裡面的ThirdPartyModuleInstallPath的 value 改成 [https://qacs2000aliweb.coach.com/BEGWCRM](https://qacs2000aliweb.coach.com/BEGWCRM),Issue fixed.
这个值我们之前没有动过吧？
**Daniel Leung** (2025-02-19):
@@Tovi Wang 没有
**Tovi Wang** (2025-02-19):
@@Daniel Leung @@Bobby @@Cy Lau 现在购物历史可以打开了，但是又出现了很久之前已经修复了的一个issue,404 error [ACU-76].下面截图和vedio供您参考。
**Tovi Wang** (2025-02-20):
@@Daniel Leung @@Bobby @@Cy Lau Double checked with Neil,404 error still，And Another previous “Unknow” issue occured again.
1. 
2.
**Tovi Wang** (2025-02-20):
@@Daniel Leung Please check.Thanks!
**Tovi Wang** (2025-02-20):
@@Daniel Leung Please check.
**Tovi Wang** (2025-02-20):
@@Daniel Leung02-20 MPOS log here
**Cy Lau** (2025-02-21):
@Daniel Leung
Please build IPA with log for tracing
**Daniel Leung** (2025-02-21):
Log version has been uploaded to [🔗](https://ios.ctil.com/mpos/PreCoach/)
**Cy Lau** (2025-02-21):
@Tovi Wang
please help to delivery the IPA to Neil, not the link but the IPA file to them for logging
**Cy Lau** (2025-02-21):
From IPA Log :
At 14:23:12 , the aliasName is correct
When it reached 14:32:57 , it returns unknown
On 20-Feb:
**Cy Lau** (2025-02-21):
From lic Server record :
**Cy Lau** (2025-02-21):
@@Tovi Wang Please help to gather the IPA log , upon to the lic server , Neil did perform the testing since 2025-02-21 14:25:16.593
**Tovi Wang** (2025-02-21):
@@Cy Lau @@Daniel Leung
Neil completed the testing and member profile 404 error still.
up testing vedio & 02-21 MPOS log for your further checking
**Daniel Leung** (2025-02-21):
@@Tovi Wang Please try both Purchase History and Member Profile again. We have changed the maximum query string length setting in IIS
**Cy Lau** (2025-02-21):
For record :
**Tovi Wang** (2025-02-21):
@@Daniel Leung @@Cy Lau double confirm with Neil,404 error gone.
**Tovi Wang** (2025-02-21):
But “Unknow“ issue still.Please help to further checking.Thanks!
**Cy Lau** (2025-02-21):
The "Unknown" issue is owing to license server connection failure
The failure is caused by Connection timeout.
Would follow up with that on Monday by using portable sqlconnection tools
**Andrew_Au** (2025-02-24):
@@Daniel Leung What is the status of the issue ?
**Daniel Leung** (2025-02-24):
Multiple issue in this Jira. 
1.  unable to check the purchase history for CRM Member (fixed)
2. 'Unknow '  Alias Name (investigating)
**Ken Wang** (2025-02-25):
@tovi Please update the ticket status.
**Tovi Wang** (2025-02-27):
@@Cy Lau @@Daniel Leung MPOS-77 2 issues all fixed,right?
**Sherman tse** (2025-05-02):
Issue has handled & closed, details please refer to [https://jira.tapestry.support/browse/MPOS-77](https://jira.tapestry.support/browse/MPOS-77)
Close case

## 相關資訊

- Jira: [MP-747](https://ctil.atlassian.net/browse/MP-747)
- Fix Version: 未記錄
- 解決日期: 2025-05-02
