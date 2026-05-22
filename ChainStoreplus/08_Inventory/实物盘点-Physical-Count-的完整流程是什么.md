---
project: ChainStorePlus
title: 实物盘点（Physical Count）的完整流程是什么？
category: 库存管理
source: v7 Book-3 Section 6.8 Pages 37-47
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

实物盘点的完整流程如下：

**目标：** 在实际盘点库存后执行库存更新。

**先决条件：**
- 在创建实物盘点批次信息之前，必须先处理 Freeze On Hand Quantity（冻结库存数量）。
- 由于最终的过账操作通常远晚于盘点数据输入，冻结流程对于正确计算过账后的库存数量至关重要。

**完整操作流程：**

**第1步：冻结库存数量（Freeze On Hand Quantity）**
- 清理盘点地点的所有未完成数据批次。
- 执行 Stock Freeze，输入冻结范围（留空为选择所有商品）。
- 确认后系统以当前日期冻结库存状态。
- 重要：冻结至盘点完成期间，盘点地点不允许有任何库存移动。

**第2步：创建盘点批次并输入数据（Batch Maintenance）**
- 针对特定地点创建新的批次。
- 输入盘点表编号（Count Sheet No.）、日期和商品明细。
- 同一商品可多次输入，系统后续会合并处理。
- 此时可恢复盘点地点的正常库存活动（前提是实物盘点已完全完成）。

**第3步：验证并生成差异报告（Validation & Variance Report）**
- 执行 Batch Validation 验证数据。
- 系统自动打印 Stock Variance Report 到打印队列。
- 检查差异报告，确认是否需要进行调整。

**第4步：过账（Batch Posting）**
- 执行最终过账。
- 过账后库存 = Current_On_Hand + (Physical_On_Hand - Freeze_On_Hand)。
- 如果存在差异，系统生成 Physical Adjustment Journal。
- 未在盘点记录中输入的商品将被设置为零库存。
- 过账后不可回退。

**支持的功能：**
1. Freeze On Hand Quantity（冻结数量）
2. Batch Maintenance（批次维护）：创建/修改/删除记录
3. Batch Validation（批次验证）
4. Batch Posting（过账）
5. Modify Description（修改描述）
6. Scratch Batch（废弃批次）
7. Clear In Use Status（清除使用中状态）
8. Change Status（更改状态：Input, Validated）

**批次状态说明：**
- Input：批次正在输入
- Validated：批次已验证
- Partly Pst：过账时出错，需要重新过账

**支持两种数据输入方式：**
- 手工数据输入（Manual Data Input）
- 手持扫描设备输入（Hand Held Scanner Input）
