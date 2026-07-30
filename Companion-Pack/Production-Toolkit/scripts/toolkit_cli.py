#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
from production_toolkit.toolkit import *

def main():
 p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='command',required=True)
 g=sub.add_parser('generate'); g.add_argument('--output',required=True)
 t=sub.add_parser('texture'); t.add_argument('source'); t.add_argument('output'); t.add_argument('--dry-run',action='store_true')
 a=sub.add_parser('audio'); a.add_argument('source'); a.add_argument('output'); a.add_argument('--target-rate',type=int,default=22050); a.add_argument('--dry-run',action='store_true')
 v=sub.add_parser('validate'); v.add_argument('paths',nargs='+'); v.add_argument('--report')
 r=sub.add_parser('rename'); r.add_argument('inputs',nargs='+'); r.add_argument('--output-dir',required=True); r.add_argument('--mapping'); r.add_argument('--dry-run',action='store_true')
 c=sub.add_parser('catalog'); c.add_argument('paths',nargs='+'); c.add_argument('--json',required=True); c.add_argument('--csv',required=True); c.add_argument('--dry-run',action='store_true')
 b=sub.add_parser('batch'); b.add_argument('--plan',required=True); b.add_argument('--source-root',required=True); b.add_argument('--workspace',required=True); b.add_argument('--checkpoint'); b.add_argument('--dry-run',action='store_true'); b.add_argument('--fail-task')
 z=sub.add_parser('package'); z.add_argument('root'); z.add_argument('output'); z.add_argument('--dry-run',action='store_true')
 x=p.parse_args(); tool='production-toolkit-'+x.command
 try:
  if x.command=='generate': result={'files':[str(p) for p in generate_synthetic(x.output)]}
  elif x.command=='texture': result=convert_texture(x.source,x.output,x.dry_run)
  elif x.command=='audio': result=convert_audio(x.source,x.output,x.target_rate,x.dry_run)
  elif x.command=='validate':
   results=[{'path':p,**validate_asset(p)} for p in x.paths]; result={'results':results,'valid':all(i['valid'] for i in results)}
   if x.report: atomic_json(x.report,result)
   if not result['valid']: emit(tool,'failed','error',**result); return EXIT_VALIDATION
  elif x.command=='rename':
   mapping=build_mapping(x.inputs); outputs=apply_mapping(mapping,x.output_dir,x.dry_run); result={'mapping':mapping,'outputs':outputs}
   if x.mapping and not x.dry_run: atomic_json(x.mapping,{'schema_version':1,'mapping':mapping})
  elif x.command=='catalog':
   result=build_catalog(x.paths)
   if not x.dry_run: write_catalog(result,x.json,x.csv)
  elif x.command=='batch':
   plan=json.loads(Path(x.plan).read_text(encoding='utf-8')); checkpoint=x.checkpoint or str(Path(x.workspace)/'checkpoint.json'); result=run_pipeline(plan,x.source_root,x.workspace,checkpoint,x.dry_run,x.fail_task)
  elif x.command=='package': result=package_assets(x.root,x.output,x.dry_run)
  emit(tool,'complete',dry_run=getattr(x,'dry_run',False),result=result); return EXIT_OK
 except FileExistsError as e: emit(tool,'collision','error',message=str(e)); return EXIT_COLLISION
 except Exception as e: emit(tool,'failed','error',message=str(e)); return EXIT_TASK
if __name__=='__main__': raise SystemExit(main())
