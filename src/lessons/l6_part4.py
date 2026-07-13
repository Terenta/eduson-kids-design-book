# -*- coding: utf-8 -*-
# Урок 6 «Циклы, функции и коллекции» · часть 4 (слайды 30–38)
# Правка 5 (концовки и цвет) → разбор цвета и конца → 2 квиза → отладка → привычки → чек-лист → ДЗ → финал.
SLIDES = [
    # 30 · ПРАВКА 5 · КОНЦОВКИ И ЦВЕТ
    {"notes": "Финальная правка собирает игру воедино: появляется проигрыш и атмосфера цвета. Дождитесь, пока у всех заработает, потом идём к разбору. Это самый зрелищный момент — игра выглядит как настоящая.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 5 · победа, гибель и атмосфера</div>
    <h2>Концовки и <span class="acc">цвет</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:6px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Добавь в игру концовки и цвет:
- Если state["hp"] стал 0 или меньше — напечатай красным
  «💀 Ты пал в подземелье. Игра окончена» и выйди из цикла
- Если игрок ввёл «выход» — попрощайся

Раскрась вывод ANSI-кодами, без сторонних библиотек:
- заголовок — фиолетовым
- сцены мастера — обычным цветом
- строку HP — красным
- найденные предметы — зелёным

Заведи в начале файла константы вроде RED = '\033[31m'
и RESET = '\033[0m'. Верни весь файл.</div>
  </div>
</div>"""},

    # 31 · РАЗБОР · ЦВЕТ И КОНЕЦ ИГРЫ
    {"notes": "Разбор двух вещей сразу: как красить терминал и как заканчивать игру. Подчеркните: break нужен и для гибели героя, и для слова «выход». Если цвета не появились — пусть запускают во встроенном терминале VS Code.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Цвет и <span class="acc">конец игры</span></h2>
  </div>
  <p>Терминал понимает <b>специальные последовательности</b>: <span class="code-chip">\033[..m</span> переключает цвет, <span class="code-chip">\033[0m</span> возвращает обычный. А проверка HP решает, когда игра окончена:</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">VIOLET = <span class="st">'\033[35m'</span>   <span class="cm"># заголовок</span>
RED    = <span class="st">'\033[31m'</span>   <span class="cm"># урон и гибель</span>
GREEN  = <span class="st">'\033[92m'</span>   <span class="cm"># находки</span>
RESET  = <span class="st">'\033[0m'</span>    <span class="cm"># вернуть обычный вид</span>

<span class="kw">if</span> state[<span class="st">"hp"</span>] &lt;= 0:
    <span class="kw">print</span>(<span class="st">f"{RED}💀 Ты пал в подземелье.{RESET}"</span>)
    <span class="kw">break</span>          <span class="cm"># выходим из игрового цикла</span></div>
  </div>
  <div class="ek-note ek-note--red">Цвета видны во встроенном терминале VS Code. В старых системных консолях они могут не появиться — это <b>не ошибка вашего кода</b>.</div>
</div>"""},

    # 32 · КВИЗ 1 · RETURN
    {"notes": "Вопрос про return — самая частая ошибка с функциями. Дайте 10–15 секунд, потом раскройте ответ. Свяжите с ask_master: без return сцена не дойдёт до main.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 1</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 1</span>
    <p class="q-text">Тимур написал функцию <span class="code-chip">def ask_master(messages):</span>, внутри посчитал ответ в переменную <span class="code-chip">scene</span>, но забыл строку <span class="code-chip">return scene</span>. В main он пишет <span class="code-chip">text = ask_master(messages)</span> — и в <span class="code-chip">text</span> оказывается <span class="code-chip">None</span> (пусто). Почему?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>Без <b>return</b> функция ничего не отдаёт наружу, а переменная <span class="code-chip">scene</span> живёт только внутри функции и исчезает, когда функция заканчивается.</p>
        <p>Нужно добавить <b>return scene</b> — тогда результат вернётся в <span class="code-chip">text</span>, и сцену будет видно.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 33 · КВИЗ 2 · СОСТОЯНИЕ ДО ЦИКЛА
    {"notes": "Вопрос про состояние и цикл. Очень частая ошибка новичка — создавать словарь внутри цикла. Свяжите с привычкой: состояние создаём один раз до цикла.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 2</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 2</span>
    <p class="q-text">Лиза хочет, чтобы за каждый ход HP падал на 10: она написала <span class="code-chip">state["hp"] -= 10</span>. Но HP в игре всегда остаётся 100. Оказалось, строку <span class="code-chip">state = {"hp": 100}</span> она поставила <b>внутри</b> цикла <span class="code-chip">while</span>. Где ошибка?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>Словарь <span class="code-chip">state</span> создаётся заново на каждом ходу, поэтому память героя каждый раз <b>обнуляется</b> до 100.</p>
        <p>Создавать <span class="code-chip">state</span> нужно <b>один раз до цикла</b>, а внутри цикла — только менять его значения.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 34 · ОТЛАДКА
    {"notes": "Научите читать traceback снизу вверх — пригодится на всех уроках Python. Напомните привычку: непонятную ошибку целиком копируем в DeepSeek. Три поломки справа — самые частые именно в этой игре.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Отладка</div>
    <h2>Читаем <span class="acc">ошибки</span> игры</h2>
  </div>
  <div class="grid-2">
    <div class="col">
      <p><span class="hl">Traceback — снизу вверх.</span> Последняя строка — <b>что</b> случилось (KeyError, TypeError…), строкой выше — <b>где</b>.</p>
      <div class="term" style="margin-top:14px">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
        <div class="term-body"><span class="dim">Traceback (most recent call last):
  File "game.py", line 21, in main
    print(state["hp"])</span>
<span class="usr">KeyError: 'hp'</span></div>
      </div>
    </div>
    <div class="info-card">
      <h3>Частые поломки</h3>
      <ul class="clean">
        <li><b>KeyError 'hp'</b> — опечатка в ключе словаря: проверьте кавычки и имя ключа</li>
        <li><b>В переменной None</b> — забыли <span class="code-chip">return</span> в функции</li>
        <li><b>Мастер отвечает невпопад</b> — проверьте, что <span class="code-chip">messages</span> растёт и отправляется целиком</li>
      </ul>
      <p style="margin-top:12px;font-size:14px;color:var(--ek-gray)">Непонятную ошибку целиком копируем в чат DeepSeek — привычка из прошлых уроков.</p>
    </div>
  </div>
</div>"""},

    # 35 · ПРИВЫЧКИ
    {"notes": "5 привычек урока. Дайте сфотографировать слайд. Особо подчеркните первые две: функции-кубики и return — это главное, что уносят с урока.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запомните</div>
    <h2>Привычки <span class="acc">программиста</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">01 · Функции — кубики</div><div class="v">Большую задачу делим на маленькие <span class="code-chip">def</span> с понятными именами.</div></div>
    <div class="kv-row"><div class="k">02 · return отдаёт результат</div><div class="v">Без <span class="code-chip">return</span> функция молчит и возвращает <span class="code-chip">None</span>.</div></div>
    <div class="kv-row"><div class="k">03 · Состояние — до цикла</div><div class="v">Словарь <span class="code-chip">state</span> создаём один раз перед <span class="code-chip">while</span>, внутри только меняем.</div></div>
    <div class="kv-row"><div class="k">04 · Список и словарь</div><div class="v"><span class="code-chip">list</span> — упорядоченный набор, <span class="code-chip">dict</span> — пары ключ-значение.</div></div>
    <div class="kv-row"><div class="k">05 · Промпт — характер программы</div><div class="v">Системная роль решает, какой мир построит мастер.</div></div>
  </div>
</div>"""},

    # 36 · ЧЕК-ЛИСТ
    {"notes": "Чек-лист завершения игры. Кто отметил всё — пусть даст соседу сыграть. У соседа получится другое приключение — это и есть магия AI-мастера.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Чек-лист</div>
    <h2>Готовность <span class="acc">к 55-й минуте</span></h2>
  </div>
  <div class="grid-2">
    <div class="info-card">
      <h3 style="color:var(--ek-green-deep)">Готово</h3>
      <ul class="clean">
        <li><span class="code-chip">game.py</span> запускается командой <span class="code-chip">python game.py</span></li>
        <li>Нейросеть генерирует стартовую сцену подземелья</li>
        <li>Код разложен на функции <span class="code-chip">ask_master</span>, <span class="code-chip">show</span>, <span class="code-chip">main</span></li>
      </ul>
    </div>
    <div class="info-card">
      <h3 style="color:var(--ek-violet-deep)">Работает</h3>
      <ul class="clean">
        <li>Игра идёт по кругу — выборы рождают новые сцены</li>
        <li>У героя есть HP и инвентарь через словарь и список</li>
        <li>Есть концовка — гибель или выход — и цветной вывод</li>
      </ul>
    </div>
  </div>
  <div class="ek-note ek-note--green">Всё отмечено? Дайте соседу сыграть в вашу игру — у него получится своё приключение.</div>
</div>"""},

    # 37 · ДЗ
    {"notes": "ДЗ — прокачать игру, примерно 30 минут. Каждое улучшение — отдельный диалог с DeepSeek, не всё сразу. Напомните про ключ на скриншотах.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Домашнее задание · около 30 минут</div>
    <h2>Прокачайте свою <span class="acc">игру</span></h2>
  </div>
  <p>Три улучшения — каждое через отдельный диалог с DeepSeek:</p>
  <div class="grid-3">
    <div class="info-card">
      <h3>Свой жанр</h3>
      <p>Поменяйте системную роль мастера — космос, киберпанк или сказка — и мир игры полностью изменится.</p>
    </div>
    <div class="info-card">
      <h3>Сундук с сокровищами</h3>
      <p>Добавьте функцию <span class="code-chip">open_chest()</span>: через <span class="code-chip">random.choice</span> она достаёт случайный предмет из списка и кладёт его в инвентарь.</p>
    </div>
    <div class="info-card">
      <h3>Карта приключения</h3>
      <p>Сохраняйте каждую сцену в файл <span class="code-chip">adventure.txt</span> — как историю советчика на уроке 5, режим <span class="code-chip">'a'</span>.</p>
    </div>
  </div>
  <div class="ek-note ek-note--red">Пришлите скриншот игры — <b>ключ скройте!</b> Ваш самый удачный промпт — отдельным сообщением.</div>
</div>"""},

    # 38 · ФИНАЛ
    {"cls": "slide--green",
     "notes": "Закройте урок. Сегодня вы написали движок игры и доверили нейросети роль гейм-мастера. На уроке 7 — файлы и JSON, личный дневник с AI-тегами.",
     "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">G</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">A</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">M</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">E</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="bubble">
      <h1>До встречи<br>на уроке 7!</h1>
      <p>Сегодня вы собрали движок игры — функции, циклы и словари — и доверили нейросети роль гейм-мастера. На уроке 7 научим программу по-настоящему запоминать данные: файлы и формат JSON. Соберём личный дневник, которому AI сам подбирает теги.</p>
    </div>
  </div>"""},
]
