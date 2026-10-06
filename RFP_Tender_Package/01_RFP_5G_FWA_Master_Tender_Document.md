# REQUEST FOR PROPOSAL (RFP) & TENDER SPECIFICATION
## NATIONWIDE 5G FIXED WIRELESS ACCESS (FWA) NETWORK INFRASTRUCTURE, SERVICES & MANAGED OPERATIONS

**Tender Document No:** RFP-TELTECH-FWA-2026-001  
**Project Identifier:** Nationwide 5G FWA Project (Band n50, 60 MHz TDD)  
**Issuing Authority:** Telecommunications Technology Solutions Incorporated (TelTech)  
**Author:** OLIVER TUNGOL  
**Issue Date:** October 6, 2026  
**Document Revision:** Revision 2.0 (Official Bidding Version — Blank BoQ)  
**Confidentiality:** Strictly Confidential — Competitive Commercial Tender  

---

## 1. EXECUTIVE SUMMARY & INVITATION TO BID

### 1.1 Purpose of the Tender
Telecommunications Technology Solutions Incorporated (TelTech) (hereinafter referred to as the **"Operator"** or **"Company"**) hereby invites qualified, world-class telecommunications equipment manufacturers, network systems integrators, and managed service providers (hereinafter referred to as the **"Bidder"** or **"Vendor"**) to submit comprehensive, binding technical and commercial proposals for the turnkey supply, delivery, installation, integration, optimization, and managed operations of a nationwide **5G Fixed Wireless Access (FWA) Network**. The Operator is actively seeking creative, high-impact proposals—both technical and commercial—from prospective bidders that deliver industry-leading spectral efficiency, innovative vendor financing architectures, accelerated rollout velocity, and optimized Total Cost of Ownership (TCO).

The Operator has been officially awarded a Provisional Authority / Permit to Test and Demo Broadcast for **Band n50 (1432 – 1517 MHz, 1.5 GHz L-Band TDD)** with a **60 MHz contiguous carrier block**, and holds a pending application for the permanent commercial assignment and use of the said frequency band pursuant to and subject to the provisions of the Open Access in Data Transmission Act (**Konektadong Pinoy Law**) and National Telecommunications Commission (NTC) regulatory frameworks.

### 1.2 Program Scope & Deployment Scale
The nationwide program encompasses a total footprint of **5,000 macro BTS sites** deployed across five (5) consecutive phases:
* **Phase 1 (Day-1 Priority Launch):** **1,000 Macro Sites** (Batch 1 — immediate rollout across prioritized unserved and underserved suburban and rural population centers).
* **Phases 2 to 5 (Nationwide Expansion):** **1,000 Macro Sites per annum** over Years 2 through 5, reaching full target deployment of 5,000 BTS sites serving over **2.45 to 2.66 Million active broadband subscribers**.
* **Target Addressable Population:** Over **32.3 Million residents** across 5,000 barangays (2024 PSA POPCEN Official Census baseline).
* **Initial Network Sizing Load:** 1,000 active concurrent fixed broadband subscribers per 3-sector BTS (capacity ceiling of 5,965 peak BTS units across expansion).

### 1.3 Tender Structure & Bid Lots
Bidders are invited to submit tenders for one, multiple, or all of the following distinct Lots:
* **LOT 1: Radio Access Network (RAN) Hardware, Antennas & Turnkey Deployment Services**
* **LOT 2: Power Systems & Passive Site Infrastructure (Co-location Interconnect & Hybrid DC Power)**
* **LOT 3: Cloud-Native 5G Core Network (5GC SA) & Datacenter Infrastructure**
* **LOT 4: Converged Digital OSS/BSS, Field Force Automation & Real-Time Charging Engine**
* **LOT 5: RF Planning, Greenfield Site Survey, Civil Works & Cluster Optimization Services**
* **LOT 6: Nationwide Managed Services, 24/7 Tier-2/Tier-3 NOC & Field Network Operations (MS)**
* **LOT 7: Customer Premises Equipment (CPE) 5G Sub-3 GHz High-Gain Terminals**

Bidders submitting integrated "Full Turnkey Consortium" bids spanning Lots 1 through 6 will receive multi-lot synergy evaluation scoring.

