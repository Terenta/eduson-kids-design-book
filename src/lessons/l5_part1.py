# -*- coding: utf-8 -*-
SLIDES = [
    # 1 · ТИТУЛ
    {"cls": "slide--violet", "notes": "Поприветствуйте. Сегодня большой день: первая программа на Python — и впервые нейросеть заработает внутри собственного кода. К концу урока у каждого — советчик, который отвечает на любой вопрос живым ответом DeepSeek.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">P</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">A</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">I</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">Y</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="cover-card">
      <div class="badge">Урок №5 · Модуль 2</div>
      <div class="card-top"><span class="win-dots"><i></i><i></i><i></i></span><span class="win-close"></span></div>
      <h1>Первая программа<br>на&nbsp;Python с&nbsp;AI</h1>
      <p class="cover-sub">Запустим Python в терминале и соберём советчика, внутри которого работает настоящая нейросеть: задаёте вопрос — DeepSeek отвечает прямо в вашей программе.</p>
      <div class="cover-chips"><span class="chip">Python</span><span class="chip chip--green">DeepSeek API</span><span class="chip chip--gray">Терминал</span><span class="chip chip--gray">input / print</span></div>
    </div>
  </div>"""},

    # 2 · ПЛАН
    {"notes": "План. Теории — минимум: уже на 12-й минуте каждый запускает первый скрипт, к 30-й — советчик с живой нейросетью внутри. Дальше — 5 правок через диалог, как на прошлых уроках.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Agenda · план занятия</div>
    <h2>Как пройдут <span class="acc">60 минут</span></h2>
  </div>
  <div class="agenda">
    <div class="agenda-row"><span class="t">0–5</span><div><div class="tt">Разбор ДЗ</div><div class="dd">Смотрим прокачанные «Змейки»: скорость, золотое яблоко, частицы.</div></div></div>
    <div class="agenda-row"><span class="t">5–12</span><div><div class="tt">Python и терминал</div><div class="dd">Новый язык — минимум теории, только чтобы запуститься.</div></div></div>
    <div class="agenda-row"><span class="t">12–20</span><div><div class="tt">Первый скрипт hello.py</div><div class="dd">Промпт → код → запуск в терминале.</div></div></div>
    <div class="agenda-row"><span class="t">20–30</span><div><div class="tt">Каркас советчика</div><div class="dd">Что такое API — и DeepSeek внутри вашей программы.</div></div></div>
    <div class="agenda-row"><span class="t">30–48</span><div><div class="tt">5 правок через диалог</div><div class="dd">Имя → характеры → цикл диалога → история → цвета.</div></div></div>
    <div class="agenda-row"><span class="t">48–55</span><div><div class="tt">Мини-вопросы и отладка</div><div class="dd">Читаем ошибки, проверяем понимание.</div></div></div>
    <div class="agenda-row"><span class="t">55–60</span><div><div class="tt">Демо в группе</div><div class="dd">Каждый задаёт советчику свой вопрос.</div></div></div>
  </div>
</div>"""},

    # 3 · РАЗБОР ДЗ
    {"notes": "Откройте 2-3 прокачанные «Змейки». Разбирайте диалог с нейросетью, а не только результат: какие промпты сработали с первого раза. Свяжите с сегодняшним уроком — те же приёмы работают в Python.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор ДЗ урока 4</div>
    <h2>Смотрим прокачанные <span class="acc">«Змейки»</span></h2>
  </div>
  <p>Открываем 2–3 присланные игры и разбираем именно <span class="hl">диалог с нейросетью</span>, а не только рекорды.</p>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card">
      <h3>Что сработало</h3>
      <p>Точечные промпты: одно улучшение — один запрос. Скорость, золотое яблоко и частицы добавляли по очереди.</p>
    </div>
    <div class="info-card">
      <h3>Что переделывали</h3>
      <p>Где забыли «не трогай остальной код» — нейросеть заодно сломала рестарт.</p>
    </div>
    <div class="info-card">
      <h3>Вывод</h3>
      <p>Точная формулировка плюс проверка после каждой правки. Сегодня это пригодится в <b>Python</b>.</p>
    </div>
  </div>
</div>"""},

    # 4 · ИДЕЯ УРОКА
    {"notes": "Главная мысль урока: у DeepSeek появляется вторая роль. Раньше он только писал код за нас в чате. Сегодня нейросеть впервые заработает внутри программы — advisor.py будет сам отправлять ей вопросы и печатать живые ответы.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Идея урока</div>
    <h2>Нейросеть — внутри вашей <span class="acc">программы</span></h2>
  </div>
  <p>Модуль 1 пройден: сайты, список задач и «Змейка» жили в браузере. Сегодня выходим в Python — и впервые <span class="hl">встраиваем нейросеть в собственный код</span>.</p>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>Роль 1 · пишет код за нас</h4>
      <p>Как раньше: формулируем задачу в чате DeepSeek — забираем готовый код. Это вайб-кодинг.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>Роль 2 · работает внутри программы</h4>
      <p><b>Новое:</b> наш <span class="code-chip">advisor.py</span> сам отправляет вопросы нейросети через API и печатает живые ответы в терминале.</p>
    </div>
  </div>
</div>"""},

    # 5 · PYTHON vs JAVASCRIPT
    {"notes": "Сравнение без «лучше/хуже»: JavaScript живёт в браузере, Python — в системе. Напомните: один язык им уже знаком — второй учится легче. Подход вайб-кодинга не меняется.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Сравнение</div>
    <h2>Python или JavaScript — в чём <span class="acc">разница</span></h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>JavaScript</h4>
      <p>Живёт в браузере. Ждёт события — клики и нажатия — и реагирует на них. Результат видим на странице.</p>
      <p class="note">Им мы делали список задач и «Змейку».</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>Python</h4>
      <p>Живёт в системе. Выполняется сверху вниз в терминале, управляет файлами, ботами и нейросетями.</p>
      <p class="note">На нём написаны Telegram-боты и сам DeepSeek.</p>
    </div>
  </div>
  <div class="ek-note">Языки разные, а подход вайб-кодинга один: <b>формулируем задачу — DeepSeek пишет код — мы запускаем</b>.</div>
</div>"""},

    # 6 · ТЕРМИНАЛ
    {"notes": "Терминал — текстовое окно для команд, как чат с компьютером, только команды строгие. Все открывают терминал и проверяют python --version. Не идите дальше, пока у всех не показалась версия.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Новый инструмент</div>
    <h2>Терминал в <span class="acc">VS Code</span></h2>
  </div>
  <p>Терминал — <span class="hl">текстовое окно для команд компьютеру</span>: без кнопок и мыши. Ввели команду, нажали Enter — получили ответ.</p>
  <div class="grid-2">
    <div class="col">
      <ol class="steps steps--tight">
        <li><div>Откройте папку <span class="code-chip">vibe-coding</span> в VS Code</div></li>
        <li><div>Нажмите <span class="code-chip">Ctrl+ё</span> (или меню <b>Terminal → New Terminal</b>)</div></li>
        <li><div>Введите <span class="code-chip">python --version</span> — должно показать <span class="out-chip">Python 3.12</span></div></li>
      </ol>
    </div>
    <div class="col">
      <div class="kv">
        <div class="kv-row"><div class="k">Запуск</div><div class="v"><span class="code-chip">python имя_файла.py</span> — так запускается любой Python-скрипт.</div></div>
      </div>
      <div class="ek-note ek-note--red" style="margin-top:14px">Если видите «python is not recognized» — Python ставили на уроке 1. Позовите преподавателя: чинится за минуту.</div>
    </div>
  </div>
</div>"""},

    # 7 · ПРОМПТ #1
    {"notes": "Никакой долгой подготовки: сразу просим код у DeepSeek. Промпт короткий, но с ролью и форматом — техники урока 2 работают и здесь. Дети копируют промпт целиком.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #1 · разминка</div>
    <h2>hello.py за <span class="acc">две минуты</span></h2>
  </div>
  <p>Не будем долго готовиться — попросим у DeepSeek первый скрипт и сразу запустим его в терминале.</p>
  <div class="prompt-card" style="margin-top:14px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — опытный Python-разработчик и наставник школьника.
Напиши маленький скрипт hello.py: он спрашивает имя через input,
здоровается по имени и печатает одну приятную фразу дня.
Только стандартная библиотека Python, без сторонних пакетов.
Прокомментируй код для новичка и ответь одним блоком кода.</div>
  </div>
</div>"""},

    # 8 · ЗАПУСК
    {"notes": "Фундамент урока: не идите дальше, пока у всех hello.py не запустился и не ответил. Это первый запуск Python у группы — у кого-то всплывут проблемы окружения, чините сразу.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск</div>
    <h2>Первый Python-скрипт — <span class="acc">12-я минута</span></h2>
  </div>
  <ol class="steps steps--tight">
    <li><div>В <span class="code-chip">vibe-coding</span> создайте папку <span class="code-chip">lesson-05</span></div></li>
    <li><div>Создайте файл <span class="code-chip">hello.py</span> и вставьте код из ответа DeepSeek</div></li>
    <li><div>Сохраните: <span class="code-chip">Ctrl+S</span></div></li>
    <li><div>В терминале выполните <span class="code-chip">python hello.py</span></div></li>
  </ol>
  <div class="ek-note ek-note--green" style="margin-top:16px">Программа спросила имя и ответила? Поздравляем — ваш <b>первый Python-скрипт</b> работает. Двенадцатая минута урока.</div>
</div>"""},

    # 9 · РАЗБОР hello.py
    {"notes": "Разбор на живом коде, который уже у всех запустился. Три кита сегодняшнего урока: print, input, f-строка. Подчеркните: input всегда возвращает строку — к этому вернёмся в мини-вопросе.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Что внутри <span class="acc">hello.py</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">name = input(<span class="st">"Как тебя зовут? "</span>)   <span class="cm"># ждём ответ пользователя</span>
print(f<span class="st">"Привет, {name}!"</span>)          <span class="cm"># подставляем имя в текст</span>
print(<span class="st">"Фраза дня: маленькие шаги каждый день сильнее рывков."</span>)</div>
  </div>
  <div class="kv" style="margin-top:14px">
    <div class="kv-row"><div class="k">print</div><div class="v">Выводит текст в терминал. Каждый print — новая строка.</div></div>
    <div class="kv-row"><div class="k">input</div><div class="v">Останавливает программу и ждёт Enter. Возвращает <span class="hl">всегда строку</span> — даже если ввели число.</div></div>
    <div class="kv-row"><div class="k">f-строка</div><div class="v"><span class="code-chip">f"Привет, {name}!"</span> — вставляет переменную прямо в текст через фигурные скобки.</div></div>
  </div>
</div>"""},

    # 10 · TROUBLESHOOTING
    {"notes": "Шпаргалка по трём типичным проблемам первого запуска. Почините у всех — дальше эти же команды нужны для советчика.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Типичные ситуации запуска</div>
    <h2>Если hello.py <span class="acc">не запустился</span></h2>
  </div>
  <div class="grid-3" style="margin-top:8px">
    <div class="ek-note ek-note--red">
      <b>python is not recognized</b><br>Python не добавлен в PATH. Переустановите с галочкой <b>Add to PATH</b> — или зовите преподавателя.
    </div>
    <div class="ek-note ek-note--red">
      <b>can't open file</b><br>Терминал смотрит в другую папку. Закройте его и откройте заново из VS Code — он стартует в папке проекта.
    </div>
    <div class="ek-note ek-note--red">
      <b>SyntaxError</b><br>Код скопирован не целиком. Вернитесь в чат DeepSeek и заберите весь блок кода заново.
    </div>
  </div>
</div>"""},
]
