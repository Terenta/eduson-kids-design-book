# Стайлгайд: уроки вайб-кодинга в дизайн-системе Eduson Kids

Уроки 10–12 курса «Программирование с нейросетями» (13–15 лет, 60 минут) переверстываются из тёмного шаблона в светлую дизайн-систему Eduson Kids. **Контент берётся из готовых исходников** (`_l10..12_part*.py` курса) — он выверен методистами; вёрстка полностью новая. Драматургия 38 слайдов сохраняется 1:1.

## Формат файла-части (СТРОГО)

```python
# -*- coding: utf-8 -*-
SLIDES = [
    # N · НАЗВАНИЕ
    {"notes": "Заметка преподавателю.", "html": r"""<div class="sl-body">
...
</div>"""},
]
```

- `html` — ТОЛЬКО raw-строки `r"""..."""`, без f-строк, без `"""` внутри, не заканчивать `\`.
- `notes` — обычная строка, внутри только «ёлочки», БЕЗ ASCII-кавычек `"`.
- Файл обязан импортироваться: `from l10_part1 import SLIDES`.
- Число слайдов в части: part1 = 10, part2 = 9, part3 = 10, part4 = 9. Итого 38.
- Титульный слайд (только part1, слайд 1): ключ `"cls": "slide--violet"`. Финальный (только part4, слайд 38): `"cls": "slide--green"`. Остальные — без `cls` (контентные, белые).

## Слайд 1 · Титул (part1)

```python
{"cls": "slide--violet", "notes": "...", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">S</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">A</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">I</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">K</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="cover-card">
      <div class="badge">Урок №10</div>
      <div class="card-top"><span class="win-dots"><i></i><i></i><i></i></span><span class="win-close"></span></div>
      <h1>Заголовок урока</h1>
      <p class="cover-sub">Подзаголовок — что соберём и какой результат.</p>
      <div class="cover-chips"><span class="chip">Streamlit</span><span class="chip chip--green">DeepSeek API</span><span class="chip chip--gray">Streamlit Cloud</span></div>
    </div>
  </div>"""}
```

Иконки спрайта: `#ek-i-trophy`, `#ek-i-heart`, `#ek-i-star`, `#ek-i-gem`. Буквы на орбите — латиница по теме урока.

## Слайд 38 · Финал (part4)

```python
{"cls": "slide--green", "notes": "...", "html": r"""<div class="sl-orbit">…(как титул)…</div>
  <div class="cover-center">
    <div class="bubble">
      <h1>До встречи<br>на уроке 11!</h1>
      <p>Одной-двумя фразами: что сделали сегодня и что будет дальше.</p>
    </div>
  </div>"""}
```

## Контентный слайд (все остальные)

```html
<div class="sl-body">
  <h2>Заголовок с <span class="acc">акцентом</span></h2>
  …компоненты…
</div>
```

Плотность: сцена 1280×720 БЕЗ прокрутки — контент обязан помещаться. Максимум 1 крупный компонент (код/терминал/промпт) + 1–2 текстовых блока на слайд. Заголовок h2 — до 60 знаков.

## Маппинг компонентов (старый тёмный шаблон → Eduson Kids)