---

## 2. PROJECT BACKGROUND, OPERATING ENVIRONMENT & TECHNICAL BASELINE

### 2.1 Spectrum Physics: Band n50 Advantage
Band n50 operates in the 1.5 GHz L-Band (1432 – 1517 MHz), providing superior propagation characteristics over mid-band frequencies (e.g., 3.5 GHz Band n78):
* **Propagation Efficiency:** 1.5 GHz propagation achieves an effective reliable non-line-of-sight (NLOS) and near-line-of-sight (nLOS) coverage radius of **3.5 km** (delivering up to **38.5 km²** of coverage area per site under suburban/rural clutter).
* **Penetration Resilience:** Foliage, atmospheric rain fade, and typical Philippine residential building materials (concrete hollow block, corrugated galvanized sheet roofing) suffer 8–12 dB lower path loss compared to 3.5 GHz.
* **Spectrum Allocation:** 60 MHz contiguous TDD frame structure (configurable TDD DL:UL ratios: 4:1 for broadband downlink-heavy traffic, or 3:1 for balanced enterprise transmission).

### 2.2 Site Infrastructure Landscape & Tower Strategy
The operator has completed a nationwide spatial overlay matching the 5,000 candidate barangay centroids against **13,746 verified operational cell towers** spanning six (6) tower portfolios:
* **PTCI / MIDC TowerCo:** 5,080 towers
* **FTAP Globe Telecom:** 3,529 towers
* **EdgePoint Infrastructure:** 2,775 towers
* **FTAP Smart Communications:** 1,023 towers
* **LBS Digital Infrastructure (LDIC):** 700 towers
* **FTAP BTS Dedicated Sites:** 639 towers

#### Deployment Typology (Co-location vs. Greenfield):
* **Class T1 (Immediate Co-location, <= 0.5 km):** 54.8% of Phase 1 sites (42.5% nationwide). Sited directly on operational TowerCo structures with existing AC power and civil compound.
* **Class T2 (Close Co-location, 0.5 - 1.0 km):** 26.9% of Phase 1 sites (30.4% nationwide). Sited on operational towers within beamforming reach.
* **Class T3 (Near Co-location, 1.0 - 2.0 km):** 8.0% of Phase 1 sites (17.8% nationwide). Co-location viable subject to RF propagation clearance.
* **Class T4 (Greenfield Monopole Required, > 2.0 km):** 10.3% of Phase 1 sites (9.3% nationwide; ~460 sites total). Requires self-constructed 30m/40m monopole, civil shelter, dedicated utility transformer drop, and backup diesel/solar generation.

### 2.3 Transmission & Backhaul Topology
Transmission connectivity has been audited via the Converge fiber network audit (1,296 confirmed optical nodes and 4,401 fiber segments; subject to verification on the ground):
* **Terrestrial Fiber Optic Cable (FOC):** 98.3% of Phase 1 sites connect via terrestrial fiber drops (Class A: Node <= 0.5 km; Class B: Node <= 1.0 km; Class C: Line-tap splice closure <= 0.5 km; Class D: Lateral/Microwave <= 3.0 km).
* **Satellite LEO Backhaul (Starlink Business):** 1.7% of Commercial Phase 1 sites (and up to 34.4%–43.5% in remote universal access/GIDA sites) utilize 4-terminal Starlink Business arrays (delivering aggregated 400–800 Mbps burst with SD-WAN bonding and traffic shaping).

---

## 3. SCOPE OF WORK BY TENDER LOT

### LOT 1: 5G RAN EQUIPMENT & ACCESS HARDWARE
The Bidder shall supply, deliver, install, test, and commission carrier-grade 3GPP Release 16/17 compliant 5G RAN equipment:
1. **Baseband Unit (BBU):**
   * High-capacity rack-mountable 19" subrack BBU supporting multi-cell aggregation and up to 12 cells of 60 MHz Band n50.
   * Dual redundant DC power supply inputs (-48V DC, operating range -40.5V to -57V DC).
   * Backhaul interfaces: Minimum 4x 10GE/25GE optical SFP28 interfaces supporting IEEE 1588v2 Precision Time Protocol (PTP) Telecom Profile (G.8275.1) and SyncE.
   * Fronthaul interfaces: Minimum 6x 25GE eCPRI interfaces with integrated Optical Supervisory Channel (OSC).
