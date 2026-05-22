---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Neil callout CN MPOS missing follow 2 button:"
root-cause: "待提取"
solution: "### Jira Comments (21 則)"
jira: MP-769
resolved: 
fix-version: ""
---

# MP-769: [ACU-76] [MPOS-77]CN MPOS missing  'More' button on Member profile page

## 問題

Neil callout CN MPOS missing follow 2 button:
1.1 在会员详细资料 界面没有“更多”button。
2.1 会员 界面没有“购物历史”这个button.
Member no:OCQ91MBC0000002，Tel no:17781482669
1.1 在会员详细资料界面没有“更多”button。
IPA: v3.29.5 0325.3, API: v3.29.5f
Bellow is Testing video:
1.2 之前CN MPOS有"更多"这个Button。
v3.29.5 20250108.2
2.1 会员界面没有“购物历史”这个button.确认到此会员是有销售的。
Member no:OCQ91MBC0000002，Tel no:17781482669
2.2 之前有购物历史这个button.
2.3 查询CRMBEAPI log没有发现有CRM return purchase history.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (21 則)
**Tovi Wang** (2025-05-07):
@@Cy Lau  @@Daniel Leung  Could you help to further checking why missing the 2 button on CN MPOS?Thanks!
CC: @@Joy Li  @@Anson Cheung
All MPOS log & CRMBEAPI log here.
**Daniel Leung** (2025-05-07):
@@Tovi Wang  Please also get the web.config in MPOS API, thanks
**Tovi Wang** (2025-05-07):
@@Daniel Leung   Here.
**Daniel Leung** (2025-05-07):
These two config is missing. Please add back and test again.
**Tovi Wang** (2025-05-07):
@@Daniel Leung Sorry,I provided the wrong Web.config before.
Bellow is the new Web.config.Please help to double check.Thanks!
**Tovi Wang** (2025-05-07):
@@Daniel Leung I double checked the QA CN web23 server’s Web.config.Seems still NOT have the two config.Please help to double confirm.Thanks!
**Daniel Leung** (2025-05-08):
@@Tovi Wang Yes, please add it back. The value of `ThirdPartyModuleInstallPath` should be the location of 3P module.
**Tovi Wang** (2025-05-08):
@@Daniel Leung Could you send me the 2 config file to me?Thanks!
**Tovi Wang** (2025-05-08):
@@Daniel Leung Could you send me the 2 config file to me?Thanks!
**Daniel Leung** (2025-05-08):
@@Tovi Wang  Remember to set the correct `ThirdPartyModuleInstallPath` value. it should be the location of 3P module.
**Tovi Wang** (2025-05-08):
I has applied the web.config to CN QA Web23 & Web24 server.Waiting Neil testing result.
**Tovi Wang** (2025-05-08):
@@Daniel Leung @@Cy Lau @@Joy Li 现在这2个button有了，但是一直long loading，[也没有error.](http://也没有error.Do)Please help to take a look.
Testing video:
**Daniel Leung** (2025-05-08):
@@Tovi Wang 
1.Can you connect the url (qacs2000aliweb.com/Member……….) with browser?  (You can copy the link in mpos log to test)
2. Can FE open purchase hitstory correctly?
**Tovi Wang** (2025-05-08):
@@Daniel Leung
1.Also is long loading and timeout error.
MPOS UI log:
{className: Web view: [qacs2000aliweb.coach.com/MemberPurchase/acxiom?lang=sc&data={"apiUrl"%3A"qacs2000aliweb.coach.com"%2C"memberNumber"%3A"OCQ91MBC0000002"%2C"storeCode"%3A"OCQ311"}](http://qacs2000aliweb.coach.com/MemberPurchase/acxiom?lang=sc&data=%7B%22apiUrl%22%3A%22qacs2000aliweb.coach.com%22%2C%22memberNumber%22%3A%22OCQ91MBC0000002%22%2C%22storeCode%22%3A%22OCQ311%22%7D), methodName: initState, text: Web viewURL : , timestamp: 08 May 2025 03:57:26 PM, timeInMillis: 1746691046330, exception: null, dataLogType: null, logLevel: LogLevel.SEVERE, stacktrace: null}
{className: MemoController, methodName: doExit, text: User performs exit, timestamp: 08 May 2025 03:57:48 PM, timeInMillis: 1746691068049, exception: null, dataLogType: null, logLevel: [LogLevel.INFO](http://LogLevel.INFO), stacktrace: null}
2.FE POS can normal open purchase history.
MPOS Log here:
**Daniel Leung** (2025-05-09):
@@Tovi Wang
Can you also get the FE vbretail.ini please.
**Tovi Wang** (2025-05-09):
@@Daniel Leung FE vbretail.ini
**Daniel Leung** (2025-05-09):
@@Tovi Wang Did you set the `ThirdPartyModuleInstallPath` to “`https://qacs2000aliweb.coach.com/BEGWCRM`“?
**Tovi Wang** (2025-05-09):
@@Daniel Leung Let me double confirm.Thanks!
**Tovi Wang** (2025-05-13):
Added & Corrected Follow 2 config setting,Neil double confirmed [ACU-76] & [MPOS-77] two Jira issue fixed now.
@@Joy Li @@Bobby Could you help to re-provide a correct PRO web.config as QA to Neil?
QA web.config for your reference:
**Andrew_Au** (2025-10-06):
@@pierre.shi @@Tovi Wang  Please update the status
**Tovi Wang** (2025-10-10):
issue fixed after corrected follow config setting.Closed.

## 相關資訊

- Jira: [MP-769](https://ctil.atlassian.net/browse/MP-769)
- Fix Version: 未記錄
- 解決日期: 未記錄
