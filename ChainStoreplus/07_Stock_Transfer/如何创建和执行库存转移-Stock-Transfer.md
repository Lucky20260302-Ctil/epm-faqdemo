---
project: ChainStorePlus
title: 如何创建和执行库存转移（Stock Transfer）？
category: 库存转移
source: v7 Book-3 Section 6.4 Pages 24-28
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

创建和执行库存转移的操作步骤如下：

1. **进入库存转移功能**
   - 路径：Process > Stock Transfer > Stock Transfer (Carton)。
   - 菜单功能编号：TF6000。

2. **创建转移批次**
   - 点击工具栏上的 Create 按钮，系统将创建一个新的库存转移批次。
   - 输入相关的转移地点和库存信息。

3. **按照工作流程顺序执行以下步骤**
   
   **Step 1 - Batch Maintenance（批次维护）**
   - 创建转移记录（Create Record）
   - 修改转移记录（Modify Record）
   - 删除转移记录（Delete Record）
   - 点击 Batch Maintenance 输入初始信息。

   **Step 2 - Batch Validation（批次验证）**
   - 验证批次数据的正确性。

   **Step 3 - Generate Pick List（生成拣货单）**
   - 生成 Transfer Pick List。
   - 仓库人员根据此拣货单的信息进行商品转移。

   **Step 4 - Batch Amendment（批次修正）**
   - 如果 Step 3 已完成，批次的修改只能通过此流程进行。

   **Step 5 - Print Amendment List（打印修正清单）**
   - 生成 Transfer Amendment List。
   - 这是仓库人员在执行商品转移时应参考的最新清单。

   **Step 6 - Generate Labels & D/O（生成标签和交货单）**
   - 生成标签和交货单（Delivery Note）。

   **Step 7 - Batch Posting（批次过账）**
   - 最终过账，更新库存数量。

4. **批次状态说明**
   - Input：批次处于数据输入模式
   - Validated：批次已通过验证
   - Pick Gen.：拣货单生成流程已完成
   - Amd Create：批次修正已创建
   - Amd Print：修正清单生成流程已完成
   - Label Prt：标签和交货单生成流程已完成
   - Partly Pst：过账时发生错误，批次需要重新过账

5. **其他功能**
   - Modify Description：修改描述
   - Modify Remark：修改备注
   - Scratch Batch：废弃批次
   - Clear In Use Status：清除使用中状态
   - Change Status：更改状态
   - Search Up / Search Down：上下搜索

注意：以上功能有顺序依赖关系，必须按照工作流程顺序执行。本系统称为 Location Oriented Transfer（面向地点的转移），适用于将一个地点的大量商品转移到一个或多个其他地点的情况。
