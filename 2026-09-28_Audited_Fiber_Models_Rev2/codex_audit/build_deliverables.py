from pathlib import Path
import json,html,zipfile,io,csv,collections,hashlib
import xml.etree.ElementTree as E
from PIL import Image,ImageDraw,ImageFont
P=Path(__file__).resolve().parent
R=json.loads((P/'results.json').read_text());S=json.loads((P/'summary.json').read_text());F=json.loads((P/'classified_features.json').read_text());byid={f['id']:f for f in F}
colors={'A':'#16804A','B':'#2076B5','C':'#C58A0C','D':'#DD7130','E':'#C63737','F':'#73358C'}
classdefs={'A':'Node ≤0.5 km','B':'Node >0.5–1 km','C':'Line ≤0.5 km; node >1 km','D':'Other node or line ≤3 km','E':'Nearest node or line >3–5 km','F':'Both node and line >5 km'}
def esc(v):return html.escape(str(v))
def table(headers,rows):return '<table><thead><tr>'+''.join(f'<th>{esc(h)}</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{esc(v)}</td>' for v in row)+'</tr>' for row in rows)+'</tbody></table>'
phase_rows=[]
for x in S['phase']:
    c=x['class_counts'];phase_rows.append([x['phase'],c.get('A',0)+c.get('B',0),c.get('C',0),c.get('D',0),c.get('E',0),c.get('F',0),f"{x['node_mean']:.2f}"])
