# 30-METER HEAVY-DUTY POLYGONAL TUBULAR STEEL MONOPOLE
## DETAILED DESIGN DRAWING (DDD) ENGINEERING & STRUCTURAL CALCULATION MANUAL
**Document Reference:** `TT-DDD-30M-315KPH-150KPA-MANUAL-R0`  
**Release Date:** 26-OCT-2026  
**Lead Technical Architect:** Oliver Tungol  
**Professional Structural Engineer:** Jomar Dogillo, PE  

---

### 1. Executive Summary & Design Basis
This manual is the engineering companion to the 30-Sheet Detailed Design Drawing (DDD) Dossier (`30M_315KPH_150KPA_G1_TelTech-FWA DDD.pdf`). It establishes the technical criteria for nationwide procurement, fabrication, foundation design, and construction of standard 30-meter monopoles for TelTech's Nationwide 5G Standalone (SA) Fixed Wireless Access (FWA) Expansion Program.

- **Design Wind Speed:** NSCP 2015 Section 207 / TIA-222-H Zone 1: **315 km/h** (87.5 m/s, 3-sec gust). Zone 2: 270 km/h, Zone 3 floor: 250 km/h.
- **Soil Bearing Capacity:** qa ≥ 150 kPa (with pre-engineered soft-soil remediation down to 100 kPa).
- **Tower Shaft:** 5 polygonal slip-joint sections (6,000mm length, 1,500mm overlap), ASTM A572 Grade 50 high-strength steel (Fy = 345 MPa), hot-dip galvanized to ≥ 85 µm (ASTM A123).
- **Foundation:** 5.0m × 5.0m × 0.8m mat with 1.8m × 1.8m × 1.2m chimney pedestal (f'_c ≥ 28 MPa).
- **Hold-Down Assembly:** 12x M36 Grade 105 (ASTM F1554) anchor bolts on 1,200mm PCD.
- **Telecom Load:** 3x Band n50 cross-pol macro antennas (30m AGL), 3x 8T8R RRUs (29m AGL), 1x Starlink terminal (10m AGL), future 1.2m MW dish (25m AGL).
- **Power & Earthing:** 12kW rectifiers, 2x 100Ah LiFePO4 batteries, Cadweld grounding grid ≤ 5.0 Ω.

---

### 2. Sectional Geometry & Steel Schedule
| Section | Elevation Range | Length | Base OD | Top OD | Thickness | Steel Grade | Weight (kg) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **S1 (Base)** | 0.00m - 6.00m | 6,000 mm | 1,050 mm | 960 mm | 14 mm | ASTM A572 Gr 50 | 2,240 kg |
| **S2** | 4.50m - 10.50m | 6,000 mm | 982 mm | 892 mm | 12 mm | ASTM A572 Gr 50 | 1,780 kg |
| **S3** | 9.00m - 15.00m | 6,000 mm | 914 mm | 824 mm | 12 mm | ASTM A572 Gr 50 | 1,650 kg |
| **S4** | 13.50m - 19.50m | 6,000 mm | 846 mm | 756 mm | 8 mm | ASTM A572 Gr 50 | 1,020 kg |
| **S5 (Top)** | 18.00m - 30.00m | 12,000 mm | 778 mm | 450 mm | 6 mm | ASTM A572 Gr 50 | 1,180 kg |
| **TOTAL** | **0.00m - 30.00m** | **30.0m** | **1,050 mm** | **450 mm** | **6 - 14 mm** | **Fy = 345 MPa** | **7,870 kg** |

---

### 3. Structural Reactions (Ultimate & Serviceability)
- **Extreme Wind (315 km/h, ULS):** Overturning Moment Mu = 1,850 kN·m, Shear Vu = 145 kN, Axial Pu = 120 kN.
- **Operational Wind (180 km/h, SLS):** Moment Ms = 600 kN·m, Shear Vs = 48 kN, Tip Sway Δ = 185 mm ≤ 300 mm (H/162), Tilt θ = 0.62° ≤ 1.00°.

---

### 4. Foundation Stability & Bearing Verification
- **Applied Maximum Soil Pressure:** q_{{max}} = 118.4 kPa ≤ 150.0 kPa (SF = 2.45 ≥ 2.0).
- **Minimum Soil Pressure:** q_{{min}} = 12.2 kPa > 0 (100% mat bearing, zero uplift).
- **Overturning Factor of Safety:** SF_{{OT}} = 2.15 ≥ 1.50 (+43% margin).
- **Sliding Factor of Safety:** SF_{{SL}} = 1.85 ≥ 1.50 (+23% margin).

---

### 5. Master Drawing Register (30 Sheets)
| Sheet No. | Drawing No. | Sheet Title | Scale | Discipline |
| :---: | :--- | :--- | :---: | :--- |
| Sheet 01 | `TT_AR_000` | COVER PAGE & MASTER DRAWING INDEX | 1:1 | Architectural (General) |
| Sheet 02 | `TT_AR_001` | DESIGN PARAMETERS, MATERIAL SPECS & 3D PERSPECTIVE VIEW | AS SHOWN | Architectural (General) |
| Sheet 03 | `TT_AR_002` | PHILIPPINE BASIC WIND LOAD REGIMES & STRUCTURAL LIMIT STATES | NTS | Architectural (General) |
| Sheet 04 | `TT_AR_003` | SITE LOCATION MAP, SEARCH RING & SITE DEVELOPMENT PLAN | 1:500 | Architectural (General) |
| Sheet 05 | `TT_AR_004` | STANDARD 8.0M x 8.0M COMPOUND PHYSICAL LAYOUT PLAN | 1:100 | Architectural (General) |
| Sheet 06 | `TT_AR_005` | 30-METER MONOPOLE TOWER & COMPOUND ELEVATION VIEW | 1:100 | Architectural (General) |
| Sheet 07 | `TT_ST_001` | MONOPOLE KEY PLAN, SECTIONAL GEOMETRY & STRUCTURAL REACTIONS | 1:50 | Structural / Civil |
| Sheet 08 | `TT_ST_002` | PAD AND CHIMNEY MAT FOUNDATION STRUCTURAL DETAILS | 1:50 | Structural / Civil |
| Sheet 09 | `TT_ST_003` | FOUNDATION REINFORCEMENT & REBAR SECTIONAL ARRANGEMENT | 1:25 | Structural / Civil |
| Sheet 10 | `TT_ST_004` | FOUNDATION REBAR BENDING SCHEDULE & MATERIAL TAKE-OFF | NTS | Structural / Civil |
| Sheet 11 | `TT_ST_005` | BASEPLATE TEMPLATE & HOLD-DOWN ANCHOR BOLT ASSEMBLY | 1:20 | Structural / Civil |
| Sheet 12 | `TT_ST_006` | GENERAL CONCRETE SPECIFICATIONS & CIVIL CONSTRUCTION NOTES | NTS | Structural / Civil |
| Sheet 13 | `TT_ST_007` | STRUCTURAL STEEL FABRICATION, WELDING & GALVANIZING NOTES | NTS | Structural / Civil |
| Sheet 14 | `TT_ST_008` | OUTDOOR EQUIPMENT PAD PLINTH DETAILS (2.0M x 2.0M) | 1:25 | Structural / Civil |
| Sheet 15 | `TT_ST_010` | ELEVATED CABLE GANTRY & CABLE LADDER STRUCTURAL DETAILS | 1:20 | Structural / Civil |
| Sheet 16 | `TT_ST_011` | COMPOUND SECURITY FENCING DETAILS (CYCLONE MESH & RAZOR WIRE) | 1:30 | Structural / Civil |
| Sheet 17 | `TT_ST_012` | COMPOUND ENTRANCE SWING GATE & SECURITY LOCKING ASSEMBLY | 1:25 | Structural / Civil |
| Sheet 18 | `TT_ST_013` | FENCE CORNER POST STIFFENERS & REINFORCED GRADE CURB DETAILS | 1:20 | Structural / Civil |
| Sheet 19 | `TT_ST_014` | SERVICE ENTRANCE PEDESTAL & 230V UTILITY METERING POST | 1:25 | Structural / Civil |
| Sheet 20 | `TT_ST_015` | PERIMETER SECURITY LIGHTING & FIRE EXTINGUISHER ENCLOSURE | 1:20 | Structural / Civil |
| Sheet 21 | `TT_ST_017` | BAND n50 CROSS-POL MACRO ANTENNA MOUNTING BRACKET (30M AGL) | 1:20 | Structural / Civil |
| Sheet 22 | `TT_ST_018` | STARLINK SATELLITE (10M AGL) & FUTURE EXPANSION MOUNTING | 1:25 | Structural / Civil |
| Sheet 23 | `TT_EL_001` | ELECTRICAL SINGLE LINE DIAGRAM (SLD) & POWER DISTRIBUTION | NTS | Electrical / Earthing |
| Sheet 24 | `TT_EL_002` | SITE ELECTRICAL LAYOUT, TRENCHING & CONDUIT ROUTING | 1:100 | Electrical / Earthing |
| Sheet 25 | `TT_EL_003` | SITE EARTHING & GROUNDING GRID LAYOUT PLAN (<= 5.0 OHMS) | 1:100 | Electrical / Earthing |
| Sheet 26 | `TT_EL_004` | MAIN GROUNDING BUSBAR (MGB) & EARTH PIT CONNECTION DETAILS | 1:10 | Electrical / Earthing |
| Sheet 27 | `TT_EL_005` | GROUND TEST PIT & INSPECTION CHAMBER DETAILS | 1:15 | Electrical / Earthing |
| Sheet 28 | `TT_EL_006` | TOWER LIGHTNING DOWN-CONDUCTOR & CADWELD EXOTHERMIC WELDS | 1:20 | Electrical / Earthing |
| Sheet 29 | `TT_EL_008` | FIBER OPTIC LEAD-IN, DUCTING & UNDERGROUND PULL-BOX DETAILS | 1:20 | Electrical / Earthing |
| Sheet 30 | `TT_ST_019` | GEOTECHNICAL SOIL INVESTIGATION & BEARING CAPACITY VERIFICATION | NTS | Structural / Civil |
