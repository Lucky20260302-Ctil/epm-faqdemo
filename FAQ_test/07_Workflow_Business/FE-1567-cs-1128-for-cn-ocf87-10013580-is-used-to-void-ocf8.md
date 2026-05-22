---
project: FE
issue_key: FE-1567
issue_type: Bug PRD
status: Closed
tags:
- 07_workflow_business
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1567
created: '2024-11-21'
resolved: '2025-03-20'
fix_version: ''
components:
- Deposit
- Payment
- Sales
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: complete
---
FE-1567: For CN OCF87-10013580 is used to void OCF87-10013577 on 2024-08-09, why payment amount is -2568 for 10013580 ?

| 問題
使用 LGV 付款方式結算 Deposit 並搭配 MM Coupon 折抵餘額時，系統未能正確處理溢收金額，導致付款金額顯示異常（如出現負數金額），前台與後台資料不一致。

| 根因
當 Deposit 結算使用 MM Coupon 折抵餘額後淨額為零，再以 LGV（房東禮券）付款時，POS 未正確判斷已無需找零的狀態，允許輸入 LGV 金額但未顯示溢收金額且不允許現金找零，導致付款記錄異常。

| 解法
升級至 v750.04R11（或 v750.05），修正 Deposit Settlement 使用 MM Coupons 折抵餘額時避免在無需找零下輸入 LGV 付款。修復後當 Purchase $1500、Deposit $1400、Balance $100 以 MM Discount $100 折抵至 $0，再使用 LGV $1400 時，系統將正確顯示 Excess Change $1400 並提示 LGV Tender 不允許現金找零。

| 相關資訊
- Jira: [FE-1567](https://ctil.atlassian.net/browse/FE-1567)
- 解決日期: 2025-03-20
- 組件: Deposit, Payment, Sales
- 負責人: Sherman tse
- 附件: [image-20241121-021722.png](https://ctil.atlassian.net/rest/api/3/attachment/content/48507) | [image-20241121-021911.png](https://ctil.atlassian.net/rest/api/3/attachment/content/48506) | [image-20241121-022358.png](https://ctil.atlassian.net/rest/api/3/attachment/content/48508) | [image-20241121-025721.png](https://ctil.atlassian.net/rest/api/3/attachment/content/48509) | [image-20241121-031347.png](https://ctil.atlassian.net/rest/api/3/attachment/content/48515)