phase_rows.append(['Total',1972,1153,1790,48,37,f"{S['stats']['Screened node km']['mean']:.2f}"])
examples=[next(r for r in R if r['Overall rank']==rank) for rank in [1356,57,388,465,538,177]]
example_rows=[[x['Overall rank'],f"{x['Barangay']}, {x['Municipality']}",f"{x['Workbook node km']:.2f}",f"{x['Screened node km']:.2f}",f"{x['Screened line km']:.2f}",x['Nearest raw point'],x['Screening class'][0]] for x in examples]
bars=''.join('<div class="phase"><strong>Phase '+str(x['phase'])+'</strong><div class="bar">'+''.join(f'<span title="{k}: {x["class_counts"].get(k,0)}" style="width:{x["class_counts"].get(k,0)/10}%;background:{color}">{x["class_counts"].get(k,0) if x["class_counts"].get(k,0)>=40 else ""}</span>' for k,color in colors.items())+'</div></div>' for x in S['phase'])
legend=''.join(f'<span><i style="background:{color}"></i>{k}: {esc(classdefs[k])}</span>' for k,color in colors.items())
body=f'''<p class="eyebrow">FWA BARANGAY ROLLOUT · FIBER DEPLOYMENT REVIEW</p>
<h1>Prioritize short node connections, then verify line-tap opportunities.</h1>
<p class="lead">The original plan broadly favors fiber proximity, but its “active node” count includes non-node markers and its route inventory includes unfinished and non-fiber infrastructure. The corrected screening identifies <b>1,972 sites within 1 km of a node-folder candidate</b> and <b>1,153 additional sites within 500 m of a screened line</b>.</p>
<p class="notice">These are geometric survey candidates against the <b>November 2024</b> KMZ. Neither the workbook nor the map establishes current fiber availability, spare capacity, approved splice access, or BTS construction readiness.</p>
<h2>1. Phase-by-phase deployment assessment</h2>
<p>Each phase retains its original 1,000 sites. The categories below are mutually exclusive, applied A through F. They are analyst screening bands, not operator deployment standards.</p>
<div class="legend">{legend}</div>{bars}
{table(['Phase','Node ≤1 km (A+B)','Line ≤0.5 km only (C)','Other asset ≤3 km (D)','3–5 km (E)','Both >5 km (F)','Mean node km'],phase_rows)}
<p><b>Phase 1 remains the strongest short-node cohort:</b> 824 sites are within 1 km of a node candidate, compared with 197 in Phase 5. Later phases contain more opportunities to connect to a nearby line, which need a closure/splice survey. Overall, 4,915 sites (98.3%) are within 3 km of either screened asset. The remaining 85 comprise 48 at 3–5 km and 37 beyond 5 km.</p>
<h2>2. What validates, and what does not</h2>
<ul>
<li><b>Node arithmetic reproduces, but asset meaning does not.</b> All 5,000 stored node distances reproduce within 11 m using all 2,405 KMZ points. Only 1,296 point records are in node folders (1,287 unique coordinates). The other 1,109 include poles, loops, handholes, proposed COs and other markers. 149 sites matched one of these other points; 88 have a screened node more than 0.5 km farther away. Fifty-three move from a reported node distance ≤1 km to >1 km, and 38 move from ≤3 km to >3 km.</li>
<li><b>The Phase 1 “all within 3 km” claim needs correction.</b> Ten Phase 1 sites have no node-folder candidate within 3 km. Eight still have a screened route within 3 km. Culasi, City of Roxas, and Nailon, City of Bogo, are farther than 3 km from both screened asset types.</li>
<li><b>Line-vertex distances are only partly reproducible.</b> 2,641 of 5,000 match a full nearest-vertex Haversine search within 11 m. The other 2,359 are larger than the recalculated values; 760 differ by more than 100 m. The precise source computation or vertex subset is not provided, so its cause cannot be established. Separately, using vertices instead of continuous segments overstates proximity distance by more than 100 m at 273 sites and by more than 500 m at 45 sites.</li>
<li><b>The raw line layer is unsuitable as an availability layer.</b> The nearest raw line for 834 sites falls into an excluded category. After screening, line distance is more than 500 m above the workbook figure at 314 sites. Some excluded geometry is civil works with no established cable, planned/ongoing work, CCTV infrastructure or a submarine-folder feature.</li>
<li><b>The deployment score is not fully auditable.</b> All workbook results are stored values. The documented node-decay plus fiber-bonus component reproduces 4,870 scores within 0.3 point, without an assumed power factor. Of the other 130, 123 are fixed at 25 and five at 15; the remaining two have rounded 2.00 km line distances, where an unrounded value could change the bonus. The source has no site-level power, tower or active-service inputs to verify the additional claims or residual scores.</li>
</ul>
<h2>3. Examples requiring engineering review</h2>
{table(['Rank','Barangay / municipality','Old node km','Screened node km','Screened line km','Original nearest point','Class'],example_rows)}
<p>Tampoong’s original match is explicitly named “SOGOD Proposed CO”; the nearest node-folder candidate is MSL001 in Maasin. A line alternative may still be feasible, but the original 0.45 km figure does not establish a nearby active node. Digumased illustrates a different issue: a nearby mapped node remains a candidate, while the excluded planned/ongoing route cannot be assumed available.</p>
<h2>4. How I would use this for rollout decisions</h2>
<ol>
<li><b>Survey A/B sites first for short node laterals.</b> Start with the 919 sites within 500 m, followed by 1,053 at 0.5–1 km. Ask the network team to confirm handoff location, active transport, spare strands/ports, service capacity and a feasible land route. “Within 1 km” is not proof of co-location.</li>
<li><b>Run a separate line-tap workstream for Class C.</b> These 1,153 sites have a route within 500 m but no node within 1 km. Locate an approved closure or handhole, verify access and capacity, and design a splice/branch. The nearest arbitrary point on a cable is not necessarily a connection point.</li>
<li><b>Design route options for Class D.</b> For 1,790 sites, compare an actual node lateral with an approved line tap. Measure the feasible path and crossings before estimating civil works. Use the original demand and commercial ranking to choose among equally feasible fiber options.</li>
<li><b>Review E/F before committing deployment dates.</b> For 85 sites, examine an alternative BTS location, updated fiber inventory or another backhaul design. Do not infer construction cost or delivery time from straight-line distance alone.</li>
</ol>
<p>The workbook includes a <b>fiber survey priority</b> across all 5,000 sites: class A–F, then relevant distance, then target subscribers as a tie-break. This is a fiber-only survey queue. Original rollout phase and overall rank remain intact; it does not replace radio coverage, demand, economics or land/power decisions.</p>
<h2>5. Asset evidence and sensitivity</h2>
{table(['Line interpretation','Placemark count'],list(S['line_categories'].items()))}
<p>The main route search includes 459 stronger-evidence lines, 2,218 status-unverified mapped lines and seven acceptance-pending lines. “Stronger evidence” means a built/existing/as-built label survived exclusions, not verified operational service. The nearest retained line is conditional for 2,250 sites.</p>
{table(['Phase','Within 3 km: node or screened route','Within 3 km: node or stronger-evidence route'],[[x['phase'],x['either_3km'],x['strong_either_3km']] for x in S['phase']])}
<p>Restricting routes to stronger evidence lowers the combined ≤3 km count from 4,915 to {sum(x['strong_either_3km'] for x in S['phase']):,}. Node candidates are unchanged in this sensitivity, so it still does not establish current availability. Submarine-folder features and dedicated CCTV lines are conservatively excluded from the local BTS access screen; any usable terrestrial tails or spare CCTV fiber require explicit review.</p>
<h2>6. Reproducible method and limits</h2>
<p>Inputs were read from the four Batch worksheets (5,000 unique PSGC codes) and all 6,806 point/line Placemarks in the supplied KMZ. The combined Batch 4 &amp; 5 sheet was split by overall rank. All supplied site coordinates were retained. The KMZ’s missing mwm namespace declaration was repaired only in a parsing copy.</p>
<p>To reproduce the original arithmetic, I used Haversine distances with a 6,371 km radius. For the independent results, I used <a href="https://pyproj4.github.io/pyproj/3.6.1/api/geod.html">WGS84 ellipsoidal geodesic calculations</a>, exhaustively checking eligible point candidates and minimizing distance along line segments. Line segments were subdivided to ≤500 m for conservative spatial indexing. Every result passed coordinate, asset-eligibility and nested-distance checks; 30 separate scalar-minimization checks agreed within 0.02 m on the selected routes. Computational agreement is not a statement about source-coordinate accuracy.</p>
<p>Asset classification uses names, folder paths and descriptions. Specific installed/completed labels can override inherited proposed/ongoing folder names; explicit no-cable/not-built evidence prevails. Every original feature’s text is preserved in the asset register for review. No network status was inferred from line color or visibility.</p>
<p><b>Not measured:</b> current status since November 2024; usable capacity; engineering permissions; island/river/road barriers; terrain; surveyed BTS location; feasible cable route; pole/duct condition; land, tower, power and radio coverage. The workbook labels coordinates as barangay reference points; this review does not independently verify them. Straight-line surface distances are screening lower bounds. Route planning and installation require physical infrastructure and crossing assessment, consistent with <a href="https://www.itu.int/rec/dologin_pub.asp?id=T-REC-L.163-201811-I!!PDF-E&amp;lang=e&amp;type=items">ITU-T L.163</a>.</p>
<h2>Files and source traceability</h2>
<ul><li><b>FWA_Fiber_Deployment_Validation.xlsx:</b> summary, all site results, complete KMZ asset register, and method. Filter by phase, class, flags or survey priority.</li><li><b>FWA_Validated_Fiber_Deployment.kmz:</b> separate phase folders with A–F subfolders. Pin number is the phase; pin color is screening class. Selected screened routes and node candidates are optional layers. Hidden connectors show straight-line proximity, not designed construction routes.</li><li><b>FWA_All_5000_Site_Validation.csv:</b> portable per-site results.</li></ul>
<p class="sources">Sources: FWA_Barangay_Rollout_Plan_2024_1000s_Rev1_Sep25_HT.xlsx (Batch sheets, Read Me, Methodology &amp; Assumptions, Executive Summary); NATIONAL &amp; REGIONAL BACKBONE_NOV 2024_REPORT.kmz. Original source files were not modified.</p>'''
css='''body{font:16px/1.6 Arial,sans-serif;color:#243448;margin:40px auto;max-width:1180px;padding:0 28px;background:#fff}h1{font-size:36px;line-height:1.2;max-width:1000px}h2{margin-top:42px;font-size:23px}p,li{max-width:1100px}.eyebrow{font-size:12px;letter-spacing:1.8px;color:#527083}.lead{font-size:19px}.notice{padding:16px 20px;background:#fff4d9;border-left:4px solid #c58a0c}table{border-collapse:collapse;width:100%;font-size:14px;margin:20px 0}th{text-align:left;background:#243e56;color:white;padding:10px}td{padding:10px;border-bottom:1px solid #dde4ea;vertical-align:top}tbody tr:nth-child(even){background:#f4f7fa}.phase{display:flex;gap:18px;align-items:center;margin:12px 0}.phase strong{min-width:70px}.bar{height:34px;display:flex;flex:1}.bar span{color:white;text-align:center;font-size:13px;line-height:34px;overflow:hidden}.legend{display:flex;flex-wrap:wrap;gap:10px 22px;font-size:13px}.legend span{display:flex;align-items:center;gap:7px}.legend i{width:12px;height:12px;display:inline-block}.sources{font-size:13px;color:#596977}a{color:#166fa2}li{margin:10px 0}@media print{body{margin:0;max-width:none;padding:0;font-size:11px}h1{font-size:25px}h2{font-size:17px}table{font-size:10px}tr{break-inside:avoid}h2{break-after:avoid}.bar{-webkit-print-color-adjust:exact;print-color-adjust:exact}}'''
(P/'FWA_Fiber_Deployment_Analysis.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>FWA fiber deployment analysis</title><style>'+css+'</style><body>'+body+'</body></html>')

