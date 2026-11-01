from pathlib import Path
from site_common import ROOT
from pages_home import home
from pages_capabilities import capabilities
from pages_company import about, experience, contacts, requisites, privacy, error_404

PAGES = [
    ("index.html", home),
    ("about.html", about),
    ("capabilities.html", capabilities),
    ("experience.html", experience),
    ("contacts.html", contacts),
    ("requisites.html", requisites),
    ("privacy.html", privacy),
    ("404.html", error_404),
]

for filename, builder in PAGES:
    html = builder()
    (ROOT / filename).write_text(html, encoding="utf-8")
    print(f"{filename:20} {len(html):>7} bytes")

robots = """User-agent: *
Allow: /

# Sitemap: укажите абсолютный адрес после публикации
"""
(ROOT / "robots.txt").write_text(robots, encoding="utf-8")
print("robots.txt written")
