# Philippine 5G FWA Barangay Rollout Plan — Executive Summary
## Model 2: Official DICT / UNDP GIDA Prioritization Edition (5,000 Sites)

### 1. Strategic Mandate & Framework
Model 2 prioritizes **5,000 Geographically Isolated and Disadvantaged Areas (GIDA)** across the Philippines, driven strictly by the official **DICT / UNDP FPIAP Barangay Prioritization Decision Support Tool** (Looker Studio platform).

Unlike purely commercial models that favor urban fringes with high purchasing power, this GIDA model directs capital expenditure to communities with the highest socio-economic broadband deficit, security vulnerability, and physical isolation, while maintaining carrier-grade technical viability.

---

### 2. Key Rollout Metrics & Phasing Overview

| Metric | Batch 1 (First 1,000) | Batches 1 to 5 (Total 5,000 Sites) | Methodological Rationale |
| :--- | :--- | :--- | :--- |
| **Total Sited Barangays** | **1,000** | **5,000** | Phased national deployment |
| **2024 Population Reach** | **2,247,393** | **16,839,476** | Scaled to PSA 2024 POPCEN (Proc. 973) |
| **Estimated Households** | **589,311** | **4,527,088** | Based on 2024 Provincial HH size matrix |
| **Target Subscribers (30%)** | **176,781** | **1,358,095** | 30% commercial take-up rate |
| **Day 1 BTS Deployed** | **1,000** | **5,000** | 1 BTS per barangay for immediate service |
| **Peak BTS Required** | **1,031** | **5,554** | Dimensioned @ 1,000 subs/BTS (~333/sector) |
| **Average Official GIDA Score** | **54.36 / 69.91** | **48.47 / 69.91** | Looker Studio Multi-Criteria Score |
| **Direct Optical (<3km)** | **373 (37.3%)** | **2,696 (53.9%)** | Direct fiber drop to Converge nodes |
| **Near Optical / MW (3-5km)**| **62 (6.2%)** | **181 (3.6%)** | Short-hop microwave or fiber corridor |
| **Starlink LEO Satellite (>5km)**| **565 (56.5%)** | **2,123 (42.5%)** | High-throughput remote satellite backhaul |

---

### 3. Siting Phasing Breakdown

| Phase | Sites | 2024 Population | 2024 Households | Target Subs (30%) | Day 1 BTS | Peak BTS | Avg GIDA Score | Tier 1 Critical | Direct Fiber (<3km) | Near Fiber (3-5km) | Starlink LEO (>5km) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Batch 1** | 1,000 | 2,247,393 | 589,311 | 176,781 | 1,000 | 1,031 | 54.36 | 1,000 | 373 | 62 | 565 |
| **Batch 2** | 1,000 | 2,913,679 | 760,527 | 228,156 | 1,000 | 1,076 | 50.05 | 577 | 536 | 21 | 443 |
| **Batch 3** | 1,000 | 2,143,214 | 563,931 | 169,181 | 1,000 | 1,020 | 48.69 | 0 | 780 | 13 | 207 |
| **Batch 4** | 1,000 | 3,959,964 | 1,077,889 | 323,360 | 1,000 | 1,153 | 46.48 | 0 | 528 | 31 | 441 |
| **Batch 5** | 1,000 | 5,575,226 | 1,535,430 | 460,617 | 1,000 | 1,274 | 42.79 | 0 | 479 | 54 | 467 |
| **Total** | **5,000** | **16,839,476** | **4,527,088** | **1,358,095** | **5,000** | **5,554** | **48.47** | **1,577** | **2,696** | **181** | **2,123** |

---

### 4. Technical Architecture: Band n50 & Starlink Integration
1. **Single Carrier Spectrum (Band n50, 100MHz TDD)**:
   - Band n50 (1427–1518 MHz) provides propagation characteristics ideally suited for mountainous, heavily forested, and island GIDA terrain.
2. **Dimensioning Standards**:
   - Each BTS node serves up to 1,000 concurrent subscribers across three 120° sectors (~333 per sector).
   - Day 1 begins with 1 BTS per barangay (5,000 total), with peak expansion scaling dynamically to 5,554 BTS.
3. **Transmission Backhaul Resilience**:
   - 2,877 sites (57.5%) are within 5km of Converge optical infrastructure.
   - 2,123 remote sites (42.5%) leverage Starlink Business LEO Satellite terminals, bypassing costly terrestrial fiber trenching.

---

### 5. Official Deliverables in `GIDA/` Folder
- **Standard Excel**: `GIDA/FWA_Barangay_Rollout_Plan_GIDA_1000s.xlsx` (8 reconciled tabs)
- **Dynamic Excel**: `GIDA/FWA_Barangay_Rollout_Plan_GIDA_1000s_Dynamic.xlsx` (Live parameter sensitivity formulas)
- **Metric Mapping**: `GIDA/FWA_Metric_to_Source_Mapping_GIDA.xlsx` & `.csv`
- **GIS Mapping**: `GIDA/FWA_Rollout_Sites_GIDA.kmz`
- **Presentation Deck**: `GIDA/FWA_5G_Barangay_Rollout_Presentation_GIDA.html`
