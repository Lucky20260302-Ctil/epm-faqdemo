---
project: ChainStorePlus
title: 如何使用手持扫描设备执行库存转移（Hand Held Scanner Transfer）？
category: 库存转移
source: v7 Book-3 Section 6.4 Pages 24-26
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

使用手持扫描设备执行库存转移的工作流程说明：

1. **系统支持两种数据输入方式**
   - 手工数据输入（Manual Data Input）：按照标准工作流程执行。
   - 手持扫描设备输入（Hand Held Scanner Input）：通过手持条码扫描器完成数据采集。

2. **手工输入的工作流程**
   1. Batch Maintenance（批次维护）
   2. Batch Validation（批次验证）
   3. Generate Pick List（生成拣货单）
   4. Batch Amendment（批次修正）
   5. Print Amendment List（打印修正清单）
   6. Generate Labels & D/O（生成标签和交货单）
   7. Batch Posting（批次过账）

3. **手持扫描设备的工作流程**
   - 与手工输入流程不同，手持扫描设备的工作流程单独设计。
   - 通常可以通过手持设备直接扫描商品条码和位置信息，减少人工输入错误。
   - 数据采集完成后导入系统进行处理。

4. **系统特性**
   - 此流程称为 Location Oriented Transfer（面向地点的转移）。
   - 特别适用于将大量商品从一个地点转移到另一个或多个地点的情况。
   - 使用手持设备可以显著提高盘点效率和准确性。

注意：具体的手持扫描设备操作方式可能因设备型号和系统配置而异，请参考相关设备手册。
