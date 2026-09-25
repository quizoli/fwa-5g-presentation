# FWA Barangay Rollout Plan — Band n50 BTS Dimensioning & Phasing Master Plan (2024 POPCEN & PSA FIES Edition)

## Executive Summary

To support the commercial rollout of 5G Fixed Wireless Access (FWA) home broadband, an empirical geospatial, demographic, poverty, and radio dimensioning analysis was performed across **41,976 valid barangays** in the Philippines. This edition upgrades the demographic baseline to the newly proclaimed **2024 Census of Population (POPCEN)** (Presidential Proclamation No. 973, declaring national population **112,729,484**) and integrates official **PSA Family Income and Expenditure Survey (FIES)** poverty statistics.

Demographic data is cross-referenced against Converge ICT Solutions' **2,405 backbone nodes** and **4,401 fiber line segments / 334,462 vertices** (`NATIONAL & REGIONAL BACKBONE_NOV 2024_REPORT.kmz`), with verified coordinates for all barangays from the DICT GIDA database.

The evaluation specifies **Band n50 (1432–1517 MHz, 1.5 GHz L-Band TDD)** as the primary access carrier, configured with **60 MHz contiguous channel bandwidth** and 3-sector 4T4R MIMO radio heads.

Per commercial requirements, the radio network is dimensioned for **1,000 subscribers per BTS total (across 3 sectors, ~333 subscribers per sector)**.

The objective is to determine exactly **how many n50 BTS can be deployed in each barangay**, evaluate market necessity (including broadband deficit and FIES poverty), business viability (affordability-adjusted purchasing power), and deployment ease, scheduling rollout across sequential batches of 1,000 sites.

Deliverables in this edition:
- 📊 **C-Level Rollout Model (Standard Baseline)**: `FWA_Barangay_Rollout_Plan_2024_1000s.xlsx` (25 columns with 2024 POPCEN population and exact distance to Converge nodes)
- ⚡ **Dynamic Sensitivity Model (Live Formulas)**: `FWA_Barangay_Rollout_Plan_2024_1000s_Dynamic.xlsx`
- 📋 **Metric to Source Mapping**: `FWA_Metric_to_Source_Mapping_2024.xlsx` (Citing 2024 POPCEN Proclamation No. 973 and FIES)
- 🌍 **Standalone Google Earth KMZ**: `FWA_Rollout_Sites_Master_2024.kmz`
- 🗺️ **Interactive Presentation Deck**: `FWA_5G_Barangay_Rollout_Presentation_2024.html`

---

## Master 5-Batch Rollout & n50 BTS Phasing Summary (2024 POPCEN Reconciled)

| Rollout Phase | Barangays | Initial Day 1 Build (BTS) | Peak 30% Demand Capacity (BTS) | Population (2024) | Addressable Households | Subs @ 30% | Rural % | Avg Dist to Node | Avg Score | Phase Color Code |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Batch 1 (Phase 1)** | **1,000** | **1,000 BTS** | **1,203 BTS** | **7,060,034** | **1,940,365** | **582,100** | 53.1% | 0.59 km | **78.56** | Cyan (`#00B4D8`) |
| **Batch 2 (Phase 2)** | **1,000** | **1,000 BTS** | **1,243 BTS** | **7,410,468** | **2,045,183** | **613,568** | 50.9% | 1.07 km | **72.40** | Cyan (`#00B4D8`) |
| **Batch 3 (Phase 3)** | **1,000** | **1,000 BTS** | **1,184 BTS** | **6,262,888** | **1,726,501** | **517,961** | 54.9% | 1.44 km | **68.75** | Cyan (`#00B4D8`) |
| **Batch 4 (Phase 4)** | **1,000** | **1,000 BTS** | **1,182 BTS** | **6,015,715** | **1,652,354** | **495,723** | 60.9% | 2.54 km | **65.99** | Cyan (`#00B4D8`) |
| **Batch 5 (Phase 5)** | **1,000** | **1,000 BTS** | **1,153 BTS** | **5,590,570** | **1,528,018** | **458,418** | 64.7% | 2.77 km | **63.72** | Cyan (`#00B4D8`) |
| **TOTAL (5 Batches)** | **5,000** | **5,000 BTS** | **5,965 BTS** | **32,339,675** | **8,892,421** | **2,667,770** | **56.9%** | **1.68 km** | **69.88** | Complete 5-Batch Universe |

> **Operational Architecture Note (Option A: Day 1 Build vs. Peak Capacity)**:
> - **Initial Day 1 Build (1,000 BTS per phase / 5,000 BTS total)**: Deploys exactly 1 BTS per priority barangay on Day 1 to establish immediate commercial presence without speculative overbuilding.
> - **Peak 30% Demand Capacity (5,965 BTS total)**: Total subscriber absorption potential dimensioned at 1,000 subscribers per BTS, unlocking organic expansion BTS on existing site footprints without new land acquisition.

---

## Top 20 Priority Showcase Barangays (2024 POPCEN & FIES Scoring)

