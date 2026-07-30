from __future__ import annotations
import audioop, csv, hashlib, json, math, os, re, shutil, struct, tempfile, unicodedata, wave, zipfile
from datetime import datetime, timezone
from pathlib import Path

EXIT_OK=0; EXIT_ARGUMENT=2; EXIT_VALIDATION=3; EXIT_TASK=4; EXIT_COLLISION=5

def utc_now(): return datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
def emit(tool,event,level='info',**details): print(json.dumps({'timestamp':utc_now(),'level':level,'event':event,'tool':tool,'details':details},sort_keys=True))
def sha256_file(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for chunk in iter(lambda:f.read(65536),b''): h.update(chunk)
 return h.hexdigest()
def atomic_json(path,payload):
 path=Path(path); path.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(prefix=path.name+'.',dir=path.parent)
 try:
  with os.fdopen(fd,'w',encoding='utf-8') as f: json.dump(payload,f,ensure_ascii=False,indent=2,sort_keys=True); f.write('\n')
  os.replace(tmp,path)
 finally:
  if os.path.exists(tmp): os.unlink(tmp)
def ensure_distinct(source,output):
 if Path(source).resolve()==Path(output).resolve(): raise ValueError('source and output must differ')
def safe_output(path,overwrite=False):
 path=Path(path)
 if path.exists() and not overwrite: raise FileExistsError(path)
 path.parent.mkdir(parents=True,exist_ok=True)
def slugify(name):
 stem=unicodedata.normalize('NFKD',Path(name).stem).encode('ascii','ignore').decode().lower(); stem=re.sub(r'[^a-z0-9]+','-',stem).strip('-') or 'asset'
 return stem+Path(name).suffix.lower()
def copy_preserved(source,output,overwrite=False): ensure_distinct(source,output); safe_output(output,overwrite); shutil.copy2(source,output)

def generate_synthetic(root):
 root=Path(root); root.mkdir(parents=True,exist_ok=True)
 ppm=root/'checker.ppm'; ppm.write_text('P3\n4 4\n255\n'+'\n'.join(['255 255 255 0 0 0 255 255 255 0 0 0','0 0 0 255 255 255 0 0 0 255 255 255']*2)+'\n',encoding='ascii')
 obj=root/'cube.obj'; obj.write_text('# synthetic\nv -0.5 -0.5 0\nv 0.5 -0.5 0\nv 0.5 0.5 0\nv -0.5 0.5 0\nf 1 2 3 4\n',encoding='ascii')
 wav=root/'tone.wav'; rate=44100; frames=rate//10
 with wave.open(str(wav),'wb') as out:
  out.setnchannels(2); out.setsampwidth(2); out.setframerate(rate); data=bytearray()
  for i in range(frames):
   sample=int(12000*math.sin(2*math.pi*440*i/rate)); data.extend(struct.pack('<hh',sample,sample))
  out.writeframes(bytes(data))
 atomic_json(root/'fixture-manifest.json',{'schema_version':1,'files':['checker.ppm','cube.obj','tone.wav'],'synthetic':True})
 return [ppm,obj,wav]
def convert_texture(source,output,dry_run=False,overwrite=False):
 ensure_distinct(source,output)
 if dry_run: return {'source':str(source),'output':str(output),'action':'convert-ppm-png'}
 from PIL import Image
 safe_output(output,overwrite)
 with Image.open(source) as image: width,height=image.width,image.height; image.convert('RGBA').save(output,format='PNG',optimize=False,compress_level=9)
 return {'width':width,'height':height,'mode':'RGBA'}
def convert_audio(source,output,target_rate=22050,dry_run=False,overwrite=False):
 ensure_distinct(source,output)
 if dry_run: return {'source':str(source),'output':str(output),'action':'convert-wav','rate':target_rate}
 safe_output(output,overwrite)
 with wave.open(str(source),'rb') as src: channels,width,rate,frames=src.getnchannels(),src.getsampwidth(),src.getframerate(),src.getnframes(); data=src.readframes(frames)
 if width!=2: raise ValueError('only 16-bit PCM is supported')
 if channels==2: data=audioop.tomono(data,2,0.5,0.5)
 elif channels!=1: raise ValueError('only mono or stereo is supported')
 if rate!=target_rate: data,_=audioop.ratecv(data,2,1,rate,target_rate,None)
 with wave.open(str(output),'wb') as dst: dst.setnchannels(1); dst.setsampwidth(2); dst.setframerate(target_rate); dst.writeframes(data)
 return {'channels':1,'sample_width':2,'sample_rate':target_rate,'frames':len(data)//2}
def validate_asset(path):
 path=Path(path); suffix=path.suffix.lower()
 if suffix=='.obj':
  vertices=faces=0
  for line in path.read_text(encoding='utf-8').splitlines():
   if line.startswith('v '): vertices+=1
   elif line.startswith('f '): faces+=1
  errors=[] if vertices>=3 and faces>=1 else ['obj_structure']; return {'type':'obj','valid':not errors,'vertices':vertices,'faces':faces,'errors':errors}
 if suffix=='.png':
  from PIL import Image
  with Image.open(path) as im: im.verify()
  with Image.open(path) as im: return {'type':'png','valid':im.width>0 and im.height>0,'width':im.width,'height':im.height,'mode':im.mode,'errors':[]}
 if suffix=='.wav':
  with wave.open(str(path),'rb') as src: data={'channels':src.getnchannels(),'sample_width':src.getsampwidth(),'sample_rate':src.getframerate(),'frames':src.getnframes()}
  errors=[]
  if data['channels'] not in (1,2): errors.append('channels')
  if data['sample_width']!=2: errors.append('sample_width')
  return {'type':'wav','valid':not errors,**data,'errors':errors}
 return {'type':'unknown','valid':False,'errors':['unsupported_extension']}
def build_mapping(paths):
 used=set(); result=[]
 for path in sorted((Path(p) for p in paths),key=lambda p:p.name.casefold()):
  base=slugify(path.name); candidate=base; index=2
  while candidate in used: candidate=f'{Path(base).stem}-{index}{Path(base).suffix}'; index+=1
  used.add(candidate); result.append({'source':str(path),'target':candidate})
 return result
def apply_mapping(mapping,output_dir,dry_run=False):
 if dry_run: return mapping
 outputs=[]
 for item in mapping:
  target=Path(output_dir)/item['target']; copy_preserved(item['source'],target); outputs.append(str(target))
 return outputs
def build_catalog(paths):
 assets=[]
 for path in sorted((Path(p) for p in paths),key=lambda p:p.as_posix()): assets.append({'path':path.name,'bytes':path.stat().st_size,'sha256':sha256_file(path),'validation':validate_asset(path)})
 return {'schema_version':1,'assets':assets}
def write_catalog(catalog,json_path,csv_path):
 safe_output(json_path); safe_output(csv_path); atomic_json(json_path,catalog)
 with Path(csv_path).open('w',newline='',encoding='utf-8') as f:
  writer=csv.DictWriter(f,fieldnames=['path','bytes','sha256','valid']); writer.writeheader()
  for item in catalog['assets']: writer.writerow({'path':item['path'],'bytes':item['bytes'],'sha256':item['sha256'],'valid':item['validation']['valid']})
def plan_hash(plan): return hashlib.sha256(json.dumps(plan,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def run_pipeline(plan,source_root,workspace,checkpoint,dry_run=False,fail_task=None):
 source_root=Path(source_root); workspace=Path(workspace); checkpoint=Path(checkpoint); ph=plan_hash(plan); state={'plan_hash':ph,'completed':[],'status':'partial'}
 if checkpoint.exists():
  state=json.loads(checkpoint.read_text(encoding='utf-8'))
  if state.get('plan_hash')!=ph: raise ValueError('checkpoint plan mismatch')
 operations=[]
 for task in plan['tasks']:
  if task['id'] in state['completed']: continue
  operations.append(task['id'])
  if dry_run: continue
  if fail_task==task['id']: raise RuntimeError(f'injected failure: {task["id"]}')
  output=workspace/task['output']
  if task['action']=='copy': copy_preserved(source_root/task['source'],output)
  elif task['action']=='write-json': atomic_json(output,task['payload'])
  else: raise ValueError(f'unknown action: {task["action"]}')
  state['completed'].append(task['id']); atomic_json(checkpoint,state)
 if not dry_run: state['status']='complete'; atomic_json(checkpoint,state)
 return {'operations':operations,'state':state}
def build_manifest(root):
 root=Path(root); return {'schema_version':1,'files':[{'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':sha256_file(p)} for p in sorted(x for x in root.rglob('*') if x.is_file())]}
def package_assets(root,output,dry_run=False):
 root=Path(root); output=Path(output); manifest=build_manifest(root)
 if dry_run: return manifest
 safe_output(output)
 with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as zf:
  for item in manifest['files']:
   info=zipfile.ZipInfo(item['path'],(1980,1,1,0,0,0)); info.external_attr=0o100644<<16; info.compress_type=zipfile.ZIP_DEFLATED; zf.writestr(info,(root/item['path']).read_bytes())
  info=zipfile.ZipInfo('MANIFEST.json',(1980,1,1,0,0,0)); info.external_attr=0o100644<<16; info.compress_type=zipfile.ZIP_DEFLATED; zf.writestr(info,(json.dumps(manifest,sort_keys=True,indent=2)+'\n').encode())
 return manifest
