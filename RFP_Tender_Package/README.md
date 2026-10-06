# 5G Fixed Wireless Access (FWA) — Complete Turnkey Tender Package
## Band n50 (1.5 GHz TDD, 60 MHz) — 5,000 Sites Nationwide Rollout

**Document Control Code:** RFP-TELTECH-FWA-2026-001  
**Project Owner:** Comclark Network & Technology Corp. / Telecommunications Technology Solutions Inc. (TelTech)  
**Author & Lead Architect:** OLIVER TUNGOL
**Date of Release:** October 6, 2026  
**Document Status:** Complete Single Source of Truth (SSOT) Tender Issue  

---

## 1. Directory Structure of the Tender Package

All official tender artifacts have been compiled, standardized, and saved directly into the project repository under [`RFP_Tender_Package/`](file:///Users/olivertungol/Downloads/FWA%20Project%20DL/RFP_Tender_Package):

```
RFP_Tender_Package/
├── 01_RFP_5G_FWA_Master_Tender_Document.md
│   └── Complete Request for Proposal specification (Scope, Rules, Phasing, Governance, Evaluation)
├── 02_Appendix_A_Technical_Specifications_Compliance_Matrix.md
│   └── Line-by-line compliance matrices for RAN, Power, 5GC Core, OSS/BSS, RF Planning, MS
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

| Lot Ref | Subsystem Domain | Baseline Benchmark / Technical Sizing | Primary Reference / Strategy |
| :--- | :--- | :--- | :--- |
| **LOT 1** | **Radio Access Network (RAN)** | **$75,000 USD** BTS hardware ($12k BBU, $48k RRUs, $10.5k Antennas, accessories) + **$15,900 USD** Turnkey Rollout Services = **$90,900 USD / site** | 3-sector 8T8R MIMO, 60 MHz Band n50 (1432–1517 MHz), 320W RF power/sector. |
| **LOT 2** | **Power & Passive Infrastructure** | **$4,500 USD** 6.0 kW DC Rectifier + **$3,500 USD** 150Ah LiFePO4 battery ($\ge 4\text{h}$ autonomy). Greenfield sites add **$4,000 USD** 15kVA genset + **₱3.5M PHP** 30m monopole. | Leased TowerCo co-location ($73.1\%$ Phase 1) vs. Greenfield monopole ($9.3\%$ nationwide). |
| **LOT 3** | **Cloud-Native 5G Core (5GC SA)** | **$9.72M USD** Year 1 turnkey package ($4.38M HW + $5.34M for 1M subscriber perpetual capacity). Incremental capacity @ $\le \$4.00$ / sub. | Dual Active-Active Datacenters (NCR Primary + Clark DR), 80 Gbps DPDK UPF nodes, inline CG-NAT & DPI. |
| **LOT 4** | **Converged Digital OSS/BSS** | **$13.91M USD** Year 1 turnkey stack ($4.2M SI, $2.6M CRM/Catalog, $1.1M CHF real-time charging, $1.5M Fault/Perf OSS, $700k FMS). | Prepaid-first, direct Nchf rating, GCash/Maya/7-Eleven API integration, automated dispatch for 3,500 daily work orders. |
| **LOT 5** | **RF Planning & Optimization** | High-precision propagation modeling, candidate search rings, drone TSSR, SSV acceptance, cluster drive tests. | Target RSRP $\ge -95\text{ dBm}$ across $\ge 90\%$ settlement area, $3.5\text{ km}$ nominal cell radius. |
| **LOT 6** | **Managed Services & 24/7 NOC** | **₱120,000 PHP / site / month** ($2,182 USD/mo; $26,182 USD/site/yr) full active telecom operations. | 24/7 Tier-2/Tier-3 NOC, First Line Maintenance (FLM), MTTR $\le 2\text{h}$ Urban / $\le 4\text{h}$ Rural, NBD spares delivery. |
| **LOT 7** | **5G FWA High-Gain CPE** | Target cap **$\le \$55.00$ USD / unit** for indoor Wi-Fi 6 AX1800 terminals with high-gain (8–10 dBi) Band n50 antennas. | 350,000 units in Phase 1; TR-069 / TR-369 USP remote management, PLMN SIM lock. |
| **FORM D** | **Mandatory Vendor Financing** | **80% of Capex financed**, 20% downpayment, 4-to-5 year tenor, 12-to-18 month grace period, $\le 6.50\%$ interest. | Conserves over **$52.4M USD** in Day-1 cash outflows, shrinking peak funding deficit to self-sustainability. |

---

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
|                          | Cell-Edge User DL Speed (95th %) | >= 25 Mbps        | >= 50 Mbps        |
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
