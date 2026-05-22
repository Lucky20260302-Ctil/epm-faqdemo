---
project: MPOS
issue_key: MP-747
issue_type: Bug PRD
status: Closed
tags: [faq, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-747"
created: 2025-02-17
resolved: 2025-05-02
fix_version: ""
components: ["Frontend"]
---

# MP-747: [MPOS-77] MPOS 3.29.5 - CN Region, unable to check the purchase history for CRM Member

## 問題

在中國區域（CN Region）啟用SalesHub的MPOS環境中，選取CRM會員後無法查看購買歷史記錄（Purchase History）。後續測試中又出現會員檔案顯示404錯誤，以及別名（Alias）顯示為「Unknown」的問題。

## 根因

此Jira包含三個獨立根因：1) MPOS API的web.config中ThirdPartyModuleInstallPath設定值不正確，導致購買歷史WebView無法載入正確的CRM頁面。2) IIS伺服器的maximum query string length設定過小，當請求URL過長時返回404錯誤。3) License伺服器連線逾時（Connection timeout），導致MPOS無法從授權伺服器獲取正確的別名資訊，顯示為「Unknown」。

## 解法

解決方案包含三部分：1) 修正MPOS API web.config中的ThirdPartyModuleInstallPath為正確的CRM網址。2) 在IIS中調大maximum query string length設定，允許較長的查詢字串請求。3) License伺服器連線逾時需檢查網路連線狀態及授權伺服器可用性，必要時使用可攜式SQL連線工具進行診斷。

## 相關資訊

- **Jira：** [MP-747](https://ctil.atlassian.net/browse/MP-747)
- **Fix Version：** （無明確版本號，透過組態修正解決）
- **解決日期：** 2025-05-02
- **組件：** Frontend
- **附件截圖：**
  - [image-20250217-055530.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51719)
  - [image-20250217-064643.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51729)
  - [image-20250217-073249.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51750)
  - [image-20250217-121026.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51790)
  - [image-20250218-020939.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51797)
  - [image-20250219-060105.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51888)
  - [image-20250219-070524.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51896)
  - [image-20250221-045557.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51987)
  - [image-20250221-045631.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51986)
  - [image-20250221-045923.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51988)
  - [image-20250221-063600.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51991)
  - [image-20250221-084249.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52003)
  - [vbretail.ini](https://ctil.atlassian.net/rest/api/3/attachment/content/51963)
  - [Web.config](https://ctil.atlassian.net/rest/api/3/attachment/content/51833)
