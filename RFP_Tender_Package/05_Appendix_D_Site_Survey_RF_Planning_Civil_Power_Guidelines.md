# APPENDIX D: SITE SURVEY, RF PLANNING & CIVIL/POWER ENGINEERING GUIDELINES
## 5G FWA PROGRAM (5,000 SITES NATIONWIDE)

**Tender Reference:** RFP-TELTECH-FWA-2026-001  
**Project:** Nationwide 5G FWA Project (Band n50, 60 MHz TDD)  
**Operator:** Telecommunications Technology Solutions Incorporated (TelTech)  
**Author:** OLIVER TUNGOL

---

## 1. ENGINEERING PRINCIPLES & SITING ARCHITECTURE

### 1.1 Siting Philosophy & Mandatory 3-Tier Sourcing Hierarchy
The primary engineering objective of the 5G FWA rollout is to maximize household population coverage within high-density suburban and rural barangay settlement clusters while minimizing civil capital expenditures and permitting lead times. To achieve rapid 1,000-site Phase 1 execution within 12 months, the Contractor shall execute site delivery strictly following the **Mandatory 3-Tier Infrastructure Sourcing Hierarchy**:
1. **Tier 1 (Mandatory Baseline — Existing TowerCo Co-Location):** Field teams must prioritize co-location on existing operational towers (PTCI/MIDC, EdgePoint, FTAP Globe, FTAP Smart, LDIC, Phil-Tower) located within the designated search ring. The Operator leverages an audited master database of **13,746 operational towers**. Co-location reduces Ready-for-Installation (RFI) lead times from 120–180 days down to 15–30 days while eliminating private land titling and environmental permitting complexities.
2. **Tier 2 (Secondary — TowerCo Build-to-Suit / B2S):** If all existing towers within the search ring exceed structural loading thresholds (EPA limits) or fail RF line-of-sight requirements, the vendor shall engage a licensed Independent TowerCo to execute a Build-to-Suit (B2S) under TelTech's Master Lease Agreement (MLA).
3. **Tier 3 (Restricted Exception — Operator Greenfield Own-Build):** Direct operator-constructed greenfield monopoles are strictly limited to remote isolated barangays located > 2.0 km from any operational tower structure (~9.3% of sites nationwide; 103 sites in Phase 1). Proposing an own-build greenfield site requires formal written submission of **Structural Denial / Space Unavailability Letters** from at least two (2) licensed TowerCos and written sign-off from the TelTech Project Steering Committee.

### 1.2 Search Ring Specification & Demand Centroid
For each nominal site location assigned in Document 07 (Candidate Site List):
* **Urban & Suburban Search Ring:** Defined as a circle with a radius of **500 meters** centered on the official nominal barangay demand centroid.
* **Rural & Remote Search Ring:** Defined as a circle with a radius of **1,000 meters** (expandable up to 1,500 meters upon TelTech RF approval only if prominent terrain ridges or hills provide superior line-of-sight).
* **Target Coverage Guarantee:** Sited candidate coordinates must achieve unobstructed Line-of-Sight (LOS) and target RSRP coverage ($\ge -95\text{ dBm}$) across $\ge 90\%$ of the inhabited settlement zone.

### 1.3 Mandatory Three-Candidate Rule (Candidates A, B, C)
For every search ring, the Turnkey Contractor / Site Acquisition Vendor must survey, evaluate, and submit **exactly three (3) distinct candidates** in the Technical Site Survey Report (TSSR):
* **Candidate A (BEST — Primary Recommended):** Optimal TowerCo co-location asset (or prime site) with immediate structural capacity at $\ge 30\text{m}$ AGL, available $-48\text{V}$ DC busbar or commercial AC transformer headroom, nearest fiber node, and fastest projected RFI ($\le 21\text{ calendar days}$).
* **Candidate B (BETTER — Secondary Target / Backup 1):** Fully compliant alternative TowerCo structure or site within the search ring requiring minor solvable modifications (e.g., dedicated AC sub-meter installation, mount bracket extensions, or secondary fiber lead-in route).
* **Candidate C (GOOD — Contingency / Fallback):** Third viable TowerCo asset or TowerCo Build-to-Suit option, ensuring the search ring is not stalled if Candidates A and B encounter unforeseen structural or commercial deadlocks.
* **14-Day Lease / SAA Escalation Protocol:** If the Site Application & Allocation (SAA) or Service Order (SO) negotiation for Candidate A stalls or exceeds **14 calendar days**, the vendor is contractually mandated to immediately activate and lock **Candidate B** to prevent project schedule slippage.

