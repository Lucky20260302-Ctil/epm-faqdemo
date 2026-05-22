---
project: MP
issue_key: MP-761
issue_type: Bug PRD
status: Closed
tags:
- 02_config_settings
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-761
created: '2025-03-27'
resolved: '2025-05-21'
fix_version: ''
components:
- MPOS
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: partial
---
MP-761: JP 2 V75 Pilot store MPOS keep loading and pop out error:”Fail to Connect SalesHub”after update to new version

| 問題
日本 V75 試點店鋪（J317、J328）在升級至新版本後，MPOS 持續顯示載入中，並彈出「Fail to Connect SalesHub」錯誤。使用 CS2000 帳號登入時無法正常進入銷售功能，但使用 CSAdmin 帳號則 SalesHub 可正常連線。

| 根因
根因有二：(1) CS2000 帳號沒有權限啟動 SalesHub.exe，導致 HTTP 監聽失敗，而 CSAdmin 帳號則有完整權限；(2) 預設的 9001 連接埠有時被其他未知資源佔用，且 SignalR 連線使用動態埠範圍（49152-65535），若防火牆未正確允許這些埠號的入站與出站連線，也會導致 SalesHub 連線不穩定。

| 解法
三種解決方案：(1) 以系統管理員權限執行 netsh http add urlacl url=http://+:9001/ user=\Everyone 指令，授予使用者帳號存取 SalesHub HTTP 監聽的權限；(2) 將 SalesHub 連接埠從 9001 更改為 9000，避免埠號衝突；(3) 檢查防火牆規則，確保動態埠範圍 49152-65535 已允許 TCP 入站與出站連線。

| 相關資訊
- Jira: [MP-761](https://ctil.atlassian.net/browse/MP-761)
- 解決日期: 2025-05-21
- 組件: MPOS
- 負責人: Daniel Leung
- 附件: [image-20250327-014150.png](https://ctil.atlassian.net/rest/api/3/attachment/content/53809) | [image-20250327-014515.png](https://ctil.atlassian.net/rest/api/3/attachment/content/53810) | [image-20250327-014844.png](https://ctil.atlassian.net/rest/api/3/attachment/content/53811) | [image-20250327-085000.png](https://ctil.atlassian.net/rest/api/3/attachment/content/53887) | [image-20250327-085040.png](https://ctil.atlassian.net/rest/api/3/attachment/content/53886)