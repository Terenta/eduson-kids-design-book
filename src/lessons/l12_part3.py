# -*- coding: utf-8 -*-
SLIDES = [
    # 20 · ЕСЛИ СОБЕСЕДНИК НЕ ЗАПУСТИЛСЯ
    {"notes": "Пробегитесь по четырём ситуациям простого каркаса (стрима тут ещё нет — его добавим Правкой 1). Чаще всего — забытый ключ в .env или не установленная библиотека. Помогите лично тем, у кого не запускается, остальные сверяются со слайдом.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Если собеседник не запустился</div>
    <h2>Типичные ситуации <span class="acc">запуска</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">нет ключа</div><div class="v">Модель молчит или ошибка авторизации. Проверьте: файл <span class="code-chip">.env</span> лежит рядом с <span class="code-chip">companion.py</span>, внутри строка <span class="code-chip">DEEPSEEK_KEY=...</span>, а в коде есть <span class="code-chip">load_dotenv()</span>.</div></div>
    <div class="kv-row"><div class="k">пустой ответ</div><div class="v">Собеседник ничего не печатает. Проверьте, что берёте текст из <span class="code-chip">response.choices[0].message.content</span> и печатаете его через <span class="code-chip">print</span>.</div></div>
    <div class="kv-row"><div class="k">нет выхода из цикла</div><div class="v">Программа не закрывается по «выход» — сверьте слово в условии выхода: оно должно точно совпадать с тем, что вводите (без лишних пробелов).</div></div>
    <div class="kv-row"><div class="k">ModuleNotFoundError</div><div class="v">Нет библиотеки <span class="code-chip">openai</span> или <span class="code-chip">python-dotenv</span>. В терминале: <span class="code-chip">pip install openai python-dotenv</span> — и запускайте снова.</div></div>
  </div>
</div>"""},

    # 21 · ПРАВКА 1 · СТРИМИНГ
    {"notes": "Первая правка идёт в тот же чат, где собран простой каркас. После неё ответ нейросети появляется постепенно вместо целого текста после паузы — самый наглядный момент урока. Дождитесь, пока текст начнёт появляться у всех, потом идём дальше.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 1 · стриминг</div>
    <h2>Ответ, который печатается <span class="acc">на глазах</span></h2>
  </div>
  <p>Сейчас ответ приходит целиком после паузы. Включаем <span class="hl">стриминг</span>: теперь он приходит кусочками и печатается по фрагментам — как в ChatGPT.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Включи в companion.py стриминг вместо обычного ответа: добавь stream=True в запрос и печатай ответ по словам циклом по chunk.choices[0].delta.content с print(end="", flush=True). Верни весь файл.</div>
  </div>
</div>"""},

    # 22 · РАЗБОР · КАК ПЕЧАТАЕТСЯ ПО СЛОВАМ
    {"notes": "Минимум теории. Главное: с stream=True ответ приходит не целиком, а кусочками; цикл забирает каждый кусочек и сразу печатает. Пустая строка защищает от None, end без переноса держит текст в одну строку, flush=True показывает немедленно. Покажите на экране, как текст появляется постепенно.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Как ответ появляется <span class="acc">постепенно</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">stream = client.chat.completions.create(
    model=<span class="st">"deepseek-chat"</span>,
    messages=messages,
    stream=<span class="kw">True</span>,               <span class="cm"># ответ придёт кусочками</span>
)
<span class="kw">for</span> chunk <span class="kw">in</span> stream:
    piece = chunk.choices[0].delta.content <span class="kw">or</span> <span class="st">""</span>
    print(piece, end=<span class="st">""</span>, flush=<span class="kw">True</span>)   <span class="cm"># печатаем по словам, без переносов</span>
print()</div>
  </div>
  <p style="margin-top:12px">С <span class="code-chip">stream=True</span> ответ приходит не целиком, а <b>кусочками</b> (chunks). Цикл <span class="code-chip">for chunk in stream</span> забирает очередной кусочек через <span class="code-chip">delta.content</span>, а <span class="code-chip">or ""</span> подставляет пустую строку, если кусочек пустой. <span class="code-chip">print(..., end="", flush=True)</span> печатает их <b>в одну строку и сразу</b> — текст появляется на экране постепенно.</p>
</div>"""},

    # 23 · ПРАВКА 2 · ЛИЧНОСТЬ
    {"notes": "Правка задаёт собеседнику характер через системный промпт. Базовая личность одна — в примере разбора это Макс, который любит космос; каждый описывает свою. Обязательно скажите: скоро сделаем меню из четырёх характеров — учитель, друг, пират, философ (Правка 4). Дайте ученикам написать пару фраз и услышать характер, потом идём к разбору.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 2 · личность</div>
    <h2>Собеседник с <span class="acc">характером</span></h2>
  </div>
  <p>Первое сообщение <span class="code-chip">system</span> задаёт личность: имя, стиль речи, интересы — и все ответы выдержаны в этом характере.</p>
  <p>Пока личность одна, базовая. Скоро добавим <span class="hl">меню из четырёх характеров</span> на выбор — это будет Правка 4.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Задай собеседнику характер детальным системным промптом (имя, стиль речи, интересы). Ответы должны звучать в этой личности. Верни весь файл.</div>
  </div>
</div>"""},

    # 24 · РАЗБОР · СИСТЕМНЫЙ ПРОМПТ ЗАДАЁТ ХАРАКТЕР
    {"notes": "Роли system/user знакомы с урока 5 — не объясняйте с нуля. Новое здесь: system управляет тоном ВСЕХ ответов, стоит первым в messages. Чем детальнее описание, тем ярче характер. Дайте поменять интересы Макса и услышать разницу.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Системный промпт задаёт <span class="acc">характер</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">messages = [
    {"role": <span class="st">"system"</span>, "content": <span class="st">"Ты дружелюбный собеседник по имени Макс, любишь космос."</span>},
]
messages.append({"role": <span class="st">"user"</span>, "content": user_text})</div>
  </div>
  <div class="ek-note" style="margin-top:14px">Роль <span class="code-chip">system</span> — это <b>первое сообщение</b> в <span class="code-chip">messages</span>, и оно управляет тоном всех ответов. Роли <span class="code-chip">system</span> и <span class="code-chip">user</span> вы уже видели на уроке 5. Чем детальнее описание — имя, стиль речи, интересы — тем ярче звучит характер собеседника.</div>
</div>"""},

    # 25 · ПОЛЕЗНОЕ ЗНАНИЕ · end="" И flush=True
    {"notes": "Зафиксируйте два параметра print. Покажите на экране разницу: без end=«» слова падают в столбик, без flush=True текст копится и вылетает пачкой. Это частая ошибка при первом стриме.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Полезное знание</div>
    <h2>Два параметра, которые делают <span class="acc">живую печать</span></h2>
  </div>
  <div class="vs">
    <div class="vs-col vs-col--plain">
      <h4>Обычный print</h4>
      <p>Каждый кусочек — с новой строки, текст копится и вылетает пачкой после паузы.</p>
      <p class="note">Фрагменты падают в столбик, постепенной печати нет</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>print(end="", flush=True)</h4>
      <p><span class="code-chip">end=""</span> — без переноса, кусочки идут в одну строку. <span class="code-chip">flush=True</span> — показать сразу, не копить в буфере.</p>
      <p class="note">Текст появляется постепенно, как в ChatGPT</p>
    </div>
  </div>
  <p style="margin-top:12px">Два параметра — и стрим печатается вживую: в одну строку и без задержки.</p>
</div>"""},

    # 26 · ПРАВКА 3 · ПАМЯТЬ ДИАЛОГА
    {"notes": "Правка 3 — сердце урока. После неё собеседник помнит, о чём говорили раньше: спросите про прошлую фразу — он вспомнит. Дождитесь, пока у всех диалог идёт по кругу, потом к разбору.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 3 · память диалога</div>
    <h2>Собеседник, который <span class="acc">помнит</span> разговор</h2>
  </div>
  <p>Диалог по кругу: каждый ответ нейросети дописываем в <span class="code-chip">messages</span> — и собеседник помнит всё, о чём говорили раньше.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Сделай диалог по кругу: копи сообщения в списке messages, добавляя каждый ответ нейросети как role assistant, — собеседник должен помнить, о чём говорили раньше. Выход по слову «выход». Верни весь файл.</div>
  </div>
</div>"""},

    # 27 · РАЗБОР · РОЛЬ assistant И КОНТЕКСТ
    {"notes": "Главное правило урока: собеседник помнит разговор, только если каждый его ответ дописан в messages как role assistant. Без этого модель видит лишь последний вопрос. Проверьте живьём: назовите Максу своё имя, потом спросите — он помнит, если строка с assistant на месте.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Роль <span class="acc">assistant</span> хранит контекст</h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">answer = <span class="st">""</span>
<span class="kw">for</span> chunk <span class="kw">in</span> stream:
    piece = chunk.choices[0].delta.content <span class="kw">or</span> <span class="st">""</span>
    print(piece, end=<span class="st">""</span>, flush=<span class="kw">True</span>)
    answer += piece                                        <span class="cm"># собираем ответ целиком</span>
messages.append({"role": <span class="st">"assistant"</span>, "content": answer})  <span class="cm"># память диалога</span></div>
  </div>
  <div class="ek-note ek-note--green" style="margin-top:14px">Пока стрим печатается, мы <b>копим кусочки в <span class="code-chip">answer</span></b>, а потом дописываем весь ответ в <span class="code-chip">messages</span> как <span class="code-chip">role: assistant</span>. Так модель на следующем шаге видит <b>весь диалог целиком</b> и помнит контекст. Забыли строку с <span class="code-chip">assistant</span> — собеседник отвечает без предыдущего контекста.</div>
</div>"""},

    # 28 · ПРАВКА 4 · МЕНЮ ЛИЧНОСТЕЙ
    {"notes": "ОПЦИОНАЛЬНАЯ, резервная правка — только если группа успевает. Обязательный минимум к 55-й минуте — Правки 1–3 (стрим, личность, память); Правки 4 и 5 требуют ещё двух полных перегенераций companion.py, а у группы 13–15 лет весь блок занимает около 18 минут. Если времени в обрез — эту правку перенесите в ДЗ и переходите к следующей части. Если успеваете: при запуске меню из четырёх личностей — учитель, друг, пират, философ, у каждой свой системный промпт. Дайте ученикам выбрать и поговорить с разными характерами.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 4 · меню личностей</div>
    <h2>Меню <span class="acc">характеров</span> при запуске</h2>
  </div>
  <p>Добавляем меню из четырёх личностей: <span class="hl">учитель</span>, <span class="hl">друг</span>, <span class="hl">пират</span> и <span class="hl">философ</span>. Выбор в начале подставляет свой системный промпт — и собеседник меняет характер.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Добавь при запуске меню из 4 личностей, у каждой — свой системный промпт: 1) учитель — терпеливо объясняет и приводит примеры, 2) друг — болтает просто и всегда поддерживает, 3) пират — рычит «Йо-хо-хо» и сыплет морскими словечками, 4) философ — отвечает вопросом на вопрос и рассуждает о смысле. Переключай характер выбором цифры. Верни весь файл.</div>
  </div>
