# APPENDIX D: SITE SURVEY, RF PLANNING & CIVIL/POWER ENGINEERING GUIDELINES
## 5G FWA PROGRAM (5,000 SITES NATIONWIDE)

**Tender Reference:** RFP-TELTECH-FWA-2026-001  
**Project:** Nationwide 5G FWA Project (Band n50, 60 MHz TDD)  
**Operator:** Telecommunications Technology Solutions Incorporated (TelTech)  
**Author:** OLIVER TUNGOL

---

## 1. ENGINEERING PRINCIPLES & SITING ARCHITECTURE

### 1.1 Siting Philosophy
The primary engineering objective of the 5G FWA rollout is to maximize household population coverage within high-density suburban and rural barangay settlement clusters while minimizing civil capital expenditures and permitting lead times.
* **TowerCo Co-Location First (Option A — Baseline):** The Operator leverages an audited master database of **13,746 operational towers**. For every candidate barangay, field teams must prioritize existing towers within <= 2.0 km (Classes T1, T2, and T3).
* **Greenfield Monopole (Class T4):** Restricted strictly to candidate barangays located > 2.0 km from any verified operational tower structure (~9.3% of sites nationwide; 103 sites in Phase 1).

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
* For Remote Class E/F Sites: Satellite antenna mounting location (unobstructed sky view with 0° to 80° northern elevation arc for Starlink constellation tracking).

---

## 3. RF PROPAGATION & CELL DIMENSIONING GUIDELINES

### 3.1 Link Budget Parameters (Band n50, 1.5 GHz)

| Parameter | Unit | Value (Downlink) | Value (Uplink) | Technical Notes |
| :--- | :---: | :---: | :---: | :--- |
| **Operating Frequency** | MHz | 1475.0 (Center) | 1475.0 (Center) | Band n50 TDD |
| **Channel Bandwidth** | MHz | 60.0 | 60.0 | 162 Resource Blocks (SCS 30 kHz) |
| **BTS Maximum Conducted Power** | dBm / W | 55.0 dBm (320 W) | N/A | 8 x 40W RRU configuration |
| **BTS Power per Resource Block**| dBm | 32.9 dBm | N/A | Uniform power distribution |
| **BTS Antenna Gain** | dBi | 17.5 dBi | 17.5 dBi | 8-port cross-pol macro antenna |
| **BTS Cable / Jumper Loss** | dB | 1.0 dB | 1.0 dB | Short optical/RF jumper interface |
| **CPE Maximum Transmit Power** | dBm / W | N/A | 23.0 dBm (200 mW) | Power Class 3 UE (or Class 2 26 dBm) |
| **CPE Antenna Gain** | dBi | 9.0 dBi | 9.0 dBi | High-gain directional indoor/outdoor |
| **CPE Body / Indoor Penetration Loss** | dB | 8.0 dB | 8.0 dB | Concrete hollow block & glass attenuation |
| **Foliage / Clutter Margin** | dB | 6.0 dB | 6.0 dB | Typical rural tropical tree canopy |
| **Shadowing Margin (Log-Normal)**| dB | 7.0 dB | 7.0 dB | 90% edge cell coverage reliability |
| **Thermal Noise Density** | dBm/Hz | -174.0 | -174.0 | kT @ 290K |
| **Receiver Noise Figure** | dB | 6.0 dB (CPE) | 3.5 dB (gNodeB) | Active RF front-end |
| **Target SINR for Min Service** | dB | -1.0 dB | -2.0 dB | QPSK rate 1/3 (Cell Edge 25 Mbps DL) |
| **Maximum Allowable Path Loss (MAPL)**| **dB** | **144.5 dB** | **139.8 dB** | **Uplink is coverage limiting** |
| **Calculated Reliable Cell Radius**| **km** | **{3.5 km}** | **{3.2 km}** | **Standard suburban/rural clutter** |

### 3.2 Nominal Sector Azimuth & Tilt Strategy
* **Sector Count:** 3 sectors per macro site with 120° nominal separation (0°, 120°, 240°). Azimuths must be tailored during TSSR to track actual barangay population concentrations along transport corridors and coastal plains.
* **Electrical Remote Downtilt (eRET):** Antennas must feature AISG 2.0 remote tilt adjustable between 2° and 10° from the central OSS. Mechanical tilt shall only be applied when required to clear close-in obstructions (>15°).

---

## 4. CIVIL WORKS & STRUCTURAL ENGINEERING (CLASS T4 GREENFIELD SITES)

For the ~10% of sites requiring self-constructed greenfield towers, the Contractor shall adhere to the following civil standards:
1. **Monopole Tower Specification:**
   * 30-meter or 40-meter polygonal tubular steel monopole constructed in 3 to 4 slip-joint sections.
   * Structural steel: ASTM A572 Grade 50 (or equivalent high-strength structural grade) hot-dip galvanized per ASTM A123 (>= 85microns zinc coating).
   * Design Wind Speed: Minimum **250 km/h 3-second gust** in accordance with the National Structural Code of the Philippines (NSCP 2015 / TIA-222-G/H).
   * Top antenna mounting platform capable of supporting 6x antennas/RRUs and microwave dish mountings.
2. **Compound Civil Works:**
   * Compound Footprint: Standard 8.0m x 8.0m (64 m²) gravel-topped compound.
   * Perimeter Fencing: 2.4-meter high cyclone wire mesh fence topped with 3 strands of galvanized concertina razor wire.
   * Equipment Pad: Reinforced concrete equipment plinth (Class A concrete, 28-day compressive strength >= 21MPa / 3,000psi) for outdoor cabinets and generator set.
3. **Lightning Protection & Grounding Grid:**
   * Air terminal (lightning rod) installed at monopole top extending >= 2.0m above uppermost antenna.
   * Down-conductor: 70mm² bare stranded copper cable routed externally and clamped every 1.0m to tower shaft.
   * Earth ground ring: Continuous buried bare copper loop around tower base and compound with copper-clad steel ground rods (19mm dia x 3.0m length) exothermically welded (Cadweld) at all junctions, achieving <= 5.0 Ohms.

---

## 5. SINGLE SITE VERIFICATION (SSV) & CLUSTER ACCEPTANCE CRITERIA

Before any site is granted Commercial On-Air Acceptance, the Contractor must complete and submit a signed SSV Report verifying:
1. **Stationary Functional Tests:**
   * Sector Verification: Physical azimuth and tilt match TSSR approval within +/- 2°.
   * RF Transmit Power: Conducted power on all 8 transmit paths within +/- 0.5 dB of nominal.
   * VSWR / Return Loss: Return loss >= 15 dB across all antenna feeder lines.
   * Max Throughput Test: Single CPE situated in line-of-sight achieving >= 450 Mbps DL and >= 60 Mbps UL.
2. **Short Drive Test & Static Multi-Point Test:**
   * 5 stationary measurement points per sector (Near: 500m, Mid: 1.5 km, Far/Edge: 3.0 km).
   * RSRP >= -95 dBm across >= 90% of surveyed barangay inhabited zone.
   * Ping RTT <= 20 ms to local UPF IP address; zero packet loss over 1,000 continuous pings.
   * Inter-sector handover execution without drop during transition.

---
*(End of Appendix D — Site Survey, RF Planning & Civil Engineering Guidelines)*
