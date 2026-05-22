---
project: ChainStorePlus
title: 如何验证并过账实物盘点结果（Validation, Variance Report & Posting）？
category: 库存管理
source: v7 Book-3 Section 6.8 Pages 37-47
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

验证实物盘点结果并完成过账的操作步骤如下：

**Step 3a - 数据验证（Stock Count Validation）**
1. 在完成实物盘点数据输入并确认无误后，执行验证操作。
2. 进入 Batch Validation 功能。
3. 系统将对输入数据进行验证。

**Step 3b - 打印差异报告（Variance Report Printing）**
1. 验证完成后，系统提示打印 Stock Variance Report（库存差异报告）。
2. 点击 OK 确认。
3. 系统显示处理进度。
4. 完成后显示完成消息。
5. 差异报告将显示冻结数量与实际盘点数量之间的差异。

**Step 4 - 批次过账（Stock Take Posting）**
1. 这是实物盘点流程的最后一步。
2. 系统将使用最终验证的盘点数据与冻结数量进行比较。
3. 点击 Batch Posting 按钮执行过账。
4. 系统显示处理进度。
5. 完成后显示完成消息。

6. **过账后的库存计算公式**
   - 过账后库存 = Current_On_Hand + (Physical_On_Hand - Freeze_On_Hand)
   - Current_On_Hand：当前库存数量
   - Physical_On_Hand：实际盘点数量
   - Freeze_On_Hand：冻结时的库存数量

7. **过账后的效果**
   - 库存数量将更新为实际盘点结果。
   - 如果存在差异，系统将生成相应的更新日志/历史记录（Update journal / history records）。
   - 对于在盘点记录中未输入但存在于该地点的商品，过账后其库存数量将被设置为零。

**完整工作流程回顾**
1. 过账所有未完成批次
2. Freeze On-Hand qty and average cost（冻结库存数量和平均成本）
3. Physical Stock Take at location / Fill in Count sheet（实地盘点/填写盘点表）
4. Batch Maintenance（输入盘点数据）
5. Batch Validation & Variance Report（验证并打印差异报告）
6. Batch Posting（过账）
