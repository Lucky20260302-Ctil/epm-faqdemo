---
project: ChainStorePlus
title: 如何查看POS轮询历史记录？
category: 数据接口
source: v7 Book-5 Section 8.1.4 Page 14-15
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

轮询历史记录查询（Polling History Inquiry）是一个全面的实时查询画面，用于检查各店铺POS的最新通信活动和状态。建议用户定期查看此查询，确保服务器与POS之间的数据通信正常。

轮询历史索引画面显示以下字段：
- Date（日期）：轮询日期。
- Time（时间）：轮询时间。
- Loc.（位置）：店铺/仓库位置代码。
- Till（收银机编号）：POS的机器ID。
- Sen/Rec（发送/接收）：发送(S)和接收(R)标志。
- Type（类型）：轮询通道。
- File Size（文件大小）：数据文件的文件大小。
- File Name（文件名）：数据文件的文件名。
- Completed Date（完成日期）：处理完成的日期。
- Completed Time（完成时间）：处理完成的时间。
- Error Message（错误消息）：'E'表示该文件处理出错，空白表示正常无错误。

双击索引画面中的选定项目后，将显示轮询历史详细信息画面（Polling History Detail Screen），其中显示了该特定轮询过程的详细信息页面，主要用于跟踪正在处理的文件以及任务是否完成。