2. **Remote Radio Units (RRU) / Active Antenna Units (AAU):**
   * Configuration: **8T8R MIMO**, 3 sectors per macro site (total of 3 RRUs and 3 antennas per standard macro).
   * Operating Frequency: Band n50 (1432 – 1517 MHz), full 60 MHz IBW (Instantaneous Bandwidth) and OBW (Occupied Bandwidth).
   * RF Output Power: Minimum **8 x 40W (320 W total RF power per sector)**.
   * Beamforming capability: Digital horizontal and vertical beamforming supporting dynamic multi-user MIMO (MU-MIMO) pairing.
   * Protection & Environment: IP65/IP67 ingress rating, natural convection or high-durability fanless cooling, surviving wind speeds of up to 250 km/h (Typhoon Category 5 resilience).
3. **Macro Antennas & RF Ancillaries:**
   * High-gain 8-port cross-polarized antennas (or integrated AAU) supporting Band n50 with electrical remote downtilt (eRET via AISG 2.0 / 3GPP).
   * Horizontal half-power beamwidth: 65° +/- 5°; Minimum gain >= 17.5 dBi.
   * Low PIM performance: <= -153dBc @ 2 x 43 dBm.
   * High-grade low-loss optical fiber patchcords, IP67 weatherproof boot assemblies, DC power surge protective devices (SPD Type 1+2), and grounding kits.

### LOT 2: POWER SYSTEMS & PASSIVE INFRASTRUCTURE
The Bidder shall provide unified site power solutions engineered for high availability across both leased TowerCo sites and greenfield sites:
1. **DC Power Rectifier Plant:**
   * Modular 19" 3U/4U switchmode DC power system dimensioned for **6.0 kW** continuous capacity (4 x 2.0 kW or 3 x 3.0 kW hot-swappable rectifier modules in N+1 redundancy).
   * Rectifier efficiency: >= 96.0% (80 PLUS Titanium / high-efficiency class).
   * Advanced SMPS controller with SNMPv3, HTTPS, Modbus, dry contacts, and remote cloud telemetry.
2. **Battery Energy Storage System (BESS):**
   * Lithium Iron Phosphate (LiFePO4 / LFP) battery modules: Minimum **1 x 48V / 150 Ah (or 2 x 100 Ah)** providing >= 4hours backup autonomy at standard 2.5–3.0 kW BTS operational load.
   * Cycle life: >= 4,000 cycles at 80% Depth of Discharge (DoD) @ 25°C.
   * Built-in intelligent BMS with cell-level balancing, over-charge, over-discharge, short-circuit, and high-temperature thermal runaway cutoffs.
3. **Standby Generator Sets (Greenfield Class T4 Sites):**
   * 15 kVA / 12 kW prime-rated, 230V single-phase / 400V 3-phase, 60 Hz water-cooled diesel generator with sound-attenuated weatherproof enclosure (< 68dBA @ 7m).
   * Minimum 500-liter to 1,000-liter sub-base day fuel tank providing >= 72hours continuous operation during grid blackout.
   * Automatic Transfer Switch (ATS) with motorized 4-pole contactor and mechanical interlock.
4. **TowerCo Co-Location Power Interconnect Kit:**
   * Standardized DC tap-off distribution box, sub-metering Class 1.0 revenue-grade energy meter with RS485 telemetry, and dedicated surge suppression.

### LOT 3: CLOUD-NATIVE 5G CORE (5GC SA) & DATACENTER INFRASTRUCTURE
The Bidder shall deploy a carrier-grade, cloud-native 5G Standalone (5G SA) Core Network dimensioned for **1,000,000 initial registered subscribers** scaling up to **3,000,000 subscribers**, deployed in a **Geo-Redundant, Active-Active Dual Datacenter Topology** (NCR Primary DC and Metro Clark / Region III Disaster Recovery DC):
1. **Network Functions (NFs) Scope:**
   * Control Plane: AMF, SMF, NRF, NSSF, PCF, UDM, UDR, AUSF, NEF, CHF.
   * User Plane: High-performance distributed User Plane Function (UPF) nodes.
