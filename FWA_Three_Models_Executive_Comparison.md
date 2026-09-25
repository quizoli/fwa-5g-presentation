# Philippine 5G Fixed Wireless Access (FWA) — Three-Model Executive Comparison
## Strategic Comparative Audit: POPCEN 2024 Commercial, DICT/UNDP GIDA, & Combined Hybrid Models

**Date:** September 25, 2026  
**Author & Lead Architect:** OLIVER TUNGOL  
**Target Spectrum & Radio Model:** Band n50 (1427 – 1518 MHz, 100 MHz TDD) — 3-Sector 8T8R MIMO Single-Carrier Deployment  
**BTS Siting Dimensioning Standard:** 1,000 Active Subscribers per BTS (~333 per 120° Sector across 3 Sectors, per TelTech & Comclark RAN Engineering)  
**Transmission Anchor:** Converge ICT National Optical Backbone (2,405 nodes, 45k line vertices) + Starlink Business LEO Satellite  
**Coordinate Standard:** DepEd Schools Locations Masterfile with Zero-Duplicate Spatial Dispersion Engine (100% unique coordinates and latitudes)  
**Scope Note:** Purely focuses on site selection, demographic reach, BTS dimensioning, transmission backhaul, and phased rollout scheduling. Financial Feasibility (FS) cash flow waterfalls and equipment costings are deferred pending final vendor pricing.

---

## 1. Executive Summary & Model Overview

To evaluate optimal capital deployment strategies for nationwide 5G Fixed Wireless Access, three distinct, mathematically reconciled models have been developed across independent directories using the official DepEd Schools Masterfile coordinates:

```
├── POPCEN2024/   -> Model 1: Commercial Viability Model (POPCEN 2024 + Converge Fiber Anchor + FIES)
├── GIDA/         -> Model 2: Official DICT / UNDP GIDA Prioritization Model (11 Looker Studio Criteria)
└── Combined/     -> Model 3: Hybrid Dual-Objective Optimization Model (50% Commercial + 50% Social Impact)
```

### Strategic Objectives of Each Model
1. **Model 1 (`POPCEN2024/`) — Pure Commercial Viability**:
   - **Primary Objective**: Rapid commercial payback, highest addressable subscriber volume, and minimal transmission CAPEX.
   - **Methodology**: Weights **Deployment Ease (35%)**, **Business Viability (35%)**, and **Broadband Necessity (30%)**, heavily favoring barangays within 3km of Converge optical fiber with high population clustering and purchasing power.
2. **Model 2 (`GIDA/`) — Universal Service & Social Impact**:
   - **Primary Objective**: Alleviate severe digital inequality, target marginalized communities, and satisfy government digital inclusion mandates.
   - **Methodology**: Driven strictly by the official **DICT / UNDP Looker Studio Prioritization Decision Support Tool**, evaluating 11 multi-criteria indicators including mobile deficit, road isolation, nighttime lights radiance, POI density, natural disaster hazard, and insurgency risk.
3. **Model 3 (`Combined/`) — Optimized Hybrid Model**:
   - **Primary Objective**: Deliver maximum commercial sustainability while fulfilling public interest obligations and reaching underserved communities.
   - **Methodology**: Blends the Commercial Composite Score (50%) with the Normalized UNDP GIDA Score (50%). Designed with dynamic sensitivity inputs in Excel allowing leadership to adjust weighting from 0% to 100%.

---

## 2. Master Siting & Capacity Comparison Matrix

The table below provides a 100% single-digit mathematically reconciled side-by-side comparison of initial Phase 1 deployment (Batch 1: 1,000 sites) and the full 5,000-site national program across all three models:

