---
project: ChainStorePlus
title: 如何使用型号（Model Number）查询商品信息？
category: 主数据管理
source: v7 Book-2 Section 5.3.1 Page 32
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

型号查询功能（Model Number）允许用户通过商品型号搜索键来查询或修改商品信息，查看特定库存的可用性。

**功能说明：**
通过商品搜索键，按型号（Model No.）进行查询。

**目标：**
对商品信息进行查询或修改，用户可以检查特定库存的可用性。

**字段说明：**
| 字段名称 | 格式 | 必填/可选 | 说明 |
|---------|------|----------|------|
| Item Code（商品代码） | X(14) | 必填 | 唯一标识特定商品的代码 |
| Description（描述） | X(40) | 必填 | 详细的商品描述 |
| Model Number（型号） | X(30) | 必填 | 商品的型号 |

**附加功能 - 按保修编号（Guarantee No.）查询：**
通过商品搜索键，按保修编号（Guarantee No.）进行查询，用户可以检查特定库存的保修编号。
