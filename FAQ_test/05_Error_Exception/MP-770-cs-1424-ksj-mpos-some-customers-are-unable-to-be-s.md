---
project: MP
issue_key: MP-770
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-770
created: '2025-05-07'
resolved: '2025-07-04'
fix_version: API-3.23.2-v1a_KSJ
components:
- MPOS API
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
---
MP-770: KSJ MPOS : Some customers are unable to be selected on mPOS

| 問題
日本 KSJ mPOS 試行店舖中，部分顧客可透過手機號碼或 Customer ID 成功搜尋到會員資料，但在選擇該顧客以附加至交易時，系統回傳錯誤「400 Invalid customer type（無効な顧客タイプです）」。同一店舖中部分會員正常、部分會員失敗，QA 環境則無法重現此問題。

| 根因
mPOS 的 GetMember 流程在 C360 查詢會員後，會對會員類型進行驗證，而驗證依據為本地 [dbMas].[dbo].[TblVipTyp] 資料表。PRD 環境的 TblVipTyp 表中缺少部分 C360 回傳的會員類型，導致驗證失敗並回傳「Invalid customer type」。此外，當 EnableVerifyBirthday=Y 時，會觸發此驗證路徑，進一步曝露此問題。

| 解法
修正 mPOS 的 GetMember 流程，使其與 FEPOS 行為一致：當從 C360 取得會員資料但本地 TblVipTyp 缺少對應會員類型時，改以本地暫存會員方式處理，不再強制驗證失敗。修復版本：API-3.23.2-v1a_KSJ（於 2025-07-04 發佈）。

| 相關資訊
- Jira: [MP-770](https://ctil.atlassian.net/browse/MP-770)
- Fix Version: API-3.23.2-v1a_KSJ
- 解決日期: 2025-07-04
- 組件: MPOS API
- 負責人: Sherman tse
- 附件: [202506121100070000.mp4](https://ctil.atlassian.net/rest/api/3/attachment/content/59439) | [C309-Unknown-2025-06-12 10-58-23-704495.txt](https://ctil.atlassian.net/rest/api/3/attachment/content/59438) | [CS-1424.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/56223) | [CS-1424 (d81e9193-4e27-44e8-b42e-be48daca0dcd).zip](https://ctil.atlassian.net/rest/api/3/attachment/content/59492) | [image-20250507-115610.png](https://ctil.atlassian.net/rest/api/3/attachment/content/56218)