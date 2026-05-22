# ChainStore Plus FAQ 知识库

**总计 FAQ 条目**: 173

**主要数据源**: ChainStore Plus v7 Back End User Manual r1.2 (2023)
**补充数据源**: CS2000 v6.5 User Operation Manual rev1.1 (2009)

---

## 系统入门 (8 条)

### ChainStore Plus 主菜单屏幕的布局是怎样的？如何导航？

ChainStore Plus 采用用户友好的设计，屏幕布局在整个应用程序中保持一致。主菜单屏幕布局包含以下区域：

1. **主菜单区域 (The Main Menu Area)** - 显示主要功能模块
2. **公司名称 (The Company Name in Operation)** - 显示当前操作的公司名称
3. **子菜单区域 (The Sub Menu Area)** - 显示在主菜单左侧

**系统设置入口：**
- 点击右上角的 "三个竖点" 图标（位于登录用户名旁边），可打开系统设置
- 弹出四个选项：'Settings'（设置）、'Print'（打印）、'Language'（语言）和 'Logout'（注销）

**通用菜单/索引屏幕：**
- 大多数处理模块的首页都组织了一个索引表 (INDEX TABLE)，便于用户参考和选择
- 此屏幕提供按不同排序序列显示数据的索引
- 用户可通过输入参考索引键（搜索功能）并双击来选择所需的记录或索引

**通用详情屏幕：**
- 在索引屏幕选择记录后，详细信息将显示在此屏幕上

> 来源: v7 Book-1 Section 1.2.2 Page 8-11

> 相关图片: v7_Book-1_TABLES_p008_img00.jpeg, v7_Book-1_TABLES_p008_img01.jpeg, v7_Book-1_TABLES_p009_img00.jpeg, v7_Book-1_TABLES_p010_img00.jpeg, v7_Book-1_TABLES_p010_img01.jpeg, v7_Book-1_TABLES_p011_img00.jpeg, v7_Book-1_TABLES_p011_img01.jpeg, v7_Book-1_TABLES_p011_img02.jpeg

---

### ChainStore Plus 常用的功能键（图标）有哪些？

在 ChainStore Plus 每个操作界面的顶部都有一行功能图标，每个图标的图形或文字说明了其对应的功能。常用功能键如下：

**第1排功能图标（Fig 1）：**
- 创建新记录 (Create New Record)
- 修改记录 (Modify Record)
- 删除记录 (Delete Record)
- 查看记录 (View Record)
- 复制记录为新记录 (Copy record as new)

**第2排功能图标（Fig 2）：**
- 首条记录 (First Record)
- 上一页 (Previous Page)
- 下一页 (Next Page)
- 末条记录 (Last Record)

**第3排功能图标（Fig 3）：**
- 搜索记录 (Search record)
- 按列标题排序 (Sort by header)
- 调整列宽指示 (Adjust column indication)
- 返回 (Back)
- 刷新整个页面 (Refresh entire page)

> 来源: v7 Book-1 Section 1.2.1 Page 5-6

> 相关图片: v7_Book-1_TABLES_p005_img00.jpeg, v7_Book-1_TABLES_p006_img00.jpeg, v7_Book-1_TABLES_p006_img01.jpeg

---

### ChainStore Plus 手册中字段定义的符号（如 X(n)、9(n).9(m)、S）分别代表什么含义？

手册中使用以下符号和缩写来描述字段的含义：

**1. X(n) - 字母数字字符**
- X 代表字母数字字符 (Alphanumeric character)
- n 表示字符数量
- 例如：X(5) 表示 5 个字母数字字符，可接受 "12Abc"、"ab1d3"、"123" 等

**2. 9(n).9(m) - 数字字符**
- 9 代表数字字符 (Numeric character)
- n 表示整数位数
- m 表示小数点后的位数
- 例如：9(3).99 表示 3 位整数和 2 位小数，可接受 "12.10"、"123.09"，不接受 "as8.99"、"1234.56"、"12.987"

**3. S - 带符号数字字段**
- S 表示该数字字段可带正负号 (Signed)
- 正值 (+) 和负值 (-) 均可接受

> 来源: v7 Book-1 Section 1.2.1 Page 7

---

### 如何使用 ChainStore Plus 的打印队列（Print Queue）功能？

ChainStore Plus 生成的加工报告（非 MS Reporting Services 的分析报告）会保存在打印队列系统中，而非直接发送到打印机。使用步骤如下：

1. 点击屏幕右上角的 "三个竖点" 图标
2. 选择 'Print'（打印）选项
3. 进入 'Document Queue Management'（文档队列管理）屏幕

**打印队列管理显示的信息包括：**
- 打印文件的生成日期和时间 (Generation Date and Time)
- 报告 ID 和说明 (Report ID and Description)
- 页数 (Number of pages)
- 保护标志 (Protect flag)
- 列/右边距 (Column/Right Margin)
- 打印文件页数 (Number of pages in print file)
- 公司代码 (Company Code)

**预览功能说明：**
- 'Document Queue Management' 显示和列出用户自己的文档
- 右侧的 'Save As' 按钮允许用户将文档保存为 '.TXT' 格式文件

> 来源: v7 Book-1 Section 1.2.3 Page 12-14

> 相关图片: v7_Book-1_TABLES_p012_img00.jpeg, v7_Book-1_TABLES_p013_img00.jpeg, v7_Book-1_TABLES_p014_img00.jpeg, v7_Book-1_TABLES_p014_img01.jpeg

---

### 如何正确注销 ChainStore Plus 系统？

注销系统的步骤如下：

1. 点击屏幕右上角的 "三个竖点" 图标
2. 选择 'Logout'（注销）选项
3. 系统会弹出确认对话框 (Confirmation Dialog Box)
4. 点击 'OK' 确认注销
5. 系统将自动将您登出账户

注意：注销前请确保您已完成所有未保存的工作，以免数据丢失。

> 来源: v7 Book-1 Section 1.2.2 Page 10

> 相关图片: v7_Book-1_TABLES_p010_img00.jpeg, v7_Book-1_TABLES_p010_img01.jpeg

---

### 如何登录 ChainStore Plus 系统？登录时需要注意什么？

登录流程发生在用户输入正确的 URL 后。登录屏幕是系统的安全屏障，用于防止未经授权的访问。

**登录前准备：**
- 用户必须先从系统管理员处获取账户和密码才能进行首次登录
- 每个 ChainStore Plus 用户都需要授权密钥和密码

**登录屏幕字段说明：**

| 提示 | 说明 |
|------|------|
| User Name（用户名） | X(40) - 必填字段 - 用户识别号 |
| Password（密码） | X(40) - 必填字段 - 输入时不显示明文 - 用户个人密码 |

**功能按钮：**
| 功能 | 说明 |
|------|------|
| Full Screen Mode（全屏模式） | 勾选后允许网页浏览器进入全屏模式 |
| Login（登录） | 验证并登录系统 |

**登录步骤：**
1. 输入正确的用户名 (User Name)
2. 输入与用户 ID 对应的密码 (Password)
3. 选择是否启用 "Full Screen Mode"（全屏模式），勾选或不勾选
4. 按 <Enter> 键完成登录

> 来源: v7 Book-1 Section 2 Page 15-16

> 相关图片: v7_Book-1_TABLES_p015_img00.jpeg

---

### ChainStore Plus v7 是什么系统？它包括哪些主要模块？

ChainStore Plus 是一个综合性的零售管理软件系统，由 Sanyo Extended System Services Ltd. 开发。系统设计在多公司、多店铺、多货币、多语言环境下运行，包含前端 POS（销售点）和后端办公室操作两大部分。本手册仅针对后端办公室操作。

系统主要模块包括：
1. 表维护 (Table Maintenance)
2. 主数据维护 (Master Maintenance)
3. 采购单维护 (Purchase Order Maintenance)
4. 收货 (Stock Receipt)
5. 库存调拨 (Stock Transfer)
6. 实物调整流程 (Physical Adjustment Process)
7. 实物盘点流程 (Physical Count Process)
8. 价格加价/减价 (Price Mark-up/Down)
9. 在线查询 (On-Line Inquiry)
10. 基于 SQL Server Reporting Services 的 Web 管理报表
11. 数据接口/交换 (Data Interface/Exchange)
12. 管理流程 (Administration Process)

注意：有关最新的可选模块列表，请咨询 Sanyo Extended System Services Ltd. 的销售部门。

> 来源: v7 Book-1 Section 1.1 Page 4

> 相关图片: v7_Book-1_TABLES_p001_img00.jpeg, v7_Book-1_TABLES_p001_img01.jpeg, v7_Book-1_TABLES_p001_img02.jpeg

---

### 如何访问 ChainStore Plus 的系统设置和选择语言？

访问系统设置的步骤如下：

1. 点击屏幕右上角的 "三个竖点" 图标（位于登录用户名旁边）
2. 从弹出菜单中选择 'Settings'（设置）
3. 在设置菜单中可以访问以下功能：
   - **Account（账户）** - 更改登录密码
   - **Language（语言）** - 更改系统显示语言

**语言选择：**
ChainStore Plus 支持多种语言，默认支持的语言包括：
- 英语 (English)
- 繁体中文 (Traditional Chinese)
- 简体中文 (Simplified Chinese)

用户可通过将鼠标悬停在语言选项上并点击来选择所需语言。系统界面将立即切换为所选语言显示。

> 来源: v7 Book-1 Section 1.2.2 Page 9, Section 3.8 Page 30

> 相关图片: v7_Book-1_TABLES_p009_img00.jpeg, v7_Book-1_TABLES_p030_img00.jpeg

---

## 系统工具 (8 条)

### 如何创建和管理公司文件（Company File）？字段有哪些要求？

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

> 来源: v7 Book-1 Section 3.1 Page 18-19

> 相关图片: v7_Book-1_TABLES_p018_img00.jpeg, v7_Book-1_TABLES_p019_img00.jpeg, v7_Book-1_TABLES_p019_img01.jpeg, v7_Book-1_TABLES_p019_img02.jpeg

---

### 用户表维护（User Table Maintenance）的作用是什么？如何设置用户访问权限？

用户表维护是系统的安全模块，提供对程序、文件和功能的访问控制。如果某个用户对某功能被设置为 'NO' 访问权限，则不允许未经授权的数据访问。系统管理员需要在此维护模块中根据用户权限构建访问授权。

该模块在主菜单的 Administration 下，用于以下目的：
- 维护用户登录信息
- 设置每个操作模块、程序或功能的访问授权

**可使用功能：**
1. 创建记录 (Create Record) - 向系统添加新记录
2. 修改记录 (Modify Record) - 更改现有记录信息
3. 删除记录 (Delete Record) - 移除现有记录
4. 查询记录 (Inquiry Record) - 显示选定记录的详细信息
5. 复制记录 (Copy Record) - 将现有记录复制为新记录

> 来源: v7 Book-1 Section 3.2 Page 20, Section 3.4 Page 23-24

> 相关图片: v7_Book-1_TABLES_p020_img00.jpeg, v7_Book-1_TABLES_p023_img00.jpeg

---

### 用户安全维护中各字段（用户名、用户ID、级别等）的含义是什么？

用户安全维护（User Security Maintenance）屏幕用于维护用户的登录信息和系统访问权限。以下是各字段的详细说明：

**字段说明：**

| 提示 | 说明 |
|------|------|
| User Name（用户名） | X(40) - 必填字段 - 用户登录 ID |
| Full Name（全名） | X(40) - 必填字段 - 用户全名 |
| User ID（用户编号） | X(03) - 必填字段 - 系统用户 ID |
| Class（级别） | X(01) - 必填字段 - 用户在公司的级别：0=管理员，1=正式员工（可查看产品成本），2=初级员工（不可查看产品成本） |
| User Group（用户组） | X(40) - 可选字段 - ChainStorePlus 用户组 |
| Dept（部门） | X(01) - 可选字段 - 部门代码 |
| Expiry Period（有效期限） | 月数 - 用户密码的有效期（月数） |
| Expiry Date（到期日期） | dd/mm/yyyy - 用户密码到期日期 |
| Change button（更改按钮） | 用户密码设置按钮 - 使用方法请参见下一段落（用户密码更改） |

> 来源: v7 Book-1 Section 3.4 Page 23-24

> 相关图片: v7_Book-1_TABLES_p023_img00.jpeg

---

### 如何查看用户程序访问列表（User Program Access Listing）？

用户程序访问列表用于搜索和列出用户在后台系统中可访问的程序或模块。

**操作步骤：**
1. 在 Administration 菜单中选择 User Program Access Listing
2. 系统将提示确认对话框 (Confirmation Dialog Box)
3. 确认输入信息正确后点击 "OK"
4. 生成的列表会显示在文档队列管理屏幕 (Document Queue Management Screen) 中（请参阅打印队列部分）

**排序选项：**
- **P - Program ID（程序ID）**：结果集按程序 ID 排序
- **M - Main Sequence（主序列）**：结果集按程序描述排序

**输出结果：**
打印结果将显示用户可访问的所有程序和模块的列表，便于管理员审核用户权限设置。

> 来源: v7 Book-1 Section 3.3 Page 21-22

> 相关图片: v7_Book-1_TABLES_p021_img00.jpeg, v7_Book-1_TABLES_p021_img01.jpeg, v7_Book-1_TABLES_p022_img00.jpeg

---

### 如何更改 ChainStore Plus 的登录密码？

用户可以通过以下步骤更改登录密码：

1. 点击屏幕右上角的 "三个竖点" 图标
2. 选择 'Settings'（设置）选项
3. 在设置界面点击 'Account'（账户）
4. 在密码更改界面，需要输入 'Old Password'（旧密码）进行验证
5. 输入新密码并确认
6. 保存更改

注意：请确保新密码符合公司的密码策略要求（如最小字符数、禁止包含限制关键词等）。

> 来源: v7 Book-1 Section 3.5 Page 25

> 相关图片: v7_Book-1_TABLES_p025_img00.jpeg, v7_Book-1_TABLES_p025_img01.jpeg

---

### 如何设置密码限制关键词（Password Restricted Keyword）？

密码限制关键词功能允许用户在创建账户或更改密码时禁止某些字符或字符串。此表用于查看和输入不能作为密码的全部或部分内容的文字或字符串。

**操作步骤：**
1. 进入 Administration 菜单下的 User Password Restricted Keyword
2. 输入需要限制的关键词
3. 保存设置

**字段说明：**

| 提示 | 说明 |
|------|------|
| Restricted Keyword（限制关键词） | X(40) - 必填字段 - 不能作为用户密码全部或部分内容的文字或字符串 |

**作用：**
- 设置后，任何用户在创建或更改密码时，如果密码包含这些关键词（全部或部分），系统将拒绝该密码
- 这有助于防止使用公司名称、品牌名等易被猜测的密码

> 来源: v7 Book-1 Section 3.6 Page 26-27

> 相关图片: v7_Book-1_TABLES_p026_img00.jpeg, v7_Book-1_TABLES_p027_img00.jpeg

---

### 如何设置密码策略（Password Policy）？各字段的含义是什么？

密码策略定义了密码强度规则，用于判断新密码是否有效。此功能设定密码必须遵守的规则。

**字段说明：**

| 提示 | 说明 |
|------|------|
| Effective Date（生效日期） | X(dd/mm/yyyy) - 必填字段 - 此组密码策略的生效日期 |
| Restrict the reuse recently used passwords times（限制近期密码重复使用次数） | X(5) - 必填字段 - 决定在旧密码可重新使用之前，用户账户必须关联多少个唯一新密码 |
| min char（最小字符数） | X(02) - 可选字段 - 密码的最小字符数 |

**作用：**
- 确保用户设置的新密码满足组织安全要求
- 防止密码短期内重复使用
- 设置最小密码长度，增强密码强度

> 来源: v7 Book-1 Section 3.7 Page 28-29

> 相关图片: v7_Book-1_TABLES_p028_img00.jpeg, v7_Book-1_TABLES_p029_img00.jpeg

---

### ChainStore Plus 支持哪些界面语言？如何切换系统语言？

ChainStore Plus 支持多语言显示，用户可以根据需要选择系统显示语言。

**默认支持的语言：**
- 英语 (English)
- 繁体中文 (Traditional Chinese)
- 简体中文 (Simplified Chinese)

**切换语言步骤：**
1. 点击屏幕右上角的 "三个竖点" 图标
2. 选择 'Settings'（设置）选项
3. 点击 'Language'（语言）
4. 将鼠标滑过所需语言并点击选择
5. 系统界面将立即切换为所选语言显示

> 来源: v7 Book-1 Section 3.8 Page 30

> 相关图片: v7_Book-1_TABLES_p030_img00.jpeg

---

## 基础表维护 (20 条)

### POS 付款方式（POS Tender）如何设置？各字段的含义是什么？

此表用于定义 POS 前台的销售中接受的付款类型。常见的付款方式包括现金、信用卡（AE、Visa 等）、外币（美元、日元、英镑等），甚至公司发行的现金券都可以在此表定义。

**字段说明：**

| 提示 | 说明 |
|------|------|
| Currency Code（货币代码） | X(03) - 必填字段 - 此付款类型的货币 |
| Payment Code（付款代码） | X(03) - 必填字段 - 表示此特定付款类型的唯一代码。注意："FMM"（会员退款）、"MEM"（会员）、"EPM"（电子支付）为系统保留词，用户不得使用 |
| Location Code（地点代码） | X(04) - 可选字段 - 此付款类型将适用的地点 |
| Payment Name（付款名称） | X(40) - 必填字段 - 此付款类型的描述 |
| Rate（汇率） | 9(05).9(05) - 必填字段 - POS 中此付款类型使用的汇率 |
| Payment Type（付款类型） | 必填字段 - 通过组合框选择 - 对于 POS 前台的退货凭证功能，必须定义 'Return Voucher' 和 'Return Voucher redeem' 类型。对于 POS 前台的 'Deposit Return' 功能，至少必须定义 'Credit Voucher' 类型 |
| S9000 Payment Type（S9000付款类型） | X(10) - 如果 "Payment Type"="A-Electronic Payment" 则为必填，否则为空 - 从 S9000 设备返回的付款类型 |
| Report Type（报表类型） | 必填字段 - 选择 "Card" 属于 Card 组，"Others" 属于 Others 组，"Traveller Cheque" 属于 Traveller Cheque 组，"Cash" 属于 Cash 组 |
| Commission（佣金） | 付款类型的佣金率 |
| Last Modified Date（最后修改日期） | 99/99/9999 (dd/mm/yyyy) - 仅显示 - 上次修改此付款类型记录的日期 |
| Skip Daily Ex. Rate（跳过每日汇率） | 必填字段 - 指示此付款类型是否显示在每日汇率输入屏幕的标志（选择 "Yes" 或 "No"） |

