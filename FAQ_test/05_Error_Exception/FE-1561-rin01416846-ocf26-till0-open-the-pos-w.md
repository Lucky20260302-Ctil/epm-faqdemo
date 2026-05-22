---
project: FE
title: "FE-1561: RIN01416846 - OCF26 Till0 Open the POS will show the 'TBLSALADY - 字段大小过长' this error"
issue_key: FE-1561
issue_type: Bug PRD
status: Closed
faq_score: 5.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1561"
created: 2024-11-15
resolved: 
resolution: 
has_images: True
---

# FE-1561: RIN01416846 - OCF26 Till0 Open the POS will show the "TBLSALADY - 字段大小过长" this error

## 問題描述

1.店铺在2024-11-11重装过POS后，每次打开POS的时候会有如下截图的小提示，点击‘确认’可以跳过。请检查确认如何能取消掉下面的小弹窗？是什么地方导致的这个issue？

> 📎 **image-20241115-024705.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/2e6ec3b4-503a-4a34-b888-b0ecf12345e1)（需 Jira 登入）
Troubleshooting in my side:

1.repaired POS program and reg reg,Issue still.

2.Checked the Tblsalady table in Dbsse and Dbtrans.sdf,Not found any abnormal.

3.Checked the AdoService log found bellow error.What’s this error?

> 📎 **image-20241115-031029.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/08e05931-3010-4f1f-bb8d-c52471599aa2)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20241115-024705.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2e6ec3b4-503a-4a34-b888-b0ecf12345e1)
2. 📎 **image-20241115-031029.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/08e05931-3010-4f1f-bb8d-c52471599aa2)

## 相關資訊

- **Jira:** [FE-1561](https://ctil.atlassian.net/browse/FE-1561)