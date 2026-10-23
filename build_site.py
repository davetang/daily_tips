#!/usr/bin/env python3

import argparse
import datetime
import html
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from email.utils import format_datetime
from pathlib import Path

import yaml

from random_tip import DEFAULT_TIPS, load_tips

HERE = Path(__file__).resolve().parent
SITE_URL = "https://davetang.github.io/daily_tips/"
REPO_URL = "https://github.com/davetang/daily_tips"
FEED_ITEMS = 50
# Tags with fewer tips than this go behind a "more tags" toggle.
MIN_CHIP_COUNT = 5
REQUIRED = ("date", "tip", "explanation", "tags")
# The Markdown the tips use, which README.md renders: `code`, [text](url) and
# bare URLs, plus *emphasis* or _emphasis_ in the text between them. A code
# span is a run of backticks, then the shortest text up to a run of the same
# length; nothing inside it is touched.
INLINE = re.compile(
    r"(?<!`)(?P<ticks>`+)(?!`)(?P<code>.+?)(?<!`)(?P=ticks)(?!`)"
    r"|\[(?P<text>[^\]]+)\]\((?P<href>[^)\s]+)\)"
    r"|(?P<url>https?://[^\s<>]*[^\s<>.,;:!?)'\"])")
EMPHASIS = re.compile(r"(?<![*\w])\*(?=\S)(.+?)(?<=\S)\*(?![*\w])"
                      r"|(?<![_\w])_(?=\S)(.+?)(?<=\S)_(?![_\w])")
ATOM = "http://www.w3.org/2005/Atom"

def check(tips):
    """Return a list of problems with the tip entries; empty means valid."""
    errors = []
    seen = set()
    for i, entry in enumerate(tips, 1):
        if not isinstance(entry, dict):
            errors.append(f"entry {i}: not a mapping")
            continue
        where = f"entry {i} ({entry.get('date', 'no date')})"
        missing = [key for key in REQUIRED if not entry.get(key)]
        if missing:
            errors.append(f"{where}: missing {', '.join(missing)}")
            continue
        if type(entry["date"]) is not datetime.date:
            errors.append(f"{where}: date must be an unquoted YYYY-MM-DD")
        elif entry["date"] in seen:
            errors.append(f"{where}: duplicate date")
        seen.add(entry["date"])
        for key in ("tip", "explanation"):
            if not isinstance(entry[key], str):
                errors.append(f"{where}: {key} must be a string")
        tags = entry["tags"]
        if not isinstance(tags, list) or not all(isinstance(tag, str) for tag in tags):
            errors.append(f"{where}: tags must be a list like [shell, git]")
        else:
            for tag in tags:
                if tag != tag.lower() or tag.split() != [tag]:
                    errors.append(f"{where}: tag {tag!r} must be lowercase with no spaces")
    return errors

def emphasis_html(text):
    return EMPHASIS.sub(lambda m: f"<em>{m[1] or m[2]}</em>", html.escape(text))

def inline_html(text):
    """Escape text for HTML and render its Markdown: code, links and emphasis."""
    out = []
    pos = 0
    for match in INLINE.finditer(text):
        out.append(emphasis_html(text[pos:match.start()]))
        if match["code"] is not None:
            code = match["code"]
            # As in Markdown, ` `` ` is the code `` with the padding spaces removed.
            if code.startswith(" ") and code.endswith(" ") and code.strip():
                code = code[1:-1]
            out.append(f"<code>{html.escape(code)}</code>")
        elif match["href"]:
            out.append(f'<a href="{html.escape(match["href"])}">{inline_html(match["text"])}</a>')
        else:
            url = html.escape(match["url"])
            out.append(f'<a href="{url}">{url}</a>')
        pos = match.end()
    out.append(emphasis_html(text[pos:]))
    return "".join(out)

def plain_text(text):
    """Text for places that show no markup, such as feed titles: links become their text."""
    return INLINE.sub(lambda m: m["text"] if m["href"] else m[0], text)

def tag_button(tag, count=None):
    tag = html.escape(tag)
    if count is None:
        return f'<button type="button" class="tag" data-tag="{tag}">{tag}</button>'
    return (f'<button type="button" class="tag" data-tag="{tag}" aria-pressed="false">'
            f'{tag}<span class="count">{count}</span></button>')

def tip_html(entry):
    date = entry["date"].isoformat()
    tags = "".join(tag_button(tag) for tag in entry["tags"])
    return f"""<article class="tip" id="{date}" data-tags="{html.escape(' '.join(entry['tags']))}">
<p class="date"><a href="#{date}">{date}</a></p>
<h2>{inline_html(entry['tip'])}</h2>
<p>{inline_html(entry['explanation'])}</p>
<p class="tags">{tags}</p>
</article>"""

