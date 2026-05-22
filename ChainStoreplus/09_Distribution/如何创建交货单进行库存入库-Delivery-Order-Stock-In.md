---
project: ChainStorePlus
title: 如何创建交货单进行库存入库（Delivery Order - Stock In）？
category: 配送流程
source: v7 Book-3 Section 6.11 Pages 66-67
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

创建交货单进行库存入库的操作步骤如下：

1. **进入功能**
   - 从菜单进入 Delivery Order Process - Stock In（交货单入库流程）。
   - 此功能用于处理库存入库操作。

2. **系统原理**
   - 系统将入库数据作为 Physical Adjustment（物理调整）的一种形式处理。
   - 使用用户自定义的交易代码（Transaction Codes）进行区分。
   - 更新机制与 Delivery Order - Stock Out 流程相同，但计算方向相反（逆向计算）。

3. **操作步骤**
   - 创建新批次（Create New Batch）。
   - 点击 Batch Maintenance 进入批次维护。

4. **输入头信息**
   - 参考 Delivery Order Stock Out 的头信息字段，主要包括：
   - 日期、部门编号、客户名称、交货日期、货币、汇率等。

5. **输入商品明细**
   - 输入商品代码、入库交易代码、单价、地点、数量等信息。
   - 入库交易代码由用户自定义，用于标识不同的入库原因。

6. **执行工作流程**
   - Batch Validation（批次验证）
   - Batch Posting（批次过账）

注意：具体操作细节与 Stock Out 流程相似，但因库存方向相反，对库存的影响是增加而非减少。
