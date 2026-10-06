# APPENDIX C: SERVICE LEVEL AGREEMENTS (SLAS), NETWORK KPIS & LIQUIDATED DAMAGES
## 5G FWA PROGRAM (5,000 SITES NATIONWIDE) **Tender Reference:** RFP-TELTECH-FWA-2026-001 **Project:** Nationwide 5G FWA Project (Band n50, 60 MHz TDD) **Operator:** Telecommunications Technology Solutions Incorporated (TelTech) **Author:** OLIVER TUNGOL --- ## 1. OBJECTIVE & GOVERNANCE PRINCIPLES
This Appendix defines the mandatory Service Level Agreements (SLAs), Key Performance Indicators (KPIs), measurement methodologies, reporting intervals, and financial remedies (Service Credits and Liquidated Damages) governing:
1. **Turnkey Deployment & Commissioning Phases (Lots 1, 2, 5)**
2. **5G Radio & Core Network Operational Performance (Lots 1, 3)**
3. **OSS/BSS Platform Reliability & Field Dispatch Operations (Lot 4)**
4. **Managed Services & First Line Maintenance Operations (Lot 6)** Performance shall be evaluated on a calendar monthly basis using the automated performance management OSS and audited ticketing records. --- ## 2. PROJECT ROLLOUT & DELIVERY SLAS ### 2.1 Milestone Delivery Schedule
The Contractor shall adhere strictly to the following turnkey delivery schedule for Phase 1 (1,000 sites):
* **Milestone 1 (TSSR & Nominal Engineering Approval):** Within **45 Calendar Days** of contract award for all 1,000 priority sites.
* **Milestone 2 (First 200 Sites Commercial On-Air):** Within **120 Calendar Days** of contract award.
* **Milestone 3 (Cumulative 500 Sites Commercial On-Air):** Within **210 Calendar Days** of contract award.
* **Milestone 4 (Cumulative 1,000 Sites Commercial On-Air & Integrated):** Within **365 Calendar Days** of contract award. ### 2.2 Delay Liquidated Damages (Rollout)
* If the Contractor fails to achieve Final Acceptance of a milestone by the scheduled completion date, the Operator shall deduct **Delay Liquidated Damages (DLD)** equal to **0.5% of the total milestone contract value per calendar week of delay**, up to a maximum aggregate cap of **10.0% of the total contract value**.
* Delays exceeding 60 calendar days beyond the milestone date shall entitle the Operator to terminate for default and draw down on the Contractor's Performance Bond. --- ## 3. RADIO ACCESS NETWORK (RAN) OPERATIONAL KPIS & SERVICE CREDITS ### 3.1 Core Radio KPIs (Calculated 24/7/365 Nationwide) ```
Radio Availability (%) = [(Total Operating Cell Hours - Total Unplanned Outage Cell Hours) / Total Operating Cell Hours] * 100
``` | KPI Identifier | Metric Description | Measurement Methodology | Target Standard | Minimum Threshold | Service Credit Penalty (< Threshold) |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **KPI-RAN-01** | **Radio Network Availability** | Monthly aggregate across all active cells | **>= 99.95%** | **99.70%** | 1.0% of monthly O&M fee per 0.1% shortfall |
| **KPI-RAN-02** | **5G Session Setup Success (CSSR)**| Initial RRC connection + 5G QoS flow setup | **>= 99.60%** | **99.00%** | 0.5% of monthly O&M fee per 0.2% shortfall |
| **KPI-RAN-03** | **5G Session Drop Rate (CDDR)** | Abnormal session drops during active data sessions | **<= 0.15%** | **0.50%** | 0.5% of monthly O&M fee per 0.1% excess |
| **KPI-RAN-04** | **Peak Sector DL Throughput** | Busy hour average across cell cluster | **>= 450 Mbps** | **380 Mbps** | Mandatory RF re-tuning within 5 days |
| **KPI-RAN-05** | **Cell-Edge DL User Speed** | 95th percentile stationary CPE speed | **>= 50 Mbps** | **25 Mbps** | Mandatory antenna tilt optimization |
| **KPI-RAN-06** | **Cell-Edge UL User Speed** | 95th percentile stationary CPE upload | **>= 15 Mbps** | **5 Mbps** | Uplink power control re-configuration |
| **KPI-RAN-07** | **Radio Round-Trip Latency (RTT)**| CPE to local gNodeB/UPF edge | **<= 18 ms** | **30 ms** | Audit packet buffering & backhaul |
| **KPI-RAN-08** | **Packet Loss Rate (PLR)** | User plane packet discard rate | **<= 0.01%** | **0.10%** | Transport & radio QoS re-profiling | --- ## 4. 5G CORE NETWORK & CLOUD PLATFORM KPIS ### 4.1 5GC High Availability Benchmarks | KPI Identifier | Metric Description | Measurement Target | Calculation Interval | Liquidated Remedy |
| :--- | :--- | :---: | :---: | :--- |
| **KPI-5GC-01** | **Control Plane NF Availability (AMF/SMF/UDM)** | **>= 99.999%** ("Five Nines") | Monthly | \10,000USD$ per hour outage exceeding threshold |
| **KPI-5GC-02** | **User Plane (UPF) Packet Availability** | **>= 99.999%** | Monthly | \10,000USD$ per hour outage exceeding threshold |
| **KPI-5GC-03** | **PDU Session Establishment Success Rate** | **>= 99.80%** | 24-hr Rolling | Root-cause analysis within 12 hours |
| **KPI-5GC-04** | **CG-NAT Port Allocation Success Rate** | **>= 99.99%** | Monthly | \5,000USD$ penalty for subscriber drop |
| **KPI-5GC-05** | **Active-Active Datacenter Failover Time** | **<= 30Seconds** | Semi-annual Drill | Penalty of 5% annual core AMC if drill fails |
| **KPI-5GC-06** | **UPF Internal Packet Latency** | **<= 1.0 ms** | Continuous | Hardware NIC DPDK tuning | --- ## 5. OSS/BSS & FIELD OPERATIONS SLAS ### 5.1 Commercial & Operational Velocity Metrics | KPI Identifier | Service Level Domain | Mandatory Target | Impact on Failure |
| :--- | :--- | :---: | :--- |
| **KPI-BSS-01** | **Converged Charging System (CHF) Uptime** | **>= 99.99%** | 2.0% monthly BSS maintenance fee deduction |
| **KPI-BSS-02** | **Top-Up Processing Speed (GCash / Maya)** | **<= 3.0Seconds** | Mandatory optimization of API gateway queues |
| **KPI-OSS-01** | **New Installation Dispatch Lead Time** | **<= 48Hours** | >= 95% of orders completed within 48h SLA |
| **KPI-OSS-02** | **First-Time-Right (FTR) Installation Rate**| **>= 96.0%** | Repeat truck rolls at Contractor expense |
| **KPI-OSS-03** | **Churned CPE Hardware Recovery Rate** | **>= 70.0%** | Contractor debited \55USD$ per unrecovered unit below 70% |
| **KPI-OSS-04** | **Automated Work-Order Dispatch Engine Capacity**| **>= 3,500orders/day** | Zero backlog accumulation during peak campaigns | --- ## 6. MANAGED SERVICES & FIELD INCIDENT RESTORATION SLAS ### 6.1 Incident Classification & Mean Time to Restore (MTTR) Incidents logged by the 24/7 NOC are classified into four severity tiers: ```
+---------------------------------------------------------------------------------------------------+
| Severity Level | Definition / Operational Impact | Response SLA | MTTR SLA (Urban) | MTTR SLA (Rural) |
+---------------------------------------------------------------------------------------------------+
| Severity 1 | Complete macro site outage; Core NF failure; | <= 15 Mins | <= 2.0 Hours | <= 4.0 Hours |
| (Critical) | >500 subscribers out of service; major backhaul| | | |
+---------------------------------------------------------------------------------------------------+
| Severity 2 | Single sector down; degraded throughput; | <= 30 Mins | <= 4.0 Hours | <= 6.0 Hours |
| (Major) | loss of DC battery backup; generator fault | | | |
+---------------------------------------------------------------------------------------------------+
| Severity 3 | Non-service affecting hardware fault; loss of | <= 1 Hour | <= 12.0 Hours | <= 24.0 Hours |
| (Minor) | redundancy (single PSU failed, SFP degraded) | | | |
+---------------------------------------------------------------------------------------------------+
| Severity 4 | Configuration inquiry, routine audit, planned | <= 4 Hours | <= 48.0 Hours | <= 72.0 Hours |
| (Warning/Info) | preventative maintenance scheduling | | | |
+---------------------------------------------------------------------------------------------------+
``` ### 6.2 Service Credits for MTTR Breaches
For every hour (or fraction thereof) that a Severity 1 incident exceeds the mandated MTTR threshold, the Operator shall deduct:
* **Urban / Suburban Sites:** **0.5% of monthly site Managed Services fee per hour** of prolonged outage.
* **Rural Sites:** **0.25% of monthly site Managed Services fee per hour** of prolonged outage.
* Total monthly service credit deductions for Managed Services shall be capped at **20.0% of the total monthly Managed Services fee**. --- ## 7. MONTHLY REPORTING & GOVERNANCE CADENCE 1. **Daily Operational Flash Report:** Generated automatically at 06:00 PHT summarizing the previous 24 hours of network availability, outages, MTTR compliance, and work orders.
2. **Weekly Engineering Review:** Joint operations meeting reviewing open trouble tickets, cluster drive tests, and rollout milestone progress.
3. **Monthly Governance & SLA True-Up:** Formal executive session reviewing all KPI metrics against SLA thresholds, finalizing service credits, and approving contractor invoices. ---
*(End of Appendix C — Service Level Agreements, Network KPIs & Liquidated Damages)*
