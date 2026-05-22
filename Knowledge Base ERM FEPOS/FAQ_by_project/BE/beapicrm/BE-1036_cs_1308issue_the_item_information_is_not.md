---
tags: [faq, be, beapicrm]
component: "Master"
symptom: "Issue Detail,"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1036
resolved: 2025-07-04
fix-version: ""
---

# BE-1036: [CS-1308]Issue_the item information is not completed in Mastconv Files 

## 問題

Issue Detail,
during create mastconv files, some items are missing in mastconv files.
e.g. CAG00,CAA79,
CAQ15 CAM44 CR657 CU068 CY919 CH153
only has EAN information but no item information
SOG Ticket:[RIN01428788] [INC2870184] [INC2870184]

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-04
### Jira Comments (20 則)
**Cy Lau** (2025-03-25):
@@Tovi Wang  Please help to recall that , it is 100% hit rate or any further details ?
**Tovi Wang** (2025-03-25):
@@Cy Lau @@Jerry Wong 这个issue是每次新生成的Mastconv file都有部分item missing.之前我有Export Mastconv file 和 DB对比过，Mastconv file里面的 item 数量要比DB里面的item 数量要少。稍后我再重新生成一份最新的item Mastconv file再double confirm下，然后把结果更新在这里。
**Tovi Wang** (2025-03-26):
@@Jerry Wong @@Cy Lau
下面是最新从BE UI 导出来item的mastconv file.请帮忙查看为什么有些item在DB itmast table里是有的，但是在Mastconv file里面是没有的？what’s the mastconv file generate logic?
Such as follow item NOT exit in Mastconv file，but they all exit in db Itmast table.
CAG00,CAA79,CAQ15 CAM44 CR657 CU068 CY919 CH153
**Jerry Wong** (2025-03-26):
@@Tovi Wang
select * from itmast where isnull(itmast_lock,'') <> 'Y'
export item if itmast_lock is not 'Y'
**Tovi Wang** (2025-03-27):
@@Jerry Wong Total 150476 items data of itmast_lock is not 'Y'.Follow export excel data for your further checking.
**Jerry Wong** (2025-03-27):
@@Tovi Wang 
select * from glconfig
where glconfig_key like '%mastconv_top_count%'
can u help me to check this config?
mastconv has a limited row count
**Tovi Wang** (2025-03-27):
@@Jerry Wong  mastconv_top_count config setting is 70000.
所以item Mastconv file generated逻辑是取DB itmast table前70000条数据里itmast_lock is not 'Y'的data?right?Please help to calarify the generated logic.
**Jerry Wong** (2025-03-27):
@@Tovi Wang yes
**Tovi Wang** (2025-03-27):
@@Jerry Wong 但是这样setting的话会产生一个问题啊，那70000行以下的itmast_lock is not 'Y'的data不就全missing掉了嘛？right?So we need change the config setting or other workaround?
**Tovi Wang** (2025-03-27):
@@Jerry Wong One more question.
Total 15001 items data for item mastconv file，
Total 150477 items data for Itmast table of itmast_lock is not Y.
The items data difference is very huge, Could you help to double confirm the item mastconv file generated details logic?Thanks!
**Jerry Wong** (2025-03-27):
@@Tovi Wang 我應該看錯 logic應該沒有limited row count的
你可以找log給我看嗎?
auto還是UI行program?
**Tovi Wang** (2025-03-27):
@@Jerry Wong Mastconv exe config & Mastconv log for your further checking.
**Tovi Wang** (2025-03-28):
@@Jerry Wong May I know anything update please.Thanks!
CC @@Cy Lau @@Bobby
**Cy Lau** (2025-04-10):
DI9008
**Jerry Wong** (2025-04-15):
1. 
2. 
conv_table() in di9008_auto.vb and frm_di9008.vb
# Current logic:
mastconv_top_count in glconfig
<span style="color:#ff5630">  select * from glconfig where glconfig_key = 'mastconv_top_count'</span>
first execute SQL:
<span style="color:#ff5630">select top mastconv_top_count * from itmast WITH (NOLOCK)</span>
<span style="color:#ff5630"> where isnull(itmast_lock,'') <> 'Y'</span>
Second execute SQL:
<span style="color:#ff5630">select top mastconv_top_count * from itmast WITH (NOLOCK)</span>
<span style="color:#ff5630">where itmast_item_no >  last row of first sql result</span>
**Cy Lau** (2025-04-17):
@@Jerry Wong  
#1 Please align the sql selection for both first and 2nd excutation. 
#2 by order asc
#3 Consider with since WITH(NOLOCK) would make the reference different, kind of removal of no-lock
ETA : 17Apr, QAQC on 22Apr (@@Sherman tse )
**Cy Lau** (2025-04-22):
From @@Jerry Wong  17-Apr 1606:
Dear all,
Release:
<u>[\\ds411\csms60\delivery\coach\update-DI9008-2025-04-17](file://ds411/csms60/delivery/coach/update-DI9008-2025-04-17)</u>
Notes:
Update sql for DI9008 mastconv
- 
- 
- 
JIRA:
[🔗](https://ctil.atlassian.net/browse/BE-1036)
Source:
svn://sanyosvn.ctil.com/svn/cs2000/Trunk/BackEnd.Net(VS2017 FW 4.5.2 NEW)/CS2000BNV1_Prod
**Sherman tse** (2025-04-23):
verified on QA
test case attached
**Sherman tse** (2025-05-02):
Update: under Wait deployment status in Tapestry JIRA
**Joy Li** (2025-07-04):
released on 2025-04-22 with BE V70R3.100

## 相關資訊

- Jira: [BE-1036](https://ctil.atlassian.net/browse/BE-1036)
- Fix Version: 未記錄
- 解決日期: 2025-07-04
