import json,tempfile,unittest,wave,zipfile
from pathlib import Path
from production_toolkit.toolkit import *
class ToolkitTests(unittest.TestCase):
 def test_01_slug(self): self.assertEqual(slugify('naMé Test.PNG'),'name-test.png')
 def test_02_hash(self):
  with tempfile.TemporaryDirectory() as d: p=Path(d)/'a'; p.write_text('x'); self.assertEqual(len(sha256_file(p)),64)
 def test_03_copy(self):
  with tempfile.TemporaryDirectory() as d: a=Path(d)/'a'; b=Path(d)/'b'; a.write_text('x'); copy_preserved(a,b); self.assertEqual(b.read_text(),'x')
 def test_04_collision(self):
  with tempfile.TemporaryDirectory() as d:
   a=Path(d)/'a'; b=Path(d)/'b'; a.write_text('x'); b.write_text('y')
   with self.assertRaises(FileExistsError): copy_preserved(a,b)
 def test_05_generate(self):
  with tempfile.TemporaryDirectory() as d: self.assertEqual(len(generate_synthetic(d)),3)
 def test_06_wav_source(self):
  with tempfile.TemporaryDirectory() as d:
   generate_synthetic(d)
   with wave.open(str(Path(d)/'tone.wav'),'rb') as f: self.assertEqual(f.getnchannels(),2)
 def test_07_texture_dry(self):
  with tempfile.TemporaryDirectory() as d: generate_synthetic(d); out=Path(d)/'x.png'; convert_texture(Path(d)/'checker.ppm',out,True); self.assertFalse(out.exists())
 def test_08_texture(self):
  with tempfile.TemporaryDirectory() as d: generate_synthetic(d); out=Path(d)/'x.png'; self.assertEqual(convert_texture(Path(d)/'checker.ppm',out)['width'],4)
 def test_09_audio_dry(self):
  with tempfile.TemporaryDirectory() as d: generate_synthetic(d); out=Path(d)/'x.wav'; convert_audio(Path(d)/'tone.wav',out,dry_run=True); self.assertFalse(out.exists())
 def test_10_audio(self):
  with tempfile.TemporaryDirectory() as d:
   generate_synthetic(d); out=Path(d)/'x.wav'; convert_audio(Path(d)/'tone.wav',out)
   with wave.open(str(out),'rb') as f: self.assertEqual((f.getnchannels(),f.getframerate()),(1,22050))
 def test_11_validate_obj(self):
  with tempfile.TemporaryDirectory() as d: generate_synthetic(d); self.assertTrue(validate_asset(Path(d)/'cube.obj')['valid'])
 def test_12_invalid_obj(self):
  with tempfile.TemporaryDirectory() as d: p=Path(d)/'a.obj'; p.write_text('v 0 0 0\n'); self.assertFalse(validate_asset(p)['valid'])
 def test_13_validate_png(self):
  with tempfile.TemporaryDirectory() as d: generate_synthetic(d); p=Path(d)/'x.png'; convert_texture(Path(d)/'checker.ppm',p); self.assertTrue(validate_asset(p)['valid'])
 def test_14_validate_wav(self):
  with tempfile.TemporaryDirectory() as d: generate_synthetic(d); p=Path(d)/'x.wav'; convert_audio(Path(d)/'tone.wav',p); self.assertTrue(validate_asset(p)['valid'])
 def test_15_unknown(self):
  with tempfile.TemporaryDirectory() as d: p=Path(d)/'x.bin'; p.write_bytes(b'x'); self.assertFalse(validate_asset(p)['valid'])
 def test_16_mapping_collision(self):
  with tempfile.TemporaryDirectory() as d:
   paths=[]
   for n in ['Name Test.txt','name-test.txt']: p=Path(d)/n; p.write_text(n); paths.append(p)
   self.assertEqual(len({x['target'] for x in build_mapping(paths)}),2)
 def test_17_rename_dry(self):
  with tempfile.TemporaryDirectory() as d: p=Path(d)/'A.txt'; p.write_text('a'); out=Path(d)/'out'; apply_mapping(build_mapping([p]),out,True); self.assertFalse(out.exists())
 def test_18_rename_apply(self):
  with tempfile.TemporaryDirectory() as d: p=Path(d)/'A.txt'; p.write_text('a'); out=Path(d)/'out'; self.assertTrue(Path(apply_mapping(build_mapping([p]),out)[0]).exists()); self.assertTrue(p.exists())
 def test_19_catalog(self):
  with tempfile.TemporaryDirectory() as d: files=generate_synthetic(d); self.assertTrue(build_catalog([files[1]])['assets'][0]['validation']['valid'])
 def plan(self): return {'schema_version':1,'tasks':[{'id':'a','action':'copy','source':'a.txt','output':'out/a.txt'},{'id':'b','action':'write-json','output':'out/b.json','payload':{'x':1}}]}
 def test_20_batch_dry(self):
  with tempfile.TemporaryDirectory() as d: r=Path(d); (r/'a.txt').write_text('a'); cp=r/'cp.json'; out=r/'work'; self.assertEqual(run_pipeline(self.plan(),r,out,cp,True)['operations'],['a','b']); self.assertFalse(cp.exists())
 def test_21_batch_resume(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d); (r/'a.txt').write_text('a'); cp=r/'cp.json'; out=r/'work'
   with self.assertRaises(RuntimeError): run_pipeline(self.plan(),r,out,cp,False,'b')
   self.assertEqual(run_pipeline(self.plan(),r,out,cp)['state']['status'],'complete')
 def test_22_plan_mismatch(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d); (r/'a.txt').write_text('a'); cp=r/'cp.json'; out=r/'work'; run_pipeline(self.plan(),r,out,cp); changed=self.plan(); changed['tasks'].append({'id':'c','action':'write-json','output':'c','payload':{}})
   with self.assertRaises(ValueError): run_pipeline(changed,r,out,cp)
 def test_23_hash_stable(self): self.assertEqual(plan_hash(self.plan()),plan_hash(self.plan()))
 def test_24_package_dry(self):
  with tempfile.TemporaryDirectory() as d: r=Path(d)/'root'; r.mkdir(); (r/'a').write_text('a'); out=Path(d)/'x.zip'; package_assets(r,out,True); self.assertFalse(out.exists())
 def test_25_package_deterministic(self):
  with tempfile.TemporaryDirectory() as d: r=Path(d)/'root'; r.mkdir(); (r/'a').write_text('a'); one=Path(d)/'1.zip'; two=Path(d)/'2.zip'; package_assets(r,one); package_assets(r,two); self.assertEqual(sha256_file(one),sha256_file(two))
 def test_26_manifest_inside(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d)/'root'; r.mkdir(); (r/'a').write_text('a'); out=Path(d)/'x.zip'; package_assets(r,out)
   with zipfile.ZipFile(out) as z: self.assertIn('MANIFEST.json',z.namelist())
 def test_27_package_overwrite(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d)/'root'; r.mkdir(); (r/'a').write_text('a'); out=Path(d)/'x.zip'; package_assets(r,out)
   with self.assertRaises(FileExistsError): package_assets(r,out)
 def test_28_distinct(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'a'; p.write_text('a')
   with self.assertRaises(ValueError): ensure_distinct(p,p)
 def test_29_atomic_json(self):
  with tempfile.TemporaryDirectory() as d: p=Path(d)/'x.json'; atomic_json(p,{'x':1}); self.assertEqual(json.loads(p.read_text())['x'],1)