2. **User Plane (UPF) Throughput Dimensioning:**
   * UPF capacity dimensioned for **80 Gbps usable throughput per 2U dual-socket compute node** (minimum 2 x 100GE line-rate DPDK / SR-IOV interfaces).
   * Integrated high-performance **Carrier-Grade NAT (CG-NAT)** supporting deterministic port allocation and 10:1 to 16:1 subscriber port density.
   * Integrated Deep Packet Inspection (DPI) for layer-7 traffic classification, fair-use bandwidth throttling, and URL filtering.
3. **Hardware & CaaS Virtualization Infrastructure:**
   * Enterprise OpenStack or Bare-Metal Kubernetes (CaaS) orchestration platform.
   * Dual-socket Intel Xeon / AMD EPYC server nodes, 512 GB RAM, dual 25G/100G NICs, redundant enterprise NVMe storage arrays.
   * Redundant datacenter leaf-spine fabric switches (32 x 100GE spine, 48 x 25GE + 6 x 100GE leaf), redundant perimeter next-gen firewalls, and DDoS mitigation scrubbing appliances.
4. **Licensing Framework:**
   * Tiered perpetual subscriber capacity licensing:
     * Tier 1 (First 100k subs): Bidder to quote per registered sub.
     * Tier 2 (100k to 500k subs): Bidder to quote per registered sub.
     * Tier 3 (500k to 1M+ subs): Bidder to quote per registered sub.

### LOT 4: CONVERGED DIGITAL OSS/BSS & FIELD FORCE AUTOMATION
The Bidder shall deliver an integrated, cloud-native Telecom Business Support System (BSS) and Operations Support System (OSS) optimized for high-volume, low-friction fixed broadband operations:
1. **Converged BSS & Omnichannel Customer Engagement:**
   * Omnichannel CRM, Product Catalog, and CPQ supporting 4 primary retail tariffs and SME tiers.
   * Native Prepaid-First architecture: Integration directly with 5G Core Charging Function (CHF) via 3GPP Nchf / Diameter Ro interfaces.
   * Payment Gateway Integrations: Native, production-ready REST API integrations with Philippine digital payment channels: **GCash, Maya (PayMaya), 7-Eleven CLiQQ OTC, Bayad Center**, bank transfer (InstaPay/PESONet), and municipal distributor airtime portals.
2. **Field Force Management (FMS) & Mobile Technician App:**
   * Automated work-order generation and algorithmic dispatch engine handling up to **3,500 daily work orders** (new installs, truck rolls, relocations, CPE reclaims, and trouble calls).
   * Android mobile app for field technicians: Real-time GPS dispatch, barcode/QR scanning of CPE MAC and serial numbers, automated outdoor signal sweep tool (RSRP/SINR validation), photograph proof of installation, and customer digital e-signature.
   * Turnaround SLA: Compressed installation timeline from 14 calendar days down to **under 48 hours** from order booking.
3. **CPE Warehouse Logistics & Asset Reverse Logistics (WMS):**
   * End-to-end serialized asset tracking from central warehouse staging through regional depots, technician truck float, subscriber premises, and repossession/refurbishment cycle.
   * Support for minimum 70% CPE recovery and refurbishment upon subscriber churn.
4. **OSS Network Management, Fault & Performance Monitoring:**
   * Multi-vendor RAN EMS/NMS integration via 3GPP northbound REST/Kafka/SNMP interfaces.
   * Real-time automated fault correlation, root-cause analysis (RCA), and synthetic SLA monitoring.
   * Automated NTC regulatory compliance KPI dashboard and QoS reporting engine.

### LOT 5: RF PLANNING, SITE SURVEY & CLUSTER OPTIMIZATION
The Bidder shall execute end-to-end RF planning, site survey, civil design, and cluster radio tuning:
1. **Detailed Greenfield & Co-Location Site Surveys:**
   * Technical Site Survey Report (TSSR) for each assigned candidate barangay: Detailed structural load analysis on existing towers, antenna mounting space, azimuthal line-of-sight (LOS) drone photographic sweeps (360° at 20m, 30m, 40m AGL), AC power distribution panel capacity, grounding resistance (<= 5 Ohms), and backhaul cable routing.
