---
tags: [faq, fe, 交易流程]
component: "MPOS"
symptom: "Store user has some problem with mpos"
root-cause: "待提取"
solution: "### Jira Comments (9 則)"
jira: FE-1543
resolved: 
fix-version: ""
---

# FE-1543: RIN01410237 - JP - J417  - Mpos : the mpos will register double sales

## 問題

Store user has some problem with mpos
Symptom:
1. 
Device & Network Information:
PC name: LPOS
IP Address:[http://172.24.90.211:5631](http://172.24.90.211:5631)
Software Version:
IIS: Cloud
IIS Version:72.0225.0004
MPOS Version:3.25.1
MA000865
MA000864
Troubleshooting:
1.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (9 則)
**Jason Wu** (2024-10-29):
@@Sang  
I have copied the logs in \\172.16.183.201\localuser\support\20241028\sang
**Tovi Wang** (2024-10-29):
@sang Could you help to check the root cause and provide the long term solusions?
**Tovi Wang** (2024-11-01):
@@Sang  May I know anything update for this case?
@@Joy Li @@Jason Wu  FYI.
**Cy Lau** (2024-11-04):
Dear Team,
After investigation:
|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
MPOS API :
MPOS:
|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
MPOS API :
MPOS :
---
The Http Exception - Read Failed :
A) Network Issues: Unstable or interrupted network connections can lead to read failures. This might be due to poor Wi-Fi, network congestion, or server-side issues.
B) Timeouts: If the server takes too long to respond, a timeout can occur, resulting in a read failure. This can be due to high server load or inefficient server processing.
C) Server Overload: When the server is under heavy load, it might drop connections or fail to process requests properly, leading to this error.
Incorrect Configuration: Misconfigurations in the client or server settings, such as incorrect timeout settings or connection pool limits, can also cause this error.
D) Protocol Mismatches: Differences in the HTTP protocol versions or incorrect handling of HTTP responses can lead to protocol exceptions.
**Cy Lau** (2024-11-07):
Dear Team,
From the IIS log, the response had been delivered at 10:37:35 with 200 status and response:
But the MPOS reported for Read failed as HttpException at 10:39:54
**Tovi Wang** (2024-11-07):
Dear @@Cy Lau  I has sended the logs to you by teams.So may I know if anything updates after you checked the logs?
CC: @@Jason Wu @@Joy Li  FYI.
**Tovi Wang** (2024-11-07):
@@Cy Lau  Many thanks for your update.So web server has responsed the sales details to MPOS FE.But MPOS FE failed to read the sales details from server,Right?But why MPOS FE failed to read the sales details from web server?How can we confirmed this is the network issue?
**Tovi Wang** (2025-02-05):
Dear ALL,
Explained to Lein,can closed the issue firstly.
**Tovi Wang** (2025-04-09):
Same issue:<u>[INC2897451](https://tapestry.service-now.com/incident.do?sys_id=7b61894093f4a61c21b5b4edfaba102a&sysparm_record_target=incident&sysparm_record_row=4&sysparm_record_rows=7&sysparm_record_list=categoryINSOG+-+Application%2CSOG+-+Software%2CSOG+-+Intranet%2CSOG+-+Report%2CSOG+-+Hardware%2CSOG+-+3rd+Party+Vendor%2CSOG+-+Network%2CSOG+-+Security%2CSOG+-+Monitoring+Alert%2CSOG+-+Active+Monitoring%2CSOG+-+Backend+Application%5Eassignment_group.nameSTARTSWITHSanyo+support+team%5EstateNOT+IN6%2C7%5Eu_cancel%3Dfalse%5EparentISEMPTY%5EORDERBYDESCnumber)</u>

## 相關資訊

- Jira: [FE-1543](https://ctil.atlassian.net/browse/FE-1543)
- Fix Version: 未記錄
- 解決日期: 未記錄
