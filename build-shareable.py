"""Bakes index.html into one self-contained file that can be shared as a link.

The page is normally served as four files. A shareable host has to receive a
single document, so this inlines the stylesheet, the script, and the SVGs as
data URIs, and drops the document wrapper the host supplies itself.

It is a build step rather than a hand-kept copy on purpose: a second copy of a
portfolio drifts from the first, and then neither is the one to trust.
"""

import base64
import io
import re
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "dist" / "portfolio.html"


def data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded}"


def build() -> str:
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    js = (ROOT / "main.js").read_text(encoding="utf-8")

    title = re.search(r"<title>(.*?)</title>", html, re.S).group(1).strip()

    # Everything between <body> and </body>; the host supplies the rest.
    body = re.search(r"<body>(.*)</body>", html, re.S).group(1)

    body = body.replace('<script src="./main.js"></script>', "")

    for src in re.findall(r'src="\./(assets/[^"]+)"', body):
        body = body.replace(f'src="./{src}"', f'src="{data_uri(ROOT / src)}"')

    remaining = re.findall(r'(?:src|href)="\./[^"]*"', body)
    if remaining:
        raise SystemExit(f"unresolved local references: {remaining}")

    document = f"<title>{title}</title>\n<style>\n{css}\n</style>\n{body}\n<script>\n{js}\n</script>\n"

    # Escaped to pure ASCII so the page cannot depend on the host declaring an
    # encoding. Korean text mis-decoded as latin-1 is unreadable, and the
    # document wrapper is supplied by the host, so there is no <meta charset>
    # of our own to add.
    return document.encode("ascii", "xmlcharrefreplace").decode("ascii")


OUT.parent.mkdir(exist_ok=True)
OUT.write_text(build(), encoding="utf-8")
print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB)")
