---
project: ChainStorePlus
title: 如何查询POS数据过账错误历史日志？
category: 系统管理
source: v7 Book-5 Section 9.1.2 Page 27
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

过账错误历史日志（Posting Error History Log）用于查询POS数据实时发回后台过程中的过账错误记录。如果一切正常，此查询框应为空，表示POS数据过账过程中未发现错误。

可能出现错误的原因包括：
- 某些参考表或记录在系统中缺失
- 收到损坏的记录等
- 某些显示的错误消息可能不是真正的错误，而是提醒用户更新过程中发生了异常情况

系统管理员需要判断这些消息是真正的错误及其原因，以及是否需要后续处理。

建议系统管理员至少每天检查一次此查询，或根据实际运营频率检查，确保轮询回的数据正确更新且无错误。

查询画面显示字段：
- Date（日期）：过账错误日期。
- Time（时间）：过账错误时间。
- Location（位置）：发生错误的仓库位置。
- Filename（文件名）：错误记录的文件名。
- Type（类型）：错误记录类型。
- Ref. No.（参考编号）：记录的错误参考编号（如有）。
- Error Code（错误代码）：错误参考代码（如有）。
- Error Message（错误消息）：错误消息详情。
