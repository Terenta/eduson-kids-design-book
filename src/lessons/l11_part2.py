# -*- coding: utf-8 -*-
SLIDES = [
    # 11 · requests ↔ SDK
    {"notes": "Сравнение бок о бок: было (ручной requests уроков 8–10) и стало (openai SDK). Подчеркните: результат тот же, кода меньше. URL, заголовки и разбор JSON библиотека берёт на себя.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как это работает</div>
    <h2>Ручной requests и <span class="acc">openai SDK</span></h2>
  </div>
  <p>Один и тот же запрос к DeepSeek — двумя способами. Результат одинаковый, но <span class="hl">SDK</span> берёт на себя URL, заголовки и разбор JSON.</p>
  <div class="vs">
    <div class="vs-col vs-col--plain">
      <h4>Было · уроки 8–10</h4>
      <p>Собирали запрос руками: <span class="code-chip">url</span>, <span class="code-chip">headers</span>, словарь <span class="code-chip">data</span>, потом <span class="code-chip">requests.post</span> и длинный разбор <span class="code-chip">response.json()["choices"][0]...</span></p>
      <p class="note">Много строк, легко ошибиться в скобках</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>Стало · урок 11</h4>
      <p>Создаём <span class="code-chip">client</span> и вызываем <span class="code-chip">client.chat.completions.create(...)</span>. Ответ достаём коротко: <span class="code-chip">response.choices[0].message.content</span></p>
      <p class="note">Описываем только суть запроса</p>
    </div>
  </div>
  <div class="ek-note">Мы больше не пишем адрес и заголовки руками — их знает библиотека <span class="code-chip">openai</span>. Меняем инструмент, а нейросеть та же — <b>DeepSeek</b>.</div>
</div>"""},

    # 12 · КАК УСТРОЕН ОТВЕТ SDK
    {"notes": "Роли system/user остались те же, что на уроках 8–10 — SDK их не меняет. Покажите, что текст достаём короче: response.choices[0].message.content вместо длинной цепочки из json().",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как это работает</div>
    <h2>Как устроен <span class="acc">ответ SDK</span></h2>
  </div>
  <p>Отправляем <span class="hl">список сообщений</span> с ролями — как на уроках 8–10. А ответ достаём одной короткой строкой.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">messages=[
    {"role": <span class="st">"system"</span>, "content": <span class="st">"Ты журналист. Пиши статью с заголовком и разделами."</span>},
    {"role": <span class="st">"user"</span>,   "content": <span class="st">"Напиши статью на тему: "</span> + topic},
]

article = response.choices[0].message.content   <span class="cm"># текст ответа</span></div>
  </div>
  <div class="grid-2">
    <div class="info-card"><h3>Роли те же</h3><span class="code-chip">system</span> задаёт характер, <span class="code-chip">user</span> — вопрос. SDK ничего в этом не меняет.</div>
    <div class="info-card"><h3>Ответ короче</h3>Вместо <span class="code-chip">response.json()["choices"][0]...</span> пишем <span class="code-chip">response.choices[0].message.content</span>.</div>
  </div>
</div>"""},

    # 13 · СИСТЕМНАЯ РОЛЬ ЖУРНАЛИСТА
    {"notes": "Новая роль DeepSeek на этом уроке: журналист. Урок 8 — переводчик, урок 9 — собеседник, сегодня пишет статью с заголовком и разделами. Снова всё решает системная роль.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Новая роль нейросети</div>
    <h2>Системная роль <span class="acc">журналиста</span></h2>
  </div>
  <p>В прошлых проектах DeepSeek был <span class="hl">помощником</span>. Сегодня у него новая работа: услышать тему и <span class="hl">написать статью</span> с заголовком и разделами.</p>
  <div class="info-card"><h3>Системная роль</h3>«Ты журналист. Пиши статью с заголовком и разделами».</div>
  <div class="ek-note">Видимый результат: называете тему — нейросеть <b>выдаёт готовую статью</b>. Не просто набор фактов, а текст с заголовком и разделами.</div>
</div>"""},

    # 14 · ЦЕЛЬ
    {"notes": "Прочитайте цель вслух. Подчеркните: статью пишет нейросеть, поэтому у каждого она своя. Две настройки temperature и max_tokens — то новое, ради чего урок. Слева теория, справа практика.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Цель · что будет в конце</div>
    <h2>Цель <span class="acc">урока</span></h2>
  </div>
  <div class="ek-note">К концу урока у каждого — генератор статей <span class="code-chip">writer.py</span>: называете тему, нейросеть через <b>openai SDK</b> пишет статью с заголовком и разделами, а вы настраиваете <span class="code-chip">temperature</span> и <span class="code-chip">max_tokens</span>.</div>
  <div class="grid-2" style="margin-top:10px">
    <div>
      <span class="chip">Узнаете</span>
      <ul class="clean" style="margin-top:14px">
        <li>Чем openai SDK удобнее ручного requests</li>
        <li>Что библиотека openai работает и с DeepSeek через base_url</li>
        <li>Как temperature и max_tokens управляют ответом</li>
      </ul>
    </div>
    <div>
      <span class="chip chip--green">Сделаете</span>
      <ul class="clean" style="margin-top:14px">
        <li>Соберёте генератор статей на openai SDK</li>
        <li>Сравните строгую и творческую версии</li>
        <li>Сохраните готовую статью в файл</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 15 · ДЕМО
    {"notes": "Покажите рабочий writer.py — соберите заранее. Введите тему при группе, чтобы все увидели, как нейросеть выдаёт статью. Затем покажите строгую и творческую версии.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Демо результата</div>
    <h2>Что <span class="acc">соберём</span> сегодня</h2>
  </div>
  <div class="term">
    <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
    <div class="term-body">✍️ Генератор статей
Тема статьи? <span class="usr">История видеоигр</span>
<span class="dim">Пишу статью... (openai SDK, temperature=0.7)</span>

# История видеоигр: от пикселей до целых миров
## С чего всё началось
Первые игры были простыми точками на экране...
## Золотая эпоха приставок
...
Статья сохранена в stat_История-видеоигр.md</div>
  </div>
  <p>Заголовок и разделы придумала <span class="hl">нейросеть</span> через openai SDK; готовый текст лёг в файл <span class="code-chip">stat_тема.md</span>.</p>
</div>"""},

    # 16 · ПАПКА И УСТАНОВКА
    {"notes": "Подготовка: warmup.py и writer.py лежат в той же папке lesson-11, библиотеки openai и python-dotenv уже стоят с разминки. Ключ DEEPSEEK_KEY берётся из .env: скопируйте .env с ключом в папку lesson-11, потому что load_dotenv читает .env из текущей папки. Библиотека requests больше не нужна.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Подготовка</div>
    <h2>Папка <span class="acc">lesson-11</span> и установка</h2>
  </div>
  <div class="grid-2">
    <div>
      <ol class="steps steps--tight">
        <li><div>Работаем в уже созданной папке <span class="code-chip">lesson-11</span> — там же, где <span class="code-chip">warmup.py</span></div></li>
        <li><div>Рядом создайте файл <span class="code-chip">writer.py</span></div></li>
        <li><div>Библиотеки <span class="code-chip">openai</span> и <span class="code-chip">python-dotenv</span> уже стоят с разминки</div></li>
        <li><div>Скопируйте <span class="code-chip">.env</span> с ключом <span class="code-chip">DEEPSEEK_KEY</span> в папку <span class="code-chip">lesson-11</span></div></li>
      </ol>
    </div>
    <div>
      <div class="term">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ПАПКА</span></div>
        <div class="term-body">vibe-coding/lesson-11/
├── warmup.py
├── writer.py
└── .env</div>
      </div>
      <div class="ek-note" style="margin-top:14px"><span class="code-chip">load_dotenv()</span> читает <span class="code-chip">.env</span> из текущей папки — файл с ключом должен лежать рядом с <span class="code-chip">writer.py</span>, а не в папках прошлых уроков.</div>
      <div class="ek-note" style="margin-top:12px">Библиотека <span class="code-chip">requests</span> больше не нужна — её работу берёт на себя <span class="code-chip">openai</span> SDK.</div>
    </div>
  </div>
</div>"""},

    # 17 · ПРОМПТ #2 · КАРКАС writer.py
    {"notes": "Скопировать промпт целиком в новый чат DeepSeek. Каркас — минимальный рабочий SDK-вызов: клиент OpenAI с base_url DeepSeek, один пробный вопрос к deepseek-chat, печать ответа. Ключ из .env. Раньше такой запрос писали руками через requests — теперь его собирает SDK. Наполнять генератором будем правками.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #2 · стартовый</div>
    <h2>Каркас <span class="acc">writer.py</span></h2>
  </div>
  <div class="prompt-card" style="margin-top:12px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — <span class="hl">опытный Python-разработчик</span> и наставник школьника.
Собери каркас writer.py на openai SDK — минимальный рабочий вызов: клиент OpenAI с base_url DeepSeek, один пробный вопрос к модели deepseek-chat и печать ответа. Ключ из .env. Раньше такой запрос писали руками через requests — теперь его собирает SDK, короче код. Верни весь файл.

Пиши так:
- from openai import OpenAI, ключ через os.getenv("DEEPSEEK_KEY") и load_dotenv()
- base_url="https://api.deepseek.com"
- ответ доставай как response.choices[0].message.content

Прокомментируй код для новичка. Ответь одним блоком кода.</div>
  </div>
</div>"""},

    # 18 · КЛЮЧ И ЗАПУСК
    {"notes": "Запуск каркаса. Проверьте, что .env с ключом DEEPSEEK_KEY скопирован в папку lesson-11 (load_dotenv читает .env из текущей папки, а не из папок прошлых уроков) и переменная называется DEEPSEEK_KEY. Дождитесь, пока у всех в терминале появится ответ нейросети.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск каркаса</div>
    <h2>Проверяем <span class="acc">ключ</span> и запускаем</h2>
  </div>
  <ol class="steps steps--tight">
    <li><div>Скопируйте код из ответа DeepSeek в <span class="code-chip">writer.py</span></div></li>
    <li><div>Рядом положите файл <span class="code-chip">.env</span> со строкой <span class="code-chip">DEEPSEEK_KEY=ваш-ключ</span></div></li>
    <li><div>Сохраните оба файла (<span class="code-chip">Ctrl+S</span>)</div></li>
    <li><div>В терминале выполните <span class="code-chip">python writer.py</span></div></li>
    <li><div>Дождитесь, пока нейросеть пришлёт ответ</div></li>
  </ol>
  <div class="ek-note ek-note--red">Ключ живёт в <span class="code-chip">.env</span>, а не в коде — так его не видно в <span class="code-chip">writer.py</span>. Ключ как пароль: на скриншотах для домашки скрываем.</div>
</div>"""},

    # 19 · ПЕРВАЯ СТАТЬЯ
    {"notes": "Момент: тот же результат, что раньше давал ручной requests, теперь получен коротким кодом на SDK. Каркас пустой по содержанию, но структура правильная — дальше наполняем правками.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Момент урока</div>
    <h2>Первый ответ через <span class="acc">SDK</span></h2>
  </div>
  <p>В терминале — ответ нейросети, полученный <span class="hl">без единой строки</span> ручного <span class="code-chip">requests</span>. Тот же результат, но код короче и понятнее.</p>
  <div class="ek-note ek-note--green">Весь запрос уместился в <span class="code-chip">client.chat.completions.create(...)</span>, а ответ достали строкой <span class="code-chip">response.choices[0].message.content</span>.</div>
  <div class="ek-note">Каркас пока просто печатает ответ, но <b>инструмент уже правильный</b> — дальше правками превратим его в генератор статей.</div>
</div>"""},
]
