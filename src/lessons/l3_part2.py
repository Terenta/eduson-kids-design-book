# -*- coding: utf-8 -*-
SLIDES = [
    # 11 · Что такое событие
    {"notes": "Событие — это «сигнал», который браузер отправляет, когда что-то произошло. JavaScript не следит постоянно — он подписывается на нужные события и ждёт.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Сигналы от пользователя</div>
    <h2>Что такое <span class="acc">событие</span></h2>
  </div>
  <p>Событие (event) — это <span class="hl">сигнал от браузера</span>: что-то произошло. Клик, ввод символа, отметка чекбокса, нажатие клавиши. JavaScript не «следит» постоянно — он <b>подписывается</b> на нужные события и ждёт.</p>
  <div class="ek-note" style="margin-top:6px">Аналогия: вы не стоите весь день у двери. Вы вешаете <b>звонок</b>. Когда придёт гость — звонок сработает. <span class="code-chip">addEventListener</span> — это и есть «повесить звонок».</div>
</div>"""},

    # 12 · Главные виды событий
    {"notes": "Таблица главных событий. Сегодня используем click, input, change.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Справочник</div>
    <h2>Главные виды <span class="acc">событий</span></h2>
  </div>
  <div class="kv" style="margin-top:6px">
    <div class="kv-row"><div class="k">click</div><div class="v">Клик мышью по элементу. Кнопки, ссылки, любые блоки.</div></div>
    <div class="kv-row"><div class="k">input</div><div class="v">Пользователь печатает в поле ввода. Срабатывает на каждый символ.</div></div>
    <div class="kv-row"><div class="k">change</div><div class="v">Значение изменилось и поле потеряло фокус. Чекбоксы, выпадающие списки.</div></div>
    <div class="kv-row"><div class="k">submit</div><div class="v">Отправка формы — нажатие Enter или кнопки внутри формы.</div></div>
    <div class="kv-row"><div class="k">keydown</div><div class="v">Нажата клавиша на клавиатуре. Пригодится на уроке 4 для игры.</div></div>
    <div class="kv-row"><div class="k">mouseover</div><div class="v">Курсор навёлся на элемент. Часто заменяют CSS-эффектом <span class="code-chip">:hover</span>.</div></div>
  </div>
</div>"""},

    # 13 · addEventListener — как подписаться
    {"notes": "Синтаксис подписки на событие. Это сердце всей интерактивности.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Главная команда урока</div>
    <h2><span class="acc">addEventListener</span> — как подписаться</h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body"><span class="kw">const</span> btn = document.getElementById(<span class="st">'add'</span>);

btn.addEventListener(<span class="st">'click'</span>, () =&gt; {
  console.log(<span class="st">'Кнопку нажали!'</span>);
  <span class="cm">// здесь — реакция: добавить задачу</span>
});</div>
  </div>
  <div class="grid-3" style="margin-top:14px">
    <div class="info-card"><h3>btn</h3><p>На каком элементе слушаем.</p></div>
    <div class="info-card"><h3>'click'</h3><p>Какое событие ждём.</p></div>
    <div class="info-card"><h3>() =&gt; { ... }</h3><p>Что делать, когда событие случилось.</p></div>
  </div>
</div>"""},

    # 14 · Цель урока
    {"notes": "Прочитайте цель вслух. Подчеркните: результат — рабочий список задач, которым можно пользоваться каждый день.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Goal · что будет в конце</div>
    <h2>Цель <span class="acc">урока</span></h2>
  </div>
  <div class="ek-note ek-note--green" style="font-size:16px">Собрать рабочий <b>список задач</b> через диалог с DeepSeek. Задачи добавляются, удаляются, отмечаются выполненными и сохраняются между перезагрузками страницы.</div>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>Узнаете</h3>
      <ul class="clean">
        <li>Что такое DOM и события в браузере</li>
        <li>Как JavaScript изменяет страницу</li>
        <li>Зачем нужен localStorage и как он работает</li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Сделаете</h3>
      <ul class="clean">
        <li>Каркас списка задач из 3 файлов</li>
        <li>Добавление и удаление задач</li>
        <li>Чекбоксы «выполнено»</li>
        <li>Сохранение между перезагрузками</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 15 · Что соберём сегодня (демо)
    {"notes": "Покажите готовый список (можно собрать заранее). Скажите: вот что будет у каждого к 55-й минуте.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Демо результата</div>
    <h2>Что соберём <span class="acc">сегодня</span></h2>
  </div>
  <p>К концу урока у каждого — такой список:</p>
  <div class="info-card" style="max-width:560px;margin-top:6px">
    <h3 style="margin-bottom:14px">Мои задачи</h3>
    <div style="display:flex;gap:8px;margin-bottom:14px">
      <div style="flex:1;background:var(--ek-gray-light);border-radius:10px;padding:10px 14px;font:500 15px/1 var(--f-body);color:var(--ek-gray)">Что нужно сделать…</div>
      <div style="background:var(--ek-violet);color:#fff;border-radius:10px;padding:10px 18px;font:800 15px/1 var(--f-head)">Добавить</div>
    </div>
    <div style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--ek-line)"><span class="hl">☑</span><span style="text-decoration:line-through;color:var(--ek-gray);flex:1">Сделать ДЗ по уроку 2</span><span style="color:var(--ek-red-deep)">×</span></div>
    <div style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--ek-line)"><span>☐</span><span style="flex:1">Доделать список задач</span><span style="color:var(--ek-red-deep)">×</span></div>
    <div style="display:flex;align-items:center;gap:10px;padding:10px 0"><span>☐</span><span style="flex:1">Показать другу</span><span style="color:var(--ek-red-deep)">×</span></div>
  </div>
</div>"""},

    # 16 · Папка lesson-03
    {"notes": "Структура та же, что на уроке 2 — продолжаем привычку 3 файлов.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Структура проекта</div>
    <h2>Папка <span class="acc">lesson-03</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div>
      <ol class="steps steps--tight">
        <li>На диске <span class="code-chip">D:</span> в папке <span class="code-chip">vibe-coding</span> создайте <span class="code-chip">lesson-03</span></li>
        <li>В VS Code: <span class="code-chip">File → Open Folder → lesson-03</span></li>
        <li>Создайте 3 файла: <span class="code-chip">index.html</span>, <span class="code-chip">style.css</span>, <span class="code-chip">script.js</span></li>
      </ol>
    </div>
    <div>
      <div class="term">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
        <div class="term-body">D:/vibe-coding/lesson-03/
├── index.html
├── style.css
└── script.js</div>
      </div>
      <div class="ek-note ek-note--red" style="margin-top:12px">Те же 3 файла, что на уроке 2. Привычка раскладывать проект на структуру / оформление / поведение остаётся весь курс.</div>
    </div>
  </div>
</div>"""},

    # 17 · Промпт #1 стартовый
    {"notes": "Используем все техники промтинга с урока 2: роль, контекст, формат, ограничения. Дайте скопировать.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #1 · стартовый</div>
    <h2>Каркас <span class="acc">списка задач</span></h2>
  </div>
  <div class="prompt-card">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты <span class="hl">senior фронтенд-разработчик в стиле Linear/Notion</span>.
Я делаю <span class="hl">список задач</span> — будем пользоваться им каждый день.

Требования:
- <span class="hl">Три файла</span>: index.html, style.css, script.js
- В index.html — заголовок «Мои задачи», поле ввода + кнопка «Добавить», ниже пустой <span class="hl">&lt;ul id="list"&gt;</span>
- В style.css — тёмная тема, акцент <span class="hl">фиолетовый #7C3AED</span>, мягкие отступы, скруглённые углы, лёгкая тень у карточки списка
- В script.js — пока ничего, просто пустой файл (логику добавим в правках)
- <span class="hl">Без библиотек</span>, чистый код

Ответь <span class="hl">тремя блоками</span>, по одному на каждый файл, с подписью имени файла сверху.</div>
  </div>
</div>"""},

    # 18 · Забираем код и запускаем
    {"notes": "Создаём 3 файла, копируем 3 блока, запускаем Live Server. Кнопка пока не работает — это нормально.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Из чата в проект</div>
    <h2>Забираем код и <span class="acc">запускаем</span></h2>
  </div>
  <ol class="steps steps--tight" style="margin-top:6px">
    <li>В ответе DeepSeek нажмите <b>Copy</b> над первым блоком (HTML)</li>
    <li>Вставьте в <span class="code-chip">index.html</span>, сохраните (<span class="code-chip">Ctrl+S</span>)</li>
    <li>Так же со вторым (CSS) и третьим (JS) блоком</li>
    <li>Правый клик по <span class="code-chip">index.html</span> → <b>Open with Live Server</b></li>
  </ol>
  <div class="ek-note" style="margin-top:8px">Сейчас вы видите заголовок, поле ввода и кнопку «Добавить». <b>Кнопка пока не работает</b> — логику добавим в следующих правках. Это нормально.</div>
</div>"""},

    # 19 · Типичные ситуации запуска
    {"notes": "Шпаргалка по первому запуску. Указывайте на этот слайд во время практики.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Если каркас не открылся</div>
    <h2>Типичные ситуации <span class="acc">запуска</span></h2>
  </div>
  <div class="kv" style="margin-top:6px">
    <div class="kv-row"><div class="k">страница белая</div><div class="v">Файл не сохранён (★ в имени) или скопирован не весь блок. Нажмите <span class="code-chip">Ctrl+S</span>, проверьте код.</div></div>
    <div class="kv-row"><div class="k">нет «Go Live»</div><div class="v">Расширение Live Server не активно. Перезапустите VS Code, проверьте вкладку Extensions.</div></div>
    <div class="kv-row"><div class="k">стили не применились</div><div class="v">В <span class="code-chip">index.html</span> нет тега <span class="code-chip">&lt;link rel="stylesheet" href="style.css"&gt;</span>. Проверьте.</div></div>
    <div class="kv-row"><div class="k">любая ошибка</div><div class="v">Скопируйте текст ошибки из консоли (F12) и отправьте в DeepSeek с вопросом «как исправить?».</div></div>
  </div>
</div>"""},
]
