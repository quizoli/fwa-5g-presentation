# EXHIBIT A.3.3.3.1: BASIC TOWER & SITE STRUCTURAL DESIGN PARAMETERS
## NTC REGULATORY COMPLIANCE EXHIBIT — 5G FWA TRIAL DEMO (BAND n50)

**Applicant / Operator:** Telecommunications Technology Solutions Incorporated (TelTech)  
**Partner / Network:** Comclark Network and Technology Corp.  
**System Reference:** Nationwide 5G Standalone (SA) Fixed Wireless Access (FWA) — Band n50 (1457.0 – 1517.0 MHz)  
**Lead Technical Architect & Authorized Representative:** OLIVER TUNGOL  
**Structural / Site Plan Engineer:** JOMAR DOGILLO  
**Standard Codes & References:** 
* National Structural Code of the Philippines (NSCP 2015, 7th Edition, Volume 1 — Buildings and Other Vertical Structures, Section 207 Wind Loads)
* TIA-222-G / TIA-222-H: Structural Standard for Antenna Supporting Structures and Antennas
* AISC 360-16: Specification for Structural Steel Buildings
* ASTM A572 / ASTM A123 / ASTM F1554 / ACI 318-14

---

## 1. EXECUTIVE SUMMARY & PURPOSE
This technical exhibit establishes the structural, civil, and environmental design baseline for the standard **30-Meter Heavy-Duty Polygonal Tubular Steel Monopole** and associated **8.0m x 8.0m compound site layout** utilized in the 5G FWA trial network. All structural design calculations, wind pressure determinations, foundation dimensioning, and deflection criteria strictly comply with the latest Philippine wind load regulations (NSCP 2015) and international telecommunication tower structural engineering standards (TIA-222-G/H).

---

## 2. PHILIPPINE BASIC WIND SPEED & WIND ZONE MAPPING (NSCP 2015)

In accordance with **NSCP 2015 Section 207 (Wind Loads)** and PAGASA meteorological historical typhoons data, the structure is designed to withstand the following basic wind speed regimes:

| Parameter | Philippine Wind Zone 1 (High Typhoon Corridor) | Philippine Wind Zone 2 (NCR, Central & West Luzon, Visayas) | Philippine Wind Zone 3 (Low Risk / Inland Mindanao & Palawan) |
| :--- | :---: | :---: | :---: |
| **Applicable Regions** | Batanes, Cagayan, Isabela, Aurora, Quezon, Bicol Region, Samar, Leyte, Dinagat, Surigao | **National Capital Region (NCR), Central Luzon (Pampanga, Bulacan, Tarlac, Bataan), CALABARZON, Iloilo, Cebu** | Palawan, Zamboanga, Davao, Maguindanao, Sulu, Tawi-Tawi |
| **Ultimate Basic Wind Speed ($V$) (3-sec gust)** | **315 km/h (87.5 m/s)** | **270 km/h (75.0 m/s)** | **200 km/h (55.6 m/s)** |
| **Nominal Basic Wind Speed ($V_{\text{asd}}$)** | **245 km/h (68.0 m/s)** | **210 km/h (58.3 m/s)** | **155 km/h (43.1 m/s)** |
| **Occupancy / Structure Category** | Category IV (Standard Telecommunications) / Category III (Essential Comms Facility) | Category IV / Category III | Category IV / Category III |
| **Importance Factor ($I_w$)** | 1.15 (Essential Facility) / 1.00 (Standard) | 1.15 / 1.00 | 1.15 / 1.00 |
| **Exposure Category** | Exposure C (Open flat terrain/farmlands) / Exposure D (Coastal shoreline) | Exposure B (Urban/Suburban) or Exposure C | Exposure B or Exposure C |

---

## 3. TOWER STRUCTURAL DESIGN PARAMETERS & LIMIT STATES

### 3.1 Operational vs. Survivable Wind Speed
* **Survivable / Ultimate Wind Speed ($V_{\text{survival}}$):**
  * **Designed for 270 km/h to 315 km/h** 3-second gust wind speed under Ultimate Limit State (ULS / LRFD strength design per NSCP 2015 and TIA-222-H).
  * Structure, slip-joints, baseplate, and foundation anchorage shall withstand extreme typhoon wind pressures with full operational equipment loading (3x n50 Antennas, 3x 8T8R RRUs, Starlink dish, and future expansion mounts) without plastic deformation, structural failure, or overturning.