| Performance & Siting Dimension | Model 1: POPCEN 2024 (Commercial) | Model 2: DICT / UNDP GIDA (Social Impact) | Model 3: Combined (50/50 Hybrid) | Key Comparative Insights |
| :--- | :---: | :---: | :---: | :--- |
| **Batch 1 Sites** | 1,000 | 1,000 | 1,000 | Initial 1,000-site priority tranche |
| **Total Program Sites** | 5,000 | 5,000 | 5,000 | 5 batches of 1,000 sites |
| **Batch 1 Population Reach** | **7,060,034** | **2,247,393** | **9,100,900** | Combined captures dense unserved catchments |
| **Total Population Reach (5k)** | **32,339,675** | **16,839,476** | **29,840,688** | Commercial covers 32.34M pop; GIDA covers 16.84M |
| **Batch 1 Households** | **1,940,365** | **589,311** | **2,537,442** | Scaled via PSA provincial household matrix |
| **Total Households (5k)** | **8,892,421** | **4,527,088** | **8,177,499** | Combined model captures 8.18M households |
| **Batch 1 Target Subs (30%)** | **582,100** | **176,781** | **761,219** | Combined captures 761k addressable subscribers |
| **Total Target Subs (5k)** | **2,667,770** | **1,358,095** | **2,453,270** | High-demand subscriber pool across 5k sites |
| **Day 1 BTS Deployed** | **1,000 / 5,000** | **1,000 / 5,000** | **1,000 / 5,000** | Standardized 1 BTS per barangay initially |
| **Batch 1 Peak BTS Dimensioned**| **1,203** | **1,031** | **1,420** | Sized @ 1,000 subs/BTS (~333/sector) |
| **Total Peak BTS Dimensioned** | **5,965** | **5,554** | **6,139** | Full expansion node requirements |
| **Batch 1 Direct Optical (<3km)**| **1,000 (100.0%)** | **270 (27.0%)** | **672 (67.2%)** | Direct fiber drop to Converge optical nodes |
| **Total Direct Optical (<3km)** | **4,611 (92.2%)** | **1,350 (27.0%)** | **2,486 (49.7%)** | Major CAPEX savings via fiber colocation |
| **Batch 1 Near Optical (3-5km)** | **0 (0.0%)** | **147 (14.7%)** | **129 (12.9%)** | Short-hop microwave / fiber lateral corridor |
| **Total Near Optical (3-5km)** | **384 (7.7%)** | **537 (10.7%)** | **727 (14.5%)** | Feeder link deployment |
| **Batch 1 Starlink LEO (>5km)** | **0 (0.0%)** | **583 (58.3%)** | **199 (19.9%)** | High-throughput remote satellite backhaul |
| **Total Starlink LEO (>5km)** | **5 (0.1%)** | **3,113 (62.3%)** | **1,787 (35.7%)** | GIDA relies heavily on satellite due to isolation |
| **Batch 1 Average Metric Score** | 78.56 / 100 | 54.36 / 69.91 (77.8%) | 64.20 / 100 | Looker raw score vs standardized scores |
| **Total 5k Average Metric Score**| 69.88 / 100 | 48.47 / 69.91 (69.3%) | 56.49 / 100 | High score retention across all 5 phases |
| **Coordinate Duplicate Count** | **0 (0.0%)** | **0 (0.0%)** | **0 (0.0%)** | 100% unique lat/long down to 6 decimals |

---

## 3. Site Overlap & Congruence Analysis

A spatial and administrative congruence audit was executed across all candidate barangays using official PSGC identifiers to measure the degree of site overlap between the three reconciled models.

### Batch 1 (Top 1,000 Sites) Overlap Matrix
```
+------------------------------------+-----------------+-----------------+--------------------+
| Batch 1 Overlap Matrix             | Model 1: POPCEN | Model 2: GIDA   | Model 3: Combined  |
+------------------------------------+-----------------+-----------------+--------------------+
| Model 1: POPCEN 2024 (Commercial)  |  1,000 (100.0%) |       4 (0.4%)  |      81 (8.1%)     |
| Model 2: DICT / UNDP GIDA (Social) |      4 (0.4%)   |  1,000 (100.0%) |     339 (33.9%)    |
| Model 3: Combined Hybrid (50/50)   |     81 (8.1%)   |    339 (33.9%)  |   1,000 (100.0%)   |
| 3-Way Core Intersection (All 3)    |                 4 sites in common (0.4%)               |
+------------------------------------+-----------------+-----------------+--------------------+
```

### Full Program (Total 5,000 Sites) Overlap Matrix
```
+------------------------------------+-----------------+-----------------+--------------------+
| Total 5,000 Overlap Matrix         | Model 1: POPCEN | Model 2: GIDA   | Model 3: Combined  |
+------------------------------------+-----------------+-----------------+--------------------+
| Model 1: POPCEN 2024 (Commercial)  |  5,000 (100.0%) |     286 (5.7%)  |   1,680 (33.6%)    |
| Model 2: DICT / UNDP GIDA (Social) |    286 (5.7%)   |  5,000 (100.0%) |   2,791 (55.8%)    |
| Model 3: Combined Hybrid (50/50)   |  1,680 (33.6%)  |  2,791 (55.8%)  |   5,000 (100.0%)   |
| 3-Way Core Intersection (All 3)    |               286 sites in common (5.7%)             |
+------------------------------------+-----------------+-----------------+--------------------+
```

### Root Cause Analysis of the Divergence
1. **Commercial vs. GIDA Divergence (0.4% Batch 1 / 5.7% Total Overlap)**:
   - **Commercial Model** selects densely populated, lower-poverty barangays directly situated on national highways and within 1-2 km of Converge fiber nodes (e.g., Batangas, Cavite, Bulacan, Laguna, Pampanga, Pangasinan).
   - **GIDA Model** explicitly penalizes road proximity and awards maximum points to physical isolation, lack of mobile coverage, low nighttime light radiance, and security vulnerabilities (e.g., Mountain Province, Benguet, Ilocos Norte, Samar, Sulu, Basilan).
2. **Combined Model as the Strategic Bridge**:
   - Model 3 captures **1,680 commercial priority sites (33.6%)** and **2,791 official GIDA sites (55.8%)**, creating a pragmatic bridge.
   - It identifies the "Goldilocks Zone": barangays with genuine broadband deprivation and official GIDA status that are nonetheless within reach of terrestrial fiber or viable microwave paths.

---

## 4. Transmission & Backhaul Infrastructure Strategy

