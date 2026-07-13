# -*- coding: utf-8 -*-
# Урок 8 «Работа с внешними API» · часть 4 (слайды 30–38)
# Правка 5 (цвет и ошибки) → разбор проверки cod → 2 квиза → отладка → правила (kv) → чек-лист → ДЗ → финал.
SLIDES = [
    # 30 · ПРАВКА 5 · ЦВЕТ И ОШИБКИ
    {"notes": "Финальная правка делает приложение удобнее и надёжнее: цветной вывод и корректная обработка несуществующего города. Это заметный пользовательский результат. Правка сложная: ANSI-цвета требуют аккуратности, а обработка ошибки — проверки ответа сервера. Если группа отстаёт, оставьте только обработку 404, а раскраску отдайте в ДЗ.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 5 · цвет и ошибки</div>
    <h2>Цвет и защита от <span class="acc">ошибок</span></h2>
  </div>
  <p>Финальная правка: делаем вывод цветным и учим приложение не падать на несуществующем городе.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Финальная правка. Раскрась вывод ANSI-кодами, без сторонних библиотек:
- город — голубым
- температуру — жёлтым
- комментарий нейросети — зелёным

И сделай приложение устойчивым: если такого города нет (OpenWeather вернул 404) — вежливо скажи «город не найден» и продолжи работу, без падения программы. Верни весь файл.</div>
  </div>
</div>"""},

    # 31 · РАЗБОР · ПРОВЕРЯЕМ ОТВЕТ СЕРВЕРА
    {"notes": "Ключевой слайд урока про надёжность. Подчеркните: сервер сообщает, как прошёл запрос, числом в поле cod. 200 — всё хорошо, 404 — города нет, 401 — ключ не активирован. Ответ проверяем до обращения к data['main'] — это базовое правило при работе с сетью.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Проверяем <span class="acc">ответ сервера</span></h2>
  </div>
  <p>OpenWeather в каждом ответе кладёт числовой код в поле <span class="code-chip">cod</span> — прошёл запрос или нет. Проверяем его <b>до</b> того, как достаём температуру:</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">data = requests.get(url, params=params).json()
<span class="kw">if</span> str(data[<span class="st">"cod"</span>]) != <span class="st">"200"</span>:     <span class="cm"># 200 — всё хорошо</span>
    print(<span class="st">"Город не найден"</span>)      <span class="cm"># 404 — города нет</span>
<span class="kw">else</span>:
    temp = data[<span class="st">"main"</span>][<span class="st">"temp"</span>]   <span class="cm"># только теперь читаем погоду</span>
    desc = data[<span class="st">"weather"</span>][<span class="st">0</span>][<span class="st">"description"</span>]</div>
  </div>
  <div class="ek-note ek-note--red">Если полезть в <span class="code-chip">data["main"]</span> сразу, а города нет — программа упадёт с <span class="code-chip">KeyError</span>. Сначала проверяем <span class="code-chip">cod</span>, потом читаем данные. Это общее правило для любого API.</div>
</div>"""},

    # 32 · КВИЗ 1 · .env НА GITHUB
    {"notes": "Вопрос про .env на GitHub — главная тема безопасности урока. Дайте 10–15 секунд, потом раскройте ответ. Свяжите с правилом: .env всегда в .gitignore, ключ не выкладываем.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 1</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 1</span>
    <p class="q-text">Петя выложил свой <span class="code-chip">weather.py</span> на GitHub вместе с файлом <span class="code-chip">.env</span>. На следующий день его ключ OpenWeather перестал работать: кто-то исчерпал лимит запросов. Что он сделал не так?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>Файл <span class="code-chip">.env</span> с секретными ключами <b>не выкладывают</b> в публичный репозиторий — ключи могут украсть.</p>
        <p><span class="code-chip">.env</span> добавляют в <span class="code-chip">.gitignore</span> и держат только на своём компьютере. Ключ пришлось перевыпустить.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 33 · КВИЗ 2 · КЕЛЬВИНЫ И units=metric
    {"notes": "Вопрос про Кельвины и units=metric — вторая частая ошибка с OpenWeather. Свяжите с правилом: без units=metric придут Кельвины, поэтому параметр нужен всегда.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 2</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 2</span>
    <p class="q-text">Аня запросила погоду и получила <span class="code-chip">temp = 296</span>. «На улице +20, а тут 296!» — удивилась она. Что не так и как починить?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>Без <b>units=metric</b> OpenWeather отдаёт температуру в <b>Кельвинах</b> (296 K — это примерно 23 °C).</p>
        <p>Нужно добавить в параметры <span class="code-chip">units=metric</span> — тогда придут привычные градусы Цельсия.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 34 · ОТЛАДКА · ЧИТАЕМ ОШИБКИ API
    {"notes": "Научите читать traceback снизу вверх — это пригодится на всех уроках Python. Напомните правило: непонятную ошибку целиком копируем в DeepSeek. Три проверки справа — самые частые при работе с внешним API.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Отладка</div>
    <h2>Читаем <span class="acc">ошибки</span> API</h2>
  </div>
  <div class="grid-2">
    <div class="col">
      <p><span class="hl">Traceback — снизу вверх.</span> Последняя строка — <b>что</b> случилось, строкой выше — <b>где</b>.</p>
      <div class="term" style="margin-top:14px">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
        <div class="term-body"><span class="dim">Traceback (most recent call last):
  File "weather.py", line 12, in &lt;module&gt;
    temp = data["main"]["temp"]</span>
<span class="usr">KeyError: 'main'</span></div>
      </div>
      <p style="margin-top:12px;font-size:15px"><span class="code-chip">KeyError: 'main'</span> значит: в ответе нет погоды — скорее всего города не нашли или ключ не активен.</p>
    </div>
    <div class="info-card">
      <h3>Если застряли</h3>
      <ul class="clean">
        <li>Скопируйте <b>traceback целиком</b> в чат DeepSeek — попросите объяснить и починить</li>
        <li>Код <span class="code-chip">401</span> — ключ ещё не активирован, подождите; <span class="code-chip">404</span> — проверьте название города</li>
        <li>Распечатайте весь <span class="code-chip">data</span> и посмотрите, что реально прислал сервер</li>
      </ul>
      <p style="margin-top:12px;font-size:14px;color:var(--ek-gray)">Тот же подход к отладке, что <span class="code-chip">console.log</span> в «Змейке» и print-метки на уроке 5.</p>
    </div>
  </div>
</div>"""},

    # 35 · ПРАВИЛА РАБОТЫ С API (kv)
    {"notes": "5 правил урока. Дайте сфотографировать слайд. Особо подчеркните третье и четвёртое: секреты в .env, .env в .gitignore — это базовое правило безопасности.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запомните</div>
    <h2>Правила работы с <span class="acc">API</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">01 · Запрос с параметрами</div><div class="v">Программа шлёт запрос на <span class="code-chip">url</span> с <span class="code-chip">params</span> и получает <b>JSON-ответ</b> — данные от чужого сервера.</div></div>
    <div class="kv-row"><div class="k">02 · units=metric</div><div class="v">Всегда для погоды, иначе OpenWeather отдаёт температуру в <b>Кельвинах</b>, а не в градусах Цельсия.</div></div>
    <div class="kv-row"><div class="k">03 · Секреты — в .env</div><div class="v">Ключи читаем через <span class="code-chip">load_dotenv</span> и <span class="code-chip">os.getenv</span>. В коде ключа строкой быть не должно.</div></div>
    <div class="kv-row"><div class="k">04 · .env — в .gitignore</div><div class="v">Файл с ключами не выкладываем в публичный репозиторий: украдут — придётся перевыпускать.</div></div>
    <div class="kv-row"><div class="k">05 · Проверяй код ответа</div><div class="v">Смотрим <span class="code-chip">cod</span>: <span class="code-chip">200</span> — данные есть, <span class="code-chip">404</span> — города нет. Читаем данные только после проверки.</div></div>
  </div>
</div>"""},

    # 36 · ЧЕК-ЛИСТ
    {"notes": "Чек-лист завершения приложения погоды. Кто отметил всё, пусть проверит два-три города и один несуществующий. Это проверяет, что запрос и обработка ошибки работают. Обязательный минимум к 55-й минуте — Правки 1–3 (город+погода, .env, AI-комментарий). При отставании Правки 4–5 (совет и цикл, цвет и обработка 404) уходят в ДЗ.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Чек-лист</div>
    <h2>Готовность <span class="acc">к 55-й минуте</span></h2>
  </div>
  <div class="grid-2">
    <div class="info-card">
      <h3 style="color:var(--ek-green-deep)">Готово</h3>
      <ul class="clean">
        <li><span class="code-chip">weather.py</span> запускается командой <span class="code-chip">python weather.py</span></li>
        <li>Ввёл город — пришла текущая погода из интернета</li>
        <li>Ключи лежат в <span class="code-chip">.env</span>, в коде их нет</li>
        <li>Нейросеть комментирует погоду</li>
      </ul>
    </div>
    <div class="info-card">
      <h3 style="color:var(--ek-violet-deep)">Работает</h3>
      <ul class="clean">
        <li>Программа спрашивает город по кругу до «выход»</li>
        <li>Нейросеть советует, что надеть</li>
        <li>Вывод цветной</li>
        <li>Несуществующий город — «город не найден», без падения</li>
      </ul>
    </div>
  </div>
  <div class="ek-note ek-note--green">Всё отмечено? Проверьте три реальных города и один выдуманный — приложение погоды готово.</div>
</div>"""},

    # 37 · ДЗ
    {"notes": "ДЗ — доработать приложение погоды, примерно 30 минут. Каждое улучшение — отдельный диалог с DeepSeek, не всё сразу. Напомните про ключи на скриншотах.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Домашнее задание · около 30 минут</div>
    <h2>Доработайте <span class="acc">приложение погоды</span></h2>
  </div>
  <p>Три улучшения — каждое через отдельный диалог с DeepSeek:</p>
  <div class="grid-3">
    <div class="info-card">
      <h3>Прогноз на завтра</h3>
      <p>Через диалог с DeepSeek подключите <span class="code-chip">forecast</span>-эндпоинт OpenWeather и покажите погоду не только сейчас, но и на завтра.</p>
    </div>
    <div class="info-card">
      <h3>Эмодзи погоды</h3>
      <p>Пусть программа рисует эмодзи по погоде: ☀️ ясно, 🌧️ дождь, ❄️ снег — по описанию из ответа API.</p>
    </div>
    <div class="info-card">
      <h3>Битва городов</h3>
      <p>Сравните погоду в двух городах и попросите нейросеть решить, где сегодня приятнее.</p>
    </div>
  </div>
  <div class="ek-note ek-note--red">Пришлите скриншот приложения с погодой — <b>ключи скройте!</b> Ваш самый удачный промпт — отдельным сообщением.</div>
</div>"""},

    # 38 · ФИНАЛ · МОДУЛЬ 2 ЗАКРЫТ
    {"cls": "slide--green",
     "notes": "Закройте урок и весь модуль 2. Сегодня программа впервые взяла реальные данные из интернета и перенесла ключи в .env. На уроке 9 (модуль 3) добавим интерфейс в Telegram: соберём бота, который отвечает через нейросеть.",
     "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">A</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">P</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">I</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">E</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="bubble">
      <h1>До встречи<br>на уроке 9!</h1>
      <p>Модуль 2 закрыт: сегодня программа впервые взяла реальные данные из интернета через API и перенесла ключи в <span class="code-chip">.env</span>. На уроке 9 добавим интерфейс в мессенджере — соберём Telegram-бота, который отвечает через нейросеть.</p>
    </div>
  </div>"""},
]
