# -*- coding: utf-8 -*-
SLIDES = [
    # 11 · РЕГИСТРАЦИЯ БОТА У @BotFather
    {"notes": "Бота регистрирует сам ученик у @BotFather, не преподаватель. Проверьте заранее, что @BotFather доступен. @username обязан заканчиваться на bot, иначе имя не примут.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Регистрация бота</div>
    <h2>Заводим бота у <span class="acc">@BotFather</span></h2>
  </div>
  <p>Бота создаёт Telegram через официального бота <span class="code-chip">@BotFather</span>. Пять коротких шагов — и у вас есть токен.</p>
  <ol class="steps steps--tight" style="margin-top:8px">
    <li><b>Найдите @BotFather</b> — в поиске Telegram, официальный, с синей галочкой. Откройте чат.</li>
    <li><b>Отправьте <span class="code-chip">/newbot</span></b> — команда запускает создание нового бота.</li>
    <li><b>Имя бота</b> — как он подписан в чате, любое, например «Мой AI-помощник».</li>
        <li><b>@username</b> — заканчивается на <span class="code-chip">bot</span>, например <span class="code-chip">my_ai_helper_bot</span>.</li>
  </ol>
  <div class="ek-note ek-note--green">Шаг 5: <span class="code-chip">@BotFather</span> присылает <b>токен</b> вида <span class="code-chip">123456:ABC-DEF1234...</span> — ключ от вашего бота. На первом запуске положим его в код, а затем перенесём в <span class="code-chip">.env</span>.</div>
</div>"""},

    # 12 · ТОКЕН — ЭТО ПАРОЛЬ
    {"notes": "Ключевое правило безопасности урока. Токен = пароль от бота: по нему любой управляет ботом от вашего имени. Утёк — немедленно /revoke у @BotFather. На скриншотах ДЗ токен замазывать.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Безопасность</div>
    <h2>Токен — это <span class="acc">пароль</span> от бота</h2>
  </div>
  <p>Токен даёт <span class="hl">полный контроль</span> над ботом. Кто получил токен — управляет ботом от вашего имени: читает сообщения, отвечает, меняет настройки.</p>
  <div class="grid-2" style="margin-top:8px">
    <div class="ek-note ek-note--red">
      <h3>Никогда</h3>
      <p>Не выкладывайте токен в общий чат, не пишите прямо в коде на скриншотах, не отправляйте в мессенджере. На скриншотах для домашки — <b>замазывать</b>.</p>
    </div>
    <div class="ek-note ek-note--green">
      <h3>Если утёк</h3>
      <p>Немедленно перевыпустите у <span class="code-chip">@BotFather</span> командой <span class="code-chip">/revoke</span> или <span class="code-chip">/token</span>. Старый токен сразу перестанет работать.</p>
    </div>
  </div>
  <div class="ek-note">Поэтому токен хранят так же, как ключ DeepSeek на уроке 8 — в файле <span class="code-chip">.env</span>, который не попадает в репозиторий.</div>
</div>"""},

    # 13 · СЕКРЕТЫ ИЗ .env И ЗНАКОМЫЙ DeepSeek
    {"notes": "Recap с урока 8: load_dotenv + os.getenv читают секреты из .env. Функция ask_deepseek — та же, что на уроках 5-8, её тело сегодня не переписываем, а переиспользуем.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Recap · уроки 5-8</div>
    <h2>Секреты из .env и знакомый <span class="acc">DeepSeek</span></h2>
  </div>
  <p>Два секрета — токен бота и ключ нейросети — читаем из <span class="code-chip">.env</span>, как ключ на уроке 8. А запрос к DeepSeek берём готовый с уроков 5-8.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">import</span> os
<span class="kw">from</span> dotenv <span class="kw">import</span> load_dotenv
load_dotenv()
TOKEN = os.getenv(<span class="st">"BOT_TOKEN"</span>)           <span class="cm"># токен бота — как пароль</span>
API_KEY = os.getenv(<span class="st">"DEEPSEEK_KEY"</span>)      <span class="cm"># ключ нейросети — как на уроке 8</span></div>
  </div>
  <div class="ek-note"><span class="code-chip">ask_deepseek(text)</span> — <b>та же функция</b>, что раньше: <span class="code-chip">requests.post</span> к <span class="code-chip">api.deepseek.com</span>, модель <span class="code-chip">deepseek-chat</span>, ключ из <span class="code-chip">.env</span>. Её тело сегодня не пишем заново — переиспользуем.</div>
</div>"""},

    # 14 · ЦЕЛЬ УРОКА
    {"notes": "Прочитайте цель вслух. Главное — программа получает интерфейс в Telegram и отвечает другим пользователям. Слева теория, справа практика.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Goal · что будет в конце</div>
    <h2>Цель <span class="acc">урока</span></h2>
  </div>
  <div class="ek-note">К концу урока у каждого — свой Telegram-бот: он принимает сообщение, отправляет его в DeepSeek и присылает ответ обратно в чат. Бот доступен другим пользователям, помнит контекст и показывает «печатает…».</div>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>Узнаете</h3>
      <ul class="clean">
        <li>Как программа получает интерфейс в мессенджере через Bot API</li>
        <li>Что такое long polling и почему <span class="code-chip">run_polling</span> не закрывается</li>
        <li>Почему обработчик — <span class="code-chip">async def</span>, а перед ответом — <span class="code-chip">await</span></li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Сделаете</h3>
      <ul class="clean">
        <li>Зарегистрируете бота у <span class="code-chip">@BotFather</span></li>
        <li>Подключите к нему DeepSeek</li>
        <li>Добавите команды, характер и память</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 15 · ДЕМО РЕЗУЛЬТАТА
    {"notes": "Покажите заранее собранного бота на реальном телефоне. Напишите боту при группе: пусть все увидят «печатает…» и ответ нейросети прямо в Telegram. Нужен телефон с Telegram у каждого.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Демо результата</div>
    <h2>Что соберём <span class="acc">сегодня</span></h2>
  </div>
  <div class="term">
    <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">TELEGRAM</span></div>
    <div class="term-body">🤖 Мой AI-помощник · чат в Telegram

<span class="usr">Вы:  Привет! Посоветуй книгу про космос</span>
Бот: <span class="dim">печатает…</span>
Бот: Держи: «Краткая история времени» Стивена Хокинга —
     объясняет космос простым языком. Ещё варианты?

<span class="usr">Вы:  А что-нибудь для подростка?</span>
Бот: Тогда «Астрофизика с космической скоростью» —
     та же тема, но легче и с юмором.</div>
  </div>
  <div class="ek-note">Отвечает <span class="hl">нейросеть</span>, бот помнит предыдущий вопрос и показывает «печатает…». Всё это происходит прямо в <b>Telegram</b>, а не в терминале.</div>
</div>"""},

    # 16 · ПАПКА lesson-09 И БИБЛИОТЕКА
    {"notes": "Подготовка: bot.py в новой папке lesson-09. requests стоит с уроков 5-8, python-dotenv — с урока 8. Новая только python-telegram-bot версии 20+. Проверьте заранее, что библиотека ставится.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Подготовка</div>
    <h2>Папка <span class="acc">lesson-09</span> и библиотека</h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div>
      <ol class="steps steps--tight">
        <li>Создайте папку <span class="code-chip">lesson-09</span> в <span class="code-chip">vibe-coding</span></li>
        <li>Создайте в ней файл <span class="code-chip">bot.py</span> и файл <span class="code-chip">.env</span></li>
        <li>Установите библиотеки одной командой (см. справа)</li>
      </ol>
      <div class="ek-note"><span class="code-chip">requests</span> уже стоит с уроков 5-8, <span class="code-chip">python-dotenv</span> — с урока 8. Новая — только <span class="code-chip">python-telegram-bot</span>, версия <b>20+</b>.</div>
    </div>
    <div>
      <div class="term">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
        <div class="term-body">vibe-coding/lesson-09/
├── bot.py
└── .env

<span class="usr">pip install python-telegram-bot requests python-dotenv</span></div>
      </div>
      <div class="ek-note ek-note--red">Версия <b>20+</b> важна: в старой библиотеке синтаксис без <span class="code-chip">async</span> — весь код будет другим.</div>
    </div>
  </div>
</div>"""},

    # 17 · МОСТИК: ОТ ЭХА К НЕЙРОСЕТИ
    {"notes": "Мостик к правкам. Сейчас у учеников уже работает бот-эхо из части 1: повторяет текст. Дальше пять правок превратят его в AI-бота. Каждая правка — через диалог с DeepSeek, каждая меняет поведение в чате.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Момент урока · мостик</div>
    <h2>От эха — к нейросети за <span class="acc">пять правок</span></h2>
  </div>
  <p>Сейчас бот-эхо пока <span class="hl">повторяет</span> ваше сообщение. Ядро уже собрано: <span class="code-chip">MessageHandler</span> ловит текст, <span class="code-chip">run_polling</span> держит бота в сети. Осталось поменять одну строчку — <span class="hl">что</span> бот отвечает.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">async def</span> on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    answer = ask_deepseek(text)        <span class="cm"># раньше здесь было text — теперь ответ DeepSeek</span>
    <span class="kw">await</span> update.message.reply_text(answer)</div>
  </div>
  <div class="ek-note ek-note--green">Каждая из <b>пяти правок</b> — отдельный запрос к DeepSeek в тот же чат, и после каждой бот в Telegram меняет поведение: отвечает нейросетью, знает команды, получает характер и память.</div>
</div>"""},

    # 18 · ЗАПУСК БОТА-ЭХО
    {"notes": "Запуск бота-эхо с токеном прямо в константе TOKEN — как в каркасе на слайде 9. Про .env здесь ещё не говорим: перенос токена в .env будет отдельной Правкой 1. Вставьте токен от @BotFather в строку TOKEN, запустите python bot.py. run_polling удерживает терминал — это штатная работа. Дождитесь, пока у всех бот в сети.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск бота</div>
    <h2>Запускаем бота-эхо: <span class="acc">python bot.py</span></h2>
  </div>
  <ol class="steps steps--tight">
    <li>Вставьте токен от <span class="code-chip">@BotFather</span> прямо в строку <span class="code-chip">TOKEN = "..."</span> в <span class="code-chip">bot.py</span></li>
    <li>Сохраните файл (<span class="code-chip">Ctrl+S</span>)</li>
    <li>В терминале выполните <span class="code-chip">python bot.py</span></li>
    <li>Терминал занят и не возвращает приглашение — <b>это ожидаемо</b>: бот в сети</li>
  </ol>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">TOKEN = <span class="st">"123456:ABC-DEF..."</span>   <span class="cm"># токен от @BotFather, пока прямо в коде</span></div>
  </div>
  <div class="ek-note"><span class="code-chip">run_polling()</span> — <b>бесконечный цикл</b> long polling: бот сам постоянно спрашивает Telegram «есть новые сообщения?». Пока он запущен — бот работает. Остановить — <span class="code-chip">Ctrl+C</span>. Токен спрячем в <span class="code-chip">.env</span> следующей правкой.</div>
</div>"""},

    # 19 · ПИШЕМ БОТУ ПЕРВОЕ СООБЩЕНИЕ
    {"notes": "Промежуточный результат: каждый пишет своему боту в Telegram и получает эхо-ответ. Проверьте, что ученики пишут именно своему боту (правильный @username), а не соседнему. Это первый раз, когда их код отвечает через мессенджер.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Момент урока</div>
    <h2>Пишем боту <span class="acc">первое сообщение</span></h2>
  </div>
  <p>Найдите своего бота в Telegram по <span class="hl">@username</span>, откройте чат и отправьте любое сообщение. Бот-эхо <span class="hl">вернёт тот же текст</span> — значит, связь работает.</p>
  <div class="ek-note ek-note--green">Это <b>первый раз</b>, когда ваш код отвечает не в терминале, а человеку в мессенджере. Пока он только повторяет — но канал до Telegram уже открыт.</div>
  <div class="ek-note ek-note--red">Бот молчит? Проверьте, что пишете <b>своему</b> боту (тот самый <span class="code-chip">@username</span>), что токен в <span class="code-chip">TOKEN</span> вставлен целиком без пробелов и что <span class="code-chip">python bot.py</span> запущен и не остановлен.</div>
</div>"""},
]
