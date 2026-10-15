# APPENDIX B: COMMERCIAL PROPOSAL, BILL OF QUANTITIES (BOQ) & PRICING TEMPLATES
## 5G FWA PROGRAM (5,000 SITES NATIONWIDE)

**Tender Reference:** RFP-TELTECH-FWA-2026-001  
**Project:** Nationwide 5G FWA Project (Band n50, 60 MHz TDD)  
**Operator:** Telecommunications Technology Solutions Incorporated (TelTech)  
**Issuing Body:** Technical Evaluation Board  

*Instructions to Bidders: Complete all unit rates in USD ($) and Philippine Pesos (PHP ₱ at baseline FX 55.00) using the official Excel BoQ file (`06_RFP_Commercial_Price_Book_and_BoQ_Template.xlsx`). All prices must be firm, fixed, and valid for 180 days.*

---

### TABLE 1: LOT 1 — RAN HARDWARE & ACCESS EQUIPMENT (PER SITE BASIS)

| Item Ref | Equipment Description | Technical Sizing / Model | Qty per Site | Unit Price (USD) [Bidder to Quote] | Total Price per Site (USD) | Remarks / Bidder Model |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **RAN-HW-01** | **5G Baseband Unit (BBU)** | 19" subrack, dual -48V DC PSU, 4x 25G backhaul, 6x 25G eCPRI | 1 set | `[Bidder Quote]` | `[Formula = Qty * Rate]` | Specify model & datasheet |
| **RAN-HW-02** | **8T8R Remote Radio Unit (RRU)** | Band n50 (1.5 GHz), 60 MHz IBW, 8x40W (320W total RF power) | 3 sets | `[Bidder Quote]` | `[Formula = Qty * Rate]` | 3 Sectors per site |
| **RAN-HW-03** | **Macro High-Gain Antennas** | 8-port cross-pol, 17.5 dBi gain, AISG 2.0 internal eRET | 3 sets | `[Bidder Quote]` | `[Formula = Qty * Rate]` | Or integrated AAU option |
| **RAN-HW-04** | **RF Jumpers & Optical Patchcords** | High-grade armored optical fiber, weatherproof boots, grounding kits | 1 lot | `[Bidder Quote]` | `[Formula = Qty * Rate]` | All accessories included |
| **RAN-HW-05** | **BBU Base Software & 5G Features** | Band n50 carrier license, MU-MIMO, beamforming, sleep-mode energy saving | 1 lot | `[Bidder Quote]` | `[Formula = Qty * Rate]` | Perpetual base software |
| **SUBTOTAL** | **BTS Equipment Package per Site** | *(BBU x1, 8T8R RRU x3, Antennas x3, SW)* | **1 Site** | — | **`[Sum of Items HW-01 to HW-05]`** | *Total BTS Hardware* |

---

### TABLE 2: LOT 1 — RAN TURNKEY ROLLOUT SERVICES (PER SITE BASIS)

| Item Ref | Service Description | Scope of Work | Qty per Site | Unit Price (USD) [Bidder to Quote] | Remarks / Methodology |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **RAN-SVC-01** | **Site Survey, Engineering & TSSR** | Tower audit, structural verification, drone LOS photo sweep, civil sketch | 1 site | `[Bidder Quote]` | Field survey report delivery |
| **RAN-SVC-02** | **Project Management & Mobilization** | Dedicated rollout PMO, site acquisition coordination, milestone tracking | 1 site | `[Bidder Quote]` | Dedicated PM team |
| **RAN-SVC-03** | **Installation & Commissioning (I&C)** | Rigging, antenna mounting, cable routing, BBU wiring, initial power-up | 1 site | `[Bidder Quote]` | Civil and telecom I&C |
| **RAN-SVC-04** | **Single Site Optimization (SSO/SSV)** | Station testing, sector drive test, throughput call, ping, handover test | 1 site | `[Bidder Quote]` | SSV acceptance sign-off |
| **RAN-SVC-05** | **Cluster Optimization Services** | Cluster tuning, inter-site interference, tilt adjustments (per site share) | 1 site | `[Bidder Quote]` | Cluster drive testing |
| **RAN-SVC-06** | **Central Warehousing & Logistics** | Staging, asset tagging, kitting, indoor climate storage | 1 site | `[Bidder Quote]` | Inventory management |
| **RAN-SVC-07** | **Delivery & Basic Hauling to Site** | Regional hauling, rough-road 4x4 transport to rural barangay location | 1 site | `[Bidder Quote]` | Complete site delivery |
| **SUBTOTAL** | **RAN Turnkey Services per Site** | *Full Turnkey Rollout & Commissioning Services* | **1 Site** | **`[Sum of Items SVC-01 to SVC-07]`** | *Total Turnkey Services* |

