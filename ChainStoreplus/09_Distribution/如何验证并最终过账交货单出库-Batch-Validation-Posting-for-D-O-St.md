---
project: ChainStorePlus
title: 如何验证并最终过账交货单出库（Batch Validation & Posting for D/O Stock Out）？
category: 配送流程
source: v7 Book-3 Section 6.10 Pages 61-65
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

验证并最终过账交货单出库的操作步骤如下：

**批次验证（Batch Validation）**
1. 在完成交货单数据维护后，点击 Batch Validation。
2. 系统弹出确认消息框。
3. 点击 OK 确认执行验证。
4. 验证完成后系统显示完成消息。

**生成拣货单（Generate Pick Up / Print Pick List）**
1. 验证通过后，点击 Generate Pick Up。
2. 系统弹出消息框。
3. 点击 OK 确认。
4. 生成完成后显示完成消息。
5. 仓库人员根据拣货单进行拣货。

**批次修正（Batch Amendment - 可选）**
1. 如果拣货单生成后发现需要修改，可通过 Batch Amendment 进行。
2. 修改后打印修正清单（Print Amendment List）。

**打印交货单（Print Delivery Order）**
1. 点击 Print Delivery Order。
2. 系统弹出消息框。
3. 点击 OK 确认。
4. 完成后显示完成消息。
5. 用户也可以从右上角的三个垂直点菜单中选择 Save as Delivery Order 保存。

**批次过账（Batch Posting）**
1. 这是最后一步。
2. 执行过账后，库存数据将正式更新。
3. 过账后数据不可回退。

**完整的工作流程顺序：**
1. D/O Data Maintenance（交货单数据维护）
2. D/O Batch Validation（批次验证）
3. Print Pick List（打印拣货单）
4. Batch Amendment（批次修正）
5. Print Amendment List（打印修正清单）
6. Print Delivery Order（打印交货单）
7. Batch Posting（批次过账）

注意：这些功能有严格的顺序依赖关系，必须按顺序执行，不可跳跃。
