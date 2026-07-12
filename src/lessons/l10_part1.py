# -*- coding: utf-8 -*-
SLIDES = [
    # 1 · ТИТУЛ
    {"cls": "slide--violet",
     "notes": "Поприветствуйте. Сегодня делаем следующий шаг после терминала: соберём веб-приложение. Streamlit превращает Python-скрипт в страницу с полем и кнопкой — без единой строчки HTML. Затем опубликуем проект на Streamlit Cloud и получим ссылку, которую можно открыть с любого устройства. К концу урока у каждого — рабочий AI-помощник в браузере.",
     "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">S</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">W</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">A</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">C</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="cover-card">
      <div class="badge">Урок №10</div>
      <div class="card-top"><span class="win-dots"><i></i><i></i><i></i></span><span class="win-close"></span></div>
      <h1>AI-помощник<br>в&nbsp;браузере</h1>
      <p class="cover-sub">Соберём сайт на Streamlit: вы пишете вопрос в браузере — DeepSeek отвечает, а переписка сохраняется в чате. Затем опубликуем приложение и получим собственную ссылку для любого устройства.</p>
      <div class="cover-chips"><span class="chip">Streamlit</span><span class="chip chip--green">DeepSeek</span><span class="chip chip--gray">GitHub</span><span class="chip chip--gray">Streamlit Cloud</span></div>
    </div>
  </div>"""},

    # 2 · AGENDA
    {"notes": "План. Теории — минимум: уже на 12-й минуте каждый видит свою веб-страницу в браузере, к 30-й — каркас AI-помощника с полем и ответом. Дальше — правки через диалог. Обязательный результат к 48–55-й минуте — локальный чат с AI (правки 1–4). Публикация (правка 5) опциональна: она требует аккаунтов GitHub и Streamlit Cloud, поэтому её делают только успевающие; если не хватает времени или доступов — продемонстрируйте деплой со своего экрана или отдайте в ДЗ, а на уроке доведите локальный чат.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Agenda · план занятия</div>
    <h2>Как пройдут <span class="acc">60 минут</span></h2>
  </div>
  <div class="agenda">
    <div class="agenda-row"><span class="t">0–5</span><div><div class="tt">Разбор ДЗ</div><div class="dd">Смотрим Telegram-ботов: команда /joke, свой характер, кнопки.</div></div></div>
    <div class="agenda-row"><span class="t">5–12</span><div><div class="tt">Streamlit без HTML</div><div class="dd">Минимум теории — только чтобы собрать сайт.</div></div></div>
    <div class="agenda-row"><span class="t">12–20</span><div><div class="tt">Промпт-разминка</div><div class="dd">Первое приложение открывается в браузере.</div></div></div>
    <div class="agenda-row"><span class="t">20–30</span><div><div class="tt">Каркас AI-помощника</div><div class="dd">Интерфейс с полем и ответом.</div></div></div>
    <div class="agenda-row"><span class="t">30–48</span><div><div class="tt">Правки через диалог</div><div class="dd">Нейросеть → чат-история → сайдбар → оформление.</div></div></div>
    <div class="agenda-row"><span class="t">48–55</span><div><div class="tt">Мини-вопросы и отладка</div><div class="dd">session_state, ошибки Streamlit. Публикация — для успевающих.</div></div></div>
    <div class="agenda-row"><span class="t">55–60</span><div><div class="tt">Демо в группе</div><div class="dd">Открываем свои чаты, у кого готово — по ссылке.</div></div></div>
  </div>
</div>"""},

    # 3 · РАЗБОР ДЗ УРОКА 9
    {"notes": "Откройте 1–2 присланных бота (на весь блок 5 минут). Разбирайте диалог с нейросетью, а не только результат. Подведите к главному: бот работает внутри мессенджера, поэтому интерфейс задан Telegram. Сегодня соберём собственный сайт, где внешний вид и элементы управления настраиваем сами.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор ДЗ урока 9</div>
    <h2>Смотрим <span class="acc">Telegram-ботов</span></h2>
  </div>
  <p>Открываем 1–2 присланных бота и разбираем именно <span class="hl">диалог с нейросетью</span>: команда <span class="code-chip">/joke</span>, свой характер бота через системную роль, кнопки (inline-клавиатура).</p>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card">
      <h3>Что сработало</h3>
      <p>Точечные промпты: <span class="code-chip">/joke</span> отдельным хендлером, характер бота через системную роль, кнопки одним запросом.</p>
    </div>
    <div class="info-card">
      <h3>Что переделывали</h3>
      <p>Если в промпте не просили сохранить остальной код, нейросеть могла случайно изменить рабочий хендлер сообщений.</p>
    </div>
    <div class="info-card">
      <h3>Вывод</h3>
      <p>Бот работает внутри мессенджера, и интерфейс задаёт <b>Telegram</b>. Сегодня соберём собственный сайт — с интерфейсом, который настраиваем сами.</p>
    </div>
  </div>
</div>"""},

    # 4 · ИДЕЯ УРОКА
    {"notes": "Главная мысль: терминал видите только вы, а бот с урока 9 работает внутри готового интерфейса Telegram. Сегодня — свой сайт: Streamlit делает из Python-скрипта веб-страницу без HTML, а затем публикуем проект и получаем ссылку для любого устройства. Две линии: виджеты st.* как интерфейс и публикация на Streamlit Cloud.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Идея урока</div>
    <h2>Настоящий сайт из <span class="acc">Python-скрипта</span></h2>
  </div>
  <p>Терминал видите только вы, а Telegram-бот работает в <span class="hl">готовом интерфейсе мессенджера</span>, и его внешний вид определяет сам Telegram.</p>
  <div class="ek-note" style="margin-top:6px">Сегодня соберём <b>веб-приложение</b>: Streamlit превращает Python-скрипт в веб-страницу с полями и кнопками — <b>без единой строчки HTML</b>. А потом <b>опубликуем</b> его и получим ссылку, которую можно открыть с любого устройства и отправить кому угодно.</div>
  <p>Идея урока 10: пишем <b>Python</b> — виджеты <span class="code-chip">st.*</span> сами рисуют страницу; потом <b>публикуем</b> и получаем <span class="hl">свою ссылку</span>.</p>
</div>"""},

    # 5 · ЧТО ТАКОЕ ВЕБ-ПРИЛОЖЕНИЕ
    {"notes": "Быстрый recap трёх форматов, где мог жить наш код: терминал (только у вас), Telegram-бот (внутри мессенджера), веб-приложение (открывается в браузере по ссылке на любом устройстве). Не углубляйтесь — это короткая теория, главное впереди.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Короткая теория · 1/3</div>
    <h2>Что такое <span class="acc">веб-приложение</span></h2>
  </div>
  <p>Веб-приложение <span class="hl">открывается в браузере по ссылке</span> — с телефона, планшета, любого компьютера. Не нужно ничего устанавливать: просто перейти по адресу.</p>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card">
      <h3>Терминал</h3>
      <p>Программа запускается на вашем компьютере. Результат видите <b>только вы</b>.</p>
    </div>
    <div class="info-card">
      <h3>Telegram-бот</h3>
      <p>Живёт внутри мессенджера. Интерфейс задаёт <b>Telegram</b> — поле и кнопки не ваши.</p>
    </div>
    <div class="ek-note ek-note--green" style="font-size:16px"><b>Веб-приложение</b><br>Открывается в <b>браузере по ссылке</b> на любом устройстве. Интерфейс собираете вы. Это соберём сегодня.</div>
  </div>
</div>"""},

    # 6 · STREAMLIT БЕЗ HTML
    {"notes": "Ключевая мысль слайда: обычный сайт — это три языка (HTML, CSS, JavaScript) и много работы. Со Streamlit вы пишете только Python: виджеты st.* сами рисуют страницу. Python-скрипт становится интерфейсом. Не перегружайте группу веб-разработкой — покажите контраст и идите дальше.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Короткая теория · 2/3</div>
    <h2>Streamlit — сайт <span class="acc">без HTML</span></h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>Обычный сайт</h4>
      <p>Три языка: HTML — разметка, CSS — оформление, JavaScript — логика. Долго и много кода даже ради одного поля с кнопкой.</p>
      <p class="note">Так обычно собирают сложные сайты.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>Streamlit</h4>
      <p>Пишете только <b>Python</b>. Виджеты <span class="code-chip">st.*</span> сами превращают код в страницу с полями и кнопками.</p>
      <p class="note">Это соберём сегодня.</p>
    </div>
  </div>
  <p>Со Streamlit ваш <span class="hl">Python-скрипт становится интерфейсом</span> — HTML и CSS писать не нужно.</p>
</div>"""},

    # 7 · ВИДЖЕТЫ STREAMLIT
    {"notes": "Виджеты — это готовые элементы страницы, каждый — одна строка Python. Покажите пять главных на маленьком примере: st.title, st.text_input, st.write, st.button, а st.chat_input и st.chat_message — для чата, к ним придём к концу урока. Мысль: строчка кода = элемент на странице.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Короткая теория · 3/3</div>
    <h2>Виджеты — по строчке на <span class="acc">элемент</span></h2>
  </div>
  <p>Виджет — готовый элемент страницы. Каждый — <span class="hl">одна строка Python</span>: написали строчку — на сайте появился элемент.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">import</span> streamlit <span class="kw">as</span> st

st.title(<span class="st">"Мой сайт"</span>)                 <span class="cm"># заголовок</span>
name = st.text_input(<span class="st">"Имя"</span>)          <span class="cm"># поле ввода</span>
st.write(<span class="st">"Привет, "</span> + name)          <span class="cm"># вывод текста</span>
st.button(<span class="st">"Нажми меня"</span>)              <span class="cm"># кнопка</span></div>
  </div>
  <div class="ek-note">Ещё два для чата: <span class="code-chip">st.chat_input</span> — поле сообщения, <span class="code-chip">st.chat_message</span> — пузырь переписки. К ним придём, когда сделаем AI-помощника.</div>
</div>"""},

    # 8 · ПРОМПТ #1 · РАЗМИНКА
    {"notes": "Никакой долгой подготовки: сразу просим у DeepSeek минимальное Streamlit-приложение и запускаем. Промпт с ролью и форматом — техники прошлых уроков работают и здесь. Ученики копируют промпт целиком в новый чат.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #1 · разминка</div>
    <h2>Первое приложение за <span class="acc">две минуты</span></h2>
  </div>
  <p>Не будем долго готовиться — попросим у DeepSeek минимальное Streamlit-приложение и сразу откроем его в браузере.</p>
  <div class="prompt-card" style="margin-top:14px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — опытный Python-разработчик и наставник школьника. Напиши минимальное Streamlit-приложение app.py: заголовок «Мой первый сайт», поле ввода st.text_input для имени и вывод «Привет, {имя}!» через st.write. Только streamlit. Напомни в комментарии, что запускать нужно командой streamlit run app.py. Ответь одним блоком.</div>
  </div>
</div>"""},

    # 9 · ЗАПУСК И РАЗБОР
    {"notes": "Фундамент урока: дождитесь, пока у каждого в браузере откроется страница на localhost:8501. Streamlit может устанавливаться дольше обычных библиотек — проверьте pip install streamlit requests python-dotenv заранее, до урока, на компьютерах учеников. Не идите дальше, пока страница не открылась у всех.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск и разбор</div>
    <h2>Первый сайт в <span class="acc">браузере</span></h2>
  </div>
  <div class="grid-2">
    <div class="col">
      <ol class="steps steps--tight">
        <li><div>В <span class="code-chip">vibe-coding</span> создайте папку <span class="code-chip">lesson-10</span></div></li>
        <li><div>Один раз: <span class="code-chip">pip install streamlit requests python-dotenv</span></div></li>
        <li><div>Создайте <span class="code-chip">app.py</span> и вставьте код из ответа</div></li>
        <li><div>Выполните <span class="code-chip">streamlit run app.py</span></div></li>
      </ol>
      <div class="ek-note ek-note--green" style="margin-top:14px;font-size:15px">Streamlit <b>сам откроет браузер</b> на <span class="code-chip">http://localhost:8501</span>. Ввели имя — на странице появился привет? Первый сайт готов.</div>
    </div>
    <div class="kv">
      <div class="kv-row"><div class="k">st.title</div><div class="v">Нарисовал заголовок страницы.</div></div>
      <div class="kv-row"><div class="k">st.text_input</div><div class="v">Поле ввода прямо в браузере.</div></div>
      <div class="kv-row"><div class="k">st.write</div><div class="v">Вывел текст на страницу.</div></div>
    </div>
  </div>
</div>"""},

    # 10 · ЕСЛИ НЕ ЗАПУСТИЛОСЬ (первый запуск streamlit run)
    {"notes": "Шпаргалка по первому запуску streamlit run. Почините у всех — тот же localhost:8501 и папка lesson-10 нужны дальше для самого AI-помощника. Если streamlit не находится — почти всегда дело в установке или не той среде. Ключа на этом этапе ещё нет, поэтому про 401 здесь не говорим — эта ошибка появится позже, когда подключим DeepSeek.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Первый запуск · streamlit run</div>
    <h2>Если сайт <span class="acc">не открылся</span></h2>
  </div>
  <div class="grid-3" style="margin-top:8px">
    <div class="ek-note ek-note--red" style="font-size:15px"><b>ModuleNotFoundError</b><br><span class="code-chip">streamlit: command not found</span> или <span class="code-chip">ModuleNotFoundError</span> — библиотека не установлена или не та среда. Выполните <span class="code-chip" style="white-space:normal">pip install streamlit requests python-dotenv</span> ещё раз.</div>
    <div class="ek-note ek-note--red" style="font-size:15px"><b>Порт 8501 занят</b><br>Уже открыт старый Streamlit. Закройте прежний процесс или запустите с другим портом: <span class="code-chip">--server.port 8502</span>.</div>
    <div class="ek-note ek-note--red" style="font-size:15px"><b>Страница не обновилась</b><br>Белая страница или изменения не видны. Откройте <span class="code-chip">http://localhost:8501</span> вручную и обновите вкладку.</div>
  </div>
</div>"""},
]
