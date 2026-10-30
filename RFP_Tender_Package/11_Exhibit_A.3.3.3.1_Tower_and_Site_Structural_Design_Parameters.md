# EXHIBIT A.3.3.3.1: BASIC TOWER & SITE STRUCTURAL DESIGN PARAMETERS
## NTC REGULATORY COMPLIANCE EXHIBIT — 5G FWA TRIAL DEMO (BAND n50)

**Applicant / Operator:** Telecommunications Technology Solutions Incorporated (TelTech)  
**Partner / Network:** Comclark Network and Technology Corp.  
**System Reference:** Nationwide 5G Standalone (SA) Fixed Wireless Access (FWA) — Band n50 (1457.0 – 1517.0 MHz)  
**Lead Technical Architect & Authorized Representative:** OLIVER TUNGOL, PMP, PECE  
**Structural / Site Plan Engineer:** JOMAR DOGILLO, PE  
**Standard Codes & References:** 
* National Structural Code of the Philippines (NSCP 2015, 7th Edition, Volume 1 — Buildings and Other Vertical Structures, Section 207 Wind Loads)
* TIA-222-G / TIA-222-H: Structural Standard for Antenna Supporting Structures and Antennas
* AISC 360-16: Specification for Structural Steel Buildings
* ASTM A572 / ASTM A123 / ASTM F1554 / ACI 318-14

---

## 1. EXECUTIVE SUMMARY & PURPOSE
This technical exhibit establishes the structural, civil, and environmental design baseline for the standard **30-Meter Heavy-Duty Polygonal Tubular Steel Monopole** and associated **8.0m x 8.0m compound site layout** utilized in the 5G FWA network. All structural design calculations, wind pressure determinations, foundation dimensioning, and deflection criteria strictly comply with the latest Philippine wind load regulations (NSCP 2015) and international telecommunication tower structural engineering standards (TIA-222-G/H).

> [!NOTE]
> **DRAWING ISSUE STATUS & TENDER TYPICAL NOTICE:**  
> The physical layout plans and detailed design drawings associated with this exhibit represent a generic nationwide engineering typical design baseline for 30M monopoles (315 km/h Category 5 survivability, 150 kPa soil bearing capacity). They are issued for tender reference, technical evaluation, and BoQ pricing. Site-specific construction issuance (Issued For Construction / IFC) requires confirmatory borehole geotechnical investigation (SPT), boundary coordinates (WGS84), PE wet-seal authentication, and local LGU building permit approval.

---

## 2. PHILIPPINE BASIC WIND SPEED & WIND ZONE MAPPING (NSCP 2015 VS. PROJECT DESIGN FLOOR)

In accordance with **NSCP 2015 Section 207 (Wind Loads)**, PAGASA historical typhoon recurrence data, and TelTech project engineering guidelines, the structure is designed to withstand the following basic wind speed regimes:

| Parameter | Philippine Wind Zone 1 (High Typhoon Corridor) | Philippine Wind Zone 2 (NCR, Central & West Luzon, Visayas) | Philippine Wind Zone 3 (Inland Mindanao & Palawan) |
| :--- | :---: | :---: | :---: |
| **Applicable Regions** | Batanes, Cagayan, Isabela, Aurora, Quezon, Bicol Region, Samar, Leyte, Dinagat, Surigao | **National Capital Region (NCR), Central Luzon (Pampanga, Bulacan, Tarlac, Bataan), CALABARZON, Iloilo, Cebu** | Palawan, Zamboanga Peninsula, Davao, General Santos, Maguindanao, Sulu, Tawi-Tawi |
| **NSCP 2015 Code Map Minimum (3-sec gust)** | 315 km/h (87.5 m/s) Ult / 245 km/h Nom | 270 km/h (75.0 m/s) Ult / 210 km/h Nom | 200 km/h (55.6 m/s) Ult / 155 km/h Nom |
| **TelTech Mandatory Project Design Floor (V_ult)** | **315 km/h (87.5 m/s)** | **270 km/h (75.0 m/s)** | **250 km/h (69.4 m/s) [Mandatory Project Floor]** |
| **Nominal Design Wind Speed (V_asd)** | **245 km/h (68.0 m/s)** | **210 km/h (58.3 m/s)** | **195 km/h (54.2 m/s) [Mandatory Design Baseline]** |
| **Occupancy / Structure Category** | Category IV (Standard Telecommunications) / Category III (Essential Comms Facility) | Category IV / Category III | Category IV / Category III |
| **Importance Factor (Iw)** | 1.15 (Essential Facility) / 1.00 (Standard) | 1.15 / 1.00 | 1.15 / 1.00 |
| **Exposure Category** | Exposure C (Open flat terrain/farmlands) / Exposure D (Coastal shoreline) | Exposure B (Urban/Suburban) or Exposure C | Exposure B or Exposure C |