</div>"""},

    # 29 · РАЗБОР · МЕНЮ ИЗ 4 СИСТЕМНЫХ ПРОМПТОВ
    {"notes": "Свяжите с началом урока: личность живёт в первом сообщении system. Меню — это выбор, какой из четырёх системных промптов встанет в начало messages. Личности ровно четыре: учитель, друг, пират, философ — у каждой свой system. Дайте сфотографировать. Анонсируйте: следующей правкой добавим команды /start, /help и /clear — как в чат-ботах.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Один выбор — свой <span class="acc">системный промпт</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">persons = {
    "1": <span class="st">"Ты строгий, но добрый учитель. Терпеливо объясняешь и приводишь примеры."</span>,
    "2": <span class="st">"Ты весёлый друг. Болтаешь просто и всегда поддерживаешь."</span>,
    "3": <span class="st">"Ты старый пират. Рычишь «Йо-хо-хо» и сыплешь морскими словечками."</span>,
    "4": <span class="st">"Ты философ. Отвечаешь вопросом на вопрос и рассуждаешь о смысле."</span>,
}
choice = input(<span class="st">"Выбери 1, 2, 3 или 4: "</span>)
messages = [{"role": <span class="st">"system"</span>, "content": persons[choice]}]</div>
  </div>
  <div class="ek-note" style="margin-top:12px">Четыре личности лежат в словаре <span class="code-chip">persons</span>: ключ — цифра меню, значение — свой <b>системный промпт</b>. Выбор пользователя достаёт нужный текст, и он встаёт <b>первым в <span class="code-chip">messages</span></b> как <span class="code-chip">system</span>. Один выбор — и характер собеседника меняется целиком. Следующей правкой добавим команды <span class="code-chip">/start</span>, <span class="code-chip">/help</span> и <span class="code-chip">/clear</span> — как в чат-ботах.</div>
</div>"""},
]