> 来源: v7 Book-1 Section 4.9 Page 51-52

> 相关图片: v7_Book-1_TABLES_p051_img00.jpeg

---

### POS 付款类型（Payment Type）ID 及其功能有哪些？

POS 付款类型的功能设置及其使用说明如下：

| ID | 付款类型 | 说明 |
|----|----------|------|
| A | Electronic Payment（电子支付） | 仅在启用"信用卡接口"选项时需要。客户通过已认证的 S9000 卡终端支付时，终端会自动返回代码识别具体信用卡类型（如 Visa、Master Card）。需要与表中的 "S9000 Payment Type" 字段配合使用 |
| B | EPS（易办事） | 允许 S9000 连接的 EPS 支付 |
| C | Credit Card（信用卡） | 在没有 S9000 卡终端连接的情况下接受信用卡支付。常见信用卡类型（Visa、AE、Master 等）在表中的 Payment Code 字段定义 |
| D | Credit Voucher（信用凭证） | 用于 POS 退货的不可兑换退款凭证 |
| E | Credit Card Refund（信用卡退款） | 用于销售退货或商品退货操作中的信用卡退款控制 |
| F | Return Voucher Redeem（退货凭证兑换） | 此特定付款方式归类为客户兑换退货凭证 |
| G | Cash Voucher（现金券） | 用于非序列号基的现金券 |
| H | Uniform Coupon（制服券） | 此付款代码用于"员工制服"兑换目的 |
| I | NOT use（不使用） | 不使用 |
| J | Cash Coupon（现金券，序列号） | 用于基于序列号的现金券。使用时将验证现金券的序列号 |
| K | Credit Sales（赊销） | 此付款代码归类为赊销 |
| L | Cheque（支票） | 个人银行支票付款 |
| P | Gift Certificate（礼品券） | 礼品券付款。必须使用礼品券序列号并进行验证 |
| R | Return Voucher（退货凭证） | 用于 POS 退货的可兑换现金券。必须使用退货凭证序列号并进行验证 |
| O | Online Coupon Redeem（在线券兑换） | 此付款方式由客户在线可用积分兑换的奖励积分支付 |

**S9000 相关类型：**
| ID | 付款类型 | 说明 |
|----|----------|------|
| 0 | S9000(EPM) | 仅在启用"信用卡接口"选项时需要。客户通过 S9000 卡终端使用信用卡（除 CUP 卡外）支付时使用 |
| 1 | S9000(CUP) | 仅在启用"信用卡接口"选项时需要。客户通过 S9000 卡终端使用 CUP 卡支付时使用 |
| 2 | Octopus（八达通） | 仅在启用"八达通"接口选项时需要。通过八达通智能卡支付的付款方式。需要额外的八达通读取设备和程序 |
| 3 | EPAY(Installment)（分期付款） | 不再使用 |
| 4 | S9000 (EIN) | 仅在启用"信用卡接口"选项时需要。S9000 的分期付款功能 |

> 来源: v7 Book-1 Section 4.9 Page 53-55

> 相关图片: v7_Book-1_TABLES_p053_img00.jpeg, v7_Book-1_TABLES_p053_img01.jpeg

---

### 如何设置 POS 付款按键控制（POS Payment Key Button Control）？

此流程允许用户根据个人偏好设置 POS 前台的付款按键顺序。

**操作说明：**

**按键分配规则：**
- 用户可以自由编辑/分配付款流程到每个按钮
- 最后一个 <F10> 按钮保留为 "EXIT"（退出）按钮，不可更改
- 如有必要，用户可以在一个按钮中"分组"多个付款类型
- 示例："Foreign Exchange"（外币）按钮可以将多种可接受的外币归入一个按钮下，如美元、新台币、欧元、日元等

**布局设置：**
- POS 付款按键布局可以分配到店铺级别（Shop Level）
- 如果设置为 "Blank"（空白），则表示适用于所有店铺
- POS 付款按键布局根据每种基础货币（Base Currency）定义：
  - 至少为接收港币（HK$）的香港店铺设置一套布局
  - 为接收人民币（RMB）的中国店铺设置另一套 POS 付款按键布局

**付款代码引用：**
- 按键引用的付款代码需要在 POS 付款方式表（Payment Table）中预先定义

> 来源: v7 Book-1 Section 4.10 Page 56

> 相关图片: v7_Book-1_TABLES_p056_img00.jpeg, v7_Book-1_TABLES_p056_img01.jpeg

---

### 如何维护 POS 安全访问（POS Security Access）？如何分配功能权限？

POS 安全访问维护用于定义不同的安全代码及其功能访问权限。

**摘要页面：**
- 列出系统中已定义的所有"安全代码"(Security Code)
- 这些代码根据定义的"角色描述"赋予不同的功能访问权限
- 例如："Shop Manager"（店铺经理）角色的访问权限应与 "Shop Supervisor"（店铺主管）或 "Shop Trainee"（店铺实习生）不同

**权限分配：**
- 首先需要为您需要的角色创建访问权限，如"Shop Manager"或"Sales Supervisor"的不同 POS 安全代码
- 然后将此安全代码（如店铺经理）分配给在店铺中担任销售经理角色的销售人员（或一组店铺）

**功能权限设置：**
- 勾选符号（Tick）表示已授权访问该流程的功能
- 锁符号（Lock）表示禁止访问该流程功能

**示例：**
- 管理员 (Administrator) 角色拥有所有功能的访问权限（全部勾选）
- 普通销售人员可能只有销售相关功能的访问权限

> 来源: v7 Book-1 Section 4.14 Page 63-64

> 相关图片: v7_Book-1_TABLES_p063_img00.jpeg, v7_Book-1_TABLES_p064_img00.jpeg

---

### 如何维护销售人员代码（Sales Staff Code）？POS 安全代码如何设置？

此表用于在系统中登记销售人员的详细信息。通过为每个销售人员分配唯一代码，系统将自动跟踪销售人员的访问授权、销售业绩，甚至在 POS 中的登录和签退考勤。

**字段设置说明：**

**POS 安全代码 (POS Security Code)：**
- 需要预先定义 POS 安全代码表
- 此代码已预设了功能访问权限
- 系统会对照相关表验证此代码

**密码设置：**
- 可设置限制此 POS 用户必须使用密码登录 POS
- 密码需要每 N 个月更改一次

**地点访问权限设置：**
- 这是 POS 用户的地点访问权限设置
- 示例中，此 POS 用户被设置为仅允许访问特定的"地点"/店铺
- 授权地点在示例中进一步定义为仅限 A005 地点
- 用户可以为每个用户设置多个访问地点，每个地点可设置不同的功能访问权限

> 来源: v7 Book-1 Section 4.8 Page 49-50

> 相关图片: v7_Book-1_TABLES_p049_img00.jpeg, v7_Book-1_TABLES_p050_img00.jpeg

---

### 如何维护类别代码（Category Code）？字段有哪些要求？

类别代码维护用于为商品维护通用类别信息，该信息在商品主数据维护（Item Master Maintenance）中使用。

**功能：**
1. 创建记录 (Create Record)
2. 修改记录 (Modify Record)
3. 删除记录 (Delete Record)
4. 查看记录 (View Record)
5. 复制记录为新记录 (Copy Record as new)
6. 查找记录 (Find Record)
7. 按列标题排序 (Sort by header)
8. 调整列宽指示 (Adjust column indication)

**字段说明：**

| 提示 | 说明 |
|------|------|
| Category Code（类别代码） | X(03) - 必填字段 - 用于在商品主数据维护中定义类别的唯一代码 |
| Description（描述） | X(40) - 必填字段 - 该类别的描述 |
| Sub. Category（子类别） | X(02) - 可选字段 - 定义该类别的子类别的唯一代码，使用此类别的商品必须属于其中一个子类别，最多可输入30个 |
| Sub. Category Description（子类别描述） | X(10) - 如果已定义子类别代码则为必填 - 子类别的描述 |
| Serial Flag（序列号标志） | 可选 - 设置为 "YES" 表示该类别的商品将具有序列号 |
| Discount Control（折扣控制） | X(01) - 必填字段 - 默认为 'No' - 设置为 "YES" 表示该类别的商品有折扣控制，POS 销售时不允许打折 |
| Max. Discount（最大折扣） | 99.99 - 可选字段 - 仅在折扣控制设置为 'NO' 时可用 - 以零售价的百分比表示 |

> 来源: v7 Book-1 Section 4.4 Page 43-44

> 相关图片: v7_Book-1_TABLES_p043_img00.jpeg

---

### 如何维护尺码类别（Size Category）？字段有哪些要求？

尺码类别维护用于为商品维护一组尺码范围的类别，在商品主数据维护中使用。

**功能：**
1. 创建记录 (Create Record)
2. 修改记录 (Modify Record)
3. 删除记录 (Delete Record)
4. 查看记录 (View Record)
5. 复制记录为新记录 (Copy Record as new)
6. 查找记录 (Find Record)
7. 按列标题排序 (Sort by header)
8. 调整列宽指示 (Adjust column indication)

**字段说明：**

| 提示 | 说明 |
|------|------|
| Size Category（尺码类别） | X(04) - 必填字段 - 用于定义特定尺码类别的唯一代码，在商品主数据维护中使用 |
| Size assortment（尺码分类） | X(04) - 可选字段 - 每个尺码类别最多16个尺码分类 |

**操作说明：**
- 先定义尺码类别（如服装尺码、鞋码等）
- 然后在每个类别下定义具体的尺码分类（如 S、M、L、XL 或 36、37、38 等）

> 来源: v7 Book-1 Section 4.5 Page 45

> 相关图片: v7_Book-1_TABLES_p045_img00.jpeg

---

### 如何维护颜色代码（Color Code）？各字段有什么要求？

颜色代码维护用于为商品维护通用颜色信息，在商品主数据维护中使用。

**功能：**
1. 创建记录 (Create Record)
2. 修改记录 (Modify Record)
3. 删除记录 (Delete Record)
4. 查看记录 (View Record)
5. 复制记录为新记录 (Copy Record as new)
6. 查找记录 (Find Record)
7. 按列标题排序 (Sort by header)
8. 调整列宽指示 (Adjust column indication)

**字段说明：**

| 提示 | 说明 |
|------|------|
| Color Code（颜色代码） | X(05) - 必填字段 - 用于定义特定颜色的唯一代码，在商品主数据维护中使用 |
| Description（描述） | X(40) - 可选字段 - 指代此颜色代码的简短描述 |
| Sub Color（子颜色） | 可选 - 可以在次级（可选）维护下的 "Sub Color"（子颜色）表中定义 |

> 来源: v7 Book-1 Section 4.6 Page 46-47

> 相关图片: v7_Book-1_TABLES_p046_img00.jpeg, v7_Book-1_TABLES_p046_img01.jpeg

---

### 如何维护品牌代码（Brand Code）？各字段有什么要求？

品牌代码维护用于为商品维护通用品牌信息，在商品主数据维护中使用。

**功能：**
1. 创建记录 (Create Record)
2. 修改记录 (Modify Record)
3. 删除记录 (Delete Record)
4. 查看记录 (View Record)
5. 复制记录为新记录 (Copy Record as new)
6. 查找记录 (Find Record)
7. 按列标题排序 (Sort by header)
8. 调整列宽指示 (Adjust column indication)

**字段说明：**

| 提示 | 说明 |
|------|------|
| Brand Code（品牌代码） | X(06) - 必填字段 - 用于定义特定品牌的唯一代码，在商品主数据维护中使用 |
| Brand Name（品牌名称） | X(40) - 可选字段 - 表示该品牌代码的名称 |
| Supplier Code（供应商代码） | X(08) - 必填字段 - 品牌的供应商 - 供应商代码将对照供应商表进行验证 |
| Max. Discount（最大折扣） | 99.99 - 可选字段 - 该品牌允许的最大折扣 |

> 来源: v7 Book-1 Section 4.7 Page 47-48

> 相关图片: v7_Book-1_TABLES_p047_img00.jpeg

---

### 如何维护性别/性别代码（Sex/Gender Code）？

性别/性别代码表用于定义产品的性别类型。此表是商品主数据表 (Item Master Table) 的可选表，根据需要决定是否使用。

**说明：**
- 此表归类在"特殊表（可选表）"(Special/Optional Tables) 下
- 这些表主要用于描述"产品风格"(The Product Style)，可能根据商品主数据维护的可选需求而定
- 在使用前，请务必咨询业务顾问 (Business Consultant)
- 大多数常规处理不需要此表，除非有特定目的

**示例：**
- 定义如 "Men"（男装）、"Women"（女装）、"Unisex"（男女通用）等性别类型

> 来源: v7 Book-1 Section 4.16 Page 66

> 相关图片: v7_Book-1_TABLES_p066_img00.jpeg, v7_Book-1_TABLES_p066_img01.jpeg

---

### 如何维护系列代码（Collection Code）？

系列代码表用于定义产品的特定"系列"(Collection)。此表是商品主数据表 (Item Master Table) 的可选表，根据需要决定是否使用。

**说明：**
- 此表归类在"特殊表（可选表）"(Special/Optional Tables) 下
- 主要用于描述"产品风格"(The Product Style)，属于商品主数据维护的可选需求
- 大多数常规处理不需要此表，除非有特定目的
- 在使用前，请务必咨询业务顾问 (Business Consultant)

**示例：**
- 定义如 "Spring Collection 2023"（2023春季系列）、"Summer Collection"（夏季系列）等

> 来源: v7 Book-1 Section 4.17 Page 67

> 相关图片: v7_Book-1_TABLES_p067_img00.jpeg

---

### 如何维护标签代码（Label Code）？

标签代码表用于某些特殊商品标签描述，仅限特定用途使用。

**说明：**
- 此表归类在"特殊表（可选表）"(Special/Optional Tables) 下
- 用于描述"产品风格"(The Product Style) 的可选需求
- 系统中目前没有常规处理流程使用此表
- 在使用前，请务必咨询业务顾问 (Business Consultant)
- 大多数常规处理不需要此表，除非有特定目的

> 来源: v7 Book-1 Section 4.18 Page 68

> 相关图片: v7_Book-1_TABLES_p068_img00.jpeg

---

### 如何维护计量单位（Unit of Measure）？

计量单位维护用于定义和管理系统中的计量单位。

**说明：**
- 此表属于特殊表/可选表类别
- 用于定义商品的各种计量单位（如件、箱、公斤、米等）
- 是系统基础表之一，用于商品主数据维护中定义商品的计量方式

**注意：** 此表的具体字段细节请参阅系统的实际屏幕显示，根据业务需求进行定义。

> 来源: v7 Book-1 Section 4.19 Page 69-70

> 相关图片: v7_Book-1_TABLES_p069_img00.jpeg, v7_Book-1_TABLES_p070_img00.jpeg

---

### 如何创建和管理地点代码（Location Code）？各字段的含义是什么？

地点代码用于识别特定地点的用途。系统在许多关键流程中使用地点信息。

**功能：**
1. 创建记录 (Create Record)
2. 修改记录 (Modify Record)
3. 删除记录 (Delete Record)
4. 查看记录 (View Record)
5. 复制记录为新记录 (Copy Record as new)
6. 查找记录 (Find Record)
7. 按列标题排序 (Sort by header)
8. 调整列宽指示 (Adjust column indication)

**(I) 汇总显示 (Summary Display)**

**(II) 常规信息屏幕 (General Info) 字段：**

| 提示 | 说明 |
|------|------|
| Location Code（地点代码） | X(08) - 必填字段 - 首字符应引用部门代码 - 用于定义地点的唯一代码 |
| Location Type（地点类型） | X(01) - 必填字段 - 用户必须从选择框中选择地点类型 |
| Franchisee Operation（特许经营） | 可选复选框 - 如果是特许经营店铺则勾选，其处理流程可能与常规自有店铺不同 |
| Location Name（地点名称） | X(40) - 必填字段 - 地点的描述或名称 |

**(III) 其他属性 (Other Properties) 字段：**

| 提示 | 说明 |
|------|------|
| Open/Close（开店/关店日期） | 输入店铺开业或关闭日期 - dd/mm/yyyy |
| Interface Loc（接口地点） | 可选。仅用于与第三方系统接口对接，其地点代码与 ChainStorePlus 不同 |
| Repl. W/H（补货仓库） | 可选。仅当地点有特殊补货仓库时使用 |
| Project Location（项目地点） | X(01) - 可选字段 - 勾选则启用为此地点为项目地点，需要项目编号才能在项目地点安装 POS |
| Department Store（百货商店） | X(01) - 可选字段 - 勾选则启用为此地点为百货商店 |
| Not Download to POS（不下载到POS） | X(01) - 可选字段 - 勾选则此地点不下载到前端 POS |
| Tax Exemption Allowed（允许免税） | X(01) - 可选字段 - 勾选则此地点允许免税 |
| Not allowed in Stock Transfer（不允许库存调拨） | X(01) - 可选字段 - 勾选则此地点不包含在 POS 库存调拨选择中 |
| Exclude O/H（排除在库存外） | X(01) - 可选字段 - 勾选则此地点排除在现有库存计算之外 |
| Country（国家） | X(02) - 必填字段 - 地点所在的国家代码 |
| Channel（渠道） | 必填字段 - 手动维护的渠道属性，如 1-Retail（零售）、2-Outlet（折扣店）、3-Others（其他） |

**(IV) 组分配 (Group Assignment) - 内部地区结构：**
- 用于定义地点的"内部地区结构"（即该店铺属于哪个地区）
- 示例中地点被定义为"广州市"的"城市级"
- 树状结构显示在列表框中供用户参考
- 注意：各层级之间的树状关系需要先在"Location Tree"（地点树）表中定义
- 控制地点从"店铺到仓库"和"店铺到店铺"的调拨权限
- 在示例中，该店铺设置允许向"省"级别的仓库调拨，店铺间调拨仅限"城市"内

> 来源: v7 Book-1 Section 4.2 Page 37-41

> 相关图片: v7_Book-1_TABLES_p037_img00.jpeg, v7_Book-1_TABLES_p038_img00.jpeg, v7_Book-1_TABLES_p039_img00.jpeg, v7_Book-1_TABLES_p039_img01.jpeg, v7_Book-1_TABLES_p041_img00.jpeg

---

### 地点类别维护（Location Class Maintenance）的作用是什么？

地点类别用于识别每个地点类别属性。系统在许多关键流程中使用此地点类别信息。

