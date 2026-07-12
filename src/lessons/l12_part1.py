# -*- coding: utf-8 -*-
# Урок 12 «Чат с AI, как в ChatGPT» · Часть 1 (слайды 1–10)
SLIDES = [
    # 1 · ТИТУЛ
    {"cls": "slide--violet",
     "notes": "Поприветствуйте. Сегодня соберём AI-собеседника с характером: его ответы печатаются постепенно, как в ChatGPT, системный промпт задаёт личность, а программа помнит разговор через роли system, user и assistant. Обязательный минимум — стриминг, личность и память; если группа успевает, добавляем меню личностей и команды /start, /help, /clear. Новое здесь — стриминг и память диалога; роли system и user ученикам знакомы с урока 5. К концу урока у каждого — рабочий собеседник в терминале.",
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
    <div class="cover-card">
      <div class="badge">Урок №12</div>
      <div class="card-top"><span class="win-dots"><i></i><i></i><i></i></span><span class="win-close"></span></div>
      <h1>Чат с AI,<br>как в ChatGPT</h1>
      <p class="cover-sub">Соберём AI-собеседника с характером: ответы печатаются по фрагментам через стриминг, системный промпт задаёт личность, а программа помнит весь диалог.</p>
      <div class="cover-chips"><span class="chip">Python</span><span class="chip chip--green">openai SDK</span><span class="chip chip--gray">Стриминг</span></div>
    </div>
  </div>"""},

    # 2 · AGENDA
    {"notes": "План. Теории — минимум: уже на 12-й минуте каждый запускает warmup.py и видит, как текст печатается постепенно. К 30-й — простой каркас собеседника (обычный вопрос-ответ без стрима). Дальше — правки через диалог. ВАЖНО про тайминг: обязательный минимум к 55-й минуте — правки со стримом, личностью и памятью, это уже рабочий собеседник. Меню личностей (учитель, друг, пират, философ) и команды /start, /help, /clear — резерв: каждая правка — это полная перегенерация companion.py, а у группы 13–15 лет весь блок идёт около 18 минут. Не успеваете — оставшиеся правки в ДЗ.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Agenda · план занятия</div>
    <h2>Как пройдут <span class="acc">60 минут</span></h2>
  </div>
  <div class="agenda" style="margin-top:14px">
    <div class="agenda-row"><span class="t">0–5</span><div><div class="tt">Разбор ДЗ</div><div class="dd">Смотрим статьи из writer.py: свой формат, варианты заголовка, сохранение в файл.</div></div></div>
    <div class="agenda-row"><span class="t">5–12</span><div><div class="tt">Стриминг и роли</div><div class="dd">Минимум теории — только чтобы собрать собеседника.</div></div></div>
    <div class="agenda-row"><span class="t">12–20</span><div><div class="tt">Промпт-разминка</div><div class="dd">warmup.py: один вопрос модели со stream=True, постепенная печать ответа.</div></div></div>
    <div class="agenda-row"><span class="t">20–30</span><div><div class="tt">Каркас собеседника</div><div class="dd">Простой цикл вопрос-ответ — пока без стрима и памяти.</div></div></div>
    <div class="agenda-row"><span class="t">30–48</span><div><div class="tt">Правки через диалог</div><div class="dd">Обязательно: стриминг → личность → память. Дальше — меню личностей (учитель, друг, пират, философ) и команды /start, /help, /clear.</div></div></div>
    <div class="agenda-row"><span class="t">48–55</span><div><div class="tt">Мини-вопросы и отладка</div><div class="dd">Читаем ошибки стрима и ключа, проверяем понимание.</div></div></div>
    <div class="agenda-row"><span class="t">55–60</span><div><div class="tt">Демо в группе</div><div class="dd">Проверяем стриминг и память; успевшие показывают выбор личности и команды чата.</div></div></div>
  </div>
</div>"""},

    # 3 · РАЗБОР ДЗ УРОКА 11
    {"notes": "Откройте 2–3 присланные статьи (на весь блок 5 минут). Разбирайте диалог с нейросетью, а не только результат. Подведите к главному: writer.py выдавал ответ целиком после паузы. Сегодня научим текст появляться постепенно и добавим собеседнику характер и память.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор ДЗ урока 11</div>
    <h2>Смотрим статьи из <span class="acc">writer.py</span></h2>
  </div>
  <p>Открываем 2–3 присланные статьи и разбираем именно <span class="hl">диалог с нейросетью</span>: свой формат и стиль, 5 вариантов заголовка, сохранение готовой статьи в файл.</p>
  <div class="grid-3" style="margin-top:20px">
    <div class="info-card"><h3>Что сработало</h3>Точные промпты: свой стиль через системную роль, варианты заголовка одним запросом, запись готовой статьи в файл.</div>
    <div class="info-card"><h3>Что переделывали</h3>Где забыли «верни весь файл» — нейросеть присылала обрывок, и статья не сохранялась целиком.</div>
    <div class="info-card"><h3>Вывод</h3>В <span class="code-chip">writer.py</span> ответ появлялся <b>целиком после паузы</b>. Сегодня сделаем, чтобы текст появлялся постепенно, как в ChatGPT.</div>
  </div>
</div>"""},

    # 4 · ИДЕЯ УРОКА
    {"notes": "Главная мысль: две новинки. Первая — стриминг: ответ печатается фрагментами, а не возникает целиком после паузы. Вторая — характер и память: системный промпт задаёт личность, роль assistant хранит весь диалог. Если группа успевает, добавляем меню личностей и команды управления чатом: /start начинает заново, /help показывает список команд, /clear стирает память. Роли system и user знакомы с урока 5, новое — assistant и stream=True.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Идея урока</div>
    <h2>Собеседник, который печатает <span class="acc">вживую</span> и помнит</h2>
  </div>
  <p>На уроке 11 <span class="code-chip">writer.py</span> выдавал ответ <span class="hl">целиком после паузы</span> — а в ChatGPT текст появляется постепенно, и у собеседника есть характер.</p>
  <div class="ek-note" style="margin-top:16px">Сегодня две новинки: включаем <b>стриминг</b> — ответ печатается фрагментами через <span class="code-chip">stream=True</span>, — и задаём собеседнику <b>личность системным промптом</b>. А чтобы он <b>помнил разговор</b>, каждый его ответ дописываем в диалог как роль <span class="code-chip">assistant</span>.</div>
  <p style="margin-top:14px">Управлять чатом будем командами, как в чат-ботах: <span class="code-chip">/start</span> — начать заново, <span class="code-chip">/help</span> — список команд, <span class="code-chip">/clear</span> — стереть память диалога.</p>
  <p style="margin-top:12px;font-size:14.5px;color:var(--ek-gray)">Роли <span class="code-chip">system</span> и <span class="code-chip">user</span> знакомы с урока 5 — новое здесь только <b>assistant</b> (память) и <b>stream=True</b> (живая печать).</p>
</div>"""},

    # 5 · КАК ОТВЕЧАЕТ ChatGPT
    {"notes": "Быстрый recap на живом примере: обычный запрос ждёт, пока модель допишет ответ, и лишь потом показывает его целиком. В ChatGPT текст начинает появляться сразу. Это и есть разница, которую сегодня повторим в коде. Не углубляйтесь — деталь про chunks на следующем слайде.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Вспоминаем</div>
    <h2>Как отвечает <span class="acc">ChatGPT</span></h2>
  </div>
  <p>На уроке 11 мы вызывали <span class="code-chip">client.chat.completions.create(...)</span> и ждали <span class="hl">весь ответ целиком</span>: пауза — и текст появлялся сразу весь.</p>
  <div class="code-win" style="margin-top:16px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">response = client.chat.completions.create(
    model=<span class="st">"deepseek-chat"</span>,
    messages=messages,
)
print(response.choices[0].message.content)   <span class="cm"># весь текст сразу, после паузы</span></div>
  </div>
  <div class="info-card" style="margin-top:16px">А в <b>ChatGPT</b> текст появляется <b>постепенно</b> — не нужно ждать конца. Тот же приём мы включим у себя одним параметром.</div>
</div>"""},

    # 6 · ЧТО ТАКОЕ СТРИМИНГ
    {"notes": "Ключевая новинка: со stream=True ответ приходит не целиком, а маленькими кусочками — chunks. Мы печатаем каждый кусочек сразу, и текст появляется на глазах. Покажите сравнение: ответ целиком после паузы против постепенной печати. Деталь про цикл for chunk — во второй части.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Новый приём</div>
    <h2>Что такое <span class="acc">стриминг</span></h2>
  </div>
  <div class="vs" style="margin-top:18px">
    <div class="vs-col vs-col--plain">
      <h4>Без стриминга</h4>
      <p>Модель дописывает весь ответ, и лишь потом он появляется на экране целиком. Долгий ответ — долгая пауза с пустым экраном.</p>
      <p class="note">Так работал writer.py.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>Стриминг (stream=True)</h4>
      <p>Ответ приходит маленькими кусочками — <b>chunks</b>. Каждый кусочек печатаем сразу — текст появляется постепенно, как в ChatGPT.</p>
      <p class="note">Это включим сегодня.</p>
    </div>
  </div>
  <p style="margin-top:16px">Один параметр <span class="code-chip">stream=True</span> меняет способ доставки: вместо целого ответа — <b>поток кусочков</b>, которые печатаются <b>вживую</b>.</p>
</div>"""},

    # 7 · РОЛИ И ХАРАКТЕР
    {"notes": "Recap ролей с урока 5: system задаёт, кто такой собеседник и как говорит, user — реплики человека. Новое — assistant: это ответы самой нейросети, которые мы дописываем в messages, чтобы собеседник помнил разговор. Детальный system и есть личность.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Вспоминаем и добавляем</div>
    <h2>Роли и <span class="acc">характер</span> собеседника</h2>
  </div>
  <p>Диалог с моделью — это список <span class="code-chip">messages</span>, где у каждого сообщения есть <span class="hl">роль</span>. Роли <span class="code-chip">system</span> и <span class="code-chip">user</span> вы знаете с урока 5.</p>
  <div class="code-win" style="margin-top:14px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">messages = [
    {<span class="st">"role"</span>: <span class="st">"system"</span>, <span class="st">"content"</span>: <span class="st">"Ты дружелюбный собеседник по имени Макс, любишь космос."</span>},
]
messages.append({<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: user_text})</div>
  </div>
  <div class="grid-3" style="margin-top:14px">
    <div class="info-card"><h3>system</h3>Личность собеседника: имя, стиль речи, интересы. Задаёт характер всех ответов.</div>
    <div class="info-card"><h3>user</h3>Реплики человека — то, что печатаете вы.</div>
    <div class="ek-note"><b>assistant</b> — новое: ответы нейросети. Дописываем их в <span class="code-chip">messages</span> — так рождается память.</div>
  </div>
</div>"""},

    # 8 · ПРОМПТ #1 · РАЗМИНКА
    {"notes": "Никакой долгой подготовки: сразу просим у DeepSeek маленький скрипт со стримингом и запускаем. Всё поверх openai SDK урока 11 — клиент с base_url DeepSeek, ключ из .env, ничего нового ставить не нужно. Дети копируют промпт целиком.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #1 · разминка</div>
    <h2>warmup.py за <span class="acc">две минуты</span></h2>
  </div>
  <p>Не будем долго готовиться — попросим у DeepSeek маленький скрипт со стримингом и сразу запустим его в терминале.</p>
  <div class="prompt-card" style="margin-top:28px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — опытный Python-разработчик и наставник школьника. Напиши warmup.py на openai SDK (клиент с base_url DeepSeek): отправь один вопрос модели deepseek-chat с параметром stream=True и печатай ответ по кусочкам (chunk.choices[0].delta.content) в одну строку через print(..., end="", flush=True). Прокомментируй, почему текст появляется по словам. Ответь одним блоком.</div>
  </div>
</div>"""},

    # 9 · ЗАПУСК И РАЗБОР warmup.py
    {"notes": "Самый наглядный момент урока: дождитесь, пока у всех текст начнёт появляться постепенно. На живом коде показываем сразу три вещи: stream=True, chunk.choices[0].delta.content и print с end и flush. Не идите дальше, пока не запустилось у каждого.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск и разбор</div>
    <h2>Текст появляется <span class="acc">постепенно</span></h2>
  </div>
  <div class="grid-2" style="margin-top:16px">
    <div>
      <ol class="steps steps--tight">
        <li><div>В <span class="code-chip">vibe-coding</span> создайте папку <span class="code-chip">lesson-12</span></div></li>
        <li><div>Создайте <span class="code-chip">warmup.py</span> и вставьте код из ответа</div></li>
        <li><div>Проверьте ключ <span class="code-chip">DEEPSEEK_KEY</span> в файле <span class="code-chip">.env</span></div></li>
        <li><div>Выполните <span class="code-chip">python warmup.py</span> и смотрите, как печатается ответ</div></li>
      </ol>
      <div class="ek-note ek-note--green" style="margin-top:14px">Текст появляется <b>постепенно</b>, а не сразу весь? Стриминг работает — фундамент собеседника готов.</div>
    </div>
    <div class="kv">
      <div class="kv-row"><div class="k" style="text-transform:none">stream=True</div><div class="v">Ответ придёт кусочками, а не целиком.</div></div>
      <div class="kv-row"><div class="k" style="text-transform:none">chunk.choices[0]<br>.delta.content</div><div class="v">Очередной кусочек текста из потока.</div></div>
      <div class="kv-row"><div class="k" style="text-transform:none">print(end="",<br>flush=True)</div><div class="v">Печатает кусочки в одну строку и сразу на экран.</div></div>
    </div>
  </div>
</div>"""},

    # 10 · ЕСЛИ НЕ ЗАПУСТИЛОСЬ
    {"notes": "Шпаргалка по трём типичным проблемам запуска стрима. Почините у всех — тот же ключ, папка и openai SDK нужны дальше для самого собеседника. Ошибку целиком всегда можно отправить в DeepSeek.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Типичные ситуации запуска</div>
    <h2>Если warmup.py <span class="acc">не запустился</span></h2>
  </div>
  <div class="grid-3" style="margin-top:20px">
    <div class="ek-note ek-note--red" style="font-size:15px;line-height:1.5"><b>Ключа нет / 401.</b> Нет файла <span class="code-chip">.env</span> или в нём пустой <span class="code-chip">DEEPSEEK_KEY</span>. Проверьте, что ключ на месте и <span class="code-chip">.env</span> лежит рядом со скриптом.</div>
    <div class="ek-note ek-note--red" style="font-size:15px;line-height:1.5"><b>AttributeError.</b> Падает на <span class="code-chip">delta.content</span>: иногда кусочек пустой. Берите его как <span class="code-chip">chunk.choices[0].delta.content or ""</span>.</div>
    <div class="ek-note ek-note--red" style="font-size:15px;line-height:1.5"><b>Текст с переносами.</b> Слова печатаются столбиком — забыт <span class="code-chip">end=""</span>. Печатайте кусочки через <span class="code-chip">print(piece, end="", flush=True)</span>.</div>
  </div>
  <p style="margin-top:18px">Не разобрались — отправьте текст ошибки целиком в тот же чат DeepSeek: он объяснит причину и пришлёт исправление. Рабочие ключ, папка и openai SDK нужны дальше — для самого собеседника.</p>
</div>"""},
]
