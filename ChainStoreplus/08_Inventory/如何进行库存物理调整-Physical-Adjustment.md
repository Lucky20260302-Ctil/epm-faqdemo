---
project: ChainStorePlus
title: 如何进行库存物理调整（Physical Adjustment）？
category: 库存管理
source: v7 Book-3 Section 6.7 Pages 33-36
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

进行库存物理调整的操作步骤如下：

1. **进入物理调整功能**
   - 从菜单进入 Physical Adjustment Process。
   - Physical Adjustment 允许用户对库存数量进行修正，并保留历史日志。

2. **菜单画面操作**
   - 在菜单画面中创建新的物理调整批次。

3. **批次维护画面 - 输入头信息（Batch Maintenance Screen）**
   - 各字段说明：
     - Ref. No.（参考编号）：9(08)，仅显示，系统在记录确认时自动生成，用于物理 I/O 记录的参考编号。
     - Date（日期）：格式 dd/mm/yyyy，必填字段。
     - Reason Code（原因代码）：X(02)，必填字段，唯一代码用于标识特定原因（在 Reason Table Maintenance 中预定义）。
     - Location Code（地点代码）：X(04)，必填字段，执行物理 I/O 操作的地点，旁边会显示地点描述。
     - Remarks（备注）：X(40)，必填字段，特定物理 I/O 记录的备注说明。

4. **批次维护画面 - 输入商品明细**
     - Seq（序号）：9(03)，仅显示，商品信息的顺序编号，每个参考编号最多 200 个序号。
     - Item No.（商品编号）：X(14)，每个参考编号至少需要一个商品。
     - Col（颜色）：X(04)，如果商品有颜色控制则为必填字段。
     - Size（尺寸）：X(04)，如果商品有尺寸控制则为必填字段。
     - Adjust（调整数量）：S9(07)，必填字段，对应商品的调整数量（正数为增加，负数为减少）。
     - Description（描述）：X(40)，可选，仅供参考。
     - Total（总计）：S9(07)，仅显示，总调整数量。

5. **执行验证和过账**
   1. Batch Maintenance（批次维护）：创建、修改、删除记录
   2. Batch Validation（批次验证）：验证数据
   3. Batch Posting（批次过账）：最终过账

6. **其他功能**
   - Modify Description：修改描述
   - Scratch Batch：废弃批次
   - Clear In Use Status：清除使用中状态
   - Change Status：更改状态（Input, Validated）
   - Search Up / Search Down：上下搜索

7. **批次状态说明**
   - Input：批次正在输入中
   - Validated：批次已通过验证
   - Partly Pst：过账时发生错误，需要重新过账
