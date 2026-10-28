# TELECOMMUNICATIONS TECHNOLOGY SOLUTIONS INCORPORATED (TELTECH)
## NATIONWIDE 5G STANDALONE (SA) FIXED WIRELESS ACCESS (FWA) NETWORK
### RFP REFERENCE: RFP-TELTECH-FWA-2026-001

---

# BID BULLETIN NO. 2: COMPREHENSIVE TECHNICAL, OPERATIONAL & COMMERCIAL ADDENDUM
**TO ALL PROSPECTIVE BIDDERS:** All Qualified Bidders, System Integrators, and Authorized Equipment Manufacturers  
**FROM:** Oliver Tungol, Lead Technical Architect & Tender Secretariat  
**DATE OF ISSUANCE:** October 29, 2026  
**SUBJECT:** Technical Baseline Revisions, Engineering Standard Directives, and Contractual Policy Harmonization  

---

> [!IMPORTANT]
> **GOVERNING LEGAL DIRECTIVE:** This **Bid Bulletin No. 2** is formally promulgated pursuant to Section 1.5 (*Clarification and Amendment of Bidding Documents*) of the Master RFP Document. The provisions, technical standards, and commercial rules articulated herein are seamlessly codified as binding contractual addenda to Documents 01 through 09. Prospective bidders must formulate their final 3-envelope submissions strictly in conformance with these unified engineering policies.

---

## 1. EXECUTIVE SUMMARY & TENDER STATUS OVERVIEW

Following detailed technical reviews, preliminary engineering evaluations, and structural harmonization across the 5,000 candidate barangays, TelTech officially issues this comprehensive policy bulletin. This document codifies authoritative directives across eight (8) strategic technical domains:
1. **Cloud-Native 5G SA Core Dimensioning & User Plane Throughput (Lot 3)**
2. **Spectrum Physics, Band n50 Operating Passband & Demarcation Optics (Lot 1 & Lot 6)**
3. **Customer Premises Equipment (CPE) Phased Rollout & Lifecycle Reverse Logistics (Lot 7)**
4. **Civil Works, Monopole Structural Standards & Site Power Infrastructure (Lots 2 & 5)**
5. **Operational SLAs, Radio Network KPIs & SSV Acceptance Standards (Document 04 / Appendix C)**
6. **Digital OSS/BSS, Field Force Automation & VAS Subsystems (Lot 4)**
7. **Candidate Siting Schedule Precision & Geographic Asset Provenance (Document 07)**
8. **Commercial BoQ Harmonization, Multi-Year O&M & 10-Year TCO Rules (Document 06)**

---

## 2. CLOUD-NATIVE 5G CORE (5GC SA) & DATA CENTER ARCHITECTURE (LOT 3)

### 2.1 User Plane Throughput Capacity Dimensioning
1. **Phase 1 Capacity Baseline (1,000,000 Subscribers):**
   - The cloud-native 5G SA Core User Plane Function (UPF) cluster must be physically and logically dimensioned to deliver an initial aggregated user-plane throughput floor of **300 Gbit/s to 500 Gbit/s**.
   - Dimensioning derives from an initial target of 300,000 concurrently active broadband households exhibiting an Average Busy-Hour Throughput (ABHT) of 1.5 Mbit/s to 2.0 Mbit/s per active subscriber at a standard 15% to 20% busy-hour concurrency factor.
2. **Expansion Horizon (3,000,000 Subscribers):**
   - The proposed containerized 5G Core Network Functions (CNF) running on Kubernetes / bare-metal server infrastructure must natively support horizontal auto-scaling of distributed UPF instances up to an aggregated user-plane throughput capacity of **1.5 Tbit/s**.
   - Expansion to 1.5 Tbit/s must be executable via software license expansion and incremental server node deployment without requiring architectural redesign, control plane migration (AMF/SMF/UDM), or database re-sharding.

---

## 3. RADIO ACCESS NETWORK (RAN), BAND n50 SPECTRUM & TRANSMISSION (LOTS 1 & 6)

### 3.1 Spectrum Physics, Operational Channel Window & Emission Suppression
1. **Active Operational Passband:**
   - Under the National Telecommunications Commission (NTC) regulatory framework for dedicated broadband wireless communications, the authorized operational Band n50 carrier is established as **1457.0 MHz to 1517.0 MHz**, providing a contiguous **60 MHz TDD channel bandwidth** operating at 30 kHz Subcarrier Spacing (SCS, 162 Resource Blocks).
