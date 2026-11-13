#!/usr/bin/env python3
"""Builds the GPS Navigator Hub pages from site-content.md.

Usage (from this folder):   python build.py
Edit text in site-content.md, rerun, refresh the browser. Standard library only.
District admin contacts live in data/district-admins.json.
"""
import html, json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.stdout.reconfigure(encoding="utf-8")

# ---------- content file ----------
def load_content(path):
    text = re.sub(r"<!--.*?-->", "", open(path, encoding="utf-8").read(), flags=re.S)
    pages, page, key = {}, None, None
    for line in text.splitlines():
        if line.startswith("# "):
            page, key = line[2:].strip(), None
            pages[page] = {}
        elif line.startswith("## ") and page:
            key = line[3:].strip()
            pages[page][key] = []
        elif page and key:
            pages[page][key].append(line)
    return {p: {k: "\n".join(v).strip() for k, v in d.items()} for p, d in pages.items()}

C = load_content(os.path.join(ROOT, "site-content.md"))
missing = []

def raw(page, key):
    try:
        return C[page][key]
    except KeyError:
        missing.append(f"{page}/{key}")
        return f"[missing: {page}/{key}]"

def inline(s):
    s = html.escape(s.replace("\\|", "|"), quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s

def txt(page, key):            # one line, inline formatting, no <p>
    return inline(raw(page, key).replace("\n", " "))

def block(page, key):          # paragraphs and bullet lists
    res, para, lis = [], [], []
    def flush():
        if para: res.append("<p>" + inline(" ".join(para)) + "</p>"); para.clear()
        if lis: res.append('<ul class="check">' + "".join(f"<li>{inline(x)}</li>" for x in lis) + "</ul>"); lis.clear()
    for line in raw(page, key).splitlines():
        if line.startswith("- "):
            if para: flush()
            lis.append(line[2:])
        elif line.strip():
            if lis: flush()
            para.append(line.strip())
        else:
            flush()
    flush()
    return "".join(res)

def items(page, key, n=None):  # list lines -> list of field lists
    rows = []
    for line in raw(page, key).splitlines():
        if line.startswith("- "):
            f = [x.strip() for x in line[2:].split(" | ")]
            rows.append(f)
    return rows

def esc(s):
    return html.escape(s, quote=True)

# ---------- shared chrome ----------
def guide_url(slug, kind):
    return f"viewer.html?g={slug}&amp;t={kind}"

def page(filename, title, body, extra_scripts=""):
    nav = "".join(
        f'<a href="{f[0]}"' + (' aria-current="page"' if f[0] == filename else "") + f">{inline(f[1])}</a>"
        for f in items("global", "nav")
    )
    foot_org = "<br>".join(inline(l) for l in raw("global", "footer.org").splitlines())
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} | {esc(raw('global','site.name'))}</title>
<link rel="stylesheet" href="styles.css">
</head>
<body{' class="viewer-page"' if filename == 'viewer.html' else ''}>
<a class="skip" href="#main">Skip to main content</a>
<header class="site-header"><div class="wrap">
  <a class="brand" href="index.html"><b>{txt('global','site.name')}</b><small>{txt('global','site.tagline')}</small></a>
  <nav class="nav" aria-label="Main">{nav}</nav>
</div></header>
<div class="banner"><b>{txt('global','banner.label')}</b> {txt('global','banner.text')}</div>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
  <div>{foot_org}<br>{txt('global','footer.contact')}</div>
  <div>{txt('global','footer.access')}</div>
