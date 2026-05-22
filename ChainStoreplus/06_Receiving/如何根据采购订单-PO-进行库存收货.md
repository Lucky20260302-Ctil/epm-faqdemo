---
project: ChainStorePlus
title: 如何根据采购订单（PO）进行库存收货？
category: 收货流程
source: v7 Book-3 Section 6.2 Pages 12-21
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

根据采购订单进行库存收货的操作步骤如下：

1. **进入库存收货功能**
   - 从菜单进入 Stock Receive（库存收货）功能。

2. **输入或选择采购订单**
   - 在 Stock Receive Input Against PO/DRV 画面中：
   - 方式一：直接输入 PO 编号，点击 OK。
   - 方式二：留空点击 OK，进入完整的 PO 选择页面。

3. **选择采购订单（方式二：留空搜索）**
   - 系统显示所有未完成的 PO 列表供用户选择。
   - 可按不同排序路径查看 PO：
     - PO#（采购订单编号）
     - DRV#（交货请求编号）
     - Supplier（供应商）
     - Expected Delivery Date（预计交货日期）
     - Receiving Location（收货地点）
   - 鼠标点击高亮选择目标行，左侧会显示「V」标记表示选中。
   - 允许同时选择多个 PO。
   - 点击工具栏上的 Create 按钮，系统将根据所选 PO 的未完成数量自动创建收货批次，默认收货数量等于未完成数量。

4. **输入收货批次头信息**
   - 输入收货地点代码（Receiving Location）作为收货编号的前缀。
   - 收货编号（Receive Number）部分可由用户输入或系统自动生成（如设置为系统生成则字段被保护不可输入）。
   - 输入供应商的交货单号码（Supplier Delivery Note Number），此信息对后续的供应商发票核对非常重要。
   - 某些字段由系统自动生成，不可手动输入。
   - 完成所有输入字段后，点击 Item Information Folder 进入下一步。

5. **输入/确认商品明细（Item Information Folder）**
   - 收货批次支持三种收货状态：
     - Stock Receive under PO（根据 PO 收货）
     - Stock Receive without PO（无 PO 收货）
     - Stock Receive under Delivery Request from a Blanket Order（根据 Blanket 订单的交货请求收货）
   - 红色圆圈指示当前激活的收货状态。
   - 对于颜色和尺寸有要求的商品，点击 Color & Size 按钮输入颜色和尺寸明细。
   - 支持从外部来源导入 TEXT 数据（可选功能）。

6. **保存收货信息**
   - 所有输入完成后，点击 SAVE 按钮。
   - 系统将进入下一步的收货确认流程。

功能按钮说明：
- Insert：插入一个商品项目
- Delete：删除一个商品项目
- Select PO：查询选定供应商的所有未完成 PO 并进行选择，系统将自动带入订单及默认收货数量
- Verify：每次点击时系统验证输入数据，验证后在状态栏显示警告或错误信息
- PO Enquiry：查询采购订单详情
- Color & Size：输入选定商品的颜色和尺寸明细
- Description：显示选定商品的详细描述
- Load：从系统目录导入外部 TEXT 数据（需精确的数据格式，使用前请咨询软件顾问）
- Model & Guarantee No.：特殊功能，不对一般用户开放；允许在收货阶段输入商品唯一的保修号和型号，每个商品编号只能关联一个保修号，因此每个商品仅允许数量为1（不支持颜色和尺寸）。