2. **High-Precision RF Propagation Modeling:**
   * Production-grade RF propagation model tuning in Asset / Atoll / Planet utilizing high-resolution GIS clutter and 3D digital elevation models (DEM <= 5m resolution).
   * Cell dimensioning: Sizing for 60 MHz Band n50 TDD, 3 sectors @ 120° nominal separation, antenna height 30m–45m AGL, coverage target RSRP >= -95 dBm across >= 90% of populated barangay settlement areas.
3. **Single Site Verification (SSV) & Cluster Tuning:**
   * SSV drive tests and stationary multi-point testing per site verifying 3-sector RF radiation, antenna tilt (RET), PCI validation, azimuth verification, and handover execution.
   * Cluster optimization across 10–20 site clusters to eliminate pilot pollution, optimize neighbor lists, minimize inter-cell interference, and balance sector traffic loading.

### LOT 6: NATIONWIDE MANAGED SERVICES & 24/7 NETWORK OPERATIONS (MS)
The Bidder shall provide fully managed, SLA-governed network operations, field maintenance, and spare parts management:
1. **Tier-2 & Tier-3 Network Operations Center (NOC):**
   * 24/7/365 active monitoring of RAN, Core, Transmission, Power, and OSS/BSS platforms.
   * Incident management, event correlation, dispatching field maintenance teams, and managing customer trouble ticket escalations.
2. **Nationwide First-Line Maintenance (FLM) Field Operations:**
   * Regional field maintenance hubs across Greater Luzon, Northern Luzon, Southern Luzon, Visayas, and Mindanao.
   * Mean Time to Respond (MTTR) <= 2hours in urban/suburban and <= 4hours in rural clusters for Critical/Severity-1 incidents.
   * Preventive maintenance: Quarterly inspection of RF antenna brackets, coax/optical jumpers, rectifier modules, battery conductance testing, and generator load testing.
3. **Comprehensive Spare Parts Management (SPMS):**
   * Advanced replacement logistics: Central warehouse and regional staging depots maintaining an audited safety float of BBUs, RRUs, rectifiers, lithium batteries, and SFPs.
   * Guarantee of next-business-day (NBD) on-site replacement delivery for failed hardware components.

### LOT 7: 5G HIGH-GAIN CUSTOMER PREMISES EQUIPMENT (CPE)
The Bidder shall supply outdoor and high-gain indoor 5G FWA CPE devices:
1. **RF & Modem Specifications:**
   * Chipset: 3GPP Release 16 compliant 5G NR sub-3 GHz processor.
   * Frequency Bands: Native Band n50 support (1432 – 1517 MHz, 60 MHz channel bandwidth) plus fallback sub-6 GHz bands (n1, n3, n7, n28, n41, n77, n78).
   * Antenna: Internal high-gain directional/omnidirectional antenna array (>= 8to 10 dBi antenna gain in Band n50); optional external TS-9/SMA antenna ports.
   * MIMO: 4R MIMO receiver architecture in Band n50 downlink.
2. **LAN & Local Wi-Fi Specifications:**
   * Wi-Fi 6 (802.11ax), dual-band 2.4 GHz + 5.0 GHz, 2 x 2 MU-MIMO, aggregate speed >= 1800 Mbps (AX1800).
   * Ethernet: Minimum 1 x 2.5GE + 2 x 1GE RJ-45 LAN ports.
   * Voice: 1 x FXS RJ-11 VoIP port (optional).
3. **Device Management & TR-069 / USP (TR-369):**
   * Full remote provisioning via TR-069 / TR-181 or TR-369 USP; remote firmware OTA (FOTA) upgrades; SIM-lock and network-lock enforcement tied to Operator PLMN (515-XX).

---

## 4. RIGOROUS SERVICE LEVEL AGREEMENTS (SLAs) & PERFORMANCE KPIS

The Bidder must guarantee compliance with the following international telecom best-practice KPIs. Failure to achieve these targets shall trigger contractual liquidated damages (LDs) and service credits.

