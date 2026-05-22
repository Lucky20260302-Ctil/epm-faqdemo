---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "we found there is 61 records failed to send sales data from CS2000 to Acxiom"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1002
resolved: 2025-05-02
fix-version: ""
---

# BE-1002: CS-1351 Issue_HK_POS reconsolidation have discrepancy

## 問題

we found there is 61 records failed to send sales data from CS2000 to Acxiom
pls see below record.
error is coming from VIP synchronization.
pls help check RCA and solution.
1.For sample
vip no :OCF12H00230077
sales memo:OCF1-20285439
Date: 2025-02-11
CRM log can found the error.
2.CRMlog message:
fail to send member in member sync process: OCF12H00230077
@@Anson Cheung Could you help to take a look this error?If anything other log please ping me.Thanks!

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-02
### Jira Comments (27 則)
**Tovi Wang** (2025-02-14):
@@Anson Cheung CRM log for your reference.
**Anson Cheung** (2025-02-14):
CRM returned 400 error “Vip number does not match the customer“. need to clarify the error with CRM
**Tovi Wang** (2025-02-14):
@@Anson Cheung 查询确认是因为DB手机号和CRM手机号不相符导致的error,会员OCF12H00230077 正确的手机号应该是‘96430785’.我查看T9 log 和 PC file,当时客户输入的和PC文件里面显示的手机号码都是正确的‘96430785’。为什么到DB里面的手机号就变成了 ‘96430185’？DB里错误的手机号是从哪里来的？帮忙查看下，谢谢！
**Anson Cheung** (2025-02-14):
@@Tovi Wang Could you get the beapi log? thanks.
**Tovi Wang** (2025-02-14):
@@Anson Cheung  02-11 BEAPI log for your further checking.Thanks!
**Anson Cheung** (2025-02-14):
@@Tovi Wang  The phone no. updated by BEAPI is also correct. Can you check dbtmnlogd in db to see if there are any logs of OCF12H00230077?
**Tovi Wang** (2025-02-14):
@@Anson Cheung 这个会员的change log里面没有任何record.说明这个会员没有做过信息更改。查看DB此会员data应该是 2025-02-11 14:39:10 导入到DB的。我们可以看到这个会员导入到DB的详细log嘛？vip导入到DB的时间和销售导入到db的时间有冲突，正常应该是vip data先进入到DB,销售data后进入到DB.
**Anson Cheung** (2025-02-14):
@@Tovi Wang the only action for OCF12H00230077 in BEAPI is create vip at 14:14:32, vip_last_date is 14:39:10 means this vip has updated by another program. Is there a BEAPICRM?
**Tovi Wang** (2025-02-14):
@@Anson Cheung Let me copy CRMBEAPI log to you for further checking.
**Tovi Wang** (2025-02-17):
@@Anson Cheung 02-11 CRMBEAPI log fot your further checking.Thanks!
**Anson Cheung** (2025-02-17):
@@Tovi Wang  CRMBEAPI update this vip at 14:37 with correct phone no., still have no idea where the incorrect phone no. came from.
**Tovi Wang** (2025-02-17):
@@Anson Cheung Thanks for you help to double confirm.
This issue so strange and horrible… @@Cy Lau @@Bobby @@Jason Wu Anything other advice and idea for this urgent issue?Almost every day, the same issue still occurs.
**Tovi Wang** (2025-02-17):
I am Copying Ename API log & double checking the  interface file.
**Tovi Wang** (2025-02-17):
@@Anson Cheung 02-11 Ename API log for your further checking.
**Anson Cheung** (2025-02-17):
@@Tovi Wang Ename logs you provided do not have record related to OCF12H00230077, the wrong phone no. is not updated by EName.
**Tovi Wang** (2025-02-17):
@@Cy Lau @@Anson Cheung @@Bobby Double checked the VIPmaster interface file from 02-10 to 02-17.And the tel No also is correct in the interface file for the vip no OCF12H00230077.So I have No idea for this issue.Please advice .Thanks!
**Tovi Wang** (2025-02-17):
@@Cy Lau @@Anson Cheung CS2000 web是否可以更新手机号？是否还有其它的log可以查看？我很疑惑DB里面错误的手机号具体是从哪里过来的…因为我们目前查了所有log里面都是正确的手机号，我就更觉得奇怪了。
**Cy Lau** (2025-02-18):
have ever tried to search the tel no. within the DB?
**Anson Cheung** (2025-02-18):
@@Tovi Wanglet’s check on CS2000 web. Can you get the csplusdata sqlite log? It may be located in csplusdata/systemlog or the path configurate in appsettings.json>logPath
**Cy Lau** (2025-02-18):
@@Tovi Wang  besides that,
Please list out and pin the message as
1. 
2. 
3. 
4.
**Tovi Wang** (2025-02-18):
@@Cy Lau @@Anson Cheung  Up is the excel of issue vip.If other question please ping me.
**Tovi Wang** (2025-02-25):
@@Anson Cheung “let’s check on CS2000 web. Can you get the csplusdata sqlite log? It may be located in csplusdata/systemlog or the path configurate in appsettings.json>logPath“
-->CS2K web change log在哪个server?哪个路径呀？Thanks！
CC @@Bobby @@Cy Lau
**Anson Cheung** (2025-02-25):
@@Tovi Wang there are sqlite logs in folder “csplusdata\systemlog” under web server.
**Tovi Wang** (2025-03-06):
@@Anson Cheung @@Bobby 已确认Web server无法更改手机号，所以号码更改应该也不是来自webserver.现在HK 每天还会有同样的issue发生。Please further checking and advice.
明天我会远程Joy笔记本继续做data patch.
**Andrew_Au** (2025-04-09):
@@Tovi Wang  Please update the ticket status
**Tovi Wang** (2025-04-09):
@@Andrew_Au  Still under the investigate.Still NOT found the reason where VIP_tel was changed.
CC @@Bobby @@Cy Lau @@Anson Cheung  FYI.
**Sherman tse** (2025-05-02):
Issue has been handled and closed
please refer to [https://jira.tapestry.support/browse/CS-1351](https://jira.tapestry.support/browse/CS-1351) for details
Close case

## 相關資訊

- Jira: [BE-1002](https://ctil.atlassian.net/browse/BE-1002)
- Fix Version: 未記錄
- 解決日期: 2025-05-02
