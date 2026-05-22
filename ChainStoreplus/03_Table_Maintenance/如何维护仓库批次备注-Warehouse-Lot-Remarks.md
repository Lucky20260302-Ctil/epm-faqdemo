---
project: ChainStorePlus
title: 如何维护仓库批次备注（Warehouse Lot Remarks）？
category: 基础表维护
source: v7 Book-1 Section 4.15 Page 65
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

仓库批次备注维护用于管理与商品主数据相关的仓库批次备注表，以供将来的报表使用。

**字段说明：**

| 提示 | 说明 |
|------|------|
| Item Code（商品代码） | X(14) - 显示字段 - 商品代码 |
| Description（描述） | X(30) - 显示字段 - 商品描述 |
| W/H Lot Remarks（仓库批次备注） | X(8) - 可选字段 - 商品所定义的仓库批次备注 |

**使用说明：**
- 此表属于次级表（Secondary Tables），可能仅针对特定客户有特定用途
- 用于在仓库和批次级别对商品添加备注信息
- 备注信息可用于将来的报表和分析目的
