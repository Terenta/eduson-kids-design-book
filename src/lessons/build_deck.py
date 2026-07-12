# -*- coding: utf-8 -*-
"""Сборка урока вайб-кодинга в дизайн-системе Eduson Kids.

Запуск из src/lessons/:  PYTHONUTF8=1 python build_deck.py 10
Склеивает l{N}_part1..4.py -> ../../lessons/urok_{N}.html
"""
import importlib
import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from deck_template import render_deck

TITLES = {
    10: "Своё веб-приложение в интернете",
    11: "Как программы общаются с нейросетью",
    12: "Чат с AI, как в ChatGPT",
}

def main():
    n = int(sys.argv[1])
    slides = []
    for k in range(1, 5):
        mod = importlib.import_module('l%d_part%d' % (n, k))
        importlib.reload(mod)
        slides.extend(mod.SLIDES)
        print('  part%d: %d слайдов' % (k, len(mod.SLIDES)))

    assert len(slides) == 38, 'ожидалось 38 слайдов, получено %d' % len(slides)
    covers = sum(1 for s in slides if s.get('cls') == 'slide--violet')
    finals = sum(1 for s in slides if s.get('cls') == 'slide--green')
    assert covers >= 1, 'нет титульного слайда (cls slide--violet)'
    assert finals >= 1, 'нет финального слайда (cls slide--green)'

    html = render_deck(n, TITLES[n], slides)
    out_dir = os.path.normpath(os.path.join(HERE, '..', '..', 'lessons'))
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, 'urok_%d.html' % n)
    with io.open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('  ✓ %s  (%d слайдов, %s символов)' % (out, len(slides), format(len(html), ',')))
    print('OK')

if __name__ == '__main__':
    main()
