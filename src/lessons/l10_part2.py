# -*- coding: utf-8 -*-
SLIDES = [
    # 11 · КАК РАБОТАЕТ STREAMLIT
    {"notes": "Главная идея урока. При каждом действии пользователя Streamlit прогоняет весь app.py сверху вниз. Отсюда и простота, и проблема памяти — переменные обнуляются. Не углубляйтесь: держите эту мысль в голове для следующего слайда.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как это работает</div>
    <h2>Streamlit <span class="acc">перезапускает</span> весь скрипт</h2>
  </div>
  <p>Главное правило урока: при <span class="hl">каждом</span> действии пользователя — ввод текста, клик по кнопке — Streamlit прогоняет весь <span class="code-chip">app.py</span> заново, сверху вниз.</p>
  <div class="grid-2">
    <div class="ek-note ek-note--green"><b>Отсюда простота.</b> Вы просто пишете код сверху вниз, как обычный скрипт. Никаких обработчиков событий и обновлений вручную — Streamlit сам перерисовывает страницу.</div>
    <div class="ek-note ek-note--red"><b>Отсюда проблема.</b> Раз скрипт запускается заново — обычные переменные <b>обнуляются</b>. История переписки сотрётся при каждом новом вопросе. Это чиним на следующем слайде.</div>
  </div>
  <div class="ek-note">Запомните одну фразу: <b>Streamlit перезапускает весь</b> <span class="code-chip">app.py</span> <b>на каждый ввод и клик</b>. Из неё следует всё остальное.</div>
</div>"""},

    # 12 · ПРОБЛЕМА ПАМЯТИ → session_state
    {"notes": "Решение проблемы с прошлого слайда: обычная переменная обнуляется, а st.session_state живёт между перезапусками. Свяжите с уроком 7: список entries, но здесь он живёт в памяти сессии. Готовит правку 2 (чат-история).",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как это работает</div>
    <h2>Память диалога — <span class="acc">st.session_state</span></h2>
  </div>
  <p>Обычная переменная на каждом перезапуске <span class="hl">обнуляется</span>. Чтобы переписка не терялась, историю храним в особом месте — <span class="code-chip">st.session_state</span>.</p>
  <div class="grid-2">
    <div class="info-card"><h3>Обычная переменная</h3>Создаётся заново при каждом запуске скрипта. После вопроса всё, что в ней было, <span class="hl">пропадает</span>.</div>
    <div class="info-card"><h3><span class="code-chip">st.session_state</span></h3>Хранилище, которое <span class="hl">живёт между перезапусками</span>. Здесь живёт история чата — список <span class="code-chip">st.session_state.messages</span>.</div>
  </div>
  <div class="ek-note"><span class="code-chip">st.session_state.messages</span> — это <b>список</b>, как <span class="code-chip">entries</span> в дневнике урока 7. Только он живёт не в файле, а в <b>памяти сессии</b>, пока открыта вкладка.</div>
</div>"""},

    # 13 · AI ОТВЕЧАЕТ В БРАУЗЕРЕ
    {"notes": "Новая роль DeepSeek: тот же движок, что в советчике и боте, но ответ рисуется на веб-странице. Системная роль — «полезный помощник». Функция ask_deepseek(question) шлёт запрос и возвращает текст.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Новая роль нейросети</div>
    <h2>Нейросеть отвечает <span class="acc">в браузере</span></h2>
  </div>
  <p>На уроке 5 DeepSeek был <span class="hl">советчиком</span>, на уроке 9 жил в <span class="hl">Telegram-боте</span>. Сегодня движок тот же, но ответ рисуется прямо на <span class="hl">веб-странице</span>.</p>
  <div class="info-card"><h3>Системная роль</h3>«Ты — полезный помощник. Отвечай понятно и по делу». Вопрос из поля уходит в сеть, ответ возвращается текстом.</div>
  <div class="ek-note">Всю работу с сетью прячем в функцию <span class="code-chip">ask_deepseek(question)</span>: она шлёт запрос к DeepSeek и <b>возвращает готовый текст ответа</b>, который сразу показываем на странице.</div>
</div>"""},

    # 14 · ЦЕЛЬ
    {"notes": "Прочитайте цель вслух. Подчеркните: локальный чат-сайт — обязательный минимум для всех, публикация с публичной ссылкой — для успевающих. Слева теория, справа практика.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Цель · что будет в конце</div>
    <h2><span class="acc">Цель</span> урока</h2>
  </div>
  <div class="ek-note">К 55-й минуте у каждого — сайт-чат с AI-помощником: он открывается в браузере, помнит переписку и отвечает голосом DeepSeek. А у успевающих он уже <b>опубликован на Streamlit Cloud</b> — с публичной ссылкой на любое устройство.</div>
  <div class="grid-2">
    <div class="info-card"><h3>Узнаете</h3>
      <ul class="clean">
        <li>Как Streamlit делает сайт из Python без единой строчки HTML</li>
        <li>Почему Streamlit перезапускает весь скрипт и зачем нужен <span class="code-chip">st.session_state</span></li>
        <li>Почему ключ хранят в Secrets, а не в коде</li>
      </ul>
    </div>
    <div class="info-card"><h3>Сделаете</h3>
      <ul class="clean">
        <li>Соберёте чат-интерфейс на виджетах <span class="code-chip">st.*</span></li>
        <li>Подключите DeepSeek через <span class="code-chip">requests</span> — ответы в браузере</li>
        <li>Успеете — опубликуете сайт и получите свою ссылку</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 15 · ДЕМО
    {"notes": "Покажите готовое приложение — соберите заранее. Задайте вопрос при группе, чтобы все увидели пузыри переписки и сайдбар. Обязательно покажите публичную ссылку вида ...streamlit.app в адресной строке.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Демо результата</div>
    <h2>Что соберём <span class="acc">сегодня</span></h2>
  </div>
  <div class="term">
    <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">БРАУЗЕР</span></div>
    <div class="term-body">🤖 Мой AI-помощник
<span class="dim">[ сайдбар ]  Характер: дружелюбный  ·  [ Очистить чат ]</span>

user      <span class="usr">Объясни, что такое рекурсия</span>
assistant Рекурсия — это когда функция вызывает саму себя...

Спроси что-нибудь ▸ <span class="dim">______________________________</span>

<span class="usr">https://moy-ai-pomoshnik.streamlit.app</span></div>
  </div>
  <p>Это <span class="hl">веб-приложение</span> в браузере: поле, пузыри переписки, сайдбар с выбором характера. Внизу — <b>публичная ссылка</b>, её можно открыть с телефона и отправить кому угодно.</p>
</div>"""},

    # 16 · ПАПКА И БИБЛИОТЕКИ
    {"notes": "Подготовка: папка lesson-10, файл app.py. ВАЖНО: Streamlit может устанавливаться дольше обычных библиотек — проверьте pip install streamlit requests python-dotenv заранее, до урока, на компьютерах учеников. Ставим requests, а не openai: в этом уроке к DeepSeek обращаемся напрямую через requests.post; официальный openai SDK — тема следующего урока 11. requirements.txt добавим на этапе публикации.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Подготовка</div>
    <h2>Папка lesson-10 и <span class="acc">библиотеки</span></h2>
  </div>
  <div class="grid-2">
    <div class="col">
      <ol class="steps steps--tight">
        <li><div>Создайте папку <span class="code-chip">lesson-10</span> в <span class="code-chip">vibe-coding</span></div></li>
        <li><div>Внутри создайте файл <span class="code-chip">app.py</span></div></li>
        <li><div>Поставьте библиотеки одной командой:</div></li>
      </ol>
      <div class="term" style="margin-top:12px">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
        <div class="term-body"><span class="usr">pip install streamlit requests python-dotenv</span></div>
      </div>
    </div>
    <div class="col">
      <div class="term">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ПАПКА</span></div>
        <div class="term-body">D:/vibe-coding/lesson-10/
└── app.py
    <span class="dim">(requirements.txt
     добавим при публикации)</span></div>
      </div>
      <div class="ek-note ek-note--red" style="margin-top:14px"><span class="code-chip">streamlit</span> может устанавливаться <b>заметно дольше</b> обычных библиотек. Проверьте установку заранее, до урока — иначе старт затянется.</div>
    </div>
  </div>
</div>"""},

    # 17 · ПРОМПТ #2 · КАРКАС (эхо)
    {"notes": "Скопировать промпт целиком в новый чат DeepSeek. Это рабочая заготовка: заголовок, поле ввода и вывод самого вопроса (эхо). Нейросеть подключим первой правкой, поэтому пока никакого DeepSeek и ключа тут нет. Роль наставника нужна, чтобы код был с понятными комментариями.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #2 · стартовый каркас</div>
    <h2>Каркас AI-помощника (пока <span class="acc">эхо</span>)</h2>
  </div>
  <div class="prompt-card" style="margin-top:10px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — <span class="hl">опытный Python-разработчик</span> и наставник школьника.
Собери базовый интерфейс app.py на Streamlit.

Каркас:
- заголовок страницы через st.title
- поле ввода вопроса через st.text_input
- вывод самого вопроса под полем (эхо) через st.write

Никакой нейросети пока не подключай — просто повтори введённый вопрос. Нейросеть добавим следующим шагом.
Запусти командой streamlit run app.py и открой в браузере.
Прокомментируй код для новичка. Верни весь файл одним блоком.</div>
  </div>
</div>"""},

    # 18 · ЗАПУСК КАРКАСА
    {"notes": "Запуск каркаса. Streamlit сам откроет браузер на localhost:8501. Напомните: страница обновляется сама при каждом вводе, потому что Streamlit перезапускает скрипт. Дождитесь, пока у всех откроется страница с полем.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск каркаса</div>
    <h2>Запускаем и смотрим <span class="acc">в браузере</span></h2>
  </div>
  <ol class="steps steps--tight">
    <li><div>Скопируйте код из ответа DeepSeek в <span class="code-chip">app.py</span></div></li>
    <li><div>Сохраните файл (<span class="code-chip">Ctrl+S</span>)</div></li>
    <li><div>В терминале выполните <span class="code-chip">streamlit run app.py</span></div></li>
    <li><div>Streamlit сам откроет браузер на <span class="code-chip">http://localhost:8501</span></div></li>
    <li><div>Проверьте: видны заголовок и поле вопроса, а эхо-ответ появляется под ним</div></li>
  </ol>
  <div class="ek-note">Введёте вопрос — страница <b>обновится сама</b>. Это и есть перезапуск скрипта: Streamlit прогнал весь <span class="code-chip">app.py</span> заново и перерисовал страницу.</div>
</div>"""},

    # 19 · КАРКАС ГОТОВ
    {"notes": "Момент: интерфейс уже работает в браузере, но отвечает эхом. Дальше добавляем по одной правке — нейросеть, чат-история, сайдбар, публикация. Структура правильная, добавлять функции в такую программу легко.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Момент урока</div>
    <h2>Каркас готов — интерфейс уже <span class="acc">работает</span></h2>
  </div>
  <p>У вас в браузере <span class="hl">рабочая страница</span>: заголовок, поле, ответ под ним. Пока она «отвечает» эхом — просто повторяет ваш вопрос. Это нормально: интерфейс есть, логику добавим правками.</p>
  <div class="ek-note ek-note--green">Вы собрали веб-страницу <b>без единой строчки HTML</b> — всё нарисовали виджеты <span class="code-chip">st.*</span>. И запускается она одной командой <span class="code-chip">streamlit run app.py</span>.</div>
  <div class="ek-note">Дальше наполняем по одной правке: подключим <b>нейросеть</b>, сделаем <b>чат-историю</b>, добавим <b>сайдбар</b> и <b>опубликуем</b> сайт.</div>
</div>"""},
]
