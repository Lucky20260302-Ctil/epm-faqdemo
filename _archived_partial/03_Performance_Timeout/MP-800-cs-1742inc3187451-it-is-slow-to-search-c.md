---
project: MP
issue_key: MP-800
issue_type: Task
status: Awaiting Sprint Planning or Awaiting to do
tags:
- 03_performance_timeout
- faq
- mp
- mpos
- performance_timeout
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-800
created: '2025-09-18'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'MP-800: [CS-1742][INC3187451] It is slow to search customer on MPOS'
---
# MP-800: [CS-1742][INC3187451] It is slow to search customer on MPOS

## 問題描述

C312 store callout that it is slow to search customer on MPOS.
We import the Xconfig to skip the loadbalancer,but still callout the performance issue.

Sog confirm with store.
1, Lpos search and bind customer no need long time.
2, All the time show the same.
3, Mpos search customer need 6 second and bind it to sales need over 4 second and total need time 10-17 second.

Store provide the video as follow:(Video total spend 17 s)

> 📎 **IMG_0206.mov** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8e07a3dc-d76a-470f-adf8-4d79bf438f7f)（需 Jira 登入）

Troubleshooting:

"MobilePhone":"08026352908"

"vipmas_vip_code":"2022548494"

1.

MPOS API received the request：

2025-09-13 13:17:04.431 +08:00 [INF] MembersController.Get.Start()
2025-09-13 13:17:04.540 +08:00 [INF] MobileDC.Service.GetMembers.Start()
2025-09-13 13:17:04.540 +08:00 [INF] OnlineMemberEnquiry.Start()
2025-09-13 13:17:07.822 +08:00 [INF] OnlineMemberEnquiry.End(), 3285ms
2025-09-13 13:17:07.822 +08:00 [INF] MobileDC.Service.GetMembers.End(), 3285ms

> 📎 **屏幕截图 2025-09-18 154326.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e4232774-d92f-4f27-93ea-f80c4bdb9284)（需 Jira 登入）
2.

MPOS DAL log:

2025/09/13 13:17:04.540 [20250913 01:17:04] API Call: api/v1/Member/getMemberList
2025/09/13 13:17:06.236 [20250913 01:17:06] Result:SUCCESS

> 📎 **屏幕截图 2025-09-18 155227.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ec1b2620-9ad3-43dc-8d44-d05af9b5cb32)（需 Jira 登入）
3.

POS API log:

2025-09-13 13:17:04:5631   api/v1/Member/getMemberList     Request receive

2025-09-13 13:17:04:7568   api/v1/Member/getMemberList     Request C360 API

2025-09-13 13:17:06:2150   - api/v1/Member/getMemberList    Response C360 API

> 📎 **image-20250918-075656.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a934c09f-9ef7-4e84-afae-355e94cb2310)（需 Jira 登入）
4.

MPOS DAL log:

2025/09/13 13:17:06.236 [20250913 01:17:06] API Call: api/v1/Member/getMemberDetails
2025/09/13 13:17:07.822 [20250913 01:17:07] Result:SUCCESS

POS API log:

2025-09-13 13:17:06:2479    api/v1/Member/getMemberDetails     Request receive

2025-09-13 13:17:06:4443    api/v1/Member/getMemberDetails     Request C360 API

2025-09-13 13:17:06:6880    api/v1/Member/getMemberDetails     Response C360 API

> 📎 **image-20250918-094135.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4c83c0e8-1217-4e37-9f60-63922481b667)（需 Jira 登入）



## 附件截圖

1. 📎 **IMG_0206.mov** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8e07a3dc-d76a-470f-adf8-4d79bf438f7f)
2. 📎 **屏幕截图 2025-09-18 154326.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e4232774-d92f-4f27-93ea-f80c4bdb9284)
3. 📎 **屏幕截图 2025-09-18 155227.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ec1b2620-9ad3-43dc-8d44-d05af9b5cb32)
4. 📎 **image-20250918-075656.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a934c09f-9ef7-4e84-afae-355e94cb2310)
5. 📎 **image-20250918-094135.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4c83c0e8-1217-4e37-9f60-63922481b667)

## 相關資訊

- **Jira:** [MP-800](https://ctil.atlassian.net/browse/MP-800)