**功能：**
1. 创建记录 (Create Record)
2. 修改记录 (Modify Record)
3. 删除记录 (Delete Record)
4. 查看记录 (View Record)
5. 复制记录为新记录 (Copy Record as new)
6. 查找记录 (Find Record)
7. 按列标题排序 (Sort by header)
8. 调整列宽指示 (Adjust column indication)

此表用于定义地点分类属性，例如店铺类型、仓库类型等，便于系统按类别进行管理和处理。

> 来源: v7 Book-1 Section 4.3 Page 42

> 相关图片: v7_Book-1_TABLES_p042_img00.jpeg, v7_Book-1_TABLES_p042_img01.jpeg, v7_Book-1_TABLES_p042_img02.jpeg

---

### 如何设置地点信息（Location Message）如促销信息和节日问候？

地点信息维护用于设置打印在销售单上的特殊信息，如促销信息、圣诞节和新年等节日问候。可以在特定时间段内打印。

**字段设置说明：**

- **地点代码 (Location Code)：**
  - 留空表示适用于"所有地点"（ALL location）
  - 如果输入了地点代码，则仅对该特定地点有效

- **生效日期：**
  - 设置信息在 POS 中的有效打印日期
  - 在指定日期范围内，信息才会打印在销售单上

**示例：**
- 圣诞节期间设置 "Merry Christmas" 信息
- 设置促销活动信息，如 "Summer Sale - 20% Off"
- 指定信息的生效和截止日期，确保在正确的时间段打印

> 来源: v7 Book-1 Section 4.13 Page 61-62

> 相关图片: v7_Book-1_TABLES_p061_img00.jpeg

---

### 如何维护仓库批次备注（Warehouse Lot Remarks）？

仓库批次备注维护用于管理与商品主数据相关的仓库批次备注表，以供将来的报表使用。

**字段说明：**

| 提示 | 说明 |
|------|------|
| Item Code（商品代码） | X(14) - 显示字段 - 商品代码 |
| Description（描述） | X(30) - 显示字段 - 商品描述 |
| W/H Lot Remarks（仓库批次备注） | X(8) - 可选字段 - 商品所定义的仓库批次备注 |

**使用说明：**
- 此表属于次级表（Secondary Tables），可能仅针对特定客户有特定用途
- 用于在仓库和批次级别对商品添加备注信息
- 备注信息可用于将来的报表和分析目的

> 来源: v7 Book-1 Section 4.15 Page 65

> 相关图片: v7_Book-1_TABLES_p065_img00.jpeg, v7_Book-1_TABLES_p065_img01.jpeg

---

### 如何创建部门代码（Division Code）？各字段有什么要求？

部门代码用于按不同的“经营线路”组织运营。这对于组织在 POS 零售业务中使用多个“店铺名称”或“业务性质”的情况非常有用。

**示例：**
- Division "A" = Diana Fashion Chain
- Division "B" = Top Fun Gift Shop Chain
- Division "C" = Live Fit Jeans Wear Chain
- Division "D" = Stationery Chain
- Division "E" = Electronic Product Chain

**功能：**
1. 创建记录 (Create Record)
2. 修改记录 (Modify Record)
3. 删除记录 (Delete Record)
4. 查看记录 (View Record)
5. 复制记录为新记录 (Copy Record as new)
6. 查找记录 (Find Record)
7. 按列标题排序 (Sort by header)
8. 调整列宽指示 (Adjust column indication)

**字段说明：**

| 提示 | 说明 |
|------|------|
| Division Code（部门代码） | X(01) - 必填字段 - 唯一代码，定义公司的部门 |
| Description（描述） | X(40) - 可选字段 - 所定义部门的描述或名称 |

> 来源: v7 Book-1 Section 4.1 Page 34-36

> 相关图片: v7_Book-1_TABLES_p034_img00.jpeg, v7_Book-1_TABLES_p036_img00.jpeg

---

### 如何维护汇率（Exchange Rate）？各字段的含义是什么？

汇率表用于后台操作中的基础货币计算，在收货流程中计算自有库存价值（当采购以外币结算时）。

**重要提示：** 此汇率非 POS 前端销售单使用的汇率。

**功能：**
1. 创建记录 (Create Record)
2. 修改记录 (Modify Record)
3. 删除记录 (Delete Record)
4. 查看记录 (View Record)
5. 复制记录为新记录 (Copy Record as new)
6. 查找记录 (Find Record)
7. 按列标题排序 (Sort by header)
8. 调整列宽指示 (Adjust column indication)

**字段说明：**

| 提示 | 说明 |
|------|------|
| Base Currency（基础货币） | X(03) - 必填字段 - 使用中的基础货币 |
| Exchange Currency（兑换货币） | X(03) - 必填字段 - 要兑换的外币 |
| Effective Date（生效日期） | 99/99/9999 - 必填字段 - 此汇率的生效日期 |
| Exchange Rate（汇率） | 9(05).9(05) - 必填字段 - 外币汇率 |
| Reverse Exchange Rate（反向汇率） | 9(05).9(05) - 必填字段或自动计算 - 反向汇率，值应等于 1 / 汇率 |
| Remarks（备注） | X(30) - 可选字段 - 此汇率的备注 |

> 来源: v7 Book-1 Section 4.11 Page 57-58

> 相关图片: v7_Book-1_TABLES_p057_img00.jpeg

---

### 如何维护原因表（Reason Table）？各字段有什么要求？

原因代码表需要为某些 POS 操作定义，这些操作在处理时需要选择原因代码，如库存调拨、销售退货、服务单等。

**字段说明：**

| 提示 | 说明 |
|------|------|
| Reason Code（原因代码） | X(02) - 必填字段 - 用于识别特定原因的唯一代码 |
| Description（描述） | X(40) - 必填字段 - 原因的文字描述 |

**功能设置：**
- 这些是允许使用原因代码的 POS 功能类型
- 一旦定义，相关的原代码将在操作时显示在 POS 中供用户选择
- 所有原因代码将保存在日志记录中，需要时用户可以检索以进行进一步分析

**操作说明：**
1. 创建不同的原因代码（如调拨原因、退货原因等）
2. 为每个代码添加描述
3. 将原因代码与相应的 POS 功能关联
4. 在 POS 操作时，系统会提示用户从已定义的原因中选择

> 来源: v7 Book-1 Section 4.12 Page 59-60

> 相关图片: v7_Book-1_TABLES_p059_img00.jpeg, v7_Book-1_TABLES_p059_img01.jpeg, v7_Book-1_TABLES_p060_img00.jpeg

---

## 主数据管理 (11 条)

### 如何创建和管理会员类型？

会员类型维护（Member Type Maintenance）用于创建会员类型，将会员分组到有意义的会员组中，便于组织相关数据以生成有意义的报表。\n\n**前置条件：**\n这是创建会员类型以将会员分组的表。\n\n**操作步骤：**\n1. 进入会员类型维护功能\n2. 输入会员类型代码和相关参数\n3. 使用"Other（其他）“按钮定义额外的折扣控制\n4. 验证并保存记录\n\n**功能按钮：**\n1. 创建记录（Create Record）\n2. 清除记录（Clear Record）\n3. 验证记录（Validate Record）\n\n**字段说明：**\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Member Type（会员类型） | X(01) | 必填 | 会员类型代码 |\n| Description（描述） | X(40) | 可选 | 该会员类型的文本描述 |\n| Discount %（折扣百分比） | 9(02).9(02) | 可选 | 该会员类型有权享有的销售折扣百分比 |\n| Extra %（额外折扣百分比） | 9(02).9(02) | 可选 | 特殊促销活动时有权享有的额外销售折扣百分比 |\n| Max Disc. Bar %（最大折扣百分比） | 9(02).9(02) | 可选 | 所有促销活动下允许的最大折扣百分比 |\n| Turn-over Control（营业额控制） | X(01) | 必填 | 控制是否允许营业额限制加上按金额或按数量的控制 |\n| Turn-over Limit（营业额限额） | 9(06).(02) | 可选 | 如果启用限额控制，该会员类型允许的最大累计销售金额。通常适用于员工购买环境 |\n| Control Period（控制周期） | X(01) | 可选 | 控制限额是基于一次性购买、月度还是季度基准 |\n| Sales Control（销售控制） | X(01) | 必填 | 表示营业额限制应基于总销售额（Gross Sales）还是净销售额（Net Sales） |\n| Staff Control（员工控制） | X(01) | 必填 | 表示这是非员工（non-staff）还是员工（staff）会员类型 |\n\n**跨区域客户设置：**\n此设置用于会员类型被分类为跨区域客户。意味着在该类型下指定的会员折扣将适用于在组织内的海外会员在POS销售中消费的情况。\n\n**"Other"（其他）按钮 - 额外折扣控制：**\n输入屏幕中的此按钮允许用户为此客户类型定义额外的折扣控制，指定应用的位置和方式。\n\n可配置以下维度的折扣控制：\n- 地点（Location）：指定哪些特定地点应应用此折扣\n- 部门（Division）：指定哪些特定部门应应用此折扣\n- 品牌（Brand）：指定哪些特定品牌应应用此折扣\n- 产品类别（Product Category）：指定哪些特定产品类别应应用此折扣\n\n针对以上每个维度，可设置：\n- 特定的折扣百分比（Discount %）\n- 额外的折扣百分比（Extra Discount %）

> 来源: v7 Book-2 Section 5.4.1 Pages 33-35

> 相关图片: v6.5_Book-2_MASTERS_p034_img00.png, v6.5_Book-2_MASTERS_p035_img00.jpeg

---

### 如何在POS系统中进行在线信用检查以及设置会员升级规则？

在线信用检查（Online Credit Check）功能和会员升级规则（Upgrade Rules）用于控制员工/会员的总购买限额以及会员类型的自动升级。\n\n**一、在线信用检查（Online Credit Check on Staff / Member's Total Purchase）**\n\n如果特定客户类型（如员工购买）启用了购买限额，POS系统将通过互联网连接在后台执行在线信用检查，以避免超限购买。如果发现会员（通常是员工购买）在控制周期内超出购买限额，POS前端系统将拒绝该笔销售交易。\n\n**二、会员升级规则（Upgrade Rules for Member Customer）**\n\n这是适用于所有客户从一种客户类型升级到另一种客户类型的通用升级规则，当满足以下定义的条件时触发。此会员升级流程将由后台按用户设定的计划以批处理作业方式执行。\n\n**POS提示提醒控制设置（POS Prompt Alert Controls）：**\n| 功能 | 说明 |\n|------|------|\n| Alert Prompt（提醒提示） | 勾选此选项并填写有效期限（天数）后，POS前端系统将在有效期内自动显示右侧的文本消息，作为POS用户的提醒 |\n| Effected Period（有效期限） | 以天数表示的有效期 |\n\n示例说明：\n当属于客户类型"F"的会员客户在自该客户首次购买日期起计算的180天内在店铺进行购买时，将导致POS系统在销售操作期间自动弹出右侧的文本消息，作为对POS用户的提醒。\n\n**会员类型升级控制设置（Member Type Upgrade Controls）：**\n| 功能 | 说明 |\n|------|------|\n| 升级目标类型 | 如果自首次购买日期以来赚取的奖励积分总额超过输入的数值，该客户类型内的所有会员将升级到指定的新会员类型 |\n\n示例说明：\n如果自首次购买日期以来赚取的奖励积分总额超过"5,000"分，客户类型"F"内的所有会员将升级到会员类型"E"。\n\n**重要说明：**\n截至版本6.4.3，尚无会员降级机制。

> 来源: v7 Book-2 Section 5.4.2 Pages 36-37

> 相关图片: v6.5_Book-2_MASTERS_p036_img00.jpeg, v6.5_Book-2_MASTERS_p037_img00.png

---

### 如何创建和维护会员主档？

会员主档维护（Member Master Maintenance）用于存储会员详细信息，该主档允许用户基于会员的销售历史、行为和兴趣进行客户分析。\n\n**目标：** 维护常客或潜在会员的个人信息。\n\n**操作步骤：**\n1. 进入会员主档维护功能\n2. 填写会员详细信息（共3页）\n3. 验证并保存记录\n\n**功能按钮：**\n1. 创建记录（Create Record）\n2. 清除记录（Clear Record）\n3. 验证记录（Validate Record）\n\n**第1页 - 基本会员信息：**\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Member No.（会员编号） | X(15) | 必填 | 表示会员编号的唯一编号 |\n| Type（会员类型） | X(01) | 必填 | 在”会员管理信息（Membership Management Information）“中预定义的会员类型代码 |\n| Lastname（姓氏） | X(30) | 必填 | 会员的姓氏 |\n| Firstname（名字） | X(30) | 必填 | 会员的名字 |\n| Address（地址） | X(90) x 4行 | 可选 | 加入会员的客户地址，最多4行 |\n| Area Code（地区代码） | X(02) | 可选 | 用户自定义的地区代码，仅供参考 |\n| Postal Code（邮政编码） | X(202) | 可选 | 用户自定义的邮政编码，仅供参考 |\n| Home No.（住宅电话） | X(15) | 可选 | 客户的住宅电话号码 |\n| Mobile No.（手机号码） | X(15) | 可选 | 客户的手机号码 |\n| Issue Date（发卡日期） | 99 99 9999 (dd mm yyyy) | 必填 | 会员资格的颁发日期 |\n| Issue Shop（发卡店铺） | X(04) | 必填 | 颁发此会员资格的店铺 |\n| Pickup Shop（领取店铺） | X(04) | 必填 | 会员从哪家店铺领取会员卡 |\n| Expiry Date（到期日期） | 99 99 9999 (dd mm yyyy) | 必填 | 会员资格的到期日期 |\n\n**第2页 - 个人详细信息：**\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Date of Birth（出生日期） | 99 99 9999 (dd mm yyyy) | 可选 | 加入会员的客户出生日期 |\n| Age（年龄） | 9(02) | 仅显示 | 如果提供了出生日期，系统自动计算 |\n| Age Group（年龄组） | - | 可选 | 系统选择正确的年龄组或用户自行输入 |\n| Card I.D.（身份证号码） | X(15) | 可选 | 客户的身份证号码 |\n| Nationality（国籍） | X(02) | 可选 | 加入会员的客户国籍，需对国家代码表进行检查 |\n| Sex（性别） | - | 可选 | 会员的性别 |\n\n**第3页 - 自定义备注信息：**\n此页面为自由文本输入格式（Free TEXT input format），供用户自行参考使用，没有固定的字段定义，用户可根据需要输入任意备注信息。

> 来源: v7 Book-2 Section 5.4.3 Pages 38-42

> 相关图片: v6.5_Book-2_MASTERS_p039_img00.png, v6.5_Book-2_MASTERS_p040_img00.png, v6.5_Book-2_MASTERS_p041_img00.jpeg, v6.5_Book-2_MASTERS_p042_img00.jpeg

---

### 如何创建和维护新的供应商主档？

供应商主档维护（Supplier Master Maintenance）用于输入和管理供应商的详细信息，以便进行采购处理。\n\n**操作步骤：**\n1. 进入供应商主档维护功能\n2. 系统默认显示摘要页面（Summary Page），可按”供应商代码（Supplier Code）“或”供应商名称（Supplier Name）“排序\n3. 双击某一行进入详细修改页面（Detail Modification Page）\n4. 在详细页面中包含5个标签页，填写所有必填字段后保存\n\n**功能按钮：**\n- 创建记录（Create Record）\n- 修改记录（Modify Record）\n- 删除记录（Delete Record）\n- 查看记录（View Record）\n- 复制为新记录（Copy Record as new）\n- 查找记录（Find Record）\n- 按标题排序（Sort by header）\n- 调整列指示（Adjust column indication）\n\n**标签页1 - 基本信息（Folder Page 1）：**\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Supplier Code（供应商代码） | X(8) | 必填 | 唯一标识特定供应商 |\n| Supplier Name（供应商英文名称） | X(150) | 必填 | 供应商的英文名称 |\n| Chinese Name（供应商中文名称） | X(150) | 可选 | 供应商的中文名称 |\n| Attn.（收件人） | X(20) | 可选 | 供应商的联系人 |\n| Address Line（地址行） | X(30) x 4行 | 可选 | 供应商的送货地址 |\n| City（城市） | X(20) | 可选 | 送货地址所在城市 |\n| Country（国家） | X(12) | 可选 | 送货地址所在国家 |\n| Postal（邮政编码） | X(08) | 可选 | 送货地址的邮政编码 |\n| State（州/省） | X(04) | 可选 | 送货地址的州/省 |\n| Country Code（国家代码） | X(02) | 可选 | 送货地址国家代码，需在”国家代码维护（Country Code Maintenance）“中预定义 |\n| District Code（地区代码） | X(03) | 可选 | 送货地址的地区代码，需在”地区表维护（District Table Maintenance）“中预定义 |\n\n**标签页2 - 联系信息（Folder Page 2）：**\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Country（国家码） | X(10) x 3组 | 可选 | 国家代码（可输入3组） |\n| Area（区号） | X(8) x 3组 | 可选 | 地区区号（可输入3组） |\n| Tel No.（电话号码） | X(30) x 3组 | 可选 | 电话号码（可输入3组） |\n| Extension（分机号） | X(15) x 3组 | 可选 | 分机号码（可输入3组） |\n| Telex No.（电传号） | X(25) | 必填 | 电传打字机号码 |\n| Title（职位头衔） | X(80) | 可选 | 联系人的职位头衔 |\n| First Name（联系人名字） | X(30) | 可选 | 联系人的名 |\n| Last Name（联系人姓氏） | X(30) | 可选 | 联系人的姓 |\n\n**标签页3 - 信用与折扣信息（Folder Page 3）：**\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Credit Term（信用期限） | 数字 | 可选 | 信用天数 |\n| Credit Limit（信用额度） | 金额 | 可选 | 供应商允许的最大总信用金额 |\n| Payment Method（付款方式） | - | 可选 | 付款方式的输入 |\n| Owner ID（负责人ID） | - | 必填 | 负责该供应商的用户ID |\n| Company Currency（公司货币） | - | 必填 | 该供应商采购订单使用的默认货币，可在采购订单维护过程中按需覆盖 |\n| Discount（折扣） | - | 可选 | 供应商提供的一般折扣，最多可设置5个折扣率，按”折扣叠加”机制在采购订单处理中计算，折扣基于商品的零售价目表价格（Retail List Price）计算 |\n| Discount Rate（折扣率处理方式） | X(01) | 可选 | H - 在采购订单的标题级别（Header Level）默认折扣率；I - 在采购订单的商品项目级别（Item Level）默认折扣率；或折扣率仅供参考 - 不进行计算 |\n\n**标签页4 - 电子联系信息（Folder Page 4）：**\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Email Address（电子邮件地址） | X(40) | 可选 | 联系人的电子邮件地址 |\n| Web Site（网站） | X(4) | 可选 | 在线网站地址 |\n\n说明：此区域可自由用于自行开发的报表或工具进行分析。\n\n**标签页5 - 银行与业务信息（Folder Page 5）：**\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Bank Code（银行代码） | X(20) | 可选 | 结算银行代码 |\n| Bank Name（银行名称） | X(30) | 可选 | 结算银行名称 |\n| A/C No.（银行账号） | X(10) | 可选 | 银行账户号码 |\n| CRM ID（客户关系管理ID） | X(20) | 可选 | 客户关系管理系统中的身份编号 |\n| BR（商业登记号） | X(20) | 可选 | 商业登记号码 |\n| Salutation（称谓） | X(30) | 可选 | 称呼 |

