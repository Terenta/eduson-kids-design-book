# -*- coding: utf-8 -*-
SLIDES = [
    # 30 · ПРАВКА 5 · память и «печатает…»
    {"notes": "Финальная правка собирает бота в законченный вид: появляется память по пользователям и статус «печатает…». Это заметный пользовательский результат: бот отвечает с учётом контекста. Правка сложная: словарь по user_id хранит историю каждого, а send_chat_action требует правильного порядка вызова. Если группа отстаёт, оставьте только память, а «печатает…» отдайте в ДЗ. После правки попросите написать боту два-три сообщения подряд и убедиться, что он помнит начало разговора.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 5 · память и «печатает…»</div>
    <h2>Память и <span class="acc">«печатает…»</span></h2>
  </div>
  <p>Финальная правка собирает бота в законченный вид: он помнит контекст разговора и показывает статус, пока думает над ответом.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Финальная правка. Пусть бот <span class="hl">помнит несколько последних сообщений каждого пользователя</span>: заведи словарь по <span class="hl">user_id</span> со списком messages и передавай эту историю в DeepSeek, чтобы он понимал контекст разговора.

И пока бот думает над ответом, пусть показывает статус <span class="hl">«печатает…»</span> через send_chat_action. Верни весь файл.</div>
  </div>
</div>"""},

    # 31 · РАЗБОР · память = словарь по user_id
    {"notes": "Ключевой слайд урока. Подчеркните главное: у бота один код, но много собеседников, поэтому история хранится не в одной переменной, а в словаре по user_id — у каждого свой список сообщений. Если это не учесть, бот будет смешивать разговоры разных людей.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Почему память — словарь по <span class="acc">user_id</span></h2>
  </div>
  <p>Бот один, а собеседников много. У каждого своя история, поэтому храним её в словаре по <span class="code-chip">user_id</span> — список сообщений с ролями, тот самый формат, что уходит в DeepSeek на уроках 5-8.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">history = {}                       <span class="cm"># user_id -&gt; список сообщений с ролями</span>

<span class="kw">async def</span> on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    msgs = history.setdefault(user_id, [])          <span class="cm"># своя история для каждого</span>
    msgs.append({<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: text})  <span class="cm"># запомнили вопрос</span>
    answer = ask_deepseek(msgs)                      <span class="cm"># весь список — в DeepSeek</span>
    msgs.append({<span class="st">"role"</span>: <span class="st">"assistant"</span>, <span class="st">"content"</span>: answer})  <span class="cm"># и ответ бота</span></div>
  </div>
  <div class="ek-note">Одна общая переменная не подошла бы: сообщения Вани и Насти смешались бы. Ключ словаря <span class="code-chip">user_id</span> разделяет истории — у каждого <b>свой контекст</b>.</div>
</div>"""},

    # 32 · КВИЗ 1 · run_polling
    {"notes": "Вопрос про run_polling — прямое следствие того, что бот работает не закрываясь. Дайте 10-15 секунд, потом раскройте ответ. Свяжите с правилом: run_polling удерживает терминал — это штатная работа.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 1</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 1</span>
    <p class="q-text">Ваня написал бота, запустил, но окно программы не закрывается и не возвращает приглашение терминала. Он думает, что программа не работает. Так ли это?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>Нет. <span class="code-chip">run_polling()</span> запускает <b>бесконечный цикл</b> long polling: бот сам постоянно спрашивает у Telegram «есть новые сообщения?». Программа работает не закрываясь — пока она запущена, бот в сети.</p>
        <p>Остановить бота — <span class="code-chip">Ctrl+C</span> в терминале.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 33 · КВИЗ 2 · утёкший токен
    {"notes": "Вопрос про утёкший токен — вторая частая проблема. Свяжите с правилом: токен = пароль, хранится только в .env, на скриншотах скрыт. Напомните, что перевыпуск сразу отключает старый токен.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 2</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 2</span>
    <p class="q-text">Катя случайно выложила токен бота в чат класса. Что теперь может любой из одноклассников и что делать?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>По токену любой может <b>полностью управлять ботом</b> от её имени — читать сообщения и отвечать за неё.</p>
        <p>Токен нужно немедленно перевыпустить у <span class="code-chip">@BotFather</span> (<span class="code-chip">/revoke</span> или <span class="code-chip">/token</span>) — старый сразу перестанет работать. Хранить токен только в <span class="code-chip">.env</span>.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 34 · ОТЛАДКА · читаем ошибки
    {"notes": "Научите читать traceback снизу вверх — это пригодится на всех уроках Python. Напомните правило: непонятную ошибку целиком копируем в DeepSeek. Три проверки справа — самые частые именно с ботом: не тот бот, не запущен run_polling, не поставлена библиотека.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Отладка</div>
    <h2>Читаем <span class="acc">ошибки бота</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div>
      <div class="term">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
        <div class="term-body">Traceback (most recent call last):
  File <span class="st">"bot.py"</span>, line 12, in &lt;module&gt;
    app.run_polling()
telegram.error.InvalidToken: <span class="usr">Unauthorized</span></div>
      </div>
      <p style="font-size:14px;margin-top:10px;color:#3C3C45">Последняя строка — <b>что</b> случилось, строкой выше — <b>где</b>. <span class="code-chip">Unauthorized</span> значит: токен неверный или не тот.</p>
    </div>
    <div>
      <h3 style="margin-bottom:8px">Если бот молчит</h3>
      <ul class="clean">
        <li>Скопируйте <b>traceback целиком</b> в чат DeepSeek — попросите объяснить и починить</li>
        <li>Проверьте, что программа запущена и <span class="code-chip">run_polling</span> удерживает терминал</li>
        <li>Убедитесь, что пишете <b>тому же боту</b> — сверьте <span class="code-chip">@username</span></li>
      </ul>
      <div class="ek-note" style="margin-top:10px"><span class="code-chip">ModuleNotFoundError</span> значит, что не поставлена библиотека <span class="code-chip">python-telegram-bot</span>.</div>
    </div>
  </div>
</div>"""},

    # 35 · ПРАВИЛА (kv)
    {"notes": "5 правил урока. Дайте сфотографировать слайд. Особо подчеркните второе и третье: run_polling удерживает терминал — это норма, а токен = пароль и хранится только в .env.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запомните</div>
    <h2>Правила работы с <span class="acc">ботом</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">01 · Интерфейс в мессенджере</div><div class="v">Программа отвечает людям прямо в <b>Telegram</b>, а не только в локальном терминале.</div></div>
    <div class="kv-row"><div class="k">02 · run_polling — это норма</div><div class="v">Программа работает и не закрывается — значит бот в сети. Это штатная работа. Остановить — <span class="code-chip">Ctrl+C</span>.</div></div>
    <div class="kv-row"><div class="k">03 · Токен — это пароль</div><div class="v">Не публикуем, на скриншотах скрываем, храним только в <span class="code-chip">.env</span>. Утёк — перевыпускаем у <span class="code-chip">@BotFather</span>.</div></div>
    <div class="kv-row"><div class="k">04 · Обработчик — async и await</div><div class="v">Ловим сообщения через <span class="code-chip">async def</span>, а перед <span class="code-chip">reply_text</span> ставим <span class="code-chip">await</span> — тогда бот не блокируется на одном пользователе.</div></div>
    <div class="kv-row"><div class="k">05 · Характер и память</div><div class="v">Характер задаём системной ролью, а память — словарём по <span class="code-chip">user_id</span>: у каждого свой разговор.</div></div>
  </div>
</div>"""},

    # 36 · ЧЕК-ЛИСТ (grid-2 + ul.clean)
    {"notes": "Чек-лист завершения бота. Кто отметил всё, пусть даст ссылку на бота соседу и проверит, что тот тоже получает ответы нейросети. Это проверяет, что бот доступен другим пользователям.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Чек-лист</div>
    <h2>Готовность <span class="acc">к 55-й минуте</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div class="info-card">
      <h3>Готово</h3>
      <ul class="clean">
        <li><span class="code-chip">bot.py</span> запускается командой <span class="code-chip">python bot.py</span></li>
        <li>Токен лежит в <span class="code-chip">.env</span> строкой <span class="code-chip">BOT_TOKEN</span></li>
        <li>Бот отвечает нейросетью в <b>Telegram</b></li>
        <li>Есть команды <span class="code-chip">/start</span> и <span class="code-chip">/help</span></li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Работает</h3>
      <ul class="clean">
        <li>У бота свой характер через системную роль</li>
        <li>Бот помнит несколько последних сообщений</li>
        <li>Пока думает — показывает «печатает…»</li>
        <li>Бот отвечает не только вам, но и другому пользователю</li>
      </ul>
    </div>
  </div>
  <div class="ek-note ek-note--green">Всё отмечено? Дайте ссылку на бота соседу — пусть напишет и получит ответ нейросети. Бот доступен другому пользователю.</div>
</div>"""},

    # 37 · ДЗ (grid-3 из info-card)
    {"notes": "ДЗ — доработать бота, примерно 30 минут. Каждое улучшение — отдельный диалог с DeepSeek, не всё сразу. Напомните про токен и ключ на скриншотах: их нужно скрыть.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Домашнее задание · около 30 минут</div>
    <h2>Доработайте <span class="acc">бота</span></h2>
  </div>
  <p>Три улучшения — каждое через отдельный диалог с DeepSeek:</p>
  <div class="grid-3" style="margin-top:6px">
    <div class="info-card">
      <h3>Команда /joke</h3>
      <p>Добавьте команду <span class="code-chip">/joke</span> — бот просит у нейросети свежую шутку и присылает её.</p>
    </div>
    <div class="info-card">
      <h3>Свой характер</h3>
      <p>Придумайте боту яркую личность через системную роль и проверьте, как меняются ответы.</p>
    </div>
    <div class="info-card">
      <h3>Кнопки</h3>
      <p>Добавьте боту кнопки (<span class="code-chip">ReplyKeyboardMarkup</span>) с готовыми вопросами.</p>
    </div>
  </div>
  <div class="ek-note ek-note--red">Пришлите скриншот диалога с ботом — <b>токен и ключ скройте!</b> Ваш самый удачный промпт — отдельным сообщением.</div>
</div>"""},

    # 38 · ФИНАЛ · green bubble
    {"cls": "slide--green", "notes": "Закройте урок. Сегодня программа получила интерфейс в Telegram и начала отвечать другим пользователям. На уроке 10 — веб-приложение на Streamlit: тот же AI-помощник, но со ссылкой в браузере, которую можно открыть с любого устройства.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">B</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">O</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">T</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">G</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="bubble">
      <h1>До встречи<br>на уроке 10!</h1>
      <p>Сегодня программа получила интерфейс в Telegram: бот принимает сообщения от друзей и отвечает через нейросеть. На уроке 10 сделаем второй публичный проект — веб-приложение на Streamlit: тот же AI-помощник, но со ссылкой в браузере, которую можно открыть с любого устройства.</p>
    </div>
  </div>"""},
]