* **Operational / Serviceability Wind Speed ($V_{\text{operational}}$):**
  * **Designed for 140 km/h to 160 km/h (40.0 m/s to 44.4 m/s)** continuous operational wind speed under Serviceability Limit State (SLS, 1.0 load factor).
  * Under this wind condition, all active 5G beamforming patterns, MIMO spatial multiplexing, and narrow-beam microwave/satellite transmission links remain within rigid signal integrity thresholds.

---

### 3.2 Allowable Twist, Sway (Tilt), and Verticality (Plumbness)

Under operational wind loading ($V = 140\text{ km/h} - 160\text{ km/h}$) and dead load, the tower deflection shall not exceed the stringent serviceability criteria stipulated below:

| Deflection Parameter | Allowable Limit | Technical Notes & Compliance Rationale |
| :--- | :---: | :--- |
| **Allowable Twist ($\theta_{\text{twist}}$ / Torsional Rotation)** | **$\le \pm 0.5^\circ$ (30 arcmin) for Backhaul / MW**<br>**$\le \pm 1.0^\circ$ (60 arcmin) for Macro Sector** | Torsional rotation at antenna centerline (30.0m AGL) measured about the vertical tower axis. Ensures 5G multi-beamforming alignment and backhaul link availability ($\ge 99.995\%$). |
| **Allowable Sway / Tilt ($\theta_{\text{sway}}$ / Angular Deflection)** | **$\le \pm 1.0^\circ$ (60 arcmin)** | Maximum angular deflection of the tower vertical centerline at 30.0m AGL under operational wind pressure. Prevents beam pattern decoupling over target residential clusters. |
| **Allowable Verticality (Tower Plumbness)** | **$\le 1 : 500$ ($0.20\%$ of Tower Height $H$)** | Out-of-plumb tolerance under still-air dead load. For a **30.0-meter monopole**, maximum horizontal deviation $\Delta \le \mathbf{60\text{ mm}}$ (for 40.0m monopole, $\Delta \le 80\text{ mm}$).<br>Tolerance between consecutive slip-joints: $\le 1 : 1000$ ($0.10\%$). |
| **Horizontal Top Deflection ($\Delta_{\text{top}}$)** | **$\le H / 100$ ($300\text{ mm}$ for 30m tower)** | Lateral service deflection at mast tip under serviceability wind load. |

---

## 4. TOWER & COMPOUND PHYSICAL SPECIFICATIONS

### 4.1 Tower Body & Fabrication
* **Structure Type:** 30-Meter Self-Supporting Polygonal Tubular Steel Monopole (12-sided or 18-sided tapered polygon).
* **Sectional Assembly:** 3 to 4 slip-joint telescoping sections with a minimum overlap length of $1.5 \times \text{inside mating diameter}$.
* **Structural Steel Material:** High-strength structural steel plate conforming to **ASTM A572 Grade 50** ($F_y = 345\text{ MPa} / 50\text{ ksi}$, $F_u = 450\text{ MPa} / 65\text{ ksi}$).
* **Corrosion Protection & Galvanizing:** Hot-dip galvanized per **ASTM A123 / ISO 1461** with minimum zinc coating thickness of $\ge 85\ \mu\text{m}$ ($610\text{ g/m}^2$), providing $\ge 25$-year service life in tropical coastal environments.
* **Climbing Facility:** External climbing ladder equipped with safety rail (fall-arrest cable system per OSHA / EN 353-1) and rest platforms.
* **Internal Cable Routing:** Flanged internal cable access ports with heavy-duty weatherproof cable grommets.

