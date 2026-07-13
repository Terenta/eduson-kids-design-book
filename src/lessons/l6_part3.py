# -*- coding: utf-8 -*-
SLIDES = [
    # 20 · Troubleshooting запуска каркаса
    {"notes": "Пробегитесь по четырём ситуациям. Чаще всего — забыли pip install requests или ключ вставлен с лишним пробелом. Помогите лично тем, у кого мастер молчит, остальные сверяются со слайдом.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Если игра не ответила</div>
    <h2>Типичные ситуации <span class="acc">запуска</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">ModuleNotFoundError</div><div class="v">Библиотека <span class="code-chip">requests</span> не установлена. В терминале: <span class="code-chip">pip install requests</span> — и запускайте снова.</div></div>
    <div class="kv-row"><div class="k">401 Unauthorized</div><div class="v">Ключ скопирован не целиком или с пробелом. Проверьте константу <span class="code-chip">API_KEY</span>: ключ начинается с <span class="code-chip">sk-</span> и стоит в кавычках.</div></div>
    <div class="kv-row"><div class="k">«Игра молчит»</div><div class="v">5–10 секунд тишины — это <span class="hl">мастер придумывает сцену</span>. Нормально. Дождитесь ответа.</div></div>
    <div class="kv-row"><div class="k">ConnectionError</div><div class="v">Программа не достучалась до интернета. Проверьте Wi-Fi и запустите ещё раз.</div></div>
  </div>
</div>"""},

    # 21 · Правка 1 · игровой цикл
    {"notes": "Первая правка идёт в тот же чат. После неё игра превращается в настоящее приключение. Дождитесь, пока у всех работает ход за ходом и слово «выход», потом идём дальше.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 1 · игра идёт по кругу</div>
    <h2>От одной сцены к целому <span class="acc">приключению</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Сейчас игра показывает одну сцену и закрывается. Сделай игровой цикл:
- После каждой сцены спрашивай выбор игрока через <span class="hl">input</span>: «Твой ход (1/2/3 или опиши действие): »
- Отправляй выбор мастеру следующим сообщением и печатай новую сцену
- Цикл повторяется, пока игрок не введёт <span class="hl">«выход»</span>
- Чтобы мастер помнил сюжет — храни все сообщения в списке <span class="hl">messages</span> и отправляй его целиком при каждом запросе

Верни весь файл.</div>
  </div>
</div>"""},

    # 22 · Разбор: цикл игры и память
    {"notes": "Минимум теории про цикл: while True крутит игру, break выходит. Главное — список messages растёт, поэтому мастер помнит прошлые ходы. Свяжите с памятью советчика из ДЗ урока 5.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Цикл игры и <span class="acc">память сюжета</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">messages = [{<span class="st">"role"</span>: <span class="st">"system"</span>, <span class="st">"content"</span>: <span class="st">"Ты — мастер игры…"</span>}]

<span class="kw">while</span> <span class="kw">True</span>:                              <span class="cm"># игра идёт по кругу</span>
    choice = input(<span class="st">"Твой ход: "</span>)
    <span class="kw">if</span> choice.lower() == <span class="st">"выход"</span>:
        <span class="kw">break</span>                            <span class="cm"># выйти из игры</span>
    messages.append({<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: choice})
    scene = ask_master(messages)         <span class="cm"># мастер придумывает сцену</span>
    messages.append({<span class="st">"role"</span>: <span class="st">"assistant"</span>, <span class="st">"content"</span>: scene})</div>
  </div>
  <p><span class="code-chip">while True</span> крутит игру ход за ходом, <span class="code-chip">break</span> — выход. Список <span class="code-chip">messages</span> растёт, поэтому мастер <span class="hl">помнит прошлые ходы</span> — как память советчика из ДЗ урока 5.</p>
</div>"""},

    # 23 · Правка 2 · декомпозиция на функции
    {"notes": "Ключевая правка урока: декомпозиция. Игра работает, но код длинный. Разложим на функции. Подчеркните: поведение не меняется, меняется только порядок.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 2 · наводим порядок</div>
    <h2>Разбираем игру на <span class="acc">функции</span></h2>
  </div>
  <p>Игра работает, но код стал длинным и запутанным. Разложим его на <span class="hl">функции</span> — отдельные понятные кусочки.</p>
  <div class="prompt-card prompt-card--copy">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Раздели game.py на функции, поведение не меняй:
- <span class="hl">ask_master(messages)</span> — отправляет запрос в DeepSeek и возвращает текст сцены
- <span class="hl">show(text)</span> — красиво печатает текст сцены
- <span class="hl">main()</span> — собирает игру: спрашивает имя героя, крутит игровой цикл

В самом конце файла вызови <span class="hl">main()</span>. Верни весь файл.</div>
  </div>
</div>"""},

    # 24 · Разбор: каждая функция — блок
    {"notes": "Покажите: каждая функция — отдельный блок с понятным именем. return отдаёт результат наружу. main() собирает блоки вместе. Не углубляйтесь в каждый символ.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Каждая функция — отдельный <span class="acc">блок</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">headers = {<span class="st">"Authorization"</span>: f<span class="st">"Bearer {API_KEY}"</span>}   <span class="cm"># пропуск с ключом</span>

<span class="kw">def</span> ask_master(messages):
    response = requests.post(url, headers=headers,
                             json={<span class="st">"model"</span>: <span class="st">"deepseek-chat"</span>, <span class="st">"messages"</span>: messages})
    <span class="kw">return</span> response.json()[<span class="st">"choices"</span>][0][<span class="st">"message"</span>][<span class="st">"content"</span>]

<span class="kw">def</span> show(text):
    print(text)</div>
  </div>
  <div class="ek-note ek-note--green">Каждая функция — <b>блок с понятным именем</b>: <span class="code-chip">ask_master</span> ходит к нейросети, <span class="code-chip">show</span> печатает, <span class="code-chip">main</span> собирает их вместе. <span class="code-chip">return</span> отдаёт результат наружу. Теперь игру проще чинить и улучшать: каждый кусок отдельно.</div>
</div>"""},

    # 25 · Параметры и return
    {"notes": "Зафиксируйте идею «чёрного ящика»: дал данные на вход, получил результат на выход. Параметры — вход, return — выход. Это пригодится на всех уроках Python.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Полезное знание</div>
    <h2>Параметры и <span class="acc">return</span></h2>
  </div>
  <p>Функции общаются двумя способами: <span class="hl">параметры</span> — что передаём внутрь, <span class="hl">return</span> — что функция отдаёт наружу.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">def</span> add(a, b):       <span class="cm"># a и b — параметры (вход)</span>
    <span class="kw">return</span> a + b     <span class="cm"># return — результат (выход)</span>

result = add(2, 3)   <span class="cm"># result = 5</span></div>
  </div>
  <div class="ek-note">Функция — это <b>«чёрный ящик»</b>: дал данные на вход, получил результат на выход. Игрок не знает, что внутри <span class="code-chip">ask_master</span> живёт нейросеть, — он получает готовую сцену.</div>
</div>"""},

    # 26 · Правка 3 · бросок кубика
    {"notes": "Правка 3 возвращает функцию roll_dice из разминки — функции переиспользуются. Дайте побросать кубик в игре и порадоваться, как удача и неудача меняют сюжет.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 3 · бросок кубика</div>
    <h2>Удача решает, как повернётся <span class="acc">сюжет</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Добавь случайность настоящей RPG. Перед отправкой хода мастеру брось кубик функцией <span class="hl">roll_dice()</span> (число 1–6, как в warmup.py):
- Если выпало <span class="hl">1</span> — припиши к сообщению мастеру пометку «(герою не повезло — пусть случится осложнение)»
- Если выпало <span class="hl">6</span> — припиши «(герою повезло — пусть случится удача)»

Так нейросеть учтёт удачу в сюжете. Верни весь файл.</div>
  </div>
</div>"""},

    # 27 · Разбор: функция зовёт функцию
    {"notes": "Покажите: одна функция (ход игры) зовёт другую (roll_dice) — функции соединяются в цепочку. Пометка в choice меняет сцену, которую придумает мастер.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Функция зовёт <span class="acc">функцию</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">luck = roll_dice()                  <span class="cm"># бросаем кубик из warmup.py</span>
<span class="kw">if</span> luck == 1:
    choice += <span class="st">" (герою не повезло — осложнение)"</span>
<span class="kw">elif</span> luck == 6:
    choice += <span class="st">" (герою повезло — удача)"</span></div>
  </div>
  <div class="ek-note ek-note--green">Одна функция (ход игры) зовёт другую (<span class="code-chip">roll_dice</span>) — функции соединяются в цепочку. Пометка в <span class="code-chip">choice</span> меняет сцену, которую придумает мастер. Бросьте кубик несколько раз — увидите, как удача и неудача поворачивают сюжет.</div>
</div>"""},

    # 28 · Правка 4 · HP и инвентарь
    {"notes": "Правка 4 вводит словарь и список. После запуска покажите строку с HP и инвентарём под сценой. Предупредите: мастер не всегда дописывает маркер [HP-20] или [+меч] — иногда HP и инвентарь меняются, иногда нет; на демо это нормально, надёжную механику добьём на следующих уроках. Если группа отстаёт по времени — правки 4 и 5 можно перенести в домашнее задание.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 4 · характеристики героя</div>
    <h2>HP и <span class="acc">инвентарь</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Дай герою состояние через словарь <span class="hl">state = {"hp": 100, "inventory": []}</span>:
- После каждой сцены печатай строку «❤️ HP: {hp}  🎒 {предметы}»
- Попроси мастера в системной роли иногда дописывать в конце ответа служебную строчку вида <span class="hl">[HP-20]</span> или <span class="hl">[+меч]</span>
- Программа находит эту строчку, уменьшает <span class="hl">state["hp"]</span> или добавляет предмет в список <span class="hl">inventory</span>

Верни весь файл.</div>
  </div>
</div>"""},

    # 29 · Разбор: словарь и список в деле
    {"notes": "Покажите словарь и список в работе. Главная мысль: один словарь state — это вся память героя. Дайте сфотографировать.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Словарь и список <span class="acc">в деле</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">state = {<span class="st">"hp"</span>: 100, <span class="st">"inventory"</span>: []}   <span class="cm"># память героя</span>

state[<span class="st">"hp"</span>] -= 20                       <span class="cm"># получили урон</span>
state[<span class="st">"inventory"</span>].append(<span class="st">"меч"</span>)        <span class="cm"># нашли предмет</span>

print(f<span class="st">"❤️ HP: {state['hp']}   🎒 {', '.join(state['inventory'])}"</span>)</div>
  </div>
  <div class="ek-note">Словарь <span class="code-chip">state</span> хранит характеристики по ключу, список <span class="code-chip">inventory</span> — найденные предметы. <span class="code-chip">.append</span> добавляет, <span class="code-chip">-=</span> снимает HP, <span class="code-chip">', '.join</span> склеивает список в строку. Один словарь <span class="code-chip">state</span> — <span class="hl">вся память героя</span>.</div>
</div>"""},
]
