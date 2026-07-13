# -*- coding: utf-8 -*-
SLIDES = [
    # 11 · Ответ сервера — знакомый JSON
    {"notes": "Показываем, как устроен ответ OpenWeather. JSON знаком с урока 7. Главное — что достаём: temp лежит внутри main, а описание — в первом элементе списка weather.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как это работает</div>
    <h2>Ответ сервера — знакомый <span class="acc">JSON</span></h2>
  </div>
  <p>OpenWeather присылает <span class="hl">JSON</span> — тот самый формат из урока 7. Это словарь: внутри вложены другие словари и список. Достаём из него нужные поля.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JSON</span></div>
    <div class="code-body">{
  <span class="st">"main"</span>: { <span class="st">"temp"</span>: 23.4, <span class="st">"humidity"</span>: 60 },
  <span class="st">"weather"</span>: [ { <span class="st">"description"</span>: <span class="st">"ясно"</span> } ],
  <span class="st">"name"</span>: <span class="st">"Москва"</span>
}</div>
  </div>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>Температура</h3>
      <p>Лежит внутри словаря <span class="code-chip">main</span>: берём <span class="code-chip">data["main"]["temp"]</span>.</p>
    </div>
    <div class="info-card">
      <h3>Описание</h3>
      <p><span class="code-chip">weather</span> — это <b>список</b>, поэтому сначала <span class="code-chip">[0]</span>: <span class="code-chip">data["weather"][0]["description"]</span>.</p>
    </div>
  </div>
</div>"""},

    # 12 · Что мы пишем в params
    {"notes": "Разбираем params построчно. Ключевое правило урока: без units=metric OpenWeather отдаёт Кельвины. lang=ru — чтобы описание пришло по-русски. Имена параметров не меняем.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Устройство запроса</div>
    <h2>Что мы пишем в <span class="acc">params</span></h2>
  </div>
  <p>Запрос — это адрес <span class="hl">плюс параметры</span>. В словаре <span class="code-chip">params</span> мы сообщаем серверу, что именно хотим узнать.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">url = <span class="st">"https://api.openweathermap.org/data/2.5/weather"</span>
params = {<span class="st">"q"</span>: city, <span class="st">"appid"</span>: OW_KEY, <span class="st">"units"</span>: <span class="st">"metric"</span>, <span class="st">"lang"</span>: <span class="st">"ru"</span>}</div>
  </div>
  <div class="kv" style="margin-top:8px">
    <div class="kv-row"><div class="k">q</div><div class="v">город, о котором спрашиваем</div></div>
    <div class="kv-row"><div class="k">appid</div><div class="v">ключ доступа к сервису</div></div>
    <div class="kv-row"><div class="k">units=metric</div><div class="v">градусы Цельсия, а не Кельвины</div></div>
    <div class="kv-row"><div class="k">lang=ru</div><div class="v">описание погоды по-русски</div></div>
  </div>
  <div class="ek-note ek-note--red">Без <span class="code-chip">units=metric</span> придёт <b>296</b> вместо <b>+23</b>: это температура в Кельвинах.</div>
</div>"""},

    # 13 · Нейросеть комментирует погоду
    {"notes": "Новая связка урока: внешний API даёт данные, DeepSeek формулирует комментарий. Роль DeepSeek задаёт стиль прогноза. Ключ DeepSeek теперь тоже берём из .env, а не из строки в коде.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Новая связка</div>
    <h2>Нейросеть <span class="acc">комментирует</span> погоду</h2>
  </div>
  <p>OpenWeather выдаёт данные: <span class="code-chip">+23</span>, <span class="code-chip">ясно</span>. Мы передаём их <span class="hl">DeepSeek</span>, и он формулирует короткий прогноз человеческим языком.</p>
  <div class="info-card" style="margin-top:6px">
    <h3>Системная роль</h3>
    <p>«Ты весёлый ведущий прогноза погоды, прокомментируй погоду одним бодрым абзацем».</p>
  </div>
  <div class="ek-note">Одна программа соединяет <b>два сервиса</b>: берёт актуальные данные у OpenWeather и передаёт их на комментарий DeepSeek. Ключ DeepSeek теперь тоже храним в <span class="code-chip">.env</span>.</div>
</div>"""},

    # 14 · Цель урока
    {"notes": "Прочитайте цель вслух. Подчеркните: данные впервые не придуманы программой, а взяты из интернета; секреты лежат в .env. Слева теория, справа практика.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Goal · что будет в конце</div>
    <h2>Цель <span class="acc">урока</span></h2>
  </div>
  <div class="ek-note">К 55-й минуте у каждого — приложение погоды в терминале: вводите город, программа берёт текущую погоду у OpenWeather, нейросеть комментирует её и советует, что надеть, а секретные ключи хранятся в файле <span class="code-chip">.env</span>.</div>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>Узнаете</h3>
      <ul class="clean">
        <li>Что такое API и как программа просит данные у чужого сервера</li>
        <li>Как разобрать JSON-ответ и достать нужные поля</li>
        <li>Как хранить ключи в файле <span class="code-chip">.env</span></li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Сделаете</h3>
      <ul class="clean">
        <li>Запросите текущую погоду у OpenWeather</li>
        <li>Отдадите её на комментарий DeepSeek</li>
        <li>Спрячете оба ключа в <span class="code-chip">.env</span></li>
      </ul>
    </div>
  </div>
</div>"""},

    # 15 · Что соберём сегодня (демо)
    {"notes": "Покажите заранее собранное приложение. Введите город при группе, чтобы все увидели: погода приходит из OpenWeather, а нейросеть формулирует комментарий и совет по одежде.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Демо результата</div>
    <h2>Что соберём <span class="acc">сегодня</span></h2>
  </div>
  <div class="term">
    <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
    <div class="term-body">🌦️ Погода с комментарием
Какой город? <span class="usr">Москва</span>
Москва: +23°, ясно
Ведущий: Отличный день, чтобы гулять до самого вечера!
Совет: футболка и кепка — солнце жарит вовсю.</div>
  </div>
  <p style="margin-top:10px">Температура — <span class="hl">настоящая, прямо сейчас</span> из OpenWeather; комментарий и совет придумала <span class="hl">нейросеть</span> по этим данным.</p>
</div>"""},

    # 16 · Папка lesson-08
    {"notes": "Подготовка: weather.py рядом с warmup.py. requests мог остаться с уроков 5-7, python-dotenv — новая библиотека. Два ключа (OpenWeather и DeepSeek) раздаёт преподаватель.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Подготовка</div>
    <h2>Папка <span class="acc">lesson-08</span></h2>
  </div>
  <div class="grid-2">
    <div>
      <ol class="steps">
        <li>Папка <span class="code-chip">lesson-08</span> уже есть — в ней лежит <span class="code-chip">warmup.py</span></li>
        <li>Создайте файл <span class="code-chip">weather.py</span></li>
        <li>Поставьте библиотеки: <span class="code-chip">pip install requests python-dotenv</span></li>
        <li>Возьмите у преподавателя <b>два ключа</b>: OpenWeather и DeepSeek</li>
      </ol>
    </div>
    <div>
      <div class="code-win">
        <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ПАПКА</span></div>
        <div class="code-body">D:/vibe-coding/lesson-08/
├── warmup.py
└── weather.py</div>
      </div>
      <div class="ek-note ek-note--red"><span class="code-chip">requests</span> мог остаться с прошлых уроков, а <span class="code-chip">python-dotenv</span> — новый: он умеет читать файл <span class="code-chip">.env</span>.</div>
    </div>
  </div>
</div>"""},

    # 17 · Промпт #2 · каркас weather.py
    {"notes": "Собираем каркас приложения: ввод города и функция get_weather, которая пока возвращает учебные данные. Настоящий запрос к OpenWeather добавим на Правке 1. Разделение на функции важно: дальше правки привязаны именно к get_weather.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #2 · каркас weather.py</div>
    <h2>Каркас <span class="acc">weather.py</span></h2>
  </div>
  <div class="prompt-card">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — опытный Python-разработчик и наставник школьника. Напиши weather.py: спроси город через input, напечатай «Смотрю погоду для {city}…» и вызови функцию-заглушку get_weather(city), которая пока возвращает фиктивные данные (например temp=0, описание «скоро добавим»). Раздели на функции. Только стандартная библиотека. Верни одним блоком.</div>
  </div>
  <p style="margin-top:10px">Это <b>каркас</b> <span class="code-chip">weather.py</span>: ввод города есть, а <span class="code-chip">get_weather</span> пока возвращает учебные данные. Настоящий запрос к OpenWeather добавим на Правке 1.</p>
</div>"""},

    # 18 · Вставляем каркас и запускаем
    {"notes": "Запустите каркас. Настоящего ключа тут ещё нет — get_weather возвращает учебные данные. Дождитесь, пока у всех программа спрашивает город и печатает ответ. Запрос к OpenWeather добавим на Правке 1.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск каркаса</div>
    <h2>Вставляем каркас и <span class="acc">запускаем</span></h2>
  </div>
  <ol class="steps">
    <li>Скопируйте код из ответа DeepSeek в <span class="code-chip">weather.py</span></li>
    <li>Сохраните файл (<span class="code-chip">Ctrl+S</span>)</li>
    <li>Выполните <span class="code-chip">python weather.py</span></li>
    <li>Введите город — программа напечатает «Смотрю погоду для …»</li>
    <li>Пока приходят учебные данные из <span class="code-chip">get_weather</span> — это нормально</li>
  </ol>
  <div class="ek-note ek-note--red">Настоящей погоды тут ещё нет: <span class="code-chip">get_weather</span> пока возвращает <b>учебные данные</b>. Заменим их запросом к OpenWeather на <b>Правке 1</b>.</div>
</div>"""},

    # 19 · Каркас приложения готов
    {"notes": "Зафиксируйте промежуточный результат: каркас приложения работает — есть ввод города и функция get_weather, готовая к доработке. Настоящая погода из интернета появится на Правке 1, когда учебные данные заменим запросом к OpenWeather.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Момент урока</div>
    <h2>Каркас приложения <span class="acc">готов</span></h2>
  </div>
  <p>Приложение уже <span class="hl">спрашивает город</span> и вызывает функцию <span class="code-chip">get_weather</span> — но пока она возвращает учебные данные, а не настоящую погоду.</p>
  <div class="ek-note ek-note--green">Основа на месте: <b>ввод города</b> и <b>отдельная функция</b> <span class="code-chip">get_weather</span>, к которой дальше привязаны все правки. Осталось подключить реальные данные.</div>
  <div class="ek-note">На <b>Правке 1</b> заменим учебные данные запросом к OpenWeather, дальше — ключи в <span class="code-chip">.env</span> и комментарий от нейросети.</div>
</div>"""},
]
