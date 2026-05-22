---
project: EPMTDCPROT
issue_key: EPMTDCPROT-3343
tags: [faq, epm, epmtdcprot, 05-error-exception]
jira_url: "https://ctil.atlassian.net/browse/EPMTDCPROT-3343"
category: 05_Error_Exception
category_name: "錯誤與異常"
---

EPMTDCPROT-3343: [Phase 2 DEV] Sysadmin cannot cancel the delegation

| 問題

Sysadmin 嘗試取消其他使用者建立的委派（Delegation）時出現錯誤，無法取消，該如何解決？

| 根因

根據 Comment (Michael Ren)：Sysadmin 可以取消委派，但必須符合以下三種情況之一：(1) admin 是 Delegator；(2) admin 是 Delegation-To 對象；(3) admin 是委派的創建者（Creator）。原先未正確涵蓋這三種場景，導致 Sysadmin 無法取消非自己創建的委派。

| 解法

修正 Phase 2 DEV 中的委派取消邏輯，確保 Sysadmin 在符合上述三種場景時可成功取消委派，不再出現錯誤訊息。

| 相關資訊

- Jira: [EPMTDCPROT-3343](https://ctil.atlassian.net/browse/EPMTDCPROT-3343)
- Fix Version: 未標註
- 分類: 錯誤與異常
- 專案: EPMTDCPROT