> 来源: v7 Book-2 Section 5.1.1 Pages 4-10

> 相关图片: v6.5_Book-2_MASTERS_p004_img00.jpeg, v6.5_Book-2_MASTERS_p005_img00.png, v6.5_Book-2_MASTERS_p006_img00.png, v6.5_Book-2_MASTERS_p007_img00.jpeg, v6.5_Book-2_MASTERS_p008_img00.png, v6.5_Book-2_MASTERS_p009_img00.png

---

### 如何管理供应商的送货地址？

供应商送货地址维护（Supplier Delivery Address Maintenance）用于输入和管理特定供应商的送货地址信息。\n\n**操作步骤：**\n1. 进入供应商送货地址维护功能\n2. 选择或输入供应商代码\n3. 输入送货地址代码和相关地址信息\n4. 保存记录\n\n**功能按钮：**\n1. 创建记录（Create Record）\n2. 修改记录（Modify Record）\n3. 删除记录（Delete Record）\n4. 查看记录（View Record）\n5. 复制为新记录（Copy Record as new）\n6. 查找记录（Find Record）\n7. 按标题排序（Sort by header）\n8. 调整列指示（Adjust column indication）\n\n**字段说明：**\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Supplier Code（供应商代码） | X(8) | 必填 | 特定供应商的代码 |\n| Del. Addr. Code（送货地址代码） | X(3) | 必填 | 唯一标识特定供应商的特定送货地址的代码 |\n| Attn.（收件人） | X(20) | 可选 | 该供应商的联系人/收件人 |\n| Delivery Address（送货地址） | X(30) x 4行 | 可选 | 供应商的送货地址，最多4行 |\n| City（城市） | X(20) | 可选 | 送货地址所在城市 |\n| City Code（城市代码） | X(4) | 可选 | 送货地址的城市代码 |\n| Country（国家） | X(12) | 可选 | 送货地址所在国家 |\n| Postal（邮政编码） | X(08) | 可选 | 送货地址的邮政编码 |\n| State（州/省） | X(04) | 可选 | 送货地址的州或省份 |\n| Country Code（国家代码） | X(02) | 可选 | 送货地址的国家代码，需在”国家代码维护（Country Code Maintenance）“中预定义 |\n| District Code（地区代码） | X(03) | 必填 | 送货地址的地区代码，需在”地区表维护（District Table Maintenance）“中预定义 |

> 来源: v7 Book-2 Section 5.1.2 Pages 11-12

> 相关图片: v6.5_Book-2_MASTERS_p011_img00.jpeg

---

### 如何使用型号（Model Number）查询商品信息？

型号查询功能（Model Number）允许用户通过商品型号搜索键来查询或修改商品信息，查看特定库存的可用性。\n\n**功能说明：**\n通过商品搜索键，按型号（Model No.）进行查询。\n\n**目标：**\n对商品信息进行查询或修改，用户可以检查特定库存的可用性。\n\n**字段说明：**\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Item Code（商品代码） | X(14) | 必填 | 唯一标识特定商品的代码 |\n| Description（描述） | X(40) | 必填 | 详细的商品描述 |\n| Model Number（型号） | X(30) | 必填 | 商品的型号 |\n\n**附加功能 - 按保修编号（Guarantee No.）查询：**\n通过商品搜索键，按保修编号（Guarantee No.）进行查询，用户可以检查特定库存的保修编号。

> 来源: v7 Book-2 Section 5.3.1 Page 32

> 相关图片: v6.5_Book-2_MASTERS_p032_img00.png

---

### 如何创建新的商品主档（基本信息录入）？

商品主档维护（Item Master Maintenance）是系统中最重要、最核心的主档表。它将链接许多重要的基础表，并由ChainStore Plus的许多流程或子系统共享。正确设置商品主档数据非常重要。\n\n**操作步骤：**\n1. 进入商品主档维护功能\n2. 在”主要输入（Primary Input）“文件夹中填写所有必填字段\n3. 第一文件夹（Primary Input）中的所有信息均为强制字段\n4. 其他文件夹为次要输入，但仍包含重要的数据信息\n\n**目标：** 维护商品的详细信息。\n\n**主要输入文件夹字段说明：**\n\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Item Code（商品代码） | X(14) | 必填 | 唯一标识特定商品的代码 |\n| Category Code（类别代码） | X(05) | 必填 | 在类别主档（Category Master）中预定义的代码 |\n| Sub. Category（子类别代码） | X(05) | 必填 | 在类别主档中预定义的代码，属于上述类别代码的子类别 |\n| Supplier Item Code（供应商商品代码） | X(10) | 必填 | 供应商定义的同一商品的代码 |\n| Long Description（长描述） | X(40) x 2行 | 第一行必填，第二行可选 | 详细的商品描述 |\n| Short Description（短描述） | X(20) x 2行 | 可选 | 简短的商品描述 |\n\n**多语言按钮（Multi-Language Button）：**\n用于输入其他语言的描述作为补充数据。某些可选文件（如销售单）可根据用户要求以中文打印。\n\n**尺码控制（Dimension Control）：**\n下拉选择框 - 必填字段。必须至少选择以下选项之一：\n- A - 无颜色和尺码（No Col & Size）\n- B - 有颜色和尺码（Col & Size）\n- C - 仅颜色（Color Only）\n- D - 内缝（Inseam，特定用途可选）\n\n**尺码类别（Size Category）：**\n- 格式：X(04)\n- 当尺码控制为B时必填，其他情况无需输入\n- 需要预定义尺码表（Size table）\n- "更多尺码（More Size）“按钮：允许一个商品设置多个尺码类别\n\n**库存指示符（Stock Indicator）：**\n必须至少选择以下选项之一：\n\n| 选项 | 代码 | 说明 |\n|------|------|------|\n| Buy Off Stock（买断库存） | B | 用户自有库存。最常用的指示符 |\n| Consignment Stock（寄售库存） | C | 表示该库存商品不属于用户所有。未来可能根据所购可选模块应用计算处理 |\n| Package Set（套装包） | G | 表示该商品为套装商品，链接到特定流程下预定义的商品表集。ChainStorePlus后台系统将POS前端销售的套装商品根据商品表集分解为详细商品明细，然后以分解明细写入销售日志。使用前请咨询Sanyo Extended业务顾问 |\n| Special Handle Item（特殊处理商品） | N | 特殊控制标志，用于某些定制特殊流程。不适用于一般用途。使用前请咨询Sanyo Extended业务顾问 |\n| Coupon M & M Item（优惠券搭配商品） | S | 专为POS处理中的促销搭配计算创建的商品。必须与搭配促销模块中的搭配优惠券规则配合使用 |\n| Service Item（服务商品） | V | 表示该商品可在POS中”销售”但不可计入库存，因此在正常库存控制流程下无库存变动。典型示例包括”修补"、"改衣服务”等 |\n\n**尺码/内缝类别（Size/Inseam Cat.）：**\n- 格式：X(04)，可选\n- 仅当尺码控制为B或D时可选\n- 需在尺码类别信息（Size Category Information）中预定义\n\n**定义颜色代码（Define Color Code）：**\n- 格式：X(04)\n- 当尺码控制设置为非"A"时必填\n- 需要预定义颜色表\n- 系统将在大多数流程中检查此颜色控制，如果颜色未在此控制表中预先定义，将拒绝颜色输入\n\n**零售价（Retail Price）：**\n- 格式：9(07).99，可选\n- 商品的零售价目表价格\n- 用于条码标签或价格标签打印\n- 仅在创建模式下可输入。商品一旦创建不允许修改零售价目表价格\n- 价格修改只能通过系统中的”加价/减价（Mark up Mark down）“流程进行\n\n**批发价（Wholesale Price）：**\n- 格式：9(07).99，可选\n- 商品的批发价格\n- 可用于批发与分销模块（ChainStore Plus的附加选项）中的客户发票处理

> 来源: v7 Book-2 Section 5.2 Pages 13-16

> 相关图片: v6.5_Book-2_MASTERS_p015_img00.png, v6.5_Book-2_MASTERS_p016_img00.png

---

### 如何设置商品的价格与成本信息？

价格与成本标签页（Price & Cost Tab）用于设置商品的重要价格和成本信息。\n\n**操作步骤：**\n1. 进入商品主档维护，选择需要设置的商品的\n2. 点击"Price & Cost（价格与成本）“标签页\n3. 填写各项价格和成本字段\n4. 使用相关按钮进入更详细的设置\n\n**字段说明：**\n\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Retail Price（零售价） | 9(07).99 | 可选 | 商品的零售价目表价格，用于条码标签或价格标签打印；仅在创建模式可输入，创建后不允许修改，只能通过”加价/减价”流程修改 |\n| Wholesales Price（批发价） | 9(07).99 | 可选 | 商品的批发价格，用于分销模块中的客户发票处理（ChainStore Plus的附加选项） |\n| Price Group（价格组） | X(03) | 可选 | 表示该商品所属价格组的代码 |\n| Discount Ctrl.（折扣控制） | X(01) | 必填 | 默认值为'NO'：允许在POS销售中打折；'NO'时启用最大折扣输入（Max Discount）；'YES'表示该商品不允许打折 |\n| Max Discount（最大折扣） | 99.99 | 可选 | 该商品允许的最大折扣，以零售价的百分比表示 |\n| Standard Cost（标准成本） | 9(07).99 | 可选 | 商品的标准成本，除非用户覆盖，否则不会更改 |\n| FOB Cost（FOB成本） | 9(07).99 | 可选 | 商品的FOB成本，除非用户覆盖，否则不会更改。右侧空白处可输入FOB成本的货币代码 |\n| Average Cost（平均成本） | 9(07).99 | 仅显示 | 系统在采购收货操作后自动更新计算的加权平均成本，计算公式为：(现有库存数量 × 平均成本 + 收货数量 × 收货成本) ÷ (现有库存数量 + 收货数量) |\n\n**按钮功能说明：**\n\n**"Retail"（零售）按钮：**\n点击此按钮将进入另一个输入框，用于多地点价格输入，例如不同国家、组别、地点甚至颜色和尺码的不同零售价。\n\n**"Consign"（寄售）按钮：**\n点击此按钮将进入寄售库存成本计算表（Consignment Stock Cost Calculation Table），用于寄售库存结算流程。该表仅用于供应商的寄售库存成本结算计算。如果不使用库存寄售可选模块，请忽略此表。\n\n寄售成本表的字段包括：\n- Effect Date（生效日期）：该寄售成本的生效日期\n- Consignment Settlement Cost Fixed Amount（寄售结算成本固定金额）：以固定金额表示的寄售结算成本\n- Consignment Settlement Cost Percentage（寄售结算成本百分比）：相对于零售价目表价格（Retail List Price）或零售销售价格（Retail Sold Price）的百分比。这两个字段只需输入其中一个\n- Effective Shop Location（生效店铺位置）：该寄售成本生效的店铺位置，留空表示所有位置\n\n**"Wholesales"（批发）按钮：**\n点击此按钮将进入另一个输入框，可输入最多10个不同的批发价，每个商品允许设置多个批发价。\n\n**"MORE"（更多成本）按钮：**\n点击此按钮可查看系统在不同操作阶段自动记录的不同商品成本表，用户可利用这些不同成本进行成本计算、分析和控制的报表制作。\n\n| 成本类型 | 说明 |\n|---------|------|\n| Month End Actual Cost（月末实际成本） | 月末处理后的确认商品加权平均成本。系统在月末流程中重新计算，包含自上次月末以来该商品产生的所有成本 |\n| Last Receive Average Cost（上次收货平均成本） | 收货时计算的平均成本（非加权平均成本）。包含计算时系统已知的所有其他成本，如F&I（运费和保险费） |\n| Last Receive Unit Cost（上次收货单位成本） | 上次收货时标记的单位成本。不包含任何费用或附加成本 |\n| FOB Average Cost（FOB平均成本） | 收货时计算的加权平均FOB成本。仅包含商品的FOB成本，不包含任何其他成本 |\n| Average Cost（平均成本） | 收货时计算的加权平均成本。包含计算时系统已知的所有其他成本，如F&I |\n| Last PO Unit Cost（上次采购订单单位成本） | 上次采购订单标记的单位成本。不包含任何费用或附加成本 |

> 来源: v7 Book-2 Section 5.2.1 Pages 17-22

> 相关图片: v6.5_Book-2_MASTERS_p018_img00.png, v6.5_Book-2_MASTERS_p019_img00.jpeg, v6.5_Book-2_MASTERS_p020_img00.png, v6.5_Book-2_MASTERS_p021_img00.jpeg

---

### 如何设置商品的库存信息？

库存文件夹（Inventory Folder）用于设置商品的库存相关信息。\n\n**操作步骤：**\n1. 进入商品主档维护，选择需要设置的商品\n2. 点击"Inventory（库存）“标签页\n3. 填写各项库存相关字段\n4. 点击"More Supplier"按钮可添加多个供应商\n\n**字段说明：**\n\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Main W/H（主仓库） | X(04) | 可选 | 该商品的默认仓库代码 |\n| W/H Lot Remarks（仓库批次备注） | X(10) | 可选 | 参考字段，指示该商品存放在仓库的哪个批次或区域 |\n| Reorder Level（再订购水平） | 9(07).99 | 可选 | 包含2个子字段：min（最低库存持有量）和std（标准库存持有量）。目前无实际流程应用 |\n| Inventory Group（库存组别） | - | 可选 | 用于分类商品的库存组别。目前无实际流程应用 |\n| Unit Of Measure（计量单位） | X(04) | 必填 | 表示商品计量单位的代码，如SET（套）、PCE（件）等 |\n| Supplier（供应商） | X(08) | 必填 | 供应商代码，将针对供应商主档文件（Supplier Master File）进行验证 |\n| Supplier Item Code（供应商商品代码） | X(15) | 可选 | 供应商使用的商品/产品编号，仅供参考 |\n| Producer Code（生产商代码） | X(03) | 可选 | 生产商代码，仅供参考 |\n\n**按钮功能说明：**\n\n**"Reorder"（再订购）按钮：**\n用于输入颜色和尺码的再订购水平。目前无实际流程应用。\n\n**"More Supplier"（更多供应商）按钮：**\n每个商品允许设置多个供应商。点击此按钮可添加更多供应商信息。

> 来源: v7 Book-2 Section 5.2.2 Pages 23-24

> 相关图片: v6.5_Book-2_MASTERS_p023_img00.png

---

### 如何设置商品的属性信息（属性I）？

商品属性I标签页（Item Attribute I Tab）用于设置商品的各种属性信息，包括品牌、税收、条形码等相关信息。\n\n**操作步骤：**\n1. 进入商品主档维护，选择需要设置的商品\n2. 点击"Item Attribute I（商品属性I）“标签页\n3. 依次填写各项属性字段\n\n**字段说明：**\n\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Tax Code（税码） | - | 可选 | 商品的增值税百分比/增值税金额的税码。此字段关联税率表 |\n| Special Promotion Flag（特别促销标志） | - | 可选 | 控制标志，表示该商品正在进行特别促销。目前无实际流程，仅供参考 |\n| Model Replenishment（按型号补货） | - | 可选 | 控制标志，表示该商品的补货按型号（Model No.）而非按标准商品编号（Item No.）进行 |\n| Owner ID（负责人ID） | X(05) | 必填 | 将针对负责人ID表（Owner ID table）进行验证。这是管理和处理该商品的预先定义的买手/ Merchandiser 代码 |\n| Brand（品牌） | X(06) | 必填 | 将针对品牌表（Brand table）进行验证 |\n| Country（来源国家） | X(02) | 可选 | 将针对国家表（Country table）进行验证。表示商品来源国的国家代码，如有输入需存在于国家代码主档文件中 |\n| Material Code（材料代码） | X(03) | 可选 | 将针对材料代码表（Material Code table）进行验证 |\n| Replenishment（允许补货） | - | 可选 | 勾选表示允许该商品从仓库补货到店铺 |\n| Discontinue Item（停产商品） | - | 可选 | 勾选表示该商品已停产。表示不再采购但仍继续销售。此标记允许系统处理该商品的销售，但停止采购，无需删除该商品记录 |\n| Lock/Release Item（锁定/解锁商品） | - | 可选 | 勾选表示该商品被锁定。此商品将停止所有交易。用户可选择”空白”来解锁此商品 |\n| EAN/UPC Code（EAN/UPC代码） | - | 可选 | 如果商品关联有条码值，在此输入UPC/EAN条形码值 |\n| Bar Code Sequence（条码序列号） | X(07) | 仅显示 | 系统生成的条码序列号。除非另有指定，系统默认使用此条码序列在POS前端系统中表示该商品 |\n| Reference（参考编号） | X(06) | 可选 | 用户自行参考的代码 |\n| Gift（礼品标志） | - | 可选 | 勾选表示该商品可作为礼品赠送，允许零售价和成本为零 |\n| Analysis Code Description（分析代码描述） | X(03) x 10个 | 仅显示 | 描述商品定位的简短代码。根据其在分析代码表维护（Analysis Code Table Maintenance）中定义的位置显示 |\n| Analysis Code（分析代码） | X(03) x 10个 | 可选 | 将针对分析代码表进行验证。用户可为每个字段激活自己的代码，用于将来生成分析报告 |\n| External Season（外部季节码） | X(04) | 可选 | 用于在商品代码结构”外部”需要季节代码的用户，仅供参考 |

> 来源: v7 Book-2 Section 5.2.3 Pages 25-27

> 相关图片: v6.5_Book-2_MASTERS_p026_img00.png, v6.5_Book-2_MASTERS_p027_img00.png

---

### 如何设置商品的附加属性信息（属性II）？

