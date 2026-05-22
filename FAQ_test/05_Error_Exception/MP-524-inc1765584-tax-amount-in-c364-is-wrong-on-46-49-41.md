---
project: MP
issue_key: MP-524
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-524
created: '2022-05-18'
resolved: '2024-03-01'
fix_version: '3.19'
components:
- MPOS API
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

MP-524: INC1765584 Tax amount in C364 is wrong on 4/6, 4/9, 4/10, 4/11.4/12

## 症狀

C364 門店在套用備註層級 MM 折扣（10%）且交易包含兩個以上品項時，MPOS API 計算出的稅額錯誤。系統對優惠券品項錯誤計算 VAT，導致稅額與預期不符。

## 根因

MPOS API 在處理備註層級 MM 折扣時，誤將優惠券品項納入 VAT 計算（VAT calculate on coupon item），而優惠券品項不應產生 VAT。此問題與 FE-1117 為相同根因，影響所有 Front End 及 MPOS API 版本。

## 解法

已於 MPOS API 3.19 版本修正 VAT 計算邏輯，確保 MM 折扣情境下優惠券品項不納入 VAT 計算。可重現條件：兩個以上品項 + 備註層級 MM 折扣。

## 相關資訊

- Jira: [MP-524](https://ctil.atlassian.net/browse/MP-524)
- Fix Version: 3.19
- 解決日期: 2024-03-01
- 組件: MPOS API
- 負責人: Cy Lau
