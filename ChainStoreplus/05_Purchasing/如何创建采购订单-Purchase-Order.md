---
project: ChainStorePlus
title: 如何创建采购订单（Purchase Order）？
category: 采购流程
source: v7 Book-3 Section 6.1 Pages 4-8
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

创建采购订单的操作步骤如下：

1. **进入采购订单维护画面**
   - 从菜单中点击进入 Purchase Order Maintenance 功能。
   - 点击 CREATE 按钮创建新的采购订单。

2. **输入订单头信息（Header Input）**
   - 进入 Purchase Order Detail Maintenance Screen。
   - 选择订单类型：
     - Normal PO（普通采购订单）：正常模式，允许分批收货。
     - Blanket PO（blanket 采购订单）：批量订单模式，供应商可在一段时间（如一年或一个季节）内分批次交货。Blanket PO 需要后续的「交货请求（Delivery Request）」来完成交货。
   - 勾选折扣复选框可启用行项目折扣输入字段。
   - 部分字段由系统自动计算且不可手动输入。

3. **输入采购订单条款（PO Terms Input）**
   - 点击第二个文件夹标签页（2nd folder）进入 PO 条款输入。
   - 关键字段：
     - Expected Shipment Date（预计发货日期）：部分 PO 报表以此字段作为排序依据。
     - 默认收货地点：用于 PO 收货流程的默认位置。
     - 分配地点：用于将到货库存分配到特定位置，仅在特定设计程序中生效。

4. **输入明细项目（Detail Items Input）**
   - 进入 Manage Item 页面。
   - 输入商品代码（Item Code）。
   - 如果商品有颜色和尺寸的细分，点击 Color & Size 按钮输入详细的数量。
   - 也可以直接在数量字段中输入采购数量。

5. **了解列字段含义**
   - List Price（列表价）：采购商品的标准价格。
   - Def Disc%（默认折扣率）：系统自动获取的默认折扣百分比，需预先在供应商主文件或供应商 PO 折扣表中设定。
   - Ovr Disc%（覆盖折扣率）：手动输入的覆盖折扣，当默认折扣不适用时使用；系统优先使用此折扣计算采购单价。
   - Unit Cost（单价）：系统计算的采购单价，或用户手动输入覆盖系统计算的数值；如果与默认 PO 成本不同，数值将显示为红色提示。
   - Qty（数量）：用户输入的采购数量。
   - Order Amount（订单金额）：系统基于单价乘以数量自动计算。
   - Unit（单位）：采购商品的计量单位。

6. **确认并保存**
   - 检查所有输入信息。
   - 点击保存按钮完成采购订单创建。

注意：采购订单流程支持从下单、收货、未完成订单跟踪、库存成本更新（通过收货流程）到报表的完整操作。
