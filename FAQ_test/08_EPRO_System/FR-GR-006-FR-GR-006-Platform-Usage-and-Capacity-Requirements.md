---
title: "FR-GR-006: FR-GR-006: Platform Usage and Capacity Requirements"
tags: [epro, EPRO_System]
---

# FR-GR-006: FR-GR-006: Platform Usage and Capacity Requirements

## 需求描述

Requirement ID:	FR-GR-006	Requirement Type:	General Requirements
Parent Requirement #:
None
Description:
3.1.6	The estimated usage of the Platform is as follows:
Approximately 21,000 low-value purchases, 3,650 RFQ and 250 tenders to be handled per year.
Approximately 4 suppliers will be invited on average for each RFQ / tender exercise, with the possibility of inviting a higher number up to 8 suppliers in certain cases.
Estimated 50 users, including HKTDC staff and external suppliers, will be using the Platform concurrently.
Estimated 500 HKTDC staff for named user license.
Able to support concurrently performance of 15 tenders and 300 RFQ (at different stages).
Approximately 10,000 suppliers are currently maintained on FMS Supplier Platform and shall be registered onto the Platform by stages upon launch.
Approximately 50 new supplier registration on average per month.
The average size of tender invitation documents shall be 15MB, while the average size of proposals received shall be 100MB.
Note: The procurement activities to be carried out within the Platform shall include RFQ, tenders, waivers, variation orders, low-valued purchase and purchase of items on the exemption list. Quotation exercises are not mandatory for low-valued purchases and the purchase of items on the exemption list.
3.1.7	The Contractor shall perform necessary stress testing to ensure the capability of the Platform will meet the estimated usage as stated in Section 3.1.6.
Rationale:
None
Acceptance / Fit Criteria:
Data sizing: The Platform should be designed to accommodate a 5% annual growth rate in the volume of low-value purchases, RFQs, and Tenders, while maintaining all related documents online for 7 years with audit trails. Documents older than 7 years will be archived with HKTDC confirmation for purge.
Supplier records: The Platform should be capable of handling the existing supplier records plus an additional 50 new suppliers per month, ensuring that all supplier records remain available online without purging.
System logs: The system logs, including access and error logs, will be automatically purged after 6 months to maintain data integrity and compliance.
Platform capacity: The platform should accommodate 50 users, enabling a designated number of simultaneous user accesses for Internal Users to manage 15 tenders and 300 RFQs at various stages. For External Suppliers, an average of 4 suppliers should be invited for each RFQ/tender exercise, with the possibility of inviting up to 8 suppliers in exceptional circumstances.
Stress testing: The stress testing method and acceptance criteria will be documented and reviewed during the subsequent SA&D stage to ensure the system's resilience and performance under various loads and scenarios.
Dependencies:
None
Tailoring Guidelines:
None
Change History:
None