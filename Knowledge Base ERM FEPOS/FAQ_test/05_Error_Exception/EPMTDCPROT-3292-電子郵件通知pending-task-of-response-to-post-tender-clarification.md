---
project: EPMTDCPROT
issue_key: EPMTDCPROT-3292
tags: [faq, epm, epmtdcprot, 05-error-exception]
jira_url: "https://ctil.atlassian.net/browse/EPMTDCPROT-3292"
category: 05_Error_Exception
category_name: "錯誤與異常"
---

EPMTDCPROT-3292: 

| 問題

電子郵件通知「Pending Task of Response to Post-Tender Clarifications」中的連結錯誤，供應商點擊後被重定向到內部portal（EPRO）而非正確的供應商入口，導致供應商無法直接回覆標後澄清（Post-Tender Clarification）。

| 根因

shortUrl 生成時以手動方式設置固定 domain，導致使用者收到的連結 domain 為寫死的值。先前測試環境中內部portal與供應商portal共用同一 domain，因此未發現問題；但 TDC Production 環境中內部portal與供應商portal使用不同 domain，導致供應商收到的電子郵件連結指向錯誤的內部portal。

| 解法

改用統一 function 生成 shortUrl，根據收件人身份（是否為供應商）自動判斷並選用對應的正確 domain。修復後已在多種郵件通知場景完成測試驗證，包括 RFQ 與 Tender 的 acknowledgement、NDA、Briefing、Offer Response、PTC (Technical/Fee)、PTN、LOA 等，確保各類通知連結均指向正確的入口。

| 相關資訊

- Jira: [EPMTDCPROT-3292](https://ctil.atlassian.net/browse/EPMTDCPROT-3292)
- Fix Version: 未標註
- 分類: 錯誤與異常
- 專案: EPMTDCPROT