商品属性II标签页（Item Attribute II Tab）用于设置商品更多的附加属性信息，包括品牌名称、年份、型号、季节、图片、出版信息以及特殊日期等。\n\n**操作步骤：**\n1. 进入商品主档维护，选择需要设置的商品\n2. 点击"Item Attribute II（商品属性II）“标签页\n3. 填写各项属性字段\n4. 查看商品图片和重要日期信息\n\n**常规属性字段说明：**\n\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Brand（品牌名称） | X(30) | 可选 | 商品有品牌名称时使用 |\n| Year（年份） | X(04) | 可选 | 产品的年份 |\n| Category（类别） | X(12) | 可选 | 商品的类别代码 |\n| Model Number（型号） | X(20) | 可选 | 商品的型号 |\n| Article（货号） | X(30) | 可选 | 商品的货号 |\n| Variante（变体） | X(?) | 可选 | 商品的变体信息 |\n| Sex（性别） | X(04) | 可选 | 商品的性别信息 |\n| Season（季节） | X(02) | 可选 | 季节信息，需在”季节代码（Season Code）“中预定义 |\n| Collection（系列） | X(30) | 可选 | 商品的系列/集合 |\n| Sub Category（子类别） | X(12) | 可选 | 商品的子类别代码 |\n| Label（标签） | X(20) | 可选 | 商品的标签 |\n| Product（产品） | X(20) | 可选 | 商品的产品信息 |\n\n**图片（Image）按钮：**\n- 此按钮将显示该商品的图片\n- 图片需要存储在先前定义的专用图片文件夹中\n- 图片文件名必须遵循以下格式：<文件名> = 商品编号_999，其中'999'是图片的序列号\n  - 例如：A9008765433_001, A9008765433_002, A9008765433_003 等\n- 系统将自动收集该商品的所有图片，并在标准的Windows图片浏览器中一次性显示\n\n**出版信息字段（Publication Section，适用于书籍/出版物类商品）：**\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Magazine Code（期刊代码） | X(20) | 可选 | 出版物的ID编号 |\n| Edition No.（版次） | X(20) | 可选 | 出版物的版次 |\n| Language Version（语言版本） | X(20) | 可选 | 出版物特定语言版本的版本号 |\n| Publisher（出版社） | X(40) | 可选 | 出版社名称 |\n| Author（作者） | X(40) | 可选 | 作者名称 |\n\n**特殊与日期标签页（Special & Date Tab）字段说明：**\n\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Model Number（型号） | X(30) | 可选 | 商品关联的型号。商品查询功能中有针对此型号的特殊搜索键。非常适合手表和珠宝零售商或有类似产品性质的用户 |\n| Warranty Number（保修编号） | X(30) | 可选 | 商品关联的唯一序列号。商品查询功能中有针对此序列号搜索的特殊搜索键。非常适合手表和珠宝零售商或有类似产品性质的用户 |\n| Body Number（机身号） | X(20) | 可选 | 来自制造商的信息编号 |\n| Style Number（款号） | X(12) | 可选 | 用户自行参考的代码 |\n| Volume / Content / Container（卷/内容/容器） | - | 可选 | 用户自行参考的代码 |\n| Expiration Date（有效期） | dd/mm/yyyy | 可选 | 表示商品的有效期（如有），仅供参考 |\n\n**重要日期（仅显示，不可编辑）：**\n| 字段名称 | 格式 | 说明 |\n|---------|------|------|\n| Creation Date（创建日期） | dd/mm/yyyy | 该商品主档记录创建时的日期 |\n| First Receipt Date（首次收货日期） | dd/mm/yyyy | 该商品主档记录首次收货的日期 |\n| Last Receipt Date（最后收货日期） | dd/mm/yyyy | 该商品主档记录最近一次收货的日期 |\n| First Transfer Date（首次调拨日期） | dd/mm/yyyy | 该商品主档记录首次调拨的日期（通常首次调拨是从仓库到店铺） |\n| Last Sales Date（最后销售日期） | dd/mm/yyyy | 该商品主档记录最后一次销售的日期 |\n| New Season 1st Delivery Date（新季节首次交货日期） | dd/mm/yyyy | 该商品标记为季节首次交货的日期，仅适用于特殊季节产品 |\n| Last Modified Date（最后修改日期） | dd/mm/yyyy | 该商品主档记录最后被修改并记录用户ID的日期 |

> 来源: v7 Book-2 Section 5.2.4 Pages 28-31

> 相关图片: v6.5_Book-2_MASTERS_p028_img00.png, v6.5_Book-2_MASTERS_p030_img00.png

---

## 采购流程 (3 条)

### 如何创建采购订单（Purchase Order）？

创建采购订单的操作步骤如下：

1. **进入采购订单维护画面**
   - 从菜单中点击进入 Purchase Order Maintenance 功能。
   - 点击 CREATE 按钮创建新的采购订单。

2. **输入订单头信息（Header Input）**
   - 进入 Purchase Order Detail Maintenance Screen。
   - 选择订单类型：
     - Normal PO（普通采购订单）：正常模式，允许分批收货。
     - Blanket PO（blanket 采购订单）：批量订单模式，供应商可在一段时间（如一年或一个季节）内分批次交货。Blanket PO 需要后续的「交货请求（Delivery Request）」来完成交货。
   - 勾选折扣复选框可启用行项目折扣输入字段。
   - 部分字段由系统自动计算且不可手动输入。

3. **输入采购订单条款（PO Terms Input）**
   - 点击第二个文件夹标签页（2nd folder）进入 PO 条款输入。
   - 关键字段：
     - Expected Shipment Date（预计发货日期）：部分 PO 报表以此字段作为排序依据。
     - 默认收货地点：用于 PO 收货流程的默认位置。
     - 分配地点：用于将到货库存分配到特定位置，仅在特定设计程序中生效。

4. **输入明细项目（Detail Items Input）**
   - 进入 Manage Item 页面。
   - 输入商品代码（Item Code）。
   - 如果商品有颜色和尺寸的细分，点击 Color & Size 按钮输入详细的数量。
   - 也可以直接在数量字段中输入采购数量。

5. **了解列字段含义**
   - List Price（列表价）：采购商品的标准价格。
   - Def Disc%（默认折扣率）：系统自动获取的默认折扣百分比，需预先在供应商主文件或供应商 PO 折扣表中设定。
   - Ovr Disc%（覆盖折扣率）：手动输入的覆盖折扣，当默认折扣不适用时使用；系统优先使用此折扣计算采购单价。
   - Unit Cost（单价）：系统计算的采购单价，或用户手动输入覆盖系统计算的数值；如果与默认 PO 成本不同，数值将显示为红色提示。
   - Qty（数量）：用户输入的采购数量。
   - Order Amount（订单金额）：系统基于单价乘以数量自动计算。
   - Unit（单位）：采购商品的计量单位。

6. **确认并保存**
   - 检查所有输入信息。
   - 点击保存按钮完成采购订单创建。

注意：采购订单流程支持从下单、收货、未完成订单跟踪、库存成本更新（通过收货流程）到报表的完整操作。

> 来源: v7 Book-3 Section 6.1 Pages 4-8

> 相关图片: v7_Book-3_PROCESS_p004_img00.jpeg, v7_Book-3_PROCESS_p005_img00.jpeg, v7_Book-3_PROCESS_p006_img00.jpeg, v7_Book-3_PROCESS_p007_img00.jpeg

---

### 如何使用 Load File 功能批量上传采购订单明细？

使用 Load File 功能批量上传采购订单明细的操作步骤如下：

1. **准备上传文件**
   - 文件必须是 Text file（Tab 分隔符格式，Tab delimited）。
   - 文件名没有限制。
   - 文件格式必须与 ChainStorePlus PO Load File 数据格式匹配。

2. **文件格式要求**
   | 序号 | 字段名称 | 长度 | 必填 | 说明 |
   |------|----------|------|------|------|
   | 1 | Item Code（商品代码） | X(14) | 是 | 必须在 ChainStorePlus 中已定义 |
   | 2 | Color（颜色） | X(5) | 否 | 必须在 ChainStorePlus 中已定义 |
   | 3 | Size（尺寸） | X(4) | 否 | 必须在 ChainStorePlus 中已定义 |
   | 4 | Inseam（内缝长） | X(4) | 否 | 必须在 ChainStorePlus 中已定义 |
   | 5 | Quantity（数量） | X(7) | 是 | 最大 9999999 |
   | 6 | Unit Cost（单价） | X(12) | 是 | 格式 999999999.99 |
   | 7 | Item Discount Rate（折扣率） | X(6) | 否 | 格式 999.99 |

3. **执行上传**
   - 在 Purchase Order Maintenance（PO3000）的 Manage Item 页面中。
   - 点击 Load Layout 按钮可查看上述文件格式。
   - 点击 Load 按钮。
   - 系统弹出 Load Detail 对话框，询问 PO Load 文件位置。
   - 选择准备好的 PO Load File。
   - 点击 Open 将文件上传至 PO Maintenance。

4. **验证与错误处理**
   - 上传时，程序会对上传文件的数据进行验证。
   - 如果发现错误，系统会停止加载并返回错误信息。
   - 用户需要点击 Print Queue 保存「Purchase Order Upload Error Report」以查看无效上传的原因。
   - 根据错误报告修改 Text 文件，然后重新上传。
   - 注意：PO Load File 不应包含表头行（header）。如果遇到此错误，请移除表头行后重试。

5. **上传成功**
   - 上传成功后，数据将被放入 Item Detail 列表中。
   - 用户可以编辑内容后保存 PO。

> 来源: v7 Book-3 Section 6.1 Pages 8-11

> 相关图片: v7_Book-3_PROCESS_p009_img00.jpeg, v7_Book-3_PROCESS_p010_img00.jpeg, v7_Book-3_PROCESS_p011_img00.jpeg, v7_Book-3_PROCESS_p011_img01.jpeg, v7_Book-3_PROCESS_p011_img02.jpeg

---

### 如何修改或删除已创建的采购订单？

修改或删除已创建的采购订单的操作步骤如下：

1. **进入采购订单维护画面**
   - 从菜单中点击进入 Purchase Order Maintenance（PO3000）功能。
   - 系统将显示采购订单列表。

2. **查找目标采购订单**
   - 浏览列表找到需要修改或删除的采购订单。
   - 点击选中该订单。

3. **修改采购订单**
   - 在现有订单上直接修改需要变更的字段。
   - 可修改的内容包括：
     - 订单头信息（Header）：订单类型、折扣设置等。
     - PO 条款（PO Terms）：预计发货日期、收货地点等。
     - 明细项目（Detail Items）：商品代码、颜色、尺寸、数量、单价、折扣率等。
   - 修改完成后点击保存。

4. **删除采购订单**
   - 选中需要删除的采购订单。
   - 点击删除按钮（Delete）。
   - 系统将要求确认删除操作。
   - 确认后订单将被删除。

注意：
- PO 明细中各字段的系统行为需注意：
  - Def Disc%（默认折扣率）需预先在 Supplier Master 或 Supplier PO Discount Table 中设定。
  - Ovr Disc%（覆盖折扣率）手动输入时将覆盖默认折扣。
  - Unit Cost（单价）若为红色字体，表示与默认成本不同，提醒用户注意。
- 修改操作应在订单尚未进入收货流程前进行，以避免数据不一致。

> 来源: v7 Book-3 Section 6.1 Pages 4-8

> 相关图片: v7_Book-3_PROCESS_p004_img00.jpeg

---

## 收货流程 (3 条)

### 如何根据采购订单（PO）进行库存收货？

根据采购订单进行库存收货的操作步骤如下：

1. **进入库存收货功能**
   - 从菜单进入 Stock Receive（库存收货）功能。

2. **输入或选择采购订单**
   - 在 Stock Receive Input Against PO/DRV 画面中：
   - 方式一：直接输入 PO 编号，点击 OK。
   - 方式二：留空点击 OK，进入完整的 PO 选择页面。

3. **选择采购订单（方式二：留空搜索）**
   - 系统显示所有未完成的 PO 列表供用户选择。
   - 可按不同排序路径查看 PO：
     - PO#（采购订单编号）
     - DRV#（交货请求编号）
     - Supplier（供应商）
     - Expected Delivery Date（预计交货日期）
     - Receiving Location（收货地点）
   - 鼠标点击高亮选择目标行，左侧会显示「V」标记表示选中。
   - 允许同时选择多个 PO。
   - 点击工具栏上的 Create 按钮，系统将根据所选 PO 的未完成数量自动创建收货批次，默认收货数量等于未完成数量。

4. **输入收货批次头信息**
   - 输入收货地点代码（Receiving Location）作为收货编号的前缀。
   - 收货编号（Receive Number）部分可由用户输入或系统自动生成（如设置为系统生成则字段被保护不可输入）。
   - 输入供应商的交货单号码（Supplier Delivery Note Number），此信息对后续的供应商发票核对非常重要。
   - 某些字段由系统自动生成，不可手动输入。
   - 完成所有输入字段后，点击 Item Information Folder 进入下一步。

5. **输入/确认商品明细（Item Information Folder）**
   - 收货批次支持三种收货状态：
     - Stock Receive under PO（根据 PO 收货）
     - Stock Receive without PO（无 PO 收货）
     - Stock Receive under Delivery Request from a Blanket Order（根据 Blanket 订单的交货请求收货）
   - 红色圆圈指示当前激活的收货状态。
   - 对于颜色和尺寸有要求的商品，点击 Color & Size 按钮输入颜色和尺寸明细。
   - 支持从外部来源导入 TEXT 数据（可选功能）。

6. **保存收货信息**
   - 所有输入完成后，点击 SAVE 按钮。
   - 系统将进入下一步的收货确认流程。

功能按钮说明：
- Insert：插入一个商品项目
- Delete：删除一个商品项目
- Select PO：查询选定供应商的所有未完成 PO 并进行选择，系统将自动带入订单及默认收货数量
- Verify：每次点击时系统验证输入数据，验证后在状态栏显示警告或错误信息
- PO Enquiry：查询采购订单详情
- Color & Size：输入选定商品的颜色和尺寸明细
- Description：显示选定商品的详细描述
- Load：从系统目录导入外部 TEXT 数据（需精确的数据格式，使用前请咨询软件顾问）
- Model & Guarantee No.：特殊功能，不对一般用户开放；允许在收货阶段输入商品唯一的保修号和型号，每个商品编号只能关联一个保修号，因此每个商品仅允许数量为1（不支持颜色和尺寸）。

> 来源: v7 Book-3 Section 6.2 Pages 12-21

> 相关图片: v7_Book-3_PROCESS_p013_img00.jpeg, v7_Book-3_PROCESS_p014_img00.jpeg, v7_Book-3_PROCESS_p015_img00.jpeg, v7_Book-3_PROCESS_p016_img00.jpeg, v7_Book-3_PROCESS_p017_img00.jpeg

---

### 如何在没有采购订单（PO）的情况下进行库存收货？

在没有采购订单的情况下进行库存收货的操作步骤如下：

1. **进入库存收货功能**
   - 从菜单进入 Stock Receive（库存收货）功能。

2. **设置为无 PO 收货**
   - 在收货信息页面中，选择收货指示器为 Without PO（无采购订单）。

3. **输入收货编号和地点**
   - 输入收货地点代码（Receiving Location Code）。
   - 收货编号（Receiving Number）可根据参数设置选择自动生成或手动输入。

4. **输入商品信息**
   - 输入收货商品代码（Item Code）。
   - 点击 Color & Size 按钮输入颜色和尺寸明细（如果商品有颜色和尺寸控制）。

5. **填写收货数量**
   - 输入实际收货数量。

6. **保存收货信息**
   - 点击 SAVE 按钮保存收货批次。
   - 系统将进入下一步的收货确认流程。

注意：
- 无 PO 收货适用于直接入库的场景，如赠品、样品或紧急采购后补单等情况。
- 同一收货批次可以同时包含有 PO 收货、无 PO 收货以及 Blanket 订单交货请求收货三种类型。
- 输入商品代码时，如果同时输入了单价或地点信息，则商品代码为必填字段。

> 来源: v7 Book-3 Section 6.2 Pages 12-19

> 相关图片: v7_Book-3_PROCESS_p019_img00.jpeg, v7_Book-3_PROCESS_p019_img01.jpeg

---

### 如何完成库存收货确认并过账（Posting）？

库存收货确认并过账的完整操作步骤如下：

1. **Step 1 - 修改收货批次（Modify Receive）**
   - 进入 Stock Receive Maintenance（收货维护）。
   - 允许在批次内添加、修改和删除收货项目。
   - 建议在进行下一步操作前完成所有必要的修正。
   - 注意：在 Step 6 过账之前的任何时间，都可以回退到此维护步骤进行数据修正。

2. **Step 2 - 打印收货报告（Print Receive Report）**
   - 将收货数量打印到打印队列（Print Queue）。
   - 用于纸质记录和核对。

3. **Step 3 - 生成条形码（Generate Bar Code）**
   - 为收货库存打印条形码标签。

4. **Step 4 - 生成接口文件（Generate Interface File）**
   - 根据收货批次数据生成 TEXT 接口文件。
   - 此功能为系统可选功能。

5. **Step 5 - 批次验证（Batch Validation）**
   - 执行批次验证。系统要求批次在过账前必须经过验证。
   - 验证报告将自动由系统打印到打印队列。
   - 用户必须检查验证报告，确认无误后再进入下一步的过账步骤。
   - 如果发现错误，用户可以随时返回之前的步骤进行修正。

6. **Step 6 - 批次过账（Batch Posting）**
   - 这是库存数量更新的最后一步。
   - 用户必须确保批次中的所有输入数据准确无误。
   - **过账后不允许更改数据。**
   - **过账后数据不可回退。**
   - 此步骤完成后，库存余额将根据实际收货数量进行更新。

整个流程分为两大操作：
a) 根据实际收货数量更新库存余额（由仓库或收货地点操作）。
b) 根据结算成本（与供应商发票核对后）更新库存加权平均成本（由财务部门或相关负责人确认）。

> 来源: v7 Book-3 Section 6.3 Pages 22-23

> 相关图片: v7_Book-3_PROCESS_p022_img00.jpeg, v7_Book-3_PROCESS_p023_img00.jpeg

---

## 库存转移 (4 条)

### 如何创建和执行库存转移（Stock Transfer）？

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

> 来源: v7 Book-3 Section 6.4 Pages 24-28

> 相关图片: v7_Book-3_PROCESS_p027_img00.jpeg, v7_Book-3_PROCESS_p027_img01.jpeg, v7_Book-3_PROCESS_p028_img00.jpeg, v7_Book-3_PROCESS_p028_img01.jpeg

---

### 如何使用手持扫描设备执行库存转移（Hand Held Scanner Transfer）？

