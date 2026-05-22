---
tags: [summary, project-status]
updated: 2026-05-20
---

# Troubleshooting Knowledge Base — 建置摘要

> 從 Jira 已解決 ticket 中系統化提煉根因分析與解決方案，建立可查詢、可維護的故障排除知識庫。

---

## 資料範圍

| 項目 | 內容 |
|------|------|
| **Jira 專案** | Frontend (FE) + MPOS (MP) + Backend (BE) |
| **JQL 篩選條件** | `project in (FE, MP, BE) AND status IN (Closed, Release) AND (description ~ "root cause" OR description ~ "solution" OR description ~ "fix")` |
| **總掃描 ticket 數** | 70+ 張 |
| **已建立筆記** | **38 篇** (FE: 20 + MP: 8 + BE: 10) |
| **跨距** | 2020-04 ~ 2026-05（約 6 年） |

---

## 檔案結構

```
03-Resources/troubleshooting/
├── index.md                       ← MOC 索引（依症狀、依元件、索引總表）
├── FE-1xxx-*.md  × 12            ← 第一輪：高價值 FE ticket
├── FE-1xxx-*.md  ×  8            ← 第二輪：FE + MPOS 新增 ticket
└── MP-xxx-*.md   ×  8            ← MPOS 專案 ticket
```

---

## 分類統計

### 依問題類型

| 分類 | 數量 | 說明 |
|------|------|------|
| 🛒 POS 交易流程 | 8 | 折扣計算、Coupon 處理、稅金、Barcode |
| 📅 Day End / 結算 | 3 | PCD 漏算、PC23 顯示、V75 cs2kconnect |
| 👤 會員 / eName / API | 8 | VIP Barcode、Member Type、Thread Safety、API 效能、CRM Sync |
| 📤 資料 / 上傳 | 4 | Pay Code、CAR Error、PCD Posting |
| 🖨️ 列印 / 顯示 | 3 | Bash Transfer、OPOS.net、Citizen Printer |
| ⚙️ 系統服務 / Backend | 8 | SQL Express、cs2kconnect、CAR、ITMEAN、Posting MQ |
| 📱 MPOS 平台 | 6 | iOS 相容性、Queue Busting、Coupon 狀態、Region Code |

### 依嚴重程度

| 標籤 | 數量 |
|------|------|
| `production` | 22 |
| `hotfix` | 6 |
| `qa` / `uat` | 5 |
| `improvement` / `change-request` | 2 |

### 依 Fix Version 分佈

| Release | Tickets |
|---------|---------|
| v750.04R 系列 | 7 (R04I, R04I, R07A, R10, R11, R11A, R13A) |
| v750.01~.03 系列 | 5 |
| v720.02R 系列 | 5 |
| v710.02R 系列 | 2 |
| MPOS 3.x | 7 |
| BE-V70R3 系列 | 4 (R14a, R59, R102, R145) |
| BEAPI v1.x | 3 (v1.6.20, v1.7.14, v1.7.16) |

---

## 使用方式

### 在 Obsidian 中
- 開啟 [[03-Resources/troubleshooting/index\|MOC 索引]] 瀏覽所有問題
- 用 `#jira/FE-XXXX` 或 `#jira/MP-XXX` 標籤搜尋特定 ticket
- 用 `#troubleshooting` 標籤搜尋所有 troubleshooting notes

### 自動化掃描
每日 09:30 自動執行 cron job 檢查 Jira 新 ticket（需 cron 續約，7 天一週期）

---

## 建議下一步

1. **擴充到更多專案**: 將 JQL 擴展到其他相關 Jira project
2. **嵌入截圖**: 為關鍵 ticket 加入 POS 畫面、T9 log 截圖（`![[image.png]]`）
3. **建立 KPI**: 追蹤 KB 建置後重複調查率是否下降
4. **關聯測試案例**: 連結到對應的 Test Case / QA scenario

---

## 建置歷程

| 日期 | 項目 |
|------|------|
| 2026-05-18 | 初版：12 張 FE troubleshooting notes |
| 2026-05-18 | 第二版：+8 FE + 8 MPOS notes (共 28 張) |
| 2026-05-18 | 設定 cron 每日 09:30 JQL 自動掃描 (FE+MP) |
| 2026-05-20 | 第三版：+10 BE notes (共 38 張)；擴充 cron 至 (FE+MP+BE) |
