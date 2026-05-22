---
project: ChainStorePlus
title: 如何创建交货单进行库存出库（Delivery Order - Stock Out）？
category: 配送流程
source: v7 Book-3 Section 6.10 Pages 54-65
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

创建交货单进行库存出库的操作步骤如下：

**概念说明：**
Delivery Order Process - Stock Out 允许用户使用自定义的交易代码来处理库存出库。常见的出库交易类型包括：
- Internal Use（内部使用）
- Internal Sales（内部销售）
- Give Away Samples（赠送样品）
- Sponsorship（赞助）
- Special Project Usage（特殊项目使用）
- Write Off（报废）

**操作步骤：**

1. **进入功能**
   - 从菜单进入 Delivery Order - The Stock Out Process。
   - 首先创建新批次（Create New Batch）。
   - 点击 Batch Maintenance。

2. **输入头信息（Header Information Folder）**
   - Pick Ref. No.（拣货参考编号）：X(08)，仅显示，特定交货单的参考编号。
   - Date（日期）：格式 99/99/9999，必填字段（dd/mm/yyyy），商品从此日期开始提取。
   - Dept. No.（部门编号）：X(01)，必填字段，预设的处理此交货单交易的部门代码。
   - Customer Data Input（客户数据输入）：可选。
   - Customer Name（客户名称）：X(08)，必填字段。
   - Address（地址）：必填字段。
   - Del. Date（交货日期）：格式 99/99/9999，必填字段（dd/mm/yyyy），订单需在此日期前交货。
   - Remarks（备注）：X(80)，可选字段，此拣货单的任何备注。
   - Project no.（项目编号）：X(07)，可选字段，预定义的项目 ID，如果交易基于项目则需要输入。

3. **输入货币和金额信息**
   - Currency（货币）：X(03)，必填字段，货币代码（如 HKD、USD 等）。
   - Ex. Rate（汇率）：9(05).(05)，显示字段。
   - Discount（折扣）：9(03).(02)，可选字段，交货单的折扣百分比。
   - Total Amt.（总金额）：9(09).(02)，显示字段。
   - Other Disc/Adj（其他折扣/调整）：9(09).(02)，可选字段。
   - Other Charg/Adj（其他费用/调整）：9(09).(02)，可选字段。
   - Net Total Amt.（净额）：9(09).(02)，显示字段，计算公式：Total Amt. x (1 - Discount/100) - Other Disc. + Other Charge。

4. **输入备注（Remarks Folder）**
   - Remarks（备注）：X(79)，最多 20 行文本描述。

5. **输入商品明细（Manage Item Folder）**
   - Item（商品）：X(09)，可选字段，如果输入了单价或地点则必填。
   - Trx（交易代码）：X(03)，必填字段，用户预定义并分配给此交货单的交易代码。
   - Unit Price（单价）：(+/-)9(08).9(02)，可选字段，留空则分配零价格。
   - Loc.（地点）：X(04)，必填字段，执行交货单交易的地点代码。
   - Qty（数量）：(+/-)9(07)，可选字段，如果商品没有颜色和尺寸，则数量字段变为必填字段。
   - Unit（单位）：X(04)，显示字段，自动从商品主文件检索。
   - Rec. Amt.（金额）：(+/-)9(08).9(02)，显示字段，系统自动计算。
   - Total Qty/Amt.（总数量/总金额）：显示字段。

6. **执行工作流程**
   **Step 1:** D/O Data Maintenance（交货单数据维护）
   **Step 2:** D/O Batch Validation（批次验证）- 点击 Batch Validation，系统弹出消息框，点击 OK 完成，显示完成消息。
   **Step 3:** Print Pick List（打印拣货单）- 点击 Generate Pick Up，系统弹出消息框，点击 OK 完成。
   **Step 4:** Batch Amendment（批次修正）- 可在需要时修改。
   **Step 5:** Print Amendment List（打印修正清单）
   **Step 6:** Print Delivery Order（打印交货单）- 点击 Print Delivery Order，系统弹出消息框，点击 OK 完成。用户也可以从右上角的三个垂直点菜单中选择保存为 Delivery Order。
   **Step 7:** Batch Posting（批次过账）- 最终过账。

注意：以上功能有顺序依赖关系，必须按工作流程顺序执行。
