#!/usr/bin/env python3
import json
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MANIFEST_JSON = ROOT / "lec3_contents.json"
OUT_DIR = ROOT / "LEC3"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def download(url: str, target: Path, expected_size: int) -> str:
    if target.exists() and target.stat().st_size == expected_size:
        return "exists"

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "codex-paper-reading",
            "Accept": "application/pdf,*/*",
        },
    )

    last_error = None
    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                data = response.read()
            target.write_bytes(data)
            if expected_size and target.stat().st_size != expected_size:
                return f"downloaded_size_mismatch:{target.stat().st_size}!={expected_size}"
            return "downloaded"
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            time.sleep(attempt * 2)

    return f"failed:{last_error}"


def main() -> int:
    items = json.loads(MANIFEST_JSON.read_text(encoding="utf-8"))
    rows = ["name\tpath\tsize\thtml_url\tdownload_url\tstatus"]

    failed = 0
    for item in items:
        if item.get("type") != "file" or not item.get("name", "").lower().endswith(".pdf"):
            continue

        name = item["name"]
        target = OUT_DIR / name
        status = download(item["download_url"], target, int(item.get("size") or 0))
        if status.startswith("failed"):
            failed += 1
        rows.append(
            "\t".join(
                [
                    name,
                    item.get("path", ""),
                    str(item.get("size", "")),
                    item.get("html_url", ""),
                    item.get("download_url", ""),
                    status,
                ]
            )
        )

    (ROOT / "LEC3_manifest.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
