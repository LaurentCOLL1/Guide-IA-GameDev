from __future__ import annotations
import argparse, collections, hashlib, json, math, re, sys, unicodedata
from pathlib import Path

ALLOWED_STATUS={"canonical","rumor","memory","reference"}
REQUIRED={"id","title","category","truth_status","version","language","narrator","tags","text","provenance","redistribution"}

def canonical_json(data):
    return json.dumps(data,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n"

def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()

def sha256_file(path):
    return sha256_bytes(Path(path).read_bytes())

def normalize(text):
    text=unicodedata.normalize("NFKD",text.lower())
    text="".join(c for c in text if not unicodedata.combining(c))
    return re.findall(r"[a-z0-9]+",text)

def validate_document(doc,path="<memory>"):
    missing=sorted(REQUIRED-set(doc))
    if missing: raise ValueError(f"{path}: missing {missing}")
    if doc["truth_status"] not in ALLOWED_STATUS: raise ValueError(f"{path}: invalid truth_status")
    if not isinstance(doc["tags"],list) or not all(isinstance(x,str) for x in doc["tags"]): raise ValueError(f"{path}: tags")
    if not doc["id"] or not doc["text"].strip(): raise ValueError(f"{path}: empty id/text")
    if doc["redistribution"]!="synthetic-original": raise ValueError(f"{path}: redistribution")

def load_documents(source_dir):
    source_dir=Path(source_dir); docs=[]; ids=set()
    for path in sorted(source_dir.rglob("*.json")):
        doc=json.loads(path.read_text(encoding="utf-8"))
        validate_document(doc,str(path))
        if doc["id"] in ids: raise ValueError(f"duplicate id: {doc['id']}")
        ids.add(doc["id"])
        doc=dict(doc); doc["_source"]=path.relative_to(source_dir).as_posix(); doc["_sha256"]=sha256_file(path)
        docs.append(doc)
    if not docs: raise ValueError("empty corpus")
    return docs

def chunk_words(words,max_words=45,overlap=8):
    if max_words<8 or overlap<0 or overlap>=max_words: raise ValueError("invalid chunk settings")
    out=[]; start=0
    while start<len(words):
        end=min(len(words),start+max_words); out.append((start,end,words[start:end]))
        if end==len(words): break
        start=end-overlap
    return out

def vector(tokens,dims=24):
    values=[0.0]*dims
    for token in tokens:
        digest=hashlib.sha256(token.encode()).digest()
        slot=int.from_bytes(digest[:2],"big")%dims
        values[slot]+=1.0 if digest[2]%2==0 else -1.0
    norm=math.sqrt(sum(x*x for x in values)) or 1.0
    return [round(x/norm,8) for x in values]

def build_index(source_dir,max_words=45,overlap=8):
    documents=load_documents(source_dir); chunks=[]; postings=collections.defaultdict(list)
    for doc in documents:
        words=normalize(doc["title"]+" "+doc["text"]+" "+" ".join(doc["tags"]))
        for idx,(start,end,part) in enumerate(chunk_words(words,max_words,overlap)):
            text=" ".join(part); cid=hashlib.sha256(f"{doc['id']}:{idx}:{text}".encode()).hexdigest()[:20]
            counts=collections.Counter(part)
            chunk={"chunk_id":cid,"document_id":doc["id"],"ordinal":idx,"start_word":start,"end_word":end,
                   "truth_status":doc["truth_status"],"category":doc["category"],"title":doc["title"],"text":text,
                   "term_counts":dict(sorted(counts.items())),"vector":vector(part)}
            chunks.append(chunk)
            for term in counts: postings[term].append(cid)
    docs_public=[]
    for d in documents:
        item={k:v for k,v in d.items() if k!="text" and not k.startswith("_")}
        item.update({"source":d["_source"],"source_sha256":d["_sha256"]})
        docs_public.append(item)
    source_manifest={d["id"]:d["_sha256"] for d in documents}
    index={"schema_version":1,"algorithm":"lexical-bm25+hash-vector-v1","chunking":{"max_words":max_words,"overlap":overlap},
           "source_manifest":dict(sorted(source_manifest.items())),"source_digest":sha256_bytes(canonical_json(source_manifest).encode()),
           "documents":sorted(docs_public,key=lambda x:x["id"]),"chunks":sorted(chunks,key=lambda x:x["chunk_id"]),
           "postings":{k:sorted(v) for k,v in sorted(postings.items())}}
    index["index_digest"]=sha256_bytes(canonical_json(index).encode())
    return index

def write_index(index,path):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True); path.write_text(canonical_json(index),encoding="utf-8")

def load_index(path):
    data=json.loads(Path(path).read_text(encoding="utf-8"))
    expected=data.get("index_digest"); copy=dict(data); copy.pop("index_digest",None)
    if expected!=sha256_bytes(canonical_json(copy).encode()): raise ValueError("index digest mismatch")
    return data

