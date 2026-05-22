---
project: MP
issue_key: MP-793
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, mp, install_deploy, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-793"
created: 2025-08-19
resolved: 2025-09-02
resolution: Done
has_images: False
---

# MP-793: [MPOS-115][INC3149444]CJ mPOS Prod_ J317 the transaction disappears if it`s not connected to SalesHub

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 安裝與部署 | **FAQ 分數:** 7.5
> **解決日期:** 2025-09-02
> **負責人:** Daniel Leung
> **組件:** MPOS

## 問題描述

J317 called out when I visited the store. They have experienced the issue after version upgraded(Ver 3.30.3) on 8/6.

Issue:

When a transaction is entered into the mPOS but not yet completed, and the user temporarily accesses another site (e.g., eNameCapture from an iPhone), upon returning to the mPOS screen, the entered information disappears.

According to the store, it seems like it requires to "Connected to SalesHub" in order to avoid this issue. They need to understand what caused disconnection from SalesHub.



## 相關資訊

- **Jira:** [MP-793](https://ctil.atlassian.net/browse/MP-793)
- **解決方式:** Done