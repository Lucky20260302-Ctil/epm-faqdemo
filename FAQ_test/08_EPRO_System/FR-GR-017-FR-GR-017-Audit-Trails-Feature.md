---
title: "FR-GR-017: FR-GR-017: Audit Trails Feature"
tags: [epro, EPRO_System]
---

# FR-GR-017: FR-GR-017: Audit Trails Feature

## 需求描述

Requirement ID:	FR-GR-017	Requirement Type:	General Requirements
Parent Requirement #:
None
Description:
3.1.20	The Platform shall support a detailed trail log that records all login activities and other actions performed by both Internal Users and external suppliers. The Contractor shall provide a mechanism to maintain all audit trail information, including the creation / update / deletion of individual records, along with the date, time, user involved, action taken and contents. This shall allow instant checking of the audit trail information on the Platform and the generation of summary reports for a particular purchase exercise. All records shall be retained for a period of 7 years from the date of occurrence. Upon expiry of 7 years, the historical vendor and quotation information shall be either purged or masked. Please refer to Part 2 - Technical Specifications for details.
Rationale:
None
Acceptance / Fit Criteria:
For data retention, refer to FR-GR-001 Platform Usage Estimates and Capacity Requirements.
The Platform must include a change history feature for all request e-Forms. The Platform should automatically log each field, capturing the date and time of the change, details of the changer, the modified field, and the old and new values whenever a save or submit action is performed. Additionally, the change history should also record a summary of changes with each save, manually filled out by the preparer.
< Screen mock-ups will be provided in the later SA&D stage >
The Platform must offer an action history feature for all request e-Forms. This feature should capture every status change of the e-Forms, detailing the date, time, initiator, and the new status.
< Screen mock-ups will be provided in the later SA&D stage >
The Platform must include an approval history feature for all request e-Forms that require approval. The approval history should monitor changes in the overall approval status, recording the date, time, and last approver. It should also log individual actions, capturing the date, time, person's name, action taken (e.g., approve, reject, re), reasons or remarks provided, and attachments if needed.
< Screen mock-ups will be provided in the later SA&D stage >
The Platform shall successfully perform all the actions outlined in the Use Case 12.13-16.
Dependencies:
FR-GR-006 Platform Usage and Capacity Requirements
Tailoring Guidelines:
None
Change History:
None