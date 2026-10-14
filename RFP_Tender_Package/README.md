# 5G Fixed Wireless Access (FWA) — Complete Turnkey Tender Package
## Band n50 (1.5 GHz TDD, 60 MHz) — 5,000 Sites Nationwide Rollout

**Document Control Code:** RFP-TELTECH-FWA-2026-001  
**Project Owner:** Telecommunications Technology Solutions Incorporated (TelTech)  
**Author:** OLIVER TUNGOL
**Date of Release:** October 14, 2026  
**Document Status:** Complete Single Source of Truth (SSOT) Tender Issue  

---

## 1. Directory Structure of the Tender Package

All official tender artifacts have been compiled, standardized, and saved directly into the project repository under [`RFP_Tender_Package/`](file:///Users/olivertungol/Downloads/FWA%20Project%20DL/RFP_Tender_Package):

```
RFP_Tender_Package/
├── 00_RFP_5G_FWA_Tender_Invitation_and_Transmittal_Letter.md
│   └── Commercial transmittal letter and invitation to bid with high-impact scope and timeline
├── 01_RFP_5G_FWA_Master_Tender_Document.md
│   └── Complete Request for Proposal specification (Scope, Rules, Phasing, Governance, Evaluation)
├── 02_Appendix_A_Technical_Specifications_Compliance_Matrix.md
│   └── Line-by-line compliance matrices for RAN, Power, 5GC Core, OSS/BSS, RF Planning, MS, CPE
├── 03_Appendix_B_Commercial_Proposal_BoQ_Templates.md
│   └── Turnkey Bill of Quantities (BoQ) templates, pricing caps, and Vendor Financing Form D
├── 04_Appendix_C_SLAs_KPIs_Liquidated_Damages.md
│   └── 3GPP and ITU best-practice network KPIs, availability SLAs, MTTR tiers, liquidated damages
├── 05_Appendix_D_Site_Survey_RF_Planning_Civil_Power_Guidelines.md
│   └── Siting rules, TSSR formats, Band n50 link budget, monopole engineering, SSV acceptance
└── 06_RFP_Commercial_Price_Book_and_BoQ_Template.xlsx
    └── Production-grade 8-tab Excel Price Book with dynamic formulas and pre-formatted headers
```

---

## 2. Summary of Tender Scope by Lot

| Lot Ref | Subsystem Domain | Technical Sizing & Scope Description | Primary Engineering Architecture |
| :--- | :--- | :--- | :--- |
| **LOT 1** | **Radio Access Network (RAN)** | 3-sector 8T8R Massive MIMO, 60 MHz Band n50 (1432–1517 MHz TDD), 320W total RF power/sector, high-gain antennas, BBU subracks, and full turnkey site deployment services. | Turnkey supply, delivery, rigging, installation, commissioning, and single site verification (SSV). |
| **LOT 2** | **Power & Passive Infrastructure** | Modular 6.0 kW switchmode DC rectifier plant (N+1 redundancy), Lithium Iron Phosphate (LFP / LiFePO4) energy storage (>= 4h autonomy @ 3 kW load), and hybrid backup. | TowerCo co-location tap-off & metering (Phase 1 priority) and Greenfield off-grid power solutions (15 kVA genset, ATS, 30m monopole). |
| **LOT 3** | **Cloud-Native 5G Core (5GC SA)** | Cloud-native 3GPP R16/17 Standalone 5G Core, distributed DPDK UPF nodes (80 Gbps throughput per node), high-capacity inline CG-NAT, DPI, and subscriber management. | Dual Geo-Redundant Active-Active Datacenters (NCR Primary + Clark DR) supporting 1.0M initial registered subscribers with seamless expansion. |
| **LOT 4** | **Converged Digital OSS/BSS** | Converged digital CRM, product catalog, real-time Converged Charging Function (CHF), prepaid rating engine, omnichannel payment gateway integration, and field force automation. | Cloud-native microservices architecture, automated work-order dispatch (3,500 daily tasks), real-time GCash/Maya top-up processing. |
| **LOT 5** | **RF Planning & Optimization** | High-precision propagation modeling, candidate search rings, drone TSSR, SSV acceptance, cluster drive tests, and continuous interference mitigation. | Target RSRP >= -95 dBm across >= 90% settlement area, nominal 3.5 km coverage radius per macro site. |
| **LOT 6** | **Managed Services & 24/7 NOC** | End-to-end 24/7 Tier-2/Tier-3 Network Operations Center (NOC) monitoring, First Line Maintenance (FLM), Field Force Dispatch, and nationwide corrective repair. | Strict SLA benchmarks: Severity 1 MTTR <= 2h Urban / <= 4h Rural, 99.70% radio network availability, Next-Business-Day (NBD) depot spares turnaround. |
| **LOT 7** | **5G FWA High-Gain CPE** | High-performance indoor and outdoor 5G FWA terminals, Band n50 native support, integrated directional antennas (8–10 dBi), Wi-Fi 6 AX1800, 2.5GE LAN. | 350,000 units in Phase 1 deployment; TR-069 / TR-369 USP remote management, Operator PLMN SIM lock, and OTA firmware upgrade capability. |
| **FORM D** | **Mandatory Vendor Financing** | Comprehensive OEM vendor financing facility covering at least 80% of Capex, 4-to-5 year tenor, and a minimum 12-month grace period on principal repayment. | Capital structure optimization to conserve working capital during initial rollout and align debt service with commercial broadband revenue generation. |


## 3. Best-Practice Service Level Agreements (SLAs) & Network KPIs

The tender document enforces carrier-grade SLAs benchmarked against 3GPP and ITU-T standards:

```
+----------------------------------------------------------------------------------------------------+
| Performance Domain       | Key Metric Name                  | Minimum Threshold | Target Excellence |
+----------------------------------------------------------------------------------------------------+
| Radio Access Network     | Radio Network Availability       | >= 99.70%         | >= 99.95%         |
|                          | Call/Session Setup Success (CSSR)| >= 99.00%         | >= 99.60%         |
|                          | Call/Session Drop Rate (CDDR)    | <= 0.50%          | <= 0.15%          |
|                          | Single-Sector Peak DL Throughput | >= 380 Mbps       | >= 450 Mbps       |
|                          | Cell-Edge User DL Speed (5th %) | >= 25 Mbps        | >= 50 Mbps        |
|                          | End-to-End Latency (RTT)         | <= 30 ms          | <= 18 ms          |
+----------------------------------------------------------------------------------------------------+
| Power & Site Resilience  | Site Power Continuous Uptime     | >= 99.85% (Green) | >= 99.95% (Leased)|
|                          | Lithium Battery Autonomy         | >= 4.0 Hours      | >= 5.0 Hours      |
|                          | Earth Grounding Resistance       | <= 5.0 Ohms       | <= 3.0 Ohms       |
+----------------------------------------------------------------------------------------------------+
| 5G Core & Datacenter     | Control Plane NF Availability    | >= 99.999%        | "Five Nines"      |
|                          | User Plane Forwarding Latency    | <= 1.5 ms         | <= 1.0 ms         |
|                          | Geo-Redundant DC Failover Time   | <= 30 Seconds     | Hitless Failover  |
+----------------------------------------------------------------------------------------------------+
| Operations & Dispatch    | Field Installation Lead Time     | <= 48 Hours       | <= 24 Hours       |
|                          | First-Time-Right (FTR) Installs  | >= 94.0%          | >= 96.0%          |
|                          | Churn CPE Hardware Recovery Rate | >= 65.0%          | >= 70.0%          |
|                          | Severity-1 Critical MTTR         | <= 4h (Rural)     | <= 2h (Urban)     |
+----------------------------------------------------------------------------------------------------+
```

---

## 4. Key Input Decisions & Data Needed to Finalize the Issuance

While the tender specification and dynamic BoQ are complete and ready for distribution, the following specific commercial decisions from executive management can be inserted prior to publication:
1. **Target Bidder Shortlist:** Confirm whether tender invitations will be open public international or restricted to pre-selected Tier-1 OEMs (e.g., Ericsson, Nokia, Huawei, ZTE, Samsung, Mavenir for Core/RAN; Cerillion, Comarch, Alepo, Amdocs for BSS; MIDC, EdgePoint for TowerCo).
2. **TowerCo Colocation Boundary:** Confirm whether passive power (rectifiers/batteries) will be procured via Lot 2 across all sites or if TowerCos (PTCI/MIDC, EdgePoint) will provide DC power as an all-inclusive managed utility service.
3. **Spectrum User Fee (SUF) Treatment:** Clarify in the vendor financing covenant whether the statutory ₱300M/year SUF is kept entirely as an operator expense or factored into vendor-backed working capital lines.
4. **Tender Bond & Performance Security:** Confirm if standard bank guarantee bonds (e.g., 2% Bid Bond, 10% Performance Bond) match corporate treasury requirements.
