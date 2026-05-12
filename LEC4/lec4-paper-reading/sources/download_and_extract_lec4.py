from datetime import datetime, timezone
from pathlib import Path
import subprocess
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "sources" / "original-paper"
TXT = ROOT / "extracted_text"
PDFS = [
    "1905.09822v3.pdf",
    "2111.00082v6.pdf",
    "2207.13795v4.pdf",
    "2211.05838v6.pdf",
    "2310.10168v2.pdf",
    "2402.18736v2.pdf",
    "2402.19080v2.pdf",
    "2405.06081v1.pdf",
    "2501.17466v2.pdf",
    "2506.12947v1.pdf",
    "SimplePIM_pact23.pdf",
    "TOM-programmer-transparent-GPU-near-data-processing_isca16.pdf",
    "ambit-bulk-bitwise-dram_micro17.pdf",
    "cellular_logic-in-memory_arrays.pdf",
    "figaro-fine-grained-in-dram-data-relocation-and-caching_micro20.pdf",
    "in-dram-bulk-and-or-ieee_cal15.pdf",
    "lisa-dram_hpca16.pdf",
    "micro19-gao.pdf",
    "micro22-gao.pdf",
    "network-on-memory-data-copy_ieee-cal20.pdf",
    "pim-enabled-instructons-for-low-overhead-pim_isca15.pdf",
    "rowclone_micro13.pdf",
    "simdram_asplos21.pdf",
    "stone_logic_in_memory_1970.pdf",
]


def run(cmd):
    return subprocess.run(cmd, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout


def page_count(pdf):
    out = run(["pdfinfo", str(pdf)])
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise RuntimeError(f"could not determine pages for {pdf}")


def extract_pdf(pdf, url):
    pages = page_count(pdf)
    slug = pdf.stem
    out_path = TXT / f"{slug}.txt"
    accessed = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    chunks = [
        f"Source PDF: {pdf.resolve()}",
        f"GitHub URL: https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC4/original-paper/{pdf.name}",
        f"Raw URL: {url}",
        f"Accessed: {accessed}",
        "",
    ]
    for page in range(1, pages + 1):
        page_txt = TXT / f".tmp_{slug}_{page}.txt"
        subprocess.run(
            ["pdftotext", "-layout", "-f", str(page), "-l", str(page), str(pdf), str(page_txt)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        chunks.append(f"\n\n===== Page {page} =====\n")
        chunks.append(page_txt.read_text(encoding="utf-8", errors="replace"))
        page_txt.unlink(missing_ok=True)
    out_path.write_text("\n".join(chunks), encoding="utf-8")
    return pages


def main():
    SRC.mkdir(parents=True, exist_ok=True)
    TXT.mkdir(parents=True, exist_ok=True)
    base = "https://raw.githubusercontent.com/Yuntong-Hou/computer-architecture/main/LEC4/original-paper"
    total_pages = 0
    for name in PDFS:
        url = f"{base}/{urllib.request.pathname2url(name)}"
        pdf = SRC / name
        if not pdf.exists():
            print(f"downloading {name}")
            urllib.request.urlretrieve(url, pdf)
        pages = extract_pdf(pdf, url)
        total_pages += pages
        print(f"extracted {name}: {pages} pages")
    print(f"done: {len(PDFS)} PDFs, {total_pages} pages")


if __name__ == "__main__":
    main()
