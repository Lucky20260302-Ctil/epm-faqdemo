---
project: ChainStorePlus
title: 如何创建部门代码（Division Code）？各字段有什么要求？
category: 基础表维护
source: v7 Book-1 Section 4.1 Page 34-36
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

部门代码用于按不同的“经营线路”组织运营。这对于组织在 POS 零售业务中使用多个“店铺名称”或“业务性质”的情况非常有用。

**示例：**
- Division "A" = Diana Fashion Chain
- Division "B" = Top Fun Gift Shop Chain
- Division "C" = Live Fit Jeans Wear Chain
- Division "D" = Stationery Chain
- Division "E" = Electronic Product Chain

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
| Division Code（部门代码） | X(01) - 必填字段 - 唯一代码，定义公司的部门 |
| Description（描述） | X(40) - 可选字段 - 所定义部门的描述或名称 |
