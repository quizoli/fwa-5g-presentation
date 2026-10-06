# APPENDIX A: TECHNICAL SPECIFICATIONS & COMPLIANCE MATRIX
## 5G FWA NETWORK: RAN, POWER, 5GC, OSS/BSS, RF & MANAGED SERVICES

**Tender Reference:** RFP-TELTECH-FWA-2026-001  
**Project:** Nationwide 5G FWA Project (Band n50, 60 MHz TDD)  
**Operator:** Telecommunications Technology Solutions Incorporated (TelTech)  
**Author:** OLIVER TUNGOL

*Instructions to Bidders: Complete Column D with "C" (Full Compliance), "M" (Minor Deviation - explain in remarks), or "NC" (Non-Compliant). Bidders must provide specific technical values and document references.*

---

### SECTION 1: RADIO ACCESS NETWORK (RAN) TECHNICAL SPECIFICATIONS

| Item ID | Sub-System / Feature | Detailed Specification Requirement | Compliance (C / M / NC) | Bidder Proposed Specification & Reference |
| :--- | :--- | :--- | :---: | :--- |
| **RAN-01** | **3GPP Standard** | 3GPP Release 16 and Release 17 compliant 5G NR Standalone (SA) architecture. | | |
| **RAN-02** | **Frequency Band** | Band n50 (1432 – 1517 MHz, 1.5 GHz L-Band TDD). Full RF support for 1432–1517 MHz. | | |
| **RAN-03** | **Channel Bandwidth** | Continuous 60 MHz channel bandwidth on a single carrier; software-configurable to 40 MHz / 50 MHz / 60 MHz. | | |
| **RAN-04** | **Duplex Mode** | Time Division Duplex (TDD) with flexible frame configuration (e.g., 4:1 DL:UL ratio with special slot 10:2:2). | | |
| **RAN-05** | **Subcarrier Spacing** | 30 kHz Subcarrier Spacing (SCS) with normal cyclic prefix (CP). | | |
| **RAN-06** | **Synchronization** | IEEE 1588v2 Precision Time Protocol (PTP G.8275.1 profile), Synchronous Ethernet (SyncE), and GNSS (GPS/BeiDou/GLONASS) receiver onboard BBU. | | |
| **RAN-07** | **Radio Configuration** | Standard macro site: 3 sectors, 8T8R configuration (3x 8T8R RRU or integrated AAU per site). | | |
| **RAN-08** | **RF Output Power** | Minimum 8x 40W (320W total RF output power per sector/RRU). Digital power control with dynamic power backoff. | | |
| **RAN-09** | **Beamforming** | Digital + analog beamforming (horizontal and vertical); dynamic Multi-User MIMO (MU-MIMO) pairing in DL and UL. | | |
| **RAN-10** | **Modulation Schemes** | Downlink: Up to 256-QAM adaptive modulation.<br>Uplink: Up to 64-QAM / 256-QAM adaptive modulation. | | |
| **RAN-11** | **MIMO Support** | Downlink: Up to 8-layer transmission across multiple users (MU-MIMO); up to 4-layer transmission to single 4R CPE.<br>Uplink: Up to 2-layer single user MIMO; 4-layer MU-MIMO. | | |
| **RAN-12** | **Sector Throughput** | Aggregated single-sector peak throughput >= 450 Mbps in 60 MHz DL under 4:1 TDD frame configuration. | | |
| **RAN-13** | **Subscriber Capacity** | BBU and sector software must support >= 350 active concurrent RRC connected CPEs per sector (>= 1,000 per 3-sector site) without degradation. | | |
| **RAN-14** | **BBU Architecture** | Modular 19" rack-mountable subrack (<= 3U height). Dual hot-swappable -48V DC power supplies. Redundant main control units. | | |
| **RAN-15** | **Fronthaul Interfaces** | Minimum 6x 25GE eCPRI optical interfaces per BBU; support for fiber-saving BiDi transceivers. | | |
| **RAN-16** | **Backhaul Interfaces** | Minimum 2x 10GE + 2x 25GE SFP28 interfaces supporting IP routing, VLAN tagging (802.1Q), and Segment Routing / IP MPLS. | | |
| **RAN-17** | **Environmental Rating** | Outdoor RRU/AAU: IP65 / IP67 ingress protection; operating temperature -40°C to +55°C; wind load resistance up to 250 km/h. | | |
| **RAN-18** | **Energy Saving Modes** | Micro-sleep, symbol shutdown, deep sleep during low-traffic periods, reducing idle power consumption by >= 40%. | | |
| **RAN-19** | **Antenna Specifications** | 8-port cross-pol antenna, 65° horizontal HPBW, >= 17.5 dBi gain, integrated AISG 2.0 internal remote electrical tilt (eRET) adjustable 2° to 12°. | | |
| **RAN-20** | **PIM Performance** | Passive Intermodulation (PIM) <= -153dBc @ 2 x 43 dBm carrier test. | | |