</div></footer>
{extra_scripts}
<script src="site.js"></script>
</body>
</html>
"""

def video(vid, title):
    return (f'<div style="width: 100%; height: 0px; position: relative; padding-bottom: 56.250%;">'
            f'<iframe src="https://streamable.com/e/{vid}?quality=highest" title="{esc(title)}" frameborder="0" '
            f'width="100%" height="100%" allowfullscreen style="width: 100%; height: 100%; position: absolute;"></iframe></div>')

VIDEOS = {"overview": "nvw7of", "teacher": "z9iv2i", "admin": "4keut3"}

def districts_json():
    path = os.path.join(ROOT, "data", "district-admins.json")
    data = json.load(open(path, encoding="utf-8"))
    for d in data.values():
        for p in d:
            if not p["name"]:
                p["name"] = "District user administrator"
    return json.dumps(data, ensure_ascii=False)

def access_form(section=True):
    p = "index"
    card = f"""<div class="card access" data-access
   data-subject="{esc(raw(p,'access.mail.subject'))}" data-body="{esc(raw(p,'access.mail.body'))}">
  <h2>{txt(p,'access.title')}</h2>
  <p>{txt(p,'access.body')}</p>
  <div class="access-row">
    <label for="district">{txt(p,'access.select.label')}</label>
    <select id="district"><option value="">{txt(p,'access.select.placeholder')}</option></select>
    <a class="btn btn-navy disabled" id="district-btn" aria-disabled="true" href="#access">{txt(p,'access.button')}</a>
  </div>
  <p class="access-to" id="district-to" aria-live="polite"></p>
  <p class="access-none">{txt(p,'access.none')}</p>
</div>
<script type="application/json" id="districts">{districts_json()}</script>"""
    if not section:
        return f'<div id="access">{card}</div>'
    return f'<section class="alt" id="access"><div class="wrap">{card}</div></section>'

# ---------- pages ----------
def build_index():
    p = "index"
    cards = "".join(f'<div class="card"><h3>{inline(a)}</h3><p>{inline(b)}</p></div>' for a, b in items(p, "what.cards"))
    rows = ""
    for t, hrs, pct, n in items(p, "stats.rows"):
        detail = raw(p, "stats.row.detail").replace("{pct}", pct).replace("{n}", n)
        rows += (f'<div class="card statcard"><div class="stat">{inline(hrs)}</div>'
                 f'<div class="stat-label">{txt(p,"stats.rows.label")}</div>'
                 f'<h3>{inline(t)}</h3><p class="stat-n">{esc(detail)}</p></div>')
    def pane(kind, cls):
        feats = "".join(f'<span class="tag">{inline(f[0])}</span>' for f in items(p, f"pane.{kind}.features"))
        dest = "teacher-navigator.html" if kind == "teacher" else "admin-navigator.html"
        return f"""<article class="pane {cls}">
  <div class="pane-top"><span class="pill {kind}">{txt(p,f'pane.{kind}.label')}</span>
  <h3>{txt(p,f'pane.{kind}.hook')}</h3></div>
  <dl>
    <dt>Who it's for</dt><dd>{block(p,f'pane.{kind}.who')}</dd>
    <dt>What's inside</dt><dd><div class="tag-row">{feats}</div></dd>
    <dt>How to get access</dt><dd>{txt(p,f'pane.{kind}.access')}</dd>
  </dl>
  <div class="pane-foot"><a class="btn btn-navy" href="{dest}">{txt(p,f'pane.{kind}.learn')}</a></div>
</article>"""
    steps = "".join(f"<li>{inline(f[0])}</li>" for f in items(p, "start.steps"))
    body = f"""
<div class="hero"><div class="wrap hero-grid">
  <div>
    <span class="eyebrow">{txt(p,'hero.eyebrow')}</span>
    <h1>{txt(p,'hero.title')}</h1>
    <p class="lead">{txt(p,'hero.lead')}</p>
    <div class="btn-row">
      <a class="btn btn-gold" href="#navigators">{txt(p,'hero.button1')}</a>
      <a class="btn btn-ghost" href="#get-started">{txt(p,'hero.button2')}</a>
    </div>
    <figure class="hero-photo">
      <img src="assets/images/educator-collaboration.webp" alt="{esc(raw(p,'hero.photo.alt'))}">
      <figcaption>{txt(p,'hero.photo.credit')}</figcaption>
    </figure>
  </div>
  <div>
    {video(VIDEOS['overview'], 'GPS Overview video')}
    <p class="video-caption">{txt(p,'hero.video.caption')}</p>
  </div>
