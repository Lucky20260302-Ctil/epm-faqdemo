---
project: FE
title: "FE-1808: [CS-1870][INC3295770] PRC POSv75 OCF12till0, print sales memos cost frequently 5~10 sec."
issue_key: FE-1808
issue_type: Bug DEV
status: Open
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end-v750.01r01a]
jira_url: "https://ctil.atlassian.net/browse/FE-1808"
created: 2025-11-14
resolved: 
resolution: 
has_images: True
---

# FE-1808: [CS-1870][INC3295770] PRC POSv75 OCF12till0, print sales memos cost frequently 5~10 sec.

## 問題描述

[INC3295770] PRC POSv75 OCF12till0, print sales memos cost frequently 5~10 sec.

checked in T9 logs ,it shows no error.

> 📎 **dee27648-f04d-4eee-a241-ef0e3092a4b5.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/eced7e63-6f32-4031-8df6-e2aaf197f729)（需 Jira 登入）

> 📎 **ab77ee3e-be2a-4448-b559-2d30bee15db6.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3c880617-7844-4eaf-b83b-379a37cb5b8b)（需 Jira 登入）

> 📎 **28d0c38c-f3c9-45b4-a917-bade9017ac33.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/5bd16b00-b27e-4027-8542-20a0ffa1a7cd)（需 Jira 登入）

> 📎 **42cf1db2-eaf8-41ab-91f2-4d7f7282685a.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/37ef9136-6fb1-4d88-aa33-5b0e30e1022c)（需 Jira 登入）

> 📎 **07913b66-f8fb-46e5-87b1-9aadaf8c9c18.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ac90441e-1f4f-4e03-8180-0d997e09b0b4)（需 Jira 登入）
Normally, it should be only cost 3-5 sec.

> 📎 **image-20251114-070609.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/803d4475-ceff-4b3f-a053-a2fb3d8efdb3)（需 Jira 登入）

> 📎 **image-20251114-070547.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/61ae5065-c819-4d07-ac88-5a92a9ed3f03)（需 Jira 登入）

<u>[INC3306646](https://tapestry.service-now.com/incident.do?sys_id=4ef05bad47d93e5498ab0694f16d4336&sysparm_record_target=incident&sysparm_record_row=6&sysparm_record_rows=9&sysparm_record_list=assignment_group.nameSTARTSWITHSanyo+support+team%5EstateNOT+IN6%2C7%5Eu_cancel%3Dfalse%5EparentISEMPTY%5EORDERBYshort_description)</u> PRC OCF39 打印有正常也有异常的，从百旺拿qrcode信息，一般3-5秒，此外打印所用时间大概再5-15秒之间。
这个issue跟INC3295770 OCF12类似的。

> 📎 **58b79df8-d630-4538-ac10-84ac8cc18c0a.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/645f868d-88d8-48cc-b3ae-794dcc43bb53)（需 Jira 登入）

> 📎 **33fc9042-df9c-448a-90ac-a4e37370fb6b.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/14632d74-2d50-4256-9fed-f057aafb27db)（需 Jira 登入）

> 📎 **9265cb57-090c-4f99-b7f7-d5fcec86e33b.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/cfd1de8e-4fcc-4a5a-bf42-571ce23b70e3)（需 Jira 登入）

> 📎 **b6ccaaf9-814b-4490-84cb-ae9c4c428c7b.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/88bff436-7c21-4cb3-a932-33a74736dc3b)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4c9f7596-f639-48f2-ae7a-edd3f51b1f70)（需 Jira 登入）



## 附件截圖

1. 📎 **dee27648-f04d-4eee-a241-ef0e3092a4b5.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/eced7e63-6f32-4031-8df6-e2aaf197f729)
2. 📎 **ab77ee3e-be2a-4448-b559-2d30bee15db6.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3c880617-7844-4eaf-b83b-379a37cb5b8b)
3. 📎 **28d0c38c-f3c9-45b4-a917-bade9017ac33.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/5bd16b00-b27e-4027-8542-20a0ffa1a7cd)
4. 📎 **42cf1db2-eaf8-41ab-91f2-4d7f7282685a.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/37ef9136-6fb1-4d88-aa33-5b0e30e1022c)
5. 📎 **07913b66-f8fb-46e5-87b1-9aadaf8c9c18.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ac90441e-1f4f-4e03-8180-0d997e09b0b4)
6. 📎 **image-20251114-070609.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/803d4475-ceff-4b3f-a053-a2fb3d8efdb3)
7. 📎 **image-20251114-070547.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/61ae5065-c819-4d07-ac88-5a92a9ed3f03)
8. 📎 **58b79df8-d630-4538-ac10-84ac8cc18c0a.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/645f868d-88d8-48cc-b3ae-794dcc43bb53)
9. 📎 **33fc9042-df9c-448a-90ac-a4e37370fb6b.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/14632d74-2d50-4256-9fed-f057aafb27db)
10. 📎 **9265cb57-090c-4f99-b7f7-d5fcec86e33b.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/cfd1de8e-4fcc-4a5a-bf42-571ce23b70e3)
11. 📎 **b6ccaaf9-814b-4490-84cb-ae9c4c428c7b.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/88bff436-7c21-4cb3-a932-33a74736dc3b)
12. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4c9f7596-f639-48f2-ae7a-edd3f51b1f70)

## 相關資訊

- **Jira:** [FE-1808](https://ctil.atlassian.net/browse/FE-1808)