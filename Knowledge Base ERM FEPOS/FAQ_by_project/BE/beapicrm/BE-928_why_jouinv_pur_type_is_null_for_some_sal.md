---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "Dear @@Sang @@Jason Wu"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-928
resolved: 2025-01-10
fix-version: ""
---

# BE-928: Why jouinv_pur_type is null for some sales memo in CN DB

## 問題

Dear @@Sang @@Jason Wu
I checked DB found that some sales memo with  jouinv_pur_type is null,Is this normal?Could you help to double confirm and calarify the worflow for  jouinv_pur_type?
POS version: 72.0221.0102
1.jouinv_pur_type is not null in POS FE
2.We can see that pur_type all are null which memo linked deposit,void,return memo

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-01-10
### Jira Comments (11 則)
**Tovi Wang** (2024-10-30):
Dear @@Sang I sended 2024-10-01 logs for OC103 to you by teams.
@@Joy Li @@Jason_Lin FYI.
**Andrew_Au** (2024-12-24):
@@Tovi Wang Please update the ticket status
**Tovi Wang** (2025-01-03):
@@Sang May I know if anything update for this issue?
@@Andrew_Au @@Joy Li  FYI.
**Sang** (2025-01-06):
@@Tovi Wang @@Andrew_Au @@Joy Li @@Cy Lau @@Bobby Coach China SOW - Add Purchase Type 購買類型 Drop Down in POS Sales UI (KTS 220921 v720.01R19B). If User create a new sales memo, POS will auto assign default purchase type (defined in tblconfig.PURCHASETYPE_DEFAULT), and user can select other purchase type in Sales U if necessary.  If POS settle a deposit (deposit data have not define purchase type) with amendment, POS will remind user to select purchase type in sales UI before process to Payment page. However, if user settle deposit without amendment, POS will bypass sales UI and lead user direct to payment UI,  finally keep 'purchase type' value remain null in sales journal.
Propose solution: When User settle deposit, POS will assign default purchase type value (defined in tblconfig.PURCHASETYPE_DEFAULT), If user settle deposit directly without amendment, default purchase type will be used. Otherwise user can  use settle deposit with amendment method if need to amend data (include select other purchase type in Sales UI) .  Please comment
**Tovi Wang** (2025-01-06):
@@Sang  Many Thanks for your details clarify.
I think whether it's settled deposit memo, voided memo, or returned memo, if the store user hasn't manually selected the Purchase Type, it should be like
”create a new sales memo”, POS should auto assign default purchase type to them instead of remain them NULL.
@@Joy Li  @@Cy Lau  Please help to take a look if anything other concern.
**Sang** (2025-01-06):
@@Tovi Wang I can’t re-produce Voided and return Memo with null Purchase type value. Please copy OC103 Till 0 dbhist.sdf.
**Tovi Wang** (2025-01-06):
@@Sang OC103 Till 0 dbhist.sdf for your reference.
**Sang** (2025-01-06):
@@Tovi Wang @@Andrew_Au void memos in FE dbhist.sdf has purchase type value. Please check PCD records also.
**Sang** (2025-01-06):
@@Tovi Wang @@Andrew_Au
Check OC103 DB void Memo has Purchase type value.
PCD indicated that OC103 Till 0 still use v72. In v72 if tblconfig.DotnetPCD='N' ,VB6 PCD library does not able to write Purchase type (please check OC103).  when Upgrade to v75,  POS auto use dotnetPCD and this issue can be fixed.
**Sang** (2025-01-09):
@@Tovi Wang @@Andrew_Au Fixed: Direct Settle Deposit - Write default Purchase type value (KTS 250106 Jira BE-928 v750.05, v750.04R10)
**Tovi Wang** (2025-01-09):
@@Sang Many Thanks for your double confirm.
@@Andrew_Au I think we can closed this Jira first.

## 相關資訊

- Jira: [BE-928](https://ctil.atlassian.net/browse/BE-928)
- Fix Version: 未記錄
- 解決日期: 2025-01-10
