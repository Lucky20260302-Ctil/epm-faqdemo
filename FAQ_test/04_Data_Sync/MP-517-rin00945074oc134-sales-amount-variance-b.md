---
project: MP
title: "MP-517: [RIN00945074][OC134] Sales Amount variance between POS and MPOS"
issue_key: MP-517
issue_type: Bug PRD
status: Closed
faq_score: 8.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, mp, data_sync, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-517"
created: 2022-03-09
resolved: 2024-11-06
resolution: Done
has_images: False
---

# MP-517: [RIN00945074][OC134] Sales Amount variance between POS and MPOS

## 問題描述

Coach China, OC134, user reported Final sales amount MPOS is not the same as POS
Refer to sales memo OC1134 - MA000797, the calculation will be like that by applying all 3 coupons: 
$(6150*0.9) - $300 - $500 = $4735
The sales amount is $4735 which user thinks it is correct amount.

However, when user want to apply those 3 coupons on POS, the discount is not the same as MPOS.
Refer to POS screenshot, the discount of Coupon “PVIU_V” is $115.00 only.
Checked BEUI, Coupon “PVIU_V” should apply for List Price or Non-Discount Price only.

Customer: Coach - CN
VIP: OC1340C00013864
Mpos Sales: MA000797
Date: 2022-03-05
SKU: 

- C8952 L50^0

- C0135 B45BV

Promotion:

- WOMENDAY500E,

- PVIU_V,

- RetailWD300

Coupon:

1. WOMENDAY500E --> -$500 if sales amount reaches $5000
2. PVIU_V --> - 10% of List Price
3. RetailWD300 --> -$300

MPOS:
6150*0.9= 5535.
5535-300-800= $4735

POS:
Total List Price: $6,150
Total Discount: $(500 + 115 + 300) = $915
Final Amount: $5,235

Discussed with Sang, different sorting of Coupons will lead to different sales memo;

- POS: PVIU_V --> WOMENDAY500E --> RetailWD300

- MPOS: WOMENDAY500E --> PVIU_V --> RetailWD300
 

dbtrans.SDF: Log_cs2000pos_retdata6 

File Path: [\\172.16.183.201\localuser\support\20211011\ToSang\OC134\OC134_promotion_20220305\Log_cs2000pos_retdata6](http://example.com/)



## 相關資訊

- **Jira:** [MP-517](https://ctil.atlassian.net/browse/MP-517)
- **解決方式:** Done