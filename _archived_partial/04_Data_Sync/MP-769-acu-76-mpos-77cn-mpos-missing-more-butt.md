---
project: MP
issue_key: MP-769
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-769
created: '2025-05-07'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'MP-769: [ACU-76] [MPOS-77]CN MPOS missing  ''More'' button on Member profile page'
---
# MP-769: [ACU-76] [MPOS-77]CN MPOS missing  'More' button on Member profile page

## 問題描述

Neil callout CN MPOS missing follow 2 button:

1.1 在会员详细资料 界面没有“更多”button。

2.1 会员 界面没有“购物历史”这个button.

Member no:OCQ91MBC0000002，Tel no:17781482669

1.1 在会员详细资料界面没有“更多”button。

IPA: v3.29.5 0325.3, API: v3.29.5f

Bellow is Testing video:

> 📎 **202505070915530000.mp4** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/56215d98-f5b6-41b3-81fc-da85c6907c33)（需 Jira 登入）

> 📎 **image-20250507-073737.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/5d652ff7-040c-43d6-b3e8-be2403d196a3)（需 Jira 登入）
1.2 之前CN MPOS有"更多"这个Button。

v3.29.5 20250108.2

> 📎 **image-20250507-075312.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/cb22e74d-bacd-4b7d-98a3-1154e048540f)（需 Jira 登入）

2.1 会员界面没有“购物历史”这个button.确认到此会员是有销售的。

Member no:OCQ91MBC0000002，Tel no:17781482669

> 📎 **image-20250507-074759.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/1ad5ca70-7a0b-445b-bb67-d34c7b75a028)（需 Jira 登入）
2.2 之前有购物历史这个button.

> 📎 **image-20250507-074919.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ece0bdd5-507b-415c-bf35-aa20b8d09edf)（需 Jira 登入）
2.3 查询CRMBEAPI log没有发现有CRM return purchase history.

> 📎 **image-20250507-075816.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/07a7a236-ae75-4933-a5db-ad302b1d47c5)（需 Jira 登入）


## 附件截圖

1. 📎 **202505070915530000.mp4** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/56215d98-f5b6-41b3-81fc-da85c6907c33)
2. 📎 **image-20250507-073737.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/5d652ff7-040c-43d6-b3e8-be2403d196a3)
3. 📎 **image-20250507-075312.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/cb22e74d-bacd-4b7d-98a3-1154e048540f)
4. 📎 **image-20250507-074759.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/1ad5ca70-7a0b-445b-bb67-d34c7b75a028)
5. 📎 **image-20250507-074919.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ece0bdd5-507b-415c-bf35-aa20b8d09edf)
6. 📎 **image-20250507-075816.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/07a7a236-ae75-4933-a5db-ad302b1d47c5)


## Jira Comments

> **Tovi Wang** (2025-05-07):
>      Could you help to further checking why missing the 2 button on CN MPOS?Thanks! CC:       All MPOS log & CRMBEAPI log here.

> **Daniel Leung** (2025-05-07):
>   Please also get the web.config in MPOS API, thanks

> **Tovi Wang** (2025-05-07):
>      Here.

> **Daniel Leung** (2025-05-07):
> These two config is missing. Please add back and test again.

> **Tovi Wang** (2025-05-07):
>  Sorry,I provided the wrong Web.config before. Bellow is the new Web.config.Please help to double check.Thanks!

> **Tovi Wang** (2025-05-07):
>  I double checked the QA CN web23 server’s Web.config.Seems still NOT have the two config.Please help to double confirm.Thanks!

> **Daniel Leung** (2025-05-08):
>  Yes, please add it back. The value of  ThirdPartyModuleInstallPath  should be the location of 3P module.

> **Tovi Wang** (2025-05-08):
>  Could you send me the 2 config file to me?Thanks!

> **Tovi Wang** (2025-05-08):
>  Could you send me the 2 config file to me?Thanks!

> **Daniel Leung** (2025-05-08):
>   Remember to set the correct  ThirdPartyModuleInstallPath  value. it should be the location of 3P module.

> **Tovi Wang** (2025-05-08):
> I has applied the web.config to CN QA Web23 & Web24 server.Waiting Neil testing result.

> **Tovi Wang** (2025-05-08):
>      现在这2个button有了，但是一直long loading， 也没有error. Please help to take a look. Testing video:

> **Daniel Leung** (2025-05-08):
>   1.Can you connect the url (qacs2000aliweb.com/Member……….) with browser?  (You can copy the link in mpos log to test) 2. Can FE open purchase hitstory correctly?

> **Tovi Wang** (2025-05-08):
>   1.Also is long loading and timeout error. MPOS UI log: {className: Web view:  qacs2000aliweb.coach.com/MemberPurchase/acxiom?lang=sc&data={"apiUrl"%3A"qacs2000aliweb.coach.com"%2C"memberNumber"%3A"OCQ91MBC0000002"%2C"storeCode"%3A"OCQ311"} , methodName: initState, text: Web viewURL : , timestamp: 08 May 2025 03:57:26 PM, timeInMillis: 1746691046330, exception: null, dataLogType: null, logLevel: LogLevel.SEVERE, stacktrace: null} {className: MemoController, methodName: doExit, text: User performs exit, timestamp: 08 May 2025 03:57:48 PM, timeInMillis: 1746691068049, exception: null, dataLogType: null, logLevel:  LogLevel.INFO , stacktrace: null} 2.FE POS can normal open purchase history. MPOS Log here:

> **Daniel Leung** (2025-05-09):
>   Can you also get the FE vbretail.ini please.

> **Tovi Wang** (2025-05-09):
>  FE vbretail.ini

> **Daniel Leung** (2025-05-09):
>  Did you set the  ThirdPartyModuleInstallPath  to “ https://qacs2000aliweb.coach.com/BEGWCRM “?

> **Tovi Wang** (2025-05-09):
>  Let me double confirm.Thanks!

> **Tovi Wang** (2025-05-13):
> Added & Corrected Follow 2 config setting,Neil double confirmed [ACU-76] & [MPOS-77] two Jira issue fixed now.    Could you help to re-provide a correct PRO web.config as QA to Neil? QA web.config for your reference:

> **Andrew_Au** (2025-10-06):
>     Please update the status

> **Tovi Wang** (2025-10-10):
> issue fixed after corrected follow config setting.Closed.

## 相關資訊

- **Jira:** [MP-769](https://ctil.atlassian.net/browse/MP-769)