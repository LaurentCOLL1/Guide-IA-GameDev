from __future__ import annotations
import argparse,json,sys
from pathlib import Path

def args_after_dash():
    argv=sys.argv; argv=argv[argv.index('--')+1:] if '--' in argv else []
    p=argparse.ArgumentParser(); p.add_argument('--input',required=True); p.add_argument('--output',required=True); p.add_argument('--report',required=True); p.add_argument('--dry-run',action='store_true'); return p.parse_args(argv)
a=args_after_dash(); source=Path(a.input).resolve(); output=Path(a.output).resolve(); report=Path(a.report).resolve()
if source==output: raise SystemExit('source and output must differ')
plan={'source':str(source),'output':str(output),'dry_run':a.dry_run}
if a.dry_run:
 print(json.dumps(plan,sort_keys=True)); raise SystemExit(0)
import bpy
bpy.ops.wm.read_factory_settings(use_empty=True)
if hasattr(bpy.ops.wm,'obj_import'): bpy.ops.wm.obj_import(filepath=str(source))
else: bpy.ops.import_scene.obj(filepath=str(source))
objects=[o for o in bpy.context.scene.objects if o.type=='MESH']
if not objects: raise SystemExit('no mesh imported')
for obj in objects:
 bpy.context.view_layer.objects.active=obj; obj.select_set(True)
bpy.ops.object.transform_apply(location=False,rotation=True,scale=True)
output.parent.mkdir(parents=True,exist_ok=True); report.parent.mkdir(parents=True,exist_ok=True)
bpy.ops.export_scene.gltf(filepath=str(output),export_format='GLB',export_apply=True)
report.write_text(json.dumps({'status':'success','source':source.name,'output':output.name,'mesh_objects':len(objects),'blender':bpy.app.version_string},indent=2,sort_keys=True)+'\n',encoding='utf-8')
print('PRODUCTION_TOOLKIT_BLENDER: PASS')
