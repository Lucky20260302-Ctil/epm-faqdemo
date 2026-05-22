---
project: MP
issue_key: MP-808
issue_type: Task
status: Closed
faq_score: 4.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, mp, data_sync, mpos-api]
jira_url: "https://ctil.atlassian.net/browse/MP-808"
created: 2026-01-19
resolved: 2026-05-05
resolution: Done
has_images: True
---

# MP-808: [CoachANZ] MPOS Enhancements alignemtn with FEPOS

> **類型:** Task | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 4.5
> **解決日期:** 2026-05-05
> **負責人:** Sherman tse
> **組件:** MPOS API

## 問題描述

Based on MPOS 3.30.X, 

following should be enhanced for alignment with FEPOS : 

- [ ] Rounding method
- [ ] PCD 34 for C360
- [ ] Printing for PrtCompany = 'COAHCANZ'

References : 

> 📎 **image-20260119-073716.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/362c7528-45b6-4cee-b03a-8248c45f3b1d)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260119-073716.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/362c7528-45b6-4cee-b03a-8248c45f3b1d)


## Jira Comments

> **Cy Lau** (2026-01-19):
>   please help to check for the rounding would also take part in MPOS for UI 

> **Cy Lau** (2026-01-19):
> Rounding method PCD 34 for C360 Printing for PrtCompany = 'COAHCANZ' Coach ANZ C360 - New Member - Always call Web API Aync Upsert and write PCD 34 (WEBAPIUPDATENEWMEMBER = Y/N) (KTS 251219 FE-1821 v75.04R1x, v750.04R03) add tblconfig.NVIPInputCommOpt_DefaultNo - New Member 4 Communication Channel default Value y- Disable (Default N) (KTS 251125 FE-1811 v750.04R16, v750.05) Coach ANZ Default Tax Free Mode (add tblconfig.AutoTaxFreeMode ='Y') (KTS 251104 FE-1785 v750.04R14F, v750.05)

> **Cy Lau** (2026-01-19):
> ounding method PCD 34 for C360 Printing for PrtCompany = 'COAHCANZ' #1 ValidateMemberQRCode  #2 ChangeRound_Enable, ChangeRndDec #3 CoachANZ Printing

> **Cy Lau** (2026-01-19):
>   please compile and check with MPOS App

> **Daniel Leung** (2026-02-16):
> mpos: 3.31.0-20260225.1 mpos api : \\ds411\share\POS_MPOS_Release\3.31.X\3.31.0-20260226.1b1  

> **Automation for Jira** (2026-04-02):
> Issue has been created since Days since: 72 Week since : 10 Issue due date difference Days since : 69 Weeks since: 9

> **Andrew_Au** (2026-05-05):
>  Please update the ticket status

> **Sherman tse** (2026-05-05):
> Verified on QA

## 相關資訊

- **Jira:** [MP-808](https://ctil.atlassian.net/browse/MP-808)
- **解決方式:** Done