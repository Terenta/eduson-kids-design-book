# -*- coding: utf-8 -*-
SLIDES = [
    # 20 · ЕСЛИ AI-ПРИЛОЖЕНИЕ НЕ РАБОТАЕТ (специфика AI-приложения)
    {"notes": "Поздний troubleshooting — уже не про первый запуск (это было на раннем слайде), а про специфику AI-приложения: ключ, библиотека requests, память. Чаще всего — забытый pip install и незаметное «ключ не подставлен». Про 401 говорим именно здесь, потому что ключ появляется только сейчас, с подключением DeepSeek. Напомните: после правки файла Streamlit сам предложит кнопку Rerun. Помогите лично тем, у кого не работает, остальные сверяются со слайдом.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Специфика AI-приложения</div>
    <h2>Типичные ситуации с <span class="acc">нейросетью</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">ModuleNotFoundError</div><div class="v">Не установлены <span class="code-chip">streamlit</span> или <span class="code-chip">requests</span>. В терминале: <span class="code-chip">pip install streamlit requests python-dotenv</span> — и запускайте снова.</div></div>
    <div class="kv-row"><div class="k">401 Unauthorized</div><div class="v">Пустой ответ или ошибка от DeepSeek — ключ не подставлен. Проверьте, что <span class="code-chip">API_KEY</span> на месте: локально в <span class="code-chip">.env</span>, а на Streamlit Cloud — в разделе Secrets.</div></div>
    <div class="kv-row"><div class="k">requirements.txt</div><div class="v">На Streamlit Cloud библиотеки не ставятся сами. Без файла со списком (<span class="code-chip">streamlit</span>, <span class="code-chip">requests</span>) на хостинге снова вылезет <span class="code-chip">ModuleNotFoundError</span>.</div></div>
    <div class="kv-row"><div class="k">Переписка стирается</div><div class="v">История не в <span class="code-chip">st.session_state</span>. Streamlit перезапускает скрипт на каждый ввод — обычная переменная обнуляется.</div></div>
  </div>
</div>"""},

    # 21 · ПРАВКА 1 · ОТВЕЧАЕТ НЕЙРОСЕТЬ
    {"notes": "Первая правка идёт в тот же чат: каркас-эхо превращается в рабочего AI-помощника. Вопрос уходит в DeepSeek API, ответ показывается на странице. Проверьте, что ключ подставлен и есть интернет. Это первый видимый результат — спросили, на сайте появился ответ нейросети.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 1 · отвечает нейросеть</div>
    <h2>Вопрос уходит в сеть, <span class="acc">ответ — на странице</span></h2>
  </div>
  <p>Первый шаг: поле больше не эхо. Вопрос уходит в DeepSeek API, а ответ появляется прямо на веб-странице.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Подключи DeepSeek через библиотеку requests (requests.post на https://api.deepseek.com/chat/completions, модель deepseek-chat): вопрос из поля отправляется нейросети, ответ показывается на странице вместо эха. Ключ читай из переменной API_KEY. Не используй библиотеку openai. Верни весь файл.</div>
  </div>
</div>"""},

    # 22 · РАЗБОР · ЗАПРОС К DeepSeek ЧЕРЕЗ requests
    {"notes": "Покажите, что запрос идёт в API: тот же url и модель, что в советчике и боте, но через requests.post — библиотеку openai не ставим, это тема урока 11. Ключ берём из единой переменной API_KEY. Ответ достаём из choices[0].message.content. Дайте ученикам спросить «Объясни, что такое рекурсия» и увидеть ответ на своём сайте.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Запрос к DeepSeek через <span class="acc">requests</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">import</span> requests

<span class="kw">def</span> ask_deepseek(question):
    headers = {<span class="st">"Authorization"</span>: f<span class="st">"Bearer {API_KEY}"</span>}
    data = {
        <span class="st">"model"</span>: <span class="st">"deepseek-chat"</span>,
        <span class="st">"messages"</span>: [
            {<span class="st">"role"</span>: <span class="st">"system"</span>, <span class="st">"content"</span>: <span class="st">"Ты полезный помощник"</span>},
            {<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: question},
        ],
    }
    url = <span class="st">"https://api.deepseek.com/chat/completions"</span>
    resp = requests.post(url, headers=headers, json=data)
    <span class="kw">return</span> resp.json()[<span class="st">"choices"</span>][0][<span class="st">"message"</span>][<span class="st">"content"</span>]</div>
  </div>
  <div class="ek-note ek-note--green">Тот же движок, что в советчике и боте, но обращаемся напрямую через <span class="code-chip">requests.post</span>: url <span class="code-chip">https://api.deepseek.com/chat/completions</span>, модель <span class="code-chip">deepseek-chat</span>. Ответ берём из <span class="code-chip">choices[0].message.content</span>. Библиотеку <span class="code-chip">openai</span> не ставим — это тема урока 11.</div>
</div>"""},

    # 23 · ПРАВКА 2 · ЧАТ-ИСТОРИЯ
    {"notes": "Правка 2 превращает поле в чат: st.chat_input, st.chat_message, история в st.session_state.messages. После неё переписка держится пузырями и не стирается. Дождитесь, пока у всех чат помнит несколько сообщений.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 2 · чат-история</div>
    <h2>Настоящий чат, который <span class="acc">помнит</span></h2>
  </div>
  <p>Теперь поле превращается в чат: сообщения показываются пузырями, а вся переписка держится в памяти и не стирается.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Сделай интерфейс чатом: используй st.chat_input и st.chat_message, храни переписку в st.session_state.messages, показывай всю историю. Верни весь файл.</div>
  </div>
</div>"""},

    # 24 · РАЗБОР · st.session_state.messages
    {"notes": "Вставьте канонический код целиком. Свяжите с уроком 7: список messages — как entries, только живёт в памяти сессии. Поля role/content; st.rerun перерисовывает страницу с новым сообщением. ask_deepseek(question) — та же функция на requests из предыдущего разбора. Не углубляйтесь в каждый символ.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>История чата живёт в <span class="acc">session_state</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">if</span> <span class="st">"messages"</span> <span class="kw">not in</span> st.session_state:      <span class="cm"># память между перезапусками</span>
    st.session_state.messages = []

<span class="kw">for</span> m <span class="kw">in</span> st.session_state.messages:          <span class="cm"># показать историю</span>
    st.chat_message(m[<span class="st">"role"</span>]).write(m[<span class="st">"content"</span>])

question = st.chat_input(<span class="st">"Спроси что-нибудь"</span>)
<span class="kw">if</span> question:
    st.session_state.messages.append({<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: question})
    answer = ask_deepseek(question)          <span class="cm"># запрос к DeepSeek через requests</span>
    st.session_state.messages.append({<span class="st">"role"</span>: <span class="st">"assistant"</span>, <span class="st">"content"</span>: answer})
    st.rerun()</div>
  </div>
  <p>Каждое сообщение — словарь с полями <span class="code-chip">role</span> и <span class="code-chip">content</span>. Список <span class="code-chip">messages</span> — как <span class="code-chip">entries</span> из дневника, только живёт в памяти сессии. <span class="code-chip">st.rerun</span> перерисовывает страницу с новой репликой.</p>
</div>"""},

    # 25 · ПОЛЕЗНОЕ ЗНАНИЕ · ПЕРЕЗАПУСК И session_state
    {"notes": "Зафиксируйте, почему без session_state переписка стирается: Streamlit перезапускает весь app.py на каждый ввод, обычные переменные обнуляются. Это готовит квиз 2.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Полезное знание</div>
    <h2>Почему переписка <span class="acc">стирается</span></h2>
  </div>
  <div class="vs">
    <div class="vs-col vs-col--plain">
      <h4>Обычная переменная</h4>
      <p>При каждом вводе Streamlit перезапускает весь <span class="code-chip">app.py</span> сверху вниз.</p>
      <p class="note">Переменная обнуляется — история чата пропадает.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>st.session_state</h4>
      <p>Хранит данные <b>между перезапусками</b> скрипта.</p>
      <p class="note">Здесь и живёт <span class="code-chip">st.session_state.messages</span> — вся переписка.</p>
    </div>
  </div>
  <p>Streamlit перезапускает скрипт на каждый ввод и клик. Всё, что нужно запомнить, кладём в <span class="code-chip">st.session_state</span>.</p>
</div>"""},

    # 26 · ПРАВКА 3 · НАСТРОЙКИ В САЙДБАРЕ
    {"notes": "Правка 3 добавляет боковую панель: выбор характера помощника через selectbox и кнопку «Очистить чат». После неё программа настраивается без правки кода. Дайте детям переключить характер и увидеть разницу в ответах.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 3 · настройки в сайдбаре</div>
    <h2>Характер помощника и <span class="acc">«Очистить чат»</span></h2>
  </div>
  <p>Добавляем боковую панель: выбор характера помощника и кнопка «Очистить чат» — приложение настраивается без правки кода.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Добавь боковую панель st.sidebar: выбор характера помощника (selectbox) и кнопку «Очистить чат». Выбранный характер передавай в системную роль DeepSeek. Верни весь файл.</div>
  </div>
</div>"""},

    # 27 · РАЗБОР · САЙДБАР И ХАРАКТЕР
    {"notes": "Главная мысль: выбранный характер уходит в системную роль DeepSeek — программа стала настраиваемой без правки кода. Кнопка «Очистить чат» просто обнуляет messages. Дайте сфотографировать.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Настройки, <span class="acc">не трогая код</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">with</span> st.sidebar:
    character = st.selectbox(<span class="st">"Характер"</span>, [<span class="st">"Дружелюбный"</span>, <span class="st">"Строгий"</span>, <span class="st">"Весёлый"</span>])
    <span class="kw">if</span> st.button(<span class="st">"Очистить чат"</span>):
        st.session_state.messages = []       <span class="cm"># обнулили историю</span>
        st.rerun()</div>
  </div>
  <div class="ek-note"><span class="code-chip">st.sidebar</span> рисует боковую панель. Выбранный характер уходит в <b>системную роль DeepSeek</b> — и тон ответов меняется без правки кода. Кнопка «Очистить чат» обнуляет <span class="code-chip">st.session_state.messages</span> — история очищается, и новый диалог начинается без прошлых сообщений.</div>
</div>"""},

    # 28 · ПРАВКА 4 · ОФОРМЛЕНИЕ И st.spinner
    {"notes": "Правка 4 — финальная отделка локального чата: эмодзи и заголовок, короткое описание под ним, и st.spinner «Думаю…», чтобы пока DeepSeek отвечает, пользователь видел индикатор, а не замерший экран. После неё локальный AI-чат готов полностью — это обязательный результат к 48–55-й минуте. Публикацию (правку 5) делают только успевающие, остальным — в ДЗ.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 4 · оформление</div>
    <h2>Эмодзи, описание и <span class="acc">«Думаю…»</span></h2>
  </div>
  <p>Финальная отделка: приятный заголовок с эмодзи, короткое описание под ним и индикатор ожидания, пока нейросеть думает.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Наведи красоту: добавь эмодзи и заголовок приложения, короткое описание под ним. Пока DeepSeek отвечает, показывай индикатор ожидания через st.spinner с текстом «Думаю…». Верни весь файл.</div>
  </div>
</div>"""},

    # 29 · РАЗБОР · st.spinner И ОФОРМЛЕНИЕ
    {"notes": "Главная мысль: st.spinner как контекст with оборачивает медленный запрос — пользователь видит «Думаю…», а не замерший экран. Плюс st.title с эмодзи и st.caption с описанием. На этом локальный AI-чат полностью готов. Дальше — опциональная публикация для успевающих.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Индикатор ожидания и <span class="acc">заголовок</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">st.title(<span class="st">"🤖 Мой AI-помощник"</span>)
st.caption(<span class="st">"Спрашивай что угодно — отвечает DeepSeek"</span>)

<span class="kw">if</span> question:
    st.session_state.messages.append({<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: question})
    <span class="kw">with</span> st.spinner(<span class="st">"Думаю…"</span>):                <span class="cm"># индикатор, пока идёт запрос</span>
        answer = ask_deepseek(question)
    st.session_state.messages.append({<span class="st">"role"</span>: <span class="st">"assistant"</span>, <span class="st">"content"</span>: answer})
    st.rerun()</div>
  </div>
  <div class="ek-note ek-note--green"><span class="code-chip">st.spinner("Думаю…")</span> оборачивает медленный запрос: пока DeepSeek отвечает, на странице крутится индикатор, а не замирает пустой экран. <span class="code-chip">st.title</span> с эмодзи и <span class="code-chip">st.caption</span> с описанием делают интерфейс понятнее. Локальный чат готов — это обязательный результат урока.</div>
</div>"""},
]
