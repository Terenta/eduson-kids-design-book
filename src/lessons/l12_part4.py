# -*- coding: utf-8 -*-
SLIDES = [
    # 30 · ПРАВКА 5 · КОМАНДЫ ЧАТА
    {"notes": "ОПЦИОНАЛЬНАЯ, резервная правка — как и Правка 4, только по времени. Обязательный минимум к 55-й минуте — Правки 1–3 (стрим, личность, память): это уже готовый рабочий собеседник. Правка 5 превращает его в полноценный чат: команды /start, /help, /clear и цветное имя собеседника. Сохранение диалога в файл разбираем в ДЗ — там оно становится командой /save. Если времени не осталось — целиком отдайте правку в ДЗ; если осталось несколько минут — оставьте только /clear и цветное имя.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Правка 5 · команды чата</div>
      <h2>Команды, как в <span class="acc">полноценном чате</span></h2>
    </div>
    <p>В чат-ботах команды часто начинаются со слэша. Добавим главные команды — и цветное имя собеседника, как в мессенджере. Сохранение диалога в файл оставим на домашнее задание.</p>
    <div class="prompt-card prompt-card--copy" style="margin-top:14px">
      <span class="pc-tag">→ В тот же чат</span>
      <div class="pc-text">Добавь команды управления чатом, как в настоящих ботах, и раскрась вывод. Верни весь файл.

Подсказки для нейросети:
- /start — начать заново: снова покажи выбор личности и очисти память диалога
- /help — выведи список всех команд с пояснениями
- /clear — сотри память диалога (список messages), но оставь выбранную личность
- /exit — выход из программы вместо слова «выход»
- команды проверяй до отправки запроса нейросети
- имя собеседника печатай перед каждым ответом ANSI-цветом (например, \033[35m), без сторонних библиотек</div>
    </div>
  </div>"""},

    # 31 · РАЗБОР · КОМАНДЫ И ЦВЕТНОЕ ИМЯ
    {"notes": "Ключевой разбор финальной правки. Главное: команды перехватываем сразу после input, до запроса к нейросети — continue возвращает к вводу. /clear оставляет в messages только первый элемент — system, поэтому личность не теряется; /start очищает всё и заново показывает меню личностей. ANSI-код включения цвета обязательно закрываем кодом сброса — иначе весь терминал останется фиолетовым.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Разбор кода</div>
      <h2>Команды перехватываем <span class="acc">до запроса</span></h2>
    </div>
    <p>Слэш-команды проверяем сразу после <span class="code-chip">input</span> — до обращения к нейросети. Команды <span class="code-chip">/clear</span> и <span class="code-chip">/start</span> меняют список <span class="code-chip">messages</span>, а <span class="code-chip">/help</span> печатает подсказку:</p>
    <div class="code-win" style="margin-top:12px">
      <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
      <div class="code-body">text = input(<span class="st">"Вы: "</span>)

<span class="kw">if</span> text == <span class="st">"/help"</span>:
    print(<span class="st">"Команды: /start /help /clear /exit"</span>)
    <span class="kw">continue</span>                            <span class="cm"># ответ без запроса к нейросети</span>
<span class="kw">if</span> text == <span class="st">"/clear"</span>:
    messages = [messages[0]]            <span class="cm"># остаётся только system — личность</span>
    <span class="kw">continue</span>
<span class="kw">if</span> text == <span class="st">"/start"</span>:
    messages = []                       <span class="cm"># полный сброс…</span>
    <span class="cm"># …и снова меню личностей — остальное соберёт DeepSeek</span>

print(<span class="st">"\033[35m"</span> + name + <span class="st">":\033[0m "</span>, end=<span class="st">""</span>, flush=True)   <span class="cm"># имя цветом</span></div>
    </div>
    <div class="ek-note"><span class="code-chip">/clear</span> оставляет только <span class="code-chip">messages[0]</span> — первое system-сообщение, то есть личность. А <span class="code-chip">\033[35m</span> включает цвет, и <span class="code-chip">\033[0m</span> обязательно его <b>выключает</b> — иначе весь терминал останется фиолетовым.</div>
  </div>"""},

    # 32 · MINI-QUIZ 1
    {"notes": "Вопрос про роль assistant и память диалога — главная идея урока. Дайте 10–15 секунд, потом раскройте ответ. Свяжите с правкой 5: именно этот список messages стирает команда /clear.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Проверка · вопрос 1</div>
      <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
    </div>
    <div class="quiz-box" style="margin-top:10px">
      <span class="q-num">Вопрос 1</span>
      <p class="q-text">Рома собрал собеседника, но тот забывает предыдущие фразы: каждый ответ звучит так, будто разговор только начался. Что он забыл добавить в <span class="code-chip">messages</span>?</p>
      <div class="quiz-answer">
        <button class="quiz-btn" type="button">Показать ответ</button>
        <div class="quiz-reveal">
          <p>В список <span class="code-chip">messages</span> нужно добавлять не только вопросы пользователя (роль <span class="code-chip">user</span>), но и прошлые ответы нейросети как роль <b>assistant</b>. Тогда модель видит весь диалог целиком и помнит контекст.</p>
          <p>Без <span class="code-chip">assistant</span>-сообщений память теряется, и собеседник отвечает, будто впервые. Кстати, именно этот список и стирает команда <span class="code-chip">/clear</span>.</p>
        </div>
      </div>
    </div>
  </div>"""},

    # 33 · MINI-QUIZ 2
    {"notes": "Вопрос про то, что на практике меняет stream=True — вторая ключевая идея урока. Свяжите с привычкой: stream=True плюс print с параметрами end и flush — постепенная печать фрагментов, как в ChatGPT.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Проверка · вопрос 2</div>
      <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
    </div>
    <div class="quiz-box" style="margin-top:10px">
      <span class="q-num">Вопрос 2</span>
      <p class="q-text">Что на практике меняет параметр <span class="code-chip">stream=True</span>?</p>
      <div class="quiz-answer">
        <button class="quiz-btn" type="button">Показать ответ</button>
        <div class="quiz-reveal">
          <p>Ответ приходит не целиком после паузы, а маленькими кусочками (chunks), и мы печатаем их сразу — текст появляется на глазах, как в ChatGPT.</p>
          <p><span class="code-chip">print(piece, end="", flush=True)</span> выводит кусочки <b>в одну строку и сразу на экран</b>: <span class="code-chip">end=""</span> — без переноса, <span class="code-chip">flush=True</span> — не копить в буфере.</p>
        </div>
      </div>
    </div>
  </div>"""},

    # 34 · ОТЛАДКА
    {"notes": "Научите читать traceback снизу вверх — пригодится на всех уроках Python. Напомните привычку: непонятную ошибку целиком копируем в DeepSeek. Три поломки справа — самые частые именно в стриминге и с ключом.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Отладка</div>
      <h2>Читаем <span class="acc">ошибки</span> стрима</h2>
    </div>
    <div class="grid-2">
      <div class="col">
        <div class="term">
          <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
          <div class="term-body"><span class="dim">Traceback (most recent call last):
  File "companion.py", line 21, in &lt;module&gt;
    piece = chunk.choices[0].delta.content</span>
AttributeError: 'NoneType' object has
    no attribute 'content'</div>
        </div>
        <p style="margin-top:14px;font-size:15.5px">Traceback читаем <span class="hl">снизу вверх</span>: последняя строка — <b>что</b> случилось, строкой выше — <b>где</b>. Здесь <span class="code-chip">delta.content</span> оказался <span class="code-chip">None</span> — спасает <span class="code-chip">or ""</span>.</p>
      </div>
      <div class="info-card">
        <h3>Если застряли</h3>
        <ul class="clean">
          <li>Скопируйте <b>traceback целиком</b> в чат DeepSeek — попросите объяснить и починить</li>
          <li>Пустой ключ или <span class="code-chip">.env</span> не найден — проверьте <span class="code-chip">DEEPSEEK_KEY</span></li>
          <li>Текст лезет в столбик — забыли <span class="code-chip">end=""</span> в <span class="code-chip">print</span></li>
        </ul>
        <p style="margin-top:12px;font-size:14px;color:var(--ek-gray)">Та же привычка, что <span class="code-chip">console.log</span> в «Змейке» и print-метки на уроке 5.</p>
      </div>
    </div>
  </div>"""},

    # 35 · ПРИВЫЧКИ
    {"notes": "5 привычек урока. Дайте сфотографировать слайд. Особо подчеркните третью и четвёртую: assistant — это память (её и стирает /clear), а роли system/user/assistant — язык диалога с нейросетью.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Запомните</div>
      <h2>Привычки работы с <span class="acc">диалогом</span></h2>
    </div>
    <div class="kv">
      <div class="kv-row"><div class="k">01 · Стриминг — по кусочкам</div><div class="v"><span class="code-chip">stream=True</span> присылает ответ кусочками (chunks); <span class="code-chip">print(end="", flush=True)</span> печатает их сразу.</div></div>
      <div class="kv-row"><div class="k">02 · system задаёт личность</div><div class="v">Первое сообщение с ролью <span class="code-chip">system</span> управляет именем, стилем и характером всех ответов.</div></div>
      <div class="kv-row"><div class="k">03 · assistant — это память</div><div class="v">Каждый ответ нейросети дописываем в <span class="code-chip">messages</span> как <span class="code-chip">assistant</span>, иначе диалог забывается. Именно этот список стирает <span class="code-chip">/clear</span>.</div></div>
      <div class="kv-row"><div class="k">04 · Три роли диалога</div><div class="v"><span class="code-chip">system</span> — характер, <span class="code-chip">user</span> — ваши слова, <span class="code-chip">assistant</span> — ответы модели.</div></div>
      <div class="kv-row"><div class="k">05 · Ключ — это пароль</div><div class="v">Держим в <span class="code-chip">.env</span>, не публикуем, на скриншотах замазываем.</div></div>
    </div>
  </div>"""},

    # 36 · ЧЕК-ЛИСТ
    {"notes": "Чек-лист завершения собеседника. Кто отметил всё — пусть выберет личность, проверит память (спросить одно, потом сослаться на сказанное), а затем наберёт /clear и убедится: разговор забыт, характер остался. Это доказывает и память, и команды.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Чек-лист</div>
      <h2>Что должно быть к <span class="acc">55-й минуте</span></h2>
    </div>
    <div class="grid-2">
      <div class="info-card">
        <h3 style="color:var(--ek-green-deep)">Готово</h3>
        <ul class="clean">
          <li><span class="code-chip">companion.py</span> запускается командой <span class="code-chip">python companion.py</span></li>
          <li>Ответ появляется постепенно — виден стриминг</li>
          <li>Системный промпт задаёт характер собеседника</li>
          <li>Собеседник помнит прошлые фразы диалога</li>
        </ul>
      </div>
      <div class="info-card">
        <h3 style="color:var(--ek-violet-deep)">Работает</h3>
        <ul class="clean">
          <li>Меню из четырёх личностей: учитель, друг, пират, философ</li>
          <li><span class="code-chip">/start</span> начинает заново — выбор личности и чистая память</li>
          <li><span class="code-chip">/help</span> показывает команды, <span class="code-chip">/clear</span> стирает память (личность остаётся)</li>
          <li>Имя печатается цветом, выход — по команде <span class="code-chip">/exit</span></li>
        </ul>
      </div>
    </div>
    <div class="ek-note ek-note--green">Всё отмечено? Спросите что-нибудь и следующим вопросом сошлитесь на сказанное — собеседник помнит. Теперь наберите <span class="code-chip">/clear</span>: разговор забыт, характер на месте.</div>
  </div>"""},

    # 37 · ДЗ
    {"notes": "ДЗ — прокачать собеседника, примерно 30 минут. Каждое улучшение — отдельный диалог с DeepSeek, не всё сразу. Сохранение диалога перенесено сюда из правки 5 — теперь это команда /save. Напомните про ключ на скриншотах.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Домашнее задание · около 30 минут</div>
      <h2>Прокачайте <span class="acc">собеседника</span></h2>
    </div>
    <p>Три улучшения — каждое через отдельный диалог с DeepSeek:</p>
    <div class="grid-3">
      <div class="info-card">
        <h3>Пятая личность</h3>
        <p>К четырём готовым (учитель, друг, пират, философ) добавьте <b>свою</b>: имя, характер, манера речи — детальным системным промптом.</p>
      </div>
      <div class="info-card">
        <h3>Сохранить диалог</h3>
        <p>Добавьте команду <span class="code-chip">/save</span>, сохраняющую всю беседу в файл с датой в названии — например <span class="code-chip">dialog-2026-07-03.txt</span>.</p>
      </div>
      <div class="info-card">
        <h3>Диалог двух</h3>
        <p>Пусть две личности по очереди отвечают друг другу на заданную тему — маленький спор двух характеров.</p>
      </div>
    </div>
    <div class="ek-note ek-note--red">Пришлите скриншот диалога с собеседником — <b>ключ скройте!</b> Ваш самый удачный системный промпт — отдельным сообщением.</div>
  </div>"""},

    # 38 · ФИНАЛ
    {"cls": "slide--green",
     "notes": "Закройте урок. Сегодня собеседник печатает ответ постепенно, помнит разговор, меняет личность и слушается команд /start, /help, /clear. На уроке 13 — function calling: нейросеть сама запускает ваши функции, и получается AI-агент с инструментами.",
     "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">C</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">H</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">A</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">T</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="bubble">
      <h1>До встречи<br>на уроке 13!</h1>
      <p>Сегодня ваш собеседник печатает ответ постепенно (стриминг), помнит разговор через роли system/user/assistant, меняет личность и слушается команд /start, /help, /clear. На уроке 13 — function calling: научим нейросеть саму запускать ваши функции и соберём AI-агента с инструментами.</p>
    </div>
  </div>"""},
]
