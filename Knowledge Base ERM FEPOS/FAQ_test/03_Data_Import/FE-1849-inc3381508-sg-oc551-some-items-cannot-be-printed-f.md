---
project: "FE"
issue_key: "FE-1849"
issue_type: "Bug PRD"
status: "Closed"
tags: [faq, fe]
jira_url: "https://ctil.atlassian.net/browse/FE-1849"
created: "2026-01-09"
resolved: ""
fix_version: ""
components: [Frontend]
category: "03_Data_Import"
---

FE-1849: SG OC551 Some items cannot be printed from POS system

| 問題
POS銷售頁面可搜尋到商品，但於標籤列印頁面無法找到特定商品並列印（如CCC23、CCM57、CCU00等）。以條碼搜尋可找到商品，但以Item編號搜尋則找不到

| 根因
Mastconv資料匯入後產生的dbmas中缺少部分商品主檔記錄（Item No 'CC23', 'CCM57', 'CCU00'），導致POS無法以Item編號找到商品；但EAN條碼表中仍有對應記錄，故以條碼搜尋可正常找到

| 解法
重新套用（Apply）最新的Mastconv資料至POS終端，確保商品主檔記錄完整後即可正常列印標籤

| 相關資訊
- Jira: [FE-1849](https://ctil.atlassian.net/browse/FE-1849)
- 組件: Frontend
- 負責人: Sang
- 附件: [1.png](https://ctil.atlassian.net/rest/api/3/attachment/content/72807) | [2.png](https://ctil.atlassian.net/rest/api/3/attachment/content/72808) | [3.png](https://ctil.atlassian.net/rest/api/3/attachment/content/72809) | [DbTrans OC5512.sdf](https://ctil.atlassian.net/rest/api/3/attachment/content/72940) | [image-20260112-050727.png](https://ctil.atlassian.net/rest/api/3/attachment/content/72946)