from pathlib import Path
import sys, json, re, csv, math, collections, hashlib
sys.path.insert(0,'/tmp/fwa_geo_deps')
import numpy as np
from scipy.spatial import cKDTree
from pyproj import Geod, Transformer
import openpyxl

OUT=Path(__file__).resolve().parent
SOURCE=Path('/Users/olivertungol/Downloads/FWA_Barangay_Rollout_Plan_2024_1000s_Rev1_Sep25_HT.xlsx')
F=json.loads((OUT/'features.json').read_text())
geod=Geod(ellps='WGS84')
ecef=Transformer.from_crs('EPSG:4979','EPSG:4978',always_xy=True)
def xyz(a):
    a=np.asarray(a); return np.array(ecef.transform(a[:,0],a[:,1],np.zeros(len(a)))).T
def unit(a):
    r=np.radians(a); return np.array([np.cos(r[:,1])*np.cos(r[:,0]),np.cos(r[:,1])*np.sin(r[:,0]),np.sin(r[:,1])]).T
def norm(s): return re.sub(r'\s+',' ',s).strip().upper()
def line_category(f):
    parts=[norm(x) for x in f['path'].split(' / ')[1:]]+[norm(f['name']),norm(f['description'])]
    text=' | '.join(parts)
    # Explicit absence of cable must override completed civil works.
    if re.search(r'NO CABLE|WITHOUT (?:FOC|CABLE)|FOR FIBER BLOWING|NOT (?:YET )?INSTALLED|NOT IMPLEMENTED|NOT YET STARTED|NO FOC',text):
        return 'Excluded - no cable or not built'
    if 'SUBMARINE' in text: return 'Excluded - submarine folder'
    if 'CCTV' in text: return 'Excluded - CCTV dedicated network'
    # Most specific status wins, allowing installed descendants of proposed folders.
    status=''
    for t in parts:
        if re.search(r'ON\s*GOING|PROPOS|PROP\.|PLANNED|ON HOLD|PENDING',t): status='planned'
        if re.search(r'COMPLETED|CABLE LAYED|CABLE LAID|FOC INSTALLED|INSTALLED.*(?:\d+C|FOC)|\d+C INSTALLED|FOC BLOWING COMPLETED|AS[- ]BUILT|EXISTING',t): status='built'
        if re.search(r'FOR PAT|FOR ACCEPTANCE|AWAITING ACCEPTANCE',t): status='acceptance'
    if status=='planned': return 'Excluded - planned or ongoing'
    if status=='acceptance': return 'Conditional - acceptance pending'
    cable=bool(re.search(r'\bFOC\b|\b\d+\s*(?:C|F|CORE|CORES)\b|CABLE (?:LAYED|LAID)|\bDWDM\b|\bOTN\b|\bMPLS\b|BACKBONE AERIAL|AERIAL BACKBONE',text))
    civil=bool(re.search(r'DUCT|CONDUIT|\bPIPE|HANDHOLE|\bHDD\b|TRENCH',text))
    if civil and not cable: return 'Excluded - civil works only or unclear cable'
    if status=='built': return 'Stronger evidence - built or existing label'
    return 'Conditional - mapped route, status unverified'
for f in F:
    f['node_candidate']=bool(re.search(r'(?:^| / )(?:NODES|VISAYAS NODES)(?: / |$)',f['path'],re.I))
    f['line_category']=line_category(f) if f['lines'] else ''

w=openpyxl.load_workbook(SOURCE,data_only=True)
rows=[]
for s in w:
    if s.title.startswith('Batch '):
        headers=[c.value for c in s[4]]
        for rn,vs in enumerate(s.iter_rows(min_row=5,values_only=True),5):
            if vs[1] is None: continue
            d=dict(zip(headers,vs)); d['Phase']=(int(d['Overall Rank'])-1)//1000+1;d['Source sheet']=s.title; d['Source row']=rn; rows.append(d)