</div></div>

<section id="overview"><div class="wrap">
  <div class="overview">
    <div>
      <span class="eyebrow">{txt(p,'what.eyebrow')}</span><h2>{txt(p,'what.title')}</h2>
      {''.join(f'<p><b>{inline(a)}.</b> {inline(b)}</p>' for a, b in items(p, 'what.cards'))}
    </div>
    <div>
      <span class="eyebrow">{txt(p,'who.eyebrow')}</span><h2>{txt(p,'who.title')}</h2>
      <h3 class="mini">{txt(p,'who.teacher.label')}</h3>{block(p,'who.teacher')}
      <h3 class="mini">{txt(p,'who.admin.label')}</h3>{block(p,'who.admin')}
    </div>
    <div>
      <span class="eyebrow">{txt(p,'why.eyebrow')}</span><h2>{txt(p,'why.title')}</h2>
      {block(p,'why.list')}
    </div>
  </div>
</div></section>

<section class="alt" id="time"><div class="wrap">
  <div class="time-head">
    <div><h2>{txt(p,'stats.title')}</h2>{block(p,'stats.intro')}</div>
    <div class="time-total"><div class="stat big">{txt(p,'stats.total')}</div><p>{txt(p,'stats.total.label')}</p></div>
  </div>
  <div class="grid g4">{rows}</div>
  <p class="note">{txt(p,'stats.note')}</p>
</div></section>

<section id="navigators"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{txt(p,'navigators.eyebrow')}</span><h2>{txt(p,'navigators.title')}</h2>{block(p,'navigators.body')}</div>
  <div class="panes">{pane('teacher','teacher')}{pane('admin','admin')}</div>
</div></section>

<section class="alt" id="get-started"><div class="wrap">
  <div class="start-grid">
    <div>
      <span class="eyebrow">{txt(p,'start.eyebrow')}</span><h2>{txt(p,'start.title')}</h2>
      <ol class="steps">{steps}</ol>
      <p style="margin-top:20px">{txt(p,'start.help')}</p>
      <div class="btn-row"><a class="btn btn-navy" href="assets/how-to-access-gps.pdf" target="_blank" rel="noopener">{txt(p,'start.pdf')}</a></div>
    </div>
    <div>{access_form(section=False)}</div>
  </div>
</div></section>
"""
    return page("index.html", "Home", body)

def build_navigator(kind, filename, title, hero_class):
    p = kind
    steps = "".join(f"<li>{inline(f[0])}</li>" for f in items(p, "access.steps"))
    points = "".join(f'<span class="tag">{inline(f[0])}</span>' for f in items(p, "video.points"))
    gbtn = "".join(
        f'<a class="btn {"btn-navy" if i == 0 else "btn-ghost"}" href="{guide_url(s, t)}">{inline(l)}</a>'
        for i, (s, t, l) in enumerate(items(p, "guides.buttons"))
    )
    qs = ""
    for q, steps_s, slug, label in items(p, "questions"):
        lis = "".join(f"<li>{inline(x.strip())}</li>" for x in steps_s.split(";") if x.strip())
        qs += (f'<article class="card q"><h3>{inline(q)}</h3><ol class="plain">{lis}</ol>'
               f'<a href="{guide_url(slug, "one-pager")}">{inline(label)} →</a></article>')
    more = ""
    if "more" in C[p]:
        lis = "".join(f'<li><a href="{guide_url(sl, "one-pager")}">{inline(q)}</a> <span class="dash-inline">{inline(d)}</span></li>' for q, d, sl in items(p, "more"))
        more = f'<div class="more-box"><h3>{txt(p,"more.title")}</h3><ul class="more-list">{lis}</ul></div>'
    note = ('<p class="callout">' + txt(p, "questions.note") + '</p>') if "questions.note" in C[p] else ""
    body = f"""