> **Total Day-1 RAN Capex per Site (Equipment + Turnkey Services):** `[Sum of Hardware + Turnkey Services]`  
> **Phase 1 Program Total (1,000 Sites):** `[Total per Site * 1,000]`

---

### TABLE 3: LOT 2 — POWER SYSTEMS & PASSIVE INFRASTRUCTURE

| Item Ref | System Description | Technical Sizing | Application | Unit Price (USD) [Bidder Quote] | Unit Price (PHP @ 55 FX) |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **PWR-EQ-01** | **12.0 kW Modular DC Rectifier Plant** | 19" 3U subrack, 4 x 3.0 kW modules (N+1), SMPS controller | Co-loc / Greenfield | `[Bidder Quote]` | `[Formula = USD * 55]` |
| **PWR-EQ-02** | **48V LiFePO4 Battery Bank** | High-cycle LFP with smart BMS, sized for >= 12.0 kWh usable energy over 4.0h @ 3.0 kW load, <= 80% DoD, 80% SoH (min >= 20.0 kWh nominal installed bank capacity, min 400 Ah @ 48V, loss-based calculation) | Co-loc / Greenfield | `[Bidder Quote]` | `[Formula = USD * 55]` |
| **PWR-EQ-03** | **TowerCo DC Tap-Off & Metering Kit**| DC tap enclosure, revenue Class 1.0 kWh meter, SPD Type 2 | Leased TowerCo | `[Bidder Quote]` | `[Formula = USD * 55]` |
| **PWR-EQ-04** | **15 kVA Diesel Generator Set** | Soundproof canopy, 500L–1000L tank, ATS, auto-start | Greenfield (Class T4) | `[Bidder Quote]` | `[Formula = USD * 55]` |
| **SUBTOTAL** | **Lot 2 Power Systems Turnkey Total** | *Total Phase 1 Capital Expenditure for Lot 2 Power Systems* | **1,000 Sites Footprint** | **`[Sum of Items PWR-01 to PWR-04]`** | **`[Formula = USD * 55]`** |

*(Note: Steel tower structures, foundations, compound civil construction, and site earth grounding grids are priced and evaluated under Table 6: Lot 5 Site Acquisition, Civils & Infrastructure Works)*

---

### TABLE 4: LOT 3 — 5G CORE NETWORK (5GC SA) & DATACENTER

| Item Ref | Subsystem Component | Dimensioning / Sizing | Model Type | Total Year 1 Price (USD) [Bidder Quote] |
| :--- | :--- | :--- | :--- | :---: |
| **5GC-HW-01** | **Compute Server Nodes (2U)** | Dual Xeon Gold / EPYC, 512GB RAM, NVMe (Dual Sites, N+1) | Hardware Purchase | `[Bidder Quote]` |
| **5GC-HW-02** | **High-Throughput UPF Nodes** | 80 Gbps line-rate forwarding per node with DPDK (N+1 per DC) | Hardware Purchase | `[Bidder Quote]` |
| **5GC-HW-03** | **Datacenter Network Fabric** | Spine/leaf switches (100GE / 25GE), perimeter firewalls, anti-DDoS | Hardware Purchase | `[Bidder Quote]` |
| **5GC-HW-04** | **Storage Array & Backup System** | High-IOPS redundant enterprise NVMe storage arrays | Hardware Purchase | `[Bidder Quote]` |
| **5GC-SW-01** | **5GC Control Plane Software (1M)**| AMF, SMF, PCF, UDM, UDR, AUSF, NRF, NSSF, CHF (1,000,000 Subs) | Perpetual License | `[Bidder Quote]` |
| **5GC-SW-02** | **Carrier-Grade NAT & DPI Software** | CG-NAT deterministic port license + Layer-7 DPI bandwidth policing | Perpetual License | `[Bidder Quote]` |
| **5GC-SW-03** | **CaaS / Kubernetes Orchestration**| Enterprise Kubernetes platform & container management | Perpetual / Annual | `[Bidder Quote]` |
| **5GC-SVC-01** | **Integration, IOT with RAN & UAT** | End-to-end design, commissioning, RAN interoperability testing | Professional Services | `[Bidder Quote]` |
| **SUBTOTAL** | **5G Core Year 1 Turnkey Package** | *Dual Datacenter Active-Active Setup (1M Subs)* | **Turnkey Initial** | **`[Sum of Items 5GC-01 to SVC-01]`** |

