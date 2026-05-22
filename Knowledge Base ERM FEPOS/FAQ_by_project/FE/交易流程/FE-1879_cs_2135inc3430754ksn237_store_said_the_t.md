---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Trouble shotting:"
root-cause: "待提取"
solution: "### Jira Comments (20 則)"
jira: FE-1879
resolved: 
fix-version: ""
---

# FE-1879: [CS-2135][INC3430754]KSN237 Store said the till 1 & 2 also the new log update symbol there but after clicked it showing error “Execute.Error: Object reference not set to an instance of an object.”

## 問題

Trouble shotting:
1.Repaired cs2k program,issue still.
2.Checked T9 log found so many same error:
[20260205 16:35:16 -4755]: CheckNewLog - Start : Avail V.  Memory : 140731731.927
[20260205 16:35:16 -5014]: CheckNewLog - End True : Avail V.  Memory : 140731731.927
[20260205 16:35:19 -5921]: Unhanded Exception.Error: Object reference not set to an instance of an object.
KSN237 till1 vedio:
FE logs for your further checking:

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (20 則)
**Tovi Wang** (2026-02-05):
@@Sang @@Cy Lau Could you please help to take a look this error?What’s mean this error?How can we fixed the error?Thanks!
CC @@Joy Li @@pierre.shi
**Tovi Wang** (2026-02-05):
@@Bobby @@Joy Li Please help to provide the 75.004.1900.0000 package.I can let SOG team help to un-install then re-install cs2k program.Thanks!
**Tovi Wang** (2026-02-06):
We had provided the package to SOG team.Waiting SOG team keep monitoring and feedback the result with store.
**Automation for Jira** (2026-02-06):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Tovi Wang** (2026-02-09):
Hi @@Sang @@Cy Lau ,
SOG team confirmed that they re-installed POS version on till 1 and store confirmed the new log update issue still not fixed.Could you please further checking and advice next action?Thanks!
CC @@Joy Li @@pierre.shi
**Cy Lau** (2026-02-09):
@@Tovi Wang may I knoq about was there really new Zlog files in the local folder ? or just a false alarm for the indicator ?
**Tovi Wang** (2026-02-09):
@@Cy Lau Thanks for your quick response.我之前有远程店铺测试过，可以正常update newlog,并且没有error.
但是从店铺提供的录屏可以看到：
录屏时 POS date:2026-02-05 04:27 PM.“New log update”有update 提醒。
但店铺点击“New log update”后,界面会弹出下面2个内容：
1.
先弹出 “No new update log.Update abort”,这个提示我理解是个正常的提示，表示没有newlog需要update。但没有newlog的话，为什么会有newlog update 提醒呢？It’s so confused me.
2.
然后紧接着弹出 “Execute.Error: Object reference not set to an instance of an object.”
这个error是什么error呀？Please help to further checking and advice next action.
**Cy Lau** (2026-02-09):
@@Tovi Wang 呢個我就是想問的，其實folder 裡有沒有new zlog, 如果沒有，那就是記錄跟事實不符，然後不知跳到哪
**Tovi Wang** (2026-02-09):
@@Cy Lau 目前来看有点像是这种情况。我查询了当天T9 log,发现有很多下面error info,而且是做不同的操作之后会跳出这个error.
“Execute.Error: Object reference not set to an instance of an object.”
1.一共出现了17次这个error，大部分都是在 check newlog 后出现的这个error
2.
3.
**Joy Li** (2026-02-09):
@@Tovi Wang
Could you please try below steps:
1. 
2. 
3. 
4.
**Tovi Wang** (2026-02-09):
@@Joy Li Done,Keep monitoring.
**Andrew_Au** (2026-02-23):
@@Tovi Wang  Please update Jira ticket status
**Tovi Wang** (2026-04-01):
Troubleshooting:
1.Repaied CS2000POS program,issue stiil.
2.Uninstall then reinstall Till1，Till2 CS2000 POS,issue still.
3.delete the content in zlogback table in dbhist.sdf,issue still.
4.KSN217 Till0 NOT have this error.just only KSN237 Till1,Till2 have this issue.
5.We can’t reproduce this error.
6.This error pop out does not affect the store's sales, Newlog update.
But it confusesd the store user.
@@Cy Lau @@Sang @@Joy Li So could you please help to double check this error and give me some advice.Thanks!
**Sang** (2026-04-02):
@@Tovi Wang I have reviewed 5-Feb logs, 問題應和new log scan/update 無關。現在狀況如何？
**Tovi Wang** (2026-04-02):
@@Sang 现在Till1 和 Till2还是和以前的一样的情况，查询最近几天的T9 log,每天还是会有很多这个error.
**Sang** (2026-04-02):
@@Tovi Wang Please copy
1. whole Till 1 RetData6 folder exclude SDF, SDF backup files and all sub folders.
1.
**Tovi Wang** (2026-04-08):
@@Sang I had provided all the files to you by teams.Please help to further checking.
**Tovi Wang** (2026-04-08):
**Tovi Wang** (2026-04-15):
@@Sang Sorry for chasing you.May I know if anything update for this error?Thanks!
**Tovi Wang** (2026-04-17):
Double confirmed with @@Sang ,We can be ruled out that it was caused by abnormal files in retdata6.
Comparing the task managers of Till0, Till1, and Till2, it was found that both Till1 and Till2 have AppActions.exe running, while Till0 does not.
Next action:Let Coach team stop it to observe the T9 log result.
CC @@Sang @@Joy Li  FYI.
1.Processes capture as follow:

## 相關資訊

- Jira: [FE-1879](https://ctil.atlassian.net/browse/FE-1879)
- Fix Version: 未記錄
- 解決日期: 未記錄
