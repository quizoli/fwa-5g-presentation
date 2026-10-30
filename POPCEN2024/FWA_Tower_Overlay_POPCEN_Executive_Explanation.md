# 🗼 Executive Technical Guide: Operational Cell Tower Overlay on POPCEN 2024 (13,735 Towers)

**Author & Lead Architect:** OLIVER TUNGOL, PMP, PECE  
**Entity:** Comclark Network and Technology Corp. / Telecommunications Technology Solutions Inc. (TelTech)  
**Date:** October 28, 2026 (Rev 2.6 Synchronized)  
**Document Code:** FWA-ENG-TOWER-POPCEN-2026-V2.6  
**Target Architecture:** Band n50 (1.5 GHz L-Band TDD) 3-Sector 8T8R MIMO Macro BTS  

---

## 1. Executive Summary

To accelerate time-to-market, minimize civil works CAPEX, and streamline permitting for the **POPCEN 2024 Fixed Wireless Access (FWA) 5G Rollout**, an extensive spatial overlay was executed matching the **5,000 nominal barangay candidate sites** against an expanded master portfolio of **13,735 operational cell towers** across the Philippines (incorporating the **PTCI/MIDC**, **FTAP Globe**, **FTAP Smart**, **FTAP BTS**, **LDIC**, and **Edgepoint** portfolios).

### Key Strategic Findings (POPCEN 2024 Commercial Model)
* **Phase 1 Co-Location Ratio (89.7%):** Out of 1,000 Phase 1 priority sites, **897 sites are within 2.0 km of an operational cell tower**, with **548 sites (54.8%) within immediate walking distance (≤ 0.5 km)**.
* **Nationwide Co-Location Opportunity (90.7%):** Across the entire 5,000-site rollout, **4,536 sites** have existing tower infrastructure within 2.0 km.
* **Minimal Greenfield Exposure (9.3%):** Only **464 sites** nationwide (103 in Phase 1) require greenfield monopole erection.
* **Full Coordinate Transparency (100%):** Every single candidate site now includes both the verified site coordinates (DepEd anchor school WGS84) and the exact nearest TowerCo coordinates (`Nearest Tower Latitude` and `Nearest Tower Longitude`).
* **CAPEX Savings via TowerCo Leasing:** Siting on existing towers replaces ₱1.85M greenfield monopole construction with a standardized monthly TowerCo lease (₱65k–₱85k/mo), reducing Year 1 initial civil works CAPEX by over **₱1.34 Billion**.

---

## 2. Ingested TowerCo Infrastructure Datasets (13,735 Towers)

A total of **13,735 unique operational macro towers** were ingested, validated, and coordinate-harmonized:

| Source Dataset | Operator / Owner | Tower Count | Geographic Footprint & Key Characteristics |
| :--- | :--- | :---: | :--- |
| `09_Towerco_Master_Asset_Inventory.xlsx` (Sheet: FTAP Smart) | Smart Communications / FTAP | **1,023** | Nationwide regional macro towers |
| `09_Towerco_Master_Asset_Inventory.xlsx` (Sheet: FTAP Globe) | Globe Telecom / FTAP | **3,529** | Nationwide urban/suburban macro sites |
| `09_Towerco_Master_Asset_Inventory.xlsx` (Sheet: FTAP BTS) | FTAP BTS (Smart / Globe) | **639** | Dedicated operational BTS macro sites |
| `09_Towerco_Master_Asset_Inventory.xlsx` (Sheet: LDIC) | LBS Digital Infrastructure (LDIC) | **691** | Independent TowerCo sites (Fixed 233 swapped Lat/Lon records; 2 mapped to Globe) |
| `09_Towerco_Master_Asset_Inventory.xlsx` (Sheet: Edgepoint) | EdgePoint Infrastructure | **2,773** | Major independent TowerCo portfolio (Fixed 86 swapped Lat/Lon records) |
| `09_Towerco_Master_Asset_Inventory.xlsx` (Sheet: PTCI-MIDC) | PTCI / MIDC TowerCo | **5,080** | Dedicated independent TowerCo portfolio across Greater Luzon, Visayas, and Mindanao |
| **Consolidated Master Portfolio** | **Multi-TowerCo** | **13,735** | **100% Validated WGS84 coordinates across all 17 regions** |

---

## 3. Mathematical Spatial Overlay Methodology

For each of the 5,000 nominal barangay coordinates from the official POPCEN 2024 rollout plan, the **Haversine great-circle distance** was computed against all 13,735 operational towers:

$$\Delta\sigma = 2 \arcsin \left( \sqrt{\sin^2\left(\frac{\Delta\phi}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta\lambda}{2}\right)} \right), \quad d = 6371.0 \times \Delta\sigma \text{ km}$$

### Nearest Tower Metrics Appended to Model (Columns 33–39):
1. **Column 33 (`Dist to Tower (km)`):** The exact distance from the barangay nominal anchor to the nearest operational tower.
2. **Column 34 (`Nearest Tower ID`):** Site ID code from the TowerCo inventory (e.g., `PH050122`, `S1310`, `PTNEG0050`).
3. **Column 35 (`Nearest TowerCo`):** Operator/Owner (`PTCI-MIDC`, `FTAP Globe`, `FTAP Smart`, `Edgepoint`, `LDIC`, or `FTAP BTS`).
4. **Column 36 (`Nearest Tower Latitude`):** Precise WGS84 Latitude of the nearest tower (formatted to 6 decimal places).
5. **Column 37 (`Nearest Tower Longitude`):** Precise WGS84 Longitude of the nearest tower (formatted to 6 decimal places).
6. **Column 38 (`Tower Screening Class`):** 4-tier co-location engineering classification (Classes T1 to T4).
7. **Column 39 (`Tower Commercial Status`):** Lot allocation and commercial lease recommendation.

