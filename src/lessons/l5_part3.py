# -*- coding: utf-8 -*-
SLIDES = [
    # 20 · Троблшутинг советчика
    {"notes": "Пробегитесь по четырём ситуациям. Чаще всего — забыли pip install requests или ключ вставлен с лишним пробелом. Помогите лично тем, у кого не отвечает, остальные сверяются со слайдом.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Если советчик не ответил</div>
    <h2>Типичные ситуации <span class="acc">запуска</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">ModuleNotFoundError</div><div class="v">Библиотека <span class="code-chip">requests</span> не установлена. В терминале: <span class="code-chip">pip install requests</span> — и запускайте снова.</div></div>
    <div class="kv-row"><div class="k">401 Unauthorized</div><div class="v">Ключ скопирован не целиком или с пробелом. Проверьте константу <span class="code-chip">API_KEY</span>: ключ начинается с <span class="code-chip">sk-</span> и стоит в кавычках.</div></div>
    <div class="kv-row"><div class="k">«Программа молчит»</div><div class="v">5–10 секунд тишины — это <span class="hl">нейросеть думает</span>. Нормально. Подождите ответ.</div></div>
    <div class="kv-row"><div class="k">ConnectionError</div><div class="v">Программа не достучалась до интернета. Проверьте Wi-Fi и запустите ещё раз.</div></div>
  </div>
</div>"""},

    # 21 · Разбор кода: четыре строки к нейросети
    {"notes": "Разбор ядра. Не углубляйтесь в каждый символ: четыре смысловых блока — адрес, пропуск, посылка, ответ. Остальное дети уже видели в работе.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Четыре строки, которые ходят к <span class="acc">нейросети</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">url = <span class="st">"https://api.deepseek.com/chat/completions"</span>   <span class="cm"># адрес DeepSeek</span>
headers = {<span class="st">"Authorization"</span>: f<span class="st">"Bearer {API_KEY}"</span>}     <span class="cm"># пропуск: ваш ключ</span>

data = {
    <span class="st">"model"</span>: <span class="st">"deepseek-chat"</span>,                        <span class="cm"># какая модель отвечает</span>
    <span class="st">"messages"</span>: [
        {<span class="st">"role"</span>: <span class="st">"system"</span>, <span class="st">"content"</span>: <span class="st">"Ты дружелюбный советчик…"</span>},
        {<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: question},       <span class="cm"># вопрос из input</span>
    ],
}

response = requests.post(url, headers=headers, json=data)   <span class="cm"># отправили</span>
answer = response.json()[<span class="st">"choices"</span>][0][<span class="st">"message"</span>][<span class="st">"content"</span>] <span class="cm"># достали текст</span></div>
  </div>
  <p><span class="code-chip">headers</span> — пропуск с ключом, <span class="code-chip">data</span> — что отправляем, <span class="code-chip">response</span> — что вернулось. Всё остальное — обёртка.</p>
</div>"""},

    # 22 · Два сообщения — две роли
    {"notes": "Ключевая идея урока: в messages два сообщения с разными ролями. Системную роль пишем мы — это промпт внутри программы. Свяжите с уроком 2: те же техники промптинга.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Два сообщения — <span class="acc">две роли</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">role: system</div><div class="v">Характер и правила советчика. Пишем <b>мы, один раз</b>: «Ты дружелюбный советчик для подростка. Отвечай кратко, 2–3 предложения».</div></div>
    <div class="kv-row"><div class="k">role: user</div><div class="v">Живой вопрос пользователя — то, что пришло из <span class="code-chip">input</span>. Меняется при каждом запуске.</div></div>
  </div>
  <div class="ek-note">Системная роль — это <b>промпт, который живёт внутри программы</b>. Роль, контекст, формат, ограничения — те же 5 техник из урока 2, только теперь в вашем коде.</div>
</div>"""},

    # 23 · Правка 1 — имя
    {"notes": "Первая правка идёт в тот же чат. Дождитесь, пока у всех советчик зовёт по имени, потом идём дальше.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 1 · знакомство</div>
    <h2>Советчик зовёт <span class="acc">по имени</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:14px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Доработай advisor.py, остальное не меняй:
- Перед вопросом программа знакомится: спрашивает имя через input
- Дальше обращается по имени: «{имя}, о чём поговорим?»
- Имя добавь и в системную роль: «Пользователя зовут {имя}, обращайся к нему по имени»

Верни весь обновлённый advisor.py целиком.</div>
  </div>
</div>"""},

    # 24 · Правка 2 — выбор характера
    {"notes": "Самый весёлый момент урока. После запуска дайте 2–3 минуты поиграть с характерами: один и тот же вопрос — три разных советчика.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 2 · выбор характера</div>
    <h2>Меняем роль — меняем <span class="acc">советчика</span></h2>
  </div>
  <p>Код останется тем же. Поменяем только <span class="hl">текст системной роли</span> — и советчик станет другим «человеком».</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Добавь выбор характера при запуске:
- 1 — добрый друг: поддерживает, мягкий тон
- 2 — строгий тренер: краткие чёткие шаги, без сюсюканья
- 3 — весёлый кот: шутит и мурлычет, но советы дельные
- Пользователь вводит цифру, и в системную роль подставляется соответствующее описание
- Если ввели не 1/2/3 — используй характер 1

Верни весь файл.</div>
  </div>
</div>"""},

    # 25 · Промпт — часть программы
    {"notes": "Зафиксируйте вывод: качество программы с нейросетью равно качеству промпта внутри неё. Пусть каждый задаст один вопрос всем трём характерам.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Полезное знание</div>
    <h2>Промпт — <span class="acc">часть программы</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">characters = {
    <span class="st">"1"</span>: <span class="st">"Ты добрый друг: поддерживай и подбадривай."</span>,
    <span class="st">"2"</span>: <span class="st">"Ты строгий тренер: давай чёткие шаги, без воды."</span>,
    <span class="st">"3"</span>: <span class="st">"Ты весёлый кот: шути и мурлычь, но советуй дельно."</span>,
}
role = characters.get(choice, characters[<span class="st">"1"</span>])

messages = [{<span class="st">"role"</span>: <span class="st">"system"</span>, <span class="st">"content"</span>: role}, ...]</div>
  </div>
  <div class="ek-note ek-note--green">Код один и тот же — звучит советчик совершенно иначе. <b>Качество программы с нейросетью = качество промпта внутри неё.</b> Попробуйте все три характера на одном вопросе.</div>
</div>"""},

    # 26 · Правка 3 — диалог по кругу
    {"notes": "Правка 3. После неё советчик превращается в настоящий чат. Дождитесь, пока у всех работает «выход», потом идём дальше.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 3 · разговор по кругу</div>
    <h2>Диалог, а не <span class="acc">один ответ</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:14px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Сейчас советчик отвечает один раз и выключается. Сделай диалог:
- Программа спрашивает «{имя}, о чём поговорим?» по кругу
- На каждый вопрос — новый ответ нейросети
- Цикл крутится, пока пользователь не введёт «выход»
- После «выход» — попрощайся по имени

Верни весь файл.</div>
  </div>
</div>"""},

    # 27 · Разбор: вечный цикл
    {"notes": "Минимум теории про цикл: повторяет блок, break выходит. Подчеркните, почему проверка «выход» стоит до запроса — не тратим обращение к нейросети впустую. Подробно циклы — на уроке 6.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Как работает <span class="acc">вечный цикл</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">while</span> <span class="kw">True</span>:                          <span class="cm"># повторять бесконечно</span>
    question = input(f<span class="st">"{name}, о чём поговорим? "</span>)
    <span class="kw">if</span> question.lower() == <span class="st">"выход"</span>:
        <span class="kw">break</span>                        <span class="cm"># выйти из цикла</span>
    <span class="cm"># ...запрос к нейросети и печать ответа...</span></div>
  </div>
  <p><span class="code-chip">while True</span> повторяет блок снова и снова, <span class="code-chip">break</span> — выход. Проверка «выход» стоит <b>до</b> запроса, чтобы не тратить обращение к нейросети впустую.</p>
  <div class="ek-note">Циклы — главная тема <b>урока 6</b>. Сегодня берём необходимый минимум.</div>
</div>"""},

    # 28 · Правка 4 — история
    {"notes": "Правка 4. После запуска покажите: в папке появился history.txt — откройте его прямо в VS Code, там весь разговор с датами. Если группа отстаёт по времени — правки 4 и 5 можно перенести в домашнее задание.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 4 · история диалога</div>
    <h2>Советчик ведёт <span class="acc">дневник</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:14px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Пусть советчик ведёт дневник:
- После каждого ответа дозаписывай в файл history.txt строку вида «[2026-06-12 18:30] Маша: вопрос → ответ нейросети»
- Дату и время бери из datetime.now()
- Файл открывай через with open('history.txt', 'a', encoding='utf-8')
- Если файла нет — он должен создаться сам

Верни весь файл.</div>
  </div>
</div>"""},

    # 29 · Разбор: with open и режимы
    {"notes": "Главная ловушка — режим w стирает файл. Дайте сфотографировать таблицу режимов.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2><span class="acc">with open</span> и режимы файла</h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">from</span> datetime <span class="kw">import</span> datetime

now = datetime.now().strftime(<span class="st">'%Y-%m-%d %H:%M'</span>)
<span class="kw">with</span> open(<span class="st">'history.txt'</span>, <span class="st">'a'</span>, encoding=<span class="st">'utf-8'</span>) <span class="kw">as</span> f:
    f.write(f<span class="st">"[{now}] {name}: {question} → {answer}\n"</span>)</div>
  </div>
  <div class="kv" style="margin-top:12px">
    <div class="kv-row"><div class="k">'r' — читать</div><div class="v">Только смотрим содержимое, менять нельзя.</div></div>
    <div class="kv-row"><div class="k">'w' — переписать</div><div class="v">Создаёт файл заново и <b>стирает всё старое</b>. Осторожно!</div></div>
    <div class="kv-row"><div class="k">'a' — дописать</div><div class="v">Добавляет строки в конец. История копится — нам сюда.</div></div>
  </div>
  <p><span class="code-chip">with</span> закрывает файл сам, а <span class="code-chip">encoding='utf-8'</span> бережёт русские буквы от кракозябр.</p>
</div>"""},
]
