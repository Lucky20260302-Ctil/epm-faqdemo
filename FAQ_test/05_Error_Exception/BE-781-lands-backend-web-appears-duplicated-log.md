---
project: BE
title: "BE-781: [Lands] BackEnd Web appears duplicated log in Interface Update Log Enquiry (SE8008)"
issue_key: BE-781
issue_type: Bug QA
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-781"
created: 2023-07-18
resolved: 2023-08-01
resolution: Done
has_images: True
---

# BE-781: [Lands] BackEnd Web appears duplicated log in Interface Update Log Enquiry (SE8008)

## 問題描述

VM: 172.16.138.65

[https://172.16.138.65/EnterpriseSystemAPI/swagger/index.html](https://172.16.138.65/EnterpriseSystemAPI/swagger/index.html)

Reproduce steps:

Execute import log API: /api/v1/ImportLog for **1 time** with 1753 yr

{
"data": [
{
"importEndDateTime": "1753-07-18T08:14:38.674Z",
"errMessage": "test1753",
"successfulCount": 0,
"failCount": 0,
"totalCount": 0,
"lineErrs": [
{
"lineNo": 0,
"errMessage": "test1753"
}
],
"filename": "test1753",
"importStartDateTime": "1753-07-18T08:14:38.674Z",
"fileDateTime": "1753-07-18T08:14:38.674Z"
}
]
}

 

Existing result:

BackEnd Web appears duplicated log in Interface Update Log Enquiry (SE8008)

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e32421ce-7ebf-46fa-babc-a31d746ebc0a)（需 Jira 登入）
Remark:

Issue seems occurs in inputing 1753 yr only



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e32421ce-7ebf-46fa-babc-a31d746ebc0a)

## 相關資訊

- **Jira:** [BE-781](https://ctil.atlassian.net/browse/BE-781)
- **解決方式:** Done