---

## 4. Tower Co-Location Classification Framework

| Co-Location Class | Distance Threshold | Operational Recommendation | Commercial & Permitting Impact |
| :--- | :---: | :--- | :--- |
| **Class T1: Immediate Co-loc** | **≤ 0.5 km** | **Immediate TowerCo Lease Agreement** | Zero civil works delay; shared power & shelter; rapid RF antenna mounting. |
| **Class T2: Close Co-loc** | **0.5 – 1.0 km** | **Preferred Co-Location Candidate** | Minor coverage offset easily compensated by 8T8R beamforming; eliminates greenfield CAPEX. |
| **Class T3: Near Co-loc** | **1.0 – 2.0 km** | **RF Propagation Verification** | Viable for Band n50 macro coverage depending on local terrain and clutter. |
| **Class T4: Greenfield** | **> 2.0 km** | **Greenfield Monopole Construction** | Deploy 30m/40m monopole tower; nearest tower coordinates preserved for survey. |

---

## 5. Scoring Integration: Tower Bonus Points

To reflect the substantial commercial and operational advantage of existing infrastructure, **Tower Bonus Points** were directly incorporated into the **Ease of Deployment Pillar (35% Weight)**:

$$\text{Ease Score}_{\text{new}} = \min\left(100, \; \text{Ease Score}_{\text{base}} + \text{Bonus}_{\text{tower}}\right)$$

* **Class T1 (≤ 0.5 km):** **+10 Bonus Points**
* **Class T2 (0.5 – 1.0 km):** **+5 Bonus Points**
* **Class T3 (1.0 – 2.0 km):** **+2 Bonus Points**
* **Class T4 (> 2.0 km):** **+0 Bonus Points**

### Recalculation of Composite Score:
$$\text{Composite Score} = (0.35 \times \text{Ease Score}_{\text{new}}) + (0.35 \times \text{Viability Score}) + (0.30 \times \text{Necessity Score})$$

---

## 6. Distribution Analysis Across Rollout Batches

### Phase 1 Priority (First 1,000 POPCEN Sites):
* **Class T1 (≤ 0.5 km):** **548 sites (54.8%)** — Median distance is just **460 meters**!
* **Class T2 (0.5 – 1.0 km):** **269 sites (26.9%)**
* **Class T3 (1.0 – 2.0 km):** **80 sites (8.0%)**
* **Class T4 (> 2.0 km):** **103 sites (10.3%)**
* **Total Co-Locatable (≤ 2.0 km):** **897 sites (89.7%)**
* **Top TowerCo Partners in Phase 1:** PTCI/MIDC (376), FTAP Globe (314), Edgepoint (172), FTAP Smart (72), LDIC (39), FTAP BTS (27).

### Full Nationwide Program (5,000 Sites):
* **Class T1 (≤ 0.5 km):** **2,127 sites (42.5%)**
* **Class T2 (0.5 – 1.0 km):** **1,519 sites (30.4%)**
* **Class T3 (1.0 – 2.0 km):** **890 sites (17.8%)**
* **Class T4 (> 2.0 km):** **464 sites (9.3%)**
* **Total Co-Locatable (≤ 2.0 km):** **4,536 sites (90.7%)**
* **Top TowerCo Partners Nationwide:** PTCI/MIDC (2,081), FTAP Globe (1,380), Edgepoint (782), FTAP Smart (362), FTAP BTS (211), LDIC (184).

---

## 7. Deliverables & Model Workbooks

* **POPCEN 2024 Master Rollout (39 Columns):** [FWA_Barangay_Rollout_Plan_2024_1000s_Tower_Overlay.xlsx](file:///Users/olivertungol/Downloads/FWA%20Project%20DL/01_POPCEN_Commercial/FWA_Barangay_Rollout_Plan_2024_1000s_Tower_Overlay.xlsx)
* **POPCEN 2024 Dynamic Model (39 Columns):** [FWA_Barangay_Rollout_Plan_2024_1000s_Tower_Overlay_Dynamic.xlsx](file:///Users/olivertungol/Downloads/FWA%20Project%20DL/01_POPCEN_Commercial/FWA_Barangay_Rollout_Plan_2024_1000s_Tower_Overlay_Dynamic.xlsx)
* **POPCEN 2024 Pure Demographic + Towers (32 Columns):** [FWA_Barangay_Rollout_Plan_2024_1000s_Pure_POPCEN_with_Towers_29col.xlsx](file:///Users/olivertungol/Downloads/FWA%20Project%20DL/01_POPCEN_Commercial/FWA_Barangay_Rollout_Plan_2024_1000s_Pure_POPCEN_with_Towers_29col.xlsx)
* **Consolidated Master Tower Inventory:** [09_Towerco_Master_Asset_Inventory.xlsx](file:///Users/olivertungol/Downloads/FWA%20Project%20DL/00_Confidential_Operator_Assets/09_Towerco_Master_Asset_Inventory.xlsx)
* **Online Portal App:** [03_Online_Portal](file:///Users/olivertungol/Downloads/FWA%20Project%20DL/03_Online_Portal)