rows.sort(key=lambda r:r['Overall Rank'])
q=np.array([[r['Longitude'],r['Latitude']] for r in rows]); qxyz=xyz(q)
assert len(rows)==5000 and len({r['PSGC Code'] for r in rows})==5000
assert np.isfinite(q).all() and ((q[:,0]>116)&(q[:,0]<127)&(q[:,1]>4)&(q[:,1]<22)).all()
points=[]; pointids=[]; vertices=[]
segments=[]; segids=[]
for f in F:
    for pts in f['points']:
        for p in pts: points.append(p); pointids.append(f['id'])
    for line in f['lines']:
        vertices.extend(line)
        for a,b in zip(line,line[1:]):
            az,_,length=geod.inv(*a,*b)
            if length<=1e-6: continue
            n=max(1,math.ceil(length/500))
            pts=[a]+[list(x) for x in geod.npts(*a,*b,n-1)] + [b] if n>1 else [a,b]
            for c,d in zip(pts,pts[1:]): segments.append([c,d]);segids.append(f['id'])
points=np.array(points); pointids=np.array(pointids); vertices=np.array(vertices)
segments=np.array(segments);segids=np.array(segids)
assert np.isfinite(points).all() and np.isfinite(vertices).all()
print('Inputs',len(rows),len(points),len(vertices),len(segments),'densified segments',flush=True)
byid={f['id']:f for f in F}
def spherical_nearest(coords):
    dist,ix=cKDTree(unit(coords)).query(unit(q))
    return 6371.0*2*np.arcsin(np.clip(dist/2,0,1)),ix
rawnode,rawni=spherical_nearest(points)
rawvertex,rawvi=spherical_nearest(vertices)
nodeidx=np.array([i for i,fid in enumerate(pointids) if byid[int(fid)]['node_candidate']])
nodes=points[nodeidx]
# Exhaustive ellipsoidal inverse against every node candidate, in chunks.
nd=[]; ni=[]
for p in q:
    _,_,ds=geod.inv(np.full(len(nodes),p[0]),np.full(len(nodes),p[1]),nodes[:,0],nodes[:,1])
    i=int(np.argmin(ds)); nd.append(ds[i]/1000);ni.append(nodeidx[i])
nd=np.array(nd);ni=np.array(ni)

# WGS84 point-to-segment distance. Midpoint index gives a conservative candidate
# set; chord lower bounds retain every potentially closer curved segment.
a=segments[:,0];b=segments[:,1]
az,_,length=geod.inv(a[:,0],a[:,1],b[:,0],b[:,1])
mlon,mlat,_=geod.fwd(a[:,0],a[:,1],az,length/2)
mxyz=xyz(np.column_stack([mlon,mlat])); ax=xyz(a);bx=xyz(b);v=bx-ax
vv=(v*v).sum(axis=1)
def line_nearest(mask,label):
    inds=np.flatnonzero(mask); tree=cKDTree(mxyz[inds]); maxhalf=float(length[inds].max()/2)
    result=[]
    for qi,p in enumerate(q):
        _,ii=tree.query(qxyz[qi]); ii=inds[ii]
        _,_,upper=geod.inv(*p,float(mlon[ii]),float(mlat[ii]))
        ids=inds[np.asarray(tree.query_ball_point(qxyz[qi],upper+maxhalf+0.05),dtype=int)]
        delta=qxyz[qi]-ax[ids]
        t=np.clip((delta*v[ids]).sum(axis=1)/vv[ids],0,1)
        chord=np.linalg.norm(delta-t[:,None]*v[ids],axis=1)
        x,y,_=geod.fwd(a[ids,0],a[ids,1],az[ids],t*length[ids])
        _,_,ds=geod.inv(np.full(len(ids),p[0]),np.full(len(ids),p[1]),x,y)
        # Sagitta at 500m < 0.005m; 0.02m buffer is conservative.
        keep=chord<=np.min(ds)+0.02
        ids=ids[keep]
        lo=np.zeros(len(ids));hi=length[ids].copy()
        px=np.full(len(ids),p[0]);py=np.full(len(ids),p[1])
        for _ in range(36):
            t1=(2*lo+hi)/3;t2=(lo+2*hi)/3
            x1,y1,_=geod.fwd(a[ids,0],a[ids,1],az[ids],t1)
            x2,y2,_=geod.fwd(a[ids,0],a[ids,1],az[ids],t2)
            d1=geod.inv(px,py,x1,y1)[2];d2=geod.inv(px,py,x2,y2)[2]
            sel=d1<d2;hi=np.where(sel,t2,hi);lo=np.where(sel,lo,t1)
        t=(lo+hi)/2
        x,y,_=geod.fwd(a[ids,0],a[ids,1],az[ids],t)
        ds=geod.inv(px,py,x,y)[2]
        da=geod.inv(px,py,a[ids,0],a[ids,1])[2];db=geod.inv(px,py,b[ids,0],b[ids,1])[2]
        sa=da<ds;ds=np.where(sa,da,ds);x=np.where(sa,a[ids,0],x);y=np.where(sa,a[ids,1],y)
        sb=db<ds;ds=np.where(sb,db,ds);x=np.where(sb,b[ids,0],x);y=np.where(sb,b[ids,1],y)
        j=int(np.argmin(ds)); seg=int(ids[j])
        result.append(dict(km=float(ds[j]/1000),feature_id=int(segids[seg]),lon=float(x[j]),lat=float(y[j])))
        if qi%1000==0: print(label,qi,flush=True)
    return result