### 1.4 Co-Location Candidate Evaluation Criteria Matrix (100-Point Scoring)
Field teams and SAQ specialists shall evaluate all candidates using the standardized scoring rubric:
* **Space & Structural Capacity (20%):** Antenna mounting space at $\ge 30\text{m}$ to $45\text{m}$ AGL, wind load headroom for 3x n50 antennas + 3x 8T8R RRUs ($\le 45\text{ kg}$ each), and $\ge 2.0\text{m} \times 2.0\text{m}$ compound ground space for outdoor rectifier/battery cabinets.
* **Access Road & Compound Security (15%):** All-weather paved/concrete road access, established TowerCo security fencing/guarding, and 24/7 unobstructed Operations & Maintenance (O&M) ingress/egress.
* **RF Line-of-Sight & Propagation (25%):** Dominant ground elevation AMSL, clear first Fresnel zone into residential settlement, zero close-in clutter shielding within $200\text{m}$ of sector azimuths ($0^\circ, 120^\circ, 240^\circ$).
* **Backhaul Transport Proximity (15%):** Proximity to Converge/TelTech fiber distribution closure (Class A $\le 0.5\text{km}$, Class B $\le 1.0\text{km}$), existing TowerCo cable ladder/conduit entry, or unobstructed northern sky view ($0^\circ - 80^\circ$ elevation arc) for Starlink satellite backhaul.
* **Power Availability & Utility Infrastructure (15%):** Commercial utility grid transformer capacity, available $-48\text{V}$ DC busbar tap ($\ge 63\text{A}$) or space for dedicated AC service entrance sub-meter, and shared backup genset/battery support.
* **Lease & Commercial Terms (10%):** Fast-track Service Order execution under existing TowerCo Master Lease Agreement (MLA), monthly recurring fee within budget, and guaranteed RFI timeline $\le 30\text{ calendar days}$.

---

## 2. DETAILED TECHNICAL SITE SURVEY REPORT (TSSR) REQUIREMENTS

For every nominal site candidate, the Contractor shall complete and submit a comprehensive TSSR conforming to the following structure:

### 2.1 General Site Identification & Geography
* Site Name, Candidate ID, Official PSGC Code, Region, Province, Municipality, and Barangay.
* Precision WGS84 GPS Coordinates (Latitude, Longitude recorded with >= 6 decimal places via dual-frequency GPS receiver).
* Ground Elevation Above Mean Sea Level (AMSL in meters).
* Access Road Assessment: Road surface type (concrete, asphalt, macadam, dirt trail), bridge weight limits, and 4x4 hauling accessibility during monsoon seasons.

### 2.2 Tower Structure & Loading Audit (Co-Location Sites)
* Operating TowerCo Entity (PTCI/MIDC, FTAP Globe, EdgePoint, FTAP Smart, LDIC, FTAP BTS).
* Tower Type (Self-Supporting 3-Leg/4-Leg Tower, Monopole, Guyed Mast, Rooftop Tower).
* Tower Height Above Ground Level (AGL in meters).
* Structural Space Audit: Proposed mounting height for 3x Band n50 antennas (recommended centerline: 30m to 45m AGL).
* Structural Loading Verification: Confirmation that existing tower members and foundation can accommodate additional 3x 8T8R RRUs/AAUs (< 45 kg each) and wind load profile of 250 km/h.
* Panoramic Drone Photographic Survey: High-resolution 360° continuous panoramic video and 12-cardinal-point still photos at proposed antenna centerline height to verify optical line-of-sight across populated settlements.

