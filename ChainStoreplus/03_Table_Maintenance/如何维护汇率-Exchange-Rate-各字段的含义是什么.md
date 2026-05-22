---
project: ChainStorePlus
title: 如何维护汇率（Exchange Rate）？各字段的含义是什么？
category: 基础表维护
source: v7 Book-1 Section 4.11 Page 57-58
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

汇率表用于后台操作中的基础货币计算，在收货流程中计算自有库存价值（当采购以外币结算时）。

**重要提示：** 此汇率非 POS 前端销售单使用的汇率。

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
| Base Currency（基础货币） | X(03) - 必填字段 - 使用中的基础货币 |
| Exchange Currency（兑换货币） | X(03) - 必填字段 - 要兑换的外币 |
| Effective Date（生效日期） | 99/99/9999 - 必填字段 - 此汇率的生效日期 |
| Exchange Rate（汇率） | 9(05).9(05) - 必填字段 - 外币汇率 |
| Reverse Exchange Rate（反向汇率） | 9(05).9(05) - 必填字段或自动计算 - 反向汇率，值应等于 1 / 汇率 |
| Remarks（备注） | X(30) - 可选字段 - 此汇率的备注 |
