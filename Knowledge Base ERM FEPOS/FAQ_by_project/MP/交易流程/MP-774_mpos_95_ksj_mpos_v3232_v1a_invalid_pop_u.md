---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Hi [Joy Li](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Joy_Li) (CC:[Shie Saito](http"
root-cause: "待提取"
solution: "### Jira Comments (8 則)"
jira: MP-774
resolved: 
fix-version: ""
---

# MP-774: [MPOS-95] KSJ MPOS - v3.23.2-v1a - Invalid pop-up window on Sales page

## 問題

Hi [Joy Li](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Joy_Li) (CC:[Shie Saito](https://jira.tapestry.support/secure/ViewProfile.jspa?name=ssaito%40tapestry.com) [Tovi Wang](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Tovi_Wang) ), during testing for **COACH_MPOSWebAPI_3.23.2-v1a_KSJ.zip**, on sales page, we didn't select any member and item, when click back, it will pop-up below window, kindly help to check, I've upload the UI log(apawiqwposweb02) and recording. FE Testing machine IP: 172.24.253.70(C424).
![](https://jira.tapestry.support/images/icons/link_attachment_7.gif)
[202505221444170000.mp4](https://jira.tapestry.support/secure/attachment/950556/950556_202505221444170000.mp4)

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (8 則)
**Tovi Wang** (2025-05-23):
@@Daniel LeungMPOS ALL logs here for your further checking.Thanks!
cc @@Cy Lau @@Joy Li
**Daniel Leung** (2025-05-23):
It changed only after 3.29. I think this is normal behaviour in this version. It will pop up no when user leave the sales issue page.
**Tovi Wang** (2025-05-23):
@@Daniel Leung Many Thanks for your double confirm.客户的concern是还没有选择任何item,然后点击退出弹出这个info.会不会confuse客户？并且加这个弹窗之前有和Coach team说过嘛？
1.正常是客户输入了一些item，点击退出时弹出这个info我觉得OK；
2.如果客户没有输入任何内容，点击退出时则不需要弹这个info。
@@Cy Lau @@Joy Li What about you think?
**Cy Lau** (2025-05-23):
@@Tovi Wang 我覺得並不是confuse 問題，你是對的，所以3.29 已經處理這個問題，而3.23 除了真的fatal bug 之外，並不會進行這些修改
**Cy Lau** (2025-05-23):
@@Tovi Wang 和可能和他們解釋一下，並不是Invalid Popup
**Tovi Wang** (2025-05-23):
@@Cy Lau Noted.我先和Neil解释下。
所以 3.29 会对此弹窗进行如下enhance,right?
1.客户有输入item等其它内容，点击退出则会有此弹窗提示。
2.如客户在此界面没有输入任何item等其它内容，点击退出则不会有此弹窗提示。
**Andrew_Au** (2025-09-30):
@@Tovi Wang Please update the status
**Tovi Wang** (2025-10-09):
Please closed.

## 相關資訊

- Jira: [MP-774](https://ctil.atlassian.net/browse/MP-774)
- Fix Version: 未記錄
- 解決日期: 未記錄
