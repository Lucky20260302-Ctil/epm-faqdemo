---
project: BE
issue_key: BE-1000
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, ename]
jira_url: "https://ctil.atlassian.net/browse/BE-1000"
created: 2025-02-06
resolved: 
resolution: 
has_images: True
---

# BE-1000: [CS-1341][CS-1183] Same Member ID with different names and mobile numbers

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 7.5
> **負責人:** Anson Cheung
> **組件:** eName

## 問題描述

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

> 📎 **image-20250206-014704.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c74d9c87-e2a7-42b8-bdc7-02582102687d)（需 Jira 登入）

> 📎 **image-20250206-014722.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c6e7248b-bd2e-436b-ad41-38ce692579b9)（需 Jira 登入）

Toubleshooting:

For J717WJ03463529，经过查询发现此会员名被更新过五次且都是在Ename上面更新的。

1.

The VIP no was created in Ename on 1/28/2024 4:03:10 PM.Vip name is '吉岡 じょうじ'

Ename log:  [📎附件](https://ctil.atlassian.net/rest/api/3/attachment/content/01686454-6cff-4a90-9506-2b3b23e8ee61) 

> 📎 **image-20250208-091608.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c8beb5f6-10f4-43f8-af14-a5b3be8dc258)（需 Jira 登入）
2.

The same VIP no was created in Ename on 4/28/2024 6:49:13 PM.Vip name is '秋山 洸'

Ename log: [📎附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bedea496-f116-4b6b-8701-ceb0d3221984) 

> 📎 **image-20250208-095941.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/2ba8e6f8-b943-4419-8adf-ae88ba592180)（需 Jira 登入）
3.

The VIP no was created in Ename on 5/29/2024 11:03:42 AM.Vip name is '穴倉 しん'

Ename log:  [📎附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0161d272-5f04-4e15-b9b9-1e727692fd42) 

> 📎 **image-20250208-100446.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/6288259a-fb19-4e61-886b-840218e89ac7)（需 Jira 登入）
4.

The VIP no was created in Ename on 9/19/2024 1:36:32 PM.Vip name is '小野 雄大'

Ename log: [📎附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ad8d5f03-94d5-4795-91c2-20afdce9c01e) 

5.

The VIP no was created in Ename on 9/24/2024 2:17:00 PM.Vip name is '高澤 憂'

Ename log: [📎附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3d992343-0c7c-4ebb-a9ab-595801d812cd) 



## 附件截圖

1. 📎 **image-20250206-014704.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c74d9c87-e2a7-42b8-bdc7-02582102687d)
2. 📎 **image-20250206-014722.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c6e7248b-bd2e-436b-ad41-38ce692579b9)
3. 📎 **image-20250208-091608.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c8beb5f6-10f4-43f8-af14-a5b3be8dc258)
4. 📎 **image-20250208-095941.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2ba8e6f8-b943-4419-8adf-ae88ba592180)
5. 📎 **image-20250208-100446.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/6288259a-fb19-4e61-886b-840218e89ac7)


## Jira Comments

> **Tovi Wang** (2025-02-06):
>  We can see the change records from dbtmnlogd table.Could you help to double check where the change come from?Ename OR vip interface file?Please advice.

> **Anson Cheung** (2025-02-06):
>   Can you get the ename sqlite log of the date when data changed?

> **Tovi Wang** (2025-02-06):
>   2024-09-20 & 2024-09-25 Ename API logs for your checking.Thanks!

> **Tovi Wang** (2025-02-06):
>  我在DB里发现 同一个vip_no_id '0018307333'    有2个vip no.vip_no_id是唯一值嘛？ J717WJ03463529 应该是J717 前台创建的，另一个 JXXXLJ00537648 应该是Ename 创建的。Please FYI。             

> **Anson Cheung** (2025-02-06):
>   I cannot find vip JXXXLJ00537648 or J717WJ03463529 in both ename log, is ename has log in two servers? vip_no_id is not unique.

