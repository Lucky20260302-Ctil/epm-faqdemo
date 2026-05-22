---
project: MP
issue_key: MP-832
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, mp, performance_timeout, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-832"
created: 2026-04-29
resolved: 
resolution: 
has_images: True
---

# MP-832: INC3550023 - Exchange memo NOT linked to Original sales memo

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 7.5
> **負責人:** Joy Li
> **組件:** MPOS

## 問題描述

Symptom:
Store callout when doing Exchange memo OC516-MA013763，Input the Original sales memo OC16-30038860.But Original sales memo not diplayed in PC file and BE DB.Please help to double check the MPOS UI log to find the [RCA.Is](http://RCA.Is) it store mis-operation or other issue?Thanks!

1.From MPOS UI log,We can see the return item CCY30 records. 

2026-04-20 19:37:19.574 +08:00 [INF] Result:退貨
2026-04-20 19:37:19.574 +08:00 [INF] SecurityController.GetSecurityTitle?secCode:SAL00005.End(),3ms
2026-04-20 19:37:28.037 +08:00 [INF] SecurityController.SecurityChecking?secCode:SAL00005;userCode:604082.Start()
2026-04-20 19:37:29.348 +08:00 [INF] Result:True
2026-04-20 19:37:29.348 +08:00 [INF] SecurityController.SecurityChecking?secCode:SAL00005;userCode:604082.End(),1306ms
2026-04-20 19:37:49.933 +08:00 [INF] SalesMemosController.GetReturnPrice?memoLoc:OC16;memoNo:30038860;itemNo:CCY30;color:B4YTH;size:;inseam:;isTaxEampt:False

> 📎 **image-20260429-102743.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/6561a9ab-0586-404c-b1cb-9f7395a6aebd)（需 Jira 登入）

2.Original sales memo is OC16-30038860

> 📎 **image-20260429-102706.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/da3fff54-1ee6-49e8-bd82-fe440e7f18aa)（需 Jira 登入）

3.Exchange sales memo is OC516-MA013763

> 📎 **image-20260429-102412.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/6028c3bb-71a6-4d64-bbd4-0250bb344e9f)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260429-102743.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/6561a9ab-0586-404c-b1cb-9f7395a6aebd)
2. 📎 **image-20260429-102706.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/da3fff54-1ee6-49e8-bd82-fe440e7f18aa)
3. 📎 **image-20260429-102412.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/6028c3bb-71a6-4d64-bbd4-0250bb344e9f)

## 相關資訊

- **Jira:** [MP-832](https://ctil.atlassian.net/browse/MP-832)