| Было (тёмный) | Стало (Eduson Kids) |
|---|---|
| `<div class="eyebrow">X</div>` | `<div class="q-label">X</div>` (над h2) |
| `<p class="lead">` | `<p>` (первый абзац после h2) |
| `<div class="card"><h3>…` | `<div class="info-card"><h3>…</h3>…</div>` |
| `card accent` | `<div class="ek-note">…</div>` |
| `card good` | `<div class="ek-note ek-note--green">…</div>` |
| `card warn` | `<div class="ek-note ek-note--red">…</div>` |
| `grid cols-2 / cols-3` | `grid-2` / `grid-3` |
| `check-list` | `ul.clean` |
| `num-list` / `step-card` | `ol.steps` (плотный вариант: `ol.steps.steps--tight`) |
| `kv-row (тёмный)` | `<div class="kv"><div class="kv-row"><div class="k">…</div><div class="v">…</div></div>…</div>` |
| `timeline (agenda)` | `<div class="agenda"><div class="agenda-row"><span class="t">0–5</span><div><div class="tt">Название</div><div class="dd">Описание</div></div></div>…</div>` |
| `vs-grid / vs-col minimal / detailed` | `<div class="vs"><div class="vs-col vs-col--plain"><h4>…</h4><p>…</p><p class="note">…</p></div><div class="vs-col vs-col--win">…</div></div>` |
| `prompt-box` (промпт к DeepSeek) | `<div class="prompt-card"><span class="pc-tag">→ Новый чат DeepSeek</span><div class="pc-text">…текст промпта…</div></div>`; для правок тег `→ В тот же чат` и модификатор `prompt-card prompt-card--copy` |
| `<pre><code class="language-python">` | `<div class="code-win"><div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div><div class="code-body">…код…</div></div>` |
| `<pre><code class="language-bash">` (терминальные сессии) | `<div class="term"><div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div><div class="term-body">…вывод…</div></div>` |
| quiz-card + details | `<div class="quiz-box"><span class="q-num">Вопрос 1</span><p class="q-text">…</p><div class="quiz-answer"><button class="quiz-btn" type="button">Показать ответ</button><div class="quiz-reveal"><p>…</p></div></div></div>` |
| `badge neutral/primary/cyan/good` (чипы) | `chip` / `chip chip--green` / `chip chip--gray` |
| `<em>термин</em>` | `<span class="hl">термин</span>` |
| `<strong>` | `<b>` или `<span class="hl">` |
| `<code class="inline">x</code>` | `<span class="code-chip">x</span>` |
| вывод/результат в тексте | `<span class="out-chip">…</span>` |

## Правила кода и текста

- Внутри `.code-body`, `.term-body`, `.pc-text` содержимое РОВНО как в исходнике (код и промпты не менять!). Экранируй `<` → `&lt;`, `>` → `&gt;`, `&` → `&amp;`. Отступы кода сохраняются (white-space:pre).
- В `.code-body` можно (не обязательно) подсветить: комментарии `<span class="cm"># …</span>`, строки `<span class="st">"…"</span>`, ключевые слова `<span class="kw">def</span>`.
- В `.term-body` ввод пользователя можно выделить `<span class="usr">…</span>`, приглушённое — `<span class="dim">…</span>`.
- Тексты слайдов: вы/мы-форма, «ты» только внутри промптов к нейросети. Типографика: «ёлочки», тире —. Термины: DeepSeek, VS Code, Streamlit, GitHub, Streamlit Cloud, openai SDK, папка vibe-coding/lesson-NN.
- Плотность текста как в исходнике: НЕ сокращать сути (глубина сохраняется), но резать воду можно.

## Драматургия (38 слайдов, как в исходных уроках)

part1 (1–10): титул → план (agenda) → разбор ДЗ → идея урока → 2–3 слайда теории → промпт-разминка → запуск → troubleshooting.
part2 (11–19): теория темы → цель (Узнаете/Сделаете в grid-2 с ul.clean) → демо (term) → папка/установка → стартовый промпт #2 → ключ и запуск → первый результат.
part3 (20–29): troubleshooting → Правки 1–4, каждая с разбором.
part4 (30–38): Правка 5 → разбор → квиз 1 → квиз 2 → отладка → привычки (kv) → чек-лист (grid-2 + ul.clean) → ДЗ (grid-3 из info-card) → финал (green bubble).

## Особые требования плана курса (обязательны)

- **Урок 10** «Своё веб-приложение в интернете»: акцент финала — публичная ссылка, которой можно делиться; Streamlit как способ сделать веб-страницу на Python без HTML.
- **Урок 11** «Как программы общаются с нейросетью»: openai SDK, temperature и max_tokens («длина и креативность ответов»), проект — «программа-журналист».
- **Урок 12** «Чат с AI, как в ChatGPT»: стриминг (ответ по словам), системный промпт-личность, **личности на выбор: учитель / друг / пират / философ** (ровно эти четыре) и **команды управления чатом: /start, /help, /clear** (вместо «выход» — команды как в настоящих ботах; выход — /exit или пустая строка + Ctrl+C, реши по контенту исходника, но /start /help /clear обязаны появиться в правках).
