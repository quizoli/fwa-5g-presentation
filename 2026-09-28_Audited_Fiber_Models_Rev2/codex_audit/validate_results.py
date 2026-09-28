import sys,json,collections,math
from pathlib import Path
sys.path.insert(0,'/tmp/fwa_geo_deps')
import numpy as np
from pyproj import Geod,Transformer
from scipy.optimize import minimize_scalar
P=Path(__file__).resolve().parent
r=json.loads((P/'results.json').read_text());f=json.loads((P/'classified_features.json').read_text()); byid={x['id']:x for x in f}
g=Geod(ellps='WGS84');tr=Transformer.from_crs('EPSG:4979','EPSG:4978',always_xy=True)
assert len(r)==5000 and len(set(x['PSGC code'] for x in r))==5000
for x in r:
    assert x['Screened line km']+1e-7>=x['All-line segment km']
    assert x['Stronger-evidence line km']+1e-7>=x['Screened line km']
    assert not byid[x['Nearest line ID']]['line_category'].startswith('Excluded')
    assert byid[x['Nearest node ID']]['node_candidate']
    assert abs(g.inv(x['Longitude'],x['Latitude'],x['Line nearest longitude'],x['Line nearest latitude'])[2]/1000-x['Screened line km'])<1e-8
# Independent check: minimize over every ORIGINAL segment of the selected route,
# using SciPy's scalar optimizer instead of the indexed vector ternary search.
sample=sorted(set([0,56,171,176,387,464,537,999,1355,2106,4999]+list(np.random.default_rng(23).choice(5000,19,replace=False))))
errors=[]
for i in sample:
    x=r[i]; p=(x['Longitude'],x['Latitude']); best=math.inf
    for line in byid[x['Nearest line ID']]['lines']:
        for a,b in zip(line,line[1:]):
            az,_,length=g.inv(*a,*b)
            def objective(s):
                lon,lat,_=g.fwd(*a,az,s);return g.inv(*p,lon,lat)[2]
            candidates=[objective(0),objective(length)]
            if length>0: candidates.append(minimize_scalar(objective,bounds=(0,length),method='bounded',options={'xatol':.0001}).fun)
            best=min(best,*candidates)
    errors.append(abs(best-x['Screened line km']*1000))
assert max(errors)<.02, max(errors)
actions={'A':'First survey: confirm node handoff, spare capacity and a feasible short route; co-location is not established.',
 'B':'Survey a short node lateral; confirm port/fiber capacity, access and route.',
 'C':'Locate an authorized closure or handhole and confirm splicing/capacity; nearby cable alone is insufficient.',
 'D':'Compare a routed node lateral with an approved line tap; survey crossings and permissions.',
 'E':'Develop a longer lateral design and compare alternative backhaul before scheduling.',
 'F':'Reassess BTS location or alternative backhaul; seek updated fiber inventory.'}
for x in r:
    x['Recommended action']=actions[x['Screening class'][0]]
    if x['Screening class'].startswith('D'):x['Screening class']='D - Other node or line within 3 km'
ranked=sorted(r,key=lambda x:(x['Screening class'][0],x['Screened node km'] if x['Screening class'][0] in 'AB' else x['Nearest screened asset km'],-x['Target subscribers']))
for i,x in enumerate(ranked,1): x['Fiber survey priority']=i
(P/'results.json').write_text(json.dumps(r,ensure_ascii=False))
s=json.loads((P/'summary.json').read_text())
s['classes']=dict(collections.Counter(x['Screening class'] for x in r))
s['validation']={'independent_segment_checks':len(sample),'maximum_error_m':max(errors),'all_5000_geometry_and_asset_checks':'passed'}
s['vertex_discrepancy_over_100m']=sum(abs(x['Workbook line-vertex km']-x['All-vertex reproduced km'])>.1 for x in r)
s['score25_unexplained']=sum(abs(x['Workbook deploy score']-x['Documented score no power'])>.3 and x['Workbook deploy score']==25 for x in r)
s['score15_unexplained']=sum(abs(x['Workbook deploy score']-x['Documented score no power'])>.3 and x['Workbook deploy score']==15 for x in r)
s['conditional_line_winners']=sum(x['Line evidence'].startswith('Conditional') for x in r)
s['node_under_3km']=sum(x['Screened node km']<=3 for x in r)
s['screened_line_under_500m']=sum(x['Screened line km']<=.5 for x in r)
s['either_under_3km']=sum(x['Nearest screened asset km']<=3 for x in r)
s['phase1_node_over_3km']=sum(x['Phase']==1 and x['Screened node km']>3 for x in r)
s['line_increase_500m']=sum(x['Line change km']>.5 for x in r)
s['node_exact_rounding']=sum(abs(x['All-point reproduced km']-x['Workbook node km'])<=.00501 for x in r)
(P/'summary.json').write_text(json.dumps(s,indent=2))
import csv
with (P/'FWA_All_5000_Site_Validation.csv').open('w',newline='',encoding='utf-8-sig') as fp:
    wr=csv.DictWriter(fp,fieldnames=list(r[0]));wr.writeheader();wr.writerows(r)
print(json.dumps({k:s[k] for k in ['validation','conditional_line_winners','node_under_3km','screened_line_under_500m','either_under_3km','phase1_node_over_3km','line_increase_500m','node_exact_rounding']},indent=2))
