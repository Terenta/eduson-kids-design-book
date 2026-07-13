# -*- coding: utf-8 -*-
SLIDES = [
    # 20 · TROUBLESHOOTING — если бот не отвечает
    {"notes": "Коротко разберите четыре ситуации. Чаще всего не поставлена библиотека или ученик пишет не тому боту. Тем, у кого бот молчит, помогите лично; остальные сверяются со слайдом. Напомните: run_polling удерживает терминал — это штатная работа.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Если бот не отвечает</div>
    <h2>Типичные ситуации <span class="acc">запуска</span></h2>
  </div>
  <div class="kv" style="margin-top:6px">
    <div class="kv-row"><div class="k">ModuleNotFoundError</div><div class="v">Библиотека не установлена. В терминале: <span class="code-chip">pip install python-telegram-bot</span> (версия 20+) — и запускайте снова.</div></div>
    <div class="kv-row"><div class="k">Unauthorized</div><div class="v">Токен неверный или не тот. Скопируйте <span class="code-chip">BOT_TOKEN</span> от <span class="code-chip">@BotFather</span> заново: целиком, без пробелов, с двоеточием внутри.</div></div>
    <div class="kv-row"><div class="k">Бот молчит</div><div class="v">Программа запущена, а ответа нет — скорее всего вы пишете <b>не тому боту</b>. Откройте бота по его <span class="code-chip">@username</span> из <span class="code-chip">@BotFather</span>.</div></div>
    <div class="kv-row"><div class="k">Терминал занят</div><div class="v"><span class="code-chip">run_polling()</span> не возвращает приглашение — это <b>норма</b>: пока программа работает, бот в сети. Остановить — <span class="code-chip">Ctrl+C</span>.</div></div>
  </div>
</div>"""},

    # 21 · ПРАВКА 1 — токен в .env
    {"notes": "Первая правка идёт в тот же чат. После неё токен переносится из константы в .env — правило с урока 8. Дождитесь, пока у всех бот-эхо снова отвечает в Telegram уже с токеном из .env, потом переходите дальше.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 1 · токен в .env</div>
    <h2>Токен переносим в <span class="acc">.env</span></h2>
  </div>
  <p>Секрет уходит из кода в отдельный файл — как ключ DeepSeek на уроке 8. В коде читаем токен через <span class="code-chip">python-dotenv</span>.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Заведи бота у @BotFather и получи токен. Положи токен в файл .env строкой BOT_TOKEN=..., а в коде читай через python-dotenv. Проверь, что бот-эхо отвечает в Telegram. Верни весь файл.</div>
  </div>
</div>"""},

    # 22 · РАЗБОР КОДА — как токен попадает в код из .env
    {"notes": "Дайте минимум теории. Главное: токен больше не в коде, а в .env — как ключ DeepSeek на уроке 8. load_dotenv читает файл, os.getenv достаёт значение по имени. Откройте .env в VS Code и покажите строку BOT_TOKEN. Ключ DEEPSEEK_KEY добавим в .env позже, на Правке 2, когда подключим нейросеть.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Как токен попадает в код из <span class="acc">.env</span></h2>
  </div>
  <div class="code-win" style="margin-top:6px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">from</span> dotenv <span class="kw">import</span> load_dotenv
<span class="kw">import</span> os

load_dotenv()                       <span class="cm"># прочитали файл .env рядом с bot.py</span>
TOKEN = os.getenv(<span class="st">"BOT_TOKEN"</span>)      <span class="cm"># достали токен по имени</span></div>
  </div>
  <p><span class="code-chip">load_dotenv()</span> читает файл <span class="code-chip">.env</span>, который лежит рядом с <span class="code-chip">bot.py</span>. <span class="code-chip">os.getenv("BOT_TOKEN")</span> достаёт значение по имени — ровно та же привычка, что с ключом DeepSeek на уроке 8. Токена в самом коде больше нет.</p>
</div>"""},

    # 23 · ПРАВКА 2 — отвечает нейросеть
    {"notes": "Ключевая правка урока: бот перестаёт повторять и начинает отвечать через нейросеть. Проверьте интернет и ключ DeepSeek в .env заранее. Это главный видимый результат: ученик пишет боту, бот возвращает ответ по смыслу.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 2 · отвечает нейросеть</div>
    <h2>Бот отвечает через <span class="acc">нейросеть</span></h2>
  </div>
  <p>Главный шаг урока: на каждое сообщение бот отправляет текст в <span class="hl">DeepSeek</span> и возвращает ответ нейросети — эхо превращается в AI-собеседника.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Подключи DeepSeek: на любое сообщение бот отправляет его текст в нейросеть и отвечает её ответом. Ключ DeepSeek положи в .env строкой DEEPSEEK_KEY=... и читай через python-dotenv. Верни весь файл.</div>
  </div>
</div>"""},

    # 24 · РАЗБОР КОДА — путь сообщения
    {"notes": "Покажите путь сообщения тремя строчками: взяли текст из update, отдали в ask_deepseek, ответ вернули через reply_text. Функция ask_deepseek — та же, что на уроках 5-8, её не переписываем. Дайте написать боту пару фраз и убедиться, что отвечает по смыслу.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Путь сообщения: Telegram → <span class="acc">DeepSeek</span> → назад</h2>
  </div>
  <div class="code-win" style="margin-top:6px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">async def</span> on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text          <span class="cm"># что написал человек</span>
    answer = ask_deepseek(text)         <span class="cm"># та же функция, что на уроках 5-8</span>
    <span class="kw">await</span> update.message.reply_text(answer)   <span class="cm"># ответ нейросети — в чат</span></div>
  </div>
  <div class="ek-note ek-note--green">Три шага: берём текст из <span class="code-chip">update.message.text</span>, отдаём его в <span class="code-chip">ask_deepseek(text)</span> — ту самую функцию с уроков 5-8, её не переписываем, — и возвращаем ответ через <span class="code-chip">reply_text</span>. Пишете боту любую фразу — он отвечает <b>по смыслу</b>, а не повтором.</div>
</div>"""},

    # 25 · ПОЛЕЗНОЕ ЗНАНИЕ — async и await
    {"notes": "Зафиксируйте два слова: async у обработчика и await перед reply_text. Идея простая: пока бот ждёт ответ от DeepSeek для одного человека, он не блокирует обработку других сообщений. Без await ответ не дойдёт — это частая ошибка.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Полезное знание</div>
    <h2>Два слова: <span class="acc">async</span> и await</h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>Обычная функция</h4>
      <p>Бот занят одним человеком — остальные ждут в очереди, пока придёт ответ.</p>
      <p class="note">Один медленный запрос блокирует остальных.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>async def и await</h4>
      <p>Пока бот ждёт ответ DeepSeek для одного — он принимает сообщения от других.</p>
      <p class="note"><span class="code-chip">await</span> перед <span class="code-chip">reply_text</span> обязателен.</p>
    </div>
  </div>
  <p>Обработчик — это <span class="code-chip">async def</span>, а перед отправкой ответа стоит <span class="code-chip">await</span>. Так бот не блокируется на одном пользователе и остаётся доступным для всех.</p>
</div>"""},

    # 26 · ПРАВКА 3 — /start и /help
    {"notes": "Правка 3 добавляет команды /start и /help — то, что видит человек, впервые открывший бота. Дождитесь, пока у всех по /start приходит приветствие, потом дальше. Напомните: команды начинаются со слэша и обрабатываются отдельно от обычного текста.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 3 · /start и /help</div>
    <h2>Первое, что видит <span class="acc">новый собеседник</span></h2>
  </div>
  <p>Команды со слэшем — то, с чего человек начинает знакомство с ботом. Их ловит отдельный обработчик.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Добавь команды: /start — приветствие «Привет! Я бот на нейросети, спроси что угодно», /help — короткая подсказка. Используй CommandHandler. Верни весь файл.</div>
  </div>
</div>"""},

    # 27 · РАЗБОР КОДА — команды отдельно от текста
    {"notes": "Свяжите с обработчиком текста: обычный текст ловит MessageHandler, команды со слэшем — CommandHandler. Вот зачем в фильтре стоит ~filters.COMMAND: чтобы /start не улетел в нейросеть. Не углубляйтесь в каждый аргумент.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Команды идут отдельно от <span class="acc">обычного текста</span></h2>
  </div>
  <div class="code-win" style="margin-top:6px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">async def</span> start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    <span class="kw">await</span> update.message.reply_text(<span class="st">"Привет! Я бот на нейросети, спроси что угодно"</span>)

app.add_handler(CommandHandler(<span class="st">"start"</span>, start))
app.add_handler(MessageHandler(filters.TEXT &amp; ~filters.COMMAND, on_message))</div>
  </div>
  <p>Команды со слэшем (<span class="code-chip">/start</span>, <span class="code-chip">/help</span>) ловит <span class="code-chip">CommandHandler</span>, а обычный текст — <span class="code-chip">MessageHandler</span>. Вот зачем в фильтре стоит <span class="code-chip">~filters.COMMAND</span>: чтобы <span class="code-chip">/start</span> не улетел в нейросеть, а попал в свой обработчик.</p>
</div>"""},

    # 28 · ПРАВКА 4 — характер бота
    {"notes": "Правка 4 задаёт боту характер через системную роль, как на уроках 6-7. Дайте ученикам придумать свою роль и сравнить ответы на один и тот же вопрос. Видимый результат — тон ответов меняется сразу.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 4 · характер бота</div>
    <h2>Бот получает <span class="acc">характер</span></h2>
  </div>
  <p>Тон ответов задаёт системная роль — приём с уроков 6-7. Придумайте боту свою личность и сравните, как меняются ответы на один вопрос.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Задай боту характер через системную роль (например, дружелюбный помощник-подросток). Ответы должны звучать в этом характере. Верни весь файл.</div>
  </div>
</div>"""},

    # 29 · РАЗБОР КОДА — характер в системной роли
    {"notes": "Главная мысль: характер задаётся системной ролью, как на уроках 6-7. Один и тот же вопрос при разных ролях даёт разные по тону ответы. Дайте сфотографировать. Если группа отстаёт — правку 5 (память и «печатает…») можно перенести в ДЗ.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Характер живёт в <span class="acc">системной роли</span></h2>
  </div>
  <div class="code-win" style="margin-top:6px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">messages = [
    {<span class="st">"role"</span>: <span class="st">"system"</span>, <span class="st">"content"</span>: <span class="st">"Ты дружелюбный помощник-подросток"</span>},
    {<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: text},
]</div>
  </div>
  <div class="ek-note">Характер задаёт первое сообщение с ролью <span class="code-chip">system</span> — ровно как на уроках 6-7. Меняете одну строку роли — и на <b>один и тот же вопрос</b> бот отвечает другим тоном. Сам вопрос при этом не трогаем.</div>
</div>"""},
]
