#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("results", nargs="+", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    loaded = [json.loads(path.read_text(encoding="utf-8")) for path in args.results]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    campaign = {
        "schema_version":1,
        "campaign_id":"CAMPAIGN-PACK8-CI",
        "generated_at_utc":now,
        "environment_ids":sorted({item["environment"]["environment_id"] for item in loaded}),
        "results":[{"benchmark_id":item["benchmark_id"],"median":item["statistics"]["median"],"unit":item["unit"],"oracle_status":item["oracle_status"],"evidence_level":item.get("evidence_level")} for item in loaded],
        "reservations":["hosted runner","synthetic workloads","render proxy is not a physical GPU qualification","no universal ranking"]
    }
    (args.output_dir / "campaign.json").write_text(json.dumps(campaign,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    with (args.output_dir / "campaign.csv").open("w",encoding="utf-8",newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=["benchmark_id","median","unit","oracle_status","evidence_level"])
        writer.writeheader(); writer.writerows(campaign["results"])
    lines=["# Rapport de campagne Pack 8","",f"Horodatage UTC : `{now}`.","","| Benchmark | Médiane | Unité | Oracle | Portée |","|---|---:|---|---|---|"]
    for row in campaign["results"]:
        lines.append(f"| {row['benchmark_id']} | {row['median']} | {row['unit']} | {row['oracle_status']} | {row['evidence_level']} |")
    lines += ["","## Réserves",""] + [f"- {item}" for item in campaign["reservations"]]
    (args.output_dir / "campaign.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(json.dumps({"status":"success","results":len(loaded)},sort_keys=True))
    return 0

if __name__ == "__main__": raise SystemExit(main())
