---
project: ChainStorePlus
title: 如何在没有采购订单（PO）的情况下进行库存收货？
category: 收货流程
source: v7 Book-3 Section 6.2 Pages 12-19
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

在没有采购订单的情况下进行库存收货的操作步骤如下：

1. **进入库存收货功能**
   - 从菜单进入 Stock Receive（库存收货）功能。

2. **设置为无 PO 收货**
   - 在收货信息页面中，选择收货指示器为 Without PO（无采购订单）。

3. **输入收货编号和地点**
   - 输入收货地点代码（Receiving Location Code）。
   - 收货编号（Receiving Number）可根据参数设置选择自动生成或手动输入。

4. **输入商品信息**
   - 输入收货商品代码（Item Code）。
   - 点击 Color & Size 按钮输入颜色和尺寸明细（如果商品有颜色和尺寸控制）。

5. **填写收货数量**
   - 输入实际收货数量。

6. **保存收货信息**
   - 点击 SAVE 按钮保存收货批次。
   - 系统将进入下一步的收货确认流程。

注意：
- 无 PO 收货适用于直接入库的场景，如赠品、样品或紧急采购后补单等情况。
- 同一收货批次可以同时包含有 PO 收货、无 PO 收货以及 Blanket 订单交货请求收货三种类型。
- 输入商品代码时，如果同时输入了单价或地点信息，则商品代码为必填字段。
