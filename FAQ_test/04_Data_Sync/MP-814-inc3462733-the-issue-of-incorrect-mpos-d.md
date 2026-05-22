---
project: MP
title: "MP-814: [INC3462733] The issue of incorrect MPOS date on MPOS memo"
issue_key: MP-814
issue_type: Bug PRD
status: Closed
faq_score: 5.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, mp, data_sync, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-814"
created: 2026-02-27
resolved: 
resolution: 
has_images: True
---

# MP-814: [INC3462733] The issue of incorrect MPOS date on MPOS memo

## 問題描述

@@Sang J364 店铺反馈 2026-02-23创建三笔MPOS销售，但是MPOS date 却显示 2026-02-22。请帮忙查询RCA.什么情况下会发生这种情况？谢谢！

根据我的理解，MPOS的销售日期是根据 Till0 POS date走的。说明店铺2026-02-23创建这三笔MPOS销售的时候，POS date当时显示是 2026-02-22。但我查询2026-02-22 日结已正常完成.

J364-MB002725，create time: 2026-02-23 12:35
J364-MA003745，create time: 2026-02-23 12:04
J364-MC002018，create time: 2026-02-23 14:34

[1.BE](http://1.BE) capture

> 📎 **image-20260227-100210.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f384a888-426a-4e4d-9ae1-8a6759dadc6f)（需 Jira 登入）
2.查询T9 log如下图：

> 📎 **image-20260227-100941.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/be96d44f-95e9-44b9-8fae-6c6ba6051018)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260227-100210.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f384a888-426a-4e4d-9ae1-8a6759dadc6f)
2. 📎 **image-20260227-100941.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/be96d44f-95e9-44b9-8fae-6c6ba6051018)


## Jira Comments

> **Tovi Wang** (2026-02-27):
>  22 Feb & 23 Feb till0 logs for your further checking. CC       

> **Automation for Jira** (2026-03-03):
> Issue has been created since Days since: 3 Week since : 0 Issue due date difference Days since :  Weeks since: 

> **Tovi Wang** (2026-03-04):
> Store not open cs2000 on 02-23 morning.update the details to SOG & Coach team.Can be closed first.

## 相關資訊

- **Jira:** [MP-814](https://ctil.atlassian.net/browse/MP-814)