*Incremental Capacity Expansion License (Tiers above 1,000,000 Subscribers):*
* *Subscribers 1,000,001 to 2,000,000:* [Bidder to Quote USD] per registered subscriber.
* *Subscribers 2,000,001 to 3,000,000:* [Bidder to Quote USD] per registered subscriber.
* *Annual Software Maintenance & Support (AMC):* [Bidder to Quote] % per annum.

---

### TABLE 5: LOT 4 — DIGITAL OSS/BSS & FIELD FORCE AUTOMATION

| Item Ref | OSS/BSS Functional Module | Detailed Functional Scope | License Type | Total Year 1 Price (USD) [Bidder Quote] |
| :--- | :--- | :--- | :--- | :---: |
| **BSS-01** | **Converged CRM & Product Catalog** | Omnichannel customer onboarding, product catalog (4 FWA tariffs) | Perpetual / Enterprise | `[Bidder Quote]` |
| **BSS-02** | **Real-Time Balance & Rating Engine**| CHF adapter, real-time prepaid quota metering, zero-balance redirect | Perpetual License | `[Bidder Quote]` |
| **BSS-03** | **Payment Channel Integration** | Native API integrations: GCash, Maya, 7-Eleven CLiQQ, Bayad Center | Integration Module | `[Bidder Quote]` |
| **BSS-04** | **Billing & Invoicing Engine** | Postpaid billing engine for SME and enterprise anchor tenants | Perpetual License | `[Bidder Quote]` |
| **OSS-01** | **Field Force Management (FMS)** | Algorithmic automated dispatch handling 3,500 daily work orders | Enterprise License | `[Bidder Quote]` |
| **OSS-02** | **Mobile Technician Android App** | Barcode scan, GPS dispatch, live RF RSRP/SINR validation tool | Unlimited Users | `[Bidder Quote]` |
| **OSS-03** | **CPE Warehouse Logistics & Reverse WMS**| Serialized asset lifecycle tracking, repossession & refurbishment module | Enterprise License | `[Bidder Quote]` |
| **OSS-04** | **Network Performance & Fault OSS** | Multi-vendor RAN/Core EMS integration, alarm correlation, RCA | Enterprise License | `[Bidder Quote]` |
| **OSS-05** | **Regulatory BI & NTC Dashboard** | Automated QoS speed compliance reporting to NTC | Included | `[Bidder Quote]` |
| **OSS-SVC** | **Systems Integration & UAT Launch** | End-to-end configuration, test scripts, launch support | Professional Services | `[Bidder Quote]` |
| **SUBTOTAL** | **OSS/BSS Turnkey Year 1 Package** | *Full Stack Suite Dimensioned for 1M Subscribers* | **Turnkey Initial** | **`[Sum of Items BSS-01 to OSS-SVC]`** |

---

### TABLE 6: LOT 5 — SITE ACQUISITION, DETAILED SITE SURVEY (TSSR), RF DESIGN & CIVIL WORKS

