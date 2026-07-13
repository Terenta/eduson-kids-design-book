# -*- coding: utf-8 -*-
SLIDES = [
    # 1 · ТИТУЛ
    {"cls": "slide--violet", "notes": "Поприветствуйте. Сегодня соберём приложение погоды: программа спрашивает город, получает текущую погоду через внешний сервис OpenWeather, а нейросеть формулирует комментарий. Новое — работа с внешним сервером через API и безопасное хранение секретных ключей в файле .env. Это последний урок модуля 2.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">A</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">P</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">I</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">W</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="cover-card">
      <div class="badge">Урок №8</div>
      <div class="card-top"><span class="win-dots"><i></i><i></i><i></i></span><span class="win-close"></span></div>
      <h1>Работа<br>с&nbsp;внешними API</h1>
      <p class="cover-sub">Соберём приложение погоды: программа узнаёт текущую погоду в городе через OpenWeather, нейросеть формулирует комментарий, а секретные ключи хранятся в файле .env.</p>
      <div class="cover-chips"><span class="chip">API</span><span class="chip chip--green">OpenWeather</span><span class="chip chip--gray">.env</span><span class="chip chip--gray">DeepSeek</span></div>
    </div>
  </div>"""},

    # 2 · ПЛАН
    {"notes": "План. Теории даём ровно столько, сколько нужно для практики: к 12-й минуте в терминале появляется реальная температура из интернета, к 30-й — каркас приложения погоды. Дальше — 5 последовательных правок, как на прошлых уроках. Это последнее занятие модуля 2.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Agenda · план занятия</div>
    <h2>Как пройдут <span class="acc">60 минут</span></h2>
  </div>
  <div class="agenda">
    <div class="agenda-row"><span class="t">0–5</span><div><div class="tt">Разбор ДЗ</div><div class="dd">Смотрим доработанные дневники: статистика по тегам, экспорт в Markdown, умный поиск.</div></div></div>
    <div class="agenda-row"><span class="t">5–12</span><div><div class="tt">API и .env</div><div class="dd">Коротко разбираем только то, что нужно для приложения погоды.</div></div></div>
    <div class="agenda-row"><span class="t">12–20</span><div><div class="tt">Промпт-разминка</div><div class="dd">warmup.py: живая погода Москвы из интернета через OpenWeather.</div></div></div>
    <div class="agenda-row"><span class="t">20–30</span><div><div class="tt">Каркас weather.py</div><div class="dd">Ввод города, запрос к OpenWeather, ключи в .env.</div></div></div>
    <div class="agenda-row"><span class="t">30–48</span><div><div class="tt">5 правок через диалог</div><div class="dd">Погода по городу → ключи в .env → AI-комментарий → совет и цикл → цвет и ошибки.</div></div></div>
    <div class="agenda-row"><span class="t">48–55</span><div><div class="tt">Мини-вопросы и отладка</div><div class="dd">Читаем ошибки API, проверяем понимание.</div></div></div>
    <div class="agenda-row"><span class="t">55–60</span><div><div class="tt">Демо в группе</div><div class="dd">Каждый узнаёт погоду в своём городе и получает комментарий нейросети.</div></div></div>
  </div>
</div>"""},

    # 3 · РАЗБОР ДЗ
    {"notes": "Откройте 1–2 доработанных дневника (на весь блок 5 минут). Разбирайте диалог с нейросетью, а не только результат. Подведите к главному: до сих пор данные создавали ученик, программа или нейросеть — записи, теги, историю. Сегодня программа впервые возьмёт реальные данные из интернета.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор ДЗ урока 7</div>
    <h2>Смотрим доработанные <span class="acc">дневники</span></h2>
  </div>
  <p>Открываем 2–3 присланных дневника и разбираем именно <span class="hl">диалог с нейросетью</span>: статистика по тегам, экспорт в <span class="code-chip">diary.md</span>, умный поиск по слову в тексте.</p>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card">
      <h3>Что сработало</h3>
      <p>Точечные правки: подсчёт тегов через словарь-счётчик, экспорт записей в Markdown, поиск по вхождению слова.</p>
    </div>
    <div class="info-card">
      <h3>Что переделывали</h3>
      <p>Где забыли «верни весь файл» — нейросеть присылала кусок, и терялись прежние функции дневника.</p>
    </div>
    <div class="info-card">
      <h3>Вывод</h3>
      <p>Данные для дневника <b>придумывали мы сами</b>. Сегодня программа впервые возьмёт <b>реальные данные из интернета</b>.</p>
    </div>
  </div>
</div>"""},

    # 4 · ИДЕЯ УРОКА
    {"notes": "Главная мысль: две новинки. Первая — программа впервые берёт актуальные данные из внешнего сервиса в интернете через API и передаёт их нейросети для комментария. Вторая — ключи переносим в файл .env, как обещали на уроке 7.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Идея урока</div>
    <h2>Программа получает данные из <span class="acc">интернета</span></h2>
  </div>
  <p>Раньше данные придумывала сама программа или нейросеть — записи, историю, теги. Сегодня программа берёт <span class="hl">реальные данные из внешнего сервиса</span>: погоду прямо сейчас.</p>
  <div class="ek-note" style="margin-top:6px">Программа впервые общается с внешним сервером через <b>API</b>: запрашивает у OpenWeather погоду в городе и <b>передаёт её нейросети</b> для комментария. Вторая новинка — секретные ключи храним <b>в файле .env</b>.</div>
  <p>Идея урока 8: <b>берём актуальные данные</b> из интернета, <b>передаём их нейросети</b>, а ключи <b>держим в .env</b>.</p>
</div>"""},

    # 5 · ЧТО ТАКОЕ API
    {"notes": "API — способ одной программы запросить данные у внешнего сервера. Аналогия: заказ по меню. Вы не идёте на кухню — выбираете позицию по меню и получаете готовое блюдо. Программа не работает внутри OpenWeather — отправляет запрос по правилам и получает JSON-ответ.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Новое понятие</div>
    <h2>Что такое <span class="acc">API</span></h2>
  </div>
  <p>API — это <span class="hl">способ попросить данные у чужого сервера</span> по понятным обеим сторонам правилам. Программа отправляет <b>запрос с параметрами</b> — сервер возвращает <b>JSON-ответ</b>.</p>
  <div class="ek-note" style="margin-top:6px">Как <b>заказ по меню</b>: вы не идёте на кухню, а выбираете позицию по меню и получаете готовое блюдо. Программа не работает внутри OpenWeather: отправляет запрос по правилам и получает готовые данные о погоде.</div>
  <p>JSON-ответ вам уже знаком — точно такой формат разбирали на уроке 7 в дневнике.</p>
</div>"""},

    # 6 · УСТРОЙСТВО ЗАПРОСА
    {"notes": "Показываем устройство запроса, не углубляясь. url — адрес сервиса погоды, params — что именно спрашиваем: q — город, appid — ключ, units — единицы, lang — язык ответа. Главное правило урока: units=metric, иначе придут Кельвины (296 вместо +23). requests.get сам собирает адрес — вручную URL не склеиваем.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как устроен запрос</div>
    <h2>Из чего состоит обращение к <span class="acc">API</span></h2>
  </div>
  <p>У запроса два куска: <span class="hl">url</span> — адрес сервиса погоды, и <span class="hl">params</span> — что именно спрашиваем.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">url = <span class="st">"https://api.openweathermap.org/data/2.5/weather"</span>
params = {<span class="st">"q"</span>: city, <span class="st">"appid"</span>: OW_KEY, <span class="st">"units"</span>: <span class="st">"metric"</span>, <span class="st">"lang"</span>: <span class="st">"ru"</span>}
data = requests.get(url, params=params).json()</div>
  </div>
  <div class="kv" style="margin-top:12px">
    <div class="kv-row"><div class="k">q</div><div class="v">Город, о котором спрашиваем.</div></div>
    <div class="kv-row"><div class="k">appid</div><div class="v">Ключ — пропуск к сервису.</div></div>
    <div class="kv-row"><div class="k">units=metric</div><div class="v">Градусы Цельсия, а не Кельвины.</div></div>
    <div class="kv-row"><div class="k">lang=ru</div><div class="v">Описание погоды по-русски.</div></div>
  </div>
</div>"""},

    # 7 · ЧТО ТАКОЕ .env
    {"notes": "Вторая линия урока. Ключ — это пароль к сервису, в коде строкой ему не место: если выложить код на GitHub, ключ могут украсть. Секреты кладём в отдельный файл .env рядом со скриптом, читаем через load_dotenv и os.getenv, а сам .env добавляем в .gitignore, чтобы он не попал в публичный репозиторий.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Прячем секреты</div>
    <h2>Что такое файл <span class="acc">.env</span></h2>
  </div>
  <p>Ключ — это <span class="hl">пароль к сервису</span>. Держать его строкой прямо в коде опасно: выложите код в интернет — ключ украдут и исчерпают ваш лимит.</p>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>Ключ строкой в коде</h4>
      <p>appid = "a1b2c3..." прямо в файле. Виден всем, кто увидит код.</p>
    <p class="note">Так делать небезопасно.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>Ключ в файле .env</h4>
      <p>Секреты лежат рядом со скриптом, в код не попадают. <span class="code-chip">load_dotenv()</span> и <span class="code-chip">os.getenv(...)</span> читают их из .env.</p>
      <p class="note">.env добавляем в .gitignore — в интернет он не уходит.</p>
    </div>
  </div>
  <p>В коде ключа строкой быть не должно — только чтение из <span class="code-chip">.env</span>.</p>
</div>"""},

    # 8 · ПРОМПТ #1 РАЗМИНКА
    {"notes": "Без долгой подготовки: сразу просим у DeepSeek небольшой скрипт с запросом к OpenWeather и запускаем. Ключ на разминке пока строкой — перенос в .env будет в основном проекте. Ученики копируют промпт целиком. Ключ OpenWeather раздайте заранее — он активируется не мгновенно.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #1 · разминка</div>
    <h2>warmup.py за <span class="acc">две минуты</span></h2>
  </div>
  <p>Начнём с короткого скрипта: попросим DeepSeek сделать запрос к OpenWeather и сразу запустим результат в терминале.</p>
  <div class="prompt-card" style="margin-top:14px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — опытный Python-разработчик и наставник школьника. Напиши маленький скрипт warmup.py: он делает запрос к публичному API https://api.openweathermap.org/data/2.5/weather с параметрами q=Москва, appid=КЛЮЧ, units=metric, lang=ru через библиотеку requests, разбирает JSON-ответ и печатает температуру и описание погоды. Ключ пока впиши строкой. Только requests. Прокомментируй код, ответь одним блоком.</div>
  </div>
</div>"""},

    # 9 · ЗАПУСК И РАЗБОР
    {"notes": "Базовый шаг урока: дождитесь, пока у всех в терминале появится реальная температура из интернета. На рабочем коде показываем три вещи: requests.get(...).json(), поле data['main']['temp'] и data['weather'][0]['description']. Не переходите дальше, пока скрипт не запустился у каждого. Сначала результат, затем разбор.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск и разбор</div>
    <h2>Реальная погода из <span class="acc">интернета</span></h2>
  </div>
  <div class="grid-2">
    <div class="col">
      <ol class="steps steps--tight">
        <li><div>В <span class="code-chip">vibe-coding</span> создайте папку <span class="code-chip">lesson-08</span></div></li>
        <li><div>Создайте <span class="code-chip">warmup.py</span> и вставьте код из ответа</div></li>
        <li><div>Впишите выданный ключ OpenWeather вместо <span class="code-chip">КЛЮЧ</span></div></li>
        <li><div>Выполните <span class="code-chip">python warmup.py</span> и смотрите на температуру</div></li>
      </ol>
      <div class="ek-note ek-note--green" style="margin-top:14px;font-size:15px">В терминале реальная температура в Москве прямо сейчас? Внешний API работает — база приложения погоды готова.</div>
    </div>
    <div class="kv">
      <div class="kv-row"><div class="k">requests.get(...)</div><div class="v">Отправил запрос на сервер OpenWeather.</div></div>
      <div class="kv-row"><div class="k">.json()</div><div class="v">Разобрал ответ в словарь Python.</div></div>
      <div class="kv-row"><div class="k">data["main"]["temp"]</div><div class="v">Достал температуру из ответа.</div></div>
      <div class="kv-row"><div class="k">data["weather"][0]["description"]</div><div class="v">Достал описание погоды.</div></div>
    </div>
  </div>
</div>"""},

    # 10 · TROUBLESHOOTING
    {"notes": "Разберите три типичные проблемы запуска. Самая частая — 401: ключ ещё не активировался (до пары часов после регистрации), поэтому раздавайте ключи заранее. Исправьте ошибки у всех: этот же ключ и эта же папка нужны дальше для приложения.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Типичные ситуации запуска</div>
    <h2>Если warmup.py <span class="acc">не запустился</span></h2>
  </div>
  <div class="grid-3" style="margin-top:8px">
    <div class="ek-note ek-note--red"><b>401 Unauthorized</b><br>Ключ неверный или ещё не активировался (это до пары часов после регистрации). Проверьте, что вставили выданный ключ без пробелов.</div>
    <div class="ek-note ek-note--red"><b>KeyError</b><br>В ответе нет ожидаемого поля — обычно город написан с ошибкой или сервер вернул ошибку вместо погоды. Проверьте название города.</div>
    <div class="ek-note ek-note--red"><b>ConnectionError</b><br>Нет интернета или сервис недоступен. Проверьте соединение и запустите <span class="code-chip">python warmup.py</span> заново.</div>
  </div>
</div>"""},
]
