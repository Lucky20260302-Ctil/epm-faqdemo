---
project: ChainStorePlus
title: 如何创建和管理公司文件（Company File）？字段有哪些要求？
category: 系统工具
source: v7 Book-1 Section 3.1 Page 18-19
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

公司文件维护用于管理多公司控制系统中各公司信息。不同公司的信息将区分并存储在独立的公司数据目录中。

**功能：**
1. 创建记录 (Create Record) - 向公司文件添加新记录
2. 修改记录 (Modify Record) - 更改现有公司文件记录的信息
3. 删除记录 (Delete Record) - 移除现有公司
4. 查看记录 (View Record) - 显示现有公司文件记录的详细信息
5. 复制记录 (Copy Record) - 将现有公司信息复制为新的记录

**字段说明：**

| 提示 | 说明 |
|------|------|
| Company Code（公司代码） | X(02) - 必填字段 - 唯一的代码，代表特定公司 |
| Company Name（公司名称） | X(50) - 必填字段 - 公司名称 |
| Base Currency（基础货币） | X(03) - 必填字段 - 该公司通常使用的基础货币 |

**操作步骤：**
1. 进入 Administration 菜单下的 Company File Maintenance
2. 点击 "Create New Record" 图标创建新公司
3. 输入公司代码（2位字母数字）、公司名称（最多50字符）和基础货币代码（3位）
4. 保存记录
5. 如需修改，选择记录后点击 "Modify Record" 图标进行编辑
