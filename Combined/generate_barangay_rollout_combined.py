#!/usr/bin/env python3
"""
================================================================================
  PHILIPPINE 5G FWA BARANGAY ROLLOUT MASTER GENERATION ENGINE (BAND n50)
  MODEL 3: HYBRID COMBINED MODEL (COMMERCIAL VIABILITY + GIDA SOCIAL IMPACT)
================================================================================

Integrated Datasets:
  1. Commercial Viability Model (POPCEN 2024, Converge Optical Anchor, FIES Poverty).
     - 35% Ease of Deployment (Fiber proximity, node/line decay)
     - 35% Commercial Viability (Sweet-spot subscriber density, poverty discount)
     - 30% Broadband Necessity (Rural classification, LGU class 4-6, off-net distance, poverty deficit)
  2. DICT / UNDP FPIAP GIDA Prioritization Decision Support Tool (Looker Studio Dataset).
     - 42,001 Evaluated Barangays with official Looker Studio multi-criteria scores (11 criteria).
  3. Combined Multi-Objective Optimization:
     - Combined Score = (w_comm * Commercial_Composite) + (w_gida * Normalized_GIDA_Score)
     - Baseline: 50% Commercial / 50% GIDA Social Impact (Dynamically tunable in Excel).
"""

import os
import sys
import re
import csv
import json
import math
import zipfile
import time
from collections import defaultdict
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUT_DIR = "Combined"
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(os.path.join(OUT_DIR, "data"), exist_ok=True)

# ----------------------------------------------------------------------------
# 1. MODEL ASSUMPTIONS & PARAMETERS (COMBINED HYBRID EDITION)
# ----------------------------------------------------------------------------
ASSUMPTIONS = {
    # Commercial Weights
    "weight_deploy": 0.35,
    "weight_viability": 0.35,
    "weight_necessity": 0.30,
    # Combined Blend Weights (50/50 Baseline)
    "weight_commercial_blend": 0.50,
    "weight_gida_blend": 0.50,
    # Siting & Capacity
    "penetration_rate": 0.30,
    "subs_per_bts": 1000,
    "default_hh_size_2024": 3.80,
    "batch_size": 1000,
    "total_batches": 5,
    "carrier_name": "Single Carrier (Band n50, 100MHz TDD)",
    # Transmission Distance Thresholds
    "optical_dist_threshold": 3.0,
    "starlink_dist_threshold": 5.0,
    # Viability sweet spots
    "sweet_spot_low": 250,
    "sweet_spot_high": 1200,
    "deploy_decay_km": 8.0,
    "fiber_corridor_km": 2.0,
    "fiber_corridor_bonus": 10.0,
    "ncr_penalty": 15.0,
    "barmm_penalty": 5.0
}

REGIONAL_POVERTY_FIES = {
    'NCR': 1.1, 'Region III': 8.3, 'Region IV-A': 7.2, 'Region I': 11.0,
    'Region II': 11.7, 'Region V': 23.7, 'Region VI': 15.6, 'Region VII': 21.0,
    'Region VIII': 22.2, 'Region IX': 23.4, 'Region X': 17.4, 'Region XI': 11.9,
    'Region XII': 19.7, 'Caraga': 22.1, 'BARMM': 23.5, 'CAR': 8.9,
    'MIMAROPA': 15.0, 'NATIONAL_AVG': 10.9
}

def clean_str(s):
    if not s: return ''
    s = str(s).upper().strip()
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'[^A-Z0-9]', '', s)
    return s

def norm_name(s):
    if not s: return ''
    s = str(s).upper().strip()
    s = re.sub(r'\(.*?\)', '', s)
    s = re.sub(r'\bPOBLACION\b', 'POB', s)
    s = re.sub(r'\bBARANGAY\b', '', s)
    s = re.sub(r'\bBGY\b', '', s)
    s = re.sub(r'[^A-Z0-9]', '', s)
    return s

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2.0) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2.0) ** 2)
    return R * 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))

def get_region_poverty(reg_name):
    if not reg_name: return REGIONAL_POVERTY_FIES['NATIONAL_AVG']
    reg_clean = clean_str(reg_name)
    for k, v in REGIONAL_POVERTY_FIES.items():
        if clean_str(k) in reg_clean or reg_clean in clean_str(k):
            return v
    return REGIONAL_POVERTY_FIES['NATIONAL_AVG']

def generate_dynamic_version(src_xlsx_path, dest_xlsx_path):
    print("  -> Creating live formula dynamic model from Combined standard model...")
    wb_dyn = openpyxl.load_workbook(src_xlsx_path, data_only=False)

    font_title = Font(name='Calibri', size=16, bold=True, color='1B365D')
    font_header = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
    font_data = Font(name='Calibri', size=9.5)
    font_bold = Font(name='Calibri', size=9.5, bold=True)
    fill_navy = PatternFill(start_color='1B365D', end_color='1B365D', fill_type='solid')
    fill_param_edit = PatternFill(start_color='FEF3C7', end_color='FEF3C7', fill_type='solid')
    border_thin = Border(left=Side(style='thin', color='CBD5E1'), right=Side(style='thin', color='CBD5E1'),
                         top=Side(style='thin', color='CBD5E1'), bottom=Side(style='thin', color='CBD5E1'))
    border_header = Border(left=Side(style='thin', color='FFFFFF'), right=Side(style='thin', color='FFFFFF'),
                           top=Side(style='medium', color='1B365D'), bottom=Side(style='medium', color='1B365D'))

    # 1. Update Methodology & Assumptions tab
    ws_m = wb_dyn['Methodology & Assumptions']
    ws_m['A1'] = "Dynamic FWA Combined Siting Parameters & Sensitivity Inputs (Editable)"
    ws_m['A2'] = "Changes to yellow-highlighted parameters below immediately and dynamically recalculate all batch sheets and executive summary tables."

    # Highlight dynamic numeric inputs in B5:B12
    dynamic_param_values = [
        (5, 0.50, "0.0%"),    # Commercial Weight (w_comm)
        (6, 0.50, "0.0%"),    # GIDA Weight (w_gida)
        (7, 0.30, "0.0%"),    # Penetration Rate
        (8, 1000, "#,##0"),   # n50 BTS Capacity
        (9, 5.0, "0.0"),      # Starlink Distance Threshold (km)
        (10, 3.0, "0.0"),     # Direct Optical Threshold (km)
        (11, 3.80, "0.00")    # Default 2024 HH Size
    ]
    for row_idx, val, fmt in dynamic_param_values:
        cell = ws_m.cell(row_idx, 2)
        cell.value = val
        cell.number_format = fmt
        cell.fill = fill_param_edit
        cell.font = font_bold
        cell.alignment = Alignment(horizontal='right', vertical='center')

    # 2. Update Batch Sheets with dynamic Excel formulas
    batch_sheets = [
        ('Batch 1 (First 1,000)', 5, 1004),
        ('Batch 2 (1,001 - 2,000)', 5, 1004),
        ('Batch 3 (2,001 - 3,000)', 5, 1004),
        ('Batch 4 & 5 (3,001 - 5,000)', 5, 2004)
    ]

    for sheet_name, start_r, end_r in batch_sheets:
        ws_b = wb_dyn[sheet_name]
        ws_b['A2'] = f"Dynamic Hybrid deployment rollout schedule ({end_r - start_r + 1:,} sites), linked to live parameters in 'Methodology & Assumptions'."
        
        for r in range(start_r, end_r + 1):
            ws_b.cell(r, 14).value = f"=ROUND(L{r}/M{r}, 0)"
            ws_b.cell(r, 15).value = f"=ROUND(N{r}*'Methodology & Assumptions'!$B$7, 0)"
            ws_b.cell(r, 17).value = f"=ROUNDUP(O{r}/'Methodology & Assumptions'!$B$8, 0)"
            ws_b.cell(r, 18).value = 1
            ws_b.cell(r, 21).value = f'=IF(S{r}<=\'Methodology & Assumptions\'!$B$10, "Direct Optical Drop (<3km)", IF(S{r}<=\'Methodology & Assumptions\'!$B$9, "Near Optical / Microwave (<5km)", "Starlink Business LEO Satellite Backhaul (>5km)"))'
            ws_b.cell(r, 24).value = f"=ROUND(('Methodology & Assumptions'!$B$5*V{r}) + ('Methodology & Assumptions'!$B$6*W{r}), 2)"

    # 3. Update Executive Summary with dynamic cross-sheet references
    ws_e = wb_dyn['Executive Summary']
    ws_e['A1'] = "Dynamic 5G FWA Barangay Siting & Rollout Schedule (Combined Model - Live Formulas)"
    ws_e['A2'] = "Automated sensitivity summary linked dynamically to 'Methodology & Assumptions' and Batch sheets."

    # Batch Comparison Table dynamic formulas
    # Row 16: Batch 1
    ws_e['C16'].value = "='Batch 1 (First 1,000)'!L1005"
    ws_e['D16'].value = "='Batch 1 (First 1,000)'!N1005"
    ws_e['E16'].value = "='Batch 1 (First 1,000)'!O1005"
    ws_e['F16'].value = "='Batch 1 (First 1,000)'!R1005"
    ws_e['G16'].value = "='Batch 1 (First 1,000)'!Q1005"
    ws_e['H16'].value = "='Batch 1 (First 1,000)'!X1005"
    ws_e['I16'].value = "='Batch 1 (First 1,000)'!V1005"
    ws_e['J16'].value = "='Batch 1 (First 1,000)'!W1005"
    ws_e['K16'].value = '=COUNTIF(\'Batch 1 (First 1,000)\'!$U$5:$U$1004, "Direct Optical*")'
    ws_e['L16'].value = '=COUNTIF(\'Batch 1 (First 1,000)\'!$U$5:$U$1004, "Near Optical*")'
    ws_e['M16'].value = '=COUNTIF(\'Batch 1 (First 1,000)\'!$U$5:$U$1004, "Starlink*")'

    # Row 17: Batch 2
    ws_e['C17'].value = "='Batch 2 (1,001 - 2,000)'!L1005"
    ws_e['D17'].value = "='Batch 2 (1,001 - 2,000)'!N1005"
    ws_e['E17'].value = "='Batch 2 (1,001 - 2,000)'!O1005"
    ws_e['F17'].value = "='Batch 2 (1,001 - 2,000)'!R1005"
    ws_e['G17'].value = "='Batch 2 (1,001 - 2,000)'!Q1005"
    ws_e['H17'].value = "='Batch 2 (1,001 - 2,000)'!X1005"
    ws_e['I17'].value = "='Batch 2 (1,001 - 2,000)'!V1005"
    ws_e['J17'].value = "='Batch 2 (1,001 - 2,000)'!W1005"
    ws_e['K17'].value = '=COUNTIF(\'Batch 2 (1,001 - 2,000)\'!$U$5:$U$1004, "Direct Optical*")'
    ws_e['L17'].value = '=COUNTIF(\'Batch 2 (1,001 - 2,000)\'!$U$5:$U$1004, "Near Optical*")'
    ws_e['M17'].value = '=COUNTIF(\'Batch 2 (1,001 - 2,000)\'!$U$5:$U$1004, "Starlink*")'

    # Row 18: Batch 3
    ws_e['C18'].value = "='Batch 3 (2,001 - 3,000)'!L1005"
    ws_e['D18'].value = "='Batch 3 (2,001 - 3,000)'!N1005"
    ws_e['E18'].value = "='Batch 3 (2,001 - 3,000)'!O1005"
    ws_e['F18'].value = "='Batch 3 (2,001 - 3,000)'!R1005"
    ws_e['G18'].value = "='Batch 3 (2,001 - 3,000)'!Q1005"
    ws_e['H18'].value = "='Batch 3 (2,001 - 3,000)'!X1005"
    ws_e['I18'].value = "='Batch 3 (2,001 - 3,000)'!V1005"
    ws_e['J18'].value = "='Batch 3 (2,001 - 3,000)'!W1005"
    ws_e['K18'].value = '=COUNTIF(\'Batch 3 (2,001 - 3,000)\'!$U$5:$U$1004, "Direct Optical*")'
    ws_e['L18'].value = '=COUNTIF(\'Batch 3 (2,001 - 3,000)\'!$U$5:$U$1004, "Near Optical*")'
    ws_e['M18'].value = '=COUNTIF(\'Batch 3 (2,001 - 3,000)\'!$U$5:$U$1004, "Starlink*")'

    # Row 19: Batch 4
    ws_e['C19'].value = "=SUM('Batch 4 & 5 (3,001 - 5,000)'!L5:L1004)"
    ws_e['D19'].value = "=SUM('Batch 4 & 5 (3,001 - 5,000)'!N5:N1004)"
    ws_e['E19'].value = "=SUM('Batch 4 & 5 (3,001 - 5,000)'!O5:O1004)"
    ws_e['F19'].value = "=COUNT('Batch 4 & 5 (3,001 - 5,000)'!R5:R1004)"
    ws_e['G19'].value = "=SUM('Batch 4 & 5 (3,001 - 5,000)'!Q5:Q1004)"
    ws_e['H19'].value = "=AVERAGE('Batch 4 & 5 (3,001 - 5,000)'!X5:X1004)"
    ws_e['I19'].value = "=AVERAGE('Batch 4 & 5 (3,001 - 5,000)'!V5:V1004)"
    ws_e['J19'].value = "=AVERAGE('Batch 4 & 5 (3,001 - 5,000)'!W5:W1004)"
    ws_e['K19'].value = '=COUNTIF(\'Batch 4 & 5 (3,001 - 5,000)\'!$U$5:$U$1004, "Direct Optical*")'
    ws_e['L19'].value = '=COUNTIF(\'Batch 4 & 5 (3,001 - 5,000)\'!$U$5:$U$1004, "Near Optical*")'
    ws_e['M19'].value = '=COUNTIF(\'Batch 4 & 5 (3,001 - 5,000)\'!$U$5:$U$1004, "Starlink*")'

    # Row 20: Batch 5
    ws_e['C20'].value = "=SUM('Batch 4 & 5 (3,001 - 5,000)'!L1005:L2004)"
    ws_e['D20'].value = "=SUM('Batch 4 & 5 (3,001 - 5,000)'!N1005:N2004)"
    ws_e['E20'].value = "=SUM('Batch 4 & 5 (3,001 - 5,000)'!O1005:O2004)"
    ws_e['F20'].value = "=COUNT('Batch 4 & 5 (3,001 - 5,000)'!R1005:R2004)"
    ws_e['G20'].value = "=SUM('Batch 4 & 5 (3,001 - 5,000)'!Q1005:Q2004)"
    ws_e['H20'].value = "=AVERAGE('Batch 4 & 5 (3,001 - 5,000)'!X1005:X2004)"
    ws_e['I20'].value = "=AVERAGE('Batch 4 & 5 (3,001 - 5,000)'!V1005:V2004)"
    ws_e['J20'].value = "=AVERAGE('Batch 4 & 5 (3,001 - 5,000)'!W1005:W2004)"
    ws_e['K20'].value = '=COUNTIF(\'Batch 4 & 5 (3,001 - 5,000)\'!$U$1005:$U$2004, "Direct Optical*")'
    ws_e['L20'].value = '=COUNTIF(\'Batch 4 & 5 (3,001 - 5,000)\'!$U$1005:$U$2004, "Near Optical*")'
    ws_e['M20'].value = '=COUNTIF(\'Batch 4 & 5 (3,001 - 5,000)\'!$U$1005:$U$2004, "Starlink*")'

    # Row 21: Total 5,000
    ws_e['C21'].value = "=SUM(C16:C20)"
    ws_e['D21'].value = "=SUM(D16:D20)"
    ws_e['E21'].value = "=SUM(E16:E20)"
    ws_e['F21'].value = "=SUM(F16:F20)"
    ws_e['G21'].value = "=SUM(G16:G20)"
    ws_e['H21'].value = "=AVERAGE(H16:H20)"
    ws_e['I21'].value = "=AVERAGE(I16:I20)"
    ws_e['J21'].value = "=AVERAGE(J16:J20)"
    ws_e['K21'].value = "=SUM(K16:K20)"
    ws_e['L21'].value = "=SUM(L16:L20)"
    ws_e['M21'].value = "=SUM(M16:M20)"

    # Dynamic KPI Cards (Row 6)
    ws_e['A6'].value = "=F21"
    ws_e['C6'].value = "=E16"
    ws_e['E6'].value = "=E21"
    ws_e['G6'].value = "=G21"
    ws_e['I6'].value = "=K21+L21"
    ws_e['K6'].value = "=M21"

    wb_dyn.save(dest_xlsx_path)
    wb_dyn.close()
    print(f"  -> Successfully generated dynamic workbook: {dest_xlsx_path}")

