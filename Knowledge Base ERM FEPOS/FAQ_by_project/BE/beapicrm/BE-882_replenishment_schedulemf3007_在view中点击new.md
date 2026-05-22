---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Reproduce steps:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-882
resolved: 2024-09-04
fix-version: ""
---

# BE-882: Replenishment Schedule(MF3007) : 在view中，点击new，新建内容，保存成功，页面未展示新建内容

## 問題

Reproduce steps:
1. 
2. 
3. 
Incorrect result:
-

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-09-04
### Jira Comments (3 則)
**Andy Ko** (2024-08-27):
@Jerry in Location Replenishment Information (MF3007), if you double click a record vs if you single click a record and then click “View” button, then the result page will have different behavior:
Double click:
single click + view:
I think New button is not needed?
**ryan** (2024-08-28):
不是MF1006界面，是Replenishment Schedule(MF3007)界面
发件人: Andy Ko (Jira) <jira@ctil.atlassian.net>
发送时间: 2024年8月27日 12:24
收件人: Ryan Liu <Ryan.Liu@platinumchina.com>
主题: [JIRA] Andy Ko 在 [🔗](https://ctil.atlassian.net/browse/BE-882#icft=BE-882) 提及您
Andy Ko 在一项事务中提及您
Backend/[🔗](https://ctil.atlassian.net/browse/BE-882#icft=BE-882) Replenishment Schedule : 在view中，点击new，新建内容，保存成功，页面未展示新建内容  ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌
Andy Ko 在一项事务中提及您
Backend<[https://ctil.atlassian.net/browse/BE?atlOrigin=eyJpIjoiNzZmMTQ0OWQwN2NmNDJjN2I1MTFlNzQzYjM5MDhiYzIiLCJwIjoiaiJ9](https://ctil.atlassian.net/browse/BE?atlOrigin=eyJpIjoiNzZmMTQ0OWQwN2NmNDJjN2I1MTFlNzQzYjM5MDhiYzIiLCJwIjoiaiJ9)>
/
BE-882<[https://ctil.atlassian.net/browse/BE-882?atlOrigin=eyJpIjoiNzZmMTQ0OWQwN2NmNDJjN2I1MTFlNzQzYjM5MDhiYzIiLCJwIjoiaiJ9](https://ctil.atlassian.net/browse/BE-882?atlOrigin=eyJpIjoiNzZmMTQ0OWQwN2NmNDJjN2I1MTFlNzQzYjM5MDhiYzIiLCJwIjoiaiJ9)>
Replenishment Schedule : 在view中，点击new，新建内容，保存成功，页面未展示新建内容 <[https://ctil.atlassian.net/browse/BE-882?atlOrigin=eyJpIjoiNzZmMTQ0OWQwN2NmNDJjN2I1MTFlNzQzYjM5MDhiYzIiLCJwIjoiaiJ9](https://ctil.atlassian.net/browse/BE-882?atlOrigin=eyJpIjoiNzZmMTQ0OWQwN2NmNDJjN2I1MTFlNzQzYjM5MDhiYzIiLCJwIjoiaiJ9)>
[https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5d79bd2847387e0d2bcd5c24/35ca4cb3-706e-4998-889d-05336708a749/128](https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/5d79bd2847387e0d2bcd5c24/35ca4cb3-706e-4998-889d-05336708a749/128)
Andy Ko 12:23 下午 GMT+08:00
@ryan do you mean this?
1. input
1.  save
1.  after click ok
for this case, you need to exit screen and select the record you just saved. This is normal behavior. if you go back to main screen you will see:
Attached file
[矩形: 圆角: 查看事务]
[通知图标]通过自定义电子邮件通知使收件箱保持整洁。 管理通知<[https://ctil.atlassian.net/jira/settings/personal/notifications?emailPreferences=true&engagement=email_banner#emailpreferences](https://ctil.atlassian.net/jira/settings/personal/notifications?emailPreferences=true&engagement=email_banner#emailpreferences)>
Open the issue to view attachments over 100KB.
在您的手机上获取 Jira 通知！下载适用于 Android<[https://play.google.com/store/apps/details?id=com.atlassian.android.jira.core&referrer=utm_source%3DNotificationLink%26utm_medium%3DEmail](https://play.google.com/store/apps/details?id=com.atlassian.android.jira.core&referrer=utm_source%3DNotificationLink%26utm_medium%3DEmail)> 或 iOS<[https://itunes.apple.com/app/apple-store/id1006972087?pt=696495&ct=EmailNotificationLink&mt=8](https://itunes.apple.com/app/apple-store/id1006972087?pt=696495&ct=EmailNotificationLink&mt=8)> 的 Jira Cloud 应用。
管理通知<[https://ctil.atlassian.net/jira/settings/personal/notifications?emailPreferences=true&atlOrigin=eyJpIjoiNzZmMTQ0OWQwN2NmNDJjN2I1MTFlNzQzYjM5MDhiYzIiLCJwIjoiaiJ9#emailpreferences](https://ctil.atlassian.net/jira/settings/personal/notifications?emailPreferences=true&atlOrigin=eyJpIjoiNzZmMTQ0OWQwN2NmNDJjN2I1MTFlNzQzYjM5MDhiYzIiLCJwIjoiaiJ9#emailpreferences)>  •  提供反馈<[https://surveys.atlassian.com/jfe/form/SV_9X3zi1X4q1gKsqF](https://surveys.atlassian.com/jfe/form/SV_9X3zi1X4q1gKsqF)>  •  隐私政策<[https://www.atlassian.com/legal/privacy-policy](https://www.atlassian.com/legal/privacy-policy)>
**Andrew_Au** (2024-08-29):
@@ryan  View  : view record only, double click : modify record, not a issue.

## 相關資訊

- Jira: [BE-882](https://ctil.atlassian.net/browse/BE-882)
- Fix Version: 未記錄
- 解決日期: 2024-09-04