def page_html(tips):
    counts = Counter(tag for entry in tips for tag in entry["tags"])
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    common = "".join(tag_button(tag, n) for tag, n in ranked if n >= MIN_CHIP_COUNT)
    rare = [tag_button(tag, n) for tag, n in ranked if n < MIN_CHIP_COUNT]
    more = ""
    if rare:
        more = (f'<details class="more"><summary>{len(rare)} more tags</summary>'
                f'<div class="chips">{"".join(rare)}</div></details>')
    first = tips[-1]["date"].isoformat()
    body = "\n".join(tip_html(entry) for entry in tips)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Daily tips</title>
<meta name="description" content="{len(tips)} short tips on the shell, R, Linux, Vim, Git and more, one a day since {first}.">
<link rel="alternate" type="application/rss+xml" title="Daily tips" href="feed.xml">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>💡</text></svg>">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="page">
<header>
<h1>Daily tips</h1>
<p>One tip every day since {first}: {len(tips)} so far.
<a href="feed.xml">RSS feed</a> · <a href="{REPO_URL}">GitHub</a></p>
</header>
<section id="on-this-day" class="card" hidden>
<h2>On this day</h2>
<ul></ul>
</section>
<section class="controls" id="controls" hidden>
<div class="search-row">
<input type="search" id="search" placeholder="Search tips" aria-label="Search tips" autocomplete="off">
<button type="button" id="random">Random tip</button>
</div>
<div id="random-tip" class="card" aria-live="polite" hidden>
<button type="button" id="hide-random" aria-label="Hide random tip">×</button>
</div>
<div class="chips">{common}</div>
{more}
<p id="status" aria-live="polite"><span id="count"></span> <button type="button" id="clear" hidden>Show all</button></p>
</section>
<main>
{body}
</main>
</div>
<script src="script.js"></script>
</body>
</html>
"""

def feed_xml(tips, site_url):
    def pub_date(date):
        return format_datetime(datetime.datetime.combine(date, datetime.time(), datetime.timezone.utc))

    ET.register_namespace("atom", ATOM)
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    ET.SubElement(channel, "title").text = "Daily tips"
    ET.SubElement(channel, "link").text = site_url
    ET.SubElement(channel, "description").text = "One tip every day."
    ET.SubElement(channel, "language").text = "en"
    ET.SubElement(channel, "lastBuildDate").text = pub_date(tips[0]["date"])
    ET.SubElement(channel, f"{{{ATOM}}}link", href=f"{site_url}feed.xml",
                  rel="self", type="application/rss+xml")
    for entry in tips[:FEED_ITEMS]:
        link = f"{site_url}#{entry['date'].isoformat()}"
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = plain_text(entry["tip"])
        ET.SubElement(item, "link").text = link
        ET.SubElement(item, "guid").text = link
        ET.SubElement(item, "pubDate").text = pub_date(entry["date"])
        ET.SubElement(item, "description").text = (
            f"<p>{inline_html(entry['tip'])}</p>"
            f"<p>{inline_html(entry['explanation'])}</p>"
            f"<p>Tags: {', '.join(entry['tags'])}</p>")
        for tag in entry["tags"]:
            ET.SubElement(item, "category").text = tag
    ET.indent(rss)
    return ET.tostring(rss, encoding="unicode", xml_declaration=True) + "\n"

def main():
    parser = argparse.ArgumentParser(description="Build the tips website: index.html and an RSS feed.")
    parser.add_argument("tips", nargs="?", default=DEFAULT_TIPS, type=Path,
                        help="YAML file of tips (default: %(default)s)")
    parser.add_argument("-o", "--out", default=HERE / "_site", type=Path,
                        help="output directory (default: %(default)s)")
    parser.add_argument("--url", default=SITE_URL,
                        help="public URL of the site, used for links in the feed (default: %(default)s)")
    args = parser.parse_args()
    site_url = args.url.rstrip("/") + "/"

    try:
        tips = load_tips(args.tips)
    except (OSError, ValueError, yaml.YAMLError) as e:
        sys.exit(f"Error: {e}")
    errors = check(tips)
    if errors:
        sys.exit("Error: fix these entries in {}:\n  {}".format(args.tips, "\n  ".join(errors)))
    tips = sorted(tips, key=lambda entry: entry["date"], reverse=True)

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "index.html").write_text(page_html(tips), encoding="utf-8")
    (args.out / "feed.xml").write_text(feed_xml(tips, site_url), encoding="utf-8")
    for name in ("style.css", "script.js"):
        shutil.copyfile(HERE / "site" / name, args.out / name)
    print(f"Built {len(tips)} tips into {args.out}")

if __name__ == "__main__":
    main()