### 2.3 Power Infrastructure & Utility Audit
* Existing Commercial AC Utility Power: Electric Cooperative / Distribution Utility name (e.g., MERALCO, PELCO, BENECO, CAPELCO, ILPI).
* Service Entrance Capacity: Transformer rating (kVA), service voltage (230V / 400V, 60 Hz), breaker rating, and phase balance.
* TowerCo DC Power Availability: Sourcing from TowerCo DC busbar (-48V DC) vs. installing Operator-dedicated rectifier subrack.
* Sub-metering feasibility and cable tray routing for power cables.
* Grounding System Audit: Measurement of existing earth ground resistance using a 3-point fall-of-potential earth tester. Earth resistance must be <= 5.0 Ohms.

### 2.4 Backhaul Transmission Path Survey
* Audited Converge Fiber Network Match (subject to verification on the ground): Distance to nearest confirmed node candidate (Class A <= 0.5 km, Class B <= 1.0 km) or line-tap closure (Class C <= 0.5 km).
* Cable Entry Facility: Manhole, handhole, or aerial pole lead-in routing into tower shelter/compound.
* For Remote Satellite Sited Candidates (Starlink Business): Satellite antenna mounting location (unobstructed sky view with 0° to 80° northern elevation arc for Starlink constellation tracking).

---

## 3. RF PROPAGATION & CELL DIMENSIONING GUIDELINES

### 3.1 Link Budget Parameters (Band n50, 1.5 GHz)

| Parameter | Unit | Value (Downlink) | Value (Uplink) | Technical Notes |
| :--- | :---: | :---: | :---: | :--- |
| **Operating Frequency** | MHz | 1487.0 (Center) | 1487.0 (Center) | Band n50 TDD (1457.0 – 1517.0 MHz Channel Range) |
| **Channel Bandwidth** | MHz | 60.0 | 60.0 | 162 Resource Blocks (SCS 30 kHz) |
| **BTS Maximum Conducted Power** | dBm / W | 55.0 dBm (320 W) | N/A | 8 x 40W RRU configuration |
| **BTS Power per Resource Block**| dBm | 32.9 dBm | N/A | Uniform power distribution |
| **BTS Antenna Gain** | dBi | 17.5 dBi | 17.5 dBi | 8-port cross-pol macro antenna |
| **BTS Cable / Jumper Loss** | dB | 1.0 dB | 1.0 dB | Short optical/RF jumper interface |
| **CPE Maximum Transmit Power** | dBm / W | N/A | 23.0 dBm (200 mW) | Power Class 3 UE (or Class 2 26 dBm) |
| **CPE Antenna Gain** | dBi | 9.0 dBi | 9.0 dBi | Baseline model (8 dBi indoor / 12 dBi outdoor) |
| **CPE Body / Indoor Penetration Loss** | dB | 8.0 dB | 8.0 dB | Concrete hollow block & glass attenuation |
| **Foliage / Clutter Margin** | dB | 6.0 dB | 6.0 dB | Typical rural tropical tree canopy |
| **Shadowing Margin (Log-Normal)**| dB | 7.0 dB | 7.0 dB | 90% edge cell coverage reliability |
| **Thermal Noise Density** | dBm/Hz | -174.0 | -174.0 | kT @ 290K |
| **Receiver Noise Figure** | dB | 6.0 dB (CPE) | 3.5 dB (gNodeB) | Active RF front-end |
| **Target SINR for Min Service** | dB | -1.0 dB | -2.0 dB | Minimum modulation threshold (QPSK 1/3 cell-edge; +10 dB target for residential 64QAM) |
| **Maximum Allowable Path Loss (MAPL)**| **dB** | **144.5 dB** | **139.8 dB** | **Uplink is coverage limiting** |
| **Calculated Reliable Cell Radius**| **km** | **3.5 km** | **3.2 km** | **Planning model assumption in suburban/rural clutter** |

