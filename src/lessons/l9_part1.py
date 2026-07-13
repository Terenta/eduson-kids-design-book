# -*- coding: utf-8 -*-
SLIDES = [
    # 1 · ТИТУЛ
    {"cls": "slide--violet", "notes": "Поприветствуйте. Сегодня добавим к Python-программе интерфейс в Telegram: соберём бота, который принимает сообщения от пользователей и отвечает через нейросеть. Бота зарегистрируем у @BotFather, токен положим в .env. К концу урока у каждого будет рабочий бот в Telegram, которым можно поделиться с друзьями. Нужен телефон с Telegram у каждого или веб-версия web.telegram.org.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">B</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">A</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">I</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">T</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="cover-card">
      <div class="badge">Урок №9 · Модуль 3</div>
      <div class="card-top"><span class="win-dots"><i></i><i></i><i></i></span><span class="win-close"></span></div>
      <h1>Telegram-бот<br>с&nbsp;нейросетью</h1>
      <p class="cover-sub">Соберём бота, который принимает сообщения в Telegram и отвечает через DeepSeek. Зарегистрируем его у @BotFather, токен положим в .env — и бот будет доступен другим пользователям.</p>
      <div class="cover-chips"><span class="chip">Python</span><span class="chip chip--green">DeepSeek API</span><span class="chip chip--gray">@BotFather</span><span class="chip chip--gray">Telegram Bot API</span></div>
    </div>
  </div>"""},

    # 2 · ПЛАН
    {"notes": "План. Теории даём минимум: уже на 8-й минуте просим у DeepSeek бота-эхо, а первый ответ бота в Telegram ожидаем к 18–20 минуте (регистрация у @BotFather и установка библиотеки занимают время). Дальше — 5 правок через диалог с нейросетью, каждая меняет поведение бота в чате. КРИТИЧНО заранее: поставьте python-telegram-bot (версия 20+) и зарегистрируйте бота у @BotFather ДО урока, чтобы к 12-й минуте у детей уже был токен на руках — иначе первый ответ сдвинется за 25-ю минуту.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Agenda · план занятия</div>
    <h2>Как пройдут <span class="acc">60 минут</span></h2>
  </div>
  <div class="agenda">
    <div class="agenda-row"><span class="t">0–5</span><div><div class="tt">Разбор ДЗ</div><div class="dd">Смотрим доработанное приложение с погодой: прогноз на завтра, эмодзи, сравнение городов.</div></div></div>
    <div class="agenda-row"><span class="t">5–8</span><div><div class="tt">Как устроен бот</div><div class="dd">Коротко разбираем только то, что нужно для сборки: три звена и long polling.</div></div></div>
    <div class="agenda-row"><span class="t">8–12</span><div><div class="tt">Промпт-разминка</div><div class="dd">bot.py: бот-эхо, который отвечает тем же текстом.</div></div></div>
    <div class="agenda-row"><span class="t">12–20</span><div><div class="tt">Регистрация и запуск</div><div class="dd">@BotFather, токен в код, установка библиотеки — к 18–20 минуте бот отвечает в телефоне.</div></div></div>
    <div class="agenda-row"><span class="t">20–48</span><div><div class="tt">5 правок через диалог</div><div class="dd">Токен в .env → нейросеть → команды → характер → память и «печатает…».</div></div></div>
    <div class="agenda-row"><span class="t">48–55</span><div><div class="tt">Мини-вопросы и отладка</div><div class="dd">Почему run_polling не закрывается, что делать с утёкшим токеном.</div></div></div>
    <div class="agenda-row"><span class="t">55–60</span><div><div class="tt">Демо в группе</div><div class="dd">Каждый пишет своему боту и получает ответ через нейросеть.</div></div></div>
  </div>
</div>"""},

    # 3 · РАЗБОР ДЗ
    {"notes": "Откройте 1–2 доработанных приложения (на весь блок 5 минут). Разбирайте диалог с нейросетью, а не только результат. Подведите к главному: weather.py работал в терминале, поэтому результат видел только автор. Сегодня программа получит интерфейс в Telegram и сможет отвечать другим пользователям.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор ДЗ урока 8</div>
    <h2>Смотрим приложение с <span class="acc">погодой</span></h2>
  </div>
  <p>Открываем 2–3 присланных <span class="code-chip">weather.py</span> и разбираем именно <span class="hl">диалог с нейросетью</span>: прогноз на завтра, эмодзи погоды, сравнение двух городов.</p>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card">
      <h3>Что сработало</h3>
      <p>Точечные промпты: эмодзи по коду погоды, а сравнение городов — через два запроса к <span class="hl">одному</span> API.</p>
    </div>
    <div class="info-card">
      <h3>Что переделывали</h3>
      <p>Где ключ OpenWeather забыли перенести в <span class="code-chip">.env</span> — он остался прямо в коде.</p>
    </div>
    <div class="info-card">
      <h3>Вывод</h3>
      <p>Всё это работало в <span class="hl">терминале</span> — результат видел только автор. Сегодня программа будет отвечать пользователям в <b>Telegram</b>.</p>
    </div>
  </div>
</div>"""},

    # 4 · ИДЕЯ УРОКА
    {"notes": "Главная мысль урока: у Python-программы появляется интерфейс в Telegram. Это первый проект, которым можно поделиться с друзьями. Две линии: бот получает сообщения через run_polling, а на каждое сообщение отвечает DeepSeek — как на уроках 5–8.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Идея урока</div>
    <h2>У программы появляется <span class="acc">интерфейс в Telegram</span></h2>
  </div>
  <p>До сих пор программы работали в <span class="hl">терминале</span> — их видел только автор. Прогноз погоды, дневник и советчик работали локально, но ими было трудно поделиться.</p>
  <div class="ek-note" style="margin-top:6px">Сегодня программа получает <b>интерфейс в Telegram</b>: бот принимает сообщения пользователей и отвечает через нейросеть. Это <b>первый проект, которым можно поделиться</b> с другим человеком.</div>
  <p>Две линии: бот <b>говорит с Telegram</b> через <span class="code-chip">run_polling</span>, а на каждое сообщение <b>отвечает DeepSeek</b> — как на уроках 5–8.</p>
</div>"""},

    # 5 · ЧТО ТАКОЕ БОТ И BOT API
    {"notes": "Короткий recap, минимум теории. Бот — обычная программа, которая общается с людьми в мессенджере. Telegram даёт для этого Bot API — набор правил, по которым программа получает сообщения и отправляет ответы. Ваш bot.py будет работать с Telegram через готовую библиотеку.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Вспоминаем</div>
    <h2>Что такое бот и <span class="acc">Bot API</span></h2>
  </div>
  <p><b>Бот</b> — это обычная программа, которая <span class="hl">общается с людьми в мессенджере</span>: получает их сообщения и отправляет ответы. За ботом всегда стоит код — сегодня это будет ваш <span class="code-chip">bot.py</span>.</p>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>Bot API</h3>
      <p>Telegram даёт <span class="hl">Bot API</span> — набор правил, по которым программа получает сообщения и отправляет ответы. Обращаться к нему напрямую сложно.</p>
    </div>
    <div class="ek-note ek-note--green" style="font-size:16px"><b>Библиотека делает это за вас</b><br><span class="code-chip">python-telegram-bot</span> берёт на себя технические детали: вы описываете реакцию на сообщение, а библиотека работает с Telegram.</div>
  </div>
</div>"""},

    # 6 · ЧЕМ ПЛОХ ТЕРМИНАЛ
    {"notes": "Покажите разницу на примере: программу в терминале запускает и видит только автор на своём компьютере. Чтобы показать её другу, пришлось бы дать доступ к своему ноутбуку. Бот в Telegram доступен любому, у кого есть его @username. Это мотивация всего урока.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Зачем нам новое</div>
    <h2>Чем плох <span class="acc">терминал</span></h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>Программа в терминале</h4>
      <p>Запускается на <span class="hl">вашем</span> компьютере, и результат видите только вы. Чтобы показать другу, пришлось бы посадить его за свой ноутбук.</p>
      <p class="note">Так работали все прошлые проекты.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>Бот в Telegram</h4>
      <p>Любой, кому вы дали <b>@username</b> бота, пишет ему из своего телефона и получает ответ. Программа стала общей.</p>
      <p class="note">Это соберём сегодня.</p>
    </div>
  </div>
  <p>Как только код выходит <b>в мессенджер</b>, им можно <span class="hl">поделиться</span> — и это работает у каждого в телефоне.</p>
</div>"""},

    # 7 · ТРИ ЗВЕНА И LONG POLLING
    {"notes": "Одна схема на весь урок: три звена — пользователь, Telegram, ваш bot.py. Ключевая мысль про long polling: бот не ждёт отдельного запуска на каждое сообщение, а сам постоянно спрашивает у Telegram «есть новые сообщения?». Это делает функция run_polling. Больше про устройство пока знать не нужно.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как это работает</div>
    <h2>Три звена и <span class="acc">long polling</span></h2>
  </div>
  <p>Между вами и ботом всегда три звена: <span class="hl">пользователь</span> пишет в <span class="hl">Telegram</span>, а ваш <span class="code-chip">bot.py</span> забирает сообщение и отправляет ответ обратно.</p>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card"><h3>1 · Пользователь</h3><p>Пишет боту в Telegram со своего телефона.</p></div>
    <div class="info-card"><h3>2 · Telegram</h3><p>Хранит сообщение и ждёт, пока программа его заберёт.</p></div>
    <div class="info-card"><h3>3 · Ваш bot.py</h3><p>Забирает сообщение, готовит ответ и шлёт назад.</p></div>
  </div>
  <div class="ek-note"><b>Long polling</b>: бот сам постоянно спрашивает у Telegram «есть новые сообщения?». Это делает одна строчка — <span class="code-chip">run_polling()</span>. Пока она работает — бот в сети.</div>
</div>"""},

    # 8 · ПРОМПТ #1 БОТ-ЭХО
    {"notes": "Без долгой подготовки: сразу просим у DeepSeek минимального бота-эхо и готовимся запустить. Промпт с ролью и точным заданием — техники прошлых уроков работают и здесь. Ученики копируют промпт целиком в новый чат DeepSeek. Токен пока подставим прямо в константу TOKEN, перенесём в .env следующей правкой.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #1 · разминка</div>
    <h2>Бот-эхо за <span class="acc">две минуты</span></h2>
  </div>
  <p>Начнём с минимального бота: попросим DeepSeek написать эхо-бота, который отвечает <span class="hl">тем же текстом</span>, что ему написали. Токен пока подставим прямо в код.</p>
  <div class="prompt-card" style="margin-top:14px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — опытный Python-разработчик и наставник школьника. Напиши минимального Telegram-бота-эхо bot.py на библиотеке python-telegram-bot (версия 20+, async): бот принимает любое текстовое сообщение и отвечает тем же текстом. Токен возьми из константы TOKEN. Используй Application, MessageHandler, filters.TEXT и run_polling. Прокомментируй код для новичка, ответь одним блоком.</div>
  </div>
</div>"""},

    # 9 · БОТ-ЭХО ОТВЕЧАЕТ (КОД + РАЗБОР)
    {"notes": "Базовый шаг урока: дождитесь, пока бот-эхо ответит в Telegram у каждого. На рабочем коде показываем три вещи: обработчик на async def с await, фильтр текст-но-не-команды и run_polling как бесконечный цикл. Токен пока в константе TOKEN — перенесём в .env следующей правкой. Бота регистрируют у @BotFather (следующий слайд), запускают локально; run_polling удерживает терминал — это норма, остановка через Ctrl+C.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск и разбор</div>
    <h2>Бот-эхо отвечает в <span class="acc">Telegram</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px;align-items:start">
    <div class="code-win">
      <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
      <div class="code-body"><span class="kw">import</span> os
<span class="kw">from</span> telegram <span class="kw">import</span> Update
<span class="kw">from</span> telegram.ext <span class="kw">import</span> (Application,
    MessageHandler, filters, ContextTypes)

TOKEN = <span class="st">"123456:ABC-DEF..."</span>   <span class="cm"># пока прямо здесь</span>

<span class="kw">async def</span> on_message(update: Update,
        context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    <span class="kw">await</span> update.message.reply_text(text)

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(
    filters.TEXT &amp; ~filters.COMMAND, on_message))
app.run_polling()   <span class="cm"># бот спрашивает Telegram</span></div>
    </div>
    <div class="kv">
      <div class="kv-row"><div class="k">async def</div><div class="v">Обработчик асинхронный, перед reply_text — await.</div></div>
      <div class="kv-row"><div class="k">filters.TEXT &amp; ~COMMAND</div><div class="v">Ловим обычный текст, но не команды.</div></div>
      <div class="kv-row"><div class="k">run_polling()</div><div class="v">Бесконечный цикл: бот сам спрашивает про сообщения.</div></div>
      <div class="ek-note ek-note--green" style="margin-top:12px">Бот повторил ваше сообщение в Telegram? Каркас готов — дальше подключим ответы через нейросеть.</div>
    </div>
  </div>
</div>"""},

    # 10 · TROUBLESHOOTING
    {"notes": "Разберите три типичные проблемы запуска бота-эхо. Исправьте ошибки у всех: этот же bot.py нужен дальше для всех пяти правок. Напомните: заранее проверьте, что python-telegram-bot ставится именно версии 20+ (в старом синтаксисе всё иначе).", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Типичные ситуации запуска</div>
    <h2>Если бот-эхо <span class="acc">не запустился</span></h2>
  </div>
  <div class="grid-3" style="margin-top:8px">
    <div class="ek-note ek-note--red">
      <h3>Unauthorized</h3>
      <p>Токен неверный или скопирован с лишним пробелом. Возьмите токен у <span class="code-chip">@BotFather</span> заново и вставьте целиком.</p>
    </div>
    <div class="ek-note ek-note--red">
      <h3>Старый синтаксис</h3>
      <p>Ошибки на <span class="code-chip">Application</span> или <span class="code-chip">async</span> — стоит старая библиотека. Нужна <span class="code-chip">python-telegram-bot</span> версии 20+.</p>
    </div>
    <div class="ek-note ek-note--red">
      <h3>Бот молчит</h3>
      <p>Пишете <span class="hl">не тому</span> боту. Проверьте, что открыли чат именно со своим <span class="code-chip">@username</span>, и что <span class="code-chip">run_polling</span> запущен.</p>
    </div>
  </div>
</div>"""},
]
