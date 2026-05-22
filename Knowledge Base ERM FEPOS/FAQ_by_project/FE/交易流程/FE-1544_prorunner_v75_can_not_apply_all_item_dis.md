---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "I have copied the full set data in below VM, please help to check why it cant apply the total memo 1"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1544
resolved: 2024-12-24
fix-version: ""
---

# FE-1544: ProRunner V75 can not apply all item discount

## 問題

I have copied the full set data in below VM, please help to check why it cant apply the total memo 10% discoun
VM 172.16.138.104
Login .\sxd
password :P@ssw0rd

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-12-24
### Jira Comments (8 則)
**Jason Wu** (2024-10-31):
**Sang** (2024-10-31):
Original Setting
**Sang** (2024-10-31):
Change MixTable_Disc_Perc=10
**Jason Wu** (2024-11-07):
Hi @@Sang ,
I checked and confirmed that the issue is not related to Zlog. It appears that the problem lies with `Dbtrans.sdf` when the POS is processing the coupon Zlog. Here are the conditions I tested:
- 
- 
All testing Dbmas files have been purged.
1. 
2. 
3. 
4. 
5. 
6. 
---
Both Dbtrans are able to upload the promotion to display in below screen
POS login
Username 1031
Password   11
---
The logs has been copied to below path.
\\172.16.183.201\localuser\support\20241107\Sang
**Sang** (2024-11-18):
v750.04R05B
1.
**Jason Wu** (2024-11-21):
@@Andrew_Au  Please help to have a test on it.
**Andy Ko** (2024-11-22):
newtonsoft error.
env: 172.16.138.104
login:    .\sxd  |  P@ssw0rd@09
**Andy Ko** (2024-11-22):
env: 172.16.138.104
login: .\sxd | P@ssw0rd@09
update files: [\\ds411\share\POS_FE_Release_64\20241118 ProRunner v750.04R05B](file://ds411/share/POS_FE_Release_64/20241118%20ProRunner%20v750.04R05B)

## 相關資訊

- Jira: [FE-1544](https://ctil.atlassian.net/browse/FE-1544)
- Fix Version: 未記錄
- 解決日期: 2024-12-24