---

### SECTION 2: POWER SYSTEMS & PASSIVE SITE INFRASTRUCTURE

| Item ID | Sub-System / Feature | Detailed Specification Requirement | Compliance (C / M / NC) | Bidder Proposed Specification & Reference |
| :--- | :--- | :--- | :---: | :--- |
| **PWR-01** | **DC Power Plant** | 19" 3U/4U modular high-efficiency switchmode rectifier system; continuous rating >= 6.0 kW @ -48V DC. | | |
| **PWR-02** | **Rectifier Modules** | Hot-swappable 2.0 kW or 3.0 kW modules in N+1 redundant configuration. Operating efficiency >= 96.0%. | | |
| **PWR-03** | **Input Voltage Range** | Wide AC input operating range: 85V AC to 300V AC nominal single phase (230V, 60 Hz), withstanding rural grid fluctuations. | | |
| **PWR-04** | **Lithium Battery (BESS)**| Lithium Iron Phosphate (LiFePO4 / LFP) battery bank: minimum 48V / 150 Ah capacity (>= 7.2 kWh energy storage). | | |
| **PWR-05** | **Battery Autonomy** | Guaranteed >= 4.0hours continuous operation at 2.5–3.0 kW continuous BTS load without AC utility input. | | |
| **PWR-06** | **Battery Cycle Life** | >= 4,000 cycles at 80% Depth of Discharge (DoD) at +25°C; built-in intelligent Battery Management System (BMS). | | |
| **PWR-07** | **Standby Genset** | For Greenfield (Class T4) sites: 15 kVA / 12 kW prime, 230V, 60 Hz diesel generator in sound-attenuated weatherproof canopy (<68dBA @ 7m). | | |
| **PWR-08** | **Fuel Autonomy** | Integrated sub-base fuel tank with minimum 500L–1,000L capacity providing >= 72hours continuous runtime under full load. | | |
| **PWR-09** | **Automatic Transfer (ATS)**| Microprocessor-controlled ATS with 4-pole motorized breaker and mechanical interlock, transferring power within 30 seconds of grid failure. | | |
| **PWR-10** | **Surge Protection** | Coordinated SPD Type 1+2 on AC input (>= 40kA) and DC distribution busbar (>= 20kA). | | |
| **PWR-11** | **TowerCo Tap-Off Kit** | Standardized co-location DC tap box with integrated Class 1.0 revenue-grade kWh energy meter and RS485/Modbus telemetry. | | |
| **PWR-12** | **Grounding & Lightning** | Comprehensive grounding system achieving <= 5.0 Ohms earth electrode resistance; copper busbars and copper-clad steel ground rods. | | |

---

### SECTION 3: 5G CORE NETWORK (5GC SA) & DATACENTER INFRASTRUCTURE

