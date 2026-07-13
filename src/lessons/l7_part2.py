# -*- coding: utf-8 -*-
SLIDES = [
    # 11 · JSON похож на структуры Python
    {"notes": "Покажите, что JSON похож на Python-структуры. Не углубляйтесь в детали: главное, что словарь и список из Python можно сохранить в файл как JSON и прочитать обратно.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как это работает</div>
    <h2>JSON похож на структуры <span class="acc">Python</span></h2>
  </div>
  <p>JSON нужен, чтобы хранить <span class="hl">структуру</span> в обычном текстовом файле. Он похож на знакомые вам список и словарь.</p>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>Типы совпадают</h3>
      <p>Словарь <span class="code-chip">{ }</span> ↔ object, список <span class="code-chip">[ ]</span> ↔ array, строка ↔ string, число ↔ number, <span class="code-chip">True/False</span> ↔ true/false.</p>
    </div>
    <div class="info-card">
      <h3>Две команды</h3>
      <p>В файл — <span class="code-chip">json.dump</span> и <span class="code-chip">json.load</span> (ими и будем работать). А <span class="code-chip">dumps</span>/<span class="code-chip">loads</span> — то же самое, но со строкой в памяти.</p>
    </div>
  </div>
  <div class="ek-note" style="margin-top:8px">Один параметр обязателен для русского: <span class="code-chip">ensure_ascii=False</span>. Без него слово «шахматы» превратится в коды вроде <span class="code-chip">ш...</span>.</div>
</div>"""},

    # 12 · Дневник — это список словарей
    {"notes": "Структура дневника: список записей, каждая — словарь с полями. Свяжите с уроком 6: list и dict уже знакомы. entries.append добавляет запись в конец.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Структура дневника</div>
    <h2>Дневник — это <span class="acc">список словарей</span></h2>
  </div>
  <p>Каждая запись — <span class="hl">словарь</span> с полями, а весь дневник — <span class="hl">список</span> таких записей. Обе коллекции знакомы с урока 6.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">entries = [
    {<span class="st">"date"</span>: <span class="st">"2026-06-12"</span>,
     <span class="st">"text"</span>: <span class="st">"Выиграл турнир по шахматам"</span>,
     <span class="st">"tags"</span>: [<span class="st">"шахматы"</span>, <span class="st">"победа"</span>],
     <span class="st">"mood"</span>: <span class="st">"радость"</span>},
]

entries.append(new_entry)   <span class="cm"># добавить новую запись в конец списка</span></div>
  </div>
  <div class="ek-note" style="margin-top:8px"><span class="code-chip">entries</span> — <b>список</b> из урока 6, а каждая запись — <b>словарь</b> с полями <span class="code-chip">date</span>, <span class="code-chip">text</span>, <span class="code-chip">tags</span>, <span class="code-chip">mood</span>.</div>
</div>"""},

    # 13 · Нейросеть подбирает теги
    {"notes": "Новая роль DeepSeek: помощник по разметке дневника. Урок 5 — советчик, урок 6 — гейм-мастер, сегодня — разметка записей. Снова ключевую роль задаёт системное сообщение.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Новая роль нейросети</div>
    <h2>Нейросеть <span class="acc">подбирает теги</span></h2>
  </div>
  <p>На уроке 5 DeepSeek был <span class="hl">советчиком</span>, на уроке 6 — <span class="hl">гейм-мастером</span>. Сегодня его задача — прочитать запись и <span class="hl">разметить</span> её тегами.</p>
  <div class="info-card" style="margin-top:8px">
    <h3>Системная роль</h3>
    <p>«Ты помощник дневника. Прочитай запись и верни 3-5 тегов через запятую, одной строкой, без пояснений».</p>
  </div>
  <div class="ek-note" style="margin-top:8px">Видимый результат: пишете строку — нейросеть <b>подбирает теги</b>. Программа не только хранит запись, но и получает разметку её смысла.</div>
</div>"""},

    # 14 · Цель урока
    {"notes": "Прочитайте цель вслух. Подчеркните: теги и настроение подбирает нейросеть, поэтому дневник у каждого будет отличаться по содержанию. Слева теория, справа практика.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Goal · что будет в конце</div>
    <h2>Цель <span class="acc">урока</span></h2>
  </div>
  <div class="ek-note">К 55-й минуте у каждого — личный дневник в терминале: вы пишете запись, нейросеть подбирает теги и настроение, всё сохраняется в <span class="code-chip">diary.json</span>, а записи можно показать списком и найти по тегу.</div>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>Узнаете</h3>
      <ul class="clean">
        <li>Как файлы хранят данные между запусками программы</li>
        <li>Что такое JSON и сериализация</li>
        <li>Как список словарей хранит записи дневника</li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Сделаете</h3>
      <ul class="clean">
        <li>Сохраните данные в JSON-файл</li>
        <li>Подключите AI для подбора тегов</li>
        <li>Соберёте поиск по дневнику</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 15 · Что соберём сегодня (демо)
    {"notes": "Покажите заранее собранный дневник. Сделайте запись при группе, чтобы все увидели, как нейросеть подбирает теги и настроение.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Демо результата</div>
    <h2>Что соберём <span class="acc">сегодня</span></h2>
  </div>
  <div class="term">
    <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
    <div class="term-body">📔 Личный дневник
1 — новая запись   2 — показать все   3 — поиск   4 — выход
<span class="usr">&gt; 1</span>
Что запишем? <span class="usr">Выиграл турнир по шахматам, но поссорился с другом</span>
Нейросеть подобрала теги: шахматы, победа, дружба, ссора
Настроение: смешанное
Запись сохранена в diary.json</div>
  </div>
  <p style="margin-top:8px">Теги и настроение подобрала <span class="hl">нейросеть</span>; запись легла в <span class="code-chip">diary.json</span> структурой, а не строкой.</p>
</div>"""},

    # 16 · Папка lesson-07
    {"notes": "Подготовка: diary.py рядом с warmup.py. requests уже установлен с урока 6, json встроен в Python. Дополнительная установка не нужна, поэтому можно быстро перейти к каркасу.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Подготовка</div>
    <h2>Папка <span class="acc">lesson-07</span></h2>
  </div>
  <div class="grid-2" style="margin-top:8px">
    <div>
      <ol class="steps">
        <li>Папка <span class="code-chip">lesson-07</span> уже есть — в ней лежит <span class="code-chip">warmup.py</span></li>
        <li>Создайте файл <span class="code-chip">diary.py</span></li>
        <li>Библиотека <span class="code-chip">requests</span> стоит с урока 6, а модуль <span class="code-chip">json</span> встроен в Python — ставить ничего не нужно</li>
      </ol>
    </div>
    <div>
      <div class="term">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
        <div class="term-body">D:/vibe-coding/lesson-07/
├── warmup.py
└── diary.py</div>
      </div>
      <div class="ek-note ek-note--red" style="margin-top:8px">Если <span class="code-chip">requests</span> всё же не найден — выполните <span class="code-chip">pip install requests</span>, как на уроке 6.</div>
    </div>
  </div>
</div>"""},

    # 17 · Каркас дневника (промпт #2)
    {"notes": "Скопируйте промпт целиком в новый чат DeepSeek. Каркас пока минимальный, но с правильной структурой из функций — как на уроке 6. Дальше будем наполнять функции отдельными правками.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #2 · стартовый</div>
    <h2>Каркас <span class="acc">дневника</span></h2>
  </div>
  <div class="prompt-card" style="margin-top:8px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — опытный Python-разработчик и наставник школьника. Напиши diary.py — личный дневник, который запускается в терминале.

Каркас:
- меню в цикле с пунктами: 1 — новая запись, 2 — показать все, 3 — поиск по тегу, 4 — выход
- раздели программу на функции: add_entry, show_all, search, main
- пока «новая запись» просто спрашивает текст и печатает его — сохранение в JSON и теги добавим следующими шагами

Ключ для будущих запросов положи в константу API_KEY в начале файла. Прокомментируй код для новичка. Ответь одним блоком кода.</div>
  </div>
</div>"""},

    # 18 · Вставляем ключ и запускаем
    {"notes": "Запустите каркас. Ключ понадобится на шаге с тегами, поэтому ученики вставляют его сразу. Дождитесь, пока у всех откроется меню и пункты переключаются.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск каркаса</div>
    <h2>Вставляем ключ и <span class="acc">запускаем</span></h2>
  </div>
  <ol class="steps" style="margin-top:8px">
    <li>Скопируйте код из ответа DeepSeek в <span class="code-chip">diary.py</span></li>
    <li>Замените <span class="code-chip">sk-...</span> на ключ, который выдал преподаватель — он пригодится для тегов</li>
    <li>Сохраните файл (<span class="code-chip">Ctrl+S</span>)</li>
    <li>Выполните <span class="code-chip">python diary.py</span></li>
    <li>Проверьте, что меню открывается и пункты переключаются</li>
  </ol>
  <div class="ek-note ek-note--red" style="margin-top:8px">Ключ — <b>в кавычках и без пробелов</b>. На скриншотах для домашки ключ замазываем.</div>
</div>"""},

    # 19 · Каркас готов: структура правильная
    {"notes": "Зафиксируйте промежуточный результат: программа уже разделена на функции, как на уроке 6. Каркас пока минимальный, но структура правильная. Дальше наполняем функции по одной.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Момент урока</div>
    <h2>Каркас готов: структура <span class="acc">правильная</span></h2>
  </div>
  <p>Меню работает, а программа уже <span class="hl">разделена на функции</span> — ровно как учились на уроке 6. Осталось наполнить каждую функцию.</p>
  <div class="ek-note ek-note--green" style="margin-top:8px">Каждый пункт меню — <b>отдельная функция</b>: <span class="code-chip">add_entry</span>, <span class="code-chip">show_all</span>, <span class="code-chip">search</span>. Дальше наполним их по одной через правки.</div>
  <div class="ek-note" style="margin-top:8px">Каркас пока минимальный, но <b>структура правильная</b> — добавлять функции в такую программу проще.</div>
</div>"""},
]
