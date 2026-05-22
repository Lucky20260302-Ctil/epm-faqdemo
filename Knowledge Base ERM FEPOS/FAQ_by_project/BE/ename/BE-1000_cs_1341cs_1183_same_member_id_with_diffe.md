---
tags: [faq, be, ename]
component: "eName"
symptom: "Coach team found that CS2K has sent AGREX different customers’ names and mobile numbers with same Me"
root-cause: "待提取"
solution: "### Jira Comments (19 則)"
jira: BE-1000
resolved: 
fix-version: ""
---

# BE-1000: [CS-1341][CS-1183] Same Member ID with different names and mobile numbers

## 問題

Coach team found that CS2K has sent AGREX different customers’ names and mobile numbers with same Member ID by CSK2CUST files.
According to Agrex, since the Member ID is same, they performed consolidation on these records. Please see below screenshot for reference.
Member ID: J717WJ03463529
Files:
・CS2KCUST20240128.dat
・CS2KCUST20240428.dat
・CS2KCUST20240529.dat
・CS2KCUST20240919.dat
・CS2KCUST20240924.dat
Could you help to investigate?
PS: We are not sure the impact on the data accuracy, like how many customers data may have similar issues. It may not be just one single case though.
There is only one **CUSTOMER ID (0018307333)** in AGREX DB for these names.
Reason is that in the interface files AGREX received from CS2K, all of these names have the same **Member ID (J717WJ03463529)**.
Thus, AGREX did the consolidation based on the Member ID as a key value.
Toubleshooting:
For J717WJ03463529，经过查询发现此会员名被更新过五次且都是在Ename上面更新的。
1.
The VIP no was created in Ename on 1/28/2024 4:03:10 PM.Vip name is '吉岡 じょうじ'
Ename log:
2.
The same VIP no was created in Ename on 4/28/2024 6:49:13 PM.Vip name is '秋山 洸'
Ename log:
3.
The VIP no was created in Ename on 5/29/2024 11:03:42 AM.Vip name is '穴倉 しん'
Ename log:
4.
The VIP no was created in Ename on 9/19/2024 1:36:32 PM.Vip name is '小野 雄大'
Ename log:
5.
The VIP no was created in Ename on 9/24/2024 2:17:00 PM.Vip name is '高澤 憂'
Ename log:

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (19 則)
**Tovi Wang** (2025-02-06):
@@Anson Cheung We can see the change records from dbtmnlogd table.Could you help to double check where the change come from?Ename OR vip interface file?Please advice.
**Anson Cheung** (2025-02-06):
@@Tovi Wang  Can you get the ename sqlite log of the date when data changed?
**Tovi Wang** (2025-02-06):
@@Anson Cheung  2024-09-20 & 2024-09-25 Ename API logs for your checking.Thanks!
**Tovi Wang** (2025-02-06):
@@Anson Cheung 我在DB里发现 同一个vip_no_id '0018307333'    有2个vip no.vip_no_id是唯一值嘛？
J717WJ03463529 应该是J717 前台创建的，另一个 JXXXLJ00537648 应该是Ename 创建的。Please FYI。
**Anson Cheung** (2025-02-06):
@@Tovi Wang  I cannot find vip JXXXLJ00537648 or J717WJ03463529 in both ename log, is ename has log in two servers?
vip_no_id is not unique.
**Tovi Wang** (2025-02-06):
@@Anson Cheung I  also NOT found the records in Ename log.As I know,AWS Ename log just in one server \\apawipwposweb25\APAWIPWPOSWEB25\eName\datastore\log
So the change where come from?Interface file?
**Anson Cheung** (2025-02-06):
@@Tovi Wang what are the activated interfaces? As I know, most of the interfaces like My_einvoice.exe and CRMSanyoPhaseInterface.exe will not modify vip records.
**Tovi Wang** (2025-02-06):
@@Anson Cheung If have vipmaster interface file in JP？I know Ali have this interface.CRM update DB vip data by the interface.But I’m NOT sure JP if have relates interface?
**Anson Cheung** (2025-02-06):
@@Tovi Wang  can you provide log of the interface?
**Tovi Wang** (2025-02-08):
@@Anson Cheung For J717WJ03463529，经过查询发现此会员名被更新过五次且都是在Ename上面更新的。详情和Ename log都已上传在description.请检查确认为什么同一个VIP no seq 会被不同的会员名使用？是客户操作问题还是Ename bug?Please confirm.Thanks!
**Anson Cheung** (2025-02-10):
@@Tovi Wang 之前也發生過這種情況，是客戶沒有按照正常程序開啟ename create vip的版面，導致使用了同一個vip no。印象中以前有handle過這個問題，需要時間confirm
**Tovi Wang** (2025-02-10):
@@Anson Cheung 之前Coach也call out过同样的问题，COach Jira ticket: CS-1183.
我们需要确认的是客户在什么情况下会做出来这样奇怪的操作，在QA是否可以reproduce这个issue？并且最终如何enhance Ename这一块避免客户再次做出这样的操作。
@@Joseph_Hu 麻烦帮忙在QA测试是否可以reproduce这个issue?谢谢！
CC: @@Bobby @@Jason Wu @@Cy Lau  FYI
**Cy Lau** (2025-02-10):
@@Tovi Wang It could be reproduced in our QA.
Steps :
Goto Create Member Page,Get a new MemberNo. Share to HomePage
every time go to the same page with that MemberNo. , then create a new member.
The details of the member would be always overwritten.
**Tovi Wang** (2025-02-10):
@@Cy Lau Many Thanks for your double confirm and the reproduced steps.So is it a Ename bug?right?
Next how can we enhance this section and avoid the same issue happend again?Please with high priority.
BTW,Can we identify how many members was impacted(How many member data is incorrect for this issue)?
**Cy Lau** (2025-02-10):
@@Tovi Wang 
I would like to share about if talking about
Owing to unexpected operation from the SA, the overwritten happens , if you call it a bug then it would be. I would called not in coverage, enhancement would be needed.
Next how can we enhance this section and avoid the same issue happend again?Please with high priority.
1. 
2. 
3. 
If about programming wise, a revamp of the ename from webpages to SPA would be suggested in order to avoiding SA using intermediate page but not from beginning.
BTW,Can we identify how many members was impacted(How many member data is incorrect for this issue)?
@@Anson Cheung  any update audit trials or indicators that the members have been modified by EName ?
**Cy Lau** (2025-02-11):
thanks @@Tovi Wang  operating on Tapestry QA environment :
**Cy Lau** (2025-02-11):
[William Cai](https://jira.tapestry.support/secure/ViewProfile.jspa?name=wcai%40tapestry.com) added a comment - [Yesterday](https://jira.tapestry.support/browse/CS-1341?focusedId=1439587&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-1439587) - edited
1. 
IIS for the EName webpage hosting on those dates would provide the information with accessing IP, accessing path(with which member no.)
1. 
From the UI log (IP and storeCode) and IIS log with IP cross check would help.
Next action :
Get the IIS log for EName webhost(01,02) on specific dates. @@Tovi Wang  @@Jason Wu
The iPad doing this kind of operation , in application layer we could only provide they didn’t starting with homepage , press button then starting member creation workflow. In the UI log, it would stated as it started with nowhere but member creation workflow step 1.
**Andrew_Au** (2025-03-21):
@@Tovi Wang @@pierre.shi The ticket pending for a long time. Please update the ticket status
**Tovi Wang** (2025-03-21):
this is coming from store operation. let's close ticket first and Coach team will prepare clear communication to store.

## 相關資訊

- Jira: [BE-1000](https://ctil.atlassian.net/browse/BE-1000)
- Fix Version: 未記錄
- 解決日期: 未記錄