使用手持扫描设备执行库存转移的工作流程说明：

1. **系统支持两种数据输入方式**
   - 手工数据输入（Manual Data Input）：按照标准工作流程执行。
   - 手持扫描设备输入（Hand Held Scanner Input）：通过手持条码扫描器完成数据采集。

2. **手工输入的工作流程**
   1. Batch Maintenance（批次维护）
   2. Batch Validation（批次验证）
   3. Generate Pick List（生成拣货单）
   4. Batch Amendment（批次修正）
   5. Print Amendment List（打印修正清单）
   6. Generate Labels & D/O（生成标签和交货单）
   7. Batch Posting（批次过账）

3. **手持扫描设备的工作流程**
   - 与手工输入流程不同，手持扫描设备的工作流程单独设计。
   - 通常可以通过手持设备直接扫描商品条码和位置信息，减少人工输入错误。
   - 数据采集完成后导入系统进行处理。

4. **系统特性**
   - 此流程称为 Location Oriented Transfer（面向地点的转移）。
   - 特别适用于将大量商品从一个地点转移到另一个或多个地点的情况。
   - 使用手持设备可以显著提高盘点效率和准确性。

注意：具体的手持扫描设备操作方式可能因设备型号和系统配置而异，请参考相关设备手册。

> 来源: v7 Book-3 Section 6.4 Pages 24-26

> 相关图片: v7_Book-3_PROCESS_p026_img00.jpeg

---

### 如何处理库存转移数量差异（Recovery & Adjustment）？

处理库存转移数量差异的操作步骤如下：

1. **进入差异恢复功能**
   - 此功能用于处理库存转移过程中不同地点之间的数量差异。
   - 当库存转移的接收方确认收货数量不一致时，需要确定责任方。

2. **查看差异记录列表**
   - 系统仅显示存在差异的转移记录。
   - 所有记录按 Transfer Reference Order Numbers（转移参考单号）排序显示。
   - 标记为 * 的记录表示等待处理（Recovery）。

3. **选择需要处理的转移单**
   - 从列表中选择一个带 * 标记的转移记录。

4. **输入恢复明细（Stock Transfer Recovery Detail Input）**
   - 系统显示该转移单的差异详细信息。
   - 用户需要判断哪个部门/方应对差异数量负责：
     - 转出方（Sending party）：如果责任在发货方
     - 接收方（Receiving party）：如果责任在收货方
     - 双方各承担一部分：按比例分配差异

5. **系统生成调整记录**
   - 根据用户的责任分配输入，系统将自动生成适当的调整记录来恢复此差异。

6. **特殊情况处理**
   - 如果双方都不对差异负责（例如运输途中丢失且无法追责），用户需要通过执行 Physical Adjustments（物理调整）来写销（write off）该差异。
   - 此操作独立于本应用程序，需要单独执行。

注意：及时处理差异记录有助于保持库存数据的准确性，建议在发现差异后尽快处理。

> 来源: v7 Book-3 Section 6.6 Pages 31-32

> 相关图片: v7_Book-3_PROCESS_p031_img00.jpeg, v7_Book-3_PROCESS_p032_img00.jpeg

---

### 如何确认库存转移的接收（Stock Transfer Receive Confirmation）？

确认库存转移接收的操作步骤如下：

1. **进入接收确认功能**
   - ChainStorePlus 要求所有库存转移操作都必须执行接收确认流程。
   - 这是一个控制流程，确保转出数量被接收方正确接收并确认。

2. **选择库存转移记录**
   - 点击或按回车选择需要确认的库存转移记录。

3. **确认接收数量**
   - 系统显示转移交货单（D/N）的数量和收货数量（Rec Qty）列。
   - Rec Qty 列默认填充为等于 D/N Qty 的数值。
   - 如果实际接收数量与交货单数量一致，直接确认无需修改。
   - 如果存在差异，在 Rec Qty 列修改为实际接收数量。
     - 例如：D/N = 8 件，实际接收 = 7 件，将 Rec Qty 修改为 7。
   - Var. 列（差异数量）将在输入后自动显示差异值。

4. **确认输入正确**
   - 检查差异数量是否正确。
   - 确认提交。

5. **差异处理**
   - 如果交货和接收数量不一致，系统将自动生成差异记录（Discrepancy Record）。
   - 这些差异记录需要后续通过手动恢复和调整流程（Stock Transfer Receive Recovery & Adjustment）处理。
   - 将在下一节（6.6）中详细讨论。

注意：此控制流程是确保库存转移准确性的关键步骤，建议认真核对实际收货数量。

> 来源: v7 Book-3 Section 6.5 Pages 29-30

> 相关图片: v7_Book-3_PROCESS_p029_img00.jpeg, v7_Book-3_PROCESS_p029_img01.jpeg, v7_Book-3_PROCESS_p029_img02.jpeg, v7_Book-3_PROCESS_p030_img00.jpeg, v7_Book-3_PROCESS_p030_img01.jpeg, v7_Book-3_PROCESS_p030_img02.jpeg

---

## 库存管理 (7 条)

### 如何冻结库存数量以准备实物盘点（Freeze On Hand Quantity）？

冻结库存数量以准备实物盘点的操作步骤如下：

1. **前期准备 - 清理未完成批次**
   - 在开始盘点之前，清理盘点地点的所有未完成数据批次。
   - 确保所有 outstanding batch 都已过账。

2. **进入冻结功能**
   - 从 Physical Count Process 功能中选择 Freeze On Hand Quantity。

3. **输入冻结范围**
   - Stock Freeze Operation 画面显示，要求输入 Stock Freeze Range。
   - 如果要对所有商品进行冻结，将范围留空（Leave Blank for Select ALL）。
   - 也可以指定特定的商品范围进行冻结。

4. **确认冻结**
   - 选择范围后点击 Confirm 确认。
   - 系统将以当前系统日期冻结商品的当前库存数量状态。
   - 系统会显示处理进度，完成后显示完成消息。

5. **重要注意事项**
   - **在 Stock Freeze 到 Physical Stock Counting Complete 期间，盘点地点不允许有任何库存移动更新或活动。**
   - 必须确保在冻结期间没有入库、出库、转移等操作影响该地点的库存。
   - 后续的库存差异计算将基于此冻结数量与实际盘点数量进行比较。

6. **后续流程**
   - 冻结完成后，即可开始实际的库存盘点操作。
   - 盘点完成后，可以将实际盘点数据输入系统（手工输入或手持设备上传）。
   - 实际盘点输入完成后，可以恢复该地点的正常库存活动。

7. **计算公式**
   - 过账后的库存数量计算公式：
     Current_On_Hand + (Physical_On_Hand - Freeze_On_Hand)
     其中：
     - Current_On_Hand：当前库存数量
     - Physical_On_Hand：实际盘点数量
     - Freeze_On_Hand：冻结时的库存数量

8. **未盘点商品的处理**
   - 如果存在于该地点但在实物盘点记录中未输入的商品，过账后其库存数量将被设置为零。

> 来源: v7 Book-3 Section 6.8 Pages 37-43

> 相关图片: v7_Book-3_PROCESS_p041_img00.jpeg, v7_Book-3_PROCESS_p042_img00.jpeg, v7_Book-3_PROCESS_p042_img01.jpeg, v7_Book-3_PROCESS_p043_img00.jpeg, v7_Book-3_PROCESS_p043_img01.jpeg, v7_Book-3_PROCESS_p043_img02.jpeg

---

### 如何输入实物盘点数据（Physical Count Stock Input）？

输入实物盘点数据的操作步骤如下：

1. **前提条件**
   - 必须已完成 Freeze On Hand Quantity（冻结库存数量）操作。
   - 实物盘点工作应已实际完成，确保数据准确。

2. **进入实物盘点输入批次功能**
   - 在完成库存冻结操作后，从 Physical Count Process 进入 Physical Count Stock Input Batch。

3. **恢复库存活动（可选）**
   - 注意：由于实物盘点在此输入阶段应已完成，用户可以恢复盘点地点的正常库存活动。
   - **但必须确保实物盘点已完全完成。**

4. **输入批次头信息**
   - Ref. No.（参考编号）：9(08)，仅显示，系统在记录确认时自动生成，用于实物盘点记录的参考编号。
   - Date（日期）：格式 dd/mm/yyyy，必填字段，实物盘点记录的录入日期。
   - Count Sheet No.（盘点表编号）：X(15)，必填字段，用于参考的盘点表编号。
   - Remarks（备注）：X(20)，可选字段，实物盘点记录的备注说明。

5. **输入商品明细**
   - Item No.（商品编号）：X(14)，每个记录至少需要一个商品。
   - Col.（颜色）：如果商品有颜色控制则为必填字段。
   - Size（尺寸）：如果商品有尺寸控制则为必填字段。
   - Quantity（数量）：9(08)，必填字段，实际盘点数量。
   - Description（描述）：可选，仅供参考。
   - Total Qty（总数量）：9(08)，仅显示，记录的总盘点数量。

6. **注意事项**
   - 同一商品可多次输入，因为系统后续会进行合并处理（consolidation）。
   - 如果导入数据与系统现有数据不同，系统会生成 Physical Adjustment Journal。

> 来源: v7 Book-3 Section 6.8 Pages 43-45

> 相关图片: v7_Book-3_PROCESS_p044_img00.jpeg, v7_Book-3_PROCESS_p044_img01.jpeg, v7_Book-3_PROCESS_p044_img02.jpeg

---

### 如何验证并过账实物盘点结果（Validation, Variance Report & Posting）？

验证实物盘点结果并完成过账的操作步骤如下：

**Step 3a - 数据验证（Stock Count Validation）**
1. 在完成实物盘点数据输入并确认无误后，执行验证操作。
2. 进入 Batch Validation 功能。
3. 系统将对输入数据进行验证。

**Step 3b - 打印差异报告（Variance Report Printing）**
1. 验证完成后，系统提示打印 Stock Variance Report（库存差异报告）。
2. 点击 OK 确认。
3. 系统显示处理进度。
4. 完成后显示完成消息。
5. 差异报告将显示冻结数量与实际盘点数量之间的差异。

**Step 4 - 批次过账（Stock Take Posting）**
1. 这是实物盘点流程的最后一步。
2. 系统将使用最终验证的盘点数据与冻结数量进行比较。
3. 点击 Batch Posting 按钮执行过账。
4. 系统显示处理进度。
5. 完成后显示完成消息。

6. **过账后的库存计算公式**
   - 过账后库存 = Current_On_Hand + (Physical_On_Hand - Freeze_On_Hand)
   - Current_On_Hand：当前库存数量
   - Physical_On_Hand：实际盘点数量
   - Freeze_On_Hand：冻结时的库存数量

7. **过账后的效果**
   - 库存数量将更新为实际盘点结果。
   - 如果存在差异，系统将生成相应的更新日志/历史记录（Update journal / history records）。
   - 对于在盘点记录中未输入但存在于该地点的商品，过账后其库存数量将被设置为零。

**完整工作流程回顾**
1. 过账所有未完成批次
2. Freeze On-Hand qty and average cost（冻结库存数量和平均成本）
3. Physical Stock Take at location / Fill in Count sheet（实地盘点/填写盘点表）
4. Batch Maintenance（输入盘点数据）
5. Batch Validation & Variance Report（验证并打印差异报告）
6. Batch Posting（过账）

> 来源: v7 Book-3 Section 6.8 Pages 37-47

> 相关图片: v7_Book-3_PROCESS_p046_img00.jpeg, v7_Book-3_PROCESS_p046_img01.jpeg, v7_Book-3_PROCESS_p046_img02.jpeg, v7_Book-3_PROCESS_p046_img03.jpeg, v7_Book-3_PROCESS_p046_img04.jpeg, v7_Book-3_PROCESS_p047_img00.jpeg, v7_Book-3_PROCESS_p047_img01.jpeg, v7_Book-3_PROCESS_p047_img02.jpeg

---

### 实物盘点（Physical Count）的完整流程是什么？

实物盘点的完整流程如下：

**目标：** 在实际盘点库存后执行库存更新。

**先决条件：**
- 在创建实物盘点批次信息之前，必须先处理 Freeze On Hand Quantity（冻结库存数量）。
- 由于最终的过账操作通常远晚于盘点数据输入，冻结流程对于正确计算过账后的库存数量至关重要。

**完整操作流程：**

**第1步：冻结库存数量（Freeze On Hand Quantity）**
- 清理盘点地点的所有未完成数据批次。
- 执行 Stock Freeze，输入冻结范围（留空为选择所有商品）。
- 确认后系统以当前日期冻结库存状态。
- 重要：冻结至盘点完成期间，盘点地点不允许有任何库存移动。

**第2步：创建盘点批次并输入数据（Batch Maintenance）**
- 针对特定地点创建新的批次。
- 输入盘点表编号（Count Sheet No.）、日期和商品明细。
- 同一商品可多次输入，系统后续会合并处理。
- 此时可恢复盘点地点的正常库存活动（前提是实物盘点已完全完成）。

**第3步：验证并生成差异报告（Validation & Variance Report）**
- 执行 Batch Validation 验证数据。
- 系统自动打印 Stock Variance Report 到打印队列。
- 检查差异报告，确认是否需要进行调整。

**第4步：过账（Batch Posting）**
- 执行最终过账。
- 过账后库存 = Current_On_Hand + (Physical_On_Hand - Freeze_On_Hand)。
- 如果存在差异，系统生成 Physical Adjustment Journal。
- 未在盘点记录中输入的商品将被设置为零库存。
- 过账后不可回退。

**支持的功能：**
1. Freeze On Hand Quantity（冻结数量）
2. Batch Maintenance（批次维护）：创建/修改/删除记录
3. Batch Validation（批次验证）
4. Batch Posting（过账）
5. Modify Description（修改描述）
6. Scratch Batch（废弃批次）
7. Clear In Use Status（清除使用中状态）
8. Change Status（更改状态：Input, Validated）

**批次状态说明：**
- Input：批次正在输入
- Validated：批次已验证
- Partly Pst：过账时出错，需要重新过账

**支持两种数据输入方式：**
- 手工数据输入（Manual Data Input）
- 手持扫描设备输入（Hand Held Scanner Input）

> 来源: v7 Book-3 Section 6.8 Pages 37-47

> 相关图片: v7_Book-3_PROCESS_p041_img00.jpeg, v7_Book-3_PROCESS_p042_img00.jpeg, v7_Book-3_PROCESS_p044_img00.jpeg, v7_Book-3_PROCESS_p046_img00.jpeg, v7_Book-3_PROCESS_p047_img00.jpeg

---

### 如何进行库存物理调整（Physical Adjustment）？

进行库存物理调整的操作步骤如下：

1. **进入物理调整功能**
   - 从菜单进入 Physical Adjustment Process。
   - Physical Adjustment 允许用户对库存数量进行修正，并保留历史日志。

2. **菜单画面操作**
   - 在菜单画面中创建新的物理调整批次。

3. **批次维护画面 - 输入头信息（Batch Maintenance Screen）**
   - 各字段说明：
     - Ref. No.（参考编号）：9(08)，仅显示，系统在记录确认时自动生成，用于物理 I/O 记录的参考编号。
     - Date（日期）：格式 dd/mm/yyyy，必填字段。
     - Reason Code（原因代码）：X(02)，必填字段，唯一代码用于标识特定原因（在 Reason Table Maintenance 中预定义）。
     - Location Code（地点代码）：X(04)，必填字段，执行物理 I/O 操作的地点，旁边会显示地点描述。
     - Remarks（备注）：X(40)，必填字段，特定物理 I/O 记录的备注说明。

4. **批次维护画面 - 输入商品明细**
     - Seq（序号）：9(03)，仅显示，商品信息的顺序编号，每个参考编号最多 200 个序号。
     - Item No.（商品编号）：X(14)，每个参考编号至少需要一个商品。
     - Col（颜色）：X(04)，如果商品有颜色控制则为必填字段。
     - Size（尺寸）：X(04)，如果商品有尺寸控制则为必填字段。
     - Adjust（调整数量）：S9(07)，必填字段，对应商品的调整数量（正数为增加，负数为减少）。
     - Description（描述）：X(40)，可选，仅供参考。
     - Total（总计）：S9(07)，仅显示，总调整数量。

5. **执行验证和过账**
   1. Batch Maintenance（批次维护）：创建、修改、删除记录
   2. Batch Validation（批次验证）：验证数据
   3. Batch Posting（批次过账）：最终过账

6. **其他功能**
   - Modify Description：修改描述
   - Scratch Batch：废弃批次
   - Clear In Use Status：清除使用中状态
   - Change Status：更改状态（Input, Validated）
   - Search Up / Search Down：上下搜索

7. **批次状态说明**
   - Input：批次正在输入中
   - Validated：批次已通过验证
   - Partly Pst：过账时发生错误，需要重新过账

> 来源: v7 Book-3 Section 6.7 Pages 33-36

> 相关图片: v7_Book-3_PROCESS_p034_img00.jpeg, v7_Book-3_PROCESS_p034_img01.jpeg, v7_Book-3_PROCESS_p035_img00.jpeg

---

### 如何创建退货给供应商的单据（Return to Suppliers）？

创建退货给供应商的单据操作步骤如下：

1. **进入功能**
   - 从菜单进入 Return to Suppliers（RTS）功能。
   - 此功能允许用户将商品退回给供应商，适用于错误交货、产品损坏等情况。