NS='http://www.opengis.net/kml/2.2';E.register_namespace('',NS)
def el(p,t,v=None,**attrs):
    e=E.SubElement(p,'{'+NS+'}'+t,attrs)
    if v is not None:e.text=str(v)
    return e
root=E.Element('{'+NS+'}kml');doc=el(root,'Document');el(doc,'name','FWA — validated fiber deployment screening')
el(doc,'description','November 2024 backbone snapshot. Numbers identify original phases. Colors identify screening classes A–F. All fiber availability is unverified. Connectors are straight-line distances, not planned cable routes. See accompanying analysis and workbook.')
icons={};font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',60)
for phase in range(1,6):
    for c,color in colors.items():
        im=Image.new('RGBA',(128,160));d=ImageDraw.Draw(im);d.polygon([(20,75),(108,75),(64,156)],fill=color,outline='white',width=5);d.ellipse((7,3,121,117),fill=color,outline='white',width=5);d.text((64,59),str(phase),font=font,fill='white',anchor='mm');im=im.resize((64,80),Image.Resampling.LANCZOS);b=io.BytesIO();im.save(b,format='PNG');key=f'icons/{phase}{c}.png';icons[key]=b.getvalue()
        st=el(doc,'Style',id=f'p{phase}{c}');i=el(st,'IconStyle');el(i,'scale',.75);el(el(i,'Icon'),'href',key);el(i,'hotSpot',x='0.5',y='0',xunits='fraction',yunits='fraction');el(el(st,'LabelStyle'),'scale',0.6)
