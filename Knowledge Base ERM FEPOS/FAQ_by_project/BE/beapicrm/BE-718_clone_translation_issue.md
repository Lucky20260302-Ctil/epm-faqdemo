---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Env: [https://172.16.138.101/chainstoreplus/home](https://172.16.138.101/chainstoreplus/home)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-718
resolved: 2023-02-21
fix-version: ""
---

# BE-718: CLONE - Translation issue

## 問題

Env: [https://172.16.138.101/chainstoreplus/home](https://172.16.138.101/chainstoreplus/home)
The following words are still displaying as English under Chinese Tradition condition
Lang: 繁中
**Location: Home page**
1. 
2. 
3. 
4. 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
5.  Setting panel > Theme  主題
- 
- 
6. Save Changes? Yse/No/Cancel 儲存更變? 是/否/取消
**Home page >colunm: Table maintenance**
Primary  主表格
1. ~~Nationality (By Display Sequence)   國籍 (以顯示為排列)~~
副表格 (可選項表格)
1. ~~Tax Free Products Exclusion Table  非免稅產品~~
~~2. Denomination Face Value Table  面值表~~
~~3. Secondary Tax Free Eligible Products Table 第二合資格貨品免稅表~~
~~4. Sales staff password restricted keyword 員工密碼限制關鍵字~~
~~5. Sales staff password Policy Table Maintenance 員工密碼設定規則~~
~~6. Sub Color 副顏色~~
~~7. Delivery Time Slot 送貨時間表~~
~~8. Notification Code 通知碼~~
Specials (Custom):
~~1. Associate Store Code Maintenance 相關店舖代碼表格~~
**Home page >colunm: Master Maintenance**
~~Member Master~~
~~1. Member Managemant Maintenance 會員管理表格~~
~~Price Promation > Promotion Mix & Match~~
~~1. Item  x MM Event(s) Match-Up Process   貨品與促銷活動配搭程序~~
**Home page >colunm: Process**
~~1. Order Form Process     訂單表格程序~~
~~2. Online Order Reserve Process 線上貨品預訂~~
~~3. Online Order Invoice Generation 線上訂單發票生成~~
~~4. Print Onlline Order Invoive & Delivery Note 列印線上訂單發票及送貨紀錄~~
~~5. Online Order Delivery Note Return 退回線上訂單送貨紀錄~~
**Home page >colunm: Inquiry**
1. 
2. 
3. 
**Home page >colunm: Data Interface**
數據輸出
~~1. Outbound Interface Log Enquiry  向外界面紀錄查詢~~
~~2. Define Account Code for Accounting Interface 為會計界面定義帳戶編碼~~
**Home page >colunm: Administration**
~~1. Month End process 月結處理~~
~~2. 清除歷史記錄 > Purge Transaction History 清除交易記錄~~
~~3. Journal Anendment 日誌修改 > Journal Amendment Log Enquiry 日誌修改記錄查詢~~
~~4. Manual User Unlock 手動用戶解鎖~~
~~5. User Group Access Listing 用戶群組存取列表~~
~~6.  Company File 公司檔案~~
~~7. Global B.P. sync process全球B.P.同步程序~~
~~8. System Configuration Maintenance 系統設置列表~~
~~9. Global System Configuration Maintenance  全球系統設置列表~~
Detail page of some tabs still show English in Tradition Chinese mode
**Location:  Detail page of some programs**
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 
10. 
11. 
12. 
13. 
14. 
15. 
16. 
17. 
18. 
19. 
20. 
21. 
22. 
23. 
24. 
25. 
26. 
27. 
28. 
29. 
30. 
31. 
32. 
33. 
34. 
35. 
36. 
37. 
38. 
39. 
40. 
41. 
42. 
43. 
44. 
45. 
46. 
47. 
48. 
49. 
50. 
51. 
52. 
53. 
54. 
55. 
56. 
57. 
58. 
59. 
60. 
61. 
62. 
63. 
64. 
65. 
66. 
67. 
68. 
**When Mouse hovers over some icon:** (Ref: 4.png) (Ref: 7.png) (Ref: 13.png)
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
**Some programs are available to edit rows.**
- 
**Description in Docoument Queue Management still show in English** (Ref: 6.png)
**Words in button of "Show/Hide/Reorder Columns"** (Ref: 8.png)
**Tittle of all Selection list** (Ref: 9.png)
**Field of "This is mandatory". It should be show as 必須輸入** (Ref: 10.png)
**Click "<" would pop up "Top of file is reached"** (Ref: 11.png)
**RC1000 Click one of the info: Print receive Report > Still show English "By Input Sequence"** (Ref:12.png)
**Most of txt file in print queue are using English under TC condition** (Ref:14.png)
**Still pop up English "Validate Successful" after Click 審核** (Ref: 15.png)
**SE9006 Click one of the info: all options still display in English** (Ref: 16.png)
**Words next to tick box / drop dorwn list in MX9009** (Ref17.png)
**MF2003  Click one of the info: Edit Additional Price** (Ref: 18.png)
**DO1002** **Click one of the info: Print DO-Stk In** (Ref: 19.png)
**SE1001** **Click one of the info: Trabfer Detail Enquiry** (Ref: 20.png)
**SE9012 Click on Day end report >  Day end report shown as English** (Ref: 21.png)
**Some pop up Dialog still using English:**
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 
10. 
11. 
12. 
13. 
14. 
15. 
**Whole page of some programs still using English:**
Location Grouping Control Maintenance (MX0003)
~~Purchase Order Maintenance (PO3000) > Click Create~~
Vendor Delivery Note Information (RC2001) > Click Create
Stock Receive Confirmation Process (RC1000) > Click Create
Stock Receive Information (RC4000) > Click into one of the record
Create Delivery Order From Transfer (IC2008)
Delivery Order Journal Enquiry (SE2015) > Click into one of the record
On Sale Price Maintenance (Group Mode) (MF3006) > Click Create
from Stock On-Hand By Item (SE1001) >Click into one of the record > To Item Distribution Inquiry (SE1003)/ Item Distribution Summary Inquiry (SE1005)/ Quantity Status Inquiry (SE1002)/ Item Master Maintenance (MF0001)/ On Sale Price Enquiry (SE4007)/ Item Transfer Detail Enquiry (SE1006)/ Item Reserved Enquiry (SE2000)/ Item On Order Detail Enquiry (SE1008)
Purchase Receive Enquiry (RC5001) > Click into one of the record
**Parts of tables are still using English:**
1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 
10. 
11. 
12. 
13. 
14. 
15. 
16. 
17. 
18. 
19. 
20. 
21. 
22. 
23. 
24. 
25. 
26. 
27. 
28. 
29. 
30. 
31. 
32. 
33. 
34. 
35. 
36. 
37. 
38. 
39. 
40. 
41. 
42. 
43. 
44. 
45. 
46. 
47. 
48. 
49. 
50. 
51. 
52. 
53. 
54. 
55. 
56. 
57. 
58. 
59. 
60. 
61. 
62. 
63. 
64. 
65. 
66. 
67. 
68. 
69. 
70. 
71. 
72. 
73. 
74. 
75. 
76. 
77. 
78. 
79.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-02-21

## 相關資訊

- Jira: [BE-718](https://ctil.atlassian.net/browse/BE-718)
- Fix Version: 未記錄
- 解決日期: 2023-02-21
