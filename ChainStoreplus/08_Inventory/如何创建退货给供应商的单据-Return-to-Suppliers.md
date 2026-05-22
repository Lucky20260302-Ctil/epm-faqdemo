---
project: ChainStorePlus
title: 如何创建退货给供应商的单据（Return to Suppliers）？
category: 库存管理
source: v7 Book-3 Section 6.9 Pages 48-53
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

创建退货给供应商的单据操作步骤如下：

1. **进入功能**
   - 从菜单进入 Return to Suppliers（RTS）功能。
   - 此功能允许用户将商品退回给供应商，适用于错误交货、产品损坏等情况。

2. **按照工作流程执行**
   **Step 1 - Batch Maintenance（批次维护 - Header Information Folder）**
   - 点击 Create 创建新的退货批次。
   - 输入以下头信息字段：
     - Return No.（退货编号）：X(08)，必填字段，特定退货单的参考编号。
     - Date（日期）：格式 99/99/9999，必填字段（dd/mm/yyyy），退货日期。
     - Return Type（退货类型）：X(01)，必填字段，退货类型：Normal（正常）或 Consignment（代销）。
     - Supplier（供应商）：X(08)，必填字段，供应商名称。
     - Supplier Ref.（供应商参考号）：X(08)，可选字段，供应商的参考编号。
     - Transfer Ref.（转移参考号）：X(08)，可选字段，转移的参考编号。
     - Currency（货币）：X(03)，必填字段，货币代码（如 HKD、USD 等）。
     - Ex. Rate（汇率）：9(05).(05)，显示字段，基础货币与外币之间的汇率。
     - Total Ret. Qty（退货总数量）：X(08)，仅显示。
     - Ret. Amt.（退货金额）：X(08)，仅显示。
     - Discount Amt.（折扣金额）：X(08)，仅显示。
     - Net Return Amt.（退货净额）：9(09).(02)，显示字段，计算公式：总金额 x (1 - 折扣/100) - 其他折扣 + 其他费用。
     - Remarks（备注）：X(79)，两行文本描述用于备注输入。

   **Step 2 - 输入商品明细（Manage Item Folder）**
   - Item（商品）：X(09)，可选字段，如果输入了单价或地点则必填。
   - Unit Price（单价）：(+/-)9(08).9(02)，可选字段，留空/空格则分配零价格。
   - Loc.（地点）：X(04)，必填字段，执行退货交易的地点代码。
   - Qty（数量）：(+/-)9(07)，可选字段，如果商品没有颜色和尺寸，则数量字段变为必填字段。
   - Unit（单位）：X(04)，显示字段，自动从商品主文件记录中检索用户预定义的计量单位。
   - Rec. Amt.（收货金额）：(+/-)9(08).9(02)，显示字段，总金额 = 单价 x 数量，系统自动计算。
   - Total Qty/Amt.（总数量/总金额）：显示字段，该交货单中交货的商品总数量和总金额。

   **Step 3 - Batch Validation（批次验证）**
   - 验证批次数据。

   **Step 4 - Generate RTS List（生成退货清单）**
   - 生成退货清单。

   **Step 5 - Generate RTS Note（生成退货单）**
   - 生成退货单。

   **Step 6 - Batch Posting（批次过账）**
   - 最终过账，更新库存。

3. **批次状态说明**
   - Input：批次处于数据输入模式
   - Validated：批次已验证
   - RTS List：退货清单已生成
   - RTS Note：退货单已生成
