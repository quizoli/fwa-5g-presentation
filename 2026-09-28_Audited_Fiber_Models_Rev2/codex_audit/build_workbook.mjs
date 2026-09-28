import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const out=path.dirname(fileURLToPath(import.meta.url));
const rows=JSON.parse(await fs.readFile(path.join(out,'results.json'),'utf8'));
const stats=JSON.parse(await fs.readFile(path.join(out,'summary.json'),'utf8'));
const assets=JSON.parse(await fs.readFile(path.join(out,'classified_features.json'),'utf8'));
const wb=Workbook.create();
const summary=wb.worksheets.add('Summary'),sites=wb.worksheets.add('Site analysis'),registry=wb.worksheets.add('KMZ asset register'),method=wb.worksheets.add('Method and sources');
const colors={A:'#DDEEDD',B:'#E1EDF8',C:'#FFF0CE',D:'#F8E4D7',E:'#F4D7D7',F:'#E9DCEA'};
function col(i){let s='';for(i++;i;i=Math.floor((i-1)/26))s=String.fromCharCode(65+(i-1)%26)+s;return s;}
function table(sh,headers,data,start=4,name='Data'){
 const end=start+data.length,last=col(headers.length-1);
 sh.getRange(`A${start}:${last}${end}`).values=[headers,...data];
 const r=sh.getRange(`A${start}:${last}${end}`);r.format.font={name:'Arial',size:10};r.format.rowHeight=30;r.format.verticalAlignment='center';
 sh.getRange(`A${start}:${last}${start}`).format={fill:'#243E56',font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:48};
 sh.tables.add(`A${start}:${last}${end}`,true,name);
 sh.freezePanes.freezeRows(start);sh.freezePanes.freezeColumns(3);
 sh.getRange(`A1:${last}${end}`).format.columnWidth=18;
 return end;
}
for(const sh of [summary,sites,registry,method]){sh.showGridLines=false;sh.getRange('A2').format.font={name:'Arial',size:15,bold:true};}
const main=['Overall rank','Phase','PSGC code','Barangay','Municipality','Province','Screening class','Screened node km','Screened line km','Nearest screened asset km','Workbook node km','Node change km','Workbook line-vertex km','Line change km','Nearest node','Nearest line','Line evidence','Recommended action','Fiber survey priority'];
const headers=[...main,...Object.keys(rows[0]).filter(k=>!main.includes(k))];
sites.getRange('A2').values=[['All 5,000 sites: fiber proximity and deployment screening']];
const last=table(sites,headers,rows.map(r=>headers.map(h=>r[h])),4,'SiteAnalysis');
for(let i=0;i<headers.length;i++){
 const h=headers[i],c=col(i),range=sites.getRange(`${c}5:${c}${last}`);
 if(/km$/.test(h))range.setNumberFormat('0.000');
 else if(/latitude|longitude/i.test(h))range.setNumberFormat('0.000000');
 else if(/score|composite/i.test(h))range.setNumberFormat('0.0');
 if(/PSGC/.test(h))range.setNumberFormat('0000000000');
 if(['Barangay','Municipality','Province'].includes(h))sites.getRange(`${c}4:${c}${last}`).format.columnWidth=25;
 if(['Nearest node','Nearest line','Line evidence','Screening class'].includes(h)){sites.getRange(`${c}4:${c}${last}`).format.columnWidth=40;range.format.wrapText=true;}
 if(['Recommended action','Review flags'].includes(h)){sites.getRange(`${c}4:${c}${last}`).format.columnWidth=70;range.format.wrapText=true;}
}
sites.getRange(`A5:${col(headers.length-1)}${last}`).format.rowHeight=60;
sites.getRange(`G5:G${last}`).conditionalFormats.add('beginsWith',{text:'A',format:{fill:colors.A}});
for(const k of ['B','C','D','E','F'])sites.getRange(`G5:G${last}`).conditionalFormats.add('beginsWith',{text:k,format:{fill:colors[k]}});
const ar=assets.map(a=>[a.id,a.points.length?'Point':'Line',a.name,a.points.length?(a.node_candidate?'Node-folder candidate':'Other point; not counted as node'):a.line_category,a.path,a.description]);
registry.getRange('A2').values=[['Source KMZ features and classification evidence']];
table(registry,['Feature ID','Geometry','Feature name','Screening interpretation','KMZ folder path','Source description'],ar,4,'AssetRegister');
registry.getRange(`C4:D${ar.length+4}`).format.columnWidth=43;
registry.getRange(`E4:F${ar.length+4}`).format.columnWidth=85;
registry.getRange(`C5:F${ar.length+4}`).format.wrapText=true;
registry.getRange(`A5:F${ar.length+4}`).format.rowHeight=100;
summary.getRange('A2').values=[['FWA deployment: fiber proximity review']];
summary.getRange('A4').values=[['5,000 sites assessed against the November 2024 backbone snapshot.']];
summary.getRange('A5').values=[['Proximity identifies survey candidates; operational availability and routed build length remain unverified.']];
summary.getRange('A7:H7').values=[['Phase','Sites','Node ≤1 km','Other line ≤0.5 km','Other asset ≤3 km','Nearest 3–5 km','Both >5 km','Mean node km']];
summary.getRange('A7:H7').format={fill:'#243E56',font:{bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:42};
for(let p=1;p<=5;p++){
 const n=p+7;summary.getRange(`A${n}`).values=[[p]];
 summary.getRange(`B${n}:H${n}`).formulas=[[
 `=COUNTIFS('Site analysis'!$B$5:$B$5004,A${n})`,
 `=COUNTIFS('Site analysis'!$B$5:$B$5004,A${n},'Site analysis'!$H$5:$H$5004,"<=1")`,
 `=COUNTIFS('Site analysis'!$B$5:$B$5004,A${n},'Site analysis'!$G$5:$G$5004,"C - Line within 0.5 km; node over 1 km")`,
 `=COUNTIFS('Site analysis'!$B$5:$B$5004,A${n},'Site analysis'!$G$5:$G$5004,"D - Other node or line within 3 km")`,
 `=COUNTIFS('Site analysis'!$B$5:$B$5004,A${n},'Site analysis'!$G$5:$G$5004,"E - Nearest node or line 3-5 km")`,
 `=COUNTIFS('Site analysis'!$B$5:$B$5004,A${n},'Site analysis'!$G$5:$G$5004,"F - Nearest node and line over 5 km")`,
 `=AVERAGEIFS('Site analysis'!$H$5:$H$5004,'Site analysis'!$B$5:$B$5004,A${n})`]];
}
summary.getRange('A13').values=[['Total']];
summary.getRange('B13:G13').formulas=[['=SUM(B8:B12)','=SUM(C8:C12)','=SUM(D8:D12)','=SUM(E8:E12)','=SUM(F8:F12)','=SUM(G8:G12)']];
summary.getRange('H13').formulas=[["=AVERAGE('Site analysis'!H5:H5004)"]];
summary.getRange('H8:H13').setNumberFormat('0.00');
summary.getRange('A13:H13').format.font={bold:true};
const findings=[
 ['Finding','Result','Meaning'],
 ['Node distances reproduce',stats['node_reproduced_0.011km'],'All-point Haversine matches within 11 m, but the point set includes non-node markers.'],
 ['Node-folder records',stats.node_candidates,'1,287 unique coordinates; node labels do not establish active service or spare capacity.'],
 ['Sites matched to non-node points',stats.raw_point_not_node,'149 sites matched poles, handholes, proposed COs or other points outside node folders.'],
 ['Line-vertex distances not reproduced',5000-stats['vertex_reproduced_0.011km'],'2,359 differ by more than 11 m; 760 differ by more than 100 m.'],
 ['Nearest raw line excluded',stats.excluded_nearest_line,'Exclusions include civil works, no cable, ongoing works, CCTV and submarine folders.'],
 ['Either screened asset within 3 km',stats.either_under_3km,'4,915 geometric candidates; this does not certify fiber access.'],
 ['Nearest screened line status unverified',stats.conditional_line_winners,'2,250 nearest-route matches need status or acceptance confirmation.'],
 ['Phase 1 nodes farther than 3 km',stats.phase1_node_over_3km,'The workbook states all Phase 1 sites are within 3 km of a node.'],
];
summary.getRange('A16:C24').values=findings;
summary.getRange('A16:C16').format={fill:'#243E56',font:{bold:true,color:'#FFFFFF'}};
summary.getRange('C16:H16').merge();summary.getRange('C16:H16').format.fill='#243E56';
for(let i=17;i<=24;i++){summary.getRange(`A${i}`).format.wrapText=true;summary.getRange(`C${i}:H${i}`).merge();summary.getRange(`C${i}`).format.wrapText=true;}
summary.getRange('A17:H24').format.rowHeight=45;
summary.getRange('A1:H24').format.font.name='Arial';summary.getRange('A1:H24').format.columnWidth=18;
summary.getRange('A7:A24').format.columnWidth=31;
summary.getRange('A4:H5').format.font={name:'Arial',size:10,italic:true};
summary.getRange('A8:H13').format.rowHeight=26;
const notes=[
 ['Scope','All 5,000 workbook barangay coordinates; original phase and overall rank retained. Coordinates are treated as supplied barangay reference points, not surveyed BTS locations.'],
 ['Workbook source','FWA_Barangay_Rollout_Plan_2024_1000s_Rev1_Sep25_HT.xlsx; Batch sheets row 5 onward. S/T hold distances; U/V hold deployment tier/score.'],
 ['Backbone source','NATIONAL & REGIONAL BACKBONE_NOV 2024_REPORT.kmz; November 2024 snapshot. Feature IDs are zero-based original Placemark order. Full paths and descriptions appear in KMZ asset register.'],
 ['Distance reproduction','Haversine with 6,371 km spherical radius against all 2,405 points and all 334,462 vertices. 11 m comparison tolerance accommodates 0.01 km source rounding and small computational differences.'],
 ['Independent distances','WGS84 ellipsoidal distances. Node search covers all 1,296 point records in node folders. Line distance is minimized along each polyline segment, not just its vertices.'],
 ['Line geometry','Segments are treated as shortest WGS84 geodesics between consecutive stored vertices and subdivided to at most 500 m. A conservative midpoint search and chord bounds screen candidates; segment minima use numerical minimization.'],
 ['Node eligibility','Only points under NODES or VISAYAS NODES folders, case-insensitive. Other points remain in the asset register. A node-folder entry is a candidate, not a claim of an active BTS handoff.'],
 ['Line exclusions','Explicit no cable / not installed / not implemented / not yet started; planned/ongoing labels; submarine folders; CCTV networks; civil works without cable evidence. Submarine folders may contain terrestrial tails, conservatively excluded pending review.'],
 ['Status precedence','Specific feature descriptions and names can supersede parent proposed/ongoing labels when explicit completion/installation evidence exists. Explicit no-cable and not-built labels override completion. Classification is a text-based screening interpretation.'],
 ['Screened route set','Stronger evidence plus conditional mapped routes and acceptance-pending routes. Conditional does not mean available. Asset classification can be reviewed using retained source text.'],
 ['Stronger route sensitivity','Uses only built/existing/as-built labels after exclusions. Such labels still do not verify current service, acceptance, commercial access or capacity. Node candidates remain unchanged.'],
 ['A / B','A: node ≤0.5 km. B: node >0.5 and ≤1 km. First survey candidates for short node laterals; distance does not prove co-location.'],
 ['C / D','C: node >1 km and screened line ≤0.5 km. D: all remaining sites with either screened asset ≤3 km. A line tap requires an approved closure, handhole or splice location.'],
 ['E / F','E: nearest screened node or line >3 and ≤5 km. F: both >5 km. These are analyst screening bands, not operator standards or construction approvals.'],
 ['Survey priority','Sort A→F, then node distance for A/B or nearest screened asset distance for C–F, then target subscribers descending. This is a fiber-only survey queue, not a replacement commercial rollout ranking.'],
 ['Deploy-score check','Documented proximity component: min(100,100×exp(−node_km/3)+10 if line_km≤2). Power factor is omitted because the workbook provides no site-level inputs. 4,870 match within 0.3 point; 128 nonmatches sit at 25 or 15 and two at a rounded 2 km boundary.'],
 ['Score interpretation','The screened proximity score reruns only that documented component. It is not a full deployment-ease score and does not include invented power, tower, cost or availability assumptions.'],
 ['What remains unknown','Current asset status; spare strands/ports; transport capacity and service design; splice authorization; routed lateral length; road/river/sea crossings; rights of way; pole/duct condition; BTS land/tower and power feasibility.'],
 ['Distance use','Straight-line surface distance is a screening lower bound, not cable length. No road routing, island-boundary restriction, terrain or crossing penalty was applied. Nearby assets may be separated by water or other barriers.'],
 ['Recalculation','This is a spatial-analysis snapshot. Changing coordinates or the backbone requires rerunning the GIS analysis. Summary formulas update from the saved site results; Excel does not recompute geospatial nearest neighbors.'],
 ['Source repair','The KMZ lacks an mwm namespace declaration. A declaration was inserted only into the in-memory parsing copy. Original source files were not changed.'],
 ['Verification','5,000 unique PSGC rows; valid coordinates; asset eligibility and nested distance checks for every row. Thirty independent scalar-minimization spot checks agree within 0.02 m on selected routes.'],
 ['Geodesic reference','https://pyproj4.github.io/pyproj/3.6.1/api/geod.html'],
 ['Installation reference','ITU-T L.163: https://www.itu.int/rec/dologin_pub.asp?id=T-REC-L.163-201811-I!!PDF-E&lang=e&type=items']
];
method.getRange('A2').values=[['Method, interpretation and sources']];table(method,['Topic','Definition'],notes,4,'MethodSources');
method.getRange(`A4:A${notes.length+4}`).format.columnWidth=31;method.getRange(`B4:B${notes.length+4}`).format.columnWidth=120;
method.getRange(`A5:B${notes.length+4}`).format.wrapText=true;method.getRange(`A5:B${notes.length+4}`).format.rowHeight=60;
wb.recalculate();
await fs.writeFile(path.join(out,'workbook_inspect.txt'),(await wb.inspect({kind:'table',range:'Summary!A7:H13',include:'values,formulas',tableMaxRows:7,tableMaxCols:8,maxChars:6000})).ndjson);
await fs.writeFile(path.join(out,'workbook_errors.txt'),(await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#NUM!|#SPILL!',options:{useRegex:true,maxResults:10},summary:'Final error scan'})).ndjson);
for(const [sheet,range,file] of [['Summary','A2:H24','summary_preview.png'],['Site analysis','A4:J10','sites_preview.png'],['KMZ asset register','A4:F7','assets_preview.png'],['Method and sources','A4:B10','method_preview.png']]){
 const p=await wb.render({sheetName:sheet,range,scale:1.4,format:'png'});await fs.writeFile(path.join(out,file),new Uint8Array(await p.arrayBuffer()));
}
await (await SpreadsheetFile.exportXlsx(wb)).save(path.join(out,'FWA_Fiber_Deployment_Validation.xlsx'));
console.log('Workbook exported');