2. **按照工作流程执行**
   **Step 1 - Batch Maintenance（批次维护 - Header Information Folder）**
   - 点击 Create 创建新的退货批次。
   - 输入以下头信息字段：
     - Return No.（退货编号）：X(08)，必填字段，特定退货单的参考编号。
     - Date（日期）：格式 99/99/9999，必填字段（dd/mm/yyyy），退货日期。
     - Return Type（退货类型）：X(01)，必填字段，退货类型：Normal（正常）或 Consignment（代销）。
     - Supplier（供应商）：X(08)，必填字段，供应商名称。
     - Supplier Ref.（供应商参考号）：X(08)，可选字段，供应商的参考编号。
     - Transfer Ref.（转移参考号）：X(08)，可选字段，转移的参考编号。
     - Currency（货币）：X(03)，必填字段，货币代码（如 HKD、USD 等）。
     - Ex. Rate（汇率）：9(05).(05)，显示字段，基础货币与外币之间的汇率。
     - Total Ret. Qty（退货总数量）：X(08)，仅显示。
     - Ret. Amt.（退货金额）：X(08)，仅显示。
     - Discount Amt.（折扣金额）：X(08)，仅显示。
     - Net Return Amt.（退货净额）：9(09).(02)，显示字段，计算公式：总金额 x (1 - 折扣/100) - 其他折扣 + 其他费用。
     - Remarks（备注）：X(79)，两行文本描述用于备注输入。

   **Step 2 - 输入商品明细（Manage Item Folder）**
   - Item（商品）：X(09)，可选字段，如果输入了单价或地点则必填。
   - Unit Price（单价）：(+/-)9(08).9(02)，可选字段，留空/空格则分配零价格。
   - Loc.（地点）：X(04)，必填字段，执行退货交易的地点代码。
   - Qty（数量）：(+/-)9(07)，可选字段，如果商品没有颜色和尺寸，则数量字段变为必填字段。
   - Unit（单位）：X(04)，显示字段，自动从商品主文件记录中检索用户预定义的计量单位。
   - Rec. Amt.（收货金额）：(+/-)9(08).9(02)，显示字段，总金额 = 单价 x 数量，系统自动计算。
   - Total Qty/Amt.（总数量/总金额）：显示字段，该交货单中交货的商品总数量和总金额。

   **Step 3 - Batch Validation（批次验证）**
   - 验证批次数据。

   **Step 4 - Generate RTS List（生成退货清单）**
   - 生成退货清单。

   **Step 5 - Generate RTS Note（生成退货单）**
   - 生成退货单。

   **Step 6 - Batch Posting（批次过账）**
   - 最终过账，更新库存。

3. **批次状态说明**
   - Input：批次处于数据输入模式
   - Validated：批次已验证
   - RTS List：退货清单已生成
   - RTS Note：退货单已生成

> 来源: v7 Book-3 Section 6.9 Pages 48-53

> 相关图片: v7_Book-3_PROCESS_p049_img00.jpeg, v7_Book-3_PROCESS_p050_img00.jpeg, v7_Book-3_PROCESS_p052_img00.jpeg

---

### 如何完成退货给供应商的验证和过账？

完成退货给供应商的验证和过账操作步骤如下：

**1. 批次验证（Batch Validation）**
   - 在完成退货批次数据输入后，执行 Batch Validation。
   - 系统会验证退货数据的完整性，包括供应商信息、商品代码、数量等。
   - 验证通过后，批次状态变为 Validated。

**2. 生成退货清单（Generate RTS List）**
   - 验证通过后，点击 Generate RTS List。
   - 系统生成退货清单，供仓库人员拣货参考。
   - 生成后，批次状态变为 RTS List。

**3. 生成退货单（Generate RTS Note）**
   - 点击 Generate RTS Note。
   - 系统生成正式的退货单（Return to Supplier Note），可作为给供应商的退货凭证。
   - 生成后，批次状态变为 RTS Note。

**4. 批次过账（Batch Posting）**
   - 这是最后一步。
   - 执行过账后，库存数量将相应减少。
   - 系统会创建相应的库存交易记录和日志。
   - 过账后数据不可回退。

**完整工作流程顺序：**
1. Batch Maintenance（批次维护）
   - Stock Receive Input without PO（或 Receive Confirmation）
2. Batch Validation（批次验证）
3. Generate RTS List（生成退货清单）
4. Generate RTS Note（生成退货单）
5. Batch Posting（批次过账）

**批次状态变更流程：**
Input -> Validated -> RTS List -> RTS Note

注意：
- 如果退货时需同时处理收货，可以先执行 Stock Receive Input without PO（无 PO 收货）或 Receive Confirmation（收货确认），再执行退货流程。
- 退货类型分为 Normal（正常退货）和 Consignment（代销退货），两种类型的财务处理方式不同。

> 来源: v7 Book-3 Section 6.9 Pages 48-53

> 相关图片: v7_Book-3_PROCESS_p049_img00.jpeg, v7_Book-3_PROCESS_p050_img00.jpeg, v7_Book-3_PROCESS_p052_img00.jpeg

---

## 配送流程 (3 条)

### 如何创建交货单进行库存入库（Delivery Order - Stock In）？

创建交货单进行库存入库的操作步骤如下：

1. **进入功能**
   - 从菜单进入 Delivery Order Process - Stock In（交货单入库流程）。
   - 此功能用于处理库存入库操作。

2. **系统原理**
   - 系统将入库数据作为 Physical Adjustment（物理调整）的一种形式处理。
   - 使用用户自定义的交易代码（Transaction Codes）进行区分。
   - 更新机制与 Delivery Order - Stock Out 流程相同，但计算方向相反（逆向计算）。

3. **操作步骤**
   - 创建新批次（Create New Batch）。
   - 点击 Batch Maintenance 进入批次维护。

4. **输入头信息**
   - 参考 Delivery Order Stock Out 的头信息字段，主要包括：
   - 日期、部门编号、客户名称、交货日期、货币、汇率等。

5. **输入商品明细**
   - 输入商品代码、入库交易代码、单价、地点、数量等信息。
   - 入库交易代码由用户自定义，用于标识不同的入库原因。

6. **执行工作流程**
   - Batch Validation（批次验证）
   - Batch Posting（批次过账）

注意：具体操作细节与 Stock Out 流程相似，但因库存方向相反，对库存的影响是增加而非减少。

> 来源: v7 Book-3 Section 6.11 Pages 66-67

> 相关图片: v7_Book-3_PROCESS_p066_img00.jpeg, v7_Book-3_PROCESS_p066_img01.jpeg, v7_Book-3_PROCESS_p067_img00.jpeg

---

### 如何创建交货单进行库存出库（Delivery Order - Stock Out）？

创建交货单进行库存出库的操作步骤如下：

**概念说明：**
Delivery Order Process - Stock Out 允许用户使用自定义的交易代码来处理库存出库。常见的出库交易类型包括：
- Internal Use（内部使用）
- Internal Sales（内部销售）
- Give Away Samples（赠送样品）
- Sponsorship（赞助）
- Special Project Usage（特殊项目使用）
- Write Off（报废）

**操作步骤：**

1. **进入功能**
   - 从菜单进入 Delivery Order - The Stock Out Process。
   - 首先创建新批次（Create New Batch）。
   - 点击 Batch Maintenance。

2. **输入头信息（Header Information Folder）**
   - Pick Ref. No.（拣货参考编号）：X(08)，仅显示，特定交货单的参考编号。
   - Date（日期）：格式 99/99/9999，必填字段（dd/mm/yyyy），商品从此日期开始提取。
   - Dept. No.（部门编号）：X(01)，必填字段，预设的处理此交货单交易的部门代码。
   - Customer Data Input（客户数据输入）：可选。
   - Customer Name（客户名称）：X(08)，必填字段。
   - Address（地址）：必填字段。
   - Del. Date（交货日期）：格式 99/99/9999，必填字段（dd/mm/yyyy），订单需在此日期前交货。
   - Remarks（备注）：X(80)，可选字段，此拣货单的任何备注。
   - Project no.（项目编号）：X(07)，可选字段，预定义的项目 ID，如果交易基于项目则需要输入。

3. **输入货币和金额信息**
   - Currency（货币）：X(03)，必填字段，货币代码（如 HKD、USD 等）。
   - Ex. Rate（汇率）：9(05).(05)，显示字段。
   - Discount（折扣）：9(03).(02)，可选字段，交货单的折扣百分比。
   - Total Amt.（总金额）：9(09).(02)，显示字段。
   - Other Disc/Adj（其他折扣/调整）：9(09).(02)，可选字段。
   - Other Charg/Adj（其他费用/调整）：9(09).(02)，可选字段。
   - Net Total Amt.（净额）：9(09).(02)，显示字段，计算公式：Total Amt. x (1 - Discount/100) - Other Disc. + Other Charge。

4. **输入备注（Remarks Folder）**
   - Remarks（备注）：X(79)，最多 20 行文本描述。

5. **输入商品明细（Manage Item Folder）**
   - Item（商品）：X(09)，可选字段，如果输入了单价或地点则必填。
   - Trx（交易代码）：X(03)，必填字段，用户预定义并分配给此交货单的交易代码。
   - Unit Price（单价）：(+/-)9(08).9(02)，可选字段，留空则分配零价格。
   - Loc.（地点）：X(04)，必填字段，执行交货单交易的地点代码。
   - Qty（数量）：(+/-)9(07)，可选字段，如果商品没有颜色和尺寸，则数量字段变为必填字段。
   - Unit（单位）：X(04)，显示字段，自动从商品主文件检索。
   - Rec. Amt.（金额）：(+/-)9(08).9(02)，显示字段，系统自动计算。
   - Total Qty/Amt.（总数量/总金额）：显示字段。

6. **执行工作流程**
   **Step 1:** D/O Data Maintenance（交货单数据维护）
   **Step 2:** D/O Batch Validation（批次验证）- 点击 Batch Validation，系统弹出消息框，点击 OK 完成，显示完成消息。
   **Step 3:** Print Pick List（打印拣货单）- 点击 Generate Pick Up，系统弹出消息框，点击 OK 完成。
   **Step 4:** Batch Amendment（批次修正）- 可在需要时修改。
   **Step 5:** Print Amendment List（打印修正清单）
   **Step 6:** Print Delivery Order（打印交货单）- 点击 Print Delivery Order，系统弹出消息框，点击 OK 完成。用户也可以从右上角的三个垂直点菜单中选择保存为 Delivery Order。
   **Step 7:** Batch Posting（批次过账）- 最终过账。

注意：以上功能有顺序依赖关系，必须按工作流程顺序执行。

> 来源: v7 Book-3 Section 6.10 Pages 54-65

> 相关图片: v7_Book-3_PROCESS_p056_img00.jpeg, v7_Book-3_PROCESS_p056_img01.jpeg, v7_Book-3_PROCESS_p056_img02.jpeg, v7_Book-3_PROCESS_p056_img03.jpeg, v7_Book-3_PROCESS_p056_img04.jpeg, v7_Book-3_PROCESS_p057_img00.jpeg, v7_Book-3_PROCESS_p057_img01.jpeg, v7_Book-3_PROCESS_p058_img00.jpeg, v7_Book-3_PROCESS_p059_img00.jpeg, v7_Book-3_PROCESS_p060_img00.jpeg, v7_Book-3_PROCESS_p061_img00.jpeg, v7_Book-3_PROCESS_p061_img01.jpeg, v7_Book-3_PROCESS_p062_img00.jpeg, v7_Book-3_PROCESS_p062_img01.jpeg, v7_Book-3_PROCESS_p062_img02.jpeg, v7_Book-3_PROCESS_p062_img03.jpeg, v7_Book-3_PROCESS_p063_img00.jpeg, v7_Book-3_PROCESS_p063_img01.jpeg, v7_Book-3_PROCESS_p063_img02.jpeg, v7_Book-3_PROCESS_p063_img03.jpeg, v7_Book-3_PROCESS_p064_img00.jpeg, v7_Book-3_PROCESS_p064_img01.jpeg, v7_Book-3_PROCESS_p064_img02.jpeg, v7_Book-3_PROCESS_p065_img00.jpeg, v7_Book-3_PROCESS_p065_img01.jpeg

---

### 如何验证并最终过账交货单出库（Batch Validation & Posting for D/O Stock Out）？

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

> 来源: v7 Book-3 Section 6.10 Pages 61-65

> 相关图片: v7_Book-3_PROCESS_p062_img00.jpeg, v7_Book-3_PROCESS_p062_img01.jpeg, v7_Book-3_PROCESS_p062_img02.jpeg, v7_Book-3_PROCESS_p062_img03.jpeg, v7_Book-3_PROCESS_p063_img00.jpeg, v7_Book-3_PROCESS_p063_img01.jpeg, v7_Book-3_PROCESS_p063_img02.jpeg, v7_Book-3_PROCESS_p063_img03.jpeg, v7_Book-3_PROCESS_p064_img00.jpeg, v7_Book-3_PROCESS_p064_img01.jpeg, v7_Book-3_PROCESS_p064_img02.jpeg, v7_Book-3_PROCESS_p065_img00.jpeg, v7_Book-3_PROCESS_p065_img01.jpeg

---

## 在线查询 (18 条)

### 如何查询POS在线销售与销售备忘录？

此功能用于比较各店铺的销售业绩表现。

在位置选择窗口（Location Selection Window）中，您可以选择四种比较范围：
- 所有位置（All Location）
- 特定位置（Particular Location）
- 部门（Division）
- 国家/地区（Country）

在模式选择窗口（Mode Selection Window）中，您可以设置比较规则：

1. Summary By（汇总方式）：
   - Location（按位置）
   - Division（按部门）
   - Group（按组别）
   - Country（按国家/地区）

2. Mode（模式）：
   - Total（总计）
   - Sales（销售）
   - Deposit（订金）
   - Deposit Settlement（订金结算）
   - Sales (Excl Dep Set)（销售，不含订金结算）
   - Service（服务）
   - Gift Cert.（礼品券）

3. Type（类型）：
   - All Location（所有位置）
   - Own Shop（自有店铺）
   - Web Store（网店）
   - Franchise（加盟店）

4. Day Range（日期范围）：
   - Day（日）
   - Period（期间）
   - Week（周）
   - Month（月）
   - Year（年）

5. Compare（比较基准）：
   - Last Year Same Day（去年同日）
   - Last Month Same Day（上月同日）
   - Last Week Same Day（上周同日）
   - Target（目标）
   - User Define（用户自定义）

> 来源: v7 Book-4 Section 7.3 Page 12-13

> 相关图片: v7_Book-4_INQUIRY_p012_img00.jpeg

---

### 如何进行POS在线销售查询？

进入POS在线销售查询画面后，您可以查看两个不同时间段的销售数据比较。系统将以对比方式显示销售数据，帮助您分析销售趋势和业绩变化。

画面上方显示两个不同时间段的销售数据对比，通过直观的对比视图来评估销售表现。

> 来源: v7 Book-4 Section 7.4 Page 14

> 相关图片: v7_Book-4_INQUIRY_p014_img00.jpeg

---

### 如何查询交货单收货（入库）日记账？

此功能用于查询交货单收货（即库存入库）的记录信息。进入查询画面后，您可以查看已收货的交货单记录，包括入库参考编号、收货日期、供应商信息、入库商品及数量等详细信息。

> 来源: v7 Book-4 Section 7.14 Page 31

> 相关图片: v7_Book-4_INQUIRY_p031_img00.jpeg

---

### 如何查询交货单日记账？

此功能用于查询交货单（Delivery Order）及其详细信息。提供以下查询方式：
- 按参考编号查询（Reference No.）
- 按日期查询（Date）
- 按项目编号查询（Project No.）

进入交货单日记账查询画面（Delivery Order Journal Enquiry）后，显示一般索引信息：
- 参考编号（Reference Number）
- 交货单日期（Delivery Order Date）
- 客户代码/名称（Customer Code/Name，取决于系统设定）
- 交易代码（Transaction Code）
- 项目编号（Project Number）
- 总交货金额（Total Delivery Value Amount）

双击选定记录后，进入交货单详细信息画面（Delivery Order Detail Screen），显示：
- 拣货单参考编号（Pick List Reference Number）
- 部门代码（Department Code）
- 拣货单参考日期（Pick List Reference Date）
- 客户名称（Customer Name）
- 交货单日期、备注、项目编号
- 币种（Currency）
- 汇率（Exchange Rate）
- 折扣（Discount）
- 总金额（Total Amount）
- 其他折扣（Other Discount）
- 其他费用（Other Charge）
- 净总金额（Net Total Amount）

商品信息管理画面（Item Information Management Screen）显示：
- 拣货参考编号、序号、商品代码、单价、位置代码、数量、单位
- 总价和总数量、总金额、交易代码

> 来源: v7 Book-4 Section 7.12 Page 28-29

> 相关图片: v7_Book-4_INQUIRY_p028_img00.jpeg, v7_Book-4_INQUIRY_p029_img00.jpeg, v7_Book-4_INQUIRY_p029_img01.jpeg

---

### 如何查询会员活动明细？

此功能使用户能够查看每位会员客户的销售明细，可深入到最详细级别。

操作步骤：
1. 进入会员活动明细查询画面（Member Activities Details Screen）。
2. 鼠标选择所需会员并点击，系统将显示选择菜单供用户进一步操作。
3. 从弹出显示菜单中选择"ALL"（全部），即可查看该选定会员的全部活动记录。

通过该功能，您可以追踪每位会员的所有交易活动，包括购买记录、服务记录等，有助于分析会员消费行为和偏好。

> 来源: v7 Book-4 Section 7.16 Page 33-34

> 相关图片: v7_Book-4_INQUIRY_p033_img00.jpeg, v7_Book-4_INQUIRY_p034_img00.jpeg

---

### 如何查询会员销售额汇总？

此功能用于查看会员的销售数据汇总信息（Member Sales Figures Summary）。

进入会员销售信息画面（Member Sales Information Screen）后，显示以下一般信息：
- 姓名（Name）
- 类型（Type）
- 折扣（Discount）
- 身份证号（ID No.）
- 状态（Status）
- 限额（Limit）
- 月份（Month）
- 去年总销售额（Last Year Gross Sales）
- 今年总销售额（Current Year Gross Sales）
- 去年净销售额（Last Year Net Sales）
- 今年净销售额（Current Year Net Sales）

通过此功能可以对比会员的年度销售业绩变化，便于分析会员价值和消费趋势。

> 来源: v7 Book-4 Section 7.18 Page 36

> 相关图片: v7_Book-4_INQUIRY_p036_img00.jpeg, v7_Book-4_INQUIRY_p036_img01.jpeg, v7_Book-4_INQUIRY_p036_img02.jpeg

---

### 如何查询库存调拨收货信息？

此查询画面的数据格式与库存调拨收货确认处理（Stock Transfer Receive Confirmation Process）相同，但所有字段均为受保护的只读状态。您可以在该画面中查看已确认的调拨收货信息，包括调拨商品明细、数量以及相关确认信息，但不能进行任何修改操作。

> 来源: v7 Book-4 Section 7.9 Page 23

> 相关图片: v7_Book-4_INQUIRY_p023_img00.jpeg, v7_Book-4_INQUIRY_p023_img01.jpeg

---

### 如何按仓库位置查询库存？

进入仓库位置索引画面（Item Index Screen），系统将显示所有库存位置列表，包括店铺和仓库。选择一个位置后即可查看该位置的库存详情。

查询结果提供两种库存数量查看模式：
- 库存数量（不含在途库存）
- 物理库存数量（包含待收货的在途库存）

点击选定的仓库位置，将显示该位置的具体库存信息画面。

> 来源: v7 Book-4 Section 7.2 Page 11

> 相关图片: v7_Book-4_INQUIRY_p011_img00.jpeg, v7_Book-4_INQUIRY_p011_img01.jpeg

