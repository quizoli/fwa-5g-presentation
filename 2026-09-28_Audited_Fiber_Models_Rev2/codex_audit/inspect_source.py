from pathlib import Path
import zipfile, re, collections, json
from lxml import etree as E
P=Path('/Users/olivertungol/Library/CloudStorage/OneDrive-Personal/Comclark/GIDA/NATIONAL & REGIONAL BACKBONE_NOV 2024_REPORT.kmz')
s=zipfile.ZipFile(P).read('doc.kml')
# Repair missing declaration on a parsing copy; source is never changed.
s=s.replace(b'<kml ',b'<kml xmlns:mwm="https://maps.me" ',1)
r=E.fromstring(s)
ns={'k':'http://www.opengis.net/kml/2.2'}
def name(e): return e.findtext('k:name','',ns)
def path(e): return ' / '.join(name(a) for a in reversed(list(e.iterancestors())) if E.QName(a).localname in ['Folder','Document'])
features=[]
for i,p in enumerate(r.findall('.//k:Placemark',ns)):
    points=p.findall('.//k:Point/k:coordinates',ns)
    lines=p.findall('.//k:LineString/k:coordinates',ns)
    if not points and not lines: continue
    def coords(el): return [[float(v) for v in token.split(',')[:2]] for token in (el.text or '').split()]
    features.append(dict(id=i,name=name(p),path=path(p),description=p.findtext('k:description','',ns),points=[coords(c) for c in points],lines=[coords(c) for c in lines]))
Path(__file__).with_name('features.json').write_text(json.dumps(features))
print('Feature totals',len(features),'point features',sum(bool(f['points']) for f in features),'line features',sum(bool(f['lines']) for f in features),'vertices',sum(len(l) for f in features for l in f['lines']))
print('POINT GROUPS')
counts=collections.Counter(f['path'] for f in features if f['points'])
for path_,count in counts.most_common():
    examples=[f['name'] for f in features if f['points'] and f['path']==path_][:8]
    print(count,path_,examples)
print('LINE GROUPS')
for path_,count in collections.Counter(f['path'] for f in features if f['lines']).most_common(): print(count,path_)
print('POINT SAMPLE',json.dumps([f for f in features if f['points']][:8],ensure_ascii=False)[:12000])
