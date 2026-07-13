# -*- coding: utf-8 -*-
SLIDES = [
    # 11 · ФАЗА 3 · RENDER
    {"notes": "Render — только рисование. Сначала стереть весь холст, потом нарисовать заново.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Фаза 3 · Render</div>
    <h2>Стереть и <span class="acc">нарисовать заново</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body"><span class="kw">function</span> render() {
  <span class="cm">// 1. Стираем весь холст</span>
  ctx.clearRect(0, 0, 400, 400);

  <span class="cm">// 2. Рисуем каждый сегмент змейки</span>
  ctx.fillStyle = <span class="st">'#10B981'</span>;
  <span class="kw">for</span> (<span class="kw">const</span> seg <span class="kw">of</span> snake) {
    ctx.fillRect(seg.x * 20, seg.y * 20, 19, 19);
  }

  <span class="cm">// 3. Рисуем яблоко</span>
  ctx.fillStyle = <span class="st">'#EF4444'</span>;
  ctx.fillRect(apple.x * 20, apple.y * 20, 19, 19);
}</div>
  </div>
  <div class="ek-note">Главное правило: <b>сначала <span class="code-chip">clearRect</span></b>, иначе старые кадры останутся «следами».</div>
</div>"""},

    # 12 · requestAnimationFrame
    {"notes": "Что запускает цикл. Браузер сам подбирает частоту ~60 кадров/сек.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Двигатель цикла</div>
    <h2>Что такое <span class="acc">requestAnimationFrame</span></h2>
  </div>
  <p>Это функция браузера, которая вызывает ваш код <span class="hl">перед каждым кадром экрана</span> — обычно 60 раз в секунду.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body"><span class="kw">function</span> loop() {
  update();                      <span class="cm">// посчитать состояние</span>
  render();                      <span class="cm">// нарисовать</span>
  requestAnimationFrame(loop);   <span class="cm">// запросить следующий кадр</span>
}
loop();                          <span class="cm">// запускаем</span></div>
  </div>
  <div class="ek-note">В отличие от <span class="code-chip">setInterval</span>, она сама подстраивается под устройство: на слабом компьютере кадры реже, но игра остаётся плавной.</div>
</div>"""},

    # 13 · Змейка — массив клеток
    {"notes": "Объясните: змейка хранится как массив координат. Движение = добавить голову, убрать хвост.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Структура данных</div>
    <h2>Змейка — это <span class="acc">массив клеток</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body"><span class="cm">// Каждый сегмент — клетка с координатами</span>
<span class="kw">let</span> snake = [
  { x: 10, y: 10 },   <span class="cm">// голова</span>
  { x: 9,  y: 10 },
  { x: 8,  y: 10 },   <span class="cm">// хвост</span>
];</div>
  </div>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>Движение</h3>
      <p>Добавить новую голову спереди, удалить хвост сзади.</p>
    </div>
    <div class="info-card">
      <h3>Рост</h3>
      <p>Съели яблоко — голову добавили, а хвост <span class="hl">не</span> удалили.</p>
    </div>
  </div>
</div>"""},

    # 14 · Сетка вместо пикселей
    {"notes": "Почему клетки, а не пиксели. Для пошаговых игр сетка проще.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Полезный приём</div>
    <h2>Сетка вместо <span class="acc">пикселей</span></h2>
  </div>
  <p>Холст 400×400 пикселей. Клетка — 20 пикселей. Значит сетка — <span class="hl">20×20 клеток</span>.</p>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>Думаем в клетках</h3>
      <p>Змейка на клетке (10, 10). Удобно проверять столкновения.</p>
    </div>
    <div class="info-card">
      <h3>Рисуем в пикселях</h3>
      <p>Клетка (10, 10) → пиксели (200, 200): умножаем на 20.</p>
    </div>
  </div>
  <div class="code-win" style="margin-top:14px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body">ctx.fillRect(seg.x * 20, seg.y * 20, 19, 19);
<span class="cm">//            клетка→пиксели       чуть меньше — видна сетка</span></div>
  </div>
</div>"""},

    # 15 · Цель урока
    {"notes": "Цель урока. Подчеркните: к концу — играбельная игра.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Goal · что будет в конце</div>
    <h2>Цель <span class="acc">урока</span></h2>
  </div>
  <div class="ek-note ek-note--green">Через диалог с DeepSeek собрать «Змейку»: управление стрелками, поедание яблок, счёт, проигрыш при столкновении, сохранение рекорда.</div>
  <div class="grid-2" style="margin-top:14px">
    <div class="info-card">
      <h3>Узнаете</h3>
      <ul class="clean">
        <li>Что такое Canvas и как на нём рисовать</li>
        <li>Что такое игровой цикл</li>
        <li>Как ловить нажатия клавиш через keydown</li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Сделаете</h3>
      <ul class="clean">
        <li>Каркас игры с холстом и сеткой</li>
        <li>Движение змейки по клавишам</li>
        <li>Яблоки, счёт и проигрыш</li>
        <li>Сохранение рекорда между сессиями</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 16 · Демо результата
    {"notes": "Покажите готовую игру, собранную заранее. Сначала дайте увидеть результат, потом переходите к шагам сборки.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Демо результата</div>
    <h2>Что <span class="acc">соберём</span> сегодня</h2>
  </div>
  <p>К концу урока у каждого — <span class="hl">играбельная «Змейка»</span>:</p>
  <div class="grid-2" style="margin-top:8px">
    <div class="info-card">
      <h3>Игровой процесс</h3>
      <ul class="clean">
        <li>Стрелки — управление</li>
        <li>Красное яблоко — растём и набираем очки</li>
        <li>Стена или своё тело — Game Over</li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Прогресс</h3>
      <ul class="clean">
        <li>Табло «Счёт: N»</li>
        <li>«Лучший: N» — рекорд</li>
        <li>Рекорд держится после перезагрузки</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 17 · Папка lesson-04
    {"notes": "lesson-04, 3 файла как обычно.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Структура проекта</div>
    <h2>Папка <span class="acc">lesson-04</span></h2>
  </div>
  <div class="grid-2">
    <ol class="steps">
      <li>В <span class="code-chip">vibe-coding</span> создайте папку <span class="code-chip">lesson-04</span></li>
      <li>Откройте её в <b>VS Code</b></li>
      <li>Создайте 3 файла: <span class="code-chip">index.html</span>, <span class="code-chip">style.css</span>, <span class="code-chip">script.js</span></li>
    </ol>
    <div class="term">
      <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
      <div class="term-body">D:/vibe-coding/lesson-04/
├── index.html
├── style.css
└── script.js</div>
    </div>
  </div>
</div>"""},

    # 18 · Промпт #1 стартовый
    {"notes": "Каркас: холст 400×400, клетка 20px, 20×20 клеток, точка в центре, пустой цикл.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #1 · стартовый</div>
    <h2>Каркас <span class="acc">игры</span></h2>
  </div>
  <div class="prompt-card">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты senior разработчик игр, делал казуальные браузерные игры. Я делаю классическую Змейку для урока программирования.

Требования к каркасу:
- Три файла: index.html, style.css, script.js
- В index.html — заголовок «Змейка», &lt;canvas id="game" width="400" height="400"&gt;, табло «Счёт: 0»
- В style.css — тёмная тема, акцент зелёный #10B981, холст центрирован, лёгкая рамка
- В script.js — настройка холста (ctx), сетка 20×20 клеток (клетка 20px), одна точка змеи в центре, пустой игровой цикл через requestAnimationFrame, который пока только очищает холст и рисует змею

Без библиотек. Чистый JS.

Ответь тремя блоками с подписью имён файлов.</div>
  </div>
</div>"""},

    # 19 · Запуск каркаса
    {"notes": "Видим зелёную точку на чёрном фоне. Не двигается — правильно.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск каркаса</div>
    <h2>Холст и <span class="acc">одна точка</span></h2>
  </div>
  <ol class="steps">
    <li>Скопируйте 3 блока в 3 файла, сохраните</li>
    <li>Правый клик по <span class="code-chip">index.html</span> → <b>Open with Live Server</b></li>
    <li>Вы видите чёрный квадрат с <span class="hl">зелёной точкой</span> посередине</li>
  </ol>
  <div class="ek-note">Точка <b>не двигается</b> — это нормально. Движение добавим следующей правкой.</div>
</div>"""},
]
