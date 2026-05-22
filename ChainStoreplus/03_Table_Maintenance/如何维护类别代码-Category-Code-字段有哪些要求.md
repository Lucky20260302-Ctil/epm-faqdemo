---
project: ChainStorePlus
title: 如何维护类别代码（Category Code）？字段有哪些要求？
category: 基础表维护
source: v7 Book-1 Section 4.4 Page 43-44
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

类别代码维护用于为商品维护通用类别信息，该信息在商品主数据维护（Item Master Maintenance）中使用。

**功能：**
1. 创建记录 (Create Record)
2. 修改记录 (Modify Record)
3. 删除记录 (Delete Record)
4. 查看记录 (View Record)
5. 复制记录为新记录 (Copy Record as new)
6. 查找记录 (Find Record)
7. 按列标题排序 (Sort by header)
8. 调整列宽指示 (Adjust column indication)

**字段说明：**

| 提示 | 说明 |
|------|------|
| Category Code（类别代码） | X(03) - 必填字段 - 用于在商品主数据维护中定义类别的唯一代码 |
| Description（描述） | X(40) - 必填字段 - 该类别的描述 |
| Sub. Category（子类别） | X(02) - 可选字段 - 定义该类别的子类别的唯一代码，使用此类别的商品必须属于其中一个子类别，最多可输入30个 |
| Sub. Category Description（子类别描述） | X(10) - 如果已定义子类别代码则为必填 - 子类别的描述 |
| Serial Flag（序列号标志） | 可选 - 设置为 "YES" 表示该类别的商品将具有序列号 |
| Discount Control（折扣控制） | X(01) - 必填字段 - 默认为 'No' - 设置为 "YES" 表示该类别的商品有折扣控制，POS 销售时不允许打折 |
| Max. Discount（最大折扣） | 99.99 - 可选字段 - 仅在折扣控制设置为 'NO' 时可用 - 以零售价的百分比表示 |
