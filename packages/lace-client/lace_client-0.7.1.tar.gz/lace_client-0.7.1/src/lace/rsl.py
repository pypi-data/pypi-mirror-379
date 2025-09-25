"""Minimal RSL resolver for real runs (skipped in --dry-run).

Resolves RSL signals from domains via:
- /.well-known/rsl.json
- /rsl.json
- robots.txt (best-effort hints)
"""
from __future__ import annotations
import asyncio
from typing import Dict, Iterable
import httpx

DEFAULT_TIMEOUT = httpx.Timeout(2.5, connect=1.5)

async def _fetch_json(client: httpx.AsyncClient, url: str) -> dict | None:
    try:
        r = await client.get(url)
        if r.status_code == 200 and r.headers.get("content-type", "").startswith("application/json"):
            return r.json()
    except Exception:
        return None
    return None

async def resolve(domain: str) -> str:
    base = f"https://{domain}"
    async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT, follow_redirects=True) as client:
        for path in ("/.well-known/rsl.json", "/rsl.json"):
            data = await _fetch_json(client, base + path)
            if isinstance(data, dict):
                # minimal heuristic
                return data.get("policy", "unknown")
        # try robots.txt
        try:
            r = await client.get(base + "/robots.txt")
            if r.status_code == 200 and "rsl" in r.text.lower():
                return "robots-hint"
        except Exception:
            pass
    return "unknown"

async def resolve_many(domains: Iterable[str], limit: int = 10) -> Dict[str, str]:
    sem = asyncio.Semaphore(limit)
    results: Dict[str, str] = {}

    async def _one(d: str):
        async with sem:
            results[d] = await resolve(d)

    await asyncio.gather(*[_one(d) for d in domains])
    return results