### 4.2 Foundation & Soil Geotechnical Parameters
* **Foundation Configuration:** Reinforced Concrete Mat / Pad and Chimney Pedestal Foundation (or Cast-in-Place Bored Piles depending on site borehole SPT analysis).
* **Concrete Compressive Strength ($f'_c$):** $\ge 28\text{ MPa}$ ($4,000\text{ psi}$) at 28 days (Class A-1 mix design, sulfate-resistant Portland cement).
* **Reinforcing Steel Bars:** Deformed billet steel bars conforming to **ASTM A615 / PNS 49 Grade 60** ($f_y = 414\text{ MPa} / 60\text{ ksi}$).
* **Anchor Bolts:** Heavy-duty anchor bolts conforming to **ASTM F1554 Grade 55 or Grade 105**, hot-dip galvanized per ASTM A153, embedded in reinforced pedestal with dual heavy hex leveling and lock nuts.
* **Assumed Soil Bearing Capacity ($q_a$):** $\ge 150\text{ kPa}$ ($3,130\text{ psf}$) at foundation footing depth (subject to confirmatory soil investigation). Safety Factor $\ge 2.0$ against soil failure; $\ge 1.5$ against overturning and sliding.

### 4.3 Standard Compound Layout ($8.0\text{m} \times 8.0\text{m}$)
* **Compound Footprint:** $64.0\text{ m}^2$ enclosed gravel-surfaced compound with geotextile weed barrier.
* **Perimeter Fencing:** $2.4\text{m}$ high galvanized cyclone wire mesh topped with 3 strands of galvanized concertina razor wire and a $1.2\text{m} \times 2.1\text{m}$ heavy-duty lockable steel entrance gate.
* **Equipment Plinth:** Reinforced concrete equipment pad elevated $+300\text{ mm}$ above natural ground line (NGL) for outdoor integrated power cabinet and lithium battery racks.
* **Service Entrance:** Dedicated 230V, single-phase, 60A / 100A AC utility service post, utility revenue meter, and step-down transformer pad.
* **Lightning & Earthing Grid:**
  * Top-mounted Franklin lightning air terminal extending $\ge 2.0\text{m}$ above top antenna.
  * $70\text{ mm}^2$ bare stranded copper down-conductor exothermically welded (Cadweld) to ground loop.
  * Buried closed-loop perimeter copper ground ring with 4 to 6 copper-clad steel ground rods ($19\text{ mm dia} \times 3.0\text{m}$ length).
  * Measured earth ground resistance: $\mathbf{\le 5.0\ \Omega}$ (tested via 3-point fall-of-potential method).

---

## 5. ANTENNA & RADIO EQUIPMENT LOADING SCHEDULE

| Elevation (AGL) | Sector / ID | Equipment Description | Model / Spec | Weight (kg) | Wind Projected Area ($A_w$) |
| :---: | :---: | :--- | :--- | :---: | :---: |
| **30.0 m** | Sector 1 (0°) | 5G Band n50 Cross-Pol Macro Antenna | Andrew / Amplitech 8-Port | ~24.5 kg | $0.62\text{ m}^2$ |
| **30.0 m** | Sector 1 (0°) | 5G Band n50 8T8R Remote Radio Unit | 8 x 40W RRU | ~38.0 kg | $0.28\text{ m}^2$ |
| **30.0 m** | Sector 2 (120°) | 5G Band n50 Cross-Pol Macro Antenna | Andrew / Amplitech 8-Port | ~24.5 kg | $0.62\text{ m}^2$ |
| **30.0 m** | Sector 2 (120°) | 5G Band n50 8T8R Remote Radio Unit | 8 x 40W RRU | ~38.0 kg | $0.28\text{ m}^2$ |
| **30.0 m** | Sector 3 (240°) | 5G Band n50 Cross-Pol Macro Antenna | Andrew / Amplitech 8-Port | ~24.5 kg | $0.62\text{ m}^2$ |
| **30.0 m** | Sector 3 (240°) | 5G Band n50 8T8R Remote Radio Unit | 8 x 40W RRU | ~38.0 kg | $0.28\text{ m}^2$ |
| **25.0 m** | Reserved | Future Expansion Antenna / Backhaul Mount | 3-Sector Co-location Mount | ~120.0 kg | $1.20\text{ m}^2$ |
| **10.0 m** | Compound | Starlink High-Performance Satellite Terminal | LEO Phased-Array Dish | ~9.2 kg | $0.25\text{ m}^2$ |
| **32.0 m** | Mast Top | Lightning Arrestor / Air Terminal | Franklin Copper Rod | ~5.0 kg | $0.05\text{ m}^2$ |

---

*(End of Exhibit A.3.3.3.1 — Tower & Site Structural Design Parameters)*
