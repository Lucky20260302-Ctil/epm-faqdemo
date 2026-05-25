---
project: FE
issue_key: FE-1724
issue_type: Bug PRD
status: Closed
tags:
- 07_workflow_business
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1724
created: '2025-07-08'
resolved: '2025-07-15'
fix_version: FE-75.004.1305.0000
components:
- report
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: complete
---

FE-1724: No Qty for Void and return deposit listed on Till1 dayend report

## 症狀

Coach 店舖使用 Laser（A4）打印機進行日結時，Till1 的日結報表缺少「取消定金單數量」及「退回定金單數量」兩行數據，而使用 TMU 打印機的 Till0 則正常顯示。此外，合併日結報表中的按金單數量與各 Till 的按金單數量之和不一致。

## 根因

A4 雷射打印機的日結報表在「Deposit Memo Qty」區塊的顯示邏輯與 TMU 打印機不同步：A4 報表將 Void Deposit Qty 合併計入 Deposit Memo Qty，且缺少 Deposit Return Memo Qty 行。此為報表格式邏輯不一致所導致，並非資料錯誤。

## 解法

開發團隊修改 A4 日結報表之 Deposit Memo Qty 區塊，使其內容與 TMU 報表對齊，並加入 Syscon_Dep_mod 旗標控制是否列印該區塊。修復版本：FE-75.004.1305.0000（於 2025-07-15 發佈）。

## 相關資訊

- Jira: [FE-1724](https://ctil.atlassian.net/browse/FE-1724)
- Fix Version: FE-75.004.1305.0000
- 解決日期: 2025-07-15
- 組件: report
- 負責人: Sherman tse
- 附件: [ALL FE log Tilll0&Till1.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/61578) | [image-2025-07-07-20-30-56-469.png](https://ctil.atlassian.net/rest/api/3/attachment/content/61376) | [image-2025-07-07-20-31-15-846.png](https://ctil.atlassian.net/rest/api/3/attachment/content/61377) | [image-2025-07-07-20-31-40-583.png](https://ctil.atlassian.net/rest/api/3/attachment/content/61378) | [image-20250708-051756.png](https://ctil.atlassian.net/rest/api/3/attachment/content/61375)


## 相關截圖

![[../attachments/FE-1724/image-2025-07-07-20-30-56-469.png]]

![[../attachments/FE-1724/image-2025-07-07-20-31-15-846.png]]

![[../attachments/FE-1724/image-2025-07-07-20-31-40-583.png]]

![[../attachments/FE-1724/image-20250708-051756.png]]

![[../attachments/FE-1724/image-20250708-052337.png]]

> 共 11 張截圖，[查看全部](../attachments/FE-1724/)
