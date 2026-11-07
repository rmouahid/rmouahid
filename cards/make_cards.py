"""Draw the project cards of the profile README, in a light and a dark theme.

Every figure is copied from a generated report of its repository; the link
next to each card in the README points to it.

    python cards/make_cards.py
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent
WIDTH, HEIGHT = 880, 228
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
THEMES = {
    "light": {"bg": "#ffffff", "border": "#d0d7de", "tile": "#f6f8fa", "text": "#1f2328", "muted": "#59636e", "accent": "#0969da"},
    "dark": {"bg": "#0d1117", "border": "#30363d", "tile": "#161b22", "text": "#e6edf3", "muted": "#9198a1", "accent": "#4493f8"},
}
PROJECTS = {
    "rag-agent": {
        "pitch": "Question answering over your own documents, with vector indexes written from scratch",
        "metrics": [
            ("432×", "faster than an exact scan", "recall@10 0.93, 100k chunks"),
            ("0.992", "recall@10 in 0.72 ms", "HNSW on SIFT1M 100k"),
            ("0.668", "nDCG@10", "BEIR SciFact, 300 questions"),
        ],
        "stack": "Python · numpy · FAISS · FastAPI · llama.cpp · Docker",
    },
    "intern-radar": {
        "pitch": "An internship watcher that runs unattended on a VPS, every day",
        "metrics": [
            ("103", "new offers a day", "from 119 companies"),
            ("$0.15", "LLM cost a day", "API price; 63 % cut by rules first"),
            ("3 min", "detection to Telegram", "median notification delay"),
        ],
        "stack": "Python · httpx · SQLite · LLM triage · systemd · Docker",
    },
    "NovIT": {
        "pitch": "An MCP server that brings the day's tech news into an AI assistant",
        "metrics": [
            ("2.0 s", "to collect every source", "median of 3 runs"),
            ("19", "open sources", "AI, security, engineering, law"),
            ("352", "automated tests", "incl. a real MCP client"),
        ],
        "stack": "Python · MCP · SQLite FTS5 · asyncio · Docker",
    },
}


def card(name: str, project: dict, c: dict) -> str:
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}"'
        f' font-family="{FONT}" role="img" aria-label="{escape(name)}: {escape(project["pitch"])}">',
        f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{HEIGHT - 1}" rx="10" fill="{c["bg"]}" stroke="{c["border"]}"/>',
        f'<text x="28" y="46" font-size="24" font-weight="600" fill="{c["accent"]}">{escape(name)}</text>',
        f'<text x="28" y="74" font-size="15" fill="{c["muted"]}">{escape(project["pitch"])}</text>',
    ]
    gap, left = 14, 28
    tile_w = (WIDTH - 2 * left - 2 * gap) / 3
    for i, (value, label, detail) in enumerate(project["metrics"]):
        x = left + i * (tile_w + gap)
        out += [
            f'<rect x="{x:.1f}" y="94" width="{tile_w:.1f}" height="92" rx="8" fill="{c["tile"]}"/>',
            f'<text x="{x + 16:.1f}" y="134" font-size="30" font-weight="700" fill="{c["text"]}">{escape(value)}</text>',
            f'<text x="{x + 16:.1f}" y="157" font-size="14" fill="{c["text"]}">{escape(label)}</text>',
            f'<text x="{x + 16:.1f}" y="176" font-size="12" fill="{c["muted"]}">{escape(detail)}</text>',
        ]
    out += [
        f'<text x="28" y="210" font-size="13" fill="{c["muted"]}">{escape(project["stack"])}</text>',
        "</svg>",
    ]
    return "\n".join(out) + "\n"


def main() -> None:
    for name, project in PROJECTS.items():
        for theme, colors in THEMES.items():
            (OUT / f"{name.lower()}-{theme}.svg").write_text(card(name, project, colors), encoding="utf-8")


if __name__ == "__main__":
    main()
