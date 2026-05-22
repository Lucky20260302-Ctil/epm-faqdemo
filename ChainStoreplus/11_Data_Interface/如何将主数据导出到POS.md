---
project: ChainStorePlus
title: 如何将主数据导出到POS？
category: 数据接口
source: v7 Book-5 Section 8.2 Page 18-19
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

数据导出到POS（Data Export to POS）功能允许用户从后台服务器发送最新的完整主文件副本到POS。这是一个由用户按需启动的手动过程，适用于以下情况：
- 怀疑POS中文件完整性有问题时
- 需要从头重建POS应用程序和数据时

操作步骤：
1. 进入数据导出到POS画面。
2. 选择复选框，勾选需要导出到POS主数据更新文件的资料。
3. 设置筛选条件：
   - Brand Code（品牌代码）：可选，仅导出该品牌商品主数据到文件（最多10个字符）。
   - No. of record per file（每文件记录数）：整数，设置导出到文件的最大记录数。
4. 确认导出操作。

系统将生成POS主数据更新文件，供POS系统使用。