<div class="page-hero {hero_class}"><div class="wrap hero-split">
  <div>
    <span class="eyebrow">{txt(p,'hero.eyebrow')}</span>
    <h1>{txt(p,'hero.title')}</h1>
    <p>{txt(p,'hero.lead')}</p>
    <div class="toc"><a href="#what">{txt(p,'what.title')}</a><a href="#who">{txt(p,'who.title')}</a><a href="#how">{txt(p,'access.title')}</a><a href="#start">{txt(p,'start.eyebrow')}</a><a href="#questions">{txt(p,'questions.eyebrow')}</a></div>
  </div>
  <figure class="sizzle"><img src="{esc(raw(p,'hero.image'))}" alt="{esc(raw(p,'hero.image.alt'))}"><figcaption>{txt(p,'hero.image.caption')}</figcaption></figure>
</div></div>

<section id="what"><div class="wrap grid g3">
  <div class="card"><h3>{txt(p,'what.title')}</h3>{block(p,'what.body')}</div>
  <div class="card" id="who"><h3>{txt(p,'who.title')}</h3>{block(p,'who.body')}</div>
  <div class="card" id="how"><h3>{txt(p,'access.title')}</h3><ol class="plain">{steps}</ol>{block(p,'access.note')}</div>
</div></section>

<section class="alt" id="start"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{txt(p,'start.eyebrow')}</span><h2>{txt(p,'start.title')}</h2></div>
  <div class="grid g2 video-split" style="align-items:center">
    <div>{video(VIDEOS[kind], raw(p,'video.title'))}</div>
    <div>
      <h3>{txt(p,'video.points.title')}</h3>
      <div class="tag-row">{points}</div>
      {block(p,'video.blurb')}
      <div class="btn-row"><a class="btn btn-gold" href="{esc(raw('global','portal.url'))}" target="_blank" rel="noopener">{txt(p,'login.button')}</a></div>
      <p style="margin-top:14px"><a href="#access">{txt(p,'request.link')}</a></p>
    </div>
  </div>
  <div class="btn-row">{gbtn}</div>
</div></section>

<section id="questions"><div class="wrap">
  <div class="section-head"><span class="eyebrow">{txt(p,'questions.eyebrow')}</span><h2>{txt(p,'questions.title')}</h2></div>
  <div class="grid g{min(len(items(p,'questions')),3)}">{qs}</div>
  {note}
  {more}
</div></section>
{access_form()}
"""
    return page(filename, title, body)

CATALOG = {}   # slug -> {title, types}

def build_library():
    p = "library"
    rows = items(p, "guides")
    total = len(rows)
    topics, navs, fmts = [], [], []
    for r in rows:
        for lst, v in ((topics, r[3]), (navs, r[1]), (fmts, r[2])):
            if v not in lst: lst.append(v)
    cards = ""
    for slug, nav, fmt, topic, title, desc in rows:
        kind = "guide" if fmt == "Interactive walkthrough" else "one-pager"
        CATALOG[slug] = {"title": title, "types": [kind]}
        text = esc((title + " " + desc + " " + topic + " " + nav + " " + fmt).lower())
        cards += (f'<article class="card resource-card" data-topic="{esc(topic)}" data-nav="{esc(nav)}" data-format="{esc(fmt)}" data-text="{text}">'
                  f'<span class="resource-format">{esc(fmt)}</span>'
                  f'<h3><a class="stretch" href="{guide_url(slug, kind)}">{inline(title)}</a></h3>'
                  f'<p>{inline(desc)}</p>'
                  f'<div class="tag-row"><span class="tag">{esc(topic)}</span><span class="tag">{esc(nav)}</span></div>'
                  f'<span class="open">{txt(p,"open.link")}</span></article>')
    tbtn = (f'<button type="button" class="topic-button" data-topic="" aria-pressed="true"><span>{txt(p,"topics.all")}</span><span class="count">{total}</span></button>' +
            "".join(f'<button type="button" class="topic-button" data-topic="{esc(t)}" aria-pressed="false"><span>{esc(t)}</span><span class="count">{sum(1 for r in rows if r[3]==t)}</span></button>' for t in topics))
    nopt = "".join(f'<option value="{esc(n)}">{esc(n)}</option>' for n in navs)
    fopt = "".join(f'<option value="{esc(f)}">{esc(f)}</option>' for f in fmts)
    lead = raw(p, "hero.lead").replace("{count}", str(total))
    body = f"""