for sid,color,width in [('route_strong','ff8c8016',2),('route_conditional','ff999999',2),('node_link','ffb57620',1),('line_link','ff308add',1)]:
    st=el(doc,'Style',id=sid);l=el(st,'LineStyle');el(l,'color',color);el(l,'width',width)
for phase in range(1,6):
    folder=el(doc,'Folder');el(folder,'name',f'Phase {phase} — 1,000 sites');el(folder,'open',0)
    for c in colors:
        sub=el(folder,'Folder');rs=[r for r in R if r['Phase']==phase and r['Screening class'][0]==c];el(sub,'name',f'{c}: {classdefs[c]} ({len(rs)})')
        for r in rs:
            pm=el(sub,'Placemark');el(pm,'name',f"{c} | {r['Overall rank']:04d} | {r['Barangay']}, {r['Municipality']}");el(pm,'styleUrl',f'#p{phase}{c}')
            fields={k:r[k] for k in ['Phase','PSGC code','Province','Screening class','Screened node km','Screened line km','Nearest node','Nearest node ID','Nearest line','Nearest line ID','Line evidence','Workbook node km','Workbook line-vertex km','Fiber survey priority','Recommended action','Review flags']}
            fields={k:round(v,3) if isinstance(v,float) else v for k,v in fields.items()}
            el(pm,'description',table(['Field','Value'],list(fields.items()))+'<p>Availability unverified; straight-line screening distance only.</p>');pt=el(pm,'Point');el(pt,'coordinates',f"{r['Longitude']},{r['Latitude']},0")
