---
tags: [faq, be, beapicrm]
component: "MPOS"
symptom: "1."
root-cause: "待提取"
solution: "### Jira Comments (11 則)"
jira: BE-989
resolved: 
fix-version: ""
---

# BE-989: [CS-1147] - KR MPOS transaction cannot send to DB

## 問題

1.
KR MPOS sales can’t upload to DB.The issue happend in Pro.
Temp workaround: Repost the PCD file can fixed
New sample memo:
2025-01-19 OCF50-MA000029       
2025-01-19 OCF50 -MA000030
2.
Also NOT found the MPOS memo in sqlpcda table.
3.
The Coach testing machine 10.33.248.10 has upgraded to V75.Waiting Queenie teasting in this QA PC,then feedback the result to us.
QA POS version:75.004.0702
QA MPOS version:3.29.X

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (11 則)
**Tovi Wang** (2025-01-22):
MPOS log in APAWIPWPOSWEB23.
@@Cy Lau @@Anson Cheung Follow MPOS logs for your further checking.If need anything other logs please ping me in here.Thanks!
CC: @@Jason Wu FYI.
**Tovi Wang** (2025-01-23):
select * from jouinv where jouinv_date>='2025-01-01' and jouinv_line='1' and jouinv_no like 'M%'
select locreg_updatedt,* from locregister where locreg_loc='OCQ96'
select *from sqlpcda where sqlpcd_date>='2025-01-01'*
*---select A4GLIdentity,dayendh_till,dayendh_sales,dayendh_total_amt,dayendh_check,dayendh_check_date,dayendh_check_time,* from dayendh
---where dayendh_loc='OCQ96' and dayendh_date='2025-01-19'
**Tovi Wang** (2025-02-12):
@@Cy Lau Could you help to arrange dev resource to check this issue?If anything need other logs or info please ping me.Thanks!
**Cy Lau** (2025-02-12):
The log showed :
Which means the msmq written by MPOS_API was okay
**Cy Lau** (2025-02-12):
@@Tovi Wang  , For KR, Single Tx Config of MSMQ server has been enable.
So following criteria shall be fulfilled in order to successful polling :
MPOS_API , check config MSMQ_SingleTX, should be “Y“ for KR
Queue ->Enable Single Tx config enable
**Andrew_Au** (2025-03-07):
@@Tovi Wang @@pierre.shi  What is the ticket status ?
**Andrew_Au** (2025-03-26):
@@Tovi Wang @@pierre.shi  Please update the ticket status
**Tovi Wang** (2025-03-26):
@@Andrew_Au waiting KR V75 deployed,then double confirm issue if gone or not.please hold on.
**Andrew_Au** (2025-10-06):
@@Joy Li @@Tovi Wang @@pierre.shi  The ticket pending for a long time.Please update the ticket status
**Tovi Wang** (2025-10-10):
Waiting Coach Team arrange this issue into sprint.Hold on please.
@@Joy Li Please take a look this case with Shie.
**Andrew_Au** (2025-11-03):
@@Tovi Wang @@pierre.shi @@Joy Li   The ticket pending for a long time.Please update the ticket status

## 相關資訊

- Jira: [BE-989](https://ctil.atlassian.net/browse/BE-989)
- Fix Version: 未記錄
- 解決日期: 未記錄
