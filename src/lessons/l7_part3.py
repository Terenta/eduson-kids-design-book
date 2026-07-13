# -*- coding: utf-8 -*-
SLIDES = [
    # 20 · Troubleshooting каркаса
    {"notes": "Коротко разберите четыре ситуации. Чаще всего встречаются пустой или повреждённый diary.json и забытый pip install requests. Тем, у кого не запускается, помогите лично; остальные сверяются со слайдом.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Если дневник не запустился</div>
    <h2>Типичные ситуации <span class="acc">запуска</span></h2>
  </div>
  <div class="kv" style="margin-top:6px">
    <div class="kv-row"><div class="k">JSONDecodeError</div><div class="v">Файл <span class="code-chip">diary.json</span> пустой или повреждён. Удалите его — он создастся заново при первой записи.</div></div>
    <div class="kv-row"><div class="k">FileNotFoundError</div><div class="v">Файла ещё нет — это нормально при первом запуске. Программа должна проверять его наличие перед чтением.</div></div>
    <div class="kv-row"><div class="k">ModuleNotFoundError</div><div class="v">Библиотека <span class="code-chip">requests</span> не установлена. В терминале: <span class="code-chip">pip install requests</span> — и запускайте снова.</div></div>
    <div class="kv-row"><div class="k">401 Unauthorized</div><div class="v">Проверьте ключ в константе <span class="code-chip">API_KEY</span>: он начинается с <span class="code-chip">sk-</span>, стоит в кавычках, без пробелов. Ключ понадобится на шаге с тегами.</div></div>
  </div>
</div>"""},

    # 21 · Правка 1 — сохранение (промпт в тот же чат)
    {"notes": "Первая правка идёт в тот же чат. После неё записи сохраняются в файле и остаются между запусками программы. Дождитесь, пока у всех появится diary.json с первой записью, потом переходите дальше.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 1 · сохранение</div>
    <h2>Запись сохраняется <span class="acc">между запусками</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Доработай diary.py, остальное не меняй. Пункт «новая запись»:
- Спроси текст записи через input
- Добавь текущую дату из datetime
- Собери запись как словарь с полями дата и текст и добавь её в список записей
- Сохрани весь список в файл diary.json через json.dump с ensure_ascii=False и indent=2
- При запуске программы, если diary.json уже есть, загрузи записи из него через json.load

Верни весь файл целиком.</div>
  </div>
</div>"""},

    # 22 · Разбор кода — список в файл и обратно
    {"notes": "Дайте минимум теории про файлы. Главное: сохраняем и читаем весь список целиком. ensure_ascii=False и indent=2 делают файл читаемым. Откройте diary.json в VS Code и покажите структуру.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Как список попадает в файл <span class="acc">и обратно</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">with</span> open(<span class="st">"diary.json"</span>, <span class="st">"w"</span>, encoding=<span class="st">"utf-8"</span>) <span class="kw">as</span> f:
    json.dump(entries, f, ensure_ascii=<span class="kw">False</span>, indent=<span class="st">2</span>)   <span class="cm"># сохранили весь список</span>
...
<span class="kw">with</span> open(<span class="st">"diary.json"</span>, <span class="st">"r"</span>, encoding=<span class="st">"utf-8"</span>) <span class="kw">as</span> f:
    entries = json.load(f)                                <span class="cm"># прочитали весь список</span></div>
  </div>
  <div class="ek-note"><span class="code-chip">json.dump</span> сохраняет <b>весь список целиком</b>, <span class="code-chip">json.load</span> читает его обратно. <span class="code-chip">ensure_ascii=False</span> — русские буквы остаются читаемыми, <span class="code-chip">indent=2</span> — файл с отступами, его видно глазами.</div>
</div>"""},

    # 23 · Правка 2 — AI-теги (промпт в тот же чат)
    {"notes": "Ключевая правка урока: нейросеть читает запись и подбирает теги. Раздайте ключи заранее и проверьте интернет. Это видимый результат: ученик пишет запись, а программа сохраняет её уже с тегами.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 2 · AI-теги</div>
    <h2>Нейросеть <span class="acc">подбирает теги</span> сама</h2>
  </div>
  <p>Главный шаг: программа отправляет запись нейросети, а та возвращает <span class="hl">теги</span> — короткую разметку смысла записи.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:8px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Добавь автоматические теги. После ввода текста отправь его в DeepSeek API (url https://api.deepseek.com/chat/completions, модель deepseek-chat, библиотека requests) с системной ролью:
«Ты помощник дневника. Прочитай запись и верни 3-5 тегов через запятую, одной строкой, без пояснений».

Ответ нейросети разбей на список тегов и сохрани в поле tags записи. Ключ бери из API_KEY. Верни весь файл.</div>
  </div>
</div>"""},

    # 24 · Разбор кода — из строки в список тегов
    {"notes": "Покажите, как строка от нейросети превращается в список тегов. split режет по запятой, strip убирает пробелы. Дайте написать пару записей и проверить теги. Если у кого-то в тегах есть нумерация или точка в конце, объясните: модель не всегда строго следует роли. Поиск всё равно может сработать, а при необходимости промпт можно уточнить: вернуть строго через запятую.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Из строки нейросети — <span class="acc">в список тегов</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">headers = {<span class="st">"Authorization"</span>: <span class="st">f"Bearer {API_KEY}"</span>}
data = {
    <span class="st">"model"</span>: <span class="st">"deepseek-chat"</span>,
    <span class="st">"messages"</span>: [
        {<span class="st">"role"</span>: <span class="st">"system"</span>, <span class="st">"content"</span>: <span class="st">"Ты помощник дневника, верни теги через запятую"</span>},
        {<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: text},
    ],
}
response = requests.post(url, headers=headers, json=data)
answer = response.json()[<span class="st">"choices"</span>][<span class="st">0</span>][<span class="st">"message"</span>][<span class="st">"content"</span>]
tags = [t.strip() <span class="kw">for</span> t <span class="kw">in</span> answer.split(<span class="st">","</span>)]</div>
  </div>
  <div class="ek-note ek-note--green">Нейросеть вернула строку <span class="code-chip">"шахматы, победа, дружба"</span>. <span class="code-chip">split(",")</span> режет её по запятым в список, <span class="code-chip">strip()</span> убирает лишние пробелы. Пишете запись — теги <b>добавляются автоматически</b>: это видимый результат работы нейросети.</div>
</div>"""},

    # 25 · vs — два параметра для читаемого файла
    {"notes": "Зафиксируйте два параметра json.dump. Откройте diary.json без ensure_ascii=False и с ним — разница будет понятна сразу. Это частая ошибка при работе с русским текстом.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Полезное знание</div>
    <h2>Два параметра для <span class="acc">читаемого файла</span></h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>Без ensure_ascii=False</h4>
      <p>В файле вместо слова — коды: <span class="code-chip">"шах..."</span>.</p>
      <p class="note">Программа прочитает, а человек — нет.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>С ensure_ascii=False, indent=2</h4>
      <p>В файле читаемо и с отступами: <span class="code-chip">"шахматы"</span>.</p>
      <p class="note">Дневник можно открыть и прочитать как текст.</p>
    </div>
  </div>
  <p>С этими параметрами JSON-файл читают и <span class="hl">человек, и программа</span>.</p>
</div>"""},

    # 26 · Правка 3 — показать все (промпт в тот же чат)
    {"notes": "Правка 3 подключает пункт «показать все». После неё видно, что записи действительно сохранились. Дождитесь, пока у всех список печатается, потом переходите дальше.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 3 · показать все</div>
    <h2>Весь дневник <span class="acc">на экране</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Оживи пункт «показать все». Прочитай diary.json и аккуратно распечатай каждую запись: дату, текст и теги. Если записей ещё нет — напиши «Дневник пока пуст».

Верни весь файл.</div>
  </div>
</div>"""},

    # 27 · Разбор кода — перебираем список словарей
    {"notes": "Свяжите с уроком 6: список перебираем циклом for, из словаря берём поля по ключу. join склеивает список тегов в строку. Не углубляйтесь в каждый символ.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Перебираем <span class="acc">список словарей</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">for</span> e <span class="kw">in</span> entries:
    print(e[<span class="st">"date"</span>], <span class="st">"—"</span>, e[<span class="st">"text"</span>])
    print(<span class="st">"Теги:"</span>, <span class="st">", "</span>.join(e[<span class="st">"tags"</span>]))</div>
  </div>
  <div class="ek-note">Список записей перебираем циклом <span class="code-chip">for</span> — как в игре на уроке 6. Из каждого словаря достаём поля по ключу: <span class="code-chip">e["date"]</span>, <span class="code-chip">e["text"]</span>, <span class="code-chip">e["tags"]</span>. <span class="code-chip">", ".join</span> склеивает список тегов в одну строку.</div>
</div>"""},

    # 28 · Правка 4 — поиск (промпт в тот же чат)
    {"notes": "Правка 4 показывает, зачем нужен JSON. После неё дневник можно искать по тегам. Дайте ученикам проверить поиск на своих записях.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 4 · поиск</div>
    <h2>Дневник с <span class="acc">поиском по тегу</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Оживи пункт «поиск по тегу». Спроси тег через input и покажи только те записи, у которых этот тег есть в списке tags. Если ничего не нашлось — так и скажи.

Верни весь файл.</div>
  </div>
</div>"""},

    # 29 · Разбор кода — фильтрация записей
    {"notes": "Главная мысль урока: структурированный дневник можно искать одной строкой, а плоский txt для этого не подходит. Дайте сфотографировать. Если группа отстаёт, правку 5 можно перенести в ДЗ.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Оставляем только <span class="acc">нужные записи</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">found = [e <span class="kw">for</span> e <span class="kw">in</span> entries <span class="kw">if</span> tag <span class="kw">in</span> e[<span class="st">"tags"</span>]]</div>
  </div>
  <div class="ek-note">Проходим по всем записям и оставляем те, где искомый тег есть в списке <span class="code-chip">tags</span>. Вот ради чего был нужен JSON: плоский <span class="code-chip">.txt</span> так не спросишь, а структурированный дневник ищется <b>одной строкой</b>.</div>
</div>"""},
]
