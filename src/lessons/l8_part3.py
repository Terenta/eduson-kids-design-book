# -*- coding: utf-8 -*-
SLIDES = [
    # 20 · TROUBLESHOOTING ЗАПУСКА
    {"notes": "Коротко разберите пять ситуаций. Чаще всего свежий ключ OpenWeather ещё не активировался (401) или файл .env лежит не рядом со скриптом. Тем, у кого не запускается, помогите лично; остальные сверяются со слайдом.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Если приложение не запустилось</div>
    <h2>Типичные ситуации <span class="acc">запуска</span></h2>
  </div>
  <div class="kv" style="margin-top:6px">
    <div class="kv-row"><div class="k">401 Unauthorized</div><div class="v">Ключ OpenWeather ещё не активировался — после регистрации до пары часов. Подождите или возьмите рабочий ключ у преподавателя.</div></div>
    <div class="kv-row"><div class="k">KeyError</div><div class="v">Не пришло поле — например, ошиблись в названии города. Загляните в <span class="code-chip">data</span>: возможно, там сообщение об ошибке, а не погода.</div></div>
    <div class="kv-row"><div class="k">ModuleNotFoundError</div><div class="v">Не установлены библиотеки. В терминале: <span class="code-chip">pip install requests python-dotenv</span> — и запускайте снова.</div></div>
    <div class="kv-row"><div class="k">Нет интернета</div><div class="v"><span class="code-chip">requests</span> не достучался до сервера. Проверьте соединение — API живёт в интернете, без сети погоды не будет.</div></div>
    <div class="kv-row"><div class="k">Ключ пустой (None)</div><div class="v">Файл <span class="code-chip">.env</span> лежит не рядом со скриптом или в нём опечатка в имени. Положите <span class="code-chip">.env</span> в ту же папку, что и <span class="code-chip">weather.py</span>.</div></div>
  </div>
</div>"""},

    # 21 · ПРАВКА 1 · настоящая погода
    {"notes": "Первая правка идёт в тот же чат: заменяем учебные данные в get_weather настоящим запросом к OpenWeather. После неё программа печатает температуру из интернета по введённому городу. Дождитесь, пока у всех появилась погода по своему городу, потом переходите дальше.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 1 · настоящая погода</div>
    <h2>Подключаем запрос к <span class="acc">OpenWeather</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:8px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Замени заглушку внутри get_weather(city) на настоящий запрос к OpenWeather, остальное не меняй:
— запроси погоду через requests.get (url https://api.openweathermap.org/data/2.5/weather, параметры q=city, appid=КЛЮЧ, units=metric, lang=ru)
— разбери JSON-ответ и верни настоящую температуру и описание погоды
— распечатай их для введённого города

Ключ пока впиши строкой. Верни весь файл целиком.</div>
  </div>
</div>"""},

    # 22 · РАЗБОР КОДА · запрос погоды
    {"notes": "Дайте минимум теории про API. Главное: параметры складываем в словарь params, requests сам собирает адрес, .json() превращает ответ в словарь. Покажите на экране, что URL не собирали вручную.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Как программа <span class="acc">спрашивает погоду</span></h2>
  </div>
  <div class="code-win" style="margin-top:6px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">url = <span class="st">"https://api.openweathermap.org/data/2.5/weather"</span>
params = {<span class="st">"q"</span>: city, <span class="st">"appid"</span>: OW_KEY, <span class="st">"units"</span>: <span class="st">"metric"</span>, <span class="st">"lang"</span>: <span class="st">"ru"</span>}
data = requests.get(url, params=params).json()   <span class="cm"># ответ сервера как словарь</span>
temp = data[<span class="st">"main"</span>][<span class="st">"temp"</span>]
desc = data[<span class="st">"weather"</span>][0][<span class="st">"description"</span>]</div>
  </div>
  <p>Параметры складываем в словарь <span class="code-chip">params</span>, а <span class="code-chip">requests.get</span> сам собирает из них адрес — вручную URL не склеиваем. <span class="code-chip">.json()</span> превращает ответ сервера в обычный <span class="hl">словарь Python</span>, и мы достаём из него нужные поля.</p>
</div>"""},

    # 23 · ПРАВКА 2 · ключи в .env
    {"notes": "Ключевая правка про безопасность: ключи переезжают из кода в файл .env. После неё в коде остаётся только чтение ключей через переменные окружения. Проверьте у каждого, что .env лежит рядом со скриптом и погода по-прежнему приходит. DEEPSEEK_KEY кладём в .env заранее вместе с ключом OpenWeather: он понадобится на следующей правке для AI-комментария.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 2 · ключи в .env</div>
    <h2>Переносим ключи в <span class="acc">.env</span></h2>
  </div>
  <p>Главный шаг к безопасности: секретные ключи переходят из кода в отдельный файл <span class="code-chip">.env</span> — как пароль, который не пишут в открытом тексте.</p>
  <div class="prompt-card prompt-card--copy">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Спрячь ключи. Создай рядом файл .env со строками OPENWEATHER_KEY=... и DEEPSEEK_KEY=..., а в коде читай их через библиотеку python-dotenv (load_dotenv, os.getenv). В коде не должно остаться ключей строкой.

Верни весь файл целиком.</div>
  </div>
</div>"""},

    # 24 · РАЗБОР КОДА · ключи из файла
    {"notes": "Минимум теории про секреты. Главное: load_dotenv читает файл, os.getenv достаёт ключ по имени, в коде ключа строкой больше нет. Откройте .env в VS Code — покажите две строки с ключами. Напомните про .gitignore.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Как ключи попадают в код <span class="acc">из файла</span></h2>
  </div>
  <div class="code-win" style="margin-top:6px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">from</span> dotenv <span class="kw">import</span> load_dotenv
<span class="kw">import</span> os
load_dotenv()                          <span class="cm"># прочитали файл .env</span>
OW_KEY = os.getenv(<span class="st">"OPENWEATHER_KEY"</span>)  <span class="cm"># достали ключ по имени</span>
DS_KEY = os.getenv(<span class="st">"DEEPSEEK_KEY"</span>)</div>
  </div>
  <div class="ek-note ek-note--green"><span class="code-chip">load_dotenv()</span> читает файл <span class="code-chip">.env</span>, а <span class="code-chip">os.getenv</span> достаёт ключ по имени. Теперь <b>ключа строкой в коде нет</b> — код можно показывать и выкладывать, а <span class="code-chip">.env</span> добавляют в <span class="code-chip">.gitignore</span> и держат только у себя.</div>
</div>"""},

    # 25 · ПОЛЕЗНОЕ ЗНАНИЕ · units=metric
    {"notes": "Зафиксируйте, зачем нужен units=metric. Уберите его в чьём-нибудь коде и покажите 296 вместо 23 — разница понятна сразу. Это частая ошибка, она вернётся в квизе.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Полезное знание</div>
    <h2>Один параметр для <span class="acc">привычной температуры</span></h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>Без units=metric</h4>
      <p>OpenWeather отдаёт градусы Кельвина: <span class="code-chip">temp = 296</span>.</p>
      <p class="note">На улице +23, но без параметра приходит 296.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>С units=metric, lang=ru</h4>
      <p>Приходят привычные градусы Цельсия: <span class="code-chip">temp = 23</span>.</p>
      <p class="note">А <span class="code-chip">lang=ru</span> делает описание русским.</p>
    </div>
  </div>
  <p>Кельвины — шкала физиков: <span class="code-chip">296 K − 273 ≈ 23 °C</span>. С параметром <span class="code-chip">units=metric</span> температура приходит в привычном виде.</p>
</div>"""},

    # 26 · ПРАВКА 3 · AI-комментарий
    {"notes": "Ключевая правка урока: погода уходит в DeepSeek, а нейросеть формулирует комментарий. Это видимый результат: под числовыми данными появляется текстовое объяснение. Раздайте ключи заранее и проверьте интернет.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 3 · AI-комментарий</div>
    <h2>Нейросеть <span class="acc">комментирует погоду</span></h2>
  </div>
  <p>Программа берёт текущую погоду и передаёт её нейросети, чтобы получить короткий комментарий к данным.</p>
  <div class="prompt-card prompt-card--copy">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Отправь погоду в DeepSeek с системной ролью «Ты весёлый ведущий прогноза погоды, прокомментируй погоду одним бодрым абзацем» и распечатай ответ нейросети под данными о погоде. Ключ DeepSeek бери из .env.

Верни весь файл целиком.</div>
  </div>
</div>"""},

    # 27 · РАЗБОР КОДА · передаём погоду нейросети
    {"notes": "Свяжите с уроками 5-7: тот же запрос к DeepSeek, но в user-сообщение подставляем текущую погоду. Системная роль задаёт стиль ответа. Ответ печатаем под данными. Не углубляйтесь в каждое поле.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Передаём погоду <span class="acc">нейросети</span></h2>
  </div>
  <div class="code-win" style="margin-top:6px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">data = {
    <span class="st">"model"</span>: <span class="st">"deepseek-chat"</span>,
    <span class="st">"messages"</span>: [
        {<span class="st">"role"</span>: <span class="st">"system"</span>, <span class="st">"content"</span>: <span class="st">"Ты весёлый ведущий прогноза погоды, прокомментируй погоду одним бодрым абзацем."</span>},
        {<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: <span class="st">f"Город {city}: {temp} градусов, {desc}."</span>},
    ],
}
response = requests.post(url, headers=headers, json=data)
answer = response.json()[<span class="st">"choices"</span>][0][<span class="st">"message"</span>][<span class="st">"content"</span>]</div>
  </div>
  <p>Системная роль задаёт стиль ответа — <span class="hl">ведущий прогноза</span>. В <span class="code-chip">user</span>-сообщение подставляем текущую погоду: город, температуру и описание. Нейросеть возвращает короткий комментарий, и мы печатаем его под данными.</p>
</div>"""},

    # 28 · ПРАВКА 4 · совет и цикл
    {"notes": "Правка 4 превращает разовый запуск в приложение с циклом: город спрашивается по кругу, а к каждой погоде нейросеть советует, что надеть. Дайте ученикам проверить разные города и выйти по слову «выход».", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 4 · совет и цикл</div>
    <h2>Спрашиваем город <span class="acc">по кругу</span></h2>
  </div>
  <p>Разовый запуск превращаем в приложение: город спрашивается снова и снова, а к каждой погоде нейросеть советует, что надеть.</p>
  <div class="prompt-card prompt-card--copy">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Спрашивай город по кругу, пока не введут «выход». К каждой погоде проси у нейросети короткий совет, что надеть.

Верни весь файл целиком.</div>
  </div>
</div>"""},

    # 29 · РАЗБОР КОДА · цикл и совет
    {"notes": "Главная мысль урока: программа работает в цикле с внешним API. Цикл while идёт до слова «выход», второй запрос к DeepSeek даёт совет. Дайте сфотографировать. Если группа отстаёт, правку 5 можно перенести в ДЗ.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Круг вопросов и <span class="acc">совет от нейросети</span></h2>
  </div>
  <div class="code-win" style="margin-top:6px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">while</span> <span class="kw">True</span>:
    city = input(<span class="st">"Город (или «выход»): "</span>)
    <span class="kw">if</span> city == <span class="st">"выход"</span>:
        <span class="kw">break</span>
    <span class="cm"># ... запросили погоду и комментарий ...</span>
    advice = ask_ai(<span class="st">f"Погода {temp} градусов, {desc}. Что надеть? Коротко."</span>)
    print(advice)</div>
  </div>
  <div class="ek-note">Цикл <span class="code-chip">while True</span> спрашивает город снова и снова, пока не введут <span class="code-chip">«выход»</span> — тогда <span class="code-chip">break</span> выходит. Для совета делаем <b>второй запрос</b> к нейросети: погода уходит к DeepSeek уже с вопросом, что надеть.</div>
</div>"""},
]