### 4.1 Radio Access Network (RAN) Performance KPIs
| KPI Metric | Formula / Standard | Minimum Acceptance | Target Excellence | Measurement Window |
| :--- | :--- | :---: | :---: | :---: |
| **Radio Network Availability** | [(Total Available Cell Hours - Cell Outage Hours) / Total Available Cell Hours] x 100% | >= 99.70% | >= 99.95% | Monthly / 24x7 |
| **5G Radio Accessibility (CSSR)** | Call/Session Setup Success Rate (RRC + 5G QoS Flow) | >= 99.00% | >= 99.60% | Busy Hour |
| **5G Session Drop Rate (CDDR)** | Abnormal Release Rate per 100 established sessions | <= 0.50% | <= 0.15% | Busy Hour |
| **Single Sector User Capacity** | Active concurrent connected CPE sessions per sector | >= 350 CPEs | >= 450 CPEs | Peak Busy Hour |
| **Peak Cell DL Throughput (60 MHz)** | 8T8R 60 MHz TDD peak aggregated sector throughput | >= 450 Mbps | >= 520 Mbps | Lab & Single Cell Test |
| **Cell Edge DL User Throughput** | 95th percentile cell-edge subscriber download rate | >= 25 Mbps | >= 50 Mbps | Busy Hour |
| **Cell Edge UL User Throughput** | 95th percentile cell-edge subscriber upload rate | >= 5 Mbps | >= 15 Mbps | Busy Hour |
| **End-to-End User Latency (RTT)** | CPE to UPF packet round-trip time | <= 30 ms | <= 18 ms | Continuous Ping |
| **DL Packet Loss Rate (PLR)** | User Plane packet discard rate | <= 0.10% | <= 0.01% | Monthly Average |

### 4.2 Power & Site Infrastructure Resilience KPIs
| Infrastructure Metric | Technical Requirement | Minimum SLA Target | Failure Remedy |
| :--- | :--- | :---: | :---: |
| **Site Power Availability** | BTS Continuous Operating Power (AC Grid + DC Battery + Genset) | >= 99.95% (Leased)<br>>= 99.85% (Greenfield) | Service credit deduction per hour outage |
| **Battery Autonomy Duration** | Time BTS operates on LFP battery during AC utility blackouts | >= 4.0 Hours @ 3.0 kW load | Mandatory module replacement if <3.5 hrs |
| **Generator Auto-Start Reliability** | Genset starts and ATS transfers load within 60s of grid failure | >= 99.0% successful transfers | Liquidated damages on site drop |
| **Grounding Earthing Resistance** | Earth ground electrode resistance to true earth | <= 5.0 Ohms | Mandatory soil conditioning / additional rods |
| **Rectifier System Efficiency** | Operating efficiency from 30% to 90% load range | >= 96.0% | Rejection of non-compliant modules |

### 4.3 5G Core Network & Cloud Infrastructure KPIs
| Core Metric | Operational Definition | Target SLA Benchmark |
| :--- | :--- | :---: |
| **5GC Control Plane Availability** | High availability of AMF, SMF, UDM, PCF across geo-cluster | >= 99.999% ("Five Nines") |
| **5GC User Plane Availability** | Availability of UPF packet routing instances | >= 99.999% |
| **PDU Session Establishment Success** | Initial PDU session setup success rate | >= 99.80% |
| **Session Setup Delay** | End-to-end signaling time to establish 5G session | <= 80 ms (95th percentile) |
| **UPF Packet Forwarding Latency** | Processing delay through UPF hardware | <= 1.0 ms |
| **CG-NAT Port Allocation Success** | Real-time port assignment for new outbound sessions | >= 99.99% |
| **Core Failover Recovery Time (DR)** | Automatic cutover from NCR DC to Clark DR DC | <= 30seconds (Zero session loss) |

