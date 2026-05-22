---
project: FE
issue_key: FE-1117
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1117
created: '2022-05-18'
resolved: '2022-05-31'
fix_version: V720.02R16E
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
---
FE-1117: INC1765584 Tax amount in C364 is wrong on 4/6, 4/9, 4/10, 4/11.4/12

| 問題
門店 C364 在 4/6、4/9、4/10、4/11、4/12 的稅額計算錯誤。當交易包含兩個以上品項且套用備註層級 MM 折扣（10%）時，系統對優惠券品項錯誤計算 VAT，導致稅額偏高。

| 根因
備註層級 MM 折扣（Memo level MM discount）套用時，系統誤將優惠券品項納入 VAT 計算範圍（VAT calculate on coupon item），而實際上優惠券品項不應該產生 VAT。此問題同時影響含 MM Coupon 及不含 MM Coupon 的一般銷售情境。

| 解法
已於 V720.02R16E 版本修正 VAT 計算邏輯，確保 MM 折扣情境下不再對優惠券品項計算 VAT。可重現條件：兩個以上品項 + 備註層級 MM 折扣 10%。

| 相關資訊
- Jira: [FE-1117](https://ctil.atlassian.net/browse/FE-1117)
- Fix Version: V720.02R16E
- 解決日期: 2022-05-31
- 組件: Front End
- 負責人: Sang
- 附件: [RE  INC1765584 Tax amount in C364 is wrong on 4 6  4 9  4 10  4 11 4 12 .msg](https://ctil.atlassian.net/rest/api/3/attachment/content/37598) | [Revised Program result.png](https://ctil.atlassian.net/rest/api/3/attachment/content/37607) | [RE  Wrong Tax and Sales value of 46 transactions for C364 .msg](https://ctil.atlassian.net/rest/api/3/attachment/content/37602) | [Test case [FE-1117].docx](https://ctil.atlassian.net/rest/api/3/attachment/content/37614)