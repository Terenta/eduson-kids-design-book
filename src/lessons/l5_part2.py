# -*- coding: utf-8 -*-
SLIDES = [
    # 11 · Что такое API
    {"notes": "Ключевая новая идея урока. Объясните простыми словами: API — дверь, через которую программы обращаются к нейросети. Дети уже общались с DeepSeek в чате — теперь это будет делать их код.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Главная идея</div>
    <h2>Что такое <span class="acc">API</span></h2>
  </div>
  <p>Нейросеть можно вызывать не только из чата в браузере. У DeepSeek есть <span class="hl">API</span> — дверь для программ: ваш код отправляет вопрос, нейросеть возвращает ответ текстом.</p>
  <div class="ek-note" style="margin-top:8px">API — это способ, которым <b>программы разговаривают друг с другом</b>. Сегодня ваша программа впервые заговорит с нейросетью напрямую — без браузера и без чата.</div>
</div>"""},

    # 12 · Как летит запрос
    {"notes": "Пройдите по трём шагам схемы. Подчеркните: внутри — тот же DeepSeek, что писал им код, меняется только способ обращения.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как это работает</div>
    <h2>Как летит <span class="acc">запрос</span></h2>
  </div>
  <div class="grid-3" style="margin-top:6px">
    <div class="info-card">
      <h3>1 · Запрос</h3>
      <p><span class="code-chip">advisor.py</span> собирает сообщение: модель, роль советчика и вопрос пользователя.</p>
    </div>
    <div class="info-card">
      <h3>2 · Нейросеть</h3>
      <p>Сервер DeepSeek генерирует ответ — тот же «мозг», что отвечает вам в чате.</p>
    </div>
    <div class="info-card">
      <h3>3 · Ответ</h3>
      <p>Программа получает текст и печатает его в терминале.</p>
    </div>
  </div>
  <div class="ek-note" style="margin-top:8px">Всё это — одна функция <span class="code-chip">requests.post</span> и пара строк кода. Их напишет DeepSeek.</div>
</div>"""},

    # 13 · API-ключ
    {"notes": "Раздайте ключи (подготовьте заранее). Проговорите правило: ключ — как пароль, не публиковать и не показывать на скриншотах.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Пропуск к нейросети</div>
    <h2><span class="acc">API-ключ</span></h2>
  </div>
  <p>Ключ — строка вида <span class="code-chip">sk-...</span>. Это <span class="hl">пропуск</span>: по нему сервер понимает, кто стучится.</p>
  <div class="grid-2" style="margin-top:6px">
    <div class="info-card">
      <h3>Где взять</h3>
  <p>Сегодня ключ выдаст преподаватель — вставите его в код и сразу проверите запрос.</p>
    </div>
    <div class="info-card">
      <h3>Как хранить</h3>
      <p>Ключ — как пароль: не публиковать, не показывать на скриншотах. Сегодня вставим в константу <span class="code-chip">API_KEY</span> прямо в код — для учёбы можно. Правильному хранению научимся на уроке 8.</p>
    </div>
  </div>
  <div class="ek-note ek-note--red" style="margin-top:8px">Если ключ «утёк» — его <b>перевыпускают</b>: старый перестаёт работать, выдаётся новый.</div>
</div>"""},

    # 14 · Цель урока
    {"notes": "Прочитайте цель вслух. Подчеркните: сегодня внутри программы — настоящая нейросеть, ответы у всех будут разными.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Goal · что будет в конце</div>
    <h2>Цель <span class="acc">урока</span></h2>
  </div>
  <div class="ek-note">К 55-й минуте у каждого — советчик с настоящей нейросетью внутри: спрашивает имя и характер, ведёт диалог по кругу, отвечает живыми ответами DeepSeek, сохраняет историю в файл и печатает всё в цвете.</div>
  <div class="grid-2" style="margin-top:10px">
    <div class="info-card">
      <h3>Узнаете</h3>
      <ul class="clean">
        <li>Как Python-скрипт запускается в терминале</li>
        <li>Что такое API и API-ключ</li>
        <li>Как промпт живёт внутри кода — системная роль</li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Сделаете</h3>
      <ul class="clean">
        <li>Запустите первый скрипт</li>
        <li>Подключите DeepSeek API к своей программе</li>
        <li>Соберёте советчика через 5 правок</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 15 · Что соберём сегодня (демо)
    {"notes": "Покажите живой запуск советчика — соберите заранее. Спросите одно и то же дважды, чтобы группа увидела разные ответы нейросети.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Демо результата</div>
    <h2>Что соберём <span class="acc">сегодня</span></h2>
  </div>
  <div class="term">
    <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
    <div class="term-body">🔮 Советчик на связи!
Как тебя зовут? <span class="usr">Маша</span>
Выбери характер: 1 — добрый друг, 2 — строгий тренер, 3 — весёлый кот
&gt; <span class="usr">1</span>
Маша, о чём поговорим? <span class="usr">Завтра контрольная по алгебре, страшно</span>
Совет: Страх перед контрольной — это нормально. Разбери два-три
типовых примера сегодня вечером — и завтра рука сама всё вспомнит.
Маша, о чём поговорим? <span class="usr">выход</span>
Записал наш разговор в history.txt. До встречи, Маша!</div>
  </div>
  <div class="ek-note" style="margin-top:8px">Совет сгенерировала <span class="hl">нейросеть</span> — у каждого в классе ответы будут свои.</div>
</div>"""},

    # 16 · Папка lesson-05 и requests
    {"notes": "Подготовка: advisor.py рядом с hello.py, затем pip install requests. Дождитесь, пока установка пройдёт у всех — без requests дальше никак.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Подготовка</div>
    <h2>Папка lesson-05 и <span class="acc">requests</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div>
      <ol class="steps">
        <li>Папка <span class="code-chip">lesson-05</span> уже есть — в ней живёт <span class="code-chip">hello.py</span></li>
        <li>Создайте файл <span class="code-chip">advisor.py</span></li>
        <li>В терминале выполните <span class="code-chip">pip install requests</span> — библиотека, через которую Python ходит в интернет</li>
      </ol>
    </div>
    <div>
      <div class="term">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ПАПКА</span></div>
        <div class="term-body">D:/vibe-coding/lesson-05/
├── hello.py
└── advisor.py</div>
      </div>
      <div class="ek-note" style="margin-top:8px"><span class="code-chip">pip</span> ставит библиотеку один раз. При повторном запуске напишет <span class="out-chip">Requirement already satisfied</span> — это нормально.</div>
    </div>
  </div>
</div>"""},

    # 17 · Промпт #2 · каркас советчика
    {"notes": "Скопировать промпт целиком в новый чат DeepSeek. Обратите внимание: url и модель уже в промпте — нейросеть соберёт рабочий запрос сама.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #2 · стартовый</div>
    <h2>Каркас <span class="acc">советчика</span></h2>
  </div>
  <div class="prompt-card" style="margin-top:6px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — опытный Python-разработчик и наставник школьника.
Напиши advisor.py — советчика для подростка с DeepSeek API.

Что должен делать каркас:
- печатает приветствие «🔮 Советчик на связи!»
- спрашивает вопрос через input
- отправляет его в DeepSeek API: url https://api.deepseek.com/chat/completions, модель deepseek-chat, библиотека requests
- системная роль: «Ты дружелюбный советчик для подростка. Отвечай кратко, 2–3 предложения, по-русски»
- печатает ответ нейросети и прощается

Ключ — в константе API_KEY в начале файла, я вставлю свой.
Прокомментируй код для новичка. Ответь одним блоком кода.</div>
  </div>
</div>"""},

    # 18 · Вставляем ключ и запускаем
    {"notes": "Раздайте ключи заранее и проверьте интернет на машинах. Первый запуск с API — дождитесь, пока у каждого появится ответ нейросети.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск каркаса</div>
    <h2>Вставляем ключ и <span class="acc">запускаем</span></h2>
  </div>
  <ol class="steps">
    <li>Скопируйте код из ответа DeepSeek в <span class="code-chip">advisor.py</span></li>
    <li>Замените <span class="code-chip">sk-...</span> на ключ, который выдал преподаватель</li>
    <li>Сохраните файл (<span class="code-chip">Ctrl+S</span>)</li>
    <li>Выполните <span class="code-chip">python advisor.py</span></li>
    <li>Задайте советчику настоящий вопрос</li>
  </ol>
  <div class="ek-note ek-note--red" style="margin-top:8px">Ключ — <b>в кавычках и без пробелов</b>. На скриншотах для домашки ключ замазываем.</div>
</div>"""},

    # 19 · Первый ответ нейросети
    {"notes": "Дайте момент прочувствовать: их код только что поговорил с нейросетью. Попросите задать один и тот же вопрос дважды и сравнить ответы.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Момент урока</div>
    <h2>Первый ответ <span class="acc">нейросети</span></h2>
  </div>
  <p>Вы только что соединили свой код с нейросетью: вопрос ушёл из вашей программы на сервер DeepSeek — ответ вернулся в ваш терминал.</p>
  <div class="ek-note ek-note--green" style="margin-top:8px">Спросите одно и то же дважды — ответы будут <b>разными</b>: нейросеть генерирует текст заново, а не достаёт из списка.</div>
  <div class="ek-note" style="margin-top:8px">Это та же нейросеть, что писала вам код в чате, — теперь она <b>работает на вас</b> внутри вашей программы.</div>
</div>"""},
]
