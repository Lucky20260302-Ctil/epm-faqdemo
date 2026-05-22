---
project: ChainStorePlus
title: 如何控制POS数据过账过程？
category: 系统管理
source: v7 Book-5 Section 9.1.1 Page 25-26
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

POS数据过账控制（POS Data Posting Control）用于管理从POS终端轮询回服务器的数据更新过程。所有POS活动数据会实时传回后台服务器，需要及时更新到服务器数据库以提供及时的信息服务。

当前任务状态（Current Task Status）：
- In Progress：过账任务正在进行中。
- Just Submitted：过账任务刚提交。
- To be Terminated：过账任务正在终止中。
- Terminated：过账任务已终止。
- IDLE：过账任务空闲。

"Start POSTING"（开始过账）功能：
此过账任务在后台运行，每天由计划任务触发。任务执行后自动将POS上传的数据更新到相应文件，实现实时数据更新。过账任务正常运行时，状态显示为"IN PROGRESS"，任务将持续运行直到被计划任务或手动触发停止。

"STOP POSTING"（停止过账）功能：
允许用户停止后台的数据更新过账任务。仅在过账任务正在进行时有效。一旦停止，POS数据将不再过账，直到下次启动。

"Reset"（重置）功能：
将状态更改为"IDLE"，任务准备就绪可重新启动。

"Modify Repl. Time"（修改补货时间）功能：
允许用户更改库存补货计划时间。

"Refresh"（刷新）功能：
刷新查询画面以显示过账任务的最新状态。

"DISABLE/ENABLE POSTING"（禁用/启用过账）功能：
允许用户禁用或启用数据更新的过账过程。此模式下过账任务仍在后台运行，但会暂停数据更新，直到用户再次点击启用过账。
