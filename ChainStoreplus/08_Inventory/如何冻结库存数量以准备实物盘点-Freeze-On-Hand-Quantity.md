---
project: ChainStorePlus
title: 如何冻结库存数量以准备实物盘点（Freeze On Hand Quantity）？
category: 库存管理
source: v7 Book-3 Section 6.8 Pages 37-43
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

冻结库存数量以准备实物盘点的操作步骤如下：

1. **前期准备 - 清理未完成批次**
   - 在开始盘点之前，清理盘点地点的所有未完成数据批次。
   - 确保所有 outstanding batch 都已过账。

2. **进入冻结功能**
   - 从 Physical Count Process 功能中选择 Freeze On Hand Quantity。

3. **输入冻结范围**
   - Stock Freeze Operation 画面显示，要求输入 Stock Freeze Range。
   - 如果要对所有商品进行冻结，将范围留空（Leave Blank for Select ALL）。
   - 也可以指定特定的商品范围进行冻结。

4. **确认冻结**
   - 选择范围后点击 Confirm 确认。
   - 系统将以当前系统日期冻结商品的当前库存数量状态。
   - 系统会显示处理进度，完成后显示完成消息。

5. **重要注意事项**
   - **在 Stock Freeze 到 Physical Stock Counting Complete 期间，盘点地点不允许有任何库存移动更新或活动。**
   - 必须确保在冻结期间没有入库、出库、转移等操作影响该地点的库存。
   - 后续的库存差异计算将基于此冻结数量与实际盘点数量进行比较。

6. **后续流程**
   - 冻结完成后，即可开始实际的库存盘点操作。
   - 盘点完成后，可以将实际盘点数据输入系统（手工输入或手持设备上传）。
   - 实际盘点输入完成后，可以恢复该地点的正常库存活动。

7. **计算公式**
   - 过账后的库存数量计算公式：
     Current_On_Hand + (Physical_On_Hand - Freeze_On_Hand)
     其中：
     - Current_On_Hand：当前库存数量
     - Physical_On_Hand：实际盘点数量
     - Freeze_On_Hand：冻结时的库存数量

8. **未盘点商品的处理**
   - 如果存在于该地点但在实物盘点记录中未输入的商品，过账后其库存数量将被设置为零。
