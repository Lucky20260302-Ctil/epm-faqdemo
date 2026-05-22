---
tags: [faq, fe, 交易流程]
component: "Front End v720.02, Front End v750.01R01A"
symptom: "[INC2936715]Till0 receipt 00053075 can't be printed fully."
root-cause: "待提取"
solution: "### Jira Comments (28 則)"
jira: FE-1692
resolved: 
fix-version: ""
---

# FE-1692: [INC2936715]Till0 receipt 00053075 can't be printed fully

## 問題

[INC2936715]Till0 receipt 00053075 can't be printed fully.
正常应打出顾客联*1+店铺联*1且均有完整条码。但till0会时而出现问题，只会打出一张顾客联且无完整条码。
00053075 is incorrect,20006500 is correct:
checked in T9, has error report while printing:
compare with till2, no related config find

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (28 則)
**Tovi Wang** (2025-05-14):
@@Sang May I know anything update for this case?Thanks!
CC @@Cy Lau @@Joy Li @@pierre.shi
**pierre.shi** (2025-05-15):
Hi @@Sang  have we got any progress?
Could you please help to check this one urgently？ This issue has been submitted for more than 10days.
CC: @@Tovi Wang @@Joy Li
**Sang** (2025-05-15):
@@pierre.shi @@Tovi Wang @@Cy Lau @@Joy Li Sale Memo #00053075 have a long Vip No (17 Characters), when Convert to barcode 128 excess printer support the barcode width   (may be limit to around 15 Char).  Please test support barcode length of KS P using printer support length and discuss with KS JP maximum length of VIP No.  need to support.
**Tovi Wang** (2025-05-21):
@@Sang @@Cy Lau @@Joy Li
1.C322 17位会员销售T9 log有error,且打印小票不完整。
2.C318 17位会员销售T9 log没有error，且可以正常打印。
远程对比C322 till0 和 C318 till0 TMU priter是同一型号，且OPOS setting,OPOS version都一致。Please advice next action.Thanks!
1.
2.
3.
**Tovi Wang** (2025-05-21):
Compare file here
**Sang** (2025-05-22):
@@Tovi Wang @@Cy Lau I have tested on our lab by using Epson TM-T88IV printer with v2.8E ADK, POS can print vip no. barcode up to 20 Chars.  Please get C322 Till0 Dbhist.sdf for further testing.
**Tovi Wang** (2025-05-22):
@@Sang 目前只有 C322 till0一家店铺callout 这个问题，之前没有发生过这个issue.
Copying C322 Till0 Dbhist.sdf.
If need other info?
**Sang** (2025-05-22):
@@Tovi Wang Did u get dbhist.sdf?
**Tovi Wang** (2025-05-22):
@@Sang Waiting SOG team provide.Once SOG team provikded,I will update here in time.
**Tovi Wang** (2025-05-23):
@@SangC322 dbhist here.Please help to further checking.
**pierre.shi** (2025-05-26):
Hi @@Sang  any progress can be shared to us that we can also share to SOG?
CC: @@Joy Li @@Tovi Wang
**Sang** (2025-05-26):
will be update tmr
Get Outlook for iOS<[https://aka.ms/o0ukef](https://aka.ms/o0ukef)>
**pierre.shi** (2025-05-27):
Hi@@Sang , have we got any update? This issue will be long pending.
**Sherman tse** (2025-05-27):
Hi@@pierre.shi We cannot reproduce the issue with  V75 R13 & V72 R25 & printer: TM88IV. Testing data used from TP dbtrans & dbhist. We suspect that it may be related to printer issue. Could you please told TP QAQC try to use another printer to test once again for verifying the issue if related to printer or not.
Testing result from our lab:
**Tovi Wang** (2025-05-30):
Coach team are replacing C322 till0 TMU printer.waiting for store feedback the result.
**pierre.shi** (2025-06-03):
Hi @@Sang  SOG used a new printer to  test, but issue still.
Can you give any other advise?
**Sang** (2025-06-03):
@@pierre.shi
Please try to print ‘00053076’ first and then print ‘00053075’
**pierre.shi** (2025-06-04):
Hi@@Sang asked store user to printer as you required, but still show this issue.
**Sang** (2025-06-05):
@@pierre.shi Please try to print Memo#00052973, 00053075, 00053105. Get the print result and log.
**pierre.shi** (2025-06-05):
Hi @@Sang  the captures of sales memo and logs have been uploaded.please help to check.
**Sang** (2025-06-05):
@@pierre.shi Seems this printer setup can’t print 17chars barcode, please try to print memo in attached table have 14chars and 16 chars length vip no. Please get the installed Epson OPOS ADK version and TMU printer driver setup also.
**pierre.shi** (2025-06-06):
@@Sang Hi, opos version and tmu printer driver for your reference. User refused to reprint again.
**Sang** (2025-06-09):
@@Cy Lau Any suggestion?
**Cy Lau** (2025-06-09):
Please help to tick before asking them to reprint the salesmemo :
**pierre.shi** (2025-06-10):
Hi @@Cy Lau below attachment for your reference.
**pierre.shi** (2025-06-10):
@@Cy Lau
**Cy Lau** (2025-06-10):
**Tovi Wang** (2025-08-19):
Issue fixed.Please closed tickets.

## 相關資訊

- Jira: [FE-1692](https://ctil.atlassian.net/browse/FE-1692)
- Fix Version: 未記錄
- 解決日期: 未記錄
