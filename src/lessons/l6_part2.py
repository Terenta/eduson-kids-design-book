# -*- coding: utf-8 -*-
SLIDES = [
    # 11 · Список и словарь
    {"notes": "Вводим две коллекции. Список — как рюкзак с вещами по порядку, словарь — как анкета с подписанными полями. Не углубляйтесь: главное, что игре нужно где-то хранить состояние.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Новый инструмент</div>
    <h2>Список и <span class="acc">словарь</span></h2>
  </div>
  <p>Чтобы игра помнила, что происходит с героем, ей нужно <span class="hl">хранилище</span>. В Python их два главных: список и словарь.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">inventory = [<span class="st">"факел"</span>, <span class="st">"ключ"</span>]          <span class="cm"># список (list) — набор по порядку</span>
state = {<span class="st">"hp"</span>: 100, <span class="st">"name"</span>: <span class="st">"Артём"</span>}   <span class="cm"># словарь (dict) — пары ключ-значение</span>
print(state[<span class="st">"hp"</span>])                      <span class="cm"># 100 — берём значение по ключу</span></div>
  </div>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>Список</h3>
      <p>Набор значений по порядку, в квадратных скобках <span class="code-chip">[ ]</span> через запятую. Удобно для инвентаря.</p>
    </div>
    <div class="info-card">
      <h3>Словарь</h3>
      <p>Пары <span class="hl">«ключ»: значение</span> в фигурных скобках <span class="code-chip">{ }</span>. Значение достаём по ключу: <span class="code-chip">state["hp"]</span>.</p>
    </div>
  </div>
</div>"""},

    # 12 · Один словарь — вся память игры
    {"notes": "Покажите, что один словарь state хранит всю память героя. -= уменьшает число, .append добавляет в список. Это понадобится в правке 4.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Память героя</div>
    <h2>Один словарь — <span class="acc">вся память</span> игры</h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">state = {<span class="st">"hp"</span>: 100, <span class="st">"inventory"</span>: []}

state[<span class="st">"hp"</span>] -= 20                  <span class="cm"># получили урон — стало 80</span>
state[<span class="st">"inventory"</span>].append(<span class="st">"меч"</span>)   <span class="cm"># нашли предмет — он в рюкзаке</span></div>
  </div>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>Меняем число</h3>
      <p><span class="code-chip">-=</span> уменьшает значение. Так у героя убывает здоровье.</p>
    </div>
    <div class="info-card">
      <h3>Добавляем в список</h3>
      <p><span class="code-chip">.append(...)</span> кладёт предмет в конец инвентаря.</p>
    </div>
  </div>
  <div class="ek-note">Весь прогресс героя — <b>жив ли он и что у него есть</b> — лежит в одном словаре <span class="code-chip">state</span>.</div>
</div>"""},

    # 13 · Нейросеть в роли гейм-мастера
    {"notes": "Напомните урок 5: программа уже умеет вызывать DeepSeek через requests. Новое — системная роль делает из нейросети мастера игры. Подчеркните: меняешь роль — меняется мир.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как это работает</div>
    <h2>Нейросеть в роли <span class="acc">гейм-мастера</span></h2>
  </div>
  <p>На уроке 5 наша программа уже разговаривала с DeepSeek через <span class="code-chip">requests</span>. Сегодня — то же самое, но <span class="hl">системная роль</span> превращает нейросеть в мастера игры.</p>
  <div class="info-card" style="margin-top:8px">
    <h3>Системная роль</h3>
    <p>«Ты — мастер ролевой игры. Веди игрока по подземелью, описывай сцену и заканчивай тремя вариантами действий».</p>
  </div>
  <div class="ek-note">Меняешь системную роль — <b>меняется весь мир игры</b>: подземелье, космос или сказка. Промпт живёт внутри программы.</div>
</div>"""},

    # 14 · Цель урока
    {"notes": "Прочитайте цель вслух. Подчеркните: сцены генерирует нейросеть, поэтому приключение у каждого своё. Узнаёте слева — теория, делаете справа — практика.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Goal · что будет в конце</div>
    <h2>Цель <span class="acc">урока</span></h2>
  </div>
  <div class="ek-note ek-note--green">К 55-й минуте у каждого — играбельное приключение в терминале: нейросеть генерирует сцены подземелья, вы выбираете действия, у героя есть HP и инвентарь, игра идёт до победы или гибели.</div>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>Узнаете</h3>
      <ul class="clean">
        <li>Что такое функции <span class="code-chip">def</span> и зачем делить программу на части</li>
        <li>Как работают циклы <span class="code-chip">while</span> и <span class="code-chip">for</span></li>
        <li>Как списки и словари хранят состояние игры</li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Сделаете</h3>
      <ul class="clean">
        <li>Соберёте движок игры</li>
        <li>Сделаете DeepSeek гейм-мастером игры</li>
        <li>Сыграете в собственную игру</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 15 · Что соберём сегодня (демо)
    {"notes": "Покажите живой запуск игры — соберите заранее. Сделайте пару ходов, чтобы группа увидела, как мастер придумывает сцену под выбор игрока.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Демо результата</div>
    <h2>Что соберём <span class="acc">сегодня</span></h2>
  </div>
  <div class="term">
    <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
    <div class="term-body">⚔️ ПОДЗЕМЕЛЬЯ И ДРАКОНЫ
Имя героя: <span class="usr">Артём</span>
Артём, ты у входа в тёмную пещеру. С потолка капает вода, вдалеке рык.
1 — войти внутрь   2 — осмотреться   3 — позвать на помощь
&gt; <span class="usr">1</span>
Факел освещает кости на полу и блеск золота. Из мрака выходит
гоблин с ржавым кинжалом.
❤️ HP: 100   🎒 факел
1 — атаковать   2 — отступить   3 — бросить золото
&gt; <span class="usr">...</span></div>
  </div>
  <p style="margin-top:8px">Каждую сцену придумывает <span class="hl">нейросеть</span> — приключение у каждого в классе своё.</p>
</div>"""},

    # 16 · Папка lesson-06 и requests
    {"notes": "Подготовка: game.py рядом с warmup.py, затем pip install requests. Если ставили на уроке 5 — pip напишет already satisfied. Дождитесь, пока установка пройдёт у всех.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Подготовка</div>
    <h2>Папка lesson-06 и <span class="acc">requests</span></h2>
  </div>
  <div class="grid-2">
    <div>
      <ol class="steps">
        <li>Папка <span class="code-chip">lesson-06</span> уже есть — в ней лежит <span class="code-chip">warmup.py</span></li>
        <li>Создайте файл <span class="code-chip">game.py</span></li>
        <li>В терминале выполните <span class="code-chip">pip install requests</span> — библиотека для запросов в интернет</li>
      </ol>
    </div>
    <div>
      <div class="term">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ПАПКА</span></div>
        <div class="term-body">D:/vibe-coding/lesson-06/
├── warmup.py
└── game.py</div>
      </div>
      <div class="ek-note ek-note--red">Если <span class="code-chip">requests</span> уже ставили на уроке 5 — <span class="code-chip">pip</span> напишет <span class="out-chip">Requirement already satisfied</span>. Это нормально.</div>
    </div>
  </div>
</div>"""},

    # 17 · Каркас игры (промпт #2)
    {"notes": "Скопировать промпт целиком в новый чат DeepSeek. url и модель уже в промпте — нейросеть соберёт рабочий запрос сама. Первая сцена приходит от мастера.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #2 · стартовый</div>
    <h2>Каркас <span class="acc">игры</span></h2>
  </div>
  <div class="prompt-card">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — <span class="hl">опытный Python-разработчик</span>.
Напиши game.py — текстовую ролевую игру с DeepSeek API в роли гейм-мастера.

Что должен делать каркас:
- печатает заголовок «⚔️ ПОДЗЕМЕЛЬЯ И ДРАКОНЫ»
- спрашивает имя героя через input
- отправляет запрос в DeepSeek API: url <span class="hl">https://api.deepseek.com/chat/completions</span>, модель <span class="hl">deepseek-chat</span>, библиотека requests
- системная роль: «Ты — мастер текстовой ролевой игры. Веди игрока по мрачному фэнтези-подземелью, описывай сцену ярко в 2-3 предложениях и всегда заканчивай тремя вариантами действий»
- первым сообщением user отправь «Начни приключение для героя по имени {имя}»
- печатает сгенерированную стартовую сцену

Ключ — в константе API_KEY в начале файла, я вставлю свой.
Прокомментируй код для новичка. Ответь одним блоком кода.</div>
  </div>
</div>"""},

    # 18 · Вставляем ключ и запускаем
    {"notes": "Раздайте ключи заранее и проверьте интернет на машинах. Первый запрос к API — дождитесь, пока у каждого появится стартовая сцена.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск каркаса</div>
    <h2>Вставляем ключ и <span class="acc">запускаем</span></h2>
  </div>
  <ol class="steps">
    <li>Скопируйте код из ответа DeepSeek в <span class="code-chip">game.py</span></li>
    <li>Замените <span class="code-chip">sk-...</span> на ключ, который выдал преподаватель</li>
    <li>Сохраните файл (<span class="code-chip">Ctrl+S</span>)</li>
    <li>Выполните <span class="code-chip">python game.py</span></li>
    <li>Введите имя героя</li>
  </ol>
  <div class="ek-note ek-note--red">Ключ — <b>в кавычках и без пробелов</b>. На скриншотах для домашки ключ замазываем.</div>
</div>"""},

    # 19 · Нейросеть придумала вам подземелье
    {"notes": "Дайте момент прочувствовать: нейросеть только что придумала подземелье лично для их героя. Попросите перезапустить — начало будет другим. Дальше учим игру идти ходами.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Момент урока</div>
    <h2>Нейросеть придумала вам <span class="acc">подземелье</span></h2>
  </div>
  <p>Вы только что получили первую сцену, сгенерированную мастером <span class="hl">лично для вашего героя</span>. Никто в классе не увидит ровно такую же.</p>
  <div class="ek-note ek-note--green">Перезапустите игру — начало будет <b>другим</b>: мастер придумывает мир заново при каждом запуске.</div>
  <div class="ek-note">Пока это <b>одна</b> сцена. Сейчас научим игру идти ход за ходом — через цикл и функции.</div>
</div>"""},
]
