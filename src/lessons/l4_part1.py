# -*- coding: utf-8 -*-
SLIDES = [
    # 1 · ТИТУЛ
    {"cls": "slide--violet", "notes": "Поприветствуйте. Сегодня соберём настоящую игру в браузере. Самый зрелищный урок модуля — каждый получит игру, в которую можно играть и показать друзьям.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">S</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">G</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">E</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">M</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="cover-card">
      <div class="badge">Урок №4</div>
      <div class="card-top"><span class="win-dots"><i></i><i></i><i></i></span><span class="win-close"></span></div>
      <h1>Своя браузерная<br>игра на&nbsp;Canvas</h1>
      <p class="cover-sub">Соберём «Змейку» с управлением, очками и сохранением рекорда. Узнаем, что такое игровой цикл и как рисовать на холсте.</p>
      <div class="cover-chips"><span class="chip">HTML5 Canvas</span><span class="chip chip--green">Игровой цикл</span><span class="chip chip--gray">requestAnimationFrame</span><span class="chip chip--gray">localStorage</span></div>
    </div>
  </div>"""},

    # 2 · ПЛАН
    {"notes": "План. Первые 25 минут — теория и каркас. Дальше — 5 правок.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Agenda · план занятия</div>
    <h2>Как пройдут <span class="acc">60 минут</span></h2>
  </div>
  <div class="agenda">
    <div class="agenda-row"><span class="t">0–5</span><div><div class="tt">Разбор ДЗ</div><div class="dd">Смотрим расширения списка задач.</div></div></div>
    <div class="agenda-row"><span class="t">5–15</span><div><div class="tt">Canvas и игровой цикл</div><div class="dd">Холст в браузере и три фазы игры.</div></div></div>
    <div class="agenda-row"><span class="t">15–25</span><div><div class="tt">Стартовый промпт</div><div class="dd">Каркас: холст, сетка, точка-змея.</div></div></div>
    <div class="agenda-row"><span class="t">25–45</span><div><div class="tt">5 правок через диалог</div><div class="dd">Движение → клавиши → яблоки → проигрыш → рекорд.</div></div></div>
    <div class="agenda-row"><span class="t">45–55</span><div><div class="tt">Косметика и проверка</div><div class="dd">Цвета, мини-вопросы.</div></div></div>
    <div class="agenda-row"><span class="t">55–60</span><div><div class="tt">Турнир в группе</div><div class="dd">Сравниваем рекорды.</div></div></div>
  </div>
</div>"""},

    # 3 · РАЗБОР ДЗ
    {"notes": "Смотрим расширения списка задач. Отметьте, кто как реализовал фильтр.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор ДЗ урока 3</div>
    <h2>Смотрим <span class="acc">расширения списка</span></h2>
  </div>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card">
      <h3>Приоритеты</h3>
      <p>Разбираем, как реализована красная метка для высокого приоритета.</p>
    </div>
    <div class="info-card">
      <h3>Фильтр</h3>
      <p>Сравниваем подходы: скрытие через класс vs перерисовка списка.</p>
    </div>
    <div class="info-card">
      <h3>Счётчик</h3>
      <p>Где обновляется цифра — при каждом изменении или один раз.</p>
    </div>
  </div>
</div>"""},

    # 4 · ИДЕЯ УРОКА: что такое Canvas
    {"notes": "Canvas — «холст», на котором JS рисует. Не элементы, как DOM, а пиксели.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Идея урока</div>
    <h2>Что такое <span class="acc">Canvas</span></h2>
  </div>
  <p>Canvas — это <span class="hl">прямоугольная область на странице</span>, на которой JavaScript может рисовать что угодно: линии, прямоугольники, картинки, текст. Удобно для игр и анимаций.</p>
  <div class="ek-note" style="margin-top:10px">Один тег <span class="code-chip">&lt;canvas&gt;</span> — и у вас есть «лист бумаги», на котором программа рисует кадр за кадром.</div>
</div>"""},

    # 5 · СРАВНЕНИЕ Canvas / DOM
    {"notes": "Объясните разницу. DOM — элементы со стилями. Canvas — пиксели. Для игр Canvas быстрее.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Сравнение</div>
    <h2>Canvas или DOM — <span class="acc">когда что</span></h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>DOM · уроки 1–3</h4>
      <p>Набор элементов: div, button, li. У каждого свой стиль и события.</p>
      <p class="note">Удобно для интерфейсов: формы, списки.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>Canvas · урок 4</h4>
      <p>Нет элементов — только пиксели. Рисуем всё сами кадр за кадром.</p>
      <p class="note">Быстро — идеально для игр и анимаций.</p>
    </div>
  </div>
</div>"""},

    # 6 · КАК РИСОВАТЬ НА CANVAS (код)
    {"notes": "Покажите ctx и базовые методы рисования. Важно, чтобы ученики увидели связь: строка JS превращается в фигуру на холсте.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Основа рисования</div>
    <h2>Как <span class="acc">рисовать</span> на Canvas</h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body"><span class="kw">const</span> canvas = document.getElementById(<span class="st">'game'</span>);
<span class="kw">const</span> ctx = canvas.getContext(<span class="st">'2d'</span>);   <span class="cm">// «кисть» для рисования</span>

<span class="cm">// Прямоугольник: x, y, ширина, высота</span>
ctx.fillStyle = <span class="st">'#10B981'</span>;
ctx.fillRect(100, 100, 20, 20);

ctx.clearRect(0, 0, 400, 400);        <span class="cm">// очистить весь холст</span>

ctx.fillStyle = <span class="st">'white'</span>;           <span class="cm">// текст</span>
ctx.font = <span class="st">'20px Inter'</span>;
ctx.fillText(<span class="st">'Счёт: 5'</span>, 10, 30);</div>
  </div>
  <div class="ek-note"><span class="code-chip">ctx</span> (context) — это «кисть». Все рисунки идут через неё.</div>
</div>"""},

    # 7 · СИСТЕМА КООРДИНАТ
    {"notes": "Важно: начало координат в левом ВЕРХНЕМ углу. Y растёт вниз. Это частый источник путаницы.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Система координат</div>
    <h2>Где у Canvas точка <span class="acc">(0, 0)</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div>
      <p>Точка <span class="code-chip">(0, 0)</span> — в <b>левом верхнем углу</b>.</p>
      <ul class="clean">
        <li><b>X</b> растёт вправо →</li>
        <li><b>Y</b> растёт вниз ↓ — не вверх, как в математике!</li>
      </ul>
      <p style="margin-top:8px">Поэтому «движение вниз» — это увеличение Y.</p>
    </div>
    <div class="code-win">
      <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ХОЛСТ</span></div>
      <div class="code-body">(0,0) ───────────→ X
  │  ┌──────────────┐
  │  │              │
  │  │   холст      │
  ▼  │   400×400    │
  Y  └──────────────┘
            (400,400)</div>
    </div>
  </div>
</div>"""},

    # 8 · ИГРОВОЙ ЦИКЛ (3 фазы)
    {"notes": "Сердце любой игры. 3 фазы повторяются десятки раз в секунду.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Сердце любой игры</div>
    <h2>Что такое <span class="acc">игровой цикл</span></h2>
  </div>
  <p>Игра — это цикл, который повторяется много раз в секунду. На каждом «тике» — три действия:</p>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card">
      <h3>1 · Input</h3>
      <p>Что нажал игрок? Куда движется змейка?</p>
    </div>
    <div class="info-card">
      <h3>2 · Update</h3>
      <p>Двигаем объекты, проверяем столкновения, обновляем счёт.</p>
    </div>
    <div class="info-card">
      <h3>3 · Render</h3>
      <p>Стираем холст и рисуем заново: змею, яблоко, счёт.</p>
    </div>
  </div>
</div>"""},

    # 9 · ФАЗА 1 · INPUT (код)
    {"notes": "Детально про input. Игра не реагирует мгновенно — она запоминает намерение и применяет на следующем тике.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Фаза 1 · Input</div>
    <h2>Как игра <span class="acc">слышит игрока</span></h2>
  </div>
  <p>Игра <b>не двигает змейку сразу</b> при нажатии. Она запоминает <span class="hl">направление</span>, а двигает на следующем тике update.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body"><span class="kw">let</span> dir = { x: 1, y: 0 };   <span class="cm">// едем вправо</span>

document.addEventListener(<span class="st">'keydown'</span>, (e) =&gt; {
  <span class="kw">if</span> (e.key === <span class="st">'ArrowUp'</span>)    dir = { x: 0, y: -1 };
  <span class="kw">if</span> (e.key === <span class="st">'ArrowDown'</span>)  dir = { x: 0, y:  1 };
  <span class="kw">if</span> (e.key === <span class="st">'ArrowLeft'</span>)  dir = { x: -1, y: 0 };
  <span class="kw">if</span> (e.key === <span class="st">'ArrowRight'</span>) dir = { x: 1, y:  0 };
});</div>
  </div>
  <div class="ek-note">Input только <span class="hl">запоминает</span> намерение. Двигает — фаза Update.</div>
</div>"""},

    # 10 · ФАЗА 2 · UPDATE
    {"notes": "Update — вся логика. Двигаем голову, проверяем яблоко и столкновения.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Фаза 2 · Update</div>
    <h2>Где вся <span class="acc">логика игры</span></h2>
  </div>
  <p>В update происходит главное:</p>
  <ul class="clean" style="margin-top:8px">
    <li>Двигаем голову змейки на одну клетку в сторону <span class="code-chip">dir</span></li>
    <li>Проверяем: голова попала на яблоко? → счёт +1, змейка растёт</li>
    <li>Проверяем: голова вышла за стену или врезалась в себя? → game over</li>
    <li>Хвост удаляется, если яблоко не съедено — змейка «ползёт»</li>
  </ul>
  <div class="ek-note ek-note--red" style="margin-top:12px">Update <b>не рисует</b> ничего. Он только считает новое состояние. Рисование — отдельная фаза.</div>
</div>"""},
]