### 4.4 OSS/BSS, Field Operations & Managed Services SLAs
| Operational Service Domain | Metric Description | Mandatory SLA Benchmark |
| :--- | :--- | :---: |
| **BSS Billing & Rating System Availability** | Online Charging System (CHF/OCS) uptime | >= 99.99% |
| **Payment Top-Up Processing Time** | Time from payment channel confirmation to account credit | <= 3seconds |
| **Field Force Installation Lead Time** | Order placement to physical CPE on-site activation | <= 48 Hours (Standard urban/suburban) |
| **First-Time Right (FTR) Installs** | Installations operating without trouble call within 14 days | >= 96.0% |
| **Customer Churn CPE Recovery Rate** | Successful physical recovery of CPE on churned accounts | >= 70.0% |
| **Severity 1 Incident MTTR (Critical Outage)** | Time to restore full service on macro BTS outage | <= 2 Hours (Urban) / <= 4 Hours (Rural) |
| **Severity 2 Incident MTTR (Major Degraded)** | Time to restore single sector failure or degraded backhaul | <= 6 Hours |
| **Hardware Replacement Turnaround** | Depot dispatch of spare BBU/RRU/Rectifier to site | <= 24 Hours (Nationwide NBD) |

---

## 5. TENDER SUBMISSION STRUCTURE & COMPLIANCE REQUIREMENTS

Bidders must submit their proposals divided strictly into three (3) separate volumes:

### Volume I: Executive & Commercial Proposal (Financial Envelope)
1. **Form A — Bid Submission Letter & Consortium Structure:** Executed by authorized corporate officers.
2. **Form B — Bill of Quantities (BoQ) & Unit Price Book:** Exhaustive pricing matrix in USD and PHP for all hardware, software licenses, implementation services, and annual maintenance contracts (AMC), completed using the official blank Excel BoQ template.
3. **Form C — Total Cost of Ownership (TCO) Breakdown (10-Year Horizon):** Itemized Day-1 CAPEX, expansion CAPEX, and 10-year OPEX schedules.
4. **Form D — Vendor Financing Proposal (Mandatory Requirement):**
   * The Bidder **must** provide a detailed vendor financing facility covering at least **80% of Capex** (BTS hardware, core, and turnkey rollout).
   * Tenor: Minimum 4-year to 5-year repayment facility.
   * Interest Rate: Fixed commercial rate benchmarked to SOFR + spread.
   * Grace Period: Minimum 12-month grace period on principal repayment during Phase 1 deployment.

### Volume II: Technical Architecture & Compliance Matrix (Technical Envelope)
1. **Section A — RAN Technical Design:** 3GPP R16/17 compliance, Band n50 8T8R AAU/RRU datasheets, BBU subrack capacity, antenna radiation patterns, and link budget calculations.
2. **Section B — Power & Site Civil Engineering:** Rectifier plant, LFP battery cycle curves, genset specifications, and TowerCo co-location interface diagrams.
3. **Section C — 5G Core Architecture:** Cloud-native microservices architecture, dual datacenter active-active geo-redundancy topology, UPF DPDK hardware dimensioning, and CG-NAT sizing.
4. **Section D — OSS/BSS & IT Stack:** Modular architecture, digital self-care portal, payment channel API integrations, field-force management mobile application, and WMS inventory tracking.
5. **Section E — RF Planning & Cluster Optimization Methodology:** Link budget models, clutter definitions, drive-test methodology, and SSV acceptance criteria.
6. **Section F — Managed Services & Operations Plan:** NOC structure, FLM staffing model, SLA penalty framework, and spare parts dimensioning model.
7. **Compliance Matrix:** Line-by-line statement of compliance (**Compliant / Minor Deviation / Non-Compliant**) against every technical requirement in Appendix A.

### Volume III: Bidder Qualifications, References & Financial Soundness
1. **Corporate Financial Statements:** Audited financial statements for the past three (3) fiscal years demonstrating solvency, liquidity, and operational turnover.
2. **Telecom Track Record:** Proof of at least three (3) commercial 5G deployments (RAN or Core) of similar or larger scale within the past 36 months.
3. **Philippine In-Country Support Structure:** Documented local Philippine engineering entity, SEC registration, local repair center, and existing field logistics capabilities.

---

## 6. BID EVALUATION CRITERIA & AWARD METHODOLOGY

Tenders will be evaluated using a **Quality and Cost-Based Selection (QCBS)** scoring framework:

```
Total Evaluation Score = (Technical Score × 60%) + (Commercial & Financing Score × 40%)
```

