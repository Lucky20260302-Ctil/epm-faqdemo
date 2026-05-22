---
project: ChainStorePlus
title: 如何维护品牌代码（Brand Code）？各字段有什么要求？
category: 基础表维护
source: v7 Book-1 Section 4.7 Page 47-48
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

品牌代码维护用于为商品维护通用品牌信息，在商品主数据维护中使用。

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
| Brand Code（品牌代码） | X(06) - 必填字段 - 用于定义特定品牌的唯一代码，在商品主数据维护中使用 |
| Brand Name（品牌名称） | X(40) - 可选字段 - 表示该品牌代码的名称 |
| Supplier Code（供应商代码） | X(08) - 必填字段 - 品牌的供应商 - 供应商代码将对照供应商表进行验证 |
| Max. Discount（最大折扣） | 99.99 - 可选字段 - 该品牌允许的最大折扣 |
