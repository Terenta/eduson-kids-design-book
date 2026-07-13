# -*- coding: utf-8 -*-
SLIDES = [
    # 1 · ТИТУЛ
    {"cls": "slide--violet", "notes": "Поприветствуйте группу. Скажите, что сегодня вы вместе соберёте свой первый сайт через диалог с нейросетью. Покажите на экране готовый результат — страницу «Обо мне», к которой каждый придёт к концу урока.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">H</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">M</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">L</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">T</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="cover-card">
      <div class="badge">Урок №1</div>
      <div class="card-top"><span class="win-dots"><i></i><i></i><i></i></span><span class="win-close"></span></div>
      <h1>Знакомство со средой<br>и первый сайт</h1>
      <p class="cover-sub">Соберём личную страницу «Обо мне» через диалог с нейросетью. Установим инструменты, напишем первый промпт и запустим результат в браузере.</p>
      <div class="cover-chips"><span class="chip">VS Code</span><span class="chip chip--green">DeepSeek</span><span class="chip chip--gray">Python 3.12</span><span class="chip chip--gray">Live Server</span></div>
    </div>
  </div>"""},

    # 2 · ИДЕЯ УРОКА · вайб-кодинг
    {"notes": "Объясните, что такое вайб-кодинг — без сравнений с другими подходами. Дайте короткую схему: вы описываете задачу, нейросеть пишет код, вы проверяете результат. Подчеркните: главный навык — формулировать задачу, и он пригодится в любой профессии.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Идея урока</div>
    <h2>Что такое <span class="acc">вайб-кодинг</span></h2>
  </div>
  <p>Вайб-кодинг — это создание программ через диалог с нейросетью. Вы описываете задачу обычными словами, нейросеть пишет код, вы запускаете его и проверяете результат.</p>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card">
      <h3>Описываете</h3>
      <p>Рассказываете нейросети, какую страницу хотите: какие блоки, какие цвета, что происходит при клике.</p>
    </div>
    <div class="info-card">
      <h3>Нейросеть пишет</h3>
      <p>DeepSeek генерирует готовый код, который можно скопировать в файл.</p>
    </div>
    <div class="info-card">
      <h3>Вы запускаете</h3>
      <p>Открываете страницу в браузере. Нужно поправить — пишете нейросети новое сообщение.</p>
    </div>
  </div>
  <div class="ek-note">Главный навык вайб-кодера — <b>точно формулировать задачу</b>. Этот навык ценят и в IT, и в дизайне, и в науке.</div>
</div>"""},

    # 3 · ПЛАН (agenda)
    {"notes": "Покажите план занятия. Подчеркните: первый урок — это знакомство и установка, поэтому много инсталляций. Дальше будет проще.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Agenda · план занятия</div>
    <h2>Как пройдут <span class="acc">60 минут</span></h2>
  </div>
  <div class="agenda">
    <div class="agenda-row"><span class="t">0–5</span><div><div class="tt">Демо результата</div><div class="dd">Покажем готовую страницу «Обо мне», которую вы соберёте к концу урока.</div></div></div>
    <div class="agenda-row"><span class="t">5–10</span><div><div class="tt">Что такое вайб-кодинг</div><div class="dd">Главная идея и роль нейросети как помощника, который знает синтаксис.</div></div></div>
    <div class="agenda-row"><span class="t">10–25</span><div><div class="tt">Установка инструментов</div><div class="dd">VS Code → Python → расширение Live Server → рабочая папка.</div></div></div>
    <div class="agenda-row"><span class="t">25–30</span><div><div class="tt">Знакомство с DeepSeek</div><div class="dd">Регистрация через Google, обзор интерфейса.</div></div></div>
    <div class="agenda-row"><span class="t">30–45</span><div><div class="tt">Первый промпт и первый сайт</div><div class="dd">Берём готовый промпт, получаем код, запускаем страницу в браузере.</div></div></div>
    <div class="agenda-row"><span class="t">45–55</span><div><div class="tt">Доработка через диалог</div><div class="dd">Меняем кнопку, добавляем аватарку и анимацию — всё через сообщения.</div></div></div>
    <div class="agenda-row"><span class="t">55–60</span><div><div class="tt">Демо в группе</div><div class="dd">Каждый присылает скриншот своей страницы в общий чат.</div></div></div>
  </div>
</div>"""},

    # 4 · ЦЕЛЬ УРОКА (grid-2, Узнаете/Сделаете)
    {"notes": "Прочитайте цели вслух. Подчеркните: к концу урока у каждого будет рабочий файл index.html в собственной папке курса.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Goal · что будет в конце</div>
    <h2>Цель <span class="acc">урока</span></h2>
  </div>
  <div class="ek-note">Через диалог с DeepSeek собрать рабочую страницу «Обо мне». Файл <span class="code-chip">index.html</span> открывается в браузере и выглядит аккуратно.</div>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>Узнаете</h3>
      <ul class="clean">
        <li>Что такое вайб-кодинг и из каких шагов он состоит</li>
        <li>Как разговаривать с DeepSeek, чтобы получать точные ответы</li>
        <li>Зачем разработчикам VS Code, Python и Live Server</li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Сделаете</h3>
      <ul class="clean">
        <li>Установите инструменты курса</li>
        <li>Напишете первый промпт и получите код</li>
        <li>Запустите свой сайт в браузере</li>
        <li>Сделаете 3 правки через диалог</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 5 · ИНСТРУМЕНТЫ (4 info-card)
    {"notes": "Расскажите про инструменты. У каждого своя роль. На уроке используем доступные бесплатные варианты, без платных подписок.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Инструменты урока</div>
    <h2>Связка из <span class="acc">четырёх инструментов</span></h2>
  </div>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>1 · VS Code</h3>
      <p><span class="code-chip">code.visualstudio.com</span> — редактор, в котором вы будете работать с файлами проекта.</p>
    </div>
    <div class="info-card">
      <h3>2 · Python 3.12</h3>
      <p><span class="code-chip">python.org</span> — понадобится со следующих уроков. Установим заранее.</p>
    </div>
    <div class="info-card">
      <h3>3 · DeepSeek</h3>
      <p><span class="code-chip">chat.deepseek.com</span> — нейросеть, с которой вы общаетесь весь курс. Бесплатно.</p>
    </div>
    <div class="info-card">
      <h3>4 · Live Server</h3>
      <p>Расширение VS Code — запускает HTML-страницу в браузере одной кнопкой.</p>
    </div>
  </div>
  <div class="ek-note ek-note--green">На уроке используем доступные бесплатные варианты инструментов. Подписки и ввод банковской карты не требуются.</div>
</div>"""},

    # 6 · УСТАНОВКА VS Code (ol.steps)
    {"notes": "Покажите установку VS Code пошагово на проекторе. Обратите внимание на 3 галочки в установщике — особенно «Add to PATH».", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Установка · 1 из 4</div>
    <h2>Установите <span class="acc">VS Code</span></h2>
  </div>
  <ol class="steps steps--tight">
    <li>Откройте <span class="code-chip">code.visualstudio.com</span></li>
    <li>Нажмите большую синюю кнопку <b>Download for Windows</b> (или Mac)</li>
    <li>Запустите скачанный установщик</li>
    <li>Отметьте 3 галочки: <span class="code-chip">Add 'Open with Code' to file context menu</span>, <span class="code-chip">…to directory context menu</span>, <span class="code-chip">Add to PATH</span></li>
    <li>Нажмите Install → Finish → запустите редактор</li>
  </ol>
  <div class="ek-note">Первые две галочки дают открывать файлы и папки в VS Code прямо из проводника по правому клику. Третья добавляет VS Code в системные пути — пригодится дальше.</div>
</div>"""},

    # 7 · УСТАНОВКА Python (ol.steps + term проверка)
    {"notes": "Самый важный шаг — галочка «Add python.exe to PATH». Без неё команда python в терминале работать не будет. Остановите класс и проверьте у каждого, что галочка отмечена.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Установка · 2 из 4</div>
    <h2>Установите <span class="acc">Python 3.12</span></h2>
  </div>
  <ol class="steps steps--tight">
    <li>Откройте <span class="code-chip">python.org/downloads</span>, скачайте Python 3.12.x или новее</li>
    <li>Запустите установщик</li>
    <li>Отметьте галочку <span class="code-chip">Add python.exe to PATH</span> внизу окна</li>
    <li>Нажмите «Install Now», дождитесь завершения, нажмите Close</li>
  </ol>
  <p style="margin-top:4px">Проверка: откройте терминал в VS Code (<span class="code-chip">Ctrl+ё</span>) и выполните команду — программа ответит <span class="out-chip">Python 3.12.x</span>.</p>
  <div class="term">
    <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
    <div class="term-body"><span class="usr">python --version</span>
Python 3.12.x</div>
  </div>
  <div class="ek-note ek-note--red">Если ответ <span class="code-chip">python is not recognized</span> — пропущена галочка PATH. Переустановите Python и отметьте «Add python.exe to PATH».</div>
</div>"""},

    # 8 · РАСШИРЕНИЯ (ol.steps + grid-2)
    {"notes": "Расширения ставим прямо из VS Code. Покажите иконку Extensions слева. Live Server — главное на этот урок, Python — пригодится дальше.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Установка · 3 из 4</div>
    <h2>Установите <span class="acc">расширения</span> VS Code</h2>
  </div>
  <ol class="steps steps--tight">
    <li>Слева нажмите иконку <b>Extensions</b> (четыре квадратика)</li>
    <li>В строку поиска введите <span class="code-chip">Live Server</span></li>
    <li>Выберите расширение от автора <b>Ritwick Dey</b> и нажмите <b>Install</b></li>
    <li>Тем же способом установите <span class="code-chip">Python</span> от <b>Microsoft</b></li>
  </ol>
  <div class="grid-2" style="margin-top:6px">
    <div class="info-card">
      <h3>Live Server</h3>
      <p>Запускает HTML-файл в браузере одной кнопкой. При сохранении файла страница обновляется сама.</p>
    </div>
    <div class="info-card">
      <h3>Python</h3>
      <p>Подсветка синтаксиса, автодополнение, запуск .py-файлов одной кнопкой. Понадобится с урока 3.</p>
    </div>
  </div>
</div>"""},

    # 9 · РАБОЧАЯ ПАПКА (ol.steps + term структура)
    {"notes": "Создаём папку курса. Все материалы за весь курс будут лежать в одном месте — это поможет потом собрать портфолио.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Установка · 4 из 4</div>
    <h2>Создайте <span class="acc">рабочую папку</span></h2>
  </div>
  <div class="grid-2" style="margin-top:8px">
    <div>
      <ol class="steps steps--tight">
        <li>На диске <span class="code-chip">D:</span> создайте папку <span class="code-chip">vibe-coding</span></li>
        <li>Внутри неё — папку <span class="code-chip">lesson-01</span></li>
        <li>В VS Code: <span class="code-chip">File → Open Folder</span> → выберите <span class="code-chip">lesson-01</span></li>
        <li>Создайте файл: <span class="code-chip">Ctrl+N</span></li>
        <li>Сохраните как <span class="code-chip">index.html</span> (<span class="code-chip">Ctrl+S</span>)</li>
      </ol>
    </div>
    <div>
      <div class="term">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">СТРУКТУРА</span></div>
        <div class="term-body">D:/
└── vibe-coding/
    └── lesson-01/
        └── index.html  <span class="dim">← пока пустой</span></div>
      </div>
      <div class="ek-note">Папка курса соберёт все проекты в одном месте. К концу курса в ней будет <b>48 проектов</b> — готовое портфолио.</div>
    </div>
  </div>
</div>"""},

    # 10 · DeepSeek (ol.steps + info-card возможности)
    {"notes": "DeepSeek — нейросеть, с которой вы будете общаться весь курс. Регистрация через Google занимает несколько шагов. Для задач урока достаточно базового режима.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Главный собеседник курса</div>
    <h2>Знакомство с <span class="acc">DeepSeek</span></h2>
  </div>
  <div class="grid-2" style="margin-top:8px">
    <div>
      <ol class="steps steps--tight">
        <li>Откройте <span class="code-chip">chat.deepseek.com</span></li>
        <li>Нажмите <b>Log in</b></li>
        <li>Выберите <b>Continue with Google</b></li>
        <li>Выберите свой Google-аккаунт</li>
        <li>Готово — у вас есть собственный чат</li>
      </ol>
      <div class="ek-note ek-note--green">Для задач урока достаточно базового режима. Карта и подписка не нужны.</div>
    </div>
    <div class="info-card">
      <h3>Возможности интерфейса</h3>
      <ul class="clean">
        <li>Обычный режим — быстрый, для большинства задач</li>
        <li>Режим <span class="code-chip">DeepThink (R1)</span> — медленнее, для сложных вопросов</li>
        <li>Можно прикрепить файл, картинку или PDF</li>
        <li>Помнит весь диалог в текущем чате</li>
        <li>Над каждым блоком кода есть кнопка <b>Copy</b></li>
      </ul>
    </div>
  </div>
</div>"""},

    # 11 · ЧТО ТАКОЕ ПРОМПТ (4 части)
    {"notes": "Объясните, что такое промпт. 4 части — роль, задача, контекст, формат. На следующем слайде дадим готовый промпт, на этом — структура.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Анатомия хорошего промпта</div>
    <h2>Что такое <span class="acc">промпт</span></h2>
  </div>
  <p>Промпт — это сообщение, которое вы отправляете нейросети. Хороший промпт состоит из четырёх частей.</p>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>1 · Роль</h3>
      <p>Роль нейросети. Например: «Ты опытный веб-разработчик».</p>
    </div>
    <div class="info-card">
      <h3>2 · Задача</h3>
      <p>Что нужно сделать. Например: «Напиши HTML-страницу „Обо мне“».</p>
    </div>
    <div class="info-card">
      <h3>3 · Контекст</h3>
      <p>Детали: какие блоки, цвета, размеры, шрифты.</p>
    </div>
    <div class="info-card">
      <h3>4 · Формат</h3>
      <p>Формат ответа. Например: «Один файл, без библиотек».</p>
    </div>
  </div>
  <div class="ek-note">Чем точнее промпт, тем точнее ответ. Числа, имена цветов, конкретные ссылки — всё это помогает нейросети попасть в задачу.</div>
</div>"""},
]