cats=np.array([byid[int(i)]['line_category'] for i in segids])
cache=OUT/'nearest_lines.json'
if cache.exists(): lr=json.loads(cache.read_text())
else:
    lr={
        'all':line_nearest(np.ones(len(segments),dtype=bool),'all lines'),
        'screened':line_nearest(np.array([x.startswith(('Stronger','Conditional')) for x in cats]),'screened lines'),
        'strong':line_nearest(np.array([x.startswith('Stronger') for x in cats]),'stronger evidence lines')}
    cache.write_text(json.dumps(lr))

classes={
 'A':'A - Node within 0.5 km',
 'B':'B - Node 0.5-1 km',
 'C':'C - Line within 0.5 km; node over 1 km',
 'D':'D - Node or line within 1-3 km / line 0.5-3 km',
 'E':'E - Nearest node or line 3-5 km',
 'F':'F - Nearest node and line over 5 km'}
results=[]
for i,r in enumerate(rows):
    rn=byid[int(pointids[rawni[i]])];nn=byid[int(pointids[ni[i]])]
    la=lr['all'][i];ls=lr['screened'][i];lt=lr['strong'][i];lf=byid[ls['feature_id']]
    dn=float(nd[i]);dl=ls['km'];best=min(dn,dl)
    cls='A' if dn<=.5 else 'B' if dn<=1 else 'C' if dl<=.5 else 'D' if best<=3 else 'E' if best<=5 else 'F'
    oldn=float(r['Dist. to Nearest Node (km)']);oldl=float(r['Dist. to Fiber Line (km)'])
    delta_n=dn-oldn;delta_l=dl-oldl
    flags=[]
    if not rn['node_candidate']: flags.append('Original nearest point is outside node folders')
    if abs(rawnode[i]-oldn)>.011: flags.append('Node distance not reproduced within 0.011 km')
    if abs(rawvertex[i]-oldl)>.011: flags.append('Vertex distance not reproduced within 0.011 km')
    if delta_n>.5: flags.append('Screened node is >0.5 km farther')
    if dl-oldl>.5: flags.append('Screened route is >0.5 km farther')
    if rawvertex[i]-la['km']>.5: flags.append('Vertex method overstates route distance >0.5 km')
    if byid[la['feature_id']]['line_category'].startswith('Excluded'): flags.append('Nearest raw line excluded from fiber screening')
    if lf['line_category'].startswith('Conditional'): flags.append('Nearest screened line status requires confirmation')
    if any(abs(best-t)<=.05 for t in [.5,1,3,5]) or any(abs(dn-t)<=.05 for t in [.5,1]): flags.append('Within 50 m of a screening threshold')
    # Rerun the documented proximity component, without inventing a power factor.
    docscore=min(100,100*math.exp(-oldn/3)+(10 if oldl<=2 else 0))
    newscore=min(100,100*math.exp(-dn/3)+(10 if dl<=2 else 0))
    out={
      'Overall rank':r['Overall Rank'],'Phase':r['Phase'],'PSGC code':r['PSGC Code'],
      'Barangay':r['Barangay'],'Municipality':r['Municipality'],'Province':r['Province'],'Region':r['Region'],
      'Latitude':r['Latitude'],'Longitude':r['Longitude'],'Screening class':classes[cls],
      'Workbook node km':oldn,'All-point reproduced km':float(rawnode[i]),'Screened node km':dn,'Node change km':delta_n,
      'Workbook line-vertex km':oldl,'All-vertex reproduced km':float(rawvertex[i]),'All-line segment km':la['km'],
      'Screened line km':dl,'Line change km':delta_l,'Stronger-evidence line km':lt['km'],
      'Nearest screened asset km':best,'Nearest raw point':rn['name'],'Raw point is node candidate':rn['node_candidate'],
      'Nearest node ID':nn['id'],'Nearest node':nn['name'],'Node longitude':float(points[ni[i],0]),'Node latitude':float(points[ni[i],1]),
      'Nearest line ID':lf['id'],'Nearest line':lf['name'],'Line evidence':lf['line_category'],
      'Line nearest longitude':ls['lon'],'Line nearest latitude':ls['lat'],
      'Nearest raw line ID':la['feature_id'],'Nearest raw line category':byid[la['feature_id']]['line_category'],
      'Stronger line ID':lt['feature_id'],'Stronger line name':byid[lt['feature_id']]['name'],
      'Workbook tier':r['Deploy Tier'],'Workbook deploy score':r['Deploy Score (35%)'],
      'Documented score no power':docscore,'Screened proximity score no power':newscore,
      'Workbook composite':r['Composite Score'],'Target subscribers':r['Subs @ 30%'],
      'Review flags':'; '.join(flags),'Source sheet':r['Source sheet'],'Source row':r['Source row'],
    }
    results.append(out)

