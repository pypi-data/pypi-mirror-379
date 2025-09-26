#xfeed.py
from __future__ import annotations

import re
import json
from typing import ClassVar
from urllib.parse import urlparse

from truelink.exceptions import ExtractionFailedException
from truelink.types import LinkResult
from .base import BaseResolver


class XfeedResolver(BaseResolver):
    DOMAINS: ClassVar[list[str]] = ["xfeed.com", "www.xfeed.com"]

    async def resolve(self, url: str) -> LinkResult:
        async with await self._get(url, headers={"Referer": "https://xfeed.com/", "User-Agent": "Mozilla/5.0"}) as r:
            if r.status != 200:
                raise ExtractionFailedException(f"Xfeed HTTP {r.status}")
            html = await r.text()

        # Extract VIDEO_INFO block quickly
        m = re.search(r"window\.VIDEO_INFO\s*=\s*\{(.+?)\}\s*;", html, re.S)
        if not m:
            raise ExtractionFailedException("Xfeed: VIDEO_INFO not found")
        obj = "{" + m.group(1) + "}"

        # Normalize to JSON (quote keys, replace parseInt, unify quotes)
        obj = re.sub(r"(?<=\{|\s)([a-zA-Z_][a-zA-Z0-9_]*)\s*:", r'"\1":', obj)
        obj = re.sub(r'parseInt\("(\d+)"\)', r"\1", obj)
        obj = obj.replace("'", '"')

        try:
            vi = json.loads(obj)
        except Exception:
            raise ExtractionFailedException("Xfeed: VIDEO_INFO parse failed")

        d_url = vi.get("d_url")
        if not d_url:
            raise ExtractionFailedException("Xfeed: d_url missing")
        if not d_url.startswith("/"):
            d_url = "/" + d_url

        # Prefer EMBED_URL host; fallback to VIDEO_INFO.embed_url; then default
        host = None
        m = re.search(r'window\.EMBED_URL\s*=\s*"([^"]+)"', html)
        if m:
            host = urlparse(m.group(1)).netloc
        elif vi.get("embed_url"):
            host = urlparse(vi["embed_url"]).netloc
        if not host:
            host = "vxf3d.cachefly.net"

        mp4 = f"https://{host}{d_url}"
        filename, size, mime = await self._fetch_file_details(mp4)
        return LinkResult(url=mp4, filename=filename, mime_type=mime, size=size)