> [!IMPORTANT]
> **MANDATORY PROJECT WIND SPEED DESIGN FLOOR (ZONE 3 RULE):**  
> While NSCP 2015 Section 207 / Figure 207A maps Zone 3 (Mindanao / Palawan) with a minimum basic wind speed of 200 km/h (55.6 m/s ultimate) / 155 km/h (nominal), **TelTech strictly enforces a binding project design floor of 250 km/h (69.4 m/s ultimate / 195 km/h nominal)** across all Zone 3 sites (Appendix D §4.1, Bid Bulletin 01 Item 1.4, Master Specs Library, and 30M DDD manual). All structural tower fabrication, member sizing, anchor bolt dimensioning, and foundation design across Zone 3 must be calculated based on V_ult ≥ 250 km/h. Zone 2 sites require V_ult ≥ 270 km/h; Zone 1 sites require V_ult ≥ 315 km/h.

---

## 3. TOWER STRUCTURAL DESIGN PARAMETERS & LIMIT STATES

### 3.1 Operational vs. Survivable Wind Speed
* **Survivable / Ultimate Wind Speed (V_survival):**
  * **Designed for 250 km/h to 315 km/h** 3-second gust wind speed under Ultimate Limit State (ULS / LRFD strength design per NSCP 2015 and TIA-222-H):
    * **Zone 3 (Mindanao & Palawan):** V_ult = **250 km/h (69.4 m/s)** / V_asd = **195 km/h (54.2 m/s)** [Binding Project Design Floor; exceeds NSCP 200 km/h code map].
    * **Zone 2 (NCR, Central Luzon, Visayas):** V_ult = **270 km/h (75.0 m/s)** / V_asd = **210 km/h (58.3 m/s)**.
    * **Zone 1 (Typhoon Corridor / Eastern Seaboard):** V_ult = **315 km/h (87.5 m/s)** / V_asd = **245 km/h (68.0 m/s)**.
  * Structure, slip-joints, baseplate, and foundation anchorage shall withstand extreme typhoon wind pressures with full operational equipment loading (3x n50 Antennas, 3x 8T8R RRUs, Starlink dish, and future expansion mounts) without plastic deformation, structural failure, or overturning.
* **Operational / Serviceability Wind Speed (V_operational):**
  * **Designed for 140 km/h to 160 km/h (40.0 m/s to 44.4 m/s)** continuous operational wind speed under Serviceability Limit State (SLS, 1.0 load factor).
  * Under this wind condition, all active 5G beamforming patterns, MIMO spatial multiplexing, and narrow-beam microwave/satellite transmission links remain within rigid signal integrity thresholds.

---

### 3.2 Allowable Twist, Sway (Tilt), and Verticality (Plumbness)

Under operational wind loading (V = 140 km/h – 160 km/h) and dead load, the tower deflection shall not exceed the stringent serviceability criteria stipulated below:

| Deflection Parameter | Allowable Limit | Technical Notes & Compliance Rationale |
| :--- | :---: | :--- |
| **Allowable Twist (θ_twist / Torsional Rotation)** | **≤ ±0.5° (30 arcmin) for Backhaul / MW**<br>**≤ ±1.0° (60 arcmin) for Macro Sector** | Torsional rotation at antenna centerline (30.0m AGL) measured about the vertical tower axis. Ensures 5G multi-beamforming alignment and backhaul link availability (≥ 99.995%). |
| **Allowable Sway / Tilt (θ_sway / Angular Deflection)** | **≤ ±1.0° (60 arcmin)** | Maximum angular deflection of the tower vertical centerline at 30.0m AGL under operational wind pressure. Prevents beam pattern decoupling over target residential clusters. |
| **Allowable Verticality (Tower Plumbness)** | **≤ 1 : 500 (0.20% of Tower Height H)** | Out-of-plumb tolerance under still-air dead load. For a **30.0-meter monopole**, maximum horizontal deviation Δ ≤ 60 mm (for 40.0m monopole, Δ ≤ 80 mm).<br>Tolerance between consecutive slip-joints: ≤ 1 : 1000 (0.10%). |
| **Horizontal Top Deflection (Δ_top)** | **≤ H / 100 (300 mm for 30m tower)** | Lateral service deflection at mast tip under serviceability wind load. |

---

## 4. TOWER & COMPOUND PHYSICAL SPECIFICATIONS

