---
project: "MP"
issue_key: "MP-649"
issue_type: "Bug PRD"
status: "Closed"
tags: [faq, mp]
jira_url: "https://ctil.atlassian.net/browse/MP-649"
created: "2023-04-27"
resolved: "2024-08-30"
fix_version: "3.29.1"
components: [MPOS API]
category: "07_Workflow_Business"
---

MP-649: L1010B Coupon Discount Variance

| 問題
在MPOS交易中使用L1010B折價券時出現折扣金額差異，導致結帳金額與預期不符，影響交易正確性。

| 根因
MPOS在處理折價券時，未驗證輸入的折價券編號、VIP類型或商品編號與系統處理後的結果是否一致，導致資料比對不符時仍繼續完成交易，產生金額差異。

| 解法
更新至MPOS 3.29.1版本（20240821），該版本新增交易前驗證中止機制：當輸入與處理後的折價券編號、VIP類型或商品編號不符時，系統將自動中止交易，防止金額差異問題發生。

| 相關資訊
- Jira: [MP-649](https://ctil.atlassian.net/browse/MP-649)
- Fix Version: 3.29.1
- 解決日期: 2024-08-30
- 組件: MPOS API
- 負責人: Cy Lau