---

### 如何按商品查询库存？

进入商品索引画面（Item Index Screen），鼠标选择所需商品并双击弹出选择菜单。在菜单中选择"Item Distribution Detail"，系统将以矩阵形式显示该商品的库存分布详情。

画面标签说明：
- All Color：显示所有颜色的总库存数量，不按颜色细分。
- Color：显示选定颜色的库存数量。
- By Color & Location（默认矩阵显示）：颜色显示在标题行，仓库位置和尺码以矩阵形式展示。
- By Location & Color：切换显示格式，仓库位置在标题行，颜色和尺码以矩阵形式展示。
- Skip Zero Qty：隐藏库存为零的仓库位置。
- Skip Size Zero Qty：隐藏库存为零的尺码。
- Zoom：最多显示16个尺码的矩阵。
- Location Layer：通过"Location Layer"可选表进行仓库位置过滤，基于"Location Tree"可选表中的定义将仓库分组显示。
- Mode：以不同库存状态显示库存数量。

结果画面显示以下标签：
- Phy. O/H（Physical On-Hand）：实际记录的系统库存数量，包含在途库存数量。
- O/H (Excl Tfx In)：在途库存数量（尚未被收货方确认的调拨库存数量）。
- Out Transit：发出调拨库存数量（尚未被收货方确认收货的调出库存数量）。
- Non Res.（Non-Reserved Qty，可选）：批发业务中尚未预留的销售订单数量。
- Reserved（Reserved Qty，可选）：预留库存数量。店铺位置为未结"订金"数量，仓库位置为销售订单的实际预留数量。
- O/H Avail（On-hand Qty Available for Sell）= 物理库存 - 预留数量。
- On Order：该仓库位置的未结采购订单总数量。
- Tot Avail（Total Available）= 可用库存 + 在订数量。

> 来源: v7 Book-4 Section 7.1 Page 5-10

> 相关图片: v7_Book-4_INQUIRY_p005_img00.jpeg, v7_Book-4_INQUIRY_p006_img00.jpeg, v7_Book-4_INQUIRY_p006_img01.jpeg, v7_Book-4_INQUIRY_p006_img02.jpeg, v7_Book-4_INQUIRY_p007_img00.jpeg, v7_Book-4_INQUIRY_p009_img00.jpeg, v7_Book-4_INQUIRY_p009_img01.jpeg, v7_Book-4_INQUIRY_p010_img00.jpeg, v7_Book-4_INQUIRY_p010_img01.jpeg

---

### 如何按备忘录编号或仓库位置查询销售日记账？

此功能用于查询特定销售备忘录或仓库位置的销售数据。提供四种查询方式：

1. 按销售备忘录编号查询（By Sales Memo No.）：以销售备忘录编号作为参考键进行查询。
2. 按仓库位置与日期查询（By Location & Date）：以仓库位置和日期作为参考键进行查询。
3. 按型号查询（By Model No.）：以商品型号进行查询。
4. 按保修编号查询（By Guarantee No.）：以保修编号进行查询。

操作步骤：
1. 进入销售日记账查询索引画面（Sales Journal Enquiry Index Screen）。
2. 选择所需的查询方式。
3. 输入相应的查询条件。
4. 系统将显示符合条件的结果列表。
5. 点击选定记录可查看销售日记账详细信息画面（Sales Journal Detail Inquiry Screen）。

> 来源: v7 Book-4 Section 7.5 Page 15-16

> 相关图片: v7_Book-4_INQUIRY_p015_img00.jpeg, v7_Book-4_INQUIRY_p016_img00.jpeg

---

### 如何查询物理出入库日记账？

此功能用于查询物理调整（Physical Adjustment）的一般信息和详细信息。

进入物理出入库查询索引画面（Physical I/O Enquiry Index Screen）后，显示以下一般信息：
- 物理出入库参考编号（Physical I/O Reference Number）
- 物理出入库日期（Physical I/O Date）
- 物理出入库仓库位置（Physical I/O Location）
- 物理出入库数量（Physical I/O Quantity）
- 物理出入库原因（Physical I/O Reason）
- 备注（Remarks）

操作步骤：
1. 在物理出入库索引视图菜单中，双击选定的项目。
2. 系统显示物理出入库商品详细信息画面（Physical I/O Item Detail Screen）。

物理出入库商品详细信息包括：
- 物理出入库参考编号、日期、备注
- 商品编号、颜色、尺码、内缝长、位置代码
- 调整数量
- 平均成本
- 总调整成本
- 该出入库参考的总调整数量和总调整成本

> 来源: v7 Book-4 Section 7.10 Page 24-25

> 相关图片: v7_Book-4_INQUIRY_p024_img00.jpeg, v7_Book-4_INQUIRY_p025_img00.jpeg

---

### 如何查询物理盘点日记账？

此功能用于查询物理盘点的一般信息和详细信息。提供三种查询方式：

1. 按参考编号查询（By Reference No.）：以参考编号作为查询键。
2. 按日期查询（By Date）：以日期作为查询键。
3. 按盘点表编号查询（By Count Sheet No.）：以物理盘点表编号作为查询键。

进入物理盘点查询索引画面（Physical Count Enquiry Index Screen）后，选择查询方式并输入条件。

双击选定记录后，进入物理盘点商品详细信息画面（Physical Count Item Detail Screen），显示：
- 物理盘点参考编号（Physical Count Reference Number）
- 物理盘点日期（Physical Count Date）
- 备注（Remarks）
- 商品信息表格，包含：
  - 商品编号（Item Number）
  - 颜色（Color）
  - 尺码（Size）
  - 内缝长（Inseam）
  - 仓库位置（Location）
  - 物理盘点数量（Physical Count Quantity）
  - 物理盘点表编号（Physical Count Sheet Number）
  - 执行盘点操作的用户ID（User ID）

> 来源: v7 Book-4 Section 7.11 Page 26-27

> 相关图片: v7_Book-4_INQUIRY_p026_img00.jpeg, v7_Book-4_INQUIRY_p027_img00.jpeg

---

### 如何查询订金日记账？

此功能用于查询订金记录信息。提供以下查询方式：
1. 按订金编号查询（By Deposit No.）
2. 按日期查询（By Date）
3. 按客户名称查询（By Customer Name）
4. 按电话号码查询（By Phone No.）

进入订金日记账索引画面（Deposit Journal Index Screen）后，显示的索引信息包括：
- 订金编号（Deposit No.）
- 日期（Date）
- 客户名称（Customer Name）
- 电话号码（Phone No.）
- 订金金额（Deposit Amount）
- 状态（Status）

> 来源: v7 Book-4 Section 7.15 Page 32

> 相关图片: v7_Book-4_INQUIRY_p032_img00.jpeg

---

### 如何查询调拨日记账？

此功能用于查询库存系统（Stock System）中执行的调拨处理相关信息。

进入调拨日记账查询索引画面（Transfer Journal Enquiry Index Screen）：
- 显示调拨索引的一般信息：
  - 调拨参考编号（Transfer Reference Number）
  - 调拨日期（Transfer Date）
  - 调拨备注（Remarks）

操作步骤：
1. 在商品索引视图菜单中，点击选择所需项目。
2. 在弹出的选择对话框中，点击"Transfer Detail Enquiry"（调拨详细信息查询）。
3. 系统显示调拨日记账详细信息画面。

调拨商品详细信息包括：
- 调拨参考编号（Transfer Reference Number）
- 调拨日期（Transfer Date）
- 备注（Remarks）
- 调拨商品编号（Item Number）
- 商品颜色和尺码（如有）
- 调出/调入仓库位置（Transfer From/To Location）
- 调拨数量（Transfer Quantity）
- 平均成本（Average Cost）
- 总调拨成本（Total Transfer Cost）
- 拣货单编号（Reference Number of Picking List）
- 总调拨商品数量和该调拨参考的总成本

注意：如果用户登录账户对这些字段没有启用访问权限，则不会显示平均成本、总调拨成本和调拨参考总成本。

> 来源: v7 Book-4 Section 7.8 Page 21-22

> 相关图片: v7_Book-4_INQUIRY_p021_img00.jpeg, v7_Book-4_INQUIRY_p022_img00.jpeg

---

### 如何查询退货给供应商日记账？

此功能用于查询退还给供应商的记录信息。进入退货供应商日记账索引画面（Return Supplier Journal Index Screen）后，系统将显示退货记录列表，您可以查看退货相关信息，包括退货编号、退货日期、供应商信息、退货商品及数量等。

> 来源: v7 Book-4 Section 7.13 Page 30

> 相关图片: v7_Book-4_INQUIRY_p030_img00.jpeg

---

### 如何查询采购收货日记账？

此功能用于查询采购收货记录及其详细信息。数据可从不同数据路径的独立数据文件夹中检索。

进入采购收货查询索引画面（Purchase Receive Enquiry Index Screen）后，显示以下一般采购收货信息：
- 采购收货编号（Purchase Receive Number）
- 日期（Date）
- 采购订单编号（Purchase Order Number）
- 供应商代码（Supplier Code）
- 供应商参考编号（Supplier Reference Number）
- 采购收货金额（Purchase Receive Amount）
- 使用币种（Currency）
- 按数据文件夹排序显示

操作步骤：
1. 在索引列表中查找所需的采购收货记录。
2. 双击选定的采购收货记录。
3. 系统显示采购收货详细抬头画面（Purchase Receive Detail Header Screen）。
4. 数据格式与采购收货处理画面相同，但所有数据字段均为受保护的只读状态。

> 来源: v7 Book-4 Section 7.7 Page 20

> 相关图片: v7_Book-4_INQUIRY_p020_img00.jpeg, v7_Book-4_INQUIRY_p020_img01.jpeg

---

### 如何查询采购订单？

此功能用于查询采购订单及其详细信息。

进入采购订单日记账查询画面（Purchase Order Journal Enquiry）后，您可以查看：

采购订单类型（PO Type）：
- Normal PO（普通采购订单）
- Blanket PO（总括采购订单）：向供应商批量订购并按用户需求安排分次交货。

D/R Qty（交货申请数量）：
- 仅用于总括采购订单（Blanket PO）
- 表示交货申请单（Delivery Request）的数量
- 只有提出交货申请时，供应商才会安排交货

双击选定记录后，可查看采购订单详细画面（Purchase Order Detail Screen）：
- 抬头信息区（Header Info）：显示采购订单的基本信息。
- 其他与备注区（Others & Remarks）：显示附加信息。
- 商品折扣在明细项目输入画面中按商品级别设置（需勾选）。
- 发票折扣输入字段。
- 若有效期已过，收货操作可能会被拒绝。

还可查看商品信息管理画面（Item Information Management Screen）。

> 来源: v7 Book-4 Section 7.6 Page 17-19

> 相关图片: v7_Book-4_INQUIRY_p017_img00.jpeg, v7_Book-4_INQUIRY_p017_img03.jpeg, v7_Book-4_INQUIRY_p017_img04.jpeg, v7_Book-4_INQUIRY_p018_img00.jpeg, v7_Book-4_INQUIRY_p018_img01.jpeg, v7_Book-4_INQUIRY_p019_img00.jpeg

---

### 如何按会员查询销售备忘录？

此功能是会员视角的销售备忘录查询（Member Sales Memo Journal Inquiry），按会员过滤并以销售备忘录编号排序显示。

操作步骤：
1. 进入会员销售备忘录查询画面。
2. 系统按会员过滤并以销售备忘录编号排序显示。
3. 您可以查看特定会员的所有销售备忘录记录。

> 来源: v7 Book-4 Section 7.17 Page 35

> 相关图片: v7_Book-4_INQUIRY_p035_img00.jpeg, v7_Book-4_INQUIRY_p035_img01.jpeg, v7_Book-4_INQUIRY_p035_img02.jpeg

---

## 数据接口 (10 条)

### 如何查询CS2000出站接口日志？

CS2000出站接口日志查询（Outbound Interface Log Enquiry）用于查询出站接口更新日志历史记录。通过此查询画面，用户可以获取出站数据接口更新过程的详细更新日志历史，便于监控从ChainStore Plus向第三方系统导出的数据处理情况。

查询画面显示：
- 出站接口更新的历史记录
- 每次更新的处理状态
- 相关的时间戳和标识信息

> 来源: v7 Book-5 Section 8.3.3 Page 23

> 相关图片: v7_Book-5_ADMIN_p023_img00.jpeg

---

### 如何查询CS2000接口更新日志？

CS2000接口更新日志查询（Interface Update Log Inquiry）是专门为ChainStore Plus与第三方软件应用程序之间进行数据交换的接口模块。通过此查询画面，用户可以获取数据接口更新过程的详细更新日志历史记录。

查询画面将显示接口更新的历史记录，包括更新时间、更新类型、处理状态等信息，便于用户追踪数据接口的运行情况。

> 来源: v7 Book-5 Section 8.3.1 Page 21

> 相关图片: v7_Book-5_ADMIN_p021_img00.jpeg

---

### 如何查询CS2000接口过账错误？

CS2000接口过账错误查询（Interface Posting Error Enquiry）提供接口更新错误信息的查询画面。如果更新过程中发生错误，将显示错误的简要描述供用户参考。如果发现更新过程中的错误，可能需要用户进行数据恢复操作。

查询画面显示：
- 错误发生的时间
- 错误简要描述
- 相关的错误信息

用户可根据错误信息判断问题原因，并采取相应的数据恢复措施。

> 来源: v7 Book-5 Section 8.3.2 Page 22

> 相关图片: v7_Book-5_ADMIN_p022_img00.jpeg

---

### 如何设置和维护POS轮询点？

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

> 来源: v7 Book-5 Section 8.1.1 Page 5-7

> 相关图片: v7_Book-5_ADMIN_p005_img00.jpeg, v7_Book-5_ADMIN_p006_img00.jpeg

---

### 如何管理POS传输日志？

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

> 来源: v7 Book-5 Section 8.1.2 Page 8-10

> 相关图片: v7_Book-5_ADMIN_p008_img00.jpeg, v7_Book-5_ADMIN_p009_img00.jpeg, v7_Book-5_ADMIN_p010_img00.jpeg

---

### 如何查询POS传输日志更新状态？

POS传输日志更新查询（POS Transmission Log Update Inquiry）用于查询后台系统发送的POS数据更新状态。当POS收到来自后台的数据更新文件后，POS将在数据更新后发回更新状态消息至后台服务器。该返回消息将指示POS更新是否成功或发生错误。

进入查询画面后，您可以查看每个POS的更新状态记录，包括成功更新和失败的记录。

> 来源: v7 Book-5 Section 8.1.5 Page 16

> 相关图片: v7_Book-5_ADMIN_p016_img00.jpeg

---

### 如何查询POS传输日志更新错误？

POS传输日志更新错误查询（POS Transmission Log Update Error Inquiry）用于查询后台系统发送的POS数据更新错误状态。错误消息为用户提供有关POS更新错误的简要信息，后台用户可以根据这些信息采取适当的数据恢复措施。

错误查询画面显示：
- 错误信息摘要
- 相关的错误详情

系统管理员可根据错误消息判断问题原因，并决定是否需要进一步的数据恢复操作。

> 来源: v7 Book-5 Section 8.1.6 Page 17

> 相关图片: v7_Book-5_ADMIN_p017_img00.jpeg

---

### 如何启动和停止POS数据轮询？

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

> 来源: v7 Book-5 Section 8.1.3 Page 11-13

> 相关图片: v7_Book-5_ADMIN_p011_img00.jpeg, v7_Book-5_ADMIN_p012_img00.jpeg, v7_Book-5_ADMIN_p013_img00.jpeg

---

### 如何将主数据导出到POS？

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

> 来源: v7 Book-5 Section 8.2 Page 18-19

> 相关图片: v7_Book-5_ADMIN_p018_img00.jpeg, v7_Book-5_ADMIN_p018_img01.jpeg

---

### 如何查看POS轮询历史记录？

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

> 来源: v7 Book-5 Section 8.1.4 Page 14-15

> 相关图片: v7_Book-5_ADMIN_p014_img00.jpeg, v7_Book-5_ADMIN_p015_img00.jpeg

---

## 系统管理 (3 条)

### 如何控制POS数据过账过程？

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

> 来源: v7 Book-5 Section 9.1.1 Page 25-26

> 相关图片: v7_Book-5_ADMIN_p025_img00.jpeg, v7_Book-5_ADMIN_p026_img00.jpeg

---

### 如何查询POS日结记录？

POS日结查询（POS Day End Inquiry）用于记录各店铺的日结活动。POS日结是每日营业结束时由店铺POS人员执行的日常操作，用于结束当前营业日并准备下一个营业日。对于后台管理员来说，确保所有店铺按时正确完成此操作非常重要。

店铺完成日结后会自动向后台发送日结消息。如果没有收到某店铺的日结消息，可能意味着该店铺未完成日结流程，建议进一步调查。

查询画面显示字段：
- Date（日期）：日结日期。
- Time（时间）：日结时间。
- Location（位置）：日结店铺位置。
- Till（收银机编号）：POS的机器ID。
- Cashier（收银员）：收银员员工代码。
- Shift#（班次）：当班收银员员工代码。
- Sales（销售）：销售交易数量。
- Tfx（调拨）：库存调拨交易数量。
- Dep（订金）：订金交易数量。
- Serv（服务）：服务交易数量。
- Gift（礼品券）：礼品券交易数量。
- Gaway（赠品）：赠品交易数量。
- Redm（礼品兑换）：礼品兑换数量。
- Misc. Amount（杂项金额）：杂项收入金额。
- Total Amount（总金额）：总收入金额。
- Check（日结检查标志）：Y = 日结已验证，空白 = 日结未验证。

双击高亮行可查看日结交易明细：
- 点击"Payment"（付款）按钮查看付款详情，显示当日收到的付款方式。
- 点击"Count"（计数）标签查看当日交易数量。
- 点击"Amount"（金额）标签查看当日交易金额。
- 点击"Other"（其他）标签查看哪些交易有错误。

> 来源: v7 Book-5 Section 9.1.3 Page 28-32

> 相关图片: v7_Book-5_ADMIN_p028_img00.jpeg, v7_Book-5_ADMIN_p030_img00.jpeg, v7_Book-5_ADMIN_p030_img01.jpeg, v7_Book-5_ADMIN_p031_img00.jpeg, v7_Book-5_ADMIN_p031_img01.jpeg, v7_Book-5_ADMIN_p032_img00.jpeg

---

### 如何查询POS数据过账错误历史日志？

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

> 来源: v7 Book-5 Section 9.1.2 Page 27

> 相关图片: v7_Book-5_ADMIN_p027_img00.jpeg

---

