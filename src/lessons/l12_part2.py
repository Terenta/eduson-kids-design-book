# -*- coding: utf-8 -*-
SLIDES = [
    # 11 · КАК УСТРОЕН СТРИМ
    {"notes": "Разбираем цикл стрима после запущенной разминки. Главное: ответ приходит кусочками, каждый кусочек — chunk.choices[0].delta.content, копим их в answer. Не углубляйтесь в устройство chunks — достаточно понимания «кусочек за кусочком».",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как это работает</div>
    <h2>Стрим — это цикл <span class="acc">по кусочкам</span></h2>
  </div>
  <p>При <span class="code-chip">stream=True</span> ответ приходит не целиком, а маленькими <span class="hl">кусочками</span> (chunks). Мы идём по ним циклом и печатаем каждый сразу — текст «печатается» на глазах.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">answer = <span class="st">""</span>
<span class="kw">for</span> chunk <span class="kw">in</span> stream:
    piece = chunk.choices[0].delta.content <span class="kw">or</span> <span class="st">""</span>
    print(piece, end=<span class="st">""</span>, flush=True)   <span class="cm"># печатаем кусочек сразу</span>
    answer += piece                     <span class="cm"># и копим весь ответ</span>
print()</div>
  </div>
  <div class="ek-note"><span class="code-chip">delta.content</span> — очередной кусочек текста. Пишем <span class="code-chip">or ""</span>, потому что иногда кусочек пустой. Всё собранное складываем в <span class="code-chip">answer</span> — пригодится для памяти.</div>
</div>"""},

    # 12 · ПАМЯТЬ ДИАЛОГА
    {"notes": "Ключевой слайд урока: память живёт в списке messages. Свяжите с уроком 5: роли system и user уже знакомы, новое — assistant. Подчеркните, что каждый ответ нейросети нужно дописывать в messages, иначе модель забывает разговор.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как это работает</div>
    <h2>Память диалога — это список <span class="acc">messages</span></h2>
  </div>
  <p>Собеседник помнит разговор, потому что весь диалог лежит в <span class="hl">списке</span> <span class="code-chip">messages</span>. Роли <span class="code-chip">system</span> и <span class="code-chip">user</span> знакомы с урока 5 — сегодня добавляем <span class="code-chip">assistant</span>.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">messages = [
    {"role": <span class="st">"system"</span>, "content": <span class="st">"Ты дружелюбный собеседник по имени Макс, любишь космос."</span>},
]
messages.append({"role": <span class="st">"user"</span>, "content": user_text})
<span class="cm"># ... получили ответ ...</span>
messages.append({"role": <span class="st">"assistant"</span>, "content": answer})   <span class="cm"># память диалога</span></div>
  </div>
  <div class="ek-note ek-note--red">Главное правило: <b>каждый ответ дописываем в <span class="code-chip">messages</span> как <span class="code-chip">assistant</span></b>. Забыли — и модель видит только последний вопрос, отвечает без предыдущего контекста.</div>
</div>"""},

    # 13 · ЛИЧНОСТЬ ЧЕРЕЗ СИСТЕМНЫЙ ПРОМПТ
    {"notes": "Личность задаёт первое сообщение system. Чем детальнее (имя, стиль речи, интересы) — тем ярче характер во всех ответах. Свяжите с уроком 5: system-роль уже управляла тоном, теперь она задаёт целого собеседника. Анонсируйте: сегодня заведём четыре личности — учитель, друг, пират, философ.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как это работает</div>
    <h2>Личность задаёт <span class="acc">системный промпт</span></h2>
  </div>
  <p>Первое сообщение с ролью <span class="code-chip">system</span> — это <span class="hl">характер</span> собеседника. Оно управляет тоном всех ответов сразу, как режиссёр задаёт роль актёру.</p>
  <div class="vs">
    <div class="vs-col vs-col--plain">
      <h4>Коротко — нейтрально</h4>
      <p>«Ты собеседник» — отвечает нейтрально, без выраженного характера, как обычный бот.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>Детально — ярко</h4>
      <p>«Ты дружелюбный собеседник по имени <b>Макс</b>, любишь космос» — задаёт имя, стиль речи и интересы. Собеседник держится в образе.</p>
    </div>
  </div>
  <div class="ek-note">Чем детальнее <span class="code-chip">system</span> (имя, манера, увлечения) — тем выразительнее собеседник. Личность меняется <b>без единой правки кода</b> — только текстом промпта. Сегодня заведём четыре: <b>учитель, друг, пират, философ</b>.</div>
</div>"""},

    # 14 · ЦЕЛЬ
    {"notes": "Прочитайте цель вслух. Подчеркните обязательный минимум: собеседник печатает ответ постепенно, помнит разговор, а характер задаётся системным промптом. Меню из четырёх личностей и команды /start, /help, /clear — расширение для успевающих. Слева теория, справа практика.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Цель · что будет в конце</div>
    <h2><span class="acc">Цель</span> урока</h2>
  </div>
  <div class="ek-note">К 55-й минуте у каждого — свой AI-собеседник в терминале: ответы <b>появляются постепенно</b>, характер задаёт системный промпт, разговор он помнит через роли <span class="code-chip">system</span>/<span class="code-chip">user</span>/<span class="code-chip">assistant</span>. Если группа успевает, добавляем выбор одной из четырёх личностей — <b>учитель, друг, пират, философ</b>, — и команды <span class="code-chip">/start</span>, <span class="code-chip">/help</span>, <span class="code-chip">/clear</span>.</div>
  <div class="grid-2">
    <div class="info-card">
      <h3>Узнаете</h3>
      <ul class="clean">
        <li>Что такое стриминг и зачем <span class="code-chip">stream=True</span></li>
        <li>Как список <span class="code-chip">messages</span> хранит память диалога</li>
        <li>Как системный промпт задаёт личность собеседника</li>
        <li>Зачем чат-ботам команды управления: <span class="code-chip">/start</span>, <span class="code-chip">/help</span>, <span class="code-chip">/clear</span></li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Сделаете</h3>
      <ul class="clean">
        <li>Включите постепенную печать ответа</li>
        <li>Зададите личность через системный промпт</li>
        <li>Соберёте память диалога через роль <span class="code-chip">assistant</span></li>
        <li>Успеете — добавите меню личностей и команды чата</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 15 · ДЕМО
    {"notes": "Покажите готовую версию собеседника — соберите заранее. Выберите одну личность, задайте пару фраз при группе: пусть все увидят, как текст появляется постепенно, как собеседник помнит прошлую фразу и как команда /help показывает управление чатом.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Демо результата</div>
    <h2>Что <span class="acc">соберём</span> сегодня</h2>
  </div>
  <div class="term">
    <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
    <div class="term-body">💬 Выбери собеседника: 1 — учитель · 2 — друг · 3 — пират · 4 — философ
<span class="usr">Твой выбор: 3</span>
Пират: Йо-хо-хо! О чём потолкуем, юнга?

<span class="usr">Ты: Привет! Расскажи что-нибудь про Марс</span>
Пират: Арр! Марс — это... <span class="dim">(текст печатается по словам, как в ChatGPT)</span>

<span class="usr">Ты: А как он называется?</span>
Пират: Я же только что говорил, юнга, — Марс, Красная планета! <span class="dim">(помнит прошлую фразу)</span>

<span class="usr">Ты: /help</span>
Команды: /start — начать заново · /clear — стереть память · /help — список команд</div>
  </div>
  <p style="font-size:14.5px;color:var(--ek-gray)">Ответ <span class="hl">появляется постепенно</span>, личность выбрана из четырёх, команда <span class="code-chip">/help</span> показывает управление чатом, а вопрос «как он называется?» сработал, потому что собеседник <span class="hl">помнит</span> прошлую реплику.</p>
</div>"""},

    # 16 · ПАПКА И БИБЛИОТЕКА
    {"notes": "Подготовка: companion.py рядом с warmup.py. openai и python-dotenv стоят с урока 11, ставить ничего не нужно. Клиент создаём ровно как на уроке 11 — с base_url DeepSeek и ключом из .env.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Подготовка</div>
    <h2>Папка <span class="acc">lesson-12</span></h2>
  </div>
  <div class="grid-2">
    <div class="col">
      <ol class="steps steps--tight">
        <li><div>Папка <span class="code-chip">lesson-12</span> уже есть — в ней лежит <span class="code-chip">warmup.py</span> с разминки</div></li>
        <li><div>Создайте файл <span class="code-chip">companion.py</span></div></li>
        <li><div>Библиотеки <span class="code-chip">openai</span> и <span class="code-chip">python-dotenv</span> стоят с урока 11 — ставить ничего не нужно</div></li>
      </ol>
    </div>
    <div class="col">
      <div class="term">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
        <div class="term-body">D:/vibe-coding/lesson-12/
├── warmup.py
├── companion.py
└── .env</div>
      </div>
      <div class="ek-note ek-note--red" style="margin-top:14px">Если библиотека всё же не найдена — выполните <span class="code-chip">pip install openai python-dotenv</span>, как перед уроком 11.</div>
    </div>
  </div>
</div>"""},

    # 17 · ПРОМПТ #2 · КАРКАС СОБЕСЕДНИКА
    {"notes": "Скопировать промпт целиком в новый чат DeepSeek. Каркас — самый простой цикл вопрос-ответ: ввод пользователя, обычный запрос к модели без стрима, печать всего ответа целиком, выход по слову «выход». Ни стрима, ни памяти, ни детальной личности — всё это добавим дальше пятью правками.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #2 · стартовый</div>
    <h2><span class="acc">Каркас</span> собеседника</h2>
  </div>
  <div class="prompt-card" style="margin-top:10px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — <span class="hl">опытный Python-разработчик</span> и наставник школьника.
Напиши companion.py — AI-собеседник, который общается в терминале.

Сделай самый простой каркас на openai SDK (клиент с base_url DeepSeek, ключ из .env через python-dotenv):
- список messages начинается с одного системного сообщения (role system): «Ты дружелюбный собеседник»
- цикл общения: спросить ввод пользователя, добавить его как role user
- обычный ответ модели deepseek-chat через client.chat.completions.create (пока БЕЗ stream)
- напечатать весь ответ целиком одним print(response.choices[0].message.content)
- выход из цикла по слову «выход»

Пока не добавляй стриминг, память и меню — соберём это дальше по шагам.
Прокомментируй код для новичка. Ответь одним блоком кода.</div>
  </div>
</div>"""},

    # 18 · КЛЮЧ И ЗАПУСК
    {"notes": "Запуск каркаса. Ключ уже в .env с урока 11 — проверьте, что файл на месте. Дождитесь, пока у всех собеседник запустится и ответит на первую фразу. Ответ пока приходит целиком после паузы — это нормально, постепенную печать включим Правкой 1.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск каркаса</div>
    <h2>Проверяем <span class="acc">ключ</span> и запускаем</h2>
  </div>
  <ol class="steps steps--tight">
    <li><div>Скопируйте код из ответа DeepSeek в <span class="code-chip">companion.py</span></div></li>
    <li><div>Проверьте файл <span class="code-chip">.env</span> рядом — строка <span class="code-chip">DEEPSEEK_KEY=sk-...</span> с урока 11</div></li>
    <li><div>Сохраните файл (<span class="code-chip">Ctrl+S</span>)</div></li>
    <li><div>Выполните <span class="code-chip">python companion.py</span></div></li>
    <li><div>Напишите фразу — собеседник ответит <b>целиком после паузы</b></div></li>
  </ol>
  <div class="ek-note ek-note--red">Ключ <b>только в <span class="code-chip">.env</span></b>, не в коде. Это как пароль: на скриншотах для домашки его замазываем.</div>
</div>"""},

    # 19 · ПЕРВЫЙ ДИАЛОГ
    {"notes": "Момент урока: собеседник заработал, но пока совсем простой. Ответ приходит целиком после паузы — ни стриминга, ни характера, ни памяти, ни команд. Именно это узкое место дальше доработаем правками: постепенная печать, характер, память, а для успевающих — меню четырёх личностей и команды /start, /help, /clear. Не обещайте ученикам, что стрим или память уже работают.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Момент урока</div>
    <h2>Собеседник <span class="acc">заговорил</span></h2>
  </div>
  <p>Каркас работает: вы пишете фразу — собеседник отвечает. Но ответ пока приходит <span class="hl">целиком после паузы</span>, как в <span class="code-chip">writer.py</span> на прошлом уроке: экран молчит, а потом весь текст появляется сразу.</p>
  <div class="ek-note ek-note--green">Главное уже есть: <b>цикл вопрос-ответ работает</b>, модель отвечает, выход по слову «выход» срабатывает. Это фундамент, на который ляжет всё остальное.</div>
  <div class="ek-note">Собеседник пока без заданного характера, без памяти и без команд. Дальше правками сделаем его <b>похожим на полноценный чат</b>: постепенный ответ (стриминг), <b>характер</b> через системный промпт, <b>память</b> диалога, а для успевающих — <b>меню четырёх личностей</b> и команды <span class="code-chip">/start</span>, <span class="code-chip">/help</span>, <span class="code-chip">/clear</span>.</div>
</div>"""},
]
