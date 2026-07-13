# -*- coding: utf-8 -*-
SLIDES = [
    # 1 · ТИТУЛ
    {"cls": "slide--violet", "notes": "Поприветствуйте. Сегодня соберём личный дневник с автоматическими тегами: ученик пишет запись, а нейросеть подбирает теги и настроение. Новое — файлы и формат JSON: данные будем хранить структурированно, чтобы программа могла их искать и фильтровать. К концу урока у каждого будет рабочий дневник в терминале.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">J</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">S</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">O</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">N</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="cover-card">
      <div class="badge">Урок №7</div>
      <div class="card-top"><span class="win-dots"><i></i><i></i><i></i></span><span class="win-close"></span></div>
      <h1>Файлы и формат<br>JSON</h1>
      <p class="cover-sub">Соберём личный дневник: вы пишете запись, нейросеть подбирает теги и настроение, данные сохраняются структурированно в файле и находятся по тегу.</p>
      <div class="cover-chips"><span class="chip">Python</span><span class="chip chip--gray">Файлы</span><span class="chip chip--green">JSON</span><span class="chip chip--gray">DeepSeek API</span></div>
    </div>
  </div>"""},

    # 2 · ПЛАН (agenda)
    {"notes": "План. Теории даём ровно столько, сколько нужно для практики: к 12-й минуте каждый сохраняет и читает JSON-файл, к 30-й — запускает каркас дневника, где записи тегирует нейросеть. Дальше — 5 последовательных правок, как на прошлых уроках.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Agenda · план занятия</div>
    <h2>Как пройдут <span class="acc">60 минут</span></h2>
  </div>
  <div class="agenda">
    <div class="agenda-row"><span class="t">0–5</span><div><div class="tt">Разбор ДЗ</div><div class="dd">Смотрим доработанные игры: свой жанр, сундук, карта приключения.</div></div></div>
    <div class="agenda-row"><span class="t">5–12</span><div><div class="tt">Файлы и JSON</div><div class="dd">Коротко разбираем только то, что нужно для дневника.</div></div></div>
    <div class="agenda-row"><span class="t">12–20</span><div><div class="tt">Промпт-разминка</div><div class="dd">warmup.py: сохранить словарь в JSON и прочитать обратно.</div></div></div>
    <div class="agenda-row"><span class="t">20–30</span><div><div class="tt">Каркас дневника</div><div class="dd">Меню, функции и AI-теги к записям.</div></div></div>
    <div class="agenda-row"><span class="t">30–48</span><div><div class="tt">5 правок через диалог</div><div class="dd">Сохранение → AI-теги → показать записи → поиск → настроение и цвет.</div></div></div>
    <div class="agenda-row"><span class="t">48–55</span><div><div class="tt">Мини-вопросы и отладка</div><div class="dd">Читаем ошибки JSON, проверяем понимание.</div></div></div>
    <div class="agenda-row"><span class="t">55–60</span><div><div class="tt">Демо в группе</div><div class="dd">Каждый делает запись и ищет её по тегу.</div></div></div>
  </div>
</div>"""},

    # 3 · РАЗБОР ДЗ
    {"notes": "Откройте 1-2 доработанные игры (на весь блок 5 минут). Разбирайте диалог с нейросетью, а не только результат. Подведите к главному: сцены сохраняли в adventure.txt плоским текстом, поэтому такой файл трудно искать и фильтровать. Сегодня данные будем хранить так, чтобы программа могла с ними работать.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор ДЗ урока 6</div>
    <h2>Смотрим <span class="acc">доработанные игры</span></h2>
  </div>
  <p>Открываем 2–3 присланные игры и разбираем именно <span class="hl">диалог с нейросетью</span>: свой жанр, сундук с сокровищами, карту приключения.</p>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card">
      <h3>Что сработало</h3>
      <p>Точечные промпты: свой жанр через системную роль мастера, <span class="code-chip">open_chest()</span> через <span class="code-chip">random.choice</span>.</p>
    </div>
    <div class="info-card">
      <h3>Что переделывали</h3>
      <p>Где забыли «не трогай остальной код» — нейросеть заодно ломала рабочую функцию.</p>
    </div>
    <div class="info-card">
      <h3>Вывод</h3>
      <p>Сцены сохраняли в <span class="code-chip">adventure.txt</span> режимом <span class="code-chip">'a'</span> — но такой плоский текст нельзя искать. Сегодня научимся хранить с умом.</p>
    </div>
  </div>
</div>"""},

    # 4 · ИДЕЯ УРОКА
    {"notes": "Главная мысль: две новинки. Первая — структурированное хранение в JSON вместо плоского текста. Вторая — нейросеть помогает разметить данные: подбирает теги и настроение к записи. Ученик пишет дневник, DeepSeek работает как помощник по разметке текста.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Идея урока</div>
    <h2>Программа, которая <span class="acc">помнит и понимает</span></h2>
  </div>
  <p>На уроках 5–6 данные складывали <span class="hl">плоским текстом</span> (history.txt, adventure.txt) — но такой файл нельзя ни искать, ни разбирать.</p>
  <div class="ek-note" style="margin-top:6px">Сегодня две новинки: храним записи <b>структурированно в JSON</b> и используем нейросеть для <b>разметки</b> каждой записи. Вы пишете дневник, а DeepSeek читает запись и подбирает к ней теги и настроение.</div>
  <p>Идея урока 7: данные <b>храним в JSON</b>, <b>ищем по тегам</b>, а смысл записи помогает <b>определить нейросеть</b>.</p>
</div>"""},

    # 5 · ЧТО ТАКОЕ ФАЙЛ
    {"notes": "Быстрый recap: файл на диске переживает выключение программы, переменные — нет. Режимы 'r'/'w'/'a' знакомы по history.txt урока 5. Не углубляйтесь — это повторение, главное впереди.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Вспоминаем</div>
    <h2>Что такое <span class="acc">файл</span></h2>
  </div>
  <p>Файл на диске <span class="hl">переживает выключение программы</span>: переменные исчезают, а файл остаётся. С файлами вы работали на уроке 5 — дневник советчика в <span class="code-chip">history.txt</span>.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">with</span> open(<span class="st">"diary.txt"</span>, <span class="st">"w"</span>, encoding=<span class="st">"utf-8"</span>) <span class="kw">as</span> f:  <span class="cm"># 'w' — записать</span>
    f.write(<span class="st">"Первая запись"</span>)

<span class="kw">with</span> open(<span class="st">"diary.txt"</span>, <span class="st">"r"</span>, encoding=<span class="st">"utf-8"</span>) <span class="kw">as</span> f:  <span class="cm"># 'r' — прочитать</span>
    text = f.read()</div>
  </div>
  <div class="ek-note">Режимы: <span class="code-chip">'r'</span> — читать, <span class="code-chip">'w'</span> — переписать целиком, <span class="code-chip">'a'</span> — дописать в конец. Сегодня к простому тексту добавим <b>структуру</b>.</div>
</div>"""},

    # 6 · ЧЕМ ПЛОХ ПЛОСКИЙ ТЕКСТ (vs)
    {"notes": "Покажите разницу на примере: в history.txt сложно надёжно спросить «покажи записи про шахматы» — там строки одна за другой. JSON хранит каждую запись как набор полей, поэтому программа может искать и фильтровать данные. Это мотивация всего урока.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Зачем нам новое</div>
    <h2>Чем плох <span class="acc">плоский текст</span></h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>Плоский текст (.txt)</h4>
      <p>Строки идут одна за другой. Надёжно спросить «покажи записи с тегом шахматы» не получится — приходится искать вручную.</p>
      <p class="note">Так хранили советчик и игра.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>Структура (JSON)</h4>
      <p>Каждая запись — набор полей: дата, текст, теги. Программа умеет искать и фильтровать по любому полю.</p>
      <p class="note">Это соберём сегодня.</p>
    </div>
  </div>
  <p>Как только у данных появляется <b>структура</b>, программа начинает в них <b>разбираться</b>.</p>
</div>"""},

    # 7 · ЧТО ТАКОЕ JSON
    {"notes": "JSON — текстовый формат для структурированных данных. Ключевая мысль: он выглядит почти как словари и списки Python, которые дети уже видели в игре на уроке 6. Фигурные скобки — словарь, квадратные — список.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Новый формат</div>
    <h2>Что такое <span class="acc">JSON</span></h2>
  </div>
  <p>JSON — <span class="hl">текстовый формат для структурированных данных</span>. Выглядит почти как словари и списки Python, которые вы видели в игре.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JSON</span></div>
    <div class="code-body">{
  <span class="st">"date"</span>: <span class="st">"2026-06-12"</span>,
  <span class="st">"text"</span>: <span class="st">"Выиграл турнир по шахматам"</span>,
  <span class="st">"tags"</span>: [<span class="st">"шахматы"</span>, <span class="st">"победа"</span>]
}</div>
  </div>
  <div class="ek-note">Фигурные скобки <span class="code-chip">{ }</span> — как <b>словарь</b> (поле: значение), квадратные <span class="code-chip">[ ]</span> — как <b>список</b>. JSON читается и человеком, и программой.</div>
</div>"""},

    # 8 · ПРОМПТ #1 · РАЗМИНКА
    {"notes": "Без долгой подготовки: сразу просим у DeepSeek небольшой скрипт с JSON и запускаем. Промпт с ролью и форматом — техники урока 2 работают и здесь. Ученики копируют промпт целиком.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #1 · разминка</div>
    <h2>warmup.py за <span class="acc">две минуты</span></h2>
  </div>
  <p>Начнём с короткого скрипта: попросим DeepSeek показать сохранение JSON и сразу запустим результат в терминале.</p>
  <div class="prompt-card" style="margin-top:14px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — опытный Python-разработчик и наставник школьника. Напиши маленький скрипт warmup.py: создай словарь с полями имя, возраст и любимое хобби; сохрани его в файл profile.json через json.dump с ensure_ascii=False и indent=2; затем прочитай файл обратно через json.load и распечатай. Только стандартная библиотека — модуль json встроен в Python. Прокомментируй код для новичка и ответь одним блоком кода.</div>
  </div>
</div>"""},

    # 9 · ЗАПУСК И РАЗБОР
    {"notes": "Базовый шаг урока: дождитесь, пока у всех появится файл profile.json и прочитается обратно. На рабочем коде показываем три вещи: json.dump, json.load и ensure_ascii. Не переходите дальше, пока скрипт не запустился у каждого.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск и разбор</div>
    <h2>Сохраняем и читаем <span class="acc">JSON</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div>
      <ol class="steps steps--tight">
        <li>В <span class="code-chip">vibe-coding</span> создайте папку <span class="code-chip">lesson-07</span></li>
        <li>Создайте <span class="code-chip">warmup.py</span> и вставьте код из ответа</li>
        <li>Выполните <span class="code-chip">python warmup.py</span></li>
        <li>Откройте появившийся <span class="code-chip">profile.json</span> прямо в VS Code</li>
      </ol>
      <div class="ek-note ek-note--green">Файл <span class="code-chip">profile.json</span> читается глазами? JSON за пять минут — фундамент дневника готов.</div>
    </div>
    <div class="kv">
      <div class="kv-row"><div class="k">json.dump</div><div class="v">Сохранил словарь в файл.</div></div>
      <div class="kv-row"><div class="k">json.load</div><div class="v">Прочитал файл обратно в словарь.</div></div>
      <div class="kv-row"><div class="k">ensure_ascii=False</div><div class="v">Русские буквы остаются читаемыми.</div></div>
    </div>
  </div>
</div>"""},

    # 10 · TROUBLESHOOTING
    {"notes": "Коротко разберите три типичные проблемы запуска. Помогите исправить ошибки у всех: этот же JSON и эта же папка нужны дальше для дневника.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Типичные ситуации запуска</div>
    <h2>Если warmup.py <span class="acc">не запустился</span></h2>
  </div>
  <div class="grid-3" style="margin-top:8px">
    <div class="ek-note ek-note--red">
      <h3 style="margin-bottom:8px">FileNotFoundError</h3>
      <p>Пытаетесь прочитать файл, которого ещё нет. Сначала сохранение (<span class="code-chip">json.dump</span>), потом чтение — или проверьте имя файла.</p>
    </div>
    <div class="ek-note ek-note--red">
      <h3 style="margin-bottom:8px">JSONDecodeError</h3>
      <p>Файл пустой или испорчен. Удалите <span class="code-chip">profile.json</span> — он создастся заново при следующем запуске.</p>
    </div>
    <div class="ek-note ek-note--red">
      <h3 style="margin-bottom:8px">can't open file</h3>
      <p>Терминал смотрит в другую папку. Откройте папку <span class="code-chip">lesson-07</span> в VS Code и терминал заново.</p>
    </div>
  </div>
</div>"""},
]
