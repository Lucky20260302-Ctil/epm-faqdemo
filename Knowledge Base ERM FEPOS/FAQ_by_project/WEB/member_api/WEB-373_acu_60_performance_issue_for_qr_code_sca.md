---
tags: [faq, web, member_api]
component: "API"
symptom: "It will take about 10s to complete the code decryption after QR code scanning."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: WEB-373
resolved: 2024-12-24
fix-version: ""
---

# WEB-373: [ACU-60] Performance issue for QR code scanning

## 問題

It will take about 10s to complete the code decryption after QR code scanning.
please help to improve the performance.
\\172.16.183.201\localuser\support\^^ACU_Project\ACU-60.zip

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-12-24
### Jira Comments (10 則)
**Joy Li** (2024-11-26):
i will copy web 21 and 22 IIS log
**Joy Li** (2024-11-26):
added Web 21 and 22 IIS serer log in ACU-60.zip file.
**Cy Lau** (2024-11-27):
@@Anson Cheung Please review the log
@@Cy Lau  will review the IIS server log vs modules actions
**Anson Cheung** (2024-11-27):
@@Cy Lau Here is the observation from the log
in this case, setting up the cache may save 2.5s
A. verify dynamic token (2s)
	1. get glconfig	(cache can be set up in appsettings)
		0.2s	
	2. get csdata connection string from gldata (cache can be set up in appsettings)
		0.3s
	3. get dbconfig (cache can be set up in appsettings)
		0.3s
	4. call CRM get token
		0.6s
	5. call CRM verify dynamic token
		0.6s
B. return result of step A to POS, then POS call BEAPI to search member (0.5s)
C. search member (1.8s)
	1. get glconfig (cache can be set up in appsettings)
		0.2s	
	2. get csdata connection string from gldata (cache can be set up in appsettings)
		0.2s
	3. get dbconfig (cache can be set up in appsettings)
		0.2s
	4. call CRM get token
		0.6s
	5. call CRM search member
		0.6s
D. update member to backend (5s)
	1. select db time (redundant step, can be removed)
		1.6s
	2. select vip to check is member exist
		0.4s
	3. upsert wtmnlog
		0.4s
	4. check db schema (cache can be set up in appsettings)
		1.1s
	5. update vip
		0.4s
	6. upsert crmvip
		0.5s
	7. update vip_type
		0.3s
	8. select complete vip record
		0.3s
**Anson Cheung** (2024-11-29):
The process time of update member to backend can be as fast as 1s, and the entire QR code scanning process takes 5s.
**Anson Cheung** (2024-12-02):
Program v1.6.12 has been released to enhance performance.
update:
- 
- 
-
**Anson Cheung** (2024-12-05):
Release path:
-
**Andrew_Au** (2024-12-24):
@@Sherman tse Please update the ticket status
**Joseph_Hu** (2024-12-24):
ETA to Tapestry QAQC : Dec 24
**Sherman tse** (2024-12-24):
Test case added persentage of scanning time impovement

## 相關資訊

- Jira: [WEB-373](https://ctil.atlassian.net/browse/WEB-373)
- Fix Version: 未記錄
- 解決日期: 2024-12-24
