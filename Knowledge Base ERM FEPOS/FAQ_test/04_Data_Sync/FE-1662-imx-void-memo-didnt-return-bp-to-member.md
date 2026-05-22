---
project: FE
issue_key: FE-1662
issue_type: Bug PRD
status: Closed
faq_score: 8.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1662"
created: 2025-03-28
resolved: 2025-09-30
resolution: Done
has_images: True
---

# FE-1662: IMX void memo didnt return BP to member

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 8.0
> **解決日期:** 2025-09-30
> **負責人:** Jerry Wong
> **組件:** Front End

## 問題描述

Please reference the member have 2 sales & 1 void, but in the vipmovent dont have the void BP record,
Log copied in 
\\172.16.183.201\localuser\support\20250328\IMX_BP.zip

> 📎 **image-20250328-034502.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9a6f410a-eb26-4207-a0cb-a8f511c04c73)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250328-034502.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9a6f410a-eb26-4207-a0cb-a8f511c04c73)


## Jira Comments

> **Jason Wu** (2025-04-01):
> I added the BE posting error; it likely looks like the void discount record can not be posted to BE.

> **Jason Wu** (2025-04-01):
>   seems like the void memo missed the line 24/25,attetchd the PC file & the Dbtrans, please help to have a look

> **Sang** (2025-04-02):
>  please get 2025.03.01 dbtrans, PC file and log from BPSHKG35

> **Sang** (2025-04-02):
>  Void Memo does not write 24/25. Return Redeem Pts write adjusted as PCD ‘36’ . Please compare with 25.03.31 Void Memo #00042704    

> **Andrew_Au** (2025-08-28):
>     Did you know the ticket status ? Could we change the ticket status to close

> **Automation for Jira** (2025-09-30):
> Issue has been created since Days since: 185 Week since : 26 Issue due date difference Days since :  Weeks since: 

## 相關資訊

- **Jira:** [FE-1662](https://ctil.atlassian.net/browse/FE-1662)
- **解決方式:** Done