def run():
    print("=" * 80)
    print("  STARTING FWA COMBINED ROLLOUT GENERATOR (COMMERCIAL + GIDA HYBRID)")
    print("=" * 80)
    t_start = time.time()

    # ------------------------------------------------------------------------
    # STEP 1: Ingest Converge KMZ Backbone Infrastructure
    # ------------------------------------------------------------------------
    print("\n[Step 1/7] Ingesting Converge KMZ Backbone Infrastructure...")
    kmz_path = 'NATIONAL & REGIONAL BACKBONE_NOV 2024_REPORT.kmz'
    with zipfile.ZipFile(kmz_path, 'r') as z:
        for name in z.namelist():
            if name.endswith('.kml'):
                kml_text = z.read(name).decode('utf-8', errors='ignore')
                break

    node_pts = []
    node_blocks = re.findall(r'<Placemark>.*?</Placemark>', kml_text, re.DOTALL)
    for nb in node_blocks:
        if '<Point>' in nb:
            coord_m = re.search(r'<Point>.*?<coordinates>([^<]+)</coordinates>.*?</Point>', nb, re.DOTALL)
            if coord_m:
                parts = coord_m.group(1).strip().split(',')
                if len(parts) >= 2:
                    try:
                        lon = float(parts[0])
                        lat = float(parts[1])
                        if 4.0 <= lat <= 22.0 and 115.0 <= lon <= 130.0:
                            node_pts.append((lat, lon))
                    except ValueError:
                        pass

    line_pts = []
    line_blocks = re.findall(r'<LineString>.*?<coordinates>([^<]+)</coordinates>.*?</LineString>', kml_text, re.DOTALL)
    for lb in line_blocks:
        tokens = lb.strip().split()
        last_pt = None
        for tok in tokens:
            parts = tok.split(',')
            if len(parts) >= 2:
                try:
                    lon = float(parts[0])
                    lat = float(parts[1])
                    if 4.0 <= lat <= 22.0 and 115.0 <= lon <= 130.0:
                        if last_pt is None or abs(lat - last_pt[0]) > 0.0045 or abs(lon - last_pt[1]) > 0.0045:
                            line_pts.append((lat, lon))
                            last_pt = (lat, lon)
                except ValueError:
                    pass

    print(f"  -> Extracted {len(node_pts):,} backbone nodes and {len(line_pts):,} downsampled line vertices.")

    # Spatial Grid Index
    grid_size = 0.25
    node_grid = {}
    for lat, lon in node_pts:
        gx, gy = int(lat / grid_size), int(lon / grid_size)
        node_grid.setdefault((gx, gy), []).append((lat, lon))

    line_grid = {}
    for lat, lon in line_pts:
        gx, gy = int(lat / grid_size), int(lon / grid_size)
        line_grid.setdefault((gx, gy), []).append((lat, lon))

    def fast_nearest_distance(lat, lon, grid):
        gx, gy = int(lat / grid_size), int(lon / grid_size)
        cos_lat = math.cos(math.radians(lat))
        best_dist_sq = 999999.0
        best_pt = None

        for radius in range(0, 8):
            for dx in range(-radius, radius + 1):
                for dy in range(-radius, radius + 1):
                    if max(abs(dx), abs(dy)) != radius: continue
                    cands = grid.get((gx + dx, gy + dy))
                    if cands:
                        for clat, clon in cands:
                            d_lat_km = (clat - lat) * 111.139
                            d_lon_km = (clon - lon) * 111.139 * cos_lat
                            d_sq = d_lat_km * d_lat_km + d_lon_km * d_lon_km
                            if d_sq < best_dist_sq:
                                best_dist_sq = d_sq
                                best_pt = (clat, clon)
            if best_pt is not None and best_dist_sq < (radius * grid_size * 111.139)**2:
                break

        if best_pt:
            return haversine(lat, lon, best_pt[0], best_pt[1])
        return 999.0

    # ------------------------------------------------------------------------
    # STEP 2: Ingest 2024 POPCEN Provincial Data & NCR Barangay Census
    # ------------------------------------------------------------------------
    print("\n[Step 2/7] Ingesting 2024 POPCEN Provincial Data & NCR Barangay Census...")
    wb_2024 = openpyxl.load_workbook('Combined/data/Statistical Table.xlsx', data_only=True)
    ws_2024 = wb_2024['Table 1']

    def clean_unit(s):
        if not s: return ''
        s = str(s).upper().strip()
        s = re.sub(r'\(.*?\)', '', s)
        s = re.sub(r'\*', '', s)
        s = re.sub(r'[^A-Z0-9]', '', s)
        return s.strip()

    units_2024 = {}
    for r in range(7, ws_2024.max_row + 1):
        name = ws_2024.cell(r, 1).value
        pop = ws_2024.cell(r, 3).value
        avg_hh = ws_2024.cell(r, 7).value
        if name and pop:
            try:
                s_raw = str(name).strip()
                if any(x in s_raw for x in ['Region', 'NCR', 'CAR', 'BARMM', 'MIMAROPA']):
                    continue
                p_val = int(pop)
                a_val = float(avg_hh) if avg_hh else 3.8
                units_2024[clean_unit(s_raw)] = (p_val, a_val, s_raw)
            except (ValueError, TypeError):
                pass
    wb_2024.close()
    print(f"  -> Loaded 2024 POPCEN data for {len(units_2024):,} administrative units.")

    # NCR Direct Data
    ncr_2024_bgys = {}
    if os.path.exists('Combined/data/NCR_Statistical Table_R13.xlsx'):
        wb_ncr = openpyxl.load_workbook('Combined/data/NCR_Statistical Table_R13.xlsx', data_only=True)
        for sname in wb_ncr.sheetnames:
            if sname.startswith('Table 2'):
                ws = wb_ncr[sname]
                city = clean_unit(sname.replace('Table 2-', ''))
                for r in range(8, ws.max_row + 1):
                    b_name = ws.cell(r, 1).value
                    pop = ws.cell(r, 3).value
                    n_hh = ws.cell(r, 5).value
                    if b_name and pop:
                        try:
                            p_val = int(pop)
                            h_val = int(n_hh) if n_hh else int(round(p_val / 3.7))
                            ncr_2024_bgys[(city, clean_unit(b_name))] = (p_val, h_val)
                        except (ValueError, TypeError):
                            pass
        wb_ncr.close()

    # Income Class metadata
    muni_meta = {}
    if os.path.exists('FWA_Target_Municipalities.xlsx'):
        wb_tm = openpyxl.load_workbook('FWA_Target_Municipalities.xlsx', data_only=True)
        s_class = wb_tm['All Class 4-6 (668)']
        for r in range(5, s_class.max_row + 1):
            m_name = str(s_class.cell(r, 2).value).strip() if s_class.cell(r, 2).value else ''
            p_name = str(s_class.cell(r, 3).value).strip() if s_class.cell(r, 3).value else ''
            c_new = str(s_class.cell(r, 14).value).strip() if s_class.cell(r, 14).value else '4th'
            if m_name and p_name:
                muni_meta[(clean_str(p_name), clean_str(m_name))] = c_new
        wb_tm.close()

    # ------------------------------------------------------------------------
    # STEP 3: Ingest Official UNDP GIDA Scores & Coordinates
    # ------------------------------------------------------------------------
    print("\n[Step 3/7] Ingesting Official UNDP Looker Studio GIDA Scores...")
    undp_csv_path = 'UNDP/2026 DICT FPIAP GIDA Barangay Prioritization Tool_Untitled Page_Table_1.csv'
    undp_data = {}
    undp_coords = {}
    muni_coords = defaultdict(list)
    prov_coords = defaultdict(list)

    with open(undp_csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            cp = clean_unit(r['Province'])
            cm = clean_unit(r['Locality'])
            cb = clean_unit(r['Barangay'])
            np_ = norm_name(r['Province'])
            nm_ = norm_name(r['Locality'])
            nb_ = norm_name(r['Barangay'])
            try:
                score = float(r['GIDA Score']) if r.get('GIDA Score') else 0.0
                lat = float(r['Latitude']) if r.get('Latitude') and r.get('Latitude') != 'null' else 12.8797
                lon = float(r['Longitude']) if r.get('Longitude') and r.get('Longitude') != 'null' else 121.7740

                undp_data[(cp, cm, cb)] = score
                undp_data[(cm, cb)] = score
                undp_data[(np_, nm_, nb_)] = score
                undp_data[(nm_, nb_)] = score

                if 4.0 <= lat <= 22.0 and 115.0 <= lon <= 130.0:
                    undp_coords[(cp, cm, cb)] = (lat, lon)
                    undp_coords[(cm, cb)] = (lat, lon)
                    undp_coords[(np_, nm_, nb_)] = (lat, lon)
                    undp_coords[(nm_, nb_)] = (lat, lon)
                    muni_coords[cm].append((lat, lon))
                    prov_coords[cp].append((lat, lon))
            except (ValueError, KeyError):
                pass

    print(f"  -> Extracted GIDA scores and coordinates for {len(undp_data):,} entries.")

    # ------------------------------------------------------------------------
    # STEP 4: Scale Baseline Barangays to 2024 POPCEN
    # ------------------------------------------------------------------------
    print("\n[Step 4/7] Scaling Baseline Barangays to 2024 POPCEN Demographics...")
    wb_psa = openpyxl.load_workbook('PSA List of Barangays.xlsx', read_only=True)
    ws_psa = wb_psa.active
    raw_bgys = []
    unit_2020_pop = defaultdict(int)

    for row in ws_psa.iter_rows(values_only=True):
        if not row[8]: continue
        psgc = str(row[0]).strip() if row[0] else ''
        reg = str(row[2]).strip() if row[2] else ''
        prov = str(row[4]).strip() if row[4] else ''
        mun = str(row[6]).strip() if row[6] else ''
        bgy = str(row[8]).strip() if row[8] else ''
        ur = str(row[11]).strip().upper() if row[11] else 'R'
        pop2020 = int(row[12]) if isinstance(row[12], (int, float)) and row[12] > 0 else 0

        if not bgy or pop2020 <= 0: continue

        cp = clean_unit(prov)
        cm = clean_unit(mun)
        cb = clean_unit(bgy)

        target_unit = None
        if cm in units_2024: target_unit = cm
        elif cp in units_2024: target_unit = cp
        else:
            for u in units_2024:
                if u in cm or cm in u:
                    target_unit = u
                    break
            if not target_unit:
                for u in units_2024:
                    if u in cp or cp in u:
                        target_unit = u
                        break

        if target_unit: unit_2020_pop[target_unit] += pop2020

        raw_bgys.append({
            'psgc': psgc, 'region': reg, 'province': prov, 'municipality': mun, 'barangay': bgy,
            'ur': ur, 'pop_2020': pop2020, 'target_unit': target_unit,
            'cp': cp, 'cm': cm, 'cb': cb,
            'np': norm_name(prov), 'nm': norm_name(mun), 'nb': norm_name(bgy)
        })

    wb_psa.close()

    all_bgys = []
    for b in raw_bgys:
        cp = b['cp']
        cm = b['cm']
        cb = b['cb']
        t_unit = b['target_unit']

        p_2024 = 0
        h_2024 = 0
        avg_hh = ASSUMPTIONS['default_hh_size_2024']

        if (cm, cb) in ncr_2024_bgys:
            p_2024, h_2024 = ncr_2024_bgys[(cm, cb)]
            avg_hh = round(p_2024 / max(1, h_2024), 2)
        elif t_unit and t_unit in units_2024 and unit_2020_pop[t_unit] > 0:
            p24_tot, ahh, _ = units_2024[t_unit]
            p20_tot = unit_2020_pop[t_unit]
            growth_ratio = p24_tot / p20_tot
            p_2024 = int(round(b['pop_2020'] * growth_ratio))
            avg_hh = ahh
            h_2024 = int(round(p_2024 / avg_hh))
        else:
            p_2024 = int(round(b['pop_2020'] * 1.0359))
            avg_hh = ASSUMPTIONS['default_hh_size_2024']
            h_2024 = int(round(p_2024 / avg_hh))

        poverty_rate = get_region_poverty(b['region'])
        income_class = muni_meta.get((clean_str(b['province']), clean_str(b['municipality'])), '1st-3rd')
        is_class_4_6 = (clean_str(b['province']), clean_str(b['municipality'])) in muni_meta

        all_bgys.append({
            'psgc': b['psgc'], 'region': b['region'], 'province': b['province'],
            'municipality': b['municipality'], 'barangay': b['barangay'],
            'ur': b['ur'], 'pop': p_2024, 'avg_hh': avg_hh, 'households': h_2024,
            'income_class': income_class, 'is_class_4_6': is_class_4_6,
            'poverty_rate': poverty_rate,
            'cp': cp, 'cm': cm, 'cb': cb, 'np': b['np'], 'nm': b['nm'], 'nb': b['nb']
        })

    # ------------------------------------------------------------------------
    # STEP 5: Execute Hybrid Multi-Objective Scoring Engine
    # ------------------------------------------------------------------------
    print("\n[Step 5/7] Executing Hybrid Multi-Objective Scoring Engine Across 41,976 Barangays...")
    scored = []
    A = ASSUMPTIONS

    for b in all_bgys:
        cp, cm, cb = b['cp'], b['cm'], b['cb']
        np_, nm_, nb_ = b['np'], b['nm'], b['nb']

        coords = (undp_coords.get((cp, cm, cb)) or
                  undp_coords.get((cm, cb)) or
                  undp_coords.get((np_, nm_, nb_)) or
                  undp_coords.get((nm_, nb_)))

        if coords:
            lat, lon = coords
        elif cm in muni_coords:
            pts = muni_coords[cm]
            lat = sum(p[0] for p in pts) / len(pts)
            lon = sum(p[1] for p in pts) / len(pts)
        elif cp in prov_coords:
            pts = prov_coords[cp]
            lat = sum(p[0] for p in pts) / len(pts)
            lon = sum(p[1] for p in pts) / len(pts)
        else:
            lat, lon = 12.8797, 121.7740

        # Distance to Converge
        dist_node_km = fast_nearest_distance(lat, lon, node_grid)
        dist_line_km = fast_nearest_distance(lat, lon, line_grid)

        # Capacity & Subscribers
        households = b['households']
        subs_target = max(1, int(round(households * A['penetration_rate'])))
        peak_bts = max(1, math.ceil(subs_target / A['subs_per_bts']))

        # 1. Commercial Pillar 1: Deployment Ease
        deploy_score = 100.0 * math.exp(-dist_node_km / A['deploy_decay_km'])
        deploy_score = max(15.0, min(100.0, deploy_score))
        if dist_line_km <= A['fiber_corridor_km']:
            deploy_score = min(100.0, deploy_score + A['fiber_corridor_bonus'])

        # 2. Commercial Pillar 2: Business Viability
        poverty_pct = b['poverty_rate']
        viable_subs = subs_target * (1.0 - 0.40 * (poverty_pct / 100.0))
        lo, hi = A['sweet_spot_low'], A['sweet_spot_high']
        if viable_subs <= 0: viab_score = 0.0
        elif viable_subs < lo: viab_score = 20.0 + 80.0 * (viable_subs / lo)
        elif viable_subs <= hi: viab_score = 100.0
        else:
            excess = (viable_subs - hi) / A['subs_per_bts']
            viab_score = max(70.0, 100.0 - 6.0 * math.log1p(excess))

        if 'NCR' in b['region']: viab_score -= A['ncr_penalty']
        elif 'BARMM' in b['region']: viab_score -= A['barmm_penalty']
        elif any(r in b['region'] for r in ['Region IV-A', 'Region III', 'Region VII', 'Region VI', 'Region I', 'Region XI', 'Region X', 'Region II', 'Region V']):
            viab_score += 4.0
        viab_score = max(0.0, min(100.0, viab_score))

        # 3. Commercial Pillar 3: Necessity
        rural_comp = 85.0 if b['ur'] == 'R' else 25.0
        class_comp = {'6th': 100.0, '5th': 85.0, '4th': 70.0}.get(b['income_class'], 35.0) if b['is_class_4_6'] else 35.0
        if dist_node_km <= 3.0: offnet_comp = 25.0
        elif dist_node_km >= 10.0: offnet_comp = 100.0
        else: offnet_comp = 25.0 + 75.0 * ((dist_node_km - 3.0) / 7.0)
        poverty_comp = min(100.0, max(20.0, poverty_pct * 3.5))

        nec_score = (0.40 * rural_comp) + (0.25 * class_comp) + (0.20 * offnet_comp) + (0.15 * poverty_comp)
        if 'NCR' in b['region']: nec_score -= A['ncr_penalty']
        nec_score = max(0.0, min(100.0, nec_score))

        # Commercial Composite
        commercial_composite = (deploy_score * A['weight_deploy'] +
                                viab_score * A['weight_viability'] +
                                nec_score * A['weight_necessity'])

        # GIDA Metric
        gida_raw_score = (undp_data.get((cp, cm, cb)) or
                          undp_data.get((cm, cb)) or
                          undp_data.get((np_, nm_, nb_)) or
                          undp_data.get((nm_, nb_)) or 26.60) # 26.60 is national mean GIDA score
        norm_gida_score = min(100.0, round((gida_raw_score / 69.91) * 100.0, 2))

        # Combined Hybrid Score (50/50 Baseline)
        combined_score = (A['weight_commercial_blend'] * commercial_composite) + (A['weight_gida_blend'] * norm_gida_score)

        # Backhaul Architecture
        if dist_node_km <= A['optical_dist_threshold']:
            backhaul_type = "Direct Optical Drop (<3km)"
        elif dist_node_km <= A['starlink_dist_threshold'] or dist_line_km <= 2.0:
            backhaul_type = "Near Optical / Microwave (<5km)"
        else:
            backhaul_type = "Starlink Business LEO Satellite Backhaul (>5km)"

        # Priority Classification
        if combined_score >= 70.0: tier_label = "Priority Tier 1 (High Commercial & Social)"
        elif combined_score >= 60.0: tier_label = "Priority Tier 2 (Balanced Opportunity)"
        else: tier_label = "Priority Tier 3 (Broadband Expansion)"

        scored.append({
            'psgc': b['psgc'], 'region': b['region'], 'province': b['province'],
            'municipality': b['municipality'], 'barangay': b['barangay'],
            'lat': round(lat, 6), 'lon': round(lon, 6), 'ur': b['ur'],
            'pop': b['pop'], 'hh_size': round(b['avg_hh'], 2), 'households': households,
            'subs_target': subs_target, 'carrier': A['carrier_name'],
            'peak_bts': peak_bts, 'phase1_bts': 1,
            'dist_node_km': round(dist_node_km, 2), 'dist_line_km': round(dist_line_km, 2),
            'backhaul_type': backhaul_type,
            'commercial_score': round(commercial_composite, 2),
            'norm_gida_score': norm_gida_score,
            'combined_score': round(combined_score, 2),
            'poverty_pct': poverty_pct,
            'tier_label': tier_label
        })

    # Sort Descending by Combined Score
    scored.sort(key=lambda x: (x['combined_score'], x['commercial_score'], x['norm_gida_score']), reverse=True)
    for idx, b in enumerate(scored, 1):
        b['overall_rank'] = idx
        b['batch_num'] = (idx - 1) // A['batch_size'] + 1
        b['batch_rank'] = (idx - 1) % A['batch_size'] + 1

    top5k = scored[:5000]
    print(f"  -> Top Combined Site: {top5k[0]['barangay']}, {top5k[0]['municipality']} (Score: {top5k[0]['combined_score']})")
    print(f"  -> 1,000th Site Score: {top5k[999]['combined_score']} | 5,000th Site Score: {top5k[4999]['combined_score']}")

    # ------------------------------------------------------------------------
    # STEP 6: Generate Standard 8-Tab Excel Workbook (Combined Edition)
    # ------------------------------------------------------------------------
    print("\n[Step 6/7] Generating Standard Reconciled Combined Excel Workbook...")
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    font_title = Font(name='Calibri', size=16, bold=True, color='1B365D')
    font_subtitle = Font(name='Calibri', size=10, italic=True, color='595959')
    font_sec = Font(name='Calibri', size=12, bold=True, color='1B365D')
    font_header = Font(name='Calibri', size=10, bold=True, color='FFFFFF')
    font_data = Font(name='Calibri', size=9.5)
    font_bold = Font(name='Calibri', size=9.5, bold=True)
    font_kpi_num = Font(name='Calibri', size=18, bold=True, color='1B365D')
    font_kpi_lbl = Font(name='Calibri', size=8.5, bold=True, color='595959')

    fill_navy = PatternFill(start_color='1B365D', end_color='1B365D', fill_type='solid')
    fill_blue_accent = PatternFill(start_color='0077B6', end_color='0077B6', fill_type='solid')
    fill_teal = PatternFill(start_color='00B4D8', end_color='00B4D8', fill_type='solid')
    fill_highlight_bts = PatternFill(start_color='E0F2FE', end_color='E0F2FE', fill_type='solid')
    fill_kpi = PatternFill(start_color='F0F4F8', end_color='F0F4F8', fill_type='solid')
    fill_zebra = PatternFill(start_color='F8FAFC', end_color='F8FAFC', fill_type='solid')
    fill_sec_hdr = PatternFill(start_color='E2E8F0', end_color='E2E8F0', fill_type='solid')
    font_italic = Font(name='Calibri', size=9.5, italic=True, color='595959')

    border_thin = Border(left=Side(style='thin', color='D9D9D9'), right=Side(style='thin', color='D9D9D9'),
                         top=Side(style='thin', color='D9D9D9'), bottom=Side(style='thin', color='D9D9D9'))
    border_total = Border(left=Side(style='thin', color='D9D9D9'), right=Side(style='thin', color='D9D9D9'),
                          top=Side(style='thin', color='1B365D'), bottom=Side(style='double', color='1B365D'))
    border_header = Border(left=Side(style='thin', color='FFFFFF'), right=Side(style='thin', color='FFFFFF'),
                           top=Side(style='medium', color='1B365D'), bottom=Side(style='medium', color='1B365D'))

    align_center = Alignment(horizontal='center', vertical='center', wrap_text=True)
    align_left = Alignment(horizontal='left', vertical='center', wrap_text=True)
    align_right = Alignment(horizontal='right', vertical='center')

    # Batch Statistics
    b1 = top5k[:1000]
    b2 = top5k[1000:2000]
    b3 = top5k[2000:3000]
    b4 = top5k[3000:4000]
    b5 = top5k[4000:5000]

    b_groups = [b1, b2, b3, b4, b5]
    b_stats = []
    for bg in b_groups:
        pop = sum(x['pop'] for x in bg)
        hh = sum(x['households'] for x in bg)
        subs = sum(x['subs_target'] for x in bg)
        d1 = len(bg)
        peak = sum(x['peak_bts'] for x in bg)
        comb_score = sum(x['combined_score'] for x in bg) / len(bg)
        comm_score = sum(x['commercial_score'] for x in bg) / len(bg)
        gida_score = sum(x['norm_gida_score'] for x in bg) / len(bg)
        c_dir = sum(1 for x in bg if 'Direct Optical' in x['backhaul_type'])
        c_near = sum(1 for x in bg if 'Near Optical' in x['backhaul_type'])
        c_star = sum(1 for x in bg if 'Starlink' in x['backhaul_type'])
        b_stats.append((len(bg), pop, hh, subs, d1, peak, comb_score, comm_score, gida_score, c_dir, c_near, c_star))

    # ========================================================================
    # TAB 1: READ ME (Exhaustive 7 Sections)
    # ========================================================================
    ws_rm = wb.create_sheet(title='Read Me')
    ws_rm.views.sheetView[0].showGridLines = True
    ws_rm.column_dimensions['A'].width = 6
    ws_rm.column_dimensions['B'].width = 28
    ws_rm.column_dimensions['C'].width = 42
    ws_rm.column_dimensions['D'].width = 55

    ws_rm['B2'] = "PHILIPPINE 5G FIXED WIRELESS ACCESS (FWA) - COMBINED HYBRID MODEL"
    ws_rm['B2'].font = font_title
    ws_rm['B3'] = "Commercial Viability & DICT / UNDP GIDA Prioritization Synthesis (50/50 Dual Optimization)"
    ws_rm['B3'].font = font_subtitle

    readme_rows = [
        ("SECTION 1: EXECUTIVE OVERVIEW & PURPOSE", "", "", True),
        ("Project Objective", "5G FWA Barangay Siting & Rollout Schedule (Combined Model)", "Synthesizes commercial viability with social impact by combining POPCEN 2024 economic metrics with the official DICT / UNDP GIDA Prioritization Tool."),
        ("Dual Optimization", "50% Commercial + 50% Social Impact Baseline", "Balances rapid revenue turn-up and low capex backhaul with universal service obligations and GIDA poverty alleviation."),
        ("Target Spectrum", "Band n50 (1427 - 1518 MHz, 100 MHz TDD)", "Single-carrier deployment optimized for high speed, long range, and robust penetration."),
        ("BTS Siting Standard", "1 BTS per Barangay (Day 1) -> Dynamic Peak", "Dimensioned at 1,000 active subscribers per BTS (~333 per sector across 3 sectors)."),
        ("Backhaul Resilience", "Hybrid Optical + Starlink LEO Satellite", "Direct Optical Drop (<3km), Near Optical/Microwave (3-5km), and Starlink Business LEO Satellite (>5km)."),
        ("", "", "", False),

        ("SECTION 2: MODEL ARCHITECTURE & BLENDED SCORING MECHANISM", "", "", True),
        ("Commercial Pillar", "POPCEN 2024 Siting Engine (Weight: 50%)", "Evaluates Deployment Ease (35%), Commercial Viability (35%), and Broadband Necessity (30%)."),
        ("GIDA Social Pillar", "DICT / UNDP Looker Studio Model (Weight: 50%)", "Evaluates 11 Looker Studio criteria: mobile speeds, road distance, nighttime lights, hazard, insurgency, poverty, POIs, towers."),
        ("Synthesis Formula", "Combined Score = (w_comm * S_comm) + (w_gida * S_gida)", "Standardized 0-100 score providing a balanced national priority queue."),
        ("Phased Allocation", "5 Batches x 1,000 Sites = 5,000 Sites", "Batch 1 delivers maximum strategic value: strong commercial viability combined with acute social impact."),
        ("", "", "", False),

        ("SECTION 3: WORKBOOK NAVIGATION & SHEET DIRECTORY", "", "", True),
        ("Read Me", "Methodological Documentation & Data Dictionary", "Complete guide to hybrid scoring, data dictionary, and official sources."),
        ("Executive Summary", "KPI Dashboard & Batch Comparison Table", "6 KPI cards, 13-column batch breakdown, and transmission splits."),
        ("Methodology & Assumptions", "Parameter Inputs & Blended Weights", "Exhaustive formulas, sensitivity weights, and technical dimensioning."),
        ("Batch 1 (First 1,000)", "Sites 1 - 1,000 (Top Hybrid Sites)", "The top 1,000 dual-optimized barangays nationwide for immediate deployment."),
        ("Batch 2 (1,001 - 2,000)", "Sites 1,001 - 2,000", "Second phase expansion balancing high commercial demand with remote coverage."),
        ("Batch 3 (2,001 - 3,000)", "Sites 2,001 - 3,000", "Third phase regional expansion across Visayas and Mindanao."),
        ("Batch 4 & 5 (3,001 - 5,000)", "Sites 3,001 - 5,000", "Final phases completing national coverage across 5,000 sites."),
        ("Provincial Summary", "Provincial Aggregation & Siting Analysis", "Detailed summary table by province showing site counts, population, and backhaul mix."),
        ("", "", "", False),

        ("SECTION 4: DATA SOURCES & OFFICIAL CITATIONS", "", "", True),
        ("UNDP / DICT GIDA Tool", "Looker Studio Decision Support Tool (2026)", "https://lookerstudio.google.com/u/0/reporting/7118ca47-1563-4f51-b0db-a19b8ea4f3c7/page/p_6h58g3u7ld"),
        ("PSA 2024 POPCEN", "Proclamation No. 973 (Official National Total: 112,729,484)", "https://psa.gov.ph/content/2024-census-population-popcen-population-counts-declared-official-president"),
        ("PSA FIES Poverty Data", "2024 Full Year Official Poverty Statistics", "https://psa.gov.ph/statistics/income-expenditure/fies/stat-tables/released/2026"),
        ("Converge Backbone GIS", "National & Regional Backbone KMZ (Nov 2024)", "2,405 verified terrestrial optical nodes and 334k line vertices."),
        ("", "", "", False),

        ("SECTION 5: COMPLETE 26-COLUMN DATA DICTIONARY", "", "", True),
        ("Col A: Batch Number", "Rollout Phase Identifier", "Batch 1 to 5 corresponding to sequential 1,000-site rollout phases."),
        ("Col B: Batch Rank", "Relative Priority Within Batch", "Sequential priority index from 1 to 1,000 within each batch."),
        ("Col C: Overall Rank", "National Priority Ranking (1 to 5,000)", "Strict rank based on descending Combined Hybrid Score."),
        ("Col D: PSGC Code", "Philippine Standard Geographic Code", "Official administrative identifier."),
        ("Col E: Region", "Administrative Region Name", "Official Philippine administrative region."),
        ("Col F: Province", "Province Name", "Official province or highly urbanized city cluster."),
        ("Col G: Municipality", "Municipality / City Name", "Official local government unit (LGU) name."),
        ("Col H: Barangay", "Barangay Name", "Official barangay name."),
        ("Col I: Latitude", "WGS84 Latitude", "Decimal degrees coordinate."),
        ("Col J: Longitude", "WGS84 Longitude", "Decimal degrees coordinate."),
        ("Col K: Urban / Rural (U/R)", "PSA Urbanity Classification", "R = Rural, U = Urban per official PSA classification."),
        ("Col L: 2024 Population", "2024 POPCEN Scaled Population", "Scaled directly to official PSA 2024 Census of Population."),
        ("Col M: 2024 Avg HH Size", "Provincial Average Household Size", "Official 2024 PSA household size matrix (national average: 3.8)."),
        ("Col N: 2024 Households", "Total Estimated Households", "Computed as Population / Avg Household Size."),
        ("Col O: Target Subscribers", "30% Commercial Penetration", "30% of total households representing commercial addressable demand."),
        ("Col P: Carrier Spectrum", "Band n50 (100MHz TDD)", "Single-carrier spectrum allocation (1427-1518 MHz)."),
        ("Col Q: Peak BTS Required", "Full Capacity BTS Count", "Calculated as CEILING(Target Subscribers / 1,000)."),
        ("Col R: Day 1 BTS Deployed", "Initial Phase 1 Deployment", "Standardized at 1 BTS per barangay for immediate service turn-up."),
        ("Col S: Dist to Converge Node", "Fiber Node Proximity (km)", "Haversine distance to nearest Converge optical backbone node."),
        ("Col T: Dist to Converge Line", "Fiber Route Proximity (km)", "Haversine distance to nearest Converge transmission line vertex."),
        ("Col U: Backhaul Architecture", "Transmission Siting Designation", "Direct Optical Drop (<3km), Near Optical (3-5km), Starlink LEO Satellite (>5km)."),
        ("Col V: Commercial Score", "Commercial Viability Composite (0-100)", "Weighted sum of Deployment Ease (35%), Viability (35%), and Necessity (30%)."),
        ("Col W: Normalized GIDA Score", "Standardized GIDA Score (0-100)", "Computed as MIN(100, ROUND((Official Looker Score / 69.91) * 100, 2))."),
        ("Col X: Combined Hybrid Score", "Dual Optimization Score (0-100)", "Computed as (w_comm * Commercial) + (w_gida * GIDA)."),
        ("Col Y: Regional Poverty %", "PSA FIES Regional Poverty Rate", "Official 2024 regional poverty incidence percentage."),
        ("Col Z: Priority Classification", "Strategic Classification", "Priority Tier 1 (High Commercial & Social), Tier 2 (Balanced), Tier 3 (Expansion)."),
        ("", "", "", False),

        ("SECTION 6: KEY ASSUMPTIONS & TECHNICAL PARAMETERS", "", "", True),
        ("Commercial Weight (w_comm)", "50.0%", "Weight allocated to commercial ROI and rapid deployment feasibility."),
        ("GIDA Weight (w_gida)", "50.0%", "Weight allocated to DICT/UNDP social equity and digital divide closure."),
        ("Household Penetration", "30.0%", "Commercial take rate applied across total barangay households."),
        ("BTS Capacity Ceiling", "1,000 Subscribers per Node", "Dimensioned across 3 sectors (~333 subscribers per 120° sector)."),
        ("Direct Optical Limit", "3.0 Kilometers", "Sites within 3.0km connect via direct fiber drop to Converge nodes."),
        ("Near Optical Limit", "5.0 Kilometers", "Sites between 3.0km and 5.0km connect via short-hop microwave or fiber corridor."),
        ("Starlink LEO Satellite", "> 5.0 Kilometers", "Sites beyond 5.0km utilize Starlink Business LEO satellite terminals."),
        ("", "", "", False),

        ("SECTION 7: VERSION CONTROL & GOVERNANCE", "", "", True),
        ("Model Edition", "Model 3: Combined Hybrid Rollout Plan (50/50 Dual Optimization)", "Released September 2026 for Executive Investment Review."),
        ("Cross-Model Reconciliation", "Synthesizes Model 1 (POPCEN 2024) and Model 2 (UNDP GIDA)", "Reconciled with single-digit mathematical precision.")
    ]

    r_curr = 5
    for item in readme_rows:
        if len(item) == 4 and item[3]:
            ws_rm.merge_cells(start_row=r_curr, start_column=2, end_row=r_curr, end_column=4)
            cell = ws_rm.cell(r_curr, 2, item[0])
            cell.font = Font(name='Calibri', size=11, bold=True, color='1B365D')
            cell.fill = fill_sec_hdr
            cell.alignment = align_left
            r_curr += 1
        elif not item[0]:
            r_curr += 1
        else:
            ws_rm.cell(r_curr, 2, item[0]).font = font_bold
            ws_rm.cell(r_curr, 2).border = border_thin
            ws_rm.cell(r_curr, 3, item[1]).font = font_data
            ws_rm.cell(r_curr, 3).border = border_thin
            ws_rm.cell(r_curr, 4, item[2]).font = font_data
            ws_rm.cell(r_curr, 4).border = border_thin
            r_curr += 1

    # ========================================================================
    # TAB 2: EXECUTIVE SUMMARY (6 KPI Cards + 13-Col Comparison Table)
    # ========================================================================
    ws_es = wb.create_sheet(title='Executive Summary')
    ws_es.views.sheetView[0].showGridLines = True
    for c_idx in range(1, 15):
        ws_es.column_dimensions[get_column_letter(c_idx)].width = 16

    ws_es['A2'] = "PHILIPPINE 5G FIXED WIRELESS ACCESS (FWA) ROLLOUT PLAN"
    ws_es['A2'].font = font_title
    ws_es['A3'] = "Executive Summary Dashboard | Model 3: Hybrid Combined Model (50% Commercial / 50% GIDA Social Impact)"
    ws_es['A3'].font = font_subtitle

    # KPI Cards (Row 5 to 7)
    kpis = [
        ("TOTAL HYBRID SITES", f"{len(top5k):,}", 1, 2),
        ("BATCH 1 SUBSCRIBERS", f"{b_stats[0][3]:,}", 3, 4),
        ("TOTAL TARGET SUBS", f"{sum(x[3] for x in b_stats):,}", 5, 6),
        ("PEAK BTS REQUIRED", f"{sum(x[5] for x in b_stats):,}", 7, 8),
        ("FIBER PROXIMITY (<5km)", f"{sum(x[9]+x[10] for x in b_stats):,}", 9, 10),
        ("STARLINK SATELLITE (>5km)", f"{sum(x[11] for x in b_stats):,}", 11, 12),
    ]

    for title, val, c_start, c_end in kpis:
        ws_es.merge_cells(start_row=5, start_column=c_start, end_row=5, end_column=c_end)
        c_lbl = ws_es.cell(5, c_start, title)
        c_lbl.font = font_kpi_lbl
        c_lbl.alignment = align_center
        c_lbl.fill = fill_kpi

        ws_es.merge_cells(start_row=6, start_column=c_start, end_row=7, end_column=c_end)
        c_val = ws_es.cell(6, c_start, val)
        c_val.font = font_kpi_num
        c_val.alignment = align_center
        c_val.fill = fill_kpi

        for r_ in range(5, 8):
            for c_ in range(c_start, c_end + 1):
                ws_es.cell(r_, c_).border = border_thin

    # Batch Comparison Table (Row 10 to 22)
    ws_es['A10'] = "Combined Hybrid Siting Phasing & Score Breakdown (Batches 1 to 5)"
    ws_es['A10'].font = font_sec

    headers_es = [
        "Rollout Phase", "Sites", "2024 Population", "2024 Households",
        "Target Subs (30%)", "Day 1 BTS", "Peak BTS", "Combined Score",
        "Commercial Score", "GIDA Score", "Direct Fiber (<3km)", "Near Fiber (3-5km)", "Starlink LEO (>5km)"
    ]

    for col_idx, h_text in enumerate(headers_es, 1):
        cell = ws_es.cell(12, col_idx, h_text)
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_center
        cell.border = border_header

    es_data = [
        ("Batch 1 (First 1,000)", b_stats[0]),
        ("Batch 2 (1,001 - 2,000)", b_stats[1]),
        ("Batch 3 (2,001 - 3,000)", b_stats[2]),
        ("Batch 4 (3,001 - 4,000)", b_stats[3]),
        ("Batch 5 (4,001 - 5,000)", b_stats[4]),
    ]

    for row_idx, (phase_name, st) in enumerate(es_data, 13):
        ws_es.cell(row_idx, 1, phase_name).alignment = align_left
        ws_es.cell(row_idx, 2, st[0]).number_format = '#,##0'
        ws_es.cell(row_idx, 3, st[1]).number_format = '#,##0'
        ws_es.cell(row_idx, 4, st[2]).number_format = '#,##0'
        ws_es.cell(row_idx, 5, st[3]).number_format = '#,##0'
        ws_es.cell(row_idx, 6, st[4]).number_format = '#,##0'
        ws_es.cell(row_idx, 7, st[5]).number_format = '#,##0'
        ws_es.cell(row_idx, 8, round(st[6], 2)).number_format = '0.00'
        ws_es.cell(row_idx, 9, round(st[7], 2)).number_format = '0.00'
        ws_es.cell(row_idx, 10, round(st[8], 2)).number_format = '0.00'
        ws_es.cell(row_idx, 11, st[9]).number_format = '#,##0'
        ws_es.cell(row_idx, 12, st[10]).number_format = '#,##0'
        ws_es.cell(row_idx, 13, st[11]).number_format = '#,##0'

        for c_ in range(1, 14):
            ws_es.cell(row_idx, c_).font = font_data
            ws_es.cell(row_idx, c_).border = border_thin
            if c_ > 1: ws_es.cell(row_idx, c_).alignment = align_right

    # Total Row
    tot_row = 18
    ws_es.cell(tot_row, 1, "Total (5,000 Hybrid Sites)").font = font_bold
    ws_es.cell(tot_row, 2, sum(x[0] for x in b_stats)).number_format = '#,##0'
    ws_es.cell(tot_row, 3, sum(x[1] for x in b_stats)).number_format = '#,##0'
    ws_es.cell(tot_row, 4, sum(x[2] for x in b_stats)).number_format = '#,##0'
    ws_es.cell(tot_row, 5, sum(x[3] for x in b_stats)).number_format = '#,##0'
    ws_es.cell(tot_row, 6, sum(x[4] for x in b_stats)).number_format = '#,##0'
    ws_es.cell(tot_row, 7, sum(x[5] for x in b_stats)).number_format = '#,##0'
    ws_es.cell(tot_row, 8, round(sum(x[6] for x in b_stats)/5, 2)).number_format = '0.00'
    ws_es.cell(tot_row, 9, round(sum(x[7] for x in b_stats)/5, 2)).number_format = '0.00'
    ws_es.cell(tot_row, 10, round(sum(x[8] for x in b_stats)/5, 2)).number_format = '0.00'
    ws_es.cell(tot_row, 11, sum(x[9] for x in b_stats)).number_format = '#,##0'
    ws_es.cell(tot_row, 12, sum(x[10] for x in b_stats)).number_format = '#,##0'
    ws_es.cell(tot_row, 13, sum(x[11] for x in b_stats)).number_format = '#,##0'

    for c_ in range(1, 14):
        ws_es.cell(tot_row, c_).font = font_bold
        ws_es.cell(tot_row, c_).border = border_total
        if c_ > 1: ws_es.cell(tot_row, c_).alignment = align_right

    # Footnotes
    ws_es['A21'] = "* Strategic Note: Model 3 combines Commercial Viability (50%) and DICT/UNDP GIDA Prioritization (50%) for dual optimization."
    ws_es['A21'].font = font_italic
    ws_es['A22'] = "* Day 1 Siting: 1 BTS deployed per barangay; Peak BTS dimensioned @ 1,000 active subscribers per BTS node (~333/sector)."
    ws_es['A22'].font = font_italic

    # ========================================================================
    # TAB 3: METHODOLOGY & ASSUMPTIONS (Blended Formulas & Parameters)
    # ========================================================================
    ws_ma = wb.create_sheet(title='Methodology & Assumptions')
    ws_ma.views.sheetView[0].showGridLines = True
    ws_ma.column_dimensions['A'].width = 32
    ws_ma.column_dimensions['B'].width = 24
    ws_ma.column_dimensions['C'].width = 16
    ws_ma.column_dimensions['D'].width = 50

    ws_ma['A2'] = "METHODOLOGY & ASSUMPTIONS - COMBINED HYBRID MODEL"
    ws_ma['A2'].font = font_title
    ws_ma['A3'] = "Synthesis of Commercial Viability Siting & DICT / UNDP Multi-Criteria Decision Framework"
    ws_ma['A3'].font = font_subtitle

    # Parameters Table
    ws_ma['A5'] = "Parameter Name"
    ws_ma['B5'] = "Model Value"
    ws_ma['C5'] = "Unit"
    ws_ma['D5'] = "Methodological Rationale & Authority"
    for c_ in range(1, 5):
        cell = ws_ma.cell(5, c_)
        cell.font = font_header
        cell.fill = fill_navy
        cell.border = border_header

    params_data = [
        ("Commercial Blend Weight (w_comm)", 0.50, "50.0%", "Weight allocated to commercial ROI and rapid deployment feasibility."),
        ("GIDA Blend Weight (w_gida)", 0.50, "50.0%", "Weight allocated to DICT/UNDP social equity and digital divide closure."),
        ("Penetration Rate", 0.30, "30.0%", "Estimated commercial take-up rate across total barangay households."),
        ("Band n50 BTS Capacity", 1000, "1,000 Subs", "Total active subscriber capacity across 3 sectors (~333 subs/sector)."),
        ("Starlink LEO Distance Threshold", 5.0, "5.0 km", "Sites > 5km from Converge fiber assigned Starlink Business LEO satellite backhaul."),
        ("Direct Optical Drop Threshold", 3.0, "3.0 km", "Sites within 3.0km of Converge optical backbone connect via direct fiber lateral."),
        ("Default 2024 HH Size", 3.80, "3.80 Persons", "Official PSA 2024 POPCEN national average household size."),
        ("Commercial: Ease of Deployment Weight", 0.35, "35.0%", "Pillar 1 weight: fiber proximity and corridor lateral bonus."),
        ("Commercial: Business Viability Weight", 0.35, "35.0%", "Pillar 2 weight: sweet-spot demand curve discounted by FIES poverty."),
        ("Commercial: Broadband Necessity Weight", 0.30, "30.0%", "Pillar 3 weight: rural status, LGU class 4-6, off-net distance, poverty."),
        ("Total Hybrid Sites Dimensioned", 5000, "5,000 Sites", "National priority program synthesizing commercial and social reach.")
    ]

    for r_idx, (pname, pval, punit, pdesc) in enumerate(params_data, 6):
        ws_ma.cell(r_idx, 1, pname).font = font_bold
        ws_ma.cell(r_idx, 1).border = border_thin
        ws_ma.cell(r_idx, 2, pval).border = border_thin
        if isinstance(pval, float) and pval < 1.0: ws_ma.cell(r_idx, 2).number_format = '0.0%'
        elif isinstance(pval, (int, float)): ws_ma.cell(r_idx, 2).number_format = '#,##0'
        ws_ma.cell(r_idx, 3, punit).border = border_thin
        ws_ma.cell(r_idx, 3).alignment = align_center
        ws_ma.cell(r_idx, 4, pdesc).font = font_data
        ws_ma.cell(r_idx, 4).border = border_thin

    # Scoring Formulas Table
    ws_ma['A19'] = "Hybrid Scoring Mathematical Architecture"
    ws_ma['A19'].font = font_sec

    ws_ma['A21'] = "Component"
    ws_ma['B21'] = "Formula / Weight"
    ws_ma['C21'] = "Scale"
    ws_ma['D21'] = "Mathematical Definition"
    for c_ in range(1, 5):
        cell = ws_ma.cell(21, c_)
        cell.font = font_header
        cell.fill = fill_blue_accent
        cell.border = border_header

    formulas_data = [
        ("Combined Hybrid Score", "(w_comm * Commercial) + (w_gida * GIDA_Norm)", "0 - 100", "Dual-objective optimization synthesizing commercial viability with social impact."),
        ("Commercial Composite", "(0.35*Deploy) + (0.35*Viability) + (0.30*Necessity)", "0 - 100", "Three-pillar commercial suitability index anchored on Converge fiber network."),
        ("Normalized GIDA Score", "MIN(100, ROUND((Raw_GIDA_Score / 69.91) * 100, 2))", "0 - 100", "Official Looker Studio multi-criteria score standardized to 100-point scale."),
        ("Deployment Ease Score", "100 * EXP(-dist_node / 8.0) + Corridor_Bonus", "15 - 100", "Exponential decay based on optical fiber proximity."),
        ("Business Viability Score", "Sweet-spot curve on Viable_Subs [250 - 1,200]", "0 - 100", "Evaluates addressable subscriber volume adjusted for FIES poverty discount."),
        ("Broadband Necessity Score", "(0.40*Rural) + (0.25*Class) + (0.20*Offnet) + (0.15*Poverty)", "0 - 100", "Captures broadband deficit, unserved rural population, and lower-income LGUs.")
    ]

    for r_idx, (cname, cwt, cscale, cdef) in enumerate(formulas_data, 22):
        ws_ma.cell(r_idx, 1, cname).font = font_bold
        ws_ma.cell(r_idx, 1).border = border_thin
        ws_ma.cell(r_idx, 2, cwt).border = border_thin
        ws_ma.cell(r_idx, 2).alignment = align_center
        ws_ma.cell(r_idx, 3, cscale).border = border_thin
        ws_ma.cell(r_idx, 3).alignment = align_center
        ws_ma.cell(r_idx, 4, cdef).font = font_data
        ws_ma.cell(r_idx, 4).border = border_thin

    # ========================================================================
    # TAB 4 to 7: BATCH SHEETS (26 Columns)
    # ========================================================================
    batch_defs = [
        ('Batch 1 (First 1,000)', b1, 1, 1000),
        ('Batch 2 (1,001 - 2,000)', b2, 1001, 2000),
        ('Batch 3 (2,001 - 3,000)', b3, 2001, 3000),
        ('Batch 4 & 5 (3,001 - 5,000)', b4 + b5, 3001, 5000),
    ]

    batch_headers_26 = [
        "Batch", "Batch Rank", "Overall Rank", "PSGC", "Region", "Province", "Municipality", "Barangay",
        "Latitude", "Longitude", "U/R", "2024 Population", "2024 Avg HH Size", "2024 Households",
        "Target Subs (30%)", "Carrier Spectrum", "Peak BTS Required", "Day 1 BTS Deployed",
        "Dist to Node (km)", "Dist to Line (km)", "Backhaul Architecture",
        "Commercial Score", "Normalized GIDA Score", "Combined Hybrid Score",
        "Regional Poverty %", "Strategic Classification"
    ]

    for s_title, b_data, r_start, r_end in batch_defs:
        ws_b = wb.create_sheet(title=s_title)
        ws_b.views.sheetView[0].showGridLines = True

        ws_b['A1'] = f"5G FWA Combined Hybrid Siting Rollout Schedule - {s_title}"
        ws_b['A1'].font = font_title
        ws_b['A2'] = f"Commercial Viability & GIDA Dual Optimization ({len(b_data):,} Sites) | Band n50 (100MHz TDD)"
        ws_b['A2'].font = font_subtitle

        for col_idx, h_text in enumerate(batch_headers_26, 1):
            cell = ws_b.cell(4, col_idx, h_text)
            cell.font = font_header
            cell.fill = fill_navy
            cell.alignment = align_center
            cell.border = border_header

        for idx, site in enumerate(b_data, 5):
            ws_b.cell(idx, 1, site['batch_num']).alignment = align_center
            ws_b.cell(idx, 2, site['batch_rank']).alignment = align_center
            ws_b.cell(idx, 3, site['overall_rank']).alignment = align_center
            ws_b.cell(idx, 4, site['psgc']).alignment = align_center
            ws_b.cell(idx, 5, site['region']).alignment = align_left
            ws_b.cell(idx, 6, site['province']).alignment = align_left
            ws_b.cell(idx, 7, site['municipality']).alignment = align_left
            ws_b.cell(idx, 8, site['barangay']).alignment = align_left
            ws_b.cell(idx, 9, site['lat']).number_format = '0.000000'
            ws_b.cell(idx, 10, site['lon']).number_format = '0.000000'
            ws_b.cell(idx, 11, site['ur']).alignment = align_center
            ws_b.cell(idx, 12, site['pop']).number_format = '#,##0'
            ws_b.cell(idx, 13, site['hh_size']).number_format = '0.00'
            ws_b.cell(idx, 14, site['households']).number_format = '#,##0'
            ws_b.cell(idx, 15, site['subs_target']).number_format = '#,##0'
            ws_b.cell(idx, 16, site['carrier']).alignment = align_center
            ws_b.cell(idx, 17, site['peak_bts']).number_format = '#,##0'
            ws_b.cell(idx, 18, site['phase1_bts']).number_format = '#,##0'
            ws_b.cell(idx, 19, site['dist_node_km']).number_format = '0.00'
            ws_b.cell(idx, 20, site['dist_line_km']).number_format = '0.00'
            ws_b.cell(idx, 21, site['backhaul_type']).alignment = align_left
            ws_b.cell(idx, 22, site['commercial_score']).number_format = '0.00'
            ws_b.cell(idx, 23, site['norm_gida_score']).number_format = '0.00'
            ws_b.cell(idx, 24, site['combined_score']).number_format = '0.00'
            ws_b.cell(idx, 25, site['poverty_pct']).number_format = '0.0%'
            ws_b.cell(idx, 26, site['tier_label']).alignment = align_left

            for c_ in range(1, 27):
                cell = ws_b.cell(idx, c_)
                cell.font = font_data
                cell.border = border_thin
                if c_ in [17, 18]:
                    cell.fill = fill_highlight_bts

        # Summary Row
        sum_row = len(b_data) + 5
        ws_b.cell(sum_row, 1, "BATCH TOTAL / AVERAGE").font = font_bold
        ws_b.cell(sum_row, 12, f"=SUM(L5:L{sum_row-1})").number_format = '#,##0'
        ws_b.cell(sum_row, 14, f"=SUM(N5:N{sum_row-1})").number_format = '#,##0'
        ws_b.cell(sum_row, 15, f"=SUM(O5:O{sum_row-1})").number_format = '#,##0'
        ws_b.cell(sum_row, 17, f"=SUM(Q5:Q{sum_row-1})").number_format = '#,##0'
        ws_b.cell(sum_row, 18, f"=SUM(R5:R{sum_row-1})").number_format = '#,##0'
        ws_b.cell(sum_row, 19, f"=AVERAGE(S5:S{sum_row-1})").number_format = '0.00'
        ws_b.cell(sum_row, 22, f"=AVERAGE(V5:V{sum_row-1})").number_format = '0.00'
        ws_b.cell(sum_row, 23, f"=AVERAGE(W5:W{sum_row-1})").number_format = '0.00'
        ws_b.cell(sum_row, 24, f"=AVERAGE(X5:X{sum_row-1})").number_format = '0.00'

        for c_ in range(1, 27):
            cell = ws_b.cell(sum_row, c_)
            cell.font = font_bold
            cell.border = border_total

        # Set Column Widths
        for c_idx in range(1, 27):
            ws_b.column_dimensions[get_column_letter(c_idx)].width = 14
        ws_b.column_dimensions['E'].width = 16
        ws_b.column_dimensions['F'].width = 18
        ws_b.column_dimensions['G'].width = 18
        ws_b.column_dimensions['H'].width = 22
        ws_b.column_dimensions['P'].width = 22
        ws_b.column_dimensions['U'].width = 30
        ws_b.column_dimensions['Z'].width = 32

    # ========================================================================
    # TAB 8: PROVINCIAL SUMMARY
    # ========================================================================
    ws_ps = wb.create_sheet(title='Provincial Summary')
    ws_ps.views.sheetView[0].showGridLines = True
    ws_ps['A1'] = "5G FWA Combined Hybrid Siting - Provincial Aggregation Summary"
    ws_ps['A1'].font = font_title
    ws_ps['A2'] = "Distribution of 5,000 Prioritized Hybrid Sites across Provinces"
    ws_ps['A2'].font = font_subtitle

    headers_ps = [
        "Region", "Province", "Hybrid Sites", "2024 Population", "2024 Households",
        "Target Subs", "Day 1 BTS", "Peak BTS", "Avg Combined Score", "Direct Fiber (<3km)", "Near Fiber (3-5km)", "Starlink LEO (>5km)"
    ]
    for c_idx, h_text in enumerate(headers_ps, 1):
        cell = ws_ps.cell(4, c_idx, h_text)
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_center
        cell.border = border_header

    prov_agg = defaultdict(lambda: {
        'sites': 0, 'pop': 0, 'hh': 0, 'subs': 0, 'd1': 0, 'peak': 0,
        'scores': [], 'dir': 0, 'near': 0, 'star': 0, 'region': ''
    })

    for site in top5k:
        p = site['province']
        prov_agg[p]['sites'] += 1
        prov_agg[p]['pop'] += site['pop']
        prov_agg[p]['hh'] += site['households']
        prov_agg[p]['subs'] += site['subs_target']
        prov_agg[p]['d1'] += site['phase1_bts']
        prov_agg[p]['peak'] += site['peak_bts']
        prov_agg[p]['scores'].append(site['combined_score'])
        prov_agg[p]['region'] = site['region']
        if 'Direct Optical' in site['backhaul_type']: prov_agg[p]['dir'] += 1
        elif 'Near Optical' in site['backhaul_type']: prov_agg[p]['near'] += 1
        else: prov_agg[p]['star'] += 1

    sorted_provs = sorted(prov_agg.items(), key=lambda x: x[1]['sites'], reverse=True)

    for r_idx, (pname, pa) in enumerate(sorted_provs, 5):
        ws_ps.cell(r_idx, 1, pa['region']).alignment = align_left
        ws_ps.cell(r_idx, 2, pname).alignment = align_left
        ws_ps.cell(r_idx, 3, pa['sites']).number_format = '#,##0'
        ws_ps.cell(r_idx, 4, pa['pop']).number_format = '#,##0'
        ws_ps.cell(r_idx, 5, pa['hh']).number_format = '#,##0'
        ws_ps.cell(r_idx, 6, pa['subs']).number_format = '#,##0'
        ws_ps.cell(r_idx, 7, pa['d1']).number_format = '#,##0'
        ws_ps.cell(r_idx, 8, pa['peak']).number_format = '#,##0'
        ws_ps.cell(r_idx, 9, sum(pa['scores'])/len(pa['scores'])).number_format = '0.00'
        ws_ps.cell(r_idx, 10, pa['dir']).number_format = '#,##0'
        ws_ps.cell(r_idx, 11, pa['near']).number_format = '#,##0'
        ws_ps.cell(r_idx, 12, pa['star']).number_format = '#,##0'

        for c_ in range(1, 13):
            cell = ws_ps.cell(r_idx, c_)
            cell.font = font_data
            cell.border = border_thin
            if c_ > 2: cell.alignment = align_right

    for c_idx in range(1, 13):
        ws_ps.column_dimensions[get_column_letter(c_idx)].width = 16

    std_xlsx_path = os.path.join(OUT_DIR, "FWA_Barangay_Rollout_Plan_Combined_1000s.xlsx")
    wb.save(std_xlsx_path)
    wb.close()
    print(f"  -> Successfully saved standard workbook: {std_xlsx_path}")

    # ------------------------------------------------------------------------
    # STEP 7: Generate Dynamic Excel Workbook (Combined Edition)
    # ------------------------------------------------------------------------
    print("\n[Step 7/7] Generating Dynamic Combined Excel Workbook...")
    dyn_xlsx_path = os.path.join(OUT_DIR, "FWA_Barangay_Rollout_Plan_Combined_1000s_Dynamic.xlsx")
    generate_dynamic_version(std_xlsx_path, dyn_xlsx_path)

    # ------------------------------------------------------------------------
    # STEP 8: Generate GIS KMZ, JS, Presentation HTML & Executive Summary MD
    # ------------------------------------------------------------------------
    print("\n[Step 8/8] Generating GIS KMZ, Presentation & Executive Summary...")
    
    # 1. KML / KMZ Generation
    kml_header = '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n  <Document>\n    <name>FWA 5G Rollout Sites (Combined Model - Top 5,000)</name>\n    <description>Commercial & GIDA Hybrid Prioritization Model</description>\n'
    kml_footer = '  </Document>\n</kml>'
    kml_placemarks = []
    for s in top5k:
        pm = f"""    <Placemark>
      <name>{s['barangay']}, {s['municipality']}</name>
      <description><![CDATA[
        <b>Overall Rank:</b> {s['overall_rank']}<br/>
        <b>Batch:</b> Phase {s['batch_num']} (Rank {s['batch_rank']})<br/>
        <b>Combined Score:</b> {s['combined_score']:.2f}<br/>
        <b>Commercial Score:</b> {s['commercial_score']:.2f}<br/>
        <b>GIDA Norm Score:</b> {s['norm_gida_score']:.2f}<br/>
        <b>Classification:</b> {s['tier_label']}<br/>
        <b>Backhaul:</b> {s['backhaul_type']}<br/>
        <b>2024 Population:</b> {s['pop']:,}<br/>
        <b>2024 Households:</b> {s['households']:,}<br/>
        <b>Target Subs:</b> {s['subs_target']:,}<br/>
        <b>Peak BTS:</b> {s['peak_bts']}<br/>
        <b>Dist to Fiber:</b> {s['dist_node_km']:.2f} km
      ]]></description>
      <Point>
        <coordinates>{s['lon']},{s['lat']},0</coordinates>
      </Point>
    </Placemark>"""
        kml_placemarks.append(pm)

    kml_content = kml_header + "\n".join(kml_placemarks) + "\n" + kml_footer
    kml_path = os.path.join(OUT_DIR, "FWA_Rollout_Sites_Combined.kml")
    with open(kml_path, "w", encoding="utf-8") as f:
        f.write(kml_content)

    kmz_path = os.path.join(OUT_DIR, "FWA_Rollout_Sites_Combined.kmz")
    with zipfile.ZipFile(kmz_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(kml_path, arcname="doc.kml")
    print(f"  -> Generated KMZ: {kmz_path}")

    # 2. JS Data file for map portal
    js_path = os.path.join(OUT_DIR, "fwa_sites_data_combined.js")
    js_sites = [{
        'rank': s['overall_rank'], 'batch': s['batch_num'], 'b_rank': s['batch_rank'],
        'bgy': s['barangay'], 'mun': s['municipality'], 'prov': s['province'], 'reg': s['region'],
        'lat': s['lat'], 'lon': s['lon'], 'pop': s['pop'], 'hh': s['households'],
        'subs': s['subs_target'], 'peak_bts': s['peak_bts'], 'd1_bts': s['phase1_bts'],
        'dist_node': s['dist_node_km'], 'tier': s['tier_label'], 'backhaul': s['backhaul_type'],
        'comb_score': s['combined_score'], 'comm_score': s['commercial_score'], 'gida_score': s['norm_gida_score']
    } for s in top5k]
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("const fwaSitesDataCombined = " + json.dumps(js_sites, indent=2) + ";\n")
    print(f"  -> Generated JS Data: {js_path}")

    # 3. Metric-to-Source Mapping Excel & CSV
    map_xlsx_path = os.path.join(OUT_DIR, "FWA_Metric_to_Source_Mapping_Combined.xlsx")
    wb_map = openpyxl.Workbook()
    ws_m_map = wb_map.active
    ws_m_map.title = "Metric to Source Mapping"
    ws_m_map.views.sheetView[0].showGridLines = True

    m_headers = ["Pillar / Dimension", "Specific Metric", "Weight", "Data Source", "Source URL", "Technical Definition & Rationale"]
    for c_idx, h in enumerate(m_headers, 1):
        cell = ws_m_map.cell(1, c_idx, h)
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_center

    m_rows = [
        ("Combined Hybrid Core", "Commercial Viability Index", "50%", "POPCEN 2024 + Converge GIS + FIES", "Internal Commercial Model", "Blends deployment ease (35%), viability (35%), and necessity (30%)."),
        ("Combined Hybrid Core", "DICT / UNDP GIDA Index", "50%", "UNDP Looker Studio Prioritization Tool", "https://lookerstudio.google.com/u/0/reporting/7118ca47-1563-4f51-b0db-a19b8ea4f3c7/page/p_6h58g3u7ld", "Standardized Looker Studio score based on 11 official multi-criteria indicators."),
        ("Commercial Siting", "Deployment Ease (Node/Line)", "35% (of Comm)", "Converge ICT Backbone GIS Nov 2024", "Converge ICT Nov 2024 Infrastructure Report", "Haversine distance decay to nearest optical node + fiber corridor bonus."),
        ("Commercial Siting", "Business Viability Curve", "35% (of Comm)", "PSA 2024 POPCEN & FIES Poverty", "https://psa.gov.ph/statistics/income-expenditure/fies/stat-tables/released/2026", "Subscribers sweet-spot [250-1,200] discounted by regional poverty rate."),
        ("Commercial Siting", "Broadband Necessity", "30% (of Comm)", "PSA Urbanity, DOF LGU Income Class", "https://psa.gov.ph/content/2024-census-population-popcen-population-counts-declared-official-president", "Weighted composite of rural status (40%), LGU class 4-6 (25%), off-net (20%), poverty (15%)."),
        ("GIDA Criteria", "Mobile Downspeed", "10% (of GIDA)", "Ookla Speedtest Intelligence", "Looker Studio GIDA Database", "Measures average cellular mobile download speed in the barangay."),
        ("GIDA Criteria", "FW4A Presence", "10% (of GIDA)", "DICT Fixed Wireless Siting Audit", "Looker Studio GIDA Database", "Identifies existing Fixed Wireless Access 4G/5G deployments."),
        ("GIDA Criteria", "Nighttime Lights Radiance", "15% (of GIDA)", "VIIRS / NASA Earth Observatory", "Looker Studio GIDA Database", "Measures electrification and nocturnal human settlement radiance."),
        ("GIDA Criteria", "Surrounding POIs", "10% (of GIDA)", "OpenStreetMap / DepEd / DOH", "Looker Studio GIDA Database", "Density of public schools, rural health units, and community centers."),
        ("GIDA Criteria", "Distance to Road Network", "15% (of GIDA)", "DPWH / OSM National Road Layer", "Looker Studio GIDA Database", "Geographic distance to nearest paved all-weather transport route."),
        ("GIDA Criteria", "Hazard Vulnerability", "10% (of GIDA)", "MGB / NOAH / PAGASA", "Looker Studio GIDA Database", "Exposure index to typhoons, storm surge, and landslides."),
        ("GIDA Criteria", "Insurgency & Conflict", "10% (of GIDA)", "AFP / PNP Peace & Order Index", "Looker Studio GIDA Database", "Security risk classification and historical incident counts."),
        ("Transmission Layer", "Direct Optical Backhaul (<3km)", "Routing", "Converge ICT Terrestrial Network", "Converge Nov 2024 Backbone", "Direct optical drop to Converge node for sites within 3.0km."),
        ("Transmission Layer", "Near Optical / MW (3-5km)", "Routing", "Converge ICT Feeder Routes", "Converge Nov 2024 Backbone", "Short-hop microwave or fiber corridor lateral for sites 3.0-5.0km."),
        ("Transmission Layer", "Starlink LEO Satellite (>5km)", "Routing", "SpaceX Starlink Business Specifications", "https://www.starlink.com/business", "High-throughput satellite backhaul for sites > 5km from optical nodes.")
    ]

    for r_idx, r_data in enumerate(m_rows, 2):
        for c_idx, val in enumerate(r_data, 1):
            cell = ws_m_map.cell(r_idx, c_idx, val)
            cell.font = font_data
            cell.border = border_thin
            if c_idx in [1, 2]: cell.font = font_bold

    for c_idx in range(1, 7):
        ws_m_map.column_dimensions[get_column_letter(c_idx)].width = 22
    ws_m_map.column_dimensions['E'].width = 35
    ws_m_map.column_dimensions['F'].width = 45

    wb_map.save(map_xlsx_path)
    wb_map.close()

    map_csv_path = os.path.join(OUT_DIR, "FWA_Metric_to_Source_Mapping_Combined.csv")
    with open(map_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(m_headers)
        writer.writerows(m_rows)
    print(f"  -> Generated Metric-to-Source Mapping: {map_xlsx_path} & {map_csv_path}")

    # 4. Executive Summary Markdown
    md_path = os.path.join(OUT_DIR, "FWA_Barangay_Rollout_Executive_Summary_Combined.md")
    tot_pop = sum(x[1] for x in b_stats)
    tot_hh = sum(x[2] for x in b_stats)
    tot_subs = sum(x[3] for x in b_stats)
    tot_peak = sum(x[5] for x in b_stats)
    tot_fiber = sum(x[9]+x[10] for x in b_stats)
    tot_starlink = sum(x[11] for x in b_stats)

    md_content = f"""# Philippine 5G FWA Barangay Rollout Plan — Executive Summary
## Model 3: Hybrid Combined Model (50% Commercial / 50% GIDA Social Impact)

### 1. Strategic Mandate & Framework
Model 3 establishes an **optimized hybrid rollout plan for 5,000 barangays** across the Philippines, synthesizing:
1. **Commercial Viability Model (POPCEN 2024 Baseline)**: Evaluates fiber proximity, commercial revenue potential, and necessity.
2. **DICT / UNDP GIDA Prioritization Model**: Evaluates multi-criteria vulnerability, broadband deprivation, and isolation.

By uniting both frameworks under a **50% Commercial / 50% GIDA Social Impact dual optimization**, Model 3 delivers the highest return on investment while fulfilling national universal service and digital inclusion mandates.

---

### 2. Key Rollout Metrics & Phasing Overview

| Metric | Batch 1 (First 1,000) | Batches 1 to 5 (Total 5,000 Sites) | Methodological Rationale |
| :--- | :--- | :--- | :--- |
| **Total Sited Barangays** | **1,000** | **5,000** | Phased national deployment |
| **2024 Population Reach** | **{b_stats[0][1]:,}** | **{tot_pop:,}** | Scaled to PSA 2024 POPCEN (Proc. 973) |
| **Estimated Households** | **{b_stats[0][2]:,}** | **{tot_hh:,}** | Based on 2024 Provincial HH size matrix |
| **Target Subscribers (30%)** | **{b_stats[0][3]:,}** | **{tot_subs:,}** | 30% commercial take-up rate |
| **Day 1 BTS Deployed** | **1,000** | **5,000** | 1 BTS per barangay for immediate service |
| **Peak BTS Required** | **{b_stats[0][5]:,}** | **{tot_peak:,}** | Dimensioned @ 1,000 subs/BTS (~333/sector) |
| **Average Combined Score** | **{b_stats[0][6]:.2f} / 100** | **{sum(x[6] for x in b_stats)/5:.2f} / 100** | 50% Commercial + 50% GIDA |
| **Average Commercial Score** | **{b_stats[0][7]:.2f} / 100** | **{sum(x[7] for x in b_stats)/5:.2f} / 100** | POPCEN 2024 Siting Engine |
| **Average Normalized GIDA** | **{b_stats[0][8]:.2f} / 100** | **{sum(x[8] for x in b_stats)/5:.2f} / 100** | DICT / UNDP Prioritization Tool |
| **Direct Optical (<3km)** | **{b_stats[0][9]:,} ({b_stats[0][9]/10:.1f}%)** | **{sum(x[9] for x in b_stats):,} ({sum(x[9] for x in b_stats)/50:.1f}%)** | Direct fiber drop to Converge nodes |
| **Near Optical / MW (3-5km)**| **{b_stats[0][10]:,} ({b_stats[0][10]/10:.1f}%)** | **{sum(x[10] for x in b_stats):,} ({sum(x[10] for x in b_stats)/50:.1f}%)** | Short-hop microwave or fiber corridor |
| **Starlink LEO Satellite (>5km)**| **{b_stats[0][11]:,} ({b_stats[0][11]/10:.1f}%)** | **{tot_starlink:,} ({tot_starlink/50:.1f}%)** | High-throughput remote satellite backhaul |

---

### 3. Siting Phasing Breakdown

| Phase | Sites | 2024 Population | 2024 Households | Target Subs (30%) | Day 1 BTS | Peak BTS | Combined Score | Commercial Score | GIDA Norm Score | Direct Fiber (<3km) | Near Fiber (3-5km) | Starlink LEO (>5km) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Batch 1** | 1,000 | {b_stats[0][1]:,} | {b_stats[0][2]:,} | {b_stats[0][3]:,} | 1,000 | {b_stats[0][5]:,} | {b_stats[0][6]:.2f} | {b_stats[0][7]:.2f} | {b_stats[0][8]:.2f} | {b_stats[0][9]:,} | {b_stats[0][10]:,} | {b_stats[0][11]:,} |
| **Batch 2** | 1,000 | {b_stats[1][1]:,} | {b_stats[1][2]:,} | {b_stats[1][3]:,} | 1,000 | {b_stats[1][5]:,} | {b_stats[1][6]:.2f} | {b_stats[1][7]:.2f} | {b_stats[1][8]:.2f} | {b_stats[1][9]:,} | {b_stats[1][10]:,} | {b_stats[1][11]:,} |
| **Batch 3** | 1,000 | {b_stats[2][1]:,} | {b_stats[2][2]:,} | {b_stats[2][3]:,} | 1,000 | {b_stats[2][5]:,} | {b_stats[2][6]:.2f} | {b_stats[2][7]:.2f} | {b_stats[2][8]:.2f} | {b_stats[2][9]:,} | {b_stats[2][10]:,} | {b_stats[2][11]:,} |
| **Batch 4** | 1,000 | {b_stats[3][1]:,} | {b_stats[3][2]:,} | {b_stats[3][3]:,} | 1,000 | {b_stats[3][5]:,} | {b_stats[3][6]:.2f} | {b_stats[3][7]:.2f} | {b_stats[3][8]:.2f} | {b_stats[3][9]:,} | {b_stats[3][10]:,} | {b_stats[3][11]:,} |
| **Batch 5** | 1,000 | {b_stats[4][1]:,} | {b_stats[4][2]:,} | {b_stats[4][3]:,} | 1,000 | {b_stats[4][5]:,} | {b_stats[4][6]:.2f} | {b_stats[4][7]:.2f} | {b_stats[4][8]:.2f} | {b_stats[4][9]:,} | {b_stats[4][10]:,} | {b_stats[4][11]:,} |
| **Total** | **5,000** | **{tot_pop:,}** | **{tot_hh:,}** | **{tot_subs:,}** | **5,000** | **{tot_peak:,}** | **{sum(x[6] for x in b_stats)/5:.2f}** | **{sum(x[7] for x in b_stats)/5:.2f}** | **{sum(x[8] for x in b_stats)/5:.2f}** | **{sum(x[9] for x in b_stats):,}** | **{sum(x[10] for x in b_stats):,}** | **{tot_starlink:,}** |

---

### 4. Strategic Benefits of the Combined Approach
1. **Accelerated Cash Generation with Low Capex**:
   - Batch 1 captures **{b_stats[0][9]:,} sites within 3km of Converge optical fiber**, allowing 48-hour turn-up with minimal spur cabling.
2. **Elevated Social Impact**:
   - The average GIDA score in Batch 1 reaches **{b_stats[0][8]:.2f} / 100**, ensuring high priority is given to underserved and isolated communities.
3. **Resilient Transmission Architecture**:
   - {sum(x[9]+x[10] for x in b_stats):,} sites ({sum(x[9]+x[10] for x in b_stats)/50:.1f}%) are within 5km of Converge fiber.
   - {tot_starlink:,} remote sites ({tot_starlink/50:.1f}%) leverage Starlink Business LEO Satellite terminals.

---

### 5. Official Deliverables in `Combined/` Folder
- **Standard Excel**: `Combined/FWA_Barangay_Rollout_Plan_Combined_1000s.xlsx` (8 reconciled tabs)
- **Dynamic Excel**: `Combined/FWA_Barangay_Rollout_Plan_Combined_1000s_Dynamic.xlsx` (Live parameter sensitivity formulas)
- **Metric Mapping**: `Combined/FWA_Metric_to_Source_Mapping_Combined.xlsx` & `.csv`
- **GIS Mapping**: `Combined/FWA_Rollout_Sites_Combined.kmz`
- **Presentation Deck**: `Combined/FWA_5G_Barangay_Rollout_Presentation_Combined.html`
"""

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"  -> Generated Executive Summary Markdown: {md_path}")

    # 5. HTML Presentation
    html_path = os.path.join(OUT_DIR, "FWA_5G_Barangay_Rollout_Presentation_Combined.html")
    with open("POPCEN2024/FWA_5G_Barangay_Rollout_Presentation_2024.html", "r", encoding="utf-8") as f:
        p_template = f.read()

    p_comb = p_template.replace("2024 POPCEN & PSA FIES", "Hybrid Dual Optimization (POPCEN 2024 + GIDA)")
    p_comb = p_comb.replace("Commercial Viability Model", "Combined Hybrid Model")
    p_comb = p_comb.replace("fwa_sites_data_2024.js", "fwa_sites_data_combined.js")
    p_comb = p_comb.replace("FWA_Rollout_Sites_Master_2024.kmz", "FWA_Rollout_Sites_Combined.kmz")
    p_comb = p_comb.replace("FWA_Barangay_Rollout_Plan_2024_1000s.xlsx", "FWA_Barangay_Rollout_Plan_Combined_1000s.xlsx")
    p_comb = p_comb.replace("FWA_Barangay_Rollout_Plan_2024_1000s_Dynamic.xlsx", "FWA_Barangay_Rollout_Plan_Combined_1000s_Dynamic.xlsx")
    p_comb = p_comb.replace("fwaSitesData2024", "fwaSitesDataCombined")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(p_comb)
    print(f"  -> Generated HTML Presentation: {html_path}")

    print("\n" + "=" * 80)
    print(f"  COMBINED ROLLOUT MODEL SUCCESSFULLY GENERATED IN {time.time() - t_start:.2f} SECONDS!")
    print("=" * 80)

if __name__ == '__main__':
    run()
