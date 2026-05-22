---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "[INC3183121]"
root-cause: "待提取"
solution: "### Jira Comments (8 則)"
jira: MP-801
resolved: 
fix-version: ""
---

# MP-801: [MPOS-126] J804 one MPOS shows it has reached the maximum when logging in

## 問題

[INC3183121]
User has some problems with CJ one MPOS:
Symptom:
MPOS shows it has reached the maximum when logging in
Error:
Excess Maximum Number Register
Device Excess Maximum Limit
Device information
Name: J723-iphone-01
iOS: 18.6.2
Serial number: H1X9XXKXC4
SOG Checked:
1. 
2. 
Troubleshooting:
I checked BE locregister table found that J804 has registered 36 MPOS device.
I have some question for this case:
1. 
2. 
3.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (8 則)
**Tovi Wang** (2025-09-19):
Hi  @@Daniel LeungPlease help to take a look this case.Thanks!
CC @@Joy Li @@Cy Lau
**Tovi Wang** (2025-09-23):
1.Dbmas MobileDevice table: MPOS 注册信息。从table可以看到M till是按照时间先后顺序依次注册。
[2.BE](http://2.BE) locregister table: MPOS登录记录。从table可以看到，每天MPOS登录顺序没有规律，似乎M till number并不是按照时间先后来登录分配的，而是在注册时就已经确定了每一个MPOS的Till No.如我理解有误请纠正我，谢谢！
@@Joy Li @@Daniel Leung 如昨天meeting所说，请帮忙再次检查确认登录Mpos时获取Till number的逻辑。
3.查看J804 2024-01-01 MPOS历史销售，M till也没有规律。
**Daniel Leung** (2025-09-23):
@@Tovi Wang That is what I said last Friday. User can login anytime so the locreg_updatedt will update anytime
**Joy Li** (2025-09-23):
@@Daniel Leungin my understand, MPOS will refresh the Till no everyday.
So mpos will get their MPOS till no separately everyday.
Therefore, device 1 register as MA , then decive 3 register as MB……
If my understanding correct, MA update time should be early than MB…….
But actually,  i can see some record in locregistry table than MA later than MB……
this is not match what we expected.
@@Daniel Leung  Please correct me if wrong.
cc  @@Tovi Wang
**Daniel Leung** (2025-09-23):
@@Joy Li MPOS API will assign tillCode by DeviceID. If no deviceID is matched in [dbmas].[dbo].[MobileDevice], then it will assign new tillCode. Therefore, MPOS will not refresh the Till no everyday
**Tovi Wang** (2025-09-24):
@@Daniel Leung Thanks for your double calarify.
When did this logic start? Because the Coach team said that MPOS login was not based on this logic before.
CC @@Joy Li
**Daniel Leung** (2025-09-24):
@@Tovi Wang It haven't changed since 2021 .
**Tovi Wang** (2025-11-04):
New package has released to Coach QA.Can be closed.

## 相關資訊

- Jira: [MP-801](https://ctil.atlassian.net/browse/MP-801)
- Fix Version: 未記錄
- 解決日期: 未記錄
