#!/usr/bin/env python3
"""Scans folders next to this file and writes catalog.js.

  <category folder>/<subcategory>.txt   -> one link per line
Line formats:   URL     or     Title | URL     ( # = comment )
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SKIP = {"node_modules", "assets", "docs", "__pycache__"}
YT = re.compile(r"(?:youtu\.be/|youtube\.com/(?:watch\?(?:.*&)?v=|embed/|shorts/|live/))([\w-]{11})")

def natural(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]

def parse(path):
    links = []
    with open(path, encoding="utf-8-sig") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            title, url = "", line
            if "|" in line:
                title, url = [p.strip() for p in line.rsplit("|", 1)]
            if not re.match(r"https?://", url):
                continue
            m = YT.search(url)
            links.append({"title": title, "url": url, "id": m.group(1) if m else ""})
    return links

catalog = []
for cat in sorted(os.listdir(ROOT), key=natural):
    p = os.path.join(ROOT, cat)
    if not os.path.isdir(p) or cat.startswith(".") or cat.startswith("_") or cat in SKIP:
        continue
    lists = []
    for fn in sorted(os.listdir(p), key=natural):
        if fn.lower().endswith(".txt"):
            lists.append({"name": fn[:-4], "links": parse(os.path.join(p, fn))})
    if lists:
        catalog.append({"name": cat, "lists": lists})

with open(os.path.join(ROOT, "catalog.js"), "w", encoding="utf-8") as f:
    f.write("window.CATALOG = " + json.dumps(catalog, ensure_ascii=False, indent=1) + ";\n")
print("catalog.js: %d categories, %d lists, %d links" % (
    len(catalog), sum(len(c["lists"]) for c in catalog),
    sum(len(l["links"]) for c in catalog for l in c["lists"])))
