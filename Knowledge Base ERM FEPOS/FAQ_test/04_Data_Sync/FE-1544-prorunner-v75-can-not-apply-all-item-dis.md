---
project: FE
issue_key: FE-1544
issue_type: Bug PRD
status: Closed
faq_score: 6.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1544"
created: 2024-10-31
resolved: 2024-12-24
resolution: Done
has_images: False
---

# FE-1544: ProRunner V75 can not apply all item discount

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 6.0
> **解決日期:** 2024-12-24
> **負責人:** Sang
> **組件:** Front End

## 問題描述

I have copied the full set data in below VM, please help to check why it cant apply the total memo 10% discoun

VM 172.16.138.104

Login .\sxd

password :P@ssw0rd




## Jira Comments

> **Jason Wu** (2024-10-31):
> 

> **Sang** (2024-10-31):
> Original Setting

> **Sang** (2024-10-31):
> Change MixTable_Disc_Perc=10

> **Jason Wu** (2024-11-07):
> Hi   , I checked and confirmed that the issue is not related to Zlog. It appears that the problem lies with  Dbtrans.sdf  when the POS is processing the coupon Zlog. Here are the conditions I tested: P05 = Dbtrans that does not work P01 = Working Dbtrans All testing Dbmas files have been purged. Use P05 Dbtrans to update masconv & zlogs : Failed Use P05 Dbtrans to update masconv & zlogs, then switch to P01 Dbtrans : Failed Use P05 Dbtrans with P01 config (Tblconfig & Tblsyscon) to update masconv & zlogs : Failed Use P01 Dbtrans to update masconv & zlogs : Success Use P01 Dbtrans to update masconv & zlogs : Success Use P01 Dbtrans with P05 config (Tblconfig & Tblsyscon) to update masconv & zlogs : Success Both Dbtrans are able to upload the promotion to display in below screen POS login  Us

> **Sang** (2024-11-18):
> v750.04R05B Fix Only have one Effective Memo Level MM rule w/o item MM rule fail to provide MM disc Bug(KTS 241118 v750.04R05B, v750.05)

> **Jason Wu** (2024-11-21):
>   Please help to have a test on it.

> **Andy Ko** (2024-11-22):
> newtonsoft error. env: 172.16.138.104 login:    .\sxd  |  P@ssw0rd@09

> **Andy Ko** (2024-11-22):
> env: 172.16.138.104 login: .\sxd | P@ssw0rd@09 update files:  \\ds411\share\POS_FE_Release_64\20241118 ProRunner v750.04R05B

## 相關資訊

- **Jira:** [FE-1544](https://ctil.atlassian.net/browse/FE-1544)
- **解決方式:** Done