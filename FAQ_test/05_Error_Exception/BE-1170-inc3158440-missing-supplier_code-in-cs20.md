---
project: BE
issue_key: BE-1170
issue_type: Task
status: Open
tags:
- 05_error_exception
- be
- data-interface
- error_exception
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1170
created: '2025-08-27'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-1170: [INC3158440] Missing supplier_code in CS2000 BE after imported ItemMaster interface file to BE with supp_code'
---
# BE-1170: [INC3158440] Missing supplier_code in CS2000 BE after imported ItemMaster interface file to BE with supp_code

## 問題描述

Coach Team imported ItemMaster interface file to BE with supp_code,But it is missing supplier_code in CS2000 BE and NOT any error.

Troubleshooting:

I also double test to re-import the item CAK90 with supplier_code, but BE still did not show the supp_code, And there were no errors on BE, but the import was successful. (Please view the attachment:MASTERITEM_20250825000088.DAT)

 [📎附件](https://ctil.atlassian.net/rest/api/3/attachment/content/20249ef7-ae91-4b5e-bf38-f5fb3d36144d) 

@@Jerry Wong Could you help to double check and confirm why the supp_code can’t reflect to BE?Thanks!

CC @@Joy Li @@Cy Lau FYI.

> 📎 **image-20250827-125128.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7902a774-afde-409a-b0f6-9c390e9b345e)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250827-125128.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7902a774-afde-409a-b0f6-9c390e9b345e)

## 相關資訊

- **Jira:** [BE-1170](https://ctil.atlassian.net/browse/BE-1170)