| Item Ref | Service / Works Description | Detailed Technical Scope & Deliverables | Application | Phase 1 Qty | Unit Price (USD) [Bidder Quote] | Unit Price (PHP @ 55 FX) | Phase 1 Total (USD) | Remarks / Methodology |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **CIV-SVC-01** | **Detailed Site Survey Report (TSSR)** | Structural load audit, 360° drone sweep, power/grounding audit, civil sketch, PE sign-off | All Sites (Co-loc & Green) | 1,000 sites | `[Bidder Quote]` | `[Formula = USD * 55]` | `[Qty * Rate]` | Mandatory TSSR |
| **CIV-SVC-02** | **Site Acquisition & Permitting Support** | LGU building permits, Barangay clearances, CAAP height clearance, environmental docs | Greenfield Sites | 103 sites | `[Bidder Quote]` | `[Formula = USD * 55]` | `[Qty * Rate]` | Full permit clearance |
| **CIV-SVC-03** | **Equipment Pad Foundation & Cable Gantry**| Concrete plinth for DC power/battery cabinet, elevated cable ladder, AC interconnect tap | Leased TowerCo Sites | 897 sites | `[Bidder Quote]` | `[Formula = USD * 55]` | `[Qty * Rate]` | Co-location upgrade |
| **CIV-SVC-04** | **Greenfield Compound Works & Pad** | 8m x 8m compound grading, chain-link security fence, crushed gravel, equipment pad | Greenfield (Class T4) | 103 sites | `[Bidder Quote]` | `[Formula = USD * 55]` | `[Qty * Rate]` | Civil compound construction |
| **CIV-SVC-05** | **Grounding Grid & Lightning Protection** | Exothermic Cadweld copper ring, ground rods, busbar, air terminal (<= 5.0 Ohms) | Greenfield (Class T4) | 103 sites | `[Bidder Quote]` | `[Formula = USD * 55]` | `[Qty * Rate]` | Dedicated ground ring |
| **CIV-SVC-06** | **30m Monopole Tower Supply & Erection** | ASTM A572 steel monopole, 250 km/h wind survival, fall arrest ladder, PE certification | Greenfield Standard (Alt A) | 80 sites | `[Bidder Quote]` | `[Formula = USD * 55]` | `[Qty * Rate]` | 80 sites standard (mutually exclusive with 40m) |
| **CIV-SVC-07** | **40m Monopole Tower Supply & Erection** | ASTM A572 steel monopole, 250 km/h wind survival, climbing ladder, structural sign-off | Greenfield High-Clearance (Alt B) | 23 sites | `[Bidder Quote]` | `[Formula = USD * 55]` | `[Qty * Rate]` | 23 sites terrain/canopy (mutually exclusive with 30m) |
| **CIV-SVC-08** | **RF Propagation Modeling & Siting** | 3D ray-tracing simulation, clutter calibration, search ring generation, nominal plan | Macro Footprint | 1,000 sites | `[Bidder Quote]` | `[Formula = USD * 55]` | `[Qty * Rate]` | RF engineering model |
| **CIV-SVC-09** | **Cluster RF Optimization & Drive Test** | Multi-site cluster drive testing, antenna tilt/azimuth optimization, neighbor tuning | Per Site Share | 1,000 sites | `[Bidder Quote]` | `[Formula = USD * 55]` | `[Qty * Rate]` | Cluster optimization |
| **TOTAL** | **Lot 5 Civil & Siting Scope (Phase 1 Total)** | *Full Turnkey Site Acquisition, Survey, Design, Towers & Civil Construction* | **1,000 Sites Footprint** | **1,000 sites** | — | — | **`[Sum of Items CIV-SVC-01 to CIV-SVC-09]`** | *Evaluated Phase 1 Lot 5 Total* |

---

### TABLE 7: LOT 6 — MANAGED SERVICES & 24/7 NETWORK OPERATIONS (ANNUAL OPEX)