def stats(v):
    a=np.array(v); return {k:float(x) for k,x in zip(['mean','median','p90','max'],[a.mean(),np.median(a),np.percentile(a,90),a.max()])}
summary={'sites':len(rows),'point_features':sum(bool(f['points']) for f in F),'node_candidates':len(nodes),'unique_node_coordinates':len(np.unique(nodes,axis=0)),
 'line_features':sum(bool(f['lines']) for f in F),'line_vertices':len(vertices),'line_categories':dict(collections.Counter(f['line_category'] for f in F if f['lines'])),
 'node_reproduced_0.011km':sum(abs(r['All-point reproduced km']-r['Workbook node km'])<=.011 for r in results),
 'vertex_reproduced_0.011km':sum(abs(r['All-vertex reproduced km']-r['Workbook line-vertex km'])<=.011 for r in results),
 'raw_point_not_node':sum(not r['Raw point is node candidate'] for r in results),
 'node_increase_over_500m':sum(r['Node change km']>.5 for r in results),
 'node_crosses_1km':sum(r['Workbook node km']<=1 and r['Screened node km']>1 for r in results),
 'node_crosses_3km':sum(r['Workbook node km']<=3 and r['Screened node km']>3 for r in results),
 'vertex_overstatement_500m':sum(r['All-vertex reproduced km']-r['All-line segment km']>.5 for r in results),
 'vertex_overstatement_100m':sum(r['All-vertex reproduced km']-r['All-line segment km']>.1 for r in results),
 'excluded_nearest_line':sum(r['Nearest raw line category'].startswith('Excluded') for r in results),
 'score_reproduced_within_0.3':sum(abs(r['Workbook deploy score']-r['Documented score no power'])<=.3 for r in results),
 'classes':dict(collections.Counter(r['Screening class'] for r in results)),
 'stats':{col:stats([r[col] for r in results]) for col in ['Workbook node km','Screened node km','Workbook line-vertex km','All-line segment km','Screened line km','Stronger-evidence line km']},
 'phase':[]}
for phase in range(1,6):
    rs=[r for r in results if r['Phase']==phase]
    summary['phase'].append({'phase':phase,'sites':len(rs),'class_counts':dict(collections.Counter(r['Screening class'][0] for r in rs)),
      'workbook_node_mean':float(np.mean([r['Workbook node km'] for r in rs])),
      'node_mean':float(np.mean([r['Screened node km'] for r in rs])),
      'line_mean':float(np.mean([r['Screened line km'] for r in rs])),
      'node_1km':sum(r['Screened node km']<=1 for r in rs),'either_3km':sum(r['Nearest screened asset km']<=3 for r in rs),
      'strong_either_3km':sum(min(r['Screened node km'],r['Stronger-evidence line km'])<=3 for r in rs),
      'node_misclassified':sum(not r['Raw point is node candidate'] for r in rs)})
(OUT/'results.json').write_text(json.dumps(results,ensure_ascii=False))
(OUT/'summary.json').write_text(json.dumps(summary,indent=2))
(OUT/'classified_features.json').write_text(json.dumps(F,ensure_ascii=False))
with (OUT/'FWA_All_5000_Site_Validation.csv').open('w',newline='',encoding='utf-8-sig') as fp:
    writer=csv.DictWriter(fp,fieldnames=list(results[0]));writer.writeheader();writer.writerows(results)
print(json.dumps(summary,indent=2),flush=True)
