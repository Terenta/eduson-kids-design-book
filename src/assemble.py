# -*- coding: utf-8 -*-
"""Сборка index.html дизайн-бука из частей + SVG + интерактивных блоков.

Запуск из папки src/:  PYTHONUTF8=1 python assemble.py
Результат пишется в ../index.html (корень репозитория).
"""
import io, json, os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
PARTS_DIR = os.path.join(BASE, 'parts')
SVG_DIR = os.path.join(BASE, 'codex-svg')
OUT = os.path.normpath(os.path.join(BASE, '..', 'index.html'))

PART_ORDER = [
    'p00-head.html', 'p01-hero.html', 'p02-principles.html', 'p03-palette.html',
    'p04-type.html', 'p05-layout.html', 'p05d-decor.html', 'p06-components.html',
    'p07-slides.html', 'p08-interactive.html', 'p09-dodont.html', 'p10-assets.html',
    'p12-tail.html',
]

COMPONENT_ORDER = ['quiz-single', 'quiz-multi', 'true-false', 'code-output',
                   'fill-blank', 'flashcard', 'match-pairs', 'open-reveal']

def read(path):
    with io.open(path, 'r', encoding='utf-8') as f:
        return f.read()

def svg_inline(fname, style):
    """Читает SVG, убирает xml-декларацию, задаёт стиль корневому тегу."""
    s = read(os.path.join(SVG_DIR, fname)).strip()
    s = re.sub(r'^<\?xml[^>]*\?>\s*', '', s)
    s = s.replace('<svg ', '<svg style="%s" ' % style, 1)
    return s

html = '\n'.join(read(os.path.join(PARTS_DIR, p)) for p in PART_ORDER)

# --- SVG-ассеты ---
full = 'width:100%;height:100%;display:block'
icon = 'width:100%;height:auto;display:block'
html = html.replace('<!--BG_VIOLET_SVG-->', svg_inline('bg-orbit-violet.svg', full))
html = html.replace('<!--BG_GREEN_SVG-->', svg_inline('bg-orbit-green.svg', full))
html = html.replace('<!--WAVES_SVG-->', svg_inline('decor-waves-mint.svg', full))
html = html.replace('<!--WAVES_SVG2-->', svg_inline('decor-waves-mint.svg', full))
html = html.replace('<!--ICON_TROPHY_SVG-->', svg_inline(os.path.join('icons', 'trophy.svg'), icon))
html = html.replace('<!--ICON_HEART_SVG-->', svg_inline(os.path.join('icons', 'heart.svg'), icon))
html = html.replace('<!--ICON_STAR_SVG-->', svg_inline(os.path.join('icons', 'star.svg'), icon))
html = html.replace('<!--ICON_GEM_SVG-->', svg_inline(os.path.join('icons', 'gem.svg'), icon))

# --- Интерактивные блоки ---
with io.open(os.path.join(BASE, 'components.json'), 'r', encoding='utf-8') as f:
    comps = json.load(f)

by_slug = {c['slug']: c for c in comps}
ordered = [by_slug[s] for s in COMPONENT_ORDER if s in by_slug]
missing = [s for s in COMPONENT_ORDER if s not in by_slug]
if missing:
    print('ВНИМАНИЕ: нет блоков:', ', '.join(missing))

items, css_parts, js_parts = [], [], []
for i, c in enumerate(ordered, 1):
    items.append(
        '<div class="ib-item" id="tpl-%s">\n'
        '  <div class="ib-head"><span class="sec-num" style="background:var(--ek-violet);color:#fff">8.%d</span>'
        '<h3>%s</h3><span class="tag">%s</span></div>\n'
        '  <p class="ib-desc">%s</p>\n'
        '  <div class="ib-demo">\n%s\n  </div>\n'
        '</div>' % (c['slug'], i, c['title'], c['slug'], c['description'], c['html'])
    )
    css_parts.append('/* --- %s --- */\n%s' % (c['slug'], c['css']))
    js_parts.append(
        '/* --- %s --- */\ntry {\n%s\n} catch (e) { console.error("ib:%s", e); }'
        % (c['slug'], c['js'], c['slug'])
    )

html = html.replace('<!--COMPONENTS_HTML-->', '\n'.join(items))
html = html.replace('/*__COMPONENT_CSS__*/', '\n'.join(css_parts))
html = html.replace('/*__COMPONENT_JS__*/', '\n'.join(js_parts))

# --- Контроль: не осталось ли маркеров ---
leftovers = re.findall(r'<!--[A-Z_0-9]+-->|/\*__[A-Z_]+__\*/', html)
if leftovers:
    print('ВНИМАНИЕ: остались маркеры:', leftovers)

with io.open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)
print('OK:', OUT, len(html), 'символов,', len(ordered), 'интерактивных блоков')
