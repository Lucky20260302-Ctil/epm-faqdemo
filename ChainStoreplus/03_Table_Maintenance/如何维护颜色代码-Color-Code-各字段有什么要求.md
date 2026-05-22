---
project: ChainStorePlus
title: 如何维护颜色代码（Color Code）？各字段有什么要求？
category: 基础表维护
source: v7 Book-1 Section 4.6 Page 46-47
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

颜色代码维护用于为商品维护通用颜色信息，在商品主数据维护中使用。

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
| Color Code（颜色代码） | X(05) - 必填字段 - 用于定义特定颜色的唯一代码，在商品主数据维护中使用 |
| Description（描述） | X(40) - 可选字段 - 指代此颜色代码的简短描述 |
| Sub Color（子颜色） | 可选 - 可以在次级（可选）维护下的 "Sub Color"（子颜色）表中定义 |
