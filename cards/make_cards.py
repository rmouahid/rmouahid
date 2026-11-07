"""Draw the project cards of the profile README, in a light and a dark theme.

Every figure is copied from a generated report of its repository; the link
next to each card in the README points to it.

    python cards/make_cards.py
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent
WIDTH, HEIGHT = 640, 250
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
THEMES = {
    "light": {"bg": "#ffffff", "border": "#d0d7de", "tile": "#f6f8fa", "text": "#1f2328", "muted": "#59636e", "accent": "#0969da"},
    "dark": {"bg": "#0d1117", "border": "#30363d", "tile": "#161b22", "text": "#e6edf3", "muted": "#9198a1", "accent": "#4493f8"},
}
# Little text, set large: on a phone the card shrinks to the screen width.
PROJECTS = {
    "rag-agent": {
        "pitch": "Q&A over your documents, vector indexes from scratch",
        "metrics": [("432×", "faster than exact"), ("0.992", "recall@10, 0.72 ms"), ("0.668", "nDCG@10, BEIR")],
        "stack": "numpy · FAISS · FastAPI · llama.cpp · Docker",
    },
    "intern-radar": {
        "pitch": "Internship watcher that runs every day on a VPS",
        "metrics": [("103", "offers a day"), ("$0.15", "LLM cost a day"), ("3 min", "to Telegram")],
        "stack": "httpx · SQLite · LLM triage · systemd · Docker",
    },
    "NovIT": {
        "pitch": "MCP server bringing tech news into AI assistants",
        "metrics": [("2.0 s", "full collection"), ("19", "open sources"), ("352", "tests")],
        "stack": "MCP · SQLite FTS5 · asyncio · Docker",
    },
}


def card(name: str, project: dict, c: dict) -> str:
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}"'
        f' font-family="{FONT}" role="img" aria-label="{escape(name)}: {escape(project["pitch"])}">',
        f'<rect x="1" y="1" width="{WIDTH - 2}" height="{HEIGHT - 2}" rx="14" fill="{c["bg"]}" stroke="{c["border"]}" stroke-width="2"/>',
        f'<text x="26" y="50" font-size="30" font-weight="700" fill="{c["accent"]}">{escape(name)}</text>',
        f'<text x="26" y="82" font-size="19" fill="{c["muted"]}">{escape(project["pitch"])}</text>',
    ]
    gap, left = 12, 26
    tile_w = (WIDTH - 2 * left - 2 * gap) / 3
    for i, (value, label) in enumerate(project["metrics"]):
        x = left + i * (tile_w + gap)
        out += [
            f'<rect x="{x:.1f}" y="102" width="{tile_w:.1f}" height="92" rx="10" fill="{c["tile"]}"/>',
            f'<text x="{x + 16:.1f}" y="148" font-size="38" font-weight="700" fill="{c["text"]}">{escape(value)}</text>',
            f'<text x="{x + 16:.1f}" y="178" font-size="17" fill="{c["muted"]}">{escape(label)}</text>',
        ]
    out += [
        f'<text x="26" y="228" font-size="17" fill="{c["muted"]}">{escape(project["stack"])}</text>',
        "</svg>",
    ]
    return "\n".join(out) + "\n"


def main() -> None:
    for name, project in PROJECTS.items():
        for theme, colors in THEMES.items():
            (OUT / f"{name.lower()}-{theme}.svg").write_text(card(name, project, colors), encoding="utf-8")


if __name__ == "__main__":
    main()