2. **Guardband Allocation & Satellite Protection:**
   - A dedicated **1.0 MHz guardband (1517.0 MHz to 1518.0 MHz)** is allocated immediately adjacent to the upper band edge.
   - All gNodeB transceivers must implement sharp digital filtering ensuring out-of-band emissions (OOBE) into the adjacent maritime satellite service band (1518.0 – 1525.0 MHz) do not exceed **-30 dBm/MHz** at the antenna connector, strictly compliant with **ITU-R M.2159-0 / WRC-15 Resolution 223**.
3. **Out-of-Band Emission Limits:**
   - Radiated and conducted unwanted emissions in the adjacent 1432.0–1457.0 MHz block and upper out-of-band spectra must strictly meet **3GPP TS 38.104 Category B** standards with an Adjacent Channel Leakage Ratio (**ACLR $\ge$ 45 dB**).

### 3.2 Baseband Architecture & Form Factor Preferences
1. **Form Factor Preference for Co-Location (897 Sites):**
   - Outdoor blade Baseband Units (blade BBUs) featuring zero ground-footprint pole/wall mounting are strongly preferred across all 897 tower co-location sites. Blade architectures minimize TowerCo compound lease fees and accelerate deployment velocity. Compact outdoor cabinet BBUs are permitted only where indoor shelter space is pre-contracted.
2. **Site Transport Capacity & Optical Transceiver Boundary:**
   - Initial gNodeB backhaul throughput dimensioning of **1 Gbit/s** per site is approved for Day 1 traffic modeling.
   - However, backhaul interfaces must support hardware upgradeability to **10 Gbit/s** via standard SFP+ optical cages.
   - **Demarcation Supply Scope:** The RAN contractor shall supply dual-rate **10GE/25GE eCPRI/Ethernet adaptive optical modules** (1310nm Single-Mode Fiber, LC duplex, 10 km reach) for all BBU optical ports. TelTech shall provide compatible optical transceivers on the transmission demarcation router/switch ports.
   - **Configuration Boundaries:** The RAN contractor executes all BBU port IP address provisioning, VLAN tagging, QoS DSCP priority mapping, and IEEE 1588v2 PTP / SyncE frequency/phase synchronization. TelTech transmission teams configure transport tunneling (MPLS-VPN / SRv6).

---

### 3.3 Nearest Tower Geographic Coordinates & Siting Inventory Precision (Document 07)
1. **Candidate Siting Geographic Precision:**
   - In response to technical simulation requirements, high-precision WGS84 geographic coordinates (6 decimal places) for all nearest co-location towers have been populated in Document 07 (`07_RFP_5G_FWA_Candidate_Site_List_and_Rollout_Schedule.xlsx`) across Tab 'All 5,000 Sites' and Batch 1 through Batch 5.
   - All 60 previously flagged reversed coordinate entries have been fully verified and corrected against audited telecom asset databases.
   - Bidders are reminded that tower coordinate data constitute confidential operator assets provided under the RFP Non-Disclosure Agreement (NDA) solely for RF propagation modeling, link budget simulations, and construction feasibility assessment.

---

## 4. CUSTOMER PREMISES EQUIPMENT (CPE) ROLLOUT & LIFECYCLE REVERSE LOGISTICS (LOT 7)

### 4.1 Phased Hardware Delivery Model
1. **Initial Phase 1 Form Factor:**
   - Recognizing commercial manufacturing timelines for Band n50 outdoor units, TelTech authorizes a phased rollout: Bidders are permitted to supply high-gain 5G Indoor Units (IDU, minimum 8.0–10.0 dBi equivalent antenna gain with integrated 4x4 MIMO and external TS-9/SMA antenna ports) for initial Phase 1 residential deployments.
2. **Outdoor Unit (ODU) Commitment:**
   - Bidders must concurrently submit a firm, contractually committed product delivery roadmap for high-gain Outdoor Units (ODU, $\ge$ 12.0 dBi directional gain, IP67 weather-proofing, pole-mountable) within **6 to 9 months** following contract award.

### 4.2 CPE Warranty vs. Churned Reverse Logistics Lifecycle
1. **Manufacturer Warranty (Defect Liability Period):**
   - All supplied CPE hardware carries a mandatory **24-month (2-year) free replacement warranty** covering internal hardware defects, component burnout, and manufacturing faults.
