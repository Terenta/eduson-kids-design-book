# -*- coding: utf-8 -*-
SLIDES = [
    # 20 · ЕСЛИ writer.py НЕ ЗАПУСТИЛСЯ
    {"notes": "Пробегитесь по четырём ситуациям. Чаще всего — забыли pip install openai и ключ DEEPSEEK_KEY не подхватился из .env. AuthenticationError — неверный ключ. Пустой ответ обычно значит слишком маленький max_tokens. Помогите лично тем, у кого не запускается, остальные сверяются со слайдом.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Если writer.py не запустился</div>
    <h2>Типичные ситуации <span class="acc">запуска</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">ModuleNotFoundError</div><div class="v">Библиотека <span class="code-chip">openai</span> не установлена. В терминале: <span class="code-chip">pip install openai python-dotenv</span> — и запускайте снова.</div></div>
    <div class="kv-row"><div class="k">ключ = None</div><div class="v">Файл <span class="code-chip">.env</span> лежит не в папке <span class="code-chip">lesson-11</span> или переменная названа не <span class="code-chip">DEEPSEEK_KEY</span>. Проверьте имя и место файла, вызов <span class="code-chip">load_dotenv()</span> должен быть до создания клиента.</div></div>
    <div class="kv-row"><div class="k">AuthenticationError</div><div class="v">Ключ неверный или с пробелом. Скопируйте <span class="code-chip">DEEPSEEK_KEY</span> заново в <span class="code-chip">.env</span>, без кавычек и лишних пробелов.</div></div>
    <div class="kv-row"><div class="k">Пустой ответ</div><div class="v">Ответ оборвался — маловат <span class="code-chip">max_tokens</span>. Увеличьте значение (например до <span class="code-chip">800</span>) и запустите снова.</div></div>
  </div>
</div>"""},

    # 21 · ПРАВКА 1 · ГЕНЕРАТОР СТАТЕЙ
    {"notes": "Первая правка идёт в тот же чат и превращает пробный вопрос каркаса в генератор статей: называешь тему — нейросеть пишет статью с заголовком и разделами. Это видимый результат. Дождитесь, пока у всех программа спрашивает тему и печатает готовую статью, потом идём дальше.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 1 · генератор статей</div>
    <h2>Назвал тему — получил <span class="acc">статью</span></h2>
  </div>
  <p>Главный шаг урока: программа спрашивает <span class="hl">тему</span>, а нейросеть в роли журналиста пишет статью с заголовком и разделами.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px"><span class="pc-tag">→ В тот же чат</span><div class="pc-text">Спроси тему через input и попроси нейросеть написать статью с заголовком и 3–4 разделами (системная роль — журналист). Распечатай статью.

Верни весь файл.</div></div>
</div>"""},

    # 22 · РАЗБОР · СИСТЕМНАЯ И ПОЛЬЗОВАТЕЛЬСКАЯ РОЛЬ
    {"notes": "Свяжите с уроками 8–10: роли system и user те же самые. system задаёт характер (журналист), user передаёт тему. Обратите внимание, что тему подставляем в текст через конкатенацию строк. Дайте ученикам написать пару статей на разные темы.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Две роли: <span class="acc">журналист</span> и тема</h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">topic = input(<span class="st">"Тема статьи: "</span>)

response = client.chat.completions.create(
    model=<span class="st">"deepseek-chat"</span>,
    messages=[
        {<span class="st">"role"</span>: <span class="st">"system"</span>, <span class="st">"content"</span>: <span class="st">"Ты журналист. Пиши статью с заголовком и разделами."</span>},
        {<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: <span class="st">"Напиши статью на тему: "</span> + topic},
    ],
)
article = response.choices[0].message.content</div>
  </div>
  <div class="ek-note ek-note--green">Роль <span class="code-chip">system</span> задаёт <b>характер</b> нейросети — журналист, который пишет с заголовком и разделами. Роль <span class="code-chip">user</span> передаёт <b>тему</b>. Тему подставляем в текст строкой: <span class="code-chip">"Напиши статью на тему: " + topic</span>. Те же две роли, что были на уроках 8–10.</div>
</div>"""},

    # 23 · ПОЛЕЗНОЕ ЗНАНИЕ · temperature
    {"notes": "Зафиксируйте настройку temperature до правки 2. Низкая (около 0.2) — строгий и предсказуемый ответ, высокая (около 0.9) — более творческая подача. Свяжите с квизом про чай: для инструкции нужна низкая, для сказки — высокая.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Полезное знание</div>
    <h2>temperature — <span class="acc">настройка</span> строгости и творчества</h2>
  </div>
  <div class="vs">
    <div class="vs-col vs-col--plain">
      <h4>temperature = 0.2</h4>
      <p>Ответы строгие и предсказуемые.</p>
      <p class="note">Для фактов: инструкции, справки, точные статьи.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>temperature = 0.9</h4>
      <p>Ответы креативные и разные каждый раз.</p>
      <p class="note">Для творчества: сказки, истории, необычные идеи.</p>
    </div>
  </div>
  <div class="ek-note"><span class="code-chip">temperature</span> — это настройка: ближе к <b>0</b> нейросеть отвечает строже и предсказуемее, ближе к <b>1</b> — свободнее и образнее.</div>
</div>"""},

    # 24 · ПРАВКА 2 · temperature
    {"notes": "Правка 2 показывает разницу на практике: одна и та же тема при temperature 0.2 и 0.9. Дайте ученикам сравнить строгую и творческую статью на своей теме — разница видна сразу. Дождитесь, пока у всех печатаются обе версии.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 2 · temperature</div>
    <h2>Одна тема — <span class="acc">два характера</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px"><span class="pc-tag">→ В тот же чат</span><div class="pc-text">Добавь возможность задавать temperature. Сгенерируй одну и ту же тему при temperature 0.2 и 0.9 и покажи разницу (строгая статья против фантазийной).

Верни весь файл.</div></div>
</div>"""},

    # 25 · РАЗБОР · ОДНА ТЕМА — ДВА ХАРАКТЕРА
    {"notes": "Покажите, что меняется только одно число — temperature, а тема и роли те же. При 0.2 статья строгая и по делу, при 0.9 — более образная и свободная. Дайте сфотографировать разницу выводов на экране.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Меняем одно число — меняется <span class="acc">характер</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">for</span> t <span class="kw">in</span> [0.2, 0.9]:
    response = client.chat.completions.create(
        model=<span class="st">"deepseek-chat"</span>,
        messages=[...],       <span class="cm"># тема и роли те же</span>
        temperature=t,        <span class="cm"># меняется только руль</span>
    )
    print(<span class="st">"temperature ="</span>, t)
    print(response.choices[0].message.content)</div>
  </div>
  <div class="ek-note">Тема и роли одинаковые — меняется <b>только</b> <span class="code-chip">temperature</span>. При <span class="code-chip">0.2</span> статья строгая и по делу, при <span class="code-chip">0.9</span> — более образная и свободная. Одно число заметно меняет стиль ответа.</div>
</div>"""},

    # 26 · ПРАВКА 3 · ПЛАН И max_tokens
    {"notes": "Правка 3 — два запроса вместо одного: сначала нейросеть выдаёт план (список разделов), потом отдельными запросами пишет каждый раздел. max_tokens ограничивает длину, чтобы ответ не обрывался и не был слишком длинным. Это заметно сложнее — помогите отстающим.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 3 · план и max_tokens</div>
    <h2>Сначала <span class="acc">план</span>, потом текст по разделам</h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px"><span class="pc-tag">→ В тот же чат</span><div class="pc-text">Сначала пусть нейросеть выдаёт план статьи (список разделов), потом отдельным запросом пишет каждый раздел; ограничь длину через max_tokens.

Верни весь файл.</div></div>
</div>"""},

    # 27 · РАЗБОР · ДВА ЗАПРОСА И ДЛИНА
    {"notes": "Главная мысль: сложную статью собираем в два шага — сначала план, потом каждый раздел отдельным запросом. max_tokens ограничивает длину каждого ответа: обрывается на полуслове — увеличьте, слишком длинно — уменьшите. Дайте сфотографировать.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Два запроса и <span class="acc">ограничение длины</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">plan = ask(<span class="st">"Составь план статьи на тему: "</span> + topic)   <span class="cm"># запрос 1: список разделов</span>

<span class="kw">for</span> section <span class="kw">in</span> plan:
    text = client.chat.completions.create(
        model=<span class="st">"deepseek-chat"</span>,
        messages=[...],           <span class="cm"># запрос 2: пишем раздел</span>
        max_tokens=400,           <span class="cm"># ограничение длины ответа</span>
    )</div>
  </div>
  <div class="ek-note ek-note--green">Сложную статью собираем в <b>два шага</b>: сначала нейросеть выдаёт план разделов, потом пишет каждый раздел отдельным запросом. <span class="code-chip">max_tokens</span> ограничивает длину: обрывается на полуслове — увеличьте, слишком длинно — уменьшите.</div>
</div>"""},

    # 28 · ПРАВКА 4 · СОХРАНЕНИЕ И ЦИКЛ
    {"notes": "Правка 4 собирает генератор воедино: статья сохраняется в файл, работает бесконечный цикл, вывод раскрашен. Это заметный результат — writer.py выглядит как полноценная программа. Правка объёмная: цикл while, запись в файл и ANSI-цвета сразу. Если группа отстаёт — оставьте только сохранение, а цикл и раскраску отдайте в ДЗ. Имя файла складывается из темы: stat_История-видеоигр.md.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 4 · сохранение и цикл</div>
    <h2><span class="acc">Сохранение</span> и цикл</h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px"><span class="pc-tag">→ В тот же чат</span><div class="pc-text">Сохраняй готовую статью в файл вида <span class="hl">stat_тема.md</span> — чтобы её можно было открыть и показать.

Дай генерировать статьи <span class="hl">по кругу</span>: после одной темы программа снова спрашивает следующую, а на слове «выход» останавливается.

И раскрась вывод ANSI-кодами, <span class="hl">без сторонних библиотек</span>:
- заголовок статьи — голубым
- имя сохранённого файла — зелёным

Верни весь файл.</div></div>
</div>"""},

    # 29 · РАЗБОР · СОХРАНЕНИЕ И ЦИКЛ
    {"notes": "Ключевой слайд правки. Разберите три вещи: цикл while True с выходом по слову, запись статьи в .md через open, и ANSI-коды \\033[...m. Имя файла складывается из темы: для «История видеоигр» получится stat_История-видеоигр.md. Подчеркните: цикл делает программу многоразовой — не нужно перезапускать writer.py ради каждой темы.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Цикл, файл и <span class="acc">цвета</span></h2>
  </div>
  <p>Три новинки правки — бесконечный цикл, запись статьи в файл и раскраска вывода:</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">while</span> True:
    topic = input(<span class="st">"Тема статьи (или «выход»): "</span>)
    <span class="kw">if</span> topic == <span class="st">"выход"</span>:
        <span class="kw">break</span>                              <span class="cm"># цикл прервётся, программа закончится</span>
    article = generate(topic)              <span class="cm"># запрос к DeepSeek по SDK</span>
    name = <span class="st">"stat_"</span> + topic.replace(<span class="st">" "</span>, <span class="st">"-"</span>) + <span class="st">".md"</span>
    <span class="kw">with</span> open(name, <span class="st">"w"</span>, encoding=<span class="st">"utf-8"</span>) <span class="kw">as</span> f:
        f.write(article)                   <span class="cm"># статья сохранена в .md</span>
    print(<span class="st">"\033[92m"</span> + name + <span class="st">"\033[0m"</span>)   <span class="cm"># зелёным — имя файла</span></div>
  </div>
  <div class="ek-note">Имя файла собирается из темы: для «История видеоигр» получится <span class="code-chip">stat_История-видеоигр.md</span>. <span class="code-chip">while True</span> повторяет генерацию, пока не введёте «выход» — одна программа на много статей. А <span class="code-chip">\033[92m ... \033[0m</span> — это ANSI-цвет: <span class="code-chip">92m</span> включает зелёный, <span class="code-chip">0m</span> выключает.</div>
</div>"""},
]