### 3.2 Nominal Sector Azimuth & Tilt Strategy
* **Sector Count:** 3 sectors per macro site with 120° nominal separation (0°, 120°, 240°). Azimuths must be tailored during TSSR to track actual barangay population concentrations along transport corridors and coastal plains.
* **Electrical Remote Downtilt (eRET):** Antennas must feature AISG 2.0 remote tilt adjustable between 2° and 12° from the central OSS. Mechanical tilt shall only be applied when required to clear close-in obstructions (>15°).

---

## 4. CIVIL WORKS & STRUCTURAL ENGINEERING (CLASS T4 GREENFIELD & TOWERCO BTS SITES)

For sites requiring self-constructed greenfield towers or TowerCo Build-to-Suit (B2S) structures, the Contractor shall adhere to the following civil and structural standards conforming to the **National Structural Code of the Philippines (NSCP 2015 7th Edition, Section 207 Wind Loads)** and **TIA-222-G/H**:

### 4.1 Philippine Basic Wind Speed Regimes & Wind Zone Mapping
Structural design calculations and wind force determinations must strictly comply with NSCP 2015 basic wind speed maps:
* **Wind Zone 1 (Ultimate Wind Speed $V = 315\text{ km/h}$ / $87.5\text{ m/s}$):** Covers the high-typhoon corridor along the eastern seaboard (Batanes, Cagayan, Isabela, Aurora, Quezon/Polillo, Bicol Region, Samar, Leyte, Dinagat Islands, Surigao del Norte/Sur, Davao Oriental).
* **Wind Zone 2 (Ultimate Wind Speed $V = 270\text{ km/h}$ / $75.0\text{ m/s}$):** Covers Central and Western Luzon, National Capital Region (NCR), Central Luzon (Pampanga, Bulacan, Tarlac, Bataan, Zambales, Nueva Ecija), CALABARZON, MIMAROPA, and Western/Central Visayas (Iloilo, Cebu, Bohol, Negros).
* **Wind Zone 3 (Ultimate Wind Speed $V = 200\text{ km/h}$ / $55.6\text{ m/s}$):** Covers low-risk regions including Palawan, Zamboanga Peninsula, and southern inland Mindanao.

### 4.2 Structural Limit States & Deflection Criteria
* **Survivable Wind Speed ($V_{\text{survival}}$ — Ultimate Limit State / LRFD):**
  * Designed for **$270\text{ km/h}$ to $315\text{ km/h}$** 3-second gust wind speed under Ultimate Limit State with full equipment loading (3x n50 antennas, 3x RRUs, satellite dish, and mounting steelwork). Zero plastic collapse or structural overturning.
* **Operational Wind Speed ($V_{\text{operational}}$ — Serviceability Limit State / SLS):**
  * Designed for **$140\text{ km/h}$ to $160\text{ km/h}$ ($40.0\text{ m/s}$ to $44.4\text{ m/s}$)** continuous operational wind speed (1.0 load factor per TIA-222).
  * Structure maintains rigid RF alignment, ensuring uninterrupted 5G beamforming, MIMO rank-4 transmission, and backhaul link availability ($\ge 99.995\%$).
* **Allowable Twist ($\theta_{\text{twist}}$ / Torsional Rotation):**
  * $\le \pm 0.5^\circ$ ($30\text{ arcmin}$) at $30\text{m}$ AGL for narrow-beam / microwave dish antennas;
  * $\le \pm 1.0^\circ$ ($60\text{ arcmin}$) at $30\text{m}$ AGL for 5G Band n50 macro sectors.
* **Allowable Sway / Tilt ($\theta_{\text{sway}}$ / Angular Deflection):**
  * $\le \pm 1.0^\circ$ ($60\text{ arcmin}$) at top antenna mounting centerline ($30.0\text{m}$ AGL).
* **Allowable Verticality (Tower Plumbness / Alignment):**
  * $\le 1 : 500$ ($0.20\%$ of Tower Height $H$) throughout the full mast height under dead load and still air.
  * For a $30.0\text{m}$ monopole, maximum horizontal deviation $\Delta \le 60\text{ mm}$ (for $40.0\text{m}$ monopole, $\Delta \le 80\text{ mm}$).
  * Tolerance between consecutive slip-joints: $\le 1 : 1000$ ($0.10\%$).
