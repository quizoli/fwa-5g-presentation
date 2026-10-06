# 🗼 Executive Technical Guide: Operational Cell Tower Overlay on POPCEN 2024 (13,746 Towers)

**Author:** Oliver Tungol  
**Entity:** Comclark Network and Technology Corp. / Telecommunications Technology Solutions Inc. (TelTech)  
**Date:** October 5, 2026  
**Document Code:** FWA-ENG-TOWER-POPCEN-2026-V2  
**Target Architecture:** Band n50 (1.5 GHz L-Band TDD) 3-Sector 8T8R MIMO Macro BTS  

---

## 1. Executive Summary

To accelerate time-to-market, minimize civil works CAPEX, and streamline permitting for the **POPCEN 2024 Fixed Wireless Access (FWA) 5G Rollout**, an extensive spatial overlay was executed matching the **5,000 nominal barangay candidate sites** against an expanded master portfolio of **13,746 operational cell towers** across the Philippines (incorporating the new **FTAP BTS** and **Edgepoint** portfolios).

### Key Strategic Findings (POPCEN 2024 Commercial Model)
* **Phase 1 Co-Location Ratio (89.7%):** Out of 1,000 Phase 1 priority sites, **897 sites are within 2.0 km of an operational cell tower**, with **548 sites (54.8%) within immediate walking distance (≤ 0.5 km)**.
* **Nationwide Co-Location Opportunity (90.7%):** Across the entire 5,000-site rollout, **4,536 sites** have existing tower infrastructure within 2.0 km.
* **Minimal Greenfield Exposure (9.3%):** Only **464 sites** nationwide (103 in Phase 1) require greenfield monopole erection.
* **CAPEX Savings via TowerCo Leasing:** Siting on existing towers replaces ₱1.85M greenfield monopole construction with a standardized monthly TowerCo lease (₱65k–₱85k/mo), reducing Year 1 initial civil works CAPEX by over **₱1.34 Billion**.

---

## 2. Ingested TowerCo Infrastructure Datasets (13,746 Towers)

A total of **13,746 unique operational macro towers** were ingested, validated, and coordinate-harmonized:

| Source Dataset | Operator / Owner | Tower Count | Geographic Footprint & Key Characteristics |
| :--- | :--- | :---: | :--- |
|  (Sheet: FTAP Smart) | Smart Communications / FTAP | **1,023** | Nationwide regional macro towers |
|  (Sheet: FTAP Globe) | Globe Telecom / FTAP | **3,529** | Nationwide urban/suburban macro sites |
|  (Sheet: FTAP BTS) | FTAP BTS (Smart / Globe) | **639** | **NEW:** Dedicated operational BTS macro sites |
|  (Sheet: LDIC) | LBS Digital Infrastructure (LDIC) | **700** | Independent TowerCo sites (Fixed 233 swapped Lat/Lon records) |
|  (Sheet: Edgepoint) | EdgePoint Infrastructure | **2,775** | **NEW:** Major independent TowerCo portfolio (Fixed 86 swapped Lat/Lon records) |
|  | PTCI / MIDC TowerCo | **5,080** | Dedicated independent TowerCo portfolio across Greater Luzon, Visayas, and Mindanao |
| **Consolidated Master Portfolio** | **Multi-TowerCo** | **13,746** | **100% Validated WGS84 coordinates across all 17 regions** |

---

## 3. Mathematical Spatial Overlay Methodology

For each of the 5,000 nominal barangay coordinates from the official POPCEN 2024 rollout plan, the **Haversine great-circle distance** was computed against all 13,746 operational towers:

34058\Delta\sigma = 2 rcsin \left( \sqrt{\sin^2\left(rac{\Delta\phi}{2}
ight) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(rac{\Delta\lambda}{2}
ight)} 
ight), \quad d = 6371.0 	imes \Delta\sigma 	ext{ km}34058

