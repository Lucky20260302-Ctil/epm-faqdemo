---
project: ChainStorePlus
title: 如何确认库存转移的接收（Stock Transfer Receive Confirmation）？
category: 库存转移
source: v7 Book-3 Section 6.5 Pages 29-30
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

确认库存转移接收的操作步骤如下：

1. **进入接收确认功能**
   - ChainStorePlus 要求所有库存转移操作都必须执行接收确认流程。
   - 这是一个控制流程，确保转出数量被接收方正确接收并确认。

2. **选择库存转移记录**
   - 点击或按回车选择需要确认的库存转移记录。

3. **确认接收数量**
   - 系统显示转移交货单（D/N）的数量和收货数量（Rec Qty）列。
   - Rec Qty 列默认填充为等于 D/N Qty 的数值。
   - 如果实际接收数量与交货单数量一致，直接确认无需修改。
   - 如果存在差异，在 Rec Qty 列修改为实际接收数量。
     - 例如：D/N = 8 件，实际接收 = 7 件，将 Rec Qty 修改为 7。
   - Var. 列（差异数量）将在输入后自动显示差异值。

4. **确认输入正确**
   - 检查差异数量是否正确。
   - 确认提交。

5. **差异处理**
   - 如果交货和接收数量不一致，系统将自动生成差异记录（Discrepancy Record）。
   - 这些差异记录需要后续通过手动恢复和调整流程（Stock Transfer Receive Recovery & Adjustment）处理。
   - 将在下一节（6.6）中详细讨论。

注意：此控制流程是确保库存转移准确性的关键步骤，建议认真核对实际收货数量。
