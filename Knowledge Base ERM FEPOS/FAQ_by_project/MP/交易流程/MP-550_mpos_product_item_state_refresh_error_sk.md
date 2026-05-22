---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "When the user attempts to add the item (SKU: 3334), the sales memo could not show the price. However"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-550
resolved: 2024-05-15
fix-version: ""
---

# MP-550: MPOS Product item state refresh error (SKU: 3334)

## 問題

When the user attempts to add the item (SKU: 3334), the sales memo could not show the price. However, the selling price shows up when the page is refreshed once.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-05-15
### Jira Comments (1 則)
**Cy Lau** (2022-09-16):
Please apply a fix on 3.20.x first then 3.19.1
First Insight : no setstate(){} after onresult / on pop

## 相關資訊

- Jira: [MP-550](https://ctil.atlassian.net/browse/MP-550)
- Fix Version: 未記錄
- 解決日期: 2024-05-15