> **Tovi Wang** (2025-02-06):
>  I  also NOT found the records in Ename log.As I know,AWS Ename log just in one server \\apawipwposweb25\APAWIPWPOSWEB25\eName\datastore\log So the change where come from?Interface file?

> **Anson Cheung** (2025-02-06):
>  what are the activated interfaces? As I know, most of the interfaces like My_einvoice.exe and CRMSanyoPhaseInterface.exe will not modify vip records.

> **Tovi Wang** (2025-02-06):
>  If have vipmaster interface file in JP？I know Ali have this interface.CRM update DB vip data by the interface.But I’m NOT sure JP if have relates interface?

> **Anson Cheung** (2025-02-06):
>   can you provide log of the interface?

> **Tovi Wang** (2025-02-08):
>  For J717WJ03463529，经过查询发现此会员名被更新过五次且都是在Ename上面更新的。详情和Ename log都已上传在description.请检查确认为什么同一个VIP no seq 会被不同的会员名使用？是客户操作问题还是Ename bug?Please confirm.Thanks!

> **Anson Cheung** (2025-02-10):
>  之前也發生過這種情況，是客戶沒有按照正常程序開啟ename create vip的版面，導致使用了同一個vip no。印象中以前有handle過這個問題，需要時間confirm

> **Tovi Wang** (2025-02-10):
>  之前Coach也call out过同样的问题，COach Jira ticket: CS-1183. 我们需要确认的是客户在什么情况下会做出来这样奇怪的操作，在QA是否可以reproduce这个issue？并且最终如何enhance Ename这一块避免客户再次做出这样的操作。  麻烦帮忙在QA测试是否可以reproduce这个issue?谢谢！ CC:        FYI

> **Cy Lau** (2025-02-10):
>  It could be reproduced in our QA. Steps :  Goto Create Member Page,Get a new MemberNo. Share to HomePage every time go to the same page with that MemberNo. , then create a new member. The details of the member would be always overwritten.

> **Tovi Wang** (2025-02-10):
>  Many Thanks for your double confirm and the reproduced steps.So is it a Ename bug?right? Next how can we enhance this section and avoid the same issue happend again?Please with high priority. BTW,Can we identify how many members was impacted(How many member data is incorrect for this issue)?

> **Cy Lau** (2025-02-10):
>   I would like to share about if talking about  Owing to unexpected operation from the SA, the overwritten happens , if you call it a bug then it would be. I would called not in coverage, enhancement would be needed. Next how can we enhance this section and avoid the same issue happend again?Please with high priority. Educating the SA to have proper operation steps . Ask the SA follow the proper operation steps Ask the SA using the MDM pushed ICON instead of adding the intermediate page to homescreen and reuse it. If about programming wise, a revamp of the ename from webpages to SPA would be suggested in order to avoiding SA using intermediate page but not from beginning. BTW,Can we identify how many members was impacted(How many member data is incorrect for this issue)?   any update audit

> **Cy Lau** (2025-02-11):
> thanks    operating on Tapestry QA environment :

> **Cy Lau** (2025-02-11):
> William Cai  added a comment -  Yesterday  - edited please identify the iPad doing this kind of operation, we need hard evidence of the url shortcut in that iPad, after take the evidence, need to delete the short cut to avoid further issue. IIS for the EName webpage hosting on those dates would provide the information with accessing IP, accessing path(with which member no.) if this is the case, that means this iPad only used once in several months (1/28/2024 4:03:10 PM and next time:  4/28/2024 6:49:13 PM), please verify with store staff, how this can be true. From the UI log (IP and storeCode) and IIS log with IP cross check would help. Next action : Get the IIS log for EName webhost(01,02) on specific dates.       The iPad doing this kind of operation , in application layer we could only

> **Andrew_Au** (2025-03-21):
>    The ticket pending for a long time. Please update the ticket status

> **Tovi Wang** (2025-03-21):
> this is coming from store operation. let's close ticket first and Coach team will prepare clear communication to store.

## 相關資訊

- **Jira:** [BE-1000](https://ctil.atlassian.net/browse/BE-1000)