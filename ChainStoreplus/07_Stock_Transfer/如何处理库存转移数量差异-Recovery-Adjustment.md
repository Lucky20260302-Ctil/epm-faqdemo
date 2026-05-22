---
project: ChainStorePlus
title: 如何处理库存转移数量差异（Recovery & Adjustment）？
category: 库存转移
source: v7 Book-3 Section 6.6 Pages 31-32
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

处理库存转移数量差异的操作步骤如下：

1. **进入差异恢复功能**
   - 此功能用于处理库存转移过程中不同地点之间的数量差异。
   - 当库存转移的接收方确认收货数量不一致时，需要确定责任方。

2. **查看差异记录列表**
   - 系统仅显示存在差异的转移记录。
   - 所有记录按 Transfer Reference Order Numbers（转移参考单号）排序显示。
   - 标记为 * 的记录表示等待处理（Recovery）。

3. **选择需要处理的转移单**
   - 从列表中选择一个带 * 标记的转移记录。

4. **输入恢复明细（Stock Transfer Recovery Detail Input）**
   - 系统显示该转移单的差异详细信息。
   - 用户需要判断哪个部门/方应对差异数量负责：
     - 转出方（Sending party）：如果责任在发货方
     - 接收方（Receiving party）：如果责任在收货方
     - 双方各承担一部分：按比例分配差异

5. **系统生成调整记录**
   - 根据用户的责任分配输入，系统将自动生成适当的调整记录来恢复此差异。

6. **特殊情况处理**
   - 如果双方都不对差异负责（例如运输途中丢失且无法追责），用户需要通过执行 Physical Adjustments（物理调整）来写销（write off）该差异。
   - 此操作独立于本应用程序，需要单独执行。

注意：及时处理差异记录有助于保持库存数据的准确性，建议在发现差异后尽快处理。
