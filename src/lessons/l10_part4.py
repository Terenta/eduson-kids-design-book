# -*- coding: utf-8 -*-
# Урок 10 «Своё веб-приложение в интернете» · часть 4 (слайды 30–38)
# Правка 5 (публикация) → разбор Secrets → 2 квиза → отладка → привычки → чек-лист → ДЗ → финал.
SLIDES = [
    # 30 · ПРАВКА 5 · ПУБЛИКАЦИЯ (для успевающих)
    {"notes": "Опциональный финальный шаг: локальное приложение превращается в сайт с публичной ссылкой. Правка объёмная — нужны аккаунты GitHub и Streamlit Cloud, поэтому она для успевающих. Если не хватает времени или доступов, продемонстрируйте деплой со своего экрана или отдайте в ДЗ, а обязательный результат урока — готовый локальный чат с AI (правки 1–4) — уже достигнут. Главный смысл следующего слайда: код попадает на публичный GitHub, поэтому ключа в нём быть не должно. Имя переменной ключа сквозное — API_KEY.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 5 · публикация · для успевающих</div>
    <h2>Свой сайт с <span class="acc">публичной ссылкой</span></h2>
  </div>
  <p>Опциональный шаг для тех, кто закончил локальный чат: заливаем проект на GitHub и получаем публичную ссылку через Streamlit Cloud.</p>
  <div style="display:flex;gap:10px;flex-wrap:wrap"><span class="chip">GitHub</span><span class="chip chip--gray">requirements.txt</span><span class="chip chip--green">Streamlit Cloud</span></div>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Подготовь к публикации: залей проект на GitHub, добавь requirements.txt (streamlit, requests), задеплой на Streamlit Cloud (share.streamlit.io). Ключ DeepSeek положи в Secrets и читай в код так: API_KEY = st.secrets["DEEPSEEK_KEY"]. Дай пошаговую инструкцию. Верни весь файл.</div>
  </div>
</div>"""},

    # 31 · РАЗБОР · КЛЮЧ В SECRETS, НЕ В КОДЕ
    {"notes": "Ключевой слайд урока. Подчеркните главное: app.py попадает на публичный GitHub, значит ключ в коде увидят все. Имя переменной сквозное — API_KEY: та же, что в ask_deepseek. В облаке ключ берётся из st.secrets, локально — из os.getenv (файл .env). На Streamlit Cloud секрет кладут в раздел Secrets в формате toml. Если это пропустить, ученики могут случайно опубликовать ключ.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Ключ — в <span class="acc">Secrets</span>, не в коде</h2>
  </div>
  <p>Файл <span class="code-chip">app.py</span> попадает на <span class="hl">публичный GitHub</span> — всё, что в нём написано, увидят посторонние. Ключ, попавший в код, увидят все. Читаем его в ту же переменную <span class="code-chip">API_KEY</span>, что и в <span class="code-chip">ask_deepseek</span>:</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">import</span> os
<span class="kw">import</span> streamlit <span class="kw">as</span> st

<span class="cm"># в облаке — из Secrets, локально — из .env</span>
API_KEY = st.secrets.get(<span class="st">"DEEPSEEK_KEY"</span>) <span class="kw">or</span> os.getenv(<span class="st">"DEEPSEEK_KEY"</span>)</div>
  </div>
  <p>Сам ключ живёт в панели Streamlit Cloud, в разделе <span class="hl">Secrets</span>, в формате <span class="code-chip">toml</span>:</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">TOML</span></div>
    <div class="code-body">DEEPSEEK_KEY = <span class="st">"sk-..."</span></div>
  </div>
  <div class="ek-note ek-note--red">Никогда не пишите <span class="code-chip">API_KEY = "sk-..."</span> прямо в <span class="code-chip">app.py</span>. На хостинге секрет кладут в Secrets и читают через <span class="code-chip">st.secrets["DEEPSEEK_KEY"]</span> — тогда на GitHub попадает только код, без ключа.</div>
</div>"""},

    # 32 · MINI-QUIZ 1
    {"notes": "Вопрос про ключ в коде — прямое следствие предыдущего слайда. Дайте 10–15 секунд, потом раскройте ответ. Свяжите с привычкой: ключ никогда не в коде, всегда в Secrets.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 1</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 1</span>
    <p class="q-text">Оля добавила в <span class="code-chip">app.py</span> строку <span class="code-chip">API_KEY = "sk-..."</span>. Приложение работает локально, но перед публикацией на GitHub наставник сказал так не делать. Почему и как правильно?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p><span class="code-chip">app.py</span> заливается на <b>публичный GitHub</b> — ключ увидят все. На Streamlit Cloud секреты кладут в раздел <b>Secrets</b> (панель хостинга), а в коде читают через <span class="code-chip">st.secrets["DEEPSEEK_KEY"]</span>.</p>
        <p>Ключа в коде быть не должно.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 33 · MINI-QUIZ 2
    {"notes": "Вопрос про session_state — вторая ключевая идея урока. Свяжите с привычкой: Streamlit перезапускает весь скрипт, память диалога живёт в st.session_state.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 2</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 2</span>
    <p class="q-text">Максим заметил: при каждом вопросе Streamlit будто запускает скрипт заново, и без <span class="code-chip">st.session_state</span> переписка стирается. Зачем нужен <span class="code-chip">session_state</span>?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>Streamlit <b>перезапускает весь</b> <span class="code-chip">app.py</span> при каждом действии пользователя. Обычные переменные обнуляются.</p>
        <p><span class="code-chip">st.session_state</span> хранит данные (историю чата) между перезапусками — поэтому переписка не теряется.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 34 · ОТЛАДКА
    {"notes": "Научите читать traceback снизу вверх — пригодится на всех уроках Python. Напомните привычку: непонятную ошибку целиком копируем в DeepSeek. Три поломки справа — самые частые именно на Streamlit Cloud.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Отладка</div>
    <h2>Читаем <span class="acc">ошибки</span> Streamlit</h2>
  </div>
  <div class="grid-2">
    <div class="col">
      <p><span class="hl">Traceback — снизу вверх.</span> Последняя строка — <b>что</b> случилось, строкой выше — <b>где</b>.</p>
      <div class="term" style="margin-top:14px">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
        <div class="term-body"><span class="dim">Traceback (most recent call last):
  File "app.py", line 5, in &lt;module&gt;
    API_KEY = st.secrets["DEEPSEEK_KEY"]</span>
<span class="usr">KeyError: 'DEEPSEEK_KEY'</span></div>
      </div>
      <p style="margin-top:12px;font-size:15px"><span class="code-chip">KeyError</span> значит: секрет не добавлен в Secrets на Cloud.</p>
    </div>
    <div class="info-card">
      <h3>Если застряли</h3>
      <ul class="clean">
        <li>Скопируйте <b>traceback целиком</b> в чат DeepSeek — попросите объяснить и починить</li>
        <li><span class="code-chip">ModuleNotFoundError</span> на Cloud — забыли <span class="code-chip">requirements.txt</span> со списком библиотек</li>
        <li>Приложение «спит» на бесплатном тарифе — нажмите кнопку «wake up» и подождите</li>
      </ul>
      <p style="margin-top:12px;font-size:14px;color:var(--ek-gray)">Та же привычка, что <span class="code-chip">console.log</span> в «Змейке» и print-метки на прошлых уроках.</p>
    </div>
  </div>
</div>"""},

    # 35 · ПРИВЫЧКИ
    {"notes": "5 привычек урока. Дайте сфотографировать слайд. Особо подчеркните вторую (память в session_state) и третью (ключ в Secrets) — это две главные идеи урока.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запомните</div>
    <h2>Привычки работы со <span class="acc">Streamlit</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">01 · Streamlit = Python как сайт</div><div class="v">Виджеты <span class="code-chip">st.title</span>, <span class="code-chip">st.chat_input</span>, <span class="code-chip">st.write</span> рисуют страницу — HTML писать не нужно.</div></div>
    <div class="kv-row"><div class="k">02 · Память — в session_state</div><div class="v">Streamlit перезапускает весь скрипт. Историю чата храним в <span class="code-chip">st.session_state</span>, иначе она стирается.</div></div>
    <div class="kv-row"><div class="k">03 · Ключ — не в коде</div><div class="v">Всегда в Secrets, читаем через <span class="code-chip">st.secrets["DEEPSEEK_KEY"]</span>. На GitHub попадает только код.</div></div>
    <div class="kv-row"><div class="k">04 · requirements.txt</div><div class="v">Список библиотек, чтобы Streamlit Cloud их поставил. Без него — <span class="code-chip">ModuleNotFoundError</span>.</div></div>
    <div class="kv-row"><div class="k">05 · Публикация = ссылка</div><div class="v">GitHub плюс Streamlit Cloud дают свою ссылку — сайт открывается с любого устройства.</div></div>
  </div>
</div>"""},

    # 36 · ЧЕК-ЛИСТ
    {"notes": "Чек-лист завершения приложения. Левая колонка — обязательный минимум (правки 1–4): рабочий локальный AI-чат к 48–55-й минуте. Правая колонка — публикация, только для успевающих; кто дошёл до ссылки, пусть откроет её на телефоне и задаст вопрос. Остальным публикация уходит в ДЗ.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Чек-лист</div>
    <h2>Что должно быть к <span class="acc">55-й минуте</span></h2>
  </div>
  <div class="grid-2">
    <div class="info-card">
      <h3 style="color:var(--ek-green-deep)">Обязательно · локальный чат</h3>
      <ul class="clean">
        <li><span class="code-chip">app.py</span> запускается командой <span class="code-chip">streamlit run app.py</span></li>
        <li>Нейросеть отвечает на вопрос в браузере на <span class="code-chip">localhost:8501</span></li>
        <li>Чат помнит переписку</li>
        <li>Есть сайдбар с выбором характера и «Очистить чат», эмодзи и «Думаю…»</li>
      </ul>
    </div>
    <div class="info-card">
      <h3 style="color:var(--ek-violet-deep)">Для успевающих · публикация</h3>
      <ul class="clean">
        <li>Проект залит на GitHub с <span class="code-chip">requirements.txt</span></li>
        <li>Приложение задеплоено на Streamlit Cloud, ключ в Secrets</li>
        <li>Есть публичная ссылка</li>
      </ul>
    </div>
  </div>
  <div class="ek-note ek-note--green">Обязательный минимум — рабочий локальный чат из левой колонки. Успели опубликовать? Откройте свою ссылку на телефоне и задайте вопрос — сайт живёт в интернете. Не успели — публикация уходит в ДЗ.</div>
</div>"""},

    # 37 · ДЗ
    {"notes": "ДЗ — прокачать приложение, примерно 30 минут. Каждое улучшение — отдельный диалог с DeepSeek, не всё сразу. Кто не успел опубликовать сайт на уроке — доводит публикацию (GitHub + Streamlit Cloud, ключ в Secrets) дома и присылает публичную ссылку. Напомните про ключ на скриншотах: его обязательно скрыть.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Домашнее задание · около 30 минут</div>
    <h2>Прокачайте <span class="acc">приложение</span></h2>
  </div>
  <p>Три улучшения — каждое через отдельный диалог с DeepSeek:</p>
  <div class="grid-3">
    <div class="info-card">
      <h3>Оформление</h3>
      <p>Поменяйте тему, эмодзи и заголовок, добавьте короткое описание приложения под ним.</p>
    </div>
    <div class="info-card">
      <h3>Вопрос по файлу</h3>
      <p>Добавьте <span class="code-chip">st.file_uploader</span>: пользователь грузит текст, а помощник отвечает по нему.</p>
    </div>
    <div class="info-card">
      <h3>Опубликуйте и поделитесь</h3>
      <p>Не успели на уроке — задеплойте на Streamlit Cloud (ключ в Secrets), отправьте публичную ссылку другу и попросите задать вопрос.</p>
    </div>
  </div>
  <div class="ek-note ek-note--red">Пришлите скриншот приложения — <b>ключ скройте!</b> — и публичную ссылку на свой сайт.</div>
</div>"""},

    # 38 · ФИНАЛ
    {"cls": "slide--green",
     "notes": "Закройте урок и весь Модуль 3. Сегодня программа стала веб-приложением с публичной ссылкой, которую можно отправить кому угодно — чат откроется у человека в браузере. Теперь у учеников две публичные ссылки: бот в Telegram и сайт на Streamlit. На уроке 11 заглянем под капот нейросети: перейдём на официальный openai SDK, разберём temperature и max_tokens и соберём генератор статей.",
     "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">L</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">I</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">N</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">K</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="bubble">
      <h1>До встречи<br>на уроке 11!</h1>
      <p>Модуль 3 закрыт: у вас теперь две публичные ссылки — бот в Telegram и сайт на Streamlit. Отправьте их кому угодно: чат откроется у человека в браузере. На уроке 11 заглянем под капот нейросети: openai SDK, temperature и max_tokens, генератор статей.</p>
    </div>
  </div>"""},
]
