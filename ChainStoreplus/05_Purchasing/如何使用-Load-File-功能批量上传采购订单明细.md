---
project: ChainStorePlus
title: 如何使用 Load File 功能批量上传采购订单明细？
category: 采购流程
source: v7 Book-3 Section 6.1 Pages 8-11
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

使用 Load File 功能批量上传采购订单明细的操作步骤如下：

1. **准备上传文件**
   - 文件必须是 Text file（Tab 分隔符格式，Tab delimited）。
   - 文件名没有限制。
   - 文件格式必须与 ChainStorePlus PO Load File 数据格式匹配。

2. **文件格式要求**
   | 序号 | 字段名称 | 长度 | 必填 | 说明 |
   |------|----------|------|------|------|
   | 1 | Item Code（商品代码） | X(14) | 是 | 必须在 ChainStorePlus 中已定义 |
   | 2 | Color（颜色） | X(5) | 否 | 必须在 ChainStorePlus 中已定义 |
   | 3 | Size（尺寸） | X(4) | 否 | 必须在 ChainStorePlus 中已定义 |
   | 4 | Inseam（内缝长） | X(4) | 否 | 必须在 ChainStorePlus 中已定义 |
   | 5 | Quantity（数量） | X(7) | 是 | 最大 9999999 |
   | 6 | Unit Cost（单价） | X(12) | 是 | 格式 999999999.99 |
   | 7 | Item Discount Rate（折扣率） | X(6) | 否 | 格式 999.99 |

3. **执行上传**
   - 在 Purchase Order Maintenance（PO3000）的 Manage Item 页面中。
   - 点击 Load Layout 按钮可查看上述文件格式。
   - 点击 Load 按钮。
   - 系统弹出 Load Detail 对话框，询问 PO Load 文件位置。
   - 选择准备好的 PO Load File。
   - 点击 Open 将文件上传至 PO Maintenance。

4. **验证与错误处理**
   - 上传时，程序会对上传文件的数据进行验证。
   - 如果发现错误，系统会停止加载并返回错误信息。
   - 用户需要点击 Print Queue 保存「Purchase Order Upload Error Report」以查看无效上传的原因。
   - 根据错误报告修改 Text 文件，然后重新上传。
   - 注意：PO Load File 不应包含表头行（header）。如果遇到此错误，请移除表头行后重试。

5. **上传成功**
   - 上传成功后，数据将被放入 Item Detail 列表中。
   - 用户可以编辑内容后保存 PO。