2. **Churned CPE Recovery Rate ($\ge$ 70%):**
   - The contractual $\ge$ 70% recovery target applies exclusively to **reverse logistics operations executed by field force personnel** retrieving TelTech-owned CPE units from churned or canceled subscriber premises.
   - Recovered units undergo factory diagnostic testing, firmware re-flashing, cosmetic refurbishment, and re-packaging into active forward deployment inventory.
   - Hardware damage resulting from proven subscriber vandalism, fire, or force majeure is excluded from warranty and replenished via the Master Rate Card spare parts schedule.

---

## 5. CIVIL, STRUCTURAL & SITE POWER INFRASTRUCTURE (LOTS 2 & 5)

### 5.1 Class T4 Greenfield Monopoles (103 Sites)
1. **Structural Wind Load Standards:**
   - All newly built Class T4 Greenfield Monopoles must be structurally engineered in compliance with the **National Structural Code of the Philippines (NSCP 2015, 7th Edition) / EIA/TIA-222-G**.
   - Structures must withstand extreme typhoon wind gusts of **270 km/h (Zone 2) up to 315 km/h (Zone 1)** under full design dead load:
     - 6x 5G Remote Radio Units (RRUs);
     - 1x Active Antenna Unit (AAU) or 3x directional passive panel antennas;
     - Up to **1.2 m² total projected windward surface area** for microwave backhaul antennas (equivalent to 1x 1.2m or 2x 0.6m high-wind parabolic dishes);
     - Associated cable ladders, feeder runs, and top lightning protection rod.
2. **Foundation Hydrological Elevation:**
   - **Standard Non-Flood Soils:** Reinforced concrete equipment plinths shall have an elevation of **300 mm (0.30 m)** above finished grade level.
   - **Documented Flood Zones (50-Year Inundation History):** Civil contractors shall construct elevated structural steel equipment platforms raised **1.0 m to 1.5 m** above finished grade level, priced pursuant to the approved Master Rate Card.
3. **Starlink Satellite Backhaul Mounting Interface:**
   - Where hybrid LEO satellite backhaul is designated, contractors shall install a hot-dip galvanized mounting mast (minimum 60 mm / 2.375-inch outer diameter, 2.5 mm wall thickness) with an unobstructed view of the sky. For ground sites, a dedicated gantry standoff arm is utilized; for tower sites, a rigid leg standoff clamp is installed.

### 5.2 AC Electrical Utility Interconnection & Standby Power
1. **Service Entrance Capacity:**
   - AC service drops shall be sized for **100A, 230V single-phase (or 3-phase where commercially available)**.
   - The contractor’s civil/electrical scope includes installation of the weatherhead, service mast, utility-grade meter base, manual transfer switch (MTS), and main AC distribution board with Class I+II Surge Protective Devices (SPD). Utility energization and power billing accounts are administered directly by TelTech.
2. **Site Power Rectifier Architecture (Lot 2):**
   - Each site requires one (1) high-efficiency outdoor-rated rectifier system with N+1 modular switchmode rectifier redundancy (e.g. 3x 50A modules providing 100A continuous N+1 DC output). Remote SNMPv3 / Modbus-TCP telemetry reporting into the centralized OSS is mandatory.
3. **Diesel Generator Fuel at Commissioning:**
   - Contractors are responsible for supplying diesel fuel strictly for generator commissioning and full-load burn-in testing (minimum 4 hours continuous run). Routine fuel replenishment transitions to TelTech O&M upon Provisional Acceptance (PAC).

### 5.3 Technical Site Survey Reports (TSSR) & Drone Sweeps
1. **Panoramic Photographic Standards:**
   - For tower co-location sites (Class T1–T3), contractors shall perform 360° panoramic photographic sweeps at antenna centerline height (and 20m, 30m, 40m AGL) using calibrated drone photographic platforms.
   - In areas where drone operations are legally prohibited by aviation authorities (CAAP restricted airspace, airport buffer zones, military reservations) or severe inclement weather, high-resolution manual panoramic photography captured by certified tower riggers from the tower climbing platform is accepted.

---

## 6. OPERATIONAL SLAS, RADIO NETWORK KPIS & SSV ACCEPTANCE (APPENDIX C)

