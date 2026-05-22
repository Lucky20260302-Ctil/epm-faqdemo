---
project: ChainStorePlus
title: 如何设置和维护POS轮询点？
category: 数据接口
source: v7 Book-5 Section 8.1.1 Page 5-7
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

POS/远程服务器轮询点维护（POS/Remote Server Oriented Polling Point Maintenance）用于为数据接口设置每个远程店铺的轮询点。支持以下功能：
1. 创建记录（Create Record）
2. 修改记录（Modify Record）
3. 删除记录（Delete Record）

输入字段说明：
- POS Location（POS位置）：必填字段（如选择POS选项）。输入POS的位置代码（最多8个字符）。
- Till No.（收银机编号）：必填字段。输入POS的机器ID（1个字符）。
- Remote Server（远程服务器）：必填字段（如选择远程服务器选项）。输入远程服务器名称（最多10个字符）。
- FTP Login ID（FTP登录ID）：可选字段。输入POS的FTP服务器登录ID（最多256个字符）。
- FTP Password（FTP密码）：可选字段。输入POS的FTP服务器登录密码（最多10个字符）。
- ZLOG File Format（ZLOG文件格式）：选择格式。Delimited表示制表符分隔，Fixed Width表示固定宽度。
- Compress Zlog File（压缩ZLOG文件）：若Zlog文件大小超过特定大小，则进行压缩。

信息显示字段：
- Last Log Sent（最后发送的日志）：最后发送的日志文件名。
- Last Log Queued（最后排队的日志）：最后排队的日志文件名。
