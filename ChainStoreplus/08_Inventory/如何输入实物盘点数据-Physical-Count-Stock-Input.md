---
project: ChainStorePlus
title: 如何输入实物盘点数据（Physical Count Stock Input）？
category: 库存管理
source: v7 Book-3 Section 6.8 Pages 43-45
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

输入实物盘点数据的操作步骤如下：

1. **前提条件**
   - 必须已完成 Freeze On Hand Quantity（冻结库存数量）操作。
   - 实物盘点工作应已实际完成，确保数据准确。

2. **进入实物盘点输入批次功能**
   - 在完成库存冻结操作后，从 Physical Count Process 进入 Physical Count Stock Input Batch。

3. **恢复库存活动（可选）**
   - 注意：由于实物盘点在此输入阶段应已完成，用户可以恢复盘点地点的正常库存活动。
   - **但必须确保实物盘点已完全完成。**

4. **输入批次头信息**
   - Ref. No.（参考编号）：9(08)，仅显示，系统在记录确认时自动生成，用于实物盘点记录的参考编号。
   - Date（日期）：格式 dd/mm/yyyy，必填字段，实物盘点记录的录入日期。
   - Count Sheet No.（盘点表编号）：X(15)，必填字段，用于参考的盘点表编号。
   - Remarks（备注）：X(20)，可选字段，实物盘点记录的备注说明。

5. **输入商品明细**
   - Item No.（商品编号）：X(14)，每个记录至少需要一个商品。
   - Col.（颜色）：如果商品有颜色控制则为必填字段。
   - Size（尺寸）：如果商品有尺寸控制则为必填字段。
   - Quantity（数量）：9(08)，必填字段，实际盘点数量。
   - Description（描述）：可选，仅供参考。
   - Total Qty（总数量）：9(08)，仅显示，记录的总盘点数量。

6. **注意事项**
   - 同一商品可多次输入，因为系统后续会进行合并处理（consolidation）。
   - 如果导入数据与系统现有数据不同，系统会生成 Physical Adjustment Journal。