<div class="library-hero"><div class="wrap">
  <span class="eyebrow">{txt(p,'hero.eyebrow')}</span><h1>{txt(p,'hero.title')}</h1><p>{inline(lead)}</p>
</div></div>
<section><div class="wrap">
  <div class="resource-layout">
    <aside class="topic-rail" aria-label="Resource topics">
      <details class="topic-picker" open><summary>{txt(p,'topics.title')}</summary><div class="topic-list">{tbtn}</div></details>
    </aside>
    <div id="lib" data-total="{total}" data-count="{esc(raw(p,'count.text'))}">
      <label class="search-label" for="q">{txt(p,'search.label')}</label>
      <input type="search" id="q" placeholder="{esc(raw(p,'search.label'))}">
      <div class="resource-filters">
        <label class="select-filter">{txt(p,'filter.navigator')}<select id="f-nav"><option value="">{txt(p,'filter.navigator.all')}</option>{nopt}</select></label>
        <label class="select-filter">{txt(p,'filter.format')}<select id="f-format"><option value="">{txt(p,'filter.format.all')}</option>{fopt}</select></label>
        <button type="button" class="btn btn-ghost" id="f-reset">{txt(p,'filter.reset')}</button>
      </div>
      <p class="result-count" id="count" aria-live="polite"></p>
      <div class="grid g2" id="list">{cards}</div>
      <p class="empty" id="empty">{txt(p,'empty')}</p>
    </div>
  </div>
</div></section>
"""
    return page("library.html", "Guide Library", body)

def build_viewer():
    p = "viewer"
    cat = json.dumps(CATALOG, ensure_ascii=False)
    labels = json.dumps({"one-pager": "One-pager", "guide": "Interactive guide"})
    body = f"""
<div class="viewer-bar"><div class="wrap">
  <a class="btn btn-ghost" href="library.html">{txt(p,'back')}</a>
  <h1 id="v-title"></h1>
  <div class="v-switch" id="v-switch"></div>
  <a id="v-new" href="#" target="_blank" rel="noopener">{txt(p,'newtab')}</a>
</div></div>
<iframe id="v-frame" title="Guide" class="v-frame"></iframe>
<p class="empty wrap" id="v-missing" style="display:none">{txt(p,'missing')}</p>
<script type="application/json" id="catalog">{cat}</script>
<script type="application/json" id="type-labels">{labels}</script>
"""
    return page("viewer.html", "Guide", body)

def main():
    out = {
        "index.html": build_index(),
        "teacher-navigator.html": build_navigator("teacher", "teacher-navigator.html", "Teacher Navigator", ""),
        "admin-navigator.html": build_navigator("admin", "admin-navigator.html", "Administrator Navigator", "admin"),
    }
    out["library.html"] = build_library()
    out["viewer.html"] = build_viewer()
    for name, content in out.items():
        open(os.path.join(ROOT, name), "w", encoding="utf-8").write(content)
        print("wrote", name)
    for slug, c in CATALOG.items():
        for t in c["types"]:
            f = os.path.join(ROOT, "guides", slug, ("guide" if t == "guide" else t) + ".html")
            if not os.path.exists(f):
                print("WARNING: missing guide file", f)
    if missing:
        print("WARNING: content keys not found:", ", ".join(sorted(set(missing))))

main()
