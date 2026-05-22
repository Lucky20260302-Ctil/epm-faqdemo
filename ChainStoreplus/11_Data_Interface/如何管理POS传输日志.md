---
project: ChainStorePlus
title: 如何管理POS传输日志？
category: 数据接口
source: v7 Book-5 Section 8.1.2 Page 8-10
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

POS传输日志控制（POS Transmission Log Control）用于管理与POS之间的数据发送活动。ChainStore Plus后台系统会自动准备所有相关数据变更并发送到店铺POS。用户可以对传输活动进行额外控制：
- 自动发送数据（默认设置）
- 用户手动立即发送
- 根据需要从特定日期重新发送数据

画面显示以下字段：
- Date：变更数据发送的日期
- Time：变更数据发送的时间
- User：创建日志文件的用户
- Send/Receive：发送和接收标志
- Type：发送类型（Manual=手动创建，Auto=自动创建）
- Location：特定位置的日志文件
- Filename：发送的日志文件名
- Record Count：发送日志文件的记录数量

"Send Log"（发送日志）按钮：
点击此按钮将手动发送所有待发送的数据，从服务器立即发送至POS。系统会提示输入每个日志文件的记录数量，点击"OK"确认生成日志文件。

"Re-Send Log"（重新发送日志）按钮：
此功能允许用户从特定日期和位置开始，重新将下载数据从服务器发送至POS。需要输入：
- Re-send Since：输入日期（dd/mm/yyyy格式），系统将从此日期开始重新发送数据
- Log Seq：序列日志编号
- From/To Loc：将数据发送到指定范围的位置