| Item ID | Sub-System / Feature | Detailed Specification Requirement | Compliance (C / M / NC) | Bidder Proposed Specification & Reference |
| :--- | :--- | :--- | :---: | :--- |
| **5GC-01** | **Architecture** | Cloud-native, containerized microservices 5G Standalone (5GC SA) compliant with 3GPP Release 16/17 Service-Based Architecture (SBA). | | |
| **5GC-02** | **Network Functions** | Full NF suite: AMF, SMF, UPF, PCF, UDM, UDR, AUSF, NRF, NSSF, NEF, CHF, and SEPP. | | |
| **5GC-03** | **Subscriber Sizing** | Day-1 licensed capacity: 1,000,000 registered FWA subscribers. Scalable in 500k increments up to 3,000,000 subscribers. | | |
| **5GC-04** | **Geo-Redundancy** | Active-Active geo-redundant dual-datacenter deployment (Metro Manila Primary DC and Clark Pampanga DR DC). | | |
| **5GC-05** | **Hitless Failover** | Automatic session continuity and zero data plane loss during DC failover; state replication across UDR/UDM and SMF clusters. | | |
| **5GC-06** | **UPF Throughput** | UPF dimensioned for >= 80 Gbps usable wire-speed throughput per 2U dual-socket compute node with DPDK and SR-IOV acceleration. | | |
| **5GC-07** | **Carrier-Grade NAT** | Integrated or inline CG-NAT supporting deterministic port allocation, logging per NTC legal intercept mandate, and 10:1 to 16:1 subscriber ratio. | | |
| **5GC-08** | **Deep Packet Inspection** | Embedded DPI capable of Layer-7 application recognition, speed throttling per subscriber tariff tier, and fair-use policy enforcement. | | |
| **5GC-09** | **QoS & Slicing** | 5G QoS Flow mapping (5QI 1, 2, 7, 8, 9) and Network Slicing (S-NSSAI) separating consumer FWA, SME enterprise, and management traffic. | | |
| **5GC-10** | **Datacenter Compute** | Enterprise 2U server nodes (Dual Intel Xeon Gold / AMD EPYC, 512GB RAM, redundant NVMe enterprise SSDs, dual 100GE NICs). | | |
| **5GC-11** | **Datacenter Fabric** | Leaf-spine datacenter networking architecture (32 x 100GE spine switches, 48 x 25GE + 6 x 100GE leaf switches) with EVPN-VXLAN. | | |
| **5GC-12** | **Security & Scrubbing** | Redundant carrier-grade perimeter next-generation firewalls (>= 100 Gbps throughput) and inline anti-DDoS scrubbing appliances. | | |

---

### SECTION 4: CONVERGED DIGITAL OSS/BSS & FIELD FORCE AUTOMATION

| Item ID | Sub-System / Feature | Detailed Specification Requirement | Compliance (C / M / NC) | Bidder Proposed Specification & Reference |
| :--- | :--- | :--- | :---: | :--- |
| **BSS-01** | **Product Catalog & Tariffs**| Configurable telecom product catalog supporting 4 consumer FWA plans (₱599, ₱799, ₱999, ₱1,299), SME tiers, and flexible speed-cap policies. | | |
| **BSS-02** | **Prepaid Charging (CHF)** | Real-time convergent charging system (CCS/CHF) integrated via 3GPP Nchf/Diameter Ro, supporting real-time balance rating and session cutoff. | | |
| **BSS-03** | **Omnichannel Payments** | Native REST API integration with Philippine payment gateways: GCash, Maya (PayMaya), 7-Eleven CLiQQ OTC, Bayad Center, and QR Ph. | | |
| **BSS-04** | **Subscriber Portal & App** | Native Android/iOS subscriber self-care mobile app and responsive web portal for balance checking, online top-up, and speed-test diagnostics. | | |
| **OSS-01** | **Field Force App (FMS)** | Mobile app for field technicians: Real-time work-order dispatch, turn-by-turn navigation, barcode/QR scan of CPE serials, and digital e-signature. | | |
| **OSS-02** | **RF Signal Verification** | Mobile field tool must perform live outdoor RF signal validation (RSRP >= -95 dBm, SINR >= 10 dB) before allowing install closure. | | |
| **OSS-03** | **Dispatch Throughput** | Algorithmic dispatch engine capable of dynamically optimizing and dispatching >= 3,500 installation and maintenance work orders daily. | | |
| **OSS-04** | **CPE Inventory & WMS** | Serialized lifecycle tracking of CPE hardware across central warehouse, technician vehicle float, active subscriber homes, and repossession. | | |
| **OSS-05** | **Reverse Logistics** | Reverse logistics workflow tracking recovered churned CPEs through testing, factory reset, cleaning, re-boxing, and return to stock (>= 70% target). | | |
| **OSS-06** | **Fault & Performance OSS** | Unified multi-vendor EMS/NMS monitoring 5,000 RAN sites, transmission links, and 5G Core with automated RCA and alarm correlation. | | |
| **OSS-07** | **Regulatory Compliance** | Automated generation of quarterly NTC Quality of Service (QoS) and broadband speed performance audit reports. | | |