### 6.1 Radio Performance Indicators (Nationwide 24/7/366)
To harmonize rigorous carrier-grade service quality with real-world FWA wireless propagation environments, the following SLA thresholds are formally enacted:
1. **Call / Session Setup Success Rate (CSSR):**
   - **Target Standard:** **97.0%** (revised from 99.0%)
   - **Minimum Threshold:** **96.0%** (revised from 97.5%)
   - Formula: $\text{CSSR} = \text{RRC Setup Success Rate} \times \text{5G QoS Flow Setup Success Rate} \times 100\%$
2. **Call Drop Rate (CDR):**
   - **Target Standard:** **$\le$ 1.5%** (revised from $\le$ 0.5%)
   - **Maximum Threshold:** **$\le$ 2.0%** (revised from $\le$ 1.0%)
3. **Packet Loss Rate:**
   - Evaluated at the **PDCP (Packet Data Convergence Protocol) Layer** pursuant to 3GPP TS 38.314.
   - **Target Standard:** **$\le$ 0.10%**; **Maximum Threshold:** **$\le$ 0.20%**.
4. **Time-Consistent Busy Hour (TCBH):**
   - Evaluated on a per-cell basis as the rolling continuous 60-minute window demonstrating highest combined uplink/downlink traffic volume over a 30-day observation period.

### 6.2 Service Credit Assessment & Stabilization Governance
1. **Financial Penalty Floor:**
   - Service Credit liquidated damages are assessed **exclusively when monthly performance breaches the Minimum Threshold floor** (or exceeds the Maximum Threshold for CDR/Packet Loss). Performance falling between the Target Standard and Minimum Threshold mandates engineering root-cause analysis and corrective cluster optimization without financial penalty.
2. **Post-PAC Cluster Stabilization Window:**
   - A **90-day stabilization grace period** is granted for each site rollout cluster commencing from Provisional Acceptance (PAC), during which financial Service Credits for Network Availability (NAV) and MTTR are suspended while operational baselines and field spares logistics are stabilized.
3. **OSS Throughput Counters vs. Contractual SLAs:**
   - Financial penalties shall not be assessed against instantaneous OSS cell-edge throughput counters due to dependencies on subscriber traffic distribution and concurrency. Cell-edge speed compliance is governed by Single Site Verification (SSV) and cluster drive acceptance.

### 6.3 Single Site Verification (SSV) Speed Criteria by RSRP Brackets
Single Site Verification stationary throughput benchmarks for a 60 MHz Band n50 channel under a standard 8:2 (DDDDDDDSUU) or 7:3 TDD frame configuration are established as follows:
- **Near Zone (RSRP $\ge$ -80 dBm):** Downlink $\ge$ 200 Mbit/s | Uplink $\ge$ 25 Mbit/s
- **Mid Zone (-95 dBm $\le$ RSRP < -80 dBm):** Downlink $\ge$ 100 Mbit/s | Uplink $\ge$ 10 Mbit/s
- **Cell Edge Zone (-105 dBm $\le$ RSRP < -95 dBm):** Downlink $\ge$ 35 Mbit/s | Uplink $\ge$ 5 Mbit/s  
*(Note: A 5 Mbit/s uplink floor is mandatory to guarantee TCP ACK throughput and interactive voice/video responsiveness).*

### 6.4 Field Installation & Maintenance Metrics
1. **Subscriber Installation Scope:**
   - Encompasses on-site RF signal verification, optimal wall/roof/pole mounting, outdoor weather-sealed Cat6 cabling (up to 30m), PoE injection, indoor Wi-Fi router setup, zero-touch provisioning via FMS app, and verified speed test sign-off.
2. **First-Time-Right (FTR) Installation Rate ($\ge$ 95%):**
   - Calculated monthly as:
     $$\text{FTR Rate} = \left( \frac{N_{\text{completed installations}} - N_{\text{repeat visits within 14 days}}}{N_{\text{completed installations}}} \right) \times 100\%$$
   - Any physical revisit required within fourteen (14) calendar days following sign-off due to workmanship defects, misaligned antennas, or provisioning errors is classified as a failed FTR event.
3. **Spare Parts Management Service (SPMS) NBD Delivery:**
   - Next Business Day (NBD) replacement requires dispatch and physical delivery of replacement spare modules to the **designated regional forward maintenance depot / TelTech regional maintenance center** within the next business day (Monday through Saturday, cut-off 15:00) following RMA notification.

---

## 7. DIGITAL OSS/BSS, FIELD FORCE AUTOMATION & VAS INTEGRATION (LOT 4)

