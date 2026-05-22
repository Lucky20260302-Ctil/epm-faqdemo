---
project: BE
title: "BE-1008: BE v7 User Password Restricted Keyword and User Password Policy pointing to wrong DB."
issue_key: BE-1008
issue_type: Bug PRD
status: HOLD
faq_score: 6.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-1008"
created: 2025-02-21
resolved: 
resolution: 
has_images: True
---

# BE-1008: BE v7 User Password Restricted Keyword and User Password Policy pointing to wrong DB. 

## 問題描述

Tapestry’s Mason reports that he cannot see the User Password Policy and User Password Restrict Keyword in Backend after migrated to v7. I have checked that they have the data in pwrestkw, pwpolicy and pwhistlg tables under csdata10_70 database. The data is migrated from v66 to v7. However, I checked the User Password Restricted Keyword (GL5000) and User Password Policy (GL5002) are referring to glpwrestkw, glpwpolicy and dbpwhistlg tables under gldata database. I suspect this function is whether work or not in BE v7. Could you check is there any BE function is accessing the tables in csdata database? 

> 📎 **image-20250221-042244.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f69c40ee-584a-461b-b41f-c7761a6eaf6a)（需 Jira 登入）
I expect these functions should refer to csdata database rather than gldata database. Because the policy or restricted keyword may not same for each region. 



## 附件截圖

1. 📎 **image-20250221-042244.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f69c40ee-584a-461b-b41f-c7761a6eaf6a)

## 相關資訊

- **Jira:** [BE-1008](https://ctil.atlassian.net/browse/BE-1008)