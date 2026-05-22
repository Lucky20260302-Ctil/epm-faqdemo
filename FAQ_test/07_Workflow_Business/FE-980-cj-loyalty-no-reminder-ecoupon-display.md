---
project: FE
issue_key: FE-980
issue_type: Bug QA
status: Closed
tags:
- 07_workflow_business
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-980
created: '2021-06-15'
resolved: '2022-08-18'
fix_version: ''
components:
- Frontend
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: complete
---
FE-980: CJ Loyalty - no Reminder eCoupon display

| 問題
當使用者點擊PAY按鈕進入付款畫面時，即使客戶擁有可用的eCoupon，FE POS不會跳出提醒訊息框詢問使用者是否使用eCoupon。

| 根因
Coach版本v720.02R09之前的版本未正確處理eCoupon提醒的顯示邏輯，導致系統無法偵測並提示可用的eCoupon。

| 解法
更新至Coach v720.02R09修補程式版本（20210620）即可正常顯示eCoupon提醒訊息。

| 相關資訊
- Jira: [FE-980](https://ctil.atlassian.net/browse/FE-980)
- 解決日期: 2022-08-18
- 組件: Frontend
- 負責人: howard
- 附件: [image-2021-06-15-10-41-49-167.png](https://ctil.atlassian.net/rest/api/3/attachment/content/37386) | [image-2021-06-15-10-43-25-317.png](https://ctil.atlassian.net/rest/api/3/attachment/content/37394) | [image-2021-06-21-10-44-04-867.png](https://ctil.atlassian.net/rest/api/3/attachment/content/37395)