---
title: "EPM / FEPOS 故障排除知識庫"
description: "ERM 系統已知問題與解決方案 — 來自已解決的 Jira 工單，涵蓋 POS、MPOS、Backend、ProSmart"
tags: [moc, index, welcome]
updated: 2026-05-22
---

# EPM / FEPOS 故障排除知識庫

本知識庫收集 ERM 系統（EPM / FEPOS / ChainStorePlus / ProSmart）的已知問題及其解決方案。每筆記錄來自已解決的 Jira 工單，包含 **症狀描述 → 根本原因 → 解決方案**。

---

## 快速開始

| 我想… | 操作 |
|-------|------|
| 🔍 **搜尋特定問題** | 左側搜尋框輸入關鍵字（中英文、工單號如 `BE-1020`） |
| 📂 **按分類瀏覽** | 點下方分類表或左側目錄樹展開 |
| 🏷️ **依專案篩選** | 搜尋時輸入 `tag:#be` / `tag:#fe` / `tag:#mp` |

---

## ERM 故障排除 FAQ

> 160 篇 FAQ · 全部品質完整 ✅ · 11 個業務分類 · EPRO TDC 59 篇用户手册 FAQ

| 分類 | 說明 | 數量 |
|------|------|:---:|
| [[FAQ_test/01_Install_Deploy/index\|📦 安裝與部署]] | 系統安裝、升級、環境配置 | 8 |
| [[FAQ_test/02_Config_Settings/index\|⚙️ 配置與設定]] | 系統參數、功能開關、權限 | 21 |
| [[FAQ_test/03_Performance_Timeout/index\|⏱️ 效能與超時]] | 回應緩慢、Timeout、記憶體 | 5 |
| [[FAQ_test/04_Data_Sync/index\|🔄 資料同步]] | 資料上傳下載、介面傳輸 | 18 |
| [[FAQ_test/05_Error_Exception/index\|🚨 報錯與異常]] | 錯誤彈窗、系統崩潰、Log | 52 |
| [[FAQ_test/06_Printing_Hardware/index\|🖨️ 列印與硬體]] | 收據列印、OPOS、Cash Drawer | 9 |
| [[FAQ_test/06_Procurement_Workflow/index\|🏢 採購流程]] | ProSmart 招標、評標、LOA | 22 |
| [[FAQ_test/07_Workflow_Business/index\|📋 業務流程]] | 審批、交易操作、業務邏輯 | 17 |
| [[FAQ_test/03_Data_Import/index\|📥 資料匯入]] | 資料匯入處理 | 1 |
| [[FAQ_test/07_Reporting/index\|📊 報表]] | 報表相關問題 | 1 |
| [[FAQ_test/07_Other/index\|📝 其他]] | 未分類問題 | 6 |

---

## EPRO e-Procurement System

> 124 條功能需求規格 · 7 個分類

| 分類 | 數量 |
|------|:---:|
| [[EPRO_System/01_General_Requirements/index\|General Requirements]] | 28 |
| [[EPRO_System/02_PreTender/index\|Pre-Tender]] | 31 |
| [[EPRO_System/03_TenderStage/index\|Tender Stage]] | 11 |
| [[EPRO_System/04_PostTender/index\|Post-Tender]] | 16 |
| [[EPRO_System/05_Supplier/index\|Supplier]] | 10 |
| [[EPRO_System/06_Reports/index\|Reports]] | 23 |
| [[EPRO_System/07_Others/index\|Others]] | 5 |

---

## EPRO TDC — 用户手册 FAQ

> 59 条操作 FAQ · 9 个分类 · 基于 4 本官方用户手册

| 分类 | 数量 |
|------|:---:|
| [[EPRO_TDC/01_System_Access/index\|系统访问]] | 3 |
| [[EPRO_TDC/02_Dashboard/index\|仪表盘与任务管理]] | 4 |
| [[EPRO_TDC/03_Supplier_Management/index\|供应商管理]] | 4 |
| [[EPRO_TDC/04_PreTender/index\|预招标阶段]] | 4 |
| [[EPRO_TDC/05_Tender_Stage/index\|招标阶段]] | 7 |
| [[EPRO_TDC/06_Post_Tender/index\|评标与授标]] | 9 |
| [[EPRO_TDC/07_Approval_Workflow/index\|审批流程]] | 7 |
| [[EPRO_TDC/08_TAP/index\|技术评估]] | 5 |
| [[EPRO_TDC/09_Supplier_Operations/index\|供应商端操作]] | 16 |

---

## ChainStorePlus 使用者手冊

> 98 條操作 FAQ · 12 個分類

| 分類 | 數量 |
|------|:---:|
| [[ChainStoreplus/01_Getting_Started/index\|系統入門]] | 8 |
| [[ChainStoreplus/02_System_Tools/index\|系統工具]] | 8 |
| [[ChainStoreplus/03_Table_Maintenance/index\|基礎表維護]] | 20 |
| [[ChainStoreplus/04_Master_Data/index\|主數據管理]] | 11 |
| [[ChainStoreplus/10_Inquiry/index\|線上查詢]] | 18 |
| [[ChainStoreplus/11_Data_Interface/index\|數據接口]] | 10 |
| [[ChainStoreplus/08_Inventory/index\|庫存管理]] | 7 |
| [[ChainStoreplus/05_Purchasing/index\|採購流程]] | 3 |
| [[ChainStoreplus/06_Receiving/index\|收貨流程]] | 3 |
| [[ChainStoreplus/07_Stock_Transfer/index\|庫存轉移]] | 4 |
| [[ChainStoreplus/09_Distribution/index\|配送流程]] | 3 |
| [[ChainStoreplus/12_System_Admin/index\|系統管理]] | 3 |

---

## 每篇 FAQ 結構

```
🩺 症狀 → 🔍 根因 → 🔧 解法
```

每篇也包含修復版本及 Jira 工單連結。

---

## 搜尋貼士

- ✅ **直接打關鍵字** — `timeout`、`coupon`、`member search`、`列印`
- ✅ **Jira Key** — 直接搜 `BE-1003` 或 `FE-1440`
- ✅ **中英文皆可** — 打 `printer` 或 `列印` 都得
- 💡 **精準篩選** — `tag:#fe path:06_Printing_Hardware printer`

> 最後更新: 2026-05-22 · 自動同步
