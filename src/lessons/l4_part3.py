# -*- coding: utf-8 -*-
SLIDES = [
    # 20 · TROUBLESHOOTING ЗАПУСКА КАРКАСА
    {"notes": "Troubleshooting запуска каркаса игры.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Если точка не появилась</div>
    <h2>Типичные ситуации <span class="acc">запуска</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">Холст белый / пустой</div><div class="v">Откройте F12 → Console. Ошибка про <span class="code-chip">getContext</span> или <span class="code-chip">canvas</span> — скопируйте её в DeepSeek.</div></div>
    <div class="kv-row"><div class="k">Холст крошечный</div><div class="v">В теге <span class="code-chip">&lt;canvas&gt;</span> нет width/height, либо размер задан в CSS. Размер холста задаётся <b>атрибутами тега</b>.</div></div>
    <div class="kv-row"><div class="k">Страница белая</div><div class="v">Файл не сохранён. Нажмите <span class="code-chip">Ctrl+S</span> и проверьте, что код вставлен.</div></div>
  </div>
</div>"""},

    # 21 · ПРАВКА 1 · ДВИЖЕНИЕ (промпт)
    {"notes": "Учим змейку двигаться сама. Пока без управления — посмотреть, как ползёт.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 1 · движение</div>
    <h2>Змейка <span class="acc">двигается</span> сама</h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Доработай script.js:
- Змейка — теперь массив сегментов (каждый = клетка с x, y)
- Начнём с 3 сегментов в центре
- Направление движения — переменная <span class="hl">dir</span> {x, y}, по умолчанию {x: 1, y: 0} (вправо)
- В update: <span class="hl">двигай голову на одну клетку в направлении dir</span>, остальные сегменты следуют (последний удаляется, новый добавляется в начало)
- Скорость — <span class="hl">4 кадра в секунду</span> (счётчик внутри requestAnimationFrame)

Не трогай стили и HTML. Верни обновлённый script.js.</div>
  </div>
</div>"""},

    # 22 · РАЗБОР: КАК ПОЛЗЁТ ЗМЕЙКА
    {"notes": "Объясните механику: новая голова вперёд, хвост убирается. Так змейка «ползёт» не двигая каждый сегмент.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Как именно <span class="acc">ползёт</span> змейка</h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body"><span class="kw">function</span> update() {
  <span class="kw">const</span> head = snake[0];
  <span class="kw">const</span> newHead = {            <span class="cm">// новая голова на клетку вперёд</span>
    x: head.x + dir.x,
    y: head.y + dir.y
  };
  snake.unshift(newHead);      <span class="cm">// добавили голову в начало</span>
  snake.pop();                 <span class="cm">// удалили хвост в конце</span>
}</div>
  </div>
  <div class="ek-note ek-note--green" style="margin-top:12px">Ключевой приём: мы <b>не двигаем</b> каждый сегмент. Добавляем голову и убираем хвост — на экране это выглядит как ползущая змея.</div>
</div>"""},

    # 23 · ПРАВКА 2 · УПРАВЛЕНИЕ (промпт)
    {"notes": "Управление с клавиатуры. Запрещаем разворот на 180°.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 2 · управление</div>
    <h2>Управление <span class="acc">стрелками</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Добавь обработку клавиатуры:
- При нажатии стрелок (<span class="hl">ArrowUp, ArrowDown, ArrowLeft, ArrowRight</span>) — меняй направление dir
- Запрети разворот на 180°: если змейка двигается вправо, нажатие «влево» <span class="hl">не должно сработать</span>
- Используй <span class="hl">document.addEventListener('keydown', …)</span>
- Добавь <span class="hl">e.preventDefault()</span>, чтобы стрелки не прокручивали страницу

Изменения только в script.js. Верни целиком обновлённый script.js.</div>
  </div>
</div>"""},

    # 24 · ПОЧЕМУ НЕЛЬЗЯ РАЗВОРОТ НА 180° (vs + код)
    {"notes": "Объясните, почему разворот на 180 убивает игру: голова мгновенно врезается в шею.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Важная тонкость</div>
    <h2>Почему нельзя развернуться на <span class="acc">180°</span></h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>✕ Без запрета</h4>
      <p>Змейка едет вправо. Игрок жмёт «влево». Голова мгновенно врезается в свою же шею — мгновенный проигрыш на ровном месте.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>✓ С запретом</h4>
      <p>Проверяем: новое направление не противоположно текущему. Если противоположно — игнорируем нажатие.</p>
    </div>
  </div>
  <div class="code-win" style="margin-top:12px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body"><span class="cm">// нельзя влево, если едем вправо</span>
<span class="kw">if</span> (newDir.x === -dir.x && newDir.y === -dir.y) <span class="kw">return</span>;</div>
  </div>
</div>"""},

    # 25 · ЗАЧЕМ preventDefault
    {"notes": "Зачем preventDefault. Без него стрелки скроллят страницу — играть невозможно.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Полезное знание</div>
    <h2>Зачем <span class="acc">e.preventDefault()</span></h2>
  </div>
  <p>У стрелок есть <span class="hl">стандартное поведение браузера</span> — прокрутка страницы. В игре это мешает: нажал «вниз» — страница уехала.</p>
  <div class="code-win" style="margin-top:10px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body">document.addEventListener(<span class="st">'keydown'</span>, (e) =&gt; {
  e.preventDefault();          <span class="cm">// отменяем прокрутку страницы</span>
  <span class="cm">// ... меняем направление</span>
});</div>
  </div>
  <div class="ek-note" style="margin-top:12px"><span class="code-chip">preventDefault()</span> говорит браузеру: «не делай своё стандартное действие, я обработаю сам».</div>
</div>"""},

    # 26 · ПРАВКА 3 · ЯБЛОКИ (промпт)
    {"notes": "Появляется красная клетка. Съели — счёт +1, новое яблоко.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 3 · яблоки</div>
    <h2>Яблоки и <span class="acc">счёт</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Добавь яблоко:
- Случайная клетка на сетке (не на змейке)
- Цвет красный <span class="hl">#EF4444</span>
- Когда голова змейки попадает на яблоко: <span class="hl">счёт +1</span>, длина змейки <span class="hl">+1 сегмент</span>, яблоко появляется в новом случайном месте
- Обнови табло «Счёт: N»

Изменения в script.js и (если нужно) в index.html (для табло). Верни изменённые файлы.</div>
  </div>
</div>"""},

    # 27 · РАЗБОР: СЛУЧАЙНАЯ ПОЗИЦИЯ ЯБЛОКА
    {"notes": "Как генерится случайная клетка и почему её надо проверять на пересечение со змейкой.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Случайная позиция <span class="acc">яблока</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body"><span class="kw">function</span> randomApple() {
  <span class="kw">let</span> pos;
  <span class="kw">do</span> {
    pos = {
      x: Math.floor(Math.random() * 20),  <span class="cm">// 0..19</span>
      y: Math.floor(Math.random() * 20),
    };
  } <span class="kw">while</span> (snake.some(s =&gt; s.x === pos.x && s.y === pos.y));
  <span class="kw">return</span> pos;          <span class="cm">// клетка точно НЕ на змейке</span>
}</div>
  </div>
  <div class="ek-note ek-note--red" style="margin-top:12px"><span class="code-chip">do...while</span> повторяет генерацию, пока яблоко не окажется на свободной клетке. Иначе яблоко могло бы появиться внутри змейки.</div>
</div>"""},

    # 28 · ПРАВКА 4 · ПРОИГРЫШ (промпт)
    {"notes": "Столкновение со стеной или с собой = game over.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 4 · проигрыш</div>
    <h2>Game Over при <span class="acc">столкновении</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Добавь логику проигрыша:
- Если голова змейки выходит <span class="hl">за границы холста</span> — game over
- Если голова попадает в любой <span class="hl">сегмент собственного тела</span> — game over
- При game over: <span class="hl">останови игру</span>, нарисуй полупрозрачный чёрный прямоугольник на весь холст, в центре крупный белый текст «GAME OVER» и снизу «Нажмите Пробел, чтобы начать заново»
- При нажатии Пробела — игра начинается с нуля

Изменения в script.js. Верни обновлённый script.js.</div>
  </div>
</div>"""},

    # 29 · РАЗБОР: КАК ПРОВЕРЯЮТСЯ СТОЛКНОВЕНИЯ
    {"notes": "Детально: два вида столкновений — со стеной и с собой.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Как проверяются <span class="acc">столкновения</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body"><span class="kw">const</span> h = snake[0];                    <span class="cm">// голова</span>

<span class="cm">// 1. Со стеной — вышли за сетку 0..19</span>
<span class="kw">if</span> (h.x &lt; 0 || h.x &gt; 19 || h.y &lt; 0 || h.y &gt; 19) {
  gameOver();
}

<span class="cm">// 2. С собой — голова на клетке тела</span>
<span class="kw">for</span> (<span class="kw">let</span> i = 1; i &lt; snake.length; i++) {
  <span class="kw">if</span> (h.x === snake[i].x && h.y === snake[i].y) {
    gameOver();
  }
}</div>
  </div>
  <div class="ek-note" style="margin-top:12px">Проверку начинаем с <span class="code-chip">i = 1</span> — голова сама с собой не сталкивается.</div>
</div>"""},
]