| Item Ref | Managed Operations Domain | Scope of Services | Pricing Basis | Monthly Rate (PHP) [Bidder Quote] | Monthly Rate (USD @ 55 FX) | Annual Cost / Site (USD) |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **MS-OP-01** | **24/7 Tier-2/Tier-3 Central NOC** | Active surveillance, incident triage, vendor escalation | Per Site / Month | `[Bidder Quote]` | `[PHP / 55]` | `[Monthly USD * 12]` |
| **MS-OP-02** | **Field First Line Maintenance (FLM)**| 24/7 nationwide emergency restoration, MTTR <= 2-4 hrs | Per Site / Month | `[Bidder Quote]` | `[PHP / 55]` | `[Monthly USD * 12]` |
| **MS-OP-03** | **Scheduled Preventive Maintenance** | Quarterly site inspection, power, battery, grounding | Per Site / Month | `[Bidder Quote]` | `[PHP / 55]` | `[Monthly USD * 12]` |
| **MS-OP-04** | **Spare Parts Logistics & Warehousing**| Regional buffer stock, NBD replacement delivery | Per Site / Month | `[Bidder Quote]` | `[PHP / 55]` | `[Monthly USD * 12]` |
| **MS-OP-05** | **Continuous Network RF Optimization** | Routine KPI monitoring, neighbor tuning, interference mgmt | Per Site / Month | `[Bidder Quote]` | `[PHP / 55]` | `[Monthly USD * 12]` |
| **TOTAL** | **Active Network O&M Fee** | *All inclusive active telecom managed operations* | **Per Site / Month** | **`[Sum of OP-01 to OP-05]`** | **`[Sum of USD]`** | **`[Annual Total USD]`** |

---

### TABLE 8: LOT 7 — 5G CUSTOMER PREMISES EQUIPMENT (CPE)

| Item Ref | Device Description | Minimum Technical Specifications | Target Qty (Phase 1) | Unit Price (USD) [Bidder to Quote] | Total Phase 1 Cost (USD) |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **CPE-01** | **Indoor 5G High-Gain FWA Router** | Band n50 native, >= 8.0 dBi internal antenna, Wi-Fi 6 AX1800/AX3000, 1x 2.5GE + 2x 1GE ports, TR-069/TR-369 | 350,000 units | `[Bidder Quote]` | `[Formula = Qty * Rate]` |
| **CPE-02** | **Outdoor 5G High-Gain FWA Package**| Band n50, IP67 enclosure, >= 12.0 dBi directional antenna, 1x 2.5GE PoE, bundled indoor Wi-Fi 6 router & PoE injector | 15,000 units | `[Bidder Quote]` | `[Formula = Qty * Rate]` |
| **CPE-SVC** | **Staging, Pre-Config & SIM-Locking**| Custom firmware flashing, operator APN & PLMN lock, retail packaging for all Phase 1 terminals | 365,000 units | `[Bidder Quote]` | `[Formula = Qty * Rate]` |
| **TOTAL** | **Lot 7 5G CPE Terminals Package** | *Total Initial Terminal Supply & Staging (365,000 Total Devices)* | **365,000 Units** | — | **`[Sum of Items CPE-01 to CPE-SVC]`** |

---

### TABLE 9: FORM C — 10-YEAR TOTAL COST OF OWNERSHIP (TCO) & LIFECYCLE SCHEDULE

*Evaluation Baseline: Committed Phase 1 Network (1,000 Macro Sites Footprint 10-Year Lifecycle Cost). Expansion Capex for Years 2 to 5 (Phases 2 to 5, 1,000 sites/year up to 5,000 sites total) is governed by firm unit rates under contractual call-off options.*

