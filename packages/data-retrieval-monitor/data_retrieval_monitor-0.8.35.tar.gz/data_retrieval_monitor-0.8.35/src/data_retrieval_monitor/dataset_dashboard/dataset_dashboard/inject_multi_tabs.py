#!/usr/bin/env python3
import os
import json
import random
from pathlib import Path
from datetime import datetime, timezone
import requests
from typing import List, Dict, Tuple

# ---------- Config via env ----------
DASH_URL = os.getenv("DASH_URL", "http://127.0.0.1:8090/ingest_snapshot")
LOG_ROOT = Path(os.getenv("LOG_ROOT", "/tmp/drm-logs")).resolve()
OWNERS = [o.strip().lower() for o in os.getenv("OWNERS", "qsg,mkt,ops").split(",") if o.strip()]
NUM_PER_TAB = int(os.getenv("NUM_PER_TAB", "6"))        # entities per tab total (across all owners)
SEED = os.getenv("SEED")
random.seed(SEED)

# ---------- Tab/Status dictionaries ----------
TAB_IDS = ["data", "features", "alphas", "strategies"]

DATA_STAGES = ["archive", "stage", "enrich", "consolidate"]
DATA_STATUS_ORDER = ["failed", "overdue", "manual", "retrying", "running", "waiting", "succeeded", "queued", "allocated", "other"]
FEATURES_STATUS_ORDER = ["F-Stat-001", "F-Stat-002", "F-Stat-003", "other"]
ALPHAS_STATUS_ORDER    = ["A-Stat-001", "A-Stat-002", "A-Stat-003", "other"]
STRATS_STATUS_ORDER    = ["S-Stat-001", "S-Stat-002", "S-Stat-003", "other"]

def status_order_for_tab(tab: str) -> List[str]:
    t = (tab or "data").lower()
    if t == "features": return FEATURES_STATUS_ORDER
    if t == "alphas": return ALPHAS_STATUS_ORDER
    if t == "strategies": return STRATS_STATUS_ORDER
    return DATA_STATUS_ORDER

# ---------- Helpers ----------
def iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def mk_log(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(text, encoding="utf-8")

def pick(seq: List[str]) -> str:
    return random.choice(seq)

def make_chunk(status: str, abs_log: Path, proc_url: str, idx: int) -> Dict:
    """
    Use id='c{idx}', always 'c' (as requested).
    Log is absolute path so the dashboard can link via /logview/root or mem-cache.
    """
    return {
        "id": f"c{idx}",
        "status": status,
        "proc": proc_url,
        "log": str(abs_log),
    }

# ---------- Generators per tab ----------
def build_data_items(num_total: int) -> List[Dict]:
    """
    Data tab: has 4 stages, multiple chunks per stage.
    Distribute evenly across owners; entities are dataset-XXX.
    """
    items: List[Dict] = []
    if not OWNERS:
        return items

    per_owner = max(1, num_total // len(OWNERS))
    counter = 0

    for owner in OWNERS:
        for i in range(per_owner):
            dn = f"dataset-{counter:03d}"
            counter += 1
            mode = "live" if (i % 3) else "backfill"
            # one entry per stage (the store expects rows grouped by stage)
            for stg in DATA_STAGES:
                # make 2–5 chunks
                k = random.randint(2, 5)
                chunks = []
                for j in range(k):
                    status = pick(DATA_STATUS_ORDER)
                    # Create an absolute log file inside LOG_ROOT to benefit from log linker root serving
                    abs_log = (LOG_ROOT / "data" / dn / f"{stg}-{j}.log")
                    mk_log(abs_log, f"[{iso_now()}] {dn} {stg} chunk={j} status={status}\n")
                    proc = f"https://example.com/proc/{dn}/{stg}/{j}"
                    chunks.append(make_chunk(status, abs_log, proc, j))
                items.append({
                    "owner": owner,                 # keep lower-case for filters
                    "mode": mode,
                    "data_name": dn,
                    "stage": stg,                   # stage is real for Data tab
                    "chunks": chunks,
                    "errors": [],
                })
    return items

def build_simple_tab_items(tab: str, num_total: int) -> List[Dict]:
    """
    For Features / Alphas / Strategies:
    - Single 'status' column (we encode it under stage='status')
    - Entities named: feature-XXX / alpha-XXX / strategy-XXX
    - Multiple chunks per entity with tab-specific statuses
    """
    items: List[Dict] = []
    if not OWNERS:
        return items

    if tab == "features":
        base = "feature"
    elif tab == "alphas":
        base = "alpha"
    else:
        base = "strategy"

    statuses = status_order_for_tab(tab)
    per_owner = max(1, num_total // len(OWNERS))
    counter = 0

    for owner in OWNERS:
        for i in range(per_owner):
            name = f"{base}-{counter:03d}"
            counter += 1
            # 2–5 chunks total under a single pseudo-stage 'status'
            k = random.randint(2, 5)
            chunks = []
            for j in range(k):
                status = pick(statuses)
                abs_log = (LOG_ROOT / tab / name / f"status-{j}.log")
                mk_log(abs_log, f"[{iso_now()}] {tab}:{name} chunk={j} status={status}\n")
                proc = f"https://example.com/{tab}/proc/{name}/{j}"
                chunks.append(make_chunk(status, abs_log, proc, j))

            items.append({
                "owner": owner,
                "mode": "live",            # mode unused for these tabs; keep a value
                "data_name": name,         # label column on right table
                "stage": "status",         # single 'Status' column in UI
                "chunks": chunks,
                "errors": [],
            })
    return items

def make_tab_payload(tab: str, num_total: int) -> Tuple[Dict, Dict]:
    """Return (items, meta) for a given tab."""
    if tab == "data":
        items = build_data_items(num_total)
    else:
        items = build_simple_tab_items(tab, num_total)
    meta = {"env": "demo", "ingested_at": iso_now()}
    return items, meta

# ---------- POSTer ----------
def post_tab(tab: str, items: List[Dict], meta: Dict) -> Dict:
    payload = {"tab": tab, "snapshot": items, "meta": meta}
    resp = requests.post(DASH_URL, json=payload, timeout=20)
    try:
        body = resp.json()
    except Exception:
        body = {"raw": resp.text}
    print(f"[POST] {tab:<10} → {resp.status_code} {resp.reason}  body={body}")
    return payload

def main():
    print(f"DASH_URL={DASH_URL}")
    print(f"LOG_ROOT={LOG_ROOT}")
    LOG_ROOT.mkdir(parents=True, exist_ok=True)

    all_payloads = {"tabs": {}}
    for tab in TAB_IDS:
        items, meta = make_tab_payload(tab, NUM_PER_TAB)
        sent = post_tab(tab, items, meta)
        all_payloads["tabs"][tab] = sent

    # save a local copy of everything we sent
    out = Path("sample_payload.json")
    out.write_text(json.dumps(all_payloads, indent=2), encoding="utf-8")
    print(f"Saved {out.resolve()}")

if __name__ == "__main__":
    main()