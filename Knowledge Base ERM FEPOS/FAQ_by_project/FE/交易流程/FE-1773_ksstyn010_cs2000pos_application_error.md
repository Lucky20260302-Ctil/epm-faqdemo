---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "This till KSSTYN01-0 has application error after logon POS system ."
root-cause: "待提取"
solution: "### Jira Comments (7 則)"
jira: FE-1773
resolved: 
fix-version: ""
---

# FE-1773: KSSTYN010 CS2000POS application error

## 問題

This till KSSTYN01-0 has application error after logon POS system .
I try to check the setting and reinstall setup71.0214.4800 but the issue is still existed .
Please use below Teamviewer ID to remote and check this store POS especially the logs.
(*** this store POS is located in TW office so it is normal to show online receive problem )
POS version: Ver. 7.1.0.02R14ZV
Note: I have remote to the machine today (22/10/2025), and opened POS, it shows the error message at 09:56am, attached is the screen capture and log for your reference

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (7 則)
**Angela Chan** (2025-11-05):
@@Sang 
has provided more files/logs (related to 5 Nov 2025 at around 9am) for troubleshooting, tried to open CS2000POS.exe and ran into error again at 9am today, please help and thank you
**Automation for Jira** (2025-11-05):
Issue has been created since
Days since: 13
Week since : 1
Issue due date difference
Days since : 
Weeks since:
**Sang** (2025-11-05):
@@Angela Chan @@Joy Li POS ran in Window 11, properly have window updated on/before 22-Oct.  After such window update, POS encountered runtime error
Similar problem has been reported before.  You can try to roll back window update or recommend customer upgrade to v75
**Angela Chan** (2025-11-05):
@@Sang
thanks, I checked the windows update is suspended now and the latest update was on 11/9/2025, I m not sure it is related? or which update should be uninstalled? please advise
screen capture provided, thank you
**Sang** (2025-11-05):
Try uninstall
**Angela Chan** (2025-11-05):
@@Sang
there’s more windows update done, screen captures provided, pls help to see any other need to uninstall too, thanks
**Sang** (2025-11-05):
@@Angela Chan After un-install this patch  , have you try to start POS. If still have problem, better recommend them upgrade to v75.

## 相關資訊

- Jira: [FE-1773](https://ctil.atlassian.net/browse/FE-1773)
- Fix Version: 未記錄
- 解決日期: 未記錄