| Rank | Barangay | Municipality | Province | Region | Pop 2024 | Households | Subs @ 30% | Carrier | Peak 30% Cap | Day 1 Build | Score | Lat | Lon | Dist to Node |
| :---: | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **Poblacion** | Boljoon | Cebu | Region VII (Central Visayas) | 4,263 | 1,122 | 337 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **90.38** | 9.6253 | 123.48013 | 0.20 km |
| **2** | **Poblacion** | Alcoy | Cebu | Region VII (Central Visayas) | 4,032 | 1,061 | 318 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **90.38** | 9.709702 | 123.507311 | 0.14 km |
| **3** | **Poblacion** | Sugbongcogon | Misamis Oriental | Region X (Northern Mindanao) | 3,746 | 961 | 288 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **89.26** | 8.955645 | 124.78832 | 0.13 km |
| **4** | **Matacong** | San Lorenzo Ruiz | Camarines Norte | Region V (Bicol Region) | 3,830 | 958 | 287 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **87.97** | 14.036076 | 122.865496 | 0.12 km |
| **5** | **Dawis Norte** | Carmen | Cebu | Region VII (Central Visayas) | 4,807 | 1,265 | 380 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **87.76** | 10.576567 | 124.018142 | 0.10 km |
| **6** | **Poblacion Zone II** | Capoocan | Leyte | Region VIII (Eastern Visayas) | 4,790 | 1,261 | 378 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **87.76** | 11.293095 | 124.638061 | 0.29 km |
| **7** | **Bacolod** | Irosin | Sorsogon | Region V (Bicol Region) | 4,737 | 1,184 | 355 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **87.76** | 12.701407 | 124.035889 | 0.10 km |
| **8** | **Poblacion North** | San Fernando | Cebu | Region VII (Central Visayas) | 4,710 | 1,239 | 372 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **87.76** | 10.164196 | 123.707844 | 0.21 km |
| **9** | **Tacas** | Pontevedra | Capiz | Region VI (Western Visayas) | 4,684 | 1,233 | 370 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **87.76** | 11.476667 | 122.834722 | 0.16 km |
| **10** | **Abuyog** | City of Sorsogon | Sorsogon | Region V (Bicol Region) | 4,670 | 1,168 | 350 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **87.76** | 12.946322 | 124.052426 | 0.10 km |
| **11** | **Sagrada Familia** | Buhi | Camarines Sur | Region V (Bicol Region) | 4,566 | 1,087 | 326 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **87.76** | 13.415973 | 123.514163 | 0.02 km |
| **12** | **San Isidro** | Castilla | Sorsogon | Region V (Bicol Region) | 4,377 | 1,094 | 328 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **87.76** | 12.973642 | 123.840237 | 0.29 km |
| **13** | **Sacsac** | Bacong | Negros Oriental | Region VII (Central Visayas) | 4,372 | 1,151 | 345 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **87.76** | 9.25467 | 123.290063 | 0.23 km |
| **14** | **Poblacion East** | Oton | Iloilo | Region VI (Western Visayas) | 4,302 | 1,132 | 340 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **87.76** | 10.6914 | 122.478744 | 0.24 km |
| **15** | **Looc** | Villanueva | Misamis Oriental | Region X (Northern Mindanao) | 5,071 | 1,300 | 390 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **87.19** | 8.594267 | 124.773518 | 0.16 km |
| **16** | **Consuelo** | Magsaysay | Misamis Oriental | Region X (Northern Mindanao) | 4,051 | 1,039 | 312 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **87.19** | 8.915472 | 125.187387 | 0.30 km |
| **17** | **Poblacion** | Lagonglong | Misamis Oriental | Region X (Northern Mindanao) | 4,238 | 1,087 | 326 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **87.01** | 8.810485 | 124.789898 | 0.60 km |
| **18** | **Buhang** | Magallanes | Agusan del Norte | Region XIII (Caraga) | 4,178 | 1,019 | 306 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **86.9** | 9.035413 | 125.524987 | 0.25 km |
| **19** | **Diclum** | Manolo Fortich | Bukidnon | Region X (Northern Mindanao) | 5,043 | 1,327 | 398 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **86.6** | 8.373615 | 124.84948 | 0.37 km |
| **20** | **Poblacion** | Kitaotao | Bukidnon | Region X (Northern Mindanao) | 5,364 | 1,412 | 424 | Band n50 (1.5 GHz, 60 MHz) | **1 BTS** | **1 BTS** | **86.5** | 7.634214 | 125.006456 | 0.38 km |

---

## Methodological Upgrades in 2024 POPCEN Edition

1. **Official 2024 POPCEN Integration**:
   - Ingests the July 1, 2024 population counts declared official by President Ferdinand R. Marcos Jr. via Proclamation No. 973.
   - Updates average household size from the 2020 national average of 4.10 down to 3.80 persons/household based on official 2024 census records.

2. **PSA FIES Poverty Incorporation**:
   - Ingests official Family Income and Expenditure Survey (FIES) poverty incidence across Philippine regions (ranging from 1.1% in NCR to 23.5% in BARMM).
   - Necessity Pillar integrates poverty incidence alongside rurality and municipal income class to prioritize high-need digital inclusion markets.
   - Business Viability adjusts addressable demand for purchasing power by discounting households living below the basic subsistence poverty threshold.
