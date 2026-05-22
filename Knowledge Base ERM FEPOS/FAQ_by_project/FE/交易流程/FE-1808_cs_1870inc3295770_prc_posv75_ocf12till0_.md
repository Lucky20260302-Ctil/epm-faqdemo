---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "[INC3295770] PRC POSv75 OCF12till0, print sales memos cost frequently 5~10 sec."
root-cause: "待提取"
solution: "### Jira Comments (3 則)"
jira: FE-1808
resolved: 
fix-version: ""
---

# FE-1808: [CS-1870][INC3295770] PRC POSv75 OCF12till0, print sales memos cost frequently 5~10 sec.

## 問題

[INC3295770] PRC POSv75 OCF12till0, print sales memos cost frequently 5~10 sec.
checked in T9 logs ,it shows no error.
Normally, it should be only cost 3-5 sec.
<u>[INC3306646](https://tapestry.service-now.com/incident.do?sys_id=4ef05bad47d93e5498ab0694f16d4336&sysparm_record_target=incident&sysparm_record_row=6&sysparm_record_rows=9&sysparm_record_list=assignment_group.nameSTARTSWITHSanyo+support+team%5EstateNOT+IN6%2C7%5Eu_cancel%3Dfalse%5EparentISEMPTY%5EORDERBYshort_description)</u> PRC OCF39 打印有正常也有异常的，从百旺拿qrcode信息，一般3-5秒，此外打印所用时间大概再5-15秒之间。
这个issue跟INC3295770 OCF12类似的。

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (3 則)
**Tovi Wang** (2025-11-26):
@@Joy Li @@Sang 我把11-12 FE log全部检查了一遍。
1.拿 memo 00197729 作为sample来检查。从T9 log可以发现,<span style="color:#ff5630">20251112 12:38:29 </span>小票开始打印,<span style="color:#ff5630">2025/11/12 12:38:40</span>小票打印出来，一共用了11s左右。我检查了当天的其它所有log,没发现此时间段有其它action的log record.
那么这11s中间具体是在做什么？
[20251112 12:38:29 -6486]: DoReprint
[<span style="color:#ff5630">20251112 12:38:29 -6486</span>]: doPrint_Memo.Start
<span style="color:#ff5630">2025/11/12 12:38:40.467</span> Print TMU C:\retdata6\PRINTLOG\SM_OCF12_00197729_opos.dat
|N                  销售单                  
|N           Shenyang PCD Outlet            
|N 沈阳市棋盘山开发区沈棋路36号（中旅小镇内
|N            电话:024-8803 0103            
|N
|N               *** 重印 ***               
|N
|2C客户 联              
|2C
|N店铺 : OCF12                      机号 : 0
|N销售小票号码 : 00197729                   
|N收银员 : 467343                           
|N销售员 : 665873                           
|N12/11/2025                           12:37
|N
|N货号                    数量     金额(RMB)
|N------------------------------------------
|NCV933 IMXAQ                1      1,888.00
|N TERI SHOULDER BAG IN
|N
|N合计:                      1      1,888.00
|N
|N银行卡                            1,888.00
|N  wx                                      
|N找零                                  0.00
|N
|N
|N会员 :  尹兴黎
|N       (OCF12TC00006322)                  
|N
|N备注 :
|NSF1560809069979
|N
|N   全新商品于COACH中国官方网站同步发售    
|N  登陆WWW.COACHOUTLET.CN享受网上购物体验  
|N           中文官方网站闪亮登场           
|N
|N        亲爱的顾客，感谢您的光临。        
|N  为保障您的权益，结账前请详细检查商品。  
|N   商品售后相关政策请参见销售小票背面。   
|N
|N
|N
|N
|N
|N
|0fP
2025/11/12 12:38:43.316 Print TMU C:\retdata6\PRINTLOG\SM_OCF12_00197729_opos.dat
|N                  销售单                  
|N           Shenyang PCD Outlet            
|N 沈阳市棋盘山开发区沈棋路36号（中旅小镇内
|N            电话:024-8803 0103            
|N
|N               *** 重印 ***               
|N
|2C店铺 联              
|2C
|N店铺 : OCF12                      机号 : 0
|N销售小票号码 : 00197729                   
|N收银员 : 467343                           
|N销售员 : 665873                           
|N12/11/2025                           12:37
|N
|N货号                    数量     金额(RMB)
|N------------------------------------------
|NCV933 IMXAQ                1      1,888.00
|N TERI SHOULDER BAG IN
|N
|N合计:                      1      1,888.00
|N
|N银行卡                            1,888.00
|N  wx                                      
|N找零                                  0.00
|N
|N
|N会员 :  尹兴黎
|N       (OCF12TC00006322)                  
|N
|N备注 :
|NSF1560809069979
|N
|N   全新商品于COACH中国官方网站同步发售    
|N  登陆WWW.COACHOUTLET.CN享受网上购物体验  
|N           中文官方网站闪亮登场           
|N
|N        亲爱的顾客，感谢您的光临。        
|N  为保障您的权益，结账前请详细检查商品。  
|N   商品售后相关政策请参见销售小票背面。   
|N
|N
|N
|N
|N
|N
|0fP
[20251112 12:38:43 -3401]: After Print : Avail V.  Memory : 140731657.56
2.DAL log
3.NPOS log
4.WA log
**Tovi Wang** (2025-11-26):
@@Sang @@Joy Li    2025-11-12 OCF12 till0 logs for your further checking
**Andrew_Au** (2026-05-05):
@@Joy Li @@pierre.shi  Please update the ticket status

## 相關資訊

- Jira: [FE-1808](https://ctil.atlassian.net/browse/FE-1808)
- Fix Version: 未記錄
- 解決日期: 未記錄