---

### SECTION 5: RF PLANNING, SITE SURVEY & CLUSTER OPTIMIZATION

| Item ID | Sub-System / Feature | Detailed Specification Requirement | Compliance (C / M / NC) | Bidder Proposed Specification & Reference |
| :--- | :--- | :--- | :---: | :--- |
| **RFP-01** | **Planning Tool** | Carrier-grade RF planning tool (Atoll, Asset, Planet) with high-resolution digital terrain and clutter data (<= 5m resolution). | | |
| **RFP-02** | **Propagation Model** | Calibrated Band n50 (1.5 GHz) 3D ray-tracing / standard propagation model calibrated against local Philippine terrain clutter. | | |
| **RFP-03** | **Nominal Siting & Audit** | Siting validation against 13,746 tower inventory and Converge fiber network backbone routes (subject to verification on the ground); production of candidate search rings. | | |
| **RFP-04** | **Technical Site Survey** | Comprehensive TSSR per site including tower structural load audit, wind-load calculation, panoramic drone photography (360°), and power audit. | | |
| **RFP-05** | **Coverage Target** | Guaranteed outdoor RSRP >= -95 dBm and SINR >= 10 dB across >= 90% of residential settlement footprint in target barangay. | | |
| **RFP-06** | **Single Site Acceptance**| Single Site Verification (SSV) stationary and drive tests verifying sector radiation, antenna RET, PCI, TAC, and max throughput. | | |
| **RFP-07** | **Cluster Tuning** | Cluster optimization across 10–20 site clusters: Interference analysis, tilt/azimuth physical optimization, handover parameter tuning. | | |

---

### SECTION 6: MANAGED SERVICES & 24/7 NETWORK OPERATIONS (MS)

| Item ID | Sub-System / Feature | Detailed Specification Requirement | Compliance (C / M / NC) | Bidder Proposed Specification & Reference |
| :--- | :--- | :--- | :---: | :--- |
| **MS-01** | **24/7 Tier-2/Tier-3 NOC** | Continuous 24/7/365 active monitoring, incident triage, alarm dispatch, and escalation management across all network domains. | | |
| **MS-02** | **Network Availability** | Overall end-to-end radio and core network service availability >= 99.70% monthly SLA. | | |
| **MS-03** | **Critical Incident MTTR** | Mean Time to Restore full service for Critical / Severity-1 outages: <= 2hours in urban areas; <= 4hours in rural areas. | | |
| **MS-04** | **First Line Maint. (FLM)** | Dedicated nationwide field dispatch teams with dedicated 4x4 vehicles, fusion splicers, OTDRs, spectrum analyzers, and climbing gear. | | |
| **MS-05** | **Preventive Maintenance** | Quarterly scheduled site inspections: Antenna bracket torque checks, RF cable weatherproofing, battery impedance tests, genset runs. | | |
| **MS-06** | **Spare Parts Logistics** | Automated SPMS maintaining regional buffer stock; guaranteed Next Business Day (NBD) hardware replacement delivery nationwide. | | |

---
*(End of Appendix A — Technical Specifications & Compliance Matrix)*