```
Model 1 (POPCEN 2024 Commercial):
  Direct Optical (<3km) : 92.2% [==================  ] 4,611 sites
  Near Optical (3-5km)  :  7.7% [==                  ] 384 sites
  Starlink LEO (>5km)   :  0.1% [                    ] 5 sites

Model 2 (DICT / UNDP GIDA):
  Direct Optical (<3km) : 27.0% [======              ] 1,350 sites
  Near Optical (3-5km)  : 10.7% [==                  ] 537 sites
  Starlink LEO (>5km)   : 62.3% [============        ] 3,113 sites

Model 3 (Combined Hybrid):
  Direct Optical (<3km) : 49.7% [==========          ] 2,486 sites
  Near Optical (3-5km)  : 14.5% [===                 ] 727 sites
  Starlink LEO (>5km)   : 35.7% [=======             ] 1,787 sites
```

### Technical Implications
- **Terrestrial Fiber Trenching vs. Satellite Capex**:
  - In **Model 1**, 99.9% of sites are within 5km of fiber, requiring minimal civil works.
  - In **Model 2**, 62.3% (3,113 sites) require **Starlink Business LEO satellite terminals** due to extreme terrain (islands, deep cordilleras). This eliminates multimillion-peso fiber buildouts and allows 48-hour turn-up, but introduces ongoing satellite transponder OPEX.
  - In **Model 3**, Starlink usage is contained to 35.7% (1,787 sites), striking an optimal balance between fiber speed and satellite reach.

---

## 5. Strategic Trade-Offs & Leadership Recommendations

| Strategic Criteria | Model 1: Commercial (POPCEN 2024) | Model 2: GIDA (UNDP / DICT) | Model 3: Combined Hybrid |
| :--- | :--- | :--- | :--- |
| **Primary Beneficiary** | Paying households, dense rural towns | Acute unserved, vulnerable GIDA LGUs | Balanced commercial + underserved |
| **Revenue Turn-Up Speed** | **Fastest** (Large paying population) | **Slowest** (High poverty, lower ARPU) | **Balanced & Resilient** |
| **Transmission Cost** | **Lowest** (92.2% on fiber backbone) | **Highest** (62.3% satellite backhaul) | **Low** (49.7% on fiber backbone) |
| **Regulatory & Subsidy Alignment**| Lower qualification for USF grants | **100% Eligible** for DICT / UNDP funds | **High Eligibility** for PPP subsidies |
| **Recommended Use Case** | Pure private telecom CAPEX rollout | Government-funded universal service | **Joint Public-Private Partnership (PPP)** |

### Leadership Recommendation: The Phased Hybrid Compromise
If the rollout is funded as a **commercial venture with private capital**, leadership should adopt **Model 3 (Combined Hybrid)** as the primary baseline:
1. **Immediate Execution (Batch 1)**: Deploy the 1,000 hybrid sites, securing 761,219 target subscribers while capturing 672 direct optical nodes and 339 official GIDA communities.
2. **Concession & Grant Leverage**: Use the 2,791 overlapping GIDA sites in Model 3 to negotiate spectrum fee rebates, right-of-way exemptions, and universal service subsidies from DICT and the National Telecommunications Commission (NTC).
3. **Dynamic Re-Tuning**: In the generated `FWA_Barangay_Rollout_Plan_Combined_1000s_Dynamic.xlsx`, executives can instantly simulate shifting weights (e.g., 70% Commercial / 30% GIDA or vice versa) via yellow input cells `B5` and `B6`.

---

## 6. Complete Deliverables Directory Across All Models

All three models have been fully generated, mathematically reconciled, and placed in their respective self-contained folders and the consolidated release package:

```
├── 2026-09-25_Revised_Models/                             (Unified Master Release Package)
│   ├── FWA_Barangay_Rollout_Plan_2024_1000s.xlsx          (Model 1 Standard, 0 Duplicates)
│   ├── FWA_Barangay_Rollout_Plan_2024_1000s_Dynamic.xlsx  (Model 1 Dynamic Sensitivity)
│   ├── FWA_Barangay_Rollout_Plan_GIDA_1000s.xlsx          (Model 2 Standard, 0 Duplicates)
│   ├── FWA_Barangay_Rollout_Plan_GIDA_1000s_Dynamic.xlsx  (Model 2 Dynamic Sensitivity)
│   ├── FWA_Barangay_Rollout_Plan_Combined_1000s.xlsx      (Model 3 Standard, 0 Duplicates)
│   ├── FWA_Barangay_Rollout_Plan_Combined_1000s_Dynamic.xlsx (Model 3 Dynamic Sensitivity)
│   ├── FWA_Rollout_Sites_Master_2024.kmz & .kml           (Model 1 GIS Layers)
│   ├── FWA_Rollout_Sites_GIDA.kmz & .kml                  (Model 2 GIS Layers)
│   ├── FWA_Rollout_Sites_Combined.kmz & .kml              (Model 3 GIS Layers)
│   └── FWA_Three_Models_Executive_Comparison.md           (This master comparative report)
│
├── POPCEN2024/                                            (Model 1 Root Folder)
├── GIDA/                                                  (Model 2 Root Folder)
└── Combined/                                              (Model 3 Root Folder)
```
