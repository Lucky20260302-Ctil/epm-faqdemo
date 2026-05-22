---
project: ChainStorePlus
title: 如何维护尺码类别（Size Category）？字段有哪些要求？
category: 基础表维护
source: v7 Book-1 Section 4.5 Page 45
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

尺码类别维护用于为商品维护一组尺码范围的类别，在商品主数据维护中使用。

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
| Size Category（尺码类别） | X(04) - 必填字段 - 用于定义特定尺码类别的唯一代码，在商品主数据维护中使用 |
| Size assortment（尺码分类） | X(04) - 可选字段 - 每个尺码类别最多16个尺码分类 |

**操作说明：**
- 先定义尺码类别（如服装尺码、鞋码等）
- 然后在每个类别下定义具体的尺码分类（如 S、M、L、XL 或 36、37、38 等）
