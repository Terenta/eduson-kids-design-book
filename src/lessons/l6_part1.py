# -*- coding: utf-8 -*-
SLIDES = [
    # 1 · ТИТУЛ
    {"cls": "slide--violet", "notes": "Поприветствуйте. Сегодня соберём настоящую ролевую игру, где сюжет придумывает нейросеть. Новые инструменты — циклы, функции и словари — мы возьмём ровно в том объёме, который нужен для игры. К концу урока у каждого — играбельное приключение в терминале.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">R</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">P</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">G</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">AI</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="cover-card">
      <div class="badge">Урок №6</div>
      <div class="card-top"><span class="win-dots"><i></i><i></i><i></i></span><span class="win-close"></span></div>
      <h1>Игра-приключение<br>с&nbsp;сюжетом от&nbsp;AI</h1>
      <p class="cover-sub">Соберём текстовую ролевую игру, где гейм-мастером работает нейросеть: она придумывает подземелье и сюжет, а вы делаете выборы. Циклы, функции и словари — внутри.</p>
      <div class="cover-chips"><span class="chip">Python</span><span class="chip chip--green">DeepSeek API</span><span class="chip chip--gray">циклы и функции</span><span class="chip chip--gray">list / dict</span></div>
    </div>
  </div>"""},

    # 2 · ПЛАН
    {"notes": "План. Теории — минимум: уже на 12-й минуте каждый запускает функцию-разминку, к 30-й — каркас игры, где первую сцену подземелья генерирует нейросеть. Дальше — 5 правок, как на прошлых уроках.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Agenda · план занятия</div>
    <h2>Как пройдут <span class="acc">60 минут</span></h2>
  </div>
  <div class="agenda">
    <div class="agenda-row"><span class="t">0–5</span><div><div class="tt">Разбор ДЗ</div><div class="dd">Смотрим прокачанные советчики: характеры, память, ASCII-лого.</div></div></div>
    <div class="agenda-row"><span class="t">5–12</span><div><div class="tt">Функции и циклы</div><div class="dd">Минимум теории — только чтобы собрать игру.</div></div></div>
    <div class="agenda-row"><span class="t">12–20</span><div><div class="tt">Промпт-разминка</div><div class="dd">Маленькая функция: промпт → код → запуск.</div></div></div>
    <div class="agenda-row"><span class="t">20–32</span><div><div class="tt">Каркас игры</div><div class="dd">Нейросеть генерирует первую сцену подземелья.</div></div></div>
    <div class="agenda-row"><span class="t">32–48</span><div><div class="tt">5 правок через диалог</div><div class="dd">Игровой цикл → функции → бросок кубика → HP и инвентарь → концовки и цвет.</div></div></div>
    <div class="agenda-row"><span class="t">48–55</span><div><div class="tt">Мини-вопросы и отладка</div><div class="dd">Читаем ошибки, проверяем понимание.</div></div></div>
    <div class="agenda-row"><span class="t">55–60</span><div><div class="tt">Демо в группе</div><div class="dd">Каждый играет в своё приключение.</div></div></div>
  </div>
</div>"""},

    # 3 · РАЗБОР ДЗ
    {"notes": "Откройте 2-3 прокачанных советчика. Разбирайте диалог с нейросетью, а не только результат. Главное — память через список messages: это первое знакомство со списками, сегодня они станут главным инструментом игры.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор ДЗ урока 5</div>
    <h2>Смотрим прокачанные <span class="acc">советчики</span></h2>
  </div>
  <p>Открываем 2–3 присланных советчика и разбираем именно <span class="hl">диалог с нейросетью</span>: четвёртый характер, память разговора, ASCII-логотип.</p>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card">
      <h3>Что сработало</h3>
      <p>Память через список <span class="code-chip">messages</span> — первое знакомство со списками. Сегодня списки и словари станут главным инструментом.</p>
    </div>
    <div class="info-card">
      <h3>Что переделывали</h3>
      <p>Где забыли отправлять <span class="hl">весь</span> список <span class="code-chip">messages</span> — советчик не помнил прошлые реплики.</p>
    </div>
    <div class="info-card">
      <h3>Вывод</h3>
      <p>Точная формулировка плюс проверка после каждой правки. Сегодня тот же подход.</p>
    </div>
  </div>
</div>"""},

    # 4 · ИДЕЯ УРОКА
    {"notes": "Главная мысль: у DeepSeek новая роль — гейм-мастер. Раньше он писал код и давал советы, теперь ведёт целую игру: придумывает локации, врагов, повороты сюжета. Мы пишем движок, нейросеть наполняет его сюжетом.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Идея урока</div>
    <h2>Нейросеть становится <span class="acc">гейм-мастером</span></h2>
  </div>
  <p>На уроке 5 нейросеть отвечала на вопросы. Сегодня она <span class="hl">ведёт целую игру</span> — придумывает подземелье, врагов и повороты сюжета, и каждый раз заново.</p>
  <div class="ek-note" style="margin-top:6px">Вы пишете <b>движок</b> игры: циклы крутят ход за ходом, функции делят программу на кусочки, словарь помнит здоровье и инвентарь. А нейросеть наполняет движок <b>живым сюжетом</b>.</div>
  <p>Идея урока 6: большую программу <b>делим на функции</b>, <b>повторяем циклами</b>, <b>помним через словари</b>.</p>
</div>"""},

    # 5 · ЧТО ТАКОЕ ФУНКЦИЯ
    {"notes": "Функция — это команда, которую программист придумал сам. Объясните на greet: дали имя кусочку кода и зовём по имени сколько угодно раз. Параметры в скобках, return отдаёт результат наружу.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Новый инструмент</div>
    <h2>Что такое <span class="acc">функция</span></h2>
  </div>
  <p>Функция — <span class="hl">команда, которую вы придумали сами</span>: дали имя кусочку кода и зовёте его по имени, сколько нужно.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">def</span> greet(name):          <span class="cm"># создаём функцию greet</span>
    print(f<span class="st">"Привет, {name}!"</span>)

greet(<span class="st">"Артём"</span>)            <span class="cm"># зовём её по имени</span></div>
  </div>
  <div class="kv" style="margin-top:12px">
    <div class="kv-row"><div class="k">def</div><div class="v">Создаёт функцию и даёт ей имя.</div></div>
    <div class="kv-row"><div class="k">вызов</div><div class="v"><span class="code-chip">greet("Артём")</span> — запускает код функции.</div></div>
    <div class="kv-row"><div class="k">return</div><div class="v">Возвращает результат наружу, чтобы сохранить его в переменную.</div></div>
  </div>
</div>"""},

    # 6 · ЗАЧЕМ ДЕЛИТЬ НА ФУНКЦИИ
    {"notes": "Сравнение без функций и с функциями. Главная мысль — декомпозиция: большую задачу делим на маленькие понятные кусочки. Так устроены все большие программы, включая нашу игру.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Зачем это нужно</div>
    <h2>Зачем делить программу на <span class="acc">функции</span></h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>Без функций</h4>
      <p>Одна гигантская простыня кода. Один и тот же кусок копируешь снова и снова, ошибку искать невозможно.</p>
      <p class="note">Так писать игру нереально.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>С функциями</h4>
  <p>Программа из понятных блоков: <span class="code-chip">ask_master()</span>, <span class="code-chip">show()</span>, <span class="code-chip">main()</span>. Каждый кусок можно проверить отдельно и переиспользовать.</p>
      <p class="note">Это декомпозиция — большую задачу делим на маленькие.</p>
    </div>
  </div>
  <p>Именно так устроены <span class="hl">все большие программы</span> — от игр до нейросетей.</p>
</div>"""},

    # 7 · ЧТО ТАКОЕ ЦИКЛ
    {"notes": "Цикл повторяет блок кода. for — повторить N раз или пройти по списку, while — пока условие истинно. Подведите к мысли: игра — это while-цикл, который крутится ход за ходом, пока герой жив.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Новый инструмент</div>
    <h2>Что такое <span class="acc">цикл</span></h2>
  </div>
  <p>Цикл <span class="hl">повторяет блок кода</span>, чтобы не писать одно и то же руками.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">for</span> i <span class="kw">in</span> range(3):        <span class="cm"># повторить ровно 3 раза</span>
    print(<span class="st">"Шаг"</span>, i)

<span class="kw">while</span> hp &gt; 0:             <span class="cm"># повторять, пока герой жив</span>
    hp = hp - 10           <span class="cm"># каждый ход герой теряет силы</span></div>
  </div>
  <div class="ek-note" style="margin-top:12px"><span class="code-chip">for</span> — повторить N раз или пройти по списку. <span class="code-chip">while</span> — повторять, пока условие истинно. <b>Игра — это цикл</b>: ход за ходом, пока герой не победит или не падёт.</div>
</div>"""},

    # 8 · ПРОМПТ #1 РАЗМИНКА
    {"notes": "Никакой долгой подготовки: сразу просим у DeepSeek маленькую функцию и запускаем. Промпт с ролью и форматом — техники урока 2 работают и здесь. Дети копируют промпт целиком.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #1 · разминка</div>
    <h2>Кубик за <span class="acc">две минуты</span></h2>
  </div>
  <p>Не будем долго готовиться — попросим у DeepSeek маленькую функцию и сразу запустим её в терминале.</p>
  <div class="prompt-card" style="margin-top:14px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — опытный Python-разработчик и наставник школьника.
Напиши маленький скрипт warmup.py: функция roll_dice() бросает
игральный кубик — случайное число от 1 до 6 — и возвращает его.
Вызови её три раза в цикле for и каждый раз печатай результат.
Только стандартная библиотека Python.
Прокомментируй код для новичка и ответь одним блоком кода.</div>
  </div>
</div>"""},

    # 9 · ЗАПУСК ПЕРВОЙ ФУНКЦИИ
    {"notes": "Фундамент урока: дождитесь, пока у всех три броска появятся в терминале. На живом коде показываем сразу три кита игры: функция, цикл, случайность. Не идите дальше, пока не запустилось у каждого.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск и разбор</div>
    <h2>Запускаем первую <span class="acc">функцию</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div>
      <ol class="steps steps--tight">
        <li>В папке <span class="code-chip">vibe-coding</span> создайте папку <span class="code-chip">lesson-06</span></li>
        <li>Создайте <span class="code-chip">warmup.py</span> и вставьте код из ответа</li>
        <li>Сохраните: <span class="code-chip">Ctrl+S</span></li>
        <li>Выполните <span class="code-chip">python warmup.py</span></li>
      </ol>
      <div class="ek-note ek-note--green" style="margin-top:12px">Видим три броска кубика? Функция, цикл и случайность за пять минут — фундамент игры готов.</div>
    </div>
    <div class="kv">
      <div class="kv-row"><div class="k">def roll_dice()</div><div class="v">Наша первая функция.</div></div>
      <div class="kv-row"><div class="k">for _ in range(3)</div><div class="v">Повторили бросок трижды.</div></div>
      <div class="kv-row"><div class="k">random.randint(1, 6)</div><div class="v">Случайное число — кубик.</div></div>
    </div>
  </div>
</div>"""},

    # 10 · TROUBLESHOOTING
    {"notes": "Шпаргалка по трём типичным проблемам запуска. Почините у всех — эти же команды и папка нужны дальше для самой игры.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Типичные ситуации запуска</div>
    <h2>Если <span class="acc">warmup.py</span> не запустился</h2>
  </div>
  <div class="grid-3" style="margin-top:8px">
    <div class="ek-note ek-note--red">
      <h3>python is not recognized</h3>
      <p>Python не добавлен в PATH. Переустановите с галочкой <b>Add to PATH</b> — или зовите преподавателя.</p>
    </div>
    <div class="ek-note ek-note--red">
      <h3>can't open file</h3>
      <p>Терминал смотрит в другую папку. Откройте папку <span class="code-chip">lesson-06</span> в VS Code и терминал заново.</p>
    </div>
    <div class="ek-note ek-note--red">
      <h3>IndentationError</h3>
      <p>Сбит отступ. Тело функции и цикла сдвинуто на 4 пробела — не ломайте отступы при копировании.</p>
    </div>
  </div>
</div>"""},
]
