---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "Current Gender field = M/ F/ C-Couple"
root-cause: "待提取"
solution: "### Jira Comments (2 則)"
jira: BE-1264
resolved: 
fix-version: ""
---

# BE-1264: [CS-2705] ANZ - Make "Gender" as optional when create new member

## 問題

Current Gender field = M/ F/ C-Couple
Enhance programs for configurable gender option.
Coverage:
1. 
2. 
3. 
4.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (2 則)
**Joy Li** (2026-05-11):
Copy from @@Cy Lau
最基本for UI :
JSON  :
{
"display" : 
{
  "zh-hk" : "",
  "zh-tw" : "",
  "zh-cn" : "",
  "kr" : "",
  "jp" : "",
  "default" : ""
},
"value" : "M"
}
**Joy Li** (2026-05-19):
<u>**Phase_1: R41**</u>
FE:
Member UI display (All regions)
PCD generate (All regions)
Member create\upsert process (All regions)
MPOS:
Member UI display (All regions)
PCD generate (All regions)
Member create\upsert process (All regions)
BE:
posting (All regions)
VIP searching (All regions)
CAR Interface (All regions) - Need to check with downsteam.
C360Interface (AU NZ KSJ KAU KNZ) - Need to check with downsteam.
WEB:
C360 POS_API (AU NZ KSJ KAU KNZ)
<u>**Phase 2: (TBC)**</u>
BE:
Memberson Interface (KSG, KMY)
Acxiom CRM Interface (HK CN SG MY TW MO KR)
WEB:
eName (HK MO KR JP)
BEAPICRM API (HK CN SG MY TW MO KR)
Memberson API (KSG KMY)

## 相關資訊

- Jira: [BE-1264](https://ctil.atlassian.net/browse/BE-1264)
- Fix Version: 未記錄
- 解決日期: 未記錄