### 4.1 Tower Body & Fabrication
* **Structure Type:** 30-Meter Self-Supporting Polygonal Tubular Steel Monopole (12-sided or 18-sided tapered polygon).
* **Sectional Assembly:** 3 to 4 slip-joint telescoping sections with a minimum overlap length of 1.5 × inside mating diameter.
* **Structural Steel Material:** High-strength structural steel plate conforming to **ASTM A572 Grade 50** (Fy = 345 MPa / 50 ksi, Fu = 450 MPa / 65 ksi).
* **Corrosion Protection & Galvanizing:** Hot-dip galvanized per **ASTM A123 / ISO 1461** with minimum zinc coating thickness of ≥ 85 µm (610 g/m²), providing ≥ 25-year service life in tropical coastal environments.
* **Climbing Facility:** External climbing ladder equipped with safety rail (fall-arrest cable system per OSHA / EN 353-1) and rest platforms.
* **Internal Cable Routing:** Flanged internal cable access ports with heavy-duty weatherproof cable grommets.

### 4.2 Foundation & Soil Geotechnical Parameters
* **Foundation Configuration:** Reinforced Concrete Mat / Pad and Chimney Pedestal Foundation (or Cast-in-Place Bored Piles depending on site borehole SPT analysis).
* **Concrete Compressive Strength (f'_c):** ≥ 28 MPa (4,000 psi) at 28 days (Class A-1 mix design, sulfate-resistant Portland cement).
* **Reinforcing Steel Bars:** Deformed billet steel bars conforming to **ASTM A615 / PNS 49 Grade 60** (fy = 414 MPa / 60 ksi).
* **Anchor Bolts:** Heavy-duty anchor bolts conforming to **ASTM F1554 Grade 55 or Grade 105**, hot-dip galvanized per ASTM A153, embedded in reinforced pedestal with dual heavy hex leveling and lock nuts.
* **Assumed Soil Bearing Capacity (q_a):** ≥ 150 kPa (3,130 psf) at foundation footing depth (subject to confirmatory soil investigation). Safety Factor ≥ 2.0 against soil failure; ≥ 1.5 against overturning and sliding.

### 4.3 Standard Compound Layout (8.0m × 8.0m)
* **Compound Footprint:** 64.0 m² enclosed gravel-surfaced compound with geotextile weed barrier.
* **Perimeter Fencing:** 2.4m high galvanized cyclone wire mesh topped with 3 strands of galvanized concertina razor wire and a 1.2m × 2.1m heavy-duty lockable steel entrance gate.
* **Equipment Plinth:** Reinforced concrete equipment pad elevated +300 mm above natural ground line (NGL) for outdoor integrated power cabinet and lithium battery racks.
* **Service Entrance:** Dedicated 230V, single-phase, 60A / 100A AC utility service post, utility revenue meter, and step-down transformer pad.
* **Lightning & Earthing Grid:**
  * Top-mounted Franklin lightning air terminal extending ≥ 2.0m above top antenna.
  * 70 mm² bare stranded copper down-conductor exothermically welded (Cadweld) to ground loop.
  * Buried closed-loop perimeter copper ground ring with 4 to 6 copper-clad steel ground rods (19 mm dia × 3.0m length).
  * Measured earth ground resistance: ≤ 5.0 Ω (tested via 3-point fall-of-potential method).

---

## 5. ANTENNA & RADIO EQUIPMENT LOADING SCHEDULE

| Elevation (AGL) | Sector / ID | Equipment Description | Model / Spec | Weight (kg) | Wind Projected Area (Aw) |
| :---: | :---: | :--- | :--- | :---: | :---: |
| **30.0 m** | Sector 1 (0°) | 5G Band n50 Cross-Pol Macro Antenna | Andrew / Amplitech 8-Port | ~24.5 kg | 0.62 m² |
| **30.0 m** | Sector 1 (0°) | 5G Band n50 8T8R Remote Radio Unit | 8 x 40W RRU | ~38.0 kg | 0.28 m² |
| **30.0 m** | Sector 2 (120°) | 5G Band n50 Cross-Pol Macro Antenna | Andrew / Amplitech 8-Port | ~24.5 kg | 0.62 m² |
| **30.0 m** | Sector 2 (120°) | 5G Band n50 8T8R Remote Radio Unit | 8 x 40W RRU | ~38.0 kg | 0.28 m² |
| **30.0 m** | Sector 3 (240°) | 5G Band n50 Cross-Pol Macro Antenna | Andrew / Amplitech 8-Port | ~24.5 kg | 0.62 m² |
| **30.0 m** | Sector 3 (240°) | 5G Band n50 8T8R Remote Radio Unit | 8 x 40W RRU | ~38.0 kg | 0.28 m² |
| **25.0 m** | Reserved | Future Expansion Antenna / Backhaul Mount | 3-Sector Co-location Mount | ~120.0 kg | 1.20 m² |
| **10.0 m** | Compound | Starlink High-Performance Satellite Terminal | LEO Phased-Array Dish | ~9.2 kg | 0.25 m² |
| **32.0 m** | Mast Top | Lightning Arrestor / Air Terminal | Franklin Copper Rod | ~5.0 kg | 0.05 m² |

---

*(End of Exhibit A.3.3.3.1 — Tower & Site Structural Design Parameters)*
