#!/usr/bin/env python3
"""Inventory the tagged PDF structure without making a conformance claim."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from pypdf import PdfReader
from pypdf.generic import ArrayObject, DictionaryObject, IndirectObject


def dereference(value: Any) -> Any:
    if isinstance(value, IndirectObject):
        return value.get_object()
    return value


def object_key(value: Any) -> tuple[int, int] | None:
    if isinstance(value, IndirectObject):
        return value.idnum, value.generation
    return None


def text_value(value: Any) -> str | None:
    value = dereference(value)
    if value is None:
        return None
    try:
        return str(value)
    except Exception:
        return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    reader = PdfReader(str(args.pdf), strict=False)
    catalog = dereference(reader.trailer["/Root"])
    mark_info = dereference(catalog.get("/MarkInfo"))
    structure_root = dereference(catalog.get("/StructTreeRoot"))

    tags: Counter[str] = Counter()
    types: Counter[str] = Counter()
    headings: Counter[str] = Counter()
    languages: Counter[str] = Counter()
    figures = 0
    figures_with_alt = 0
    figures_with_actual_text = 0
    empty_figure_alt = 0
    tables = 0
    table_headers = 0
    table_cells = 0
    lists = 0
    list_items = 0
    links = 0
    document_nodes = 0
    alt_samples: list[str] = []
    visited: set[tuple[int, int]] = set()
    direct_seen: set[int] = set()

    def visit(value: Any) -> None:
        nonlocal figures, figures_with_alt, figures_with_actual_text
        nonlocal empty_figure_alt, tables, table_headers, table_cells
        nonlocal lists, list_items, links, document_nodes

        key = object_key(value)
        if key is not None:
            if key in visited:
                return
            visited.add(key)
        else:
            direct_id = id(value)
            if direct_id in direct_seen:
                return
            direct_seen.add(direct_id)

        value = dereference(value)
        if isinstance(value, (ArrayObject, list)):
            for child in value:
                visit(child)
            return
        if not isinstance(value, (DictionaryObject, dict)):
            return

        item_type = text_value(value.get("/Type"))
        if item_type:
            types[item_type] += 1

        tag = text_value(value.get("/S"))
        if tag:
            tags[tag] += 1
            if tag in {"/H", "/H1", "/H2", "/H3", "/H4", "/H5", "/H6"}:
                headings[tag] += 1
            if tag == "/Document":
                document_nodes += 1
            elif tag == "/Figure":
                figures += 1
                alt = text_value(value.get("/Alt"))
                actual = text_value(value.get("/ActualText"))
                if alt is not None:
                    if alt.strip():
                        figures_with_alt += 1
                        if len(alt_samples) < 20:
                            alt_samples.append(alt)
                    else:
                        empty_figure_alt += 1
                if actual is not None and actual.strip():
                    figures_with_actual_text += 1
            elif tag == "/Table":
                tables += 1
            elif tag == "/TH":
                table_headers += 1
            elif tag == "/TD":
                table_cells += 1
            elif tag == "/L":
                lists += 1
            elif tag == "/LI":
                list_items += 1
            elif tag == "/Link":
                links += 1

        language = text_value(value.get("/Lang"))
        if language:
            languages[language] += 1

        if "/K" in value:
            visit(value["/K"])

    if structure_root is not None:
        visit(structure_root.get("/K"))

    role_map: dict[str, str | None] = {}
    if structure_root is not None:
        raw_role_map = dereference(structure_root.get("/RoleMap"))
        if isinstance(raw_role_map, dict):
            role_map = {
                str(key): text_value(value)
                for key, value in sorted(
                    raw_role_map.items(), key=lambda item: str(item[0])
                )
            }

    preferences = dereference(catalog.get("/ViewerPreferences"))
    result = {
        "schema_version": 1,
        "claim": "structure-inventory-not-pdfua-conformance",
        "file": args.pdf.name,
        "bytes": args.pdf.stat().st_size,
        "pages": len(reader.pages),
        "catalog": {
            "lang": text_value(catalog.get("/Lang")),
            "mark_info": {
                str(key): bool(value)
                for key, value in (
                    mark_info.items() if isinstance(mark_info, dict) else []
                )
            },
            "has_structure_tree": structure_root is not None,
            "viewer_preferences": {
                str(key): text_value(value)
                for key, value in (
                    preferences.items() if isinstance(preferences, dict) else []
                )
            },
        },
        "structure": {
            "visited_indirect_objects": len(visited),
            "tag_counts": dict(sorted(tags.items())),
            "type_counts": dict(sorted(types.items())),
            "heading_counts": dict(sorted(headings.items())),
            "document_nodes": document_nodes,
            "figures": figures,
            "figures_with_alt": figures_with_alt,
            "figures_with_actual_text": figures_with_actual_text,
            "empty_figure_alt": empty_figure_alt,
            "figure_alt_samples": alt_samples,
            "tables": tables,
            "table_headers": table_headers,
            "table_cells": table_cells,
            "lists": lists,
            "list_items": list_items,
            "links": links,
            "languages": dict(sorted(languages.items())),
            "role_map": role_map,
        },
        "metadata": {
            str(key): str(value)
            for key, value in (
                reader.metadata.items() if reader.metadata else []
            )
        },
    }

    encoded = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
