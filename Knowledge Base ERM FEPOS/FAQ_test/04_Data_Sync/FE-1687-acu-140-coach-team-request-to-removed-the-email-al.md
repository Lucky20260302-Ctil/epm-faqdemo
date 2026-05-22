---
project: "FE"
issue_key: "FE-1687"
issue_type: "Bug PRD"
status: "Closed"
tags: [faq, fe]
jira_url: "https://ctil.atlassian.net/browse/FE-1687"
created: "2025-05-08"
resolved: ""
fix_version: ""
components: [API]
category: "04_Data_Sync"
---

FE-1687: Coach Team request to removed the Email alert for the CRM return "ERROR|CDP-CUST-404|Customer not found"

| 問題
Coach 品牌 POS 在查詢會員時，若 CRM API 回傳「ERROR|CDP-CUST-404|Customer not found」（客戶不存在），系統會持續發送 Email 警報通知。此為正常業務流程（客戶確實不存在於 CRM），不應觸發警報，造成运维人員收到大量不必要的告警郵件。

| 根因
BEAPICRM 舊版本對 CRM API 回傳的 HTTP 200 但內容為 Customer not found 的回应，仍視為異常並觸發 Email 警報。實際上 CRM 找不到客戶屬於正常業務場景，不應發送警報。

| 解法
將 BEAPICRM 更新至 ver1.17.17（build no. dd1948a1）或更新版本，該版本已移除對 404 Customer not found 的 Email 警報通知。更新後不再收到此類告警郵件。

| 相關資訊
- Jira: [FE-1687](https://ctil.atlassian.net/browse/FE-1687)
- 組件: API
- 負責人: Anson Cheung
- 附件: [build.txt](https://ctil.atlassian.net/rest/api/3/attachment/content/56340) | [image-20250508-020216.png](https://ctil.atlassian.net/rest/api/3/attachment/content/56244) | [image-20250508-020248.png](https://ctil.atlassian.net/rest/api/3/attachment/content/56243) | [image-20250508-020316.png](https://ctil.atlassian.net/rest/api/3/attachment/content/56245) | [image-20250508-020343.png](https://ctil.atlassian.net/rest/api/3/attachment/content/56242)