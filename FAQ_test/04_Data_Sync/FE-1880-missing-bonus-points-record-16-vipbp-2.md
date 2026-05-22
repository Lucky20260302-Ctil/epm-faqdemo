---
project: FE
issue_key: FE-1880
issue_type: Bug PRD
status: Open
faq_score: 6.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end-v750.01r01a]
jira_url: "https://ctil.atlassian.net/browse/FE-1880"
created: 2026-02-09
resolved: 
resolution: 
has_images: True
---

# FE-1880: Missing Bonus Points record 16- vipbp & 20 - ptsanly

> **類型:** Bug PRD | **狀態:** Open
> **分類:** 資料與同步 | **FAQ 分數:** 6.0
> **負責人:** Joy Li
> **組件:** Front End v750.01R01A

## 問題描述


> 📎 **image-20260209-035435.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/66a36818-543d-4979-95f1-dbdee5a90c18)（需 Jira 登入）

The memos KSSTPE05 - 00006958 to 00006961 are missing the bonus points (record 16) and bonus points item earned (record 20).



## 附件截圖

1. 📎 **image-20260209-035435.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/66a36818-543d-4979-95f1-dbdee5a90c18)


## Jira Comments

> **Bobby** (2026-02-09):
> Attached pcd file for your reference.

> **Bobby** (2026-02-09):
> This is the manual fixed pcd file for your reference.     

> **Sang** (2026-02-09):
>  this 2026.01.29 file indicated that pos version is 710.02R14zp, Jira indicate  affect  version is.v75. Please verify. Is this a new rule? Please copy dbtrans, dbhist.sdf, dbmas / mastconv and 2026.01.29 logs. 

> **Bobby** (2026-02-09):
>   please confirm the POS version of KSSTPE05 Till 0 and get the log files as per Sang request. Thanks.

> **Joy Li** (2026-02-09):
>     Please found the attached zback folder from KSSTPE05 till 0. Version is Ver. 7.1.0.02R14ZP  ImagineX

> **Sang** (2026-02-09):
>  Please copy dbtrans.sdf, dbhist.sdf and dbMas or mastconv also

## 相關資訊

- **Jira:** [FE-1880](https://ctil.atlassian.net/browse/FE-1880)
- **標籤:** POSTING