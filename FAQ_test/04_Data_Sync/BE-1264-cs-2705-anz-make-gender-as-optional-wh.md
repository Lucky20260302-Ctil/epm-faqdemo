---
project: BE
title: "BE-1264: [CS-2705] ANZ - Make 'Gender' as optional when create new member"
issue_key: BE-1264
issue_type: Bug PRD
status: Open
faq_score: 6.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-1264"
created: 2026-05-11
resolved: 
resolution: 
has_images: False
---

# BE-1264: [CS-2705] ANZ - Make "Gender" as optional when create new member

## 問題描述

Current Gender field = M/ F/ C-Couple

Enhance programs for configurable gender option.

Coverage:

1. import from 3rd

2. upsert within sanyo modules

3. display & selections

4. posting




## Jira Comments

> **Joy Li** (2026-05-11):
> Copy from    最基本for UI :  JSON  :  {  "display" :  {   "zh-hk" : "",   "zh-tw" : "",   "zh-cn" : "",   "kr" : "",   "jp" : "",   "default" : "" }, "value" : "M" }

> **Joy Li** (2026-05-19):
> Phase_1: R41 FE: Member UI display (All regions) PCD generate (All regions) Member create\upsert process (All regions) MPOS: Member UI display (All regions) PCD generate (All regions) Member create\upsert process (All regions) BE: posting (All regions) VIP searching (All regions) CAR Interface (All regions) - Need to check with downsteam. C360Interface (AU NZ KSJ KAU KNZ) - Need to check with downsteam. WEB: C360 POS_API (AU NZ KSJ KAU KNZ) Phase 2: (TBC) BE: Memberson Interface (KSG, KMY) Acxiom CRM Interface (HK CN SG MY TW MO KR) WEB: eName (HK MO KR JP) BEAPICRM API (HK CN SG MY TW MO KR) Memberson API (KSG KMY)

## 相關資訊

- **Jira:** [BE-1264](https://ctil.atlassian.net/browse/BE-1264)