* **Horizontal Service Deflection ($\Delta_{\text{top}}$):**
  * $\le H / 100$ ($300\text{ mm}$ maximum at $30.0\text{m}$ AGL).

### 4.3 Monopole Tower & Material Specification
* **Tower Structure:** 30-meter or 40-meter polygonal tubular steel monopole constructed in 3 to 4 slip-joint sections with minimum $1.5 \times$ inside diameter overlap.
* **Structural Steel:** ASTM A572 Grade 50 ($F_y = 345\text{ MPa} / 50\text{ ksi}$, $F_u = 450\text{ MPa}$).
* **Corrosion Protection:** Hot-dip galvanized per ASTM A123 / ISO 1461 with minimum zinc coating thickness $\ge 85\ \mu\text{m}$ ($610\text{ g/m}^2$).
* **Fasteners & Anchors:** Anchor bolts ASTM F1554 Grade 55/105 with double heavy-hex nuts; structural bolts ASTM A325 / ISO 898-1 Class 8.8 hot-dip galvanized.

### 4.4 Compound Civil Works & Foundation
* **Compound Footprint:** Standard $8.0\text{m} \times 8.0\text{m}$ ($64\text{ m}^2$) gravel-topped compound with geotextile weed barrier.
* **Perimeter Fencing:** 2.4-meter high cyclone wire mesh fence topped with 3 strands of galvanized concertina razor wire.
* **Equipment Pad:** Reinforced concrete equipment plinth (Class A concrete, 28-day compressive strength $f'_c \ge 28\text{ MPa} / 4,000\text{ psi}$, ASTM A615 Grade 60 rebar) for outdoor power/battery cabinets.
* **Foundation:** Reinforced concrete pad and chimney mat foundation or bored piles engineered with Safety Factor $\ge 2.0$ against soil bearing failure and $\ge 1.5$ against overturning/sliding.

### 4.5 Lightning Protection & Earthing Grid
* Top-mounted Franklin lightning air terminal extending $\ge 2.0\text{m}$ above uppermost antenna.
* Down-conductor: $70\text{ mm}^2$ bare stranded copper cable routed externally and clamped every $1.0\text{m}$ to tower shaft.
* Ground ring: Continuous buried bare copper loop around tower base and compound with copper-clad steel ground rods ($19\text{mm dia} \times 3.0\text{m}$ length) exothermically welded (Cadweld) at all junctions, achieving earth ground resistance $\le 5.0\ \Omega$.

---

## 5. SINGLE SITE VERIFICATION (SSV) & CLUSTER ACCEPTANCE CRITERIA

Before any site is granted Commercial On-Air Acceptance, the Contractor must complete and submit a signed SSV Report verifying:
1. **Stationary Functional Tests:**
   * Sector Verification: Physical azimuth and tilt match TSSR approval within +/- 2°.
   * RF Transmit Power: Conducted power on all 8 transmit paths within +/- 0.5 dB of nominal.
   * VSWR / Return Loss: Return loss >= 15 dB across all antenna feeder lines.
   * Max Throughput Test: Single CPE in line-of-sight achieving >= 300 Mbps DL and >= 50 Mbps UL (aggregate sector peak >= 450 Mbps DL / >= 60 Mbps UL verified under multi-CPE or loaded test).
2. **Short Drive Test & Static Multi-Point Test:**
   * 5 stationary measurement points per sector (Near: 500m, Mid: 1.5 km, Far/Edge: 3.0 km).
   * RSRP >= -95 dBm across >= 90% of surveyed barangay inhabited zone.
   * Ping RTT <= 18 ms target (<= 30 ms maximum contractual limit) to local UPF IP address over fiber backhaul; packet loss <= 0.10% over 1,000 continuous pings.
   * Inter-sector handover execution without drop during transition.

---
*(End of Appendix D — Site Survey, RF Planning & Civil Engineering Guidelines)*
