---
title: "EPM / FEPOS 故障排除知識庫"
description: "ERM 系統已知問題與解決方案 — 來自已解決的 Jira 工單，涵蓋 POS、MPOS、Backend、ProSmart"
tags: [moc, index, welcome]
updated: 2026-05-22
---

# EPM / FEPOS 故障排除知識庫

本知識庫收集 ERM 系統（EPM / FEPOS / ChainStorePlus）的已知問題及其解決方案。每筆記錄來自已解決的 Jira 工單，包含 **症狀描述 → 根本原因 → 解決方案**。

> 共收錄 **1,830+** 篇 FAQ，涵蓋 Backend · Frontend · MPOS · Web Services · ProSmart 五個專案

---

## 快速開始

| 我想… | 操作 |
|-------|------|
| 🔍 **搜尋特定問題** | 使用左側搜尋框，支援中英文、工單號（如 `BE-1020`） |
| 📂 **按分類瀏覽** | 點擊下方分類卡片，或在左側目錄樹展開 |
| 🏷️ **依專案篩選** | 搜尋時輸入 `tag:#be` / `tag:#fe` / `tag:#mp` / `tag:#web` |

---

## 分類導航

| 分類 | 說明 | 數量 |
|------|------|:---:|
| [[FAQ_test/01_Install_Deploy/index\|📦 安裝與部署]] | 系統安裝、升級、環境配置、DB 遷移 | 122 |
| [[FAQ_test/02_Config_Settings/index\|⚙️ 配置與設定]] | 系統參數、功能開關、權限設定 | 69 |
| [[FAQ_test/03_Performance_Timeout/index\|⏱️ 效能與超時]] | 回應緩慢、Timeout、記憶體問題 | 252 |
| [[FAQ_test/04_Data_Sync/index\|🔄 資料同步]] | 資料上傳下載、介面傳輸、Polling | 462 |
| [[FAQ_test/05_Error_Exception/index\|🚨 報錯與異常]] | 錯誤彈窗、系統崩潰、Log 分析 | 596 |
| [[FAQ_test/06_Printing_Hardware/index\|🖨️ 列印與硬體]] | 收據列印、條碼、OPOS、Cash Drawer | 38 |
| [[FAQ_test/06_Procurement_Workflow/index\|🏢 採購流程]] | ProSmart 招標、評標、LOA | 22 |
| [[FAQ_test/07_Workflow_Business/index\|📋 業務流程]] | 審批、交易操作、業務邏輯異常 | 248 |
| [[FAQ_test/03_Data_Import/index\|📥 資料匯入]] | 資料匯入處理 | 1 |
| [[FAQ_test/07_Reporting/index\|📊 報表]] | 報表相關問題 | 1 |
| [[FAQ_test/07_Other/index\|📝 其他]] | 未分類問題 | 6 |

---

## 專案覆蓋

| 專案 | Jira | FAQ 數量 |
|------|------|:--------:|
| **Backend** (ChainStorePlus v7) | [BE](https://ctil.atlassian.net/projects/BE) | 449 |
| **Frontend** (POS/MPOS) | [FE](https://ctil.atlassian.net/projects/FE) | 795 |
| **MPOS** (Mobile POS) | [MP](https://ctil.atlassian.net/projects/MP) | 339 |
| **Web Services** | [WEB](https://ctil.atlassian.net/projects/WEB) | 149 |
| **ProSmart** (採購系統) | [EPMTDCPROT](https://hktdc.atlassian.net/projects/EPMTDCPROT) | 50+ |

---

## 每篇 FAQ 結構

```
🩺 症狀 → 🔍 根因 → 🔧 解法
```

每篇也包含修復版本、Jira 工單連結及相關問題。

| 品質標記 | 含義 |
|----------|------|
| ✅ 資訊完整 | 症狀、根因、解法皆已確認 |
| ⚠️ 部分資訊 | 有症狀描述，根因或解法待補充 |
| ❌ 資訊不足 | 僅有標題，需查閱 Jira 工單 |

---

## 搜尋貼士

- ✅ **直接打關鍵字** — `timeout`、`coupon`、`member search`、`列印`
- ✅ **Jira Key** — 直接搜 `BE-1003` 或 `FE-1440`
- ✅ **中英文皆可** — 打 `printer` 或 `列印` 都得
- 💡 **精準篩選** — `tag:#fe path:06_Printing_Hardware printer`

---

## 相關資源

- [[ChainStoreplus/index\|ChainStorePlus 使用者手冊 FAQ]] — 173 條功能操作 FAQ
- [[Knowledge Base ERM FEPOS/03-Resources/troubleshooting/index\|原始疑難排解記錄]] — 歷史疑難排解
- [Jira ERM Board](https://ctil.atlassian.net/) — 原始工單系統

> 最後更新: 2026-05-22 · 索引由 `scripts/generate_indexes.py` 自動生成