| Line | Cost Category / Lifecycle Element | Phase 1 Capex (Yr 1) | Yr 2 | Yr 3 | Yr 4 | Yr 5 | Yrs 6-10 Cumulative | 10-Year Total TCO (USD) | Evaluation Basis & Assumptions |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **5G RAN & Site Infrastructure (Lots 1, 2, 5)** | `[Lots 1+2+5 Total]` | $0 | $0 | $0 | $0 | $0 | `[Sum Yrs 1-10]` | **[Evaluated Tender Input]** Initial 1,000 sites turnkey rollout (Lots 1, 2, 5 Phase 1 Totals). Expansion Yrs 2-5 Capex evaluated via call-off rate card. |
| **2** | **5G Core Network & Cloud DC (Lot 3)** | `[Lot 3 Total]` | $0 | $0 | $0 | $0 | $0 | `[Sum Yrs 1-10]` | **[Evaluated Tender Input]** Day-1 Core & DC infrastructure dimensioned for 1.0M subscribers (perpetual license + compute fabric). |
| **3** | **Digital OSS/BSS & Automation (Lot 4)** | `[Lot 4 Total]` | $0 | $0 | $0 | $0 | $0 | `[Sum Yrs 1-10]` | **[Evaluated Tender Input]** Turnkey BSS/OSS stack, CRM, prepaid billing, and FMS dispatch engine. |
| **4** | **5G CPE Terminals Supply (Lot 7)** | `[Lot 7 Total]` | $0 | $0 | $0 | $0 | $0 | `[Sum Yrs 1-10]` | **[Evaluated Tender Input]** Phase 1 initial supply of 365,000 subscriber terminals (350k indoor + 15k outdoor). |
| **5** | **Software Support & AMC (5GC + OSS/BSS)** | $0 | `[10% SW]` | `[10% SW]` | `[10% SW]` | `[10% SW]` | `[50% SW]` | `[Sum Yrs 1-10]` | **[Prescribed Evaluated Parameter]** 10.0% p.a. of Core (Lot 3) + OSS/BSS (Lot 4) software Capex starting Yr 2 following 12-month Day-1 warranty. |
| **6** | **Managed Services & Field O&M (Lot 6)** | `[MS * 1,000]` | `[MS * 1,000]` | `[MS * 1,000]` | `[MS * 1,000]` | `[MS * 1,000]` | `[MS * 5,000]` | `[Sum Yrs 1-10]` | **[Prescribed Evaluated Parameter]** Evaluated on Phase 1 network baseline (1,000 sites footprint @ Lot 6 quoted annual rate). Scales upon expansion call-off. |
| **7** | **Spare Parts Float & RMA Replenishment** | `[2% RAN]` | `[1% RAN]` | `[1% RAN]` | `[1% RAN]` | `[1% RAN]` | `[5% RAN]` | `[Sum Yrs 1-10]` | **[Prescribed Evaluated Parameter]** 2.0% initial spares float in Yr 1, 1.0% annual replenishment in Yrs 2-5, and 5.0% cumulative in Yrs 6-10. |
| **TOTAL** | **10-Year Evaluated Lifecycle TCO (USD)** | `[Sum B1-B7]` | `[Sum C1-C7]` | `[Sum D1-D7]` | `[Sum E1-E7]` | `[Sum F1-F7]` | `[Sum G1-G7]` | **`[10-Year Grand Total]`** | **Evaluated Total Lifecycle Cost of Ownership for Phase 1 Network Baseline** |

---

### TABLE 10: MANDATORY VENDOR FINANCING FACILITY (FORM D)

The Bidder must submit a formal, legally binding financing term sheet with the following parameters:

| Financing Lever | Operator Mandatory Requirement | Bidder Binding Offer [Bidder to Complete] |
| :--- | :--- | :--- |
| **Financing Structure** | OEM-backed Buyer's Credit or Export Credit Agency (ECA) facility | `[Bidder to Specify Facility Structure]` |
| **Financing Quantum** | Minimum **80% of Eligible Capital Expenditure** (Lots 1, 3, Turnkey Services) | `[Bidder to State % Financed]` |
| **Equity Downpayment** | Maximum **20% Downpayment** upon contract signing | `[Bidder to State Downpayment %]` |
| **Facility Tenor** | Flexible facility tenor **up to 20 Years** (minimum 4 years, 5+ years preferred) | `[Bidder to State Tenor in Months]` |
| **Principal Grace Period** | Deferred principal repayment / grace period **up to 10 Years** (minimum 12 months, 18+ months preferred) | `[Bidder to State Grace Period]` |
| **Indicative Interest Rate** | Fixed commercial rate (preferred <= 6.50% p.a.) or competitive benchmark to SOFR + spread | `[Bidder to State Fixed Rate or Spread]` |
| **Security / Collateral** | Pledge on network equipment assets without restrictive operational covenants | `[Bidder to Specify Security Terms]` |
| **Repayment Frequency** | Semi-annual or quarterly principal and interest amortizations | `[Bidder to Specify Payment Cadence]` |

---
*(End of Appendix B — Commercial Proposal & Pricing Templates)*
