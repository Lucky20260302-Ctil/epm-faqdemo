---
project: ChainStorePlus
title: 如何启动和停止POS数据轮询？
category: 数据接口
source: v7 Book-5 Section 8.1.3 Page 11-13
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

POS数据轮询控制（POS Data Polling Control）用于启动或关闭系统中"数据发送/轮询"任务。

任务状态：
- In Progress：后台轮询通信任务正在进行中。
- Just Submitted：后台轮询通信任务刚提交。
- To be Terminated：后台轮询通信任务正在终止中。
- Terminated：后台轮询任务已终止。
- IDLE：后台轮询任务空闲。

"Start Polling"（启动轮询）功能：
此轮询任务作为后台运行，每天由计划任务触发。执行后，任务自动持续检查各店铺FTP文件夹（根据"POS/Remote Server Oriented Polling Point Maint."表中注册的轮询点），将POS上传的文件从FTP文件夹传输到POS数据文件夹以供过账处理。轮询任务正常运行时，会更新轮询状态和最后操作。

"Stop Polling"（停止轮询）功能：
允许用户关闭后台的轮询/发送通信任务。此关闭功能仅在通信任务正在进行时有效。一旦关闭，服务器与POS之间的数据交换将停止，直至下一次启动。点击"Stop Polling"按钮后，系统返回"To be terminated"状态，任务停止后当前任务状态变为"Terminated"。

"Reset"（重置）功能：
将状态更改为"IDLE"，任务准备就绪可重新启动。

"Refresh"（刷新）功能：
允许用户刷新查询画面，显示通信任务的最新状态。