### Nearest Tower Metrics Appended to Model (Columns 32–35):
1. **Column 32 ():** The exact distance from the barangay nominal centroid to the nearest operational tower.
2. **Column 33 ():** Site ID code from the TowerCo inventory.
3. **Column 34 ():** Operator/Owner (, , , , , or ).
4. **Column 35 ():** 4-tier co-location engineering classification.

---

## 4. Tower Co-Location Classification Framework

| Co-Location Class | Distance Threshold | Operational Recommendation | Commercial & Permitting Impact |
| :--- | :---: | :--- | :--- |
| **Class T1: Immediate Co-loc** | **≤ 0.5 km** | **Immediate TowerCo Lease Agreement** | Zero civil works delay; shared power & shelter; rapid RF antenna mounting. |
| **Class T2: Close Co-loc** | **0.5 – 1.0 km** | **Preferred Co-Location Candidate** | Minor coverage offset easily compensated by 8T8R beamforming; eliminates greenfield CAPEX. |
| **Class T3: Near Co-loc** | **1.0 – 2.0 km** | **RF Propagation Verification** | Viable for Band n50 macro coverage depending on local terrain and clutter. |
| **Class T4: Greenfield** | **> 2.0 km** | **Greenfield Monopole Construction** | Deploy 30m/40m monopole tower; requires local LGU zoning and power drop. |

---

## 5. Scoring Integration: Tower Bonus Points

To reflect the substantial commercial and operational advantage of existing infrastructure, **Tower Bonus Points** were directly incorporated into the **Ease of Deployment Pillar (35% Weight)**:

34058	ext{Ease Score}_{	ext{new}} = \min\left(100, \; 	ext{Ease Score}_{	ext{base}} + 	ext{Bonus}_{	ext{tower}}
ight)34058

* **Class T1 (≤ 0.5 km):** **+10 Bonus Points**
* **Class T2 (0.5 – 1.0 km):** **+5 Bonus Points**
* **Class T3 (1.0 – 2.0 km):** **+2 Bonus Points**
* **Class T4 (> 2.0 km):** **+0 Bonus Points**

### Recalculation of Composite Score:
34058	ext{Composite Score} = (0.35 	imes 	ext{Ease Score}_{	ext{new}}) + (0.35 	imes 	ext{Viability Score}) + (0.30 	imes 	ext{Necessity Score})34058

---

## 6. Distribution Analysis Across Rollout Batches (Updated with FTAP BTS & Edgepoint)

### Phase 1 Priority (First 1,000 POPCEN Sites):
* **Class T1 (≤ 0.5 km):** **548 sites (54.8%)** — Median distance is just **460 meters**!
* **Class T2 (0.5 – 1.0 km):** **269 sites (26.9%)**
* **Class T3 (1.0 – 2.0 km):** **80 sites (8.0%)**
* **Class T4 (> 2.0 km):** **103 sites (10.3%)**
* **Total Co-Locatable (≤ 2.0 km):** **897 sites (89.7%)**
* **Top TowerCo Partners in Phase 1:** PTCI/MIDC (376), FTAP Globe (314), Edgepoint (172), FTAP Smart (72), LDIC (39), FTAP BTS (27).

### Full Nationwide Program (5,000 Sites):
* **Class T1:** 2,127 sites (42.5%)
* **Class T2:** 1,519 sites (30.4%)
* **Class T3:** 890 sites (17.8%)
* **Class T4:** 464 sites (9.3%)
* **Total Co-Locatable (≤ 2.0 km):** **4,536 sites (90.7%)**
* **Top TowerCo Partners Nationwide:** PTCI/MIDC (2,081), FTAP Globe (1,380), Edgepoint (782), FTAP Smart (362), FTAP BTS (211), LDIC (184).

---

## 7. Deliverables & Model Workbooks

* **POPCEN 2024 Master Rollout (35 Columns):** 
* **POPCEN 2024 Dynamic Model (35 Columns):** 
* **Clean 29-Column POPCEN + Towers:** 
* **Consolidated Master Tower List (13,746 Towers):** 
* **POPCEN Commercial 10-Yr Financial Case:** 
* **Master 3-Model Financial Comparison:** 
* **Online Portal:** Launch  in any web browser.
