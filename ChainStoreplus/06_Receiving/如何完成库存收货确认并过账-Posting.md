---
project: ChainStorePlus
title: 如何完成库存收货确认并过账（Posting）？
category: 收货流程
source: v7 Book-3 Section 6.3 Pages 22-23
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

库存收货确认并过账的完整操作步骤如下：

1. **Step 1 - 修改收货批次（Modify Receive）**
   - 进入 Stock Receive Maintenance（收货维护）。
   - 允许在批次内添加、修改和删除收货项目。
   - 建议在进行下一步操作前完成所有必要的修正。
   - 注意：在 Step 6 过账之前的任何时间，都可以回退到此维护步骤进行数据修正。

2. **Step 2 - 打印收货报告（Print Receive Report）**
   - 将收货数量打印到打印队列（Print Queue）。
   - 用于纸质记录和核对。

3. **Step 3 - 生成条形码（Generate Bar Code）**
   - 为收货库存打印条形码标签。

4. **Step 4 - 生成接口文件（Generate Interface File）**
   - 根据收货批次数据生成 TEXT 接口文件。
   - 此功能为系统可选功能。

5. **Step 5 - 批次验证（Batch Validation）**
   - 执行批次验证。系统要求批次在过账前必须经过验证。
   - 验证报告将自动由系统打印到打印队列。
   - 用户必须检查验证报告，确认无误后再进入下一步的过账步骤。
   - 如果发现错误，用户可以随时返回之前的步骤进行修正。

6. **Step 6 - 批次过账（Batch Posting）**
   - 这是库存数量更新的最后一步。
   - 用户必须确保批次中的所有输入数据准确无误。
   - **过账后不允许更改数据。**
   - **过账后数据不可回退。**
   - 此步骤完成后，库存余额将根据实际收货数量进行更新。

整个流程分为两大操作：
a) 根据实际收货数量更新库存余额（由仓库或收货地点操作）。
b) 根据结算成本（与供应商发票核对后）更新库存加权平均成本（由财务部门或相关负责人确认）。