layer=el(doc,'Folder');el(layer,'name','Nearest screened fiber routes — optional');el(layer,'visibility',0)
for fid in sorted({r['Nearest line ID'] for r in R}):
    f=byid[fid];pm=el(layer,'Placemark');el(pm,'name',f"{fid}: {f['name']}");el(pm,'visibility',0);el(pm,'styleUrl','#route_strong' if f['line_category'].startswith('Stronger') else '#route_conditional');el(pm,'description',table(['Field','Value'],[(k,f[k]) for k in ['line_category','path','description']]))
    mg=el(pm,'MultiGeometry')
    for line in f['lines']:
        ls=el(mg,'LineString');el(ls,'tessellate',1);el(ls,'coordinates',' '.join(f'{a},{b},0' for a,b in line))
layer=el(doc,'Folder');el(layer,'name','Nearest node candidates — optional');el(layer,'visibility',0)
for fid in sorted({r['Nearest node ID'] for r in R}):
    f=byid[fid];pm=el(layer,'Placemark');el(pm,'name',f['name']);el(pm,'visibility',0);el(pm,'description',f"Node-folder candidate; service/capacity unverified. Feature ID {fid}. {f['path']}")
    pt=el(pm,'Point');p=f['points'][0][0];el(pt,'coordinates',f'{p[0]},{p[1]},0')
for kind in ['node','line']:
    folder=el(doc,'Folder');el(folder,'name',f'Straight-line connectors to nearest {kind} — NOT build routes');el(folder,'visibility',0)
    for phase in range(1,6):
        sub=el(folder,'Folder');el(sub,'name',f'Phase {phase}');el(sub,'visibility',0)
        for r in R:
            if r['Phase']!=phase:continue
            pm=el(sub,'Placemark');el(pm,'visibility',0);el(pm,'name',f"{r['Overall rank']}: {r['Barangay']}");el(pm,'styleUrl',f'#{kind}_link');ls=el(pm,'LineString');el(ls,'tessellate',1)
            x,y=(r['Node longitude'],r['Node latitude']) if kind=='node' else (r['Line nearest longitude'],r['Line nearest latitude'])
            el(ls,'coordinates',f"{r['Longitude']},{r['Latitude']},0 {x},{y},0")
with zipfile.ZipFile(P/'FWA_Validated_Fiber_Deployment.kmz','w',zipfile.ZIP_DEFLATED) as z:
    z.writestr('doc.kml',E.tostring(root,encoding='utf-8',xml_declaration=True))
    for name,data in icons.items():z.writestr(name,data)
with zipfile.ZipFile(P/'FWA_Validated_Fiber_Deployment.kmz') as z:
    assert z.testzip() is None
    r=E.fromstring(z.read('doc.kml'));ns={'k':NS}
    main=r.find('k:Document',ns).findall('k:Folder',ns)[:5]
    assert [len(x.findall('.//k:Point',ns)) for x in main]==[1000]*5
    for e in r.findall('.//k:href',ns):assert e.text in z.namelist()
print('Report and KMZ created; five phase folders × 1,000 sites verified.')
