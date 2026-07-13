# -*- coding: utf-8 -*-
SLIDES = [
    # 30 · Правка 5 — рекорд в localStorage
    {"notes": "Сохраняем максимальный счёт в localStorage — связь с уроком 3.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 5 · рекорд</div>
    <h2>Сохраняем <span class="acc">рекорд</span> между сессиями</h2>
  </div>
  <p>Финальная правка: рекорд должен пережить перезагрузку страницы. Здесь снова пригодится <span class="hl">localStorage</span> — прямо как в списке задач урока 3.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Добавь рекорд:
- В localStorage храни <span class="hl">лучший счёт</span> (ключ <span class="hl">snake_best</span>)
- При game over: если текущий счёт <span class="hl">больше</span> сохранённого — обнови сохранённый
- На табло над холстом покажи <span class="hl">«Лучший: N»</span>
- При перезагрузке страницы рекорд должен подгрузиться

Изменения в script.js и index.html. Верни изменённые блоки.</div>
  </div>
</div>"""},

    # 31 · Квиз 1 — как замедлить змейку
    {"notes": "Вопрос про скорость. Подождите, потом раскройте.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 1</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 1</span>
    <p class="q-text">Змейка двигается слишком быстро — играть невозможно. Какие два способа замедлить движение, не трогая requestAnimationFrame?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p><b>1. Счётчик кадров:</b> увеличивать <span class="code-chip">frames++</span> в цикле и вызывать <span class="code-chip">update()</span> только когда <span class="code-chip">frames % 10 === 0</span>.</p>
        <p><b>2. По времени:</b> запоминать <span class="code-chip">lastTime</span> и обновлять, только если прошло, например, 150 мс.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 32 · Квиз 2 — сброс состояния при рестарте
    {"notes": "Вопрос про состояние при рестарте. Частая ошибка — забыть сбросить переменные.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 2</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 2</span>
    <p class="q-text">После Game Over игрок жмёт Пробел. Игра запускается, но змейка сразу длинная (как перед смертью) и счёт не обнулился. Что забыли сделать?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>Забыли <b>сбросить состояние</b> при рестарте. Нужно заново задать: <span class="code-chip">snake</span> — 3 сегмента в центре, <span class="code-chip">dir</span> — вправо, <span class="code-chip">score</span> — 0, новое яблоко.</p>
        <p>Промпт для DeepSeek: «при нажатии Пробела сбрасывай snake, dir, score и яблоко в начальное состояние».</p>
      </div>
    </div>
  </div>
</div>"""},

    # 33 · Отладка через Console
    {"notes": "Если игра ведёт себя странно — печатайте состояние в Console.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Инструмент отладки</div>
    <h2>Отладка игры через <span class="acc">Console</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div class="code-win">
      <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
      <div class="code-body"><span class="cm">// печатаем состояние игры</span>
console.log(<span class="st">'snake:'</span>, snake);
console.log(<span class="st">'dir:'</span>, dir);
console.log(<span class="st">'apple:'</span>, apple);</div>
    </div>
    <div>
      <h3>Частые находки</h3>
      <ul class="clean">
        <li><span class="code-chip">dir</span> не меняется → событие keydown не работает</li>
        <li><span class="code-chip">snake</span> растёт без яблок → не удаляется хвост</li>
        <li>яблоко всегда в одном месте → не вызывается randomApple</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 34 · Привычки геймдева (kv)
    {"notes": "5 привычек геймдева. Дайте сфотографировать.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запомните</div>
    <h2>Полезные привычки <span class="acc">геймдева</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">01 · 3 фазы цикла</div><div class="v">input → update → render. На каждом кадре в этом порядке.</div></div>
    <div class="kv-row"><div class="k">02 · Сетка вместо пикселей</div><div class="v">Для пошаговых игр удобнее работать с клетками.</div></div>
    <div class="kv-row"><div class="k">03 · Запрет некорректных действий</div><div class="v">Проверяйте допустимость нажатий, чтобы игра сохраняла понятные правила.</div></div>
    <div class="kv-row"><div class="k">04 · Сброс состояния при рестарте</div><div class="v">snake, dir, score, apple — всё заново в начальное состояние.</div></div>
    <div class="kv-row"><div class="k">05 · console.log — друг</div><div class="v">Странное поведение — печатайте <span class="code-chip">snake</span> и <span class="code-chip">dir</span>.</div></div>
  </div>
</div>"""},

    # 35 · Чек-лист завершения
    {"notes": "Чек-лист завершения игры.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Финальная проверка</div>
    <h2>Готовность <span class="acc">к 55-й минуте</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div>
      <h3>Готово</h3>
      <ul class="clean">
        <li>Папка <span class="code-chip">lesson-04</span> с 3 файлами</li>
        <li>Холст с зелёной змейкой</li>
        <li>Змейка управляется стрелками</li>
        <li>Не разворачивается на 180°</li>
      </ul>
    </div>
    <div>
      <h3>Работает</h3>
      <ul class="clean">
        <li>Яблоки появляются и съедаются, счёт растёт</li>
        <li>Столкновение → экран Game Over</li>
        <li>Пробел — рестарт с нуля</li>
        <li>Рекорд держится после перезагрузки</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 36 · Шпаргалка (kv)
    {"notes": "Шпаргалка по проблемам игры.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Шпаргалка</div>
    <h2>Что делать, <span class="acc">если…</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">точка не появилась</div><div class="v">F12 → Console, прочитайте ошибку про canvas, отправьте в DeepSeek.</div></div>
    <div class="kv-row"><div class="k">слишком быстро</div><div class="v">Счётчик кадров: update только когда <span class="code-chip">frames % 10 === 0</span>.</div></div>
    <div class="kv-row"><div class="k">стрелки скроллят</div><div class="v">Добавьте <span class="code-chip">e.preventDefault()</span> в обработчик keydown.</div></div>
    <div class="kv-row"><div class="k">яблоко в змейке</div><div class="v">Генерация без проверки. Промпт: «генерируй позицию, пока она не свободна».</div></div>
    <div class="kv-row"><div class="k">рестарт ломается</div><div class="v">Не сброшено состояние. Промпт: «при Пробеле сбрось snake, dir, score, apple».</div></div>
  </div>
</div>"""},

    # 37 · Домашнее задание (grid-3)
    {"notes": "ДЗ — прокачать игру. 3 улучшения через диалог.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Домашнее задание · около 30 минут</div>
    <h2>Прокачайте свою <span class="acc">змейку</span></h2>
  </div>
  <p>Через диалог с DeepSeek добавьте 3 улучшения:</p>
  <div class="grid-3" style="margin-top:6px">
    <div class="info-card">
      <h3>Растущая скорость</h3>
      <p>Каждые 5 яблок скорость +20%. К 25 яблокам играть тяжело.</p>
    </div>
    <div class="info-card">
      <h3>Золотое яблоко</h3>
      <p>Раз в 30 секунд — золотое яблоко: +5 очков, исчезает через 3 секунды.</p>
    </div>
    <div class="info-card">
      <h3>Эффект частиц</h3>
      <p>При поедании — вспышка из 5–8 точек, разлетающихся в стороны.</p>
    </div>
  </div>
  <div class="ek-note ek-note--red">Пришлите скриншот игры и ваш лучший рекорд. Один лучший промпт — отдельным сообщением.</div>
</div>"""},

    # 38 · Финал — Модуль 1 пройден
    {"cls": "slide--green", "notes": "Закройте урок. Модуль 1 (веб) завершён. Дальше — Python.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">S</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">A</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">I</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">K</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="bubble">
      <h1>До встречи<br>на уроке 5!</h1>
      <p>Модуль 1 (веб-основы) пройден: HTML, CSS, JavaScript, события, Canvas. На уроке 5 начинаем Python — и впервые подключим нейросеть прямо внутрь своей программы. Подход тот же: формулируем задачу, нейросеть пишет код, мы запускаем и проверяем.</p>
    </div>
  </div>"""},
]
