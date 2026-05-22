---
tags: [faq, fe, 交易流程]
component: "CS2kconnect, Front End v750.01R01A"
symptom: "Hi Teams, OC126 often has dayend issue after upgraded to V75."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1622
resolved: 2025-02-24
fix-version: ""
---

# FE-1622: [RIN01447976]dayend issue on OC126 on till1 after upgraded to V75

## 問題

Hi Teams, OC126 often has dayend issue after upgraded to V75.
We had store user not to shut down all PC on 6th Feb.
And found no dayendinfo in cs2000connect.log.
That caused the dayend inform not posted.
And it would be posted on the second day after the PC started.
It  can be found in the next day’s cs2Kconnect.log.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-02-24
### Jira Comments (7 則)
**Cy Lau** (2025-02-10):
@@pierre.shi  it is owing to :
Please check the config thanks
**Sang** (2025-02-11):
@@pierre.shi @@Cy Lau
OC126 Till 1 have not defined MSMQ server.   POS generate day end PCD file and wait for CS2K to pickup. If SA turn off POS after Day end before CS2k Pickup, then dayend PCD will be uploaded next day .
**pierre.shi** (2025-02-11):
Hi @@Sang @@Cy Lau OC126目前已经恢复，但是升级到v75的还有几家目前在观察中，这几家有个共同特点，都是在dayend以后，他们的cs2000connect不再上传数据。OC126已确认是，笔记本在dayend以后，没有 关机，而是直接合上了。另外几家也没有关机信息，关闭硬盘设置也是从不，不确认用户是不是点了休眠，目前也已通知用户不做相关休眠或者关机等操作，同时，将cs2000connect的计划任务设置为了一直运行，之前设置都是每天一次。
**Sang** (2025-02-11):
@@pierre.shi *‘但是升级到v75的还有几家目前在观察中，这几家有个共同特点，都是在dayend以后，他们的cs2000connect不再上传数’据*。' - Please check those shop’s MSMQ setting and POS version? further my understanding Coach CN should use MSMQ, please verify also.
**pierre.shi** (2025-02-11):
Hi @@Sang The pos version of the  three sites is 75.004.0903.0000, and they use OSS now.
CN will use OSS instead of MSMQ.
目前，将计划任务改为‘一直运行’并且保证dayend做完之后十分钟内电脑不关机，这几个site还是正常的，我们会继续观察一段时间，如果后续还有问题发生，我这边会继续更新。
**Andrew_Au** (2025-02-24):
@@pierre.shi Please update the ticket status
**pierre.shi** (2025-02-24):
Hi @@Andrew_Au please help to close this ticket.
after modify the schedule task of cs2000connect, this issue fixed.

## 相關資訊

- Jira: [FE-1622](https://ctil.atlassian.net/browse/FE-1622)
- Fix Version: 未記錄
- 解決日期: 2025-02-24