### 6.1 Technical Evaluation Breakdown (100 Points / 60% Total Weight)
* **RAN Architecture & Radio RF Performance (25 Points):** Band n50 output power, 8T8R beamforming algorithms, power consumption efficiency, and environmental durability.
* **5G Core Architecture & Geo-Redundancy (20 Points):** Cloud-native architecture, UPF line-rate throughput, CG-NAT scale, and seamless hitless failover.
* **OSS/BSS Capabilities & Local Integrations (15 Points):** Real-time charging, native Philippine digital payment interfaces, automated field dispatch tool, and WMS inventory reverse logistics.
* **Power Engineering & Site Solution (10 Points):** LFP battery cycle life, rectifier efficiency, TowerCo co-location integration simplicity, and genset reliability.
* **RF Planning, Optimization & Rollout Methodology (15 Points):** Link budget precision, cluster tuning rigor, and proven ability to mobilize 1,000 sites in 12 months.
* **Bidder Experience, References & Local Entity (15 Points):** Tier-1 telecom reference base, local Philippine support team, and spare parts warehouse infrastructure.

### 6.2 Commercial & Financing Evaluation Breakdown (100 Points / 40% Total Weight)
* **Capex Competitiveness (40 Points):** Evaluated across lowest compliant Capex bids. Lowest qualifying responsive Capex receives full points.
* **10-Year Opex & TCO Efficiency (25 Points):** Low ongoing power consumption, competitive software AMC rates, and managed services unit pricing.
* **Vendor Financing Structure (35 Points):** Grace period length, interest rate spread, financing quantum (>= 80%), and ease of financial covenants.

---

## 7. TENDER TIMELINE & KEY MILESTONES

| Milestone Event | Scheduled Date | Responsibility |
| :--- | :--- | :--- |
| **Official RFP Tender Issuance** | October 6, 2026 | Operator Tender Committee |
| **Bidder Registration & NDA Signing** | October 16, 2026 | Prospective Bidders |
| **Pre-Bid Clarification Meeting (Hybrid)** | October 23, 2026 | Operator & Bidders |
| **Deadline for Written Inquiries / RFIs** | October 30, 2026 | Prospective Bidders |
| **Operator Formal Addendum & Clarifications** | November 6, 2026 | Operator Tender Committee |
| **Tender Submission Deadline (Sealed Bids)** | November 27, 2026 (17:00 PHT) | Bidders |
| **Opening of Technical Envelopes** | November 30, 2026 | Operator Technical Board |
| **Technical Clarifications & Vendor Presentations** | December 1 – 11, 2026 | Shortlisted Bidders |
| **Opening of Commercial & Financing Envelopes** | December 15, 2026 | Operator Commercial Board |
| **Final Contract Negotiation & Award** | January 15, 2027 | Operator & Winning Bidder(s) |
| **Phase 1 Contract Execution & Kickoff** | February 1, 2027 | Operator & Appointed Contractor |
| **Phase 1 Target Commercial Launch (1,000 Sites)** | Q4 2027 (Within 12 Months) | Joint Deployment Team |

---

## 8. INSTRUCTIONS TO BIDDERS & SUBMISSION DETAILS

### 8.1 Clarifications and Communications
All formal communications, requests for interpretation, and tender queries must be submitted in writing via official email to:
* **Tender Secretariat:** `oliver.tungol@comclark.com.ph`
* **Attention:** Technical Evaluation Board / OLIVER TUNGOL (Author)
* **Subject Line:** `[RFP-TELTECH-FWA-2026-001] Technical Clarification Request - <Bidder Name>`

### 8.2 Submission Format
* **Electronic Submission:** One (1) encrypted USB storage device containing PDF and editable Excel files of all volumes, plus cloud upload to the secure Operator Tender Portal.
* **Physical Submission:** Two (2) complete hard-copy sets (One Original, One Duplicate) of Volume I, Volume II, and Volume III, sealed in wax-stamped envelopes delivered to:
  * *Tender Committee, Telecommunications Technology Solutions Incorporated (TelTech) Corporate Headquarters, Metro Manila, Philippines.*

---
*(End of Request for Proposal Specification — Tender Appendices Follow)*
