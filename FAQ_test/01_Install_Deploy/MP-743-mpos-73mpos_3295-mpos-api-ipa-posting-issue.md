---
project: MP
issue_key: MP-743
issue_type: Bug QA
status: Closed
tags:
- 01_install_deploy
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-743
created: '2025-01-16'
resolved: '2025-07-28'
fix_version: ''
components:
- MPOS
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: complete
---
MP-743: MPOS_3.29.5 (MPOS API + IPA) Posting Issue

| 問題
升級 MPOS API 至 3.29.5 版本後，locregister 資料表無法取得裝置名稱，locreg_msmqservername 顯示為 XXXX。此問題在 AWS 和 Ali 環境皆可重現，影響所有升級至此版本的區域。

| 根因
Web.config 中的 LicConnection 設定值無效（Invalid），導致 MPOS API 無法正確連接授權資料庫，進而無法取得裝置別名（AliasName）與 MSMQ Server 路徑。

| 解法
以正確的 LicConnection 值取代 Web.config 中的無效設定。確認 MSMQ_SERVER_PATH 的 ShopConfig 設定值正確，並確保 MPOS API 能正確回傳裝置的 AliasName 以寫入 locreg_computername 欄位。

| 相關資訊
- Jira: [MP-743](https://ctil.atlassian.net/browse/MP-743)
- 解決日期: 2025-07-28
- 組件: MPOS
- 負責人: Sherman tse
- 附件: [image-20250116-065523.png](https://ctil.atlassian.net/rest/api/3/attachment/content/50587) | [image-20250116-065530.png](https://ctil.atlassian.net/rest/api/3/attachment/content/50588) | [image-20250116-072647.png](https://ctil.atlassian.net/rest/api/3/attachment/content/50593) | [image-20250116-080314.png](https://ctil.atlassian.net/rest/api/3/attachment/content/50596) | [image-20250117-091849.png](https://ctil.atlassian.net/rest/api/3/attachment/content/50674)