def cosine(a,b):
    return sum(x*y for x,y in zip(a,b))

def search(index,query,top_k=5,truth_status=None,category=None,mode="hybrid"):
    terms=normalize(query)
    if not terms: return []
    chunks=index["chunks"]; n=max(1,len(chunks))
    df={t:len(index["postings"].get(t,[])) for t in set(terms)}
    qvec=vector(terms); out=[]
    for chunk in chunks:
        if truth_status and chunk["truth_status"]!=truth_status: continue
        if category and chunk["category"]!=category: continue
        lexical=0.0
        for term in terms:
            tf=chunk["term_counts"].get(term,0)
            if tf:
                lexical+=(1+math.log(tf))*math.log(1+(n-df[term]+0.5)/(df[term]+0.5))
        semantic=cosine(qvec,chunk["vector"])
        score=lexical if mode=="lexical" else semantic if mode=="vector" else lexical+max(0.0,semantic)*0.25
        if score>0:
            out.append({"chunk_id":chunk["chunk_id"],"document_id":chunk["document_id"],"title":chunk["title"],
                        "truth_status":chunk["truth_status"],"category":chunk["category"],
                        "score":round(score,8),"text":chunk["text"]})
    return sorted(out,key=lambda x:(-x["score"],x["document_id"],x["chunk_id"]))[:top_k]

def remove_document(index,document_id):
    if document_id not in {d["id"] for d in index["documents"]}: raise KeyError(document_id)
    keep_chunks=[c for c in index["chunks"] if c["document_id"]!=document_id]
    keep_ids={c["chunk_id"] for c in keep_chunks}
    out=dict(index)
    out["documents"]=[d for d in index["documents"] if d["id"]!=document_id]
    out["chunks"]=keep_chunks
    out["postings"]={t:[cid for cid in ids if cid in keep_ids] for t,ids in index["postings"].items()}
    out["postings"]={t:ids for t,ids in out["postings"].items() if ids}
    out["source_manifest"]={k:v for k,v in index["source_manifest"].items() if k!=document_id}
    out["source_digest"]=sha256_bytes(canonical_json(out["source_manifest"]).encode())
    out.pop("index_digest",None)
    out["index_digest"]=sha256_bytes(canonical_json(out).encode())
    return out

def verify_deleted(index,document_id):
    if any(d["id"]==document_id for d in index["documents"]): return False
    if any(c["document_id"]==document_id for c in index["chunks"]): return False
    return document_id not in canonical_json(index["postings"]) and document_id not in index["source_manifest"]

def build_parser():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest="cmd",required=True)
    b=sub.add_parser("build"); b.add_argument("--source-dir",required=True); b.add_argument("--output",required=True); b.add_argument("--max-words",type=int,default=45); b.add_argument("--overlap",type=int,default=8)
    s=sub.add_parser("search"); s.add_argument("--index",required=True); s.add_argument("--query",required=True); s.add_argument("--top-k",type=int,default=5); s.add_argument("--truth-status"); s.add_argument("--category"); s.add_argument("--mode",choices=["hybrid","lexical","vector"],default="hybrid"); s.add_argument("--output")
    r=sub.add_parser("remove"); r.add_argument("--index",required=True); r.add_argument("--document-id",required=True); r.add_argument("--output",required=True)
    v=sub.add_parser("verify-deleted"); v.add_argument("--index",required=True); v.add_argument("--document-id",required=True)
    return p

def main(argv=None):
    args=build_parser().parse_args(argv)
    try:
        if args.cmd=="build":
            idx=build_index(args.source_dir,args.max_words,args.overlap); write_index(idx,args.output)
            print(canonical_json({"status":"success","documents":len(idx["documents"]),"chunks":len(idx["chunks"]),"index_digest":idx["index_digest"]}),end=""); return 0
        if args.cmd=="search":
            rows=search(load_index(args.index),args.query,args.top_k,args.truth_status,args.category,args.mode)
            payload={"status":"success","query":args.query,"count":len(rows),"results":rows}
            text=json.dumps(payload,ensure_ascii=False,indent=2,sort_keys=True)+"\n"
            if args.output: Path(args.output).write_text(text,encoding="utf-8")
            print(text,end=""); return 0
        if args.cmd=="remove":
            idx=remove_document(load_index(args.index),args.document_id); write_index(idx,args.output)
            print(canonical_json({"status":"success","removed":args.document_id,"documents":len(idx["documents"])}),end=""); return 0
        idx=load_index(args.index); ok=verify_deleted(idx,args.document_id)
        print(canonical_json({"status":"success" if ok else "failure","document_id":args.document_id,"deleted":ok}),end=""); return 0 if ok else 5
    except (ValueError,KeyError,FileNotFoundError,json.JSONDecodeError) as exc:
        print(canonical_json({"status":"error","error":str(exc)}),end="",file=sys.stderr); return 2

if __name__=="__main__":
    raise SystemExit(main())