1. **Native Automated Business Intelligence (BI):**
   - The BSS/OSS suite must incorporate an integrated reporting engine providing scheduled generation of operational, billing, subscriber churn, and SLA compliance reports in CSV, Excel, and PDF formats. Furthermore, open database views / secure REST APIs must be exposed for data pipeline ingestion into TelTech’s enterprise data lake.
2. **Cloud Contact Center Integration (CCaaS):**
   - The BSS/CRM platform must expose standard TM Forum Open APIs (**TMF621 Customer Management, TMF622 Product Ordering, TMF632 Party Management**) for single-pane CTI screen-pops, automated customer verification, and unified ticketing integration with TelTech's cloud contact center.
3. **Value-Added Services (VAS) & SMS Gateway Connectivity:**
   - The BSS must provide native **SMPP v3.4 and RESTful SMS gateway adapters** to trigger automated customer notifications (one-time passwords [OTP], billing invoices, payment acknowledgments, and service notifications). TelTech provides the SMS gateway termination service.
4. **Field Force Management (FMS) Mobile Application Capabilities:**
   - **Navigation:** Deep-linking or redirecting from within the FMS app to standard third-party navigation applications (Google Maps, Waze) for routing to site/subscriber coordinates is fully approved.
   - **Electronic Signatures:** Capturing touchscreen handwritten customer signatures on the mobile application upon job completion satisfies formal proof-of-delivery. Third-party digital certificate authorities (PKI/CA) are not required for residential installation orders.
   - **RF Signal Logging:** Certified mobile RF verification tools (e.g. Cellular-Z, G-NetTrack, Nemo Handy, or OEM diagnostic suites) are approved for logging RSRP, RSRQ, SINR, and Cell ID parameters into completion reports.
   - **Automated Service Provisioning:** Work orders successfully validated and signed off on the FMS app must automatically trigger real-time subscriber service activation in the BSS/OSS.
5. **Software SLA Boundary vs. Field Managed Services Scope:**
   - Standalone OSS/BSS software SLAs (Lot 4) govern application availability ($\ge$ 99.95%), transaction processing latency, and API throughput. Field execution metrics (Dispatch Lead Times, FTR Installation Rates, Churned CPE Recoveries) apply strictly to the Managed Services & Field Operations scope (Lot 5 / Appendix E) when awarded.

---

## 8. COMMERCIAL PROPOSAL, 10-YEAR TCO & PROCUREMENT GOVERNANCE (DOCUMENT 06)

1. **Total Pricing Scope (5,000 Candidate Sites):**
   - Commercial proposals must provide firm, fixed unit rates and total pricing based on the complete **5,000 candidate site scope** (Lot 1 through Lot 7). Project deployment shall proceed under the multi-batch rollout roadmap (Phase 1: 1,000 sites; Batches 2–5: 1,000 sites each).
2. **Currency Conversion Benchmark:**
   - For bid evaluation and financial modeling, foreign currency (USD) and local currency (PHP) proposals shall be evaluated using the benchmark conversion rate of **USD 1.00 = PHP 55.00**. For offshore active equipment (Lots 1, 2, 3, 7), contracts and Letters of Credit (LC) may be denominated directly in USD.
3. **Value Added Tax (VAT) Status:**
   - All unit rates, material pricing, and services fees in Document 06 must be quoted **exclusive of 12% Philippine Value Added Tax (VAT-Exclusive)**. VAT will be added as a separate billing item pursuant to Bureau of Internal Revenue (BIR) regulations.
4. **Partial Lot Bidding & Custom Line Items:**
   - Bidders are fully permitted to bid on single Lots or arbitrary combinations of Lots (e.g. RAN only, Core only, Civil only). Non-quoted lots shall be marked 'NO BID'. Custom proprietary hardware or services may be included utilizing the designated custom line-item entry rows.
5. **Years 6–10 OPEX in 10-Year TCO:**
   - Bidders may structure Years 6–10 extended maintenance and managed services pricing as either fixed annual fees or transparent percentage-based annual escalations within Form C of Document 06.
6. **Mandatory OEM Technical Training:**
   - Turnkey proposals must include comprehensive OEM technical training and certification programs covering 5G SA Core administration, Band n50 RF planning/optimization, and OSS/BSS operations for at least twenty (20) TelTech technical personnel.

---
*End of Bid Bulletin No. 2 Draft Policy Document. Prepared for Executive & Legal Review.*
