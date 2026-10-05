# POPCEN 5,000-site n50 predictive coverage

Generated: 2026-10-05T02:15:52.839Z

## Scenario

- Sites: 5,000; sectors: 15,000 (0°, 120°, 240°)
- Band: n50; center frequency: 1,474.5 MHz; bandwidth: 80 MHz
- Radio output: 40 W (46.02 dBm) per sector
- Antenna: 30 m, 17 dBi gain, 2 dB feeder loss, 65° beamwidth, 4° electrical tilt
- Receiver: 1.5 m, 7 dB noise figure
- Propagation: 3GPP TR 38.901 UMa NLOS + FWA Rooftop CPE (7m AGL, 12 dBi); 2 km grid; 12 km evaluation radius

## Results

- Predicted covered grid area (RSRP ≥ -120 dBm): **244,408 km²**
- Average predicted RSRP across retained cells: **-96.2 dBm**
- Average predicted co-channel SINR: **-11.1 dB**
- Grid cells below 0 dB SINR: **86.7%**
- Sites that never become best server at a grid center: **973**

| RSRP class | Range | Grid cells | Approx. area km² | Share |
|---|---:|---:|---:|---:|
| Excellent | ≥ -80 dBm | 7,813 | 31,252 | 12.8% |
| Good | -95 to -80 dBm | 15,041 | 60,164 | 24.6% |
| Fair | -105 to -95 dBm | 19,137 | 76,548 | 31.3% |
| Weak | -115 to -105 dBm | 17,706 | 70,824 | 29% |
| Marginal | -120 to -115 dBm | 1,405 | 5,620 | 2.3% |

## Engineering limitations

- Screening-level prediction; no terrain elevation, clutter raster, buildings, foliage, or field calibration was applied.
- Coverage area is estimated from 2 km grid-cell centers and is not a cadastral or population-coverage measurement.
- All 15,000 sectors are modeled as co-channel and continuously transmitting; actual scheduler load and PCI/SSB planning will change SINR.
- The POPCEN coordinates are planning candidates, not certified constructed BTS locations.
