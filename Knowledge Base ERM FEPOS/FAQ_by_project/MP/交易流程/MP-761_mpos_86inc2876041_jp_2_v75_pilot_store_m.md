---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Callout store: J317 & J328."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-761
resolved: 2025-05-21
fix-version: ""
---

# MP-761: [MPOS-86][INC2876041] JP 2 V75 Pilot store MPOS keep loading and pop out error:”Fail to Connect SalesHub”after update to new version 

## 問題

Callout store: J317 & J328.
Symptom:
MPOS keep loading after update the update the new version,And pop out error:”Fail to Connect SalesHub”,as per we talked today, Saleshub program unable to launch if login account is 'CS2000', kindly help to check. Testing machine IP: 172.24.253.20.
Troubleshooting:
1. 
2. 
3. 
Device information:
CS2K: v75.004.1100.0008
Cloud IIS: 3.29.5
1.MPOS error
2.Saleshub capture:
3.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-21
### Jira Comments (13 則)
**Tovi Wang** (2025-03-27):
@@Daniel Leung Up saleshub logs for your further checking.Could you help to take a look this one and give me some advice?Thanks!
CC @@Cy Lau @@Bobby @@pierre.shi
**Tovi Wang** (2025-03-27):
@@Daniel Leung JP pilot store J328 also call out the same issue.
**Tovi Wang** (2025-03-27):
@@Daniel Leung @@Cy Lau
1.我用csadmin账号打开CSPLUS，saleshub online,
2.但是用cs2000账号打开CSPLUS,saleshub have error...
CS2000 account没有权限打开saleshub.exe?
**Tovi Wang** (2025-03-28):
Temp workaround:
netsh http add urlacl url=http://+:9001/ user=\Everyone
netsh http add urlacl url=http://*:9001/ user=\Everyone
**Tovi Wang** (2025-03-28):
Issue details & background:
1.saleshub online under csadmin account.
2.saleshub offline under cs2000 account.
RCA & Temp workaround:
The issue caused by cs2000 account NOT access to open SalesHub exe.The temp workaround is that We has granted the cs2000 account access to SalesHub mannually for J317 & J328 under the csadmin account.
long term workaround: TBC
**Tovi Wang** (2025-04-01):
New update:
Through continuous testing and verification.We have something follow new found:
1. 
2. 
Testing PC:  J805 IP: 172.24.253.20
![](https://jira.tapestry.support/secure/attachment/929857/929857_image-2025-04-01-14-10-10-963.png)
**Cy Lau** (2025-04-02):
check in-bound:
`netsh advfirewall firewall show rule name=all | findstr /R "4915[2-9] 491[6-9][0-9] 49[2-9][0-9][0-9] 5[0-9][0-9][0-9][0-9] 6[0-5][0-5][0-3][0-5]"`
check out-bound:
`netsh advfirewall firewall show rule name=all | findstr /R "4915[2-9] 491[6-9][0-9] 49[2-9][0-9][0-9] 5[0-9][0-9][0-9][0-9] 6[0-5][0-5][0-3][0-5]"`
**Cy Lau** (2025-04-02):
SignalR connection will make use of dynamic ports :
Dynamic ports :
Prod J317:
**Cy Lau** (2025-04-03):
Would having a TCP port testing Powershell script :
Running on QA :
3Apr 0010:
Only 39 ports not available with reason :
Exception calling "Start" with "0" argument(s): "Only one usage of each socket address (protocol/network address/port) is normally permitted"
For TCP connection result:
Failed to connect to 172.24.253.20 :9000 from port 56972 : Exception calling "Connect" with "2" argument(s): "Only one usage of each socket address (protocol/network address/port) is normally permitted 172.24.253.20:9000"
Failed to connect to 172.24.253.20 :9000 from port 56987 : Exception calling "Bind" with "1" argument(s): "Only one usage of each socket address (protocol/network address/port) is normally permitted"
**Cy Lau** (2025-04-09):
Updates for 9Apr2025:
Using SalesHubHleathChecker :
Cannot establish TCP connection on the high numbered port, both making connection from oneself or from remote.
With a random VM in QA without using saleshub before - 10.33.248.3
Connection to itself
Making connection from remote client:
using csadmin :
using cs2000:
It proves that Both SalesHubHosting and SalesHubClient would be able to receive and send message from 49152 - 65535
Observatory :
10.33.248.3 using :
Prod using :
**Sherman tse** (2025-05-02):
Updates for 2May2025: Issue under monitoring
**Andrew_Au** (2025-05-21):
@Tovi Please update the ticket status
**Tovi Wang** (2025-05-21):
Dear ALL,
So far,We don’t receive the callout from store.So the issue should be fixed.Closed ticket first.

## 相關資訊

- Jira: [MP-761](https://ctil.atlassian.net/browse/MP-761)
- Fix Version: 未記錄
- 解決日期: 2025-05-21
