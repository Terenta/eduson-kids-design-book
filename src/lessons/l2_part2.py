# -*- coding: utf-8 -*-
SLIDES = [
    # 12 · Практика — карточка персонажа
    {"notes": "Главный проект урока. Каждый выбирает любимого персонажа — Гарри Поттер, Месси, Доктор Стрэндж, кто угодно.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Практика · 20 минут</div>
    <h2>Карточка любимого <span class="acc">персонажа</span></h2>
  </div>
  <div class="grid-2" style="margin-top:8px">
    <div>
      <h3>Состав карточки</h3>
      <ul class="clean">
        <li>Имя, аватар, краткое описание</li>
        <li>3 характеристики: Сила, Ум, Харизма (числа 1–100)</li>
        <li>При наведении — <span class="hl">3D-наклон</span> в сторону курсора</li>
        <li>При клике — <span class="hl">раскрывается биография</span></li>
        <li>Стеклянный эффект (backdrop blur)</li>
      </ul>
    </div>
    <div class="ek-note">
      <h3>Как соберём</h3>
      <ul class="clean">
        <li>3 файла: <span class="code-chip">index.html</span> · <span class="code-chip">style.css</span> · <span class="code-chip">script.js</span></li>
        <li>Без библиотек — чистый HTML, CSS, JavaScript</li>
        <li>Запускаем через Live Server</li>
      </ul>
      <p style="margin-top:12px">Персонажа выбирайте сами: Гарри Поттер, Лионель Месси, Капитан Америка, Кратос…</p>
    </div>
  </div>
</div>"""},

    # 13 · Стартовый промпт со всеми 5 техниками
    {"notes": "Стартовый промпт собирает в себе все 5 техник: роль, контекст, формат, ограничения. Дайте ученикам скопировать целиком.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #1 · стартовый</div>
    <h2>Промпт со всеми <span class="acc">пятью техниками</span></h2>
  </div>
  <div class="prompt-card" style="margin-top:10px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты <span class="hl">senior фронтенд-разработчик в стиле Apple/Linear</span>.
Я делаю карточку любимого персонажа — <span class="hl">Гарри Поттера</span> (замените на своего). Зрители — мои одноклассники в школьном чате.

Требования:
- <span class="hl">Три файла</span>: index.html, style.css, script.js
- В index.html — структура: имя, аватар (placeholder div), описание, три характеристики (Сила, Ум, Харизма) с числами 1-100
- В style.css — тёмная тема, акцент <span class="hl">золотой #D4AF37</span>, стеклянный эффект (backdrop-filter blur), tilt 3D при наведении
- В script.js — при клике на карточку показывается всплывающий блок с биографией (3-5 предложений)
- <span class="hl">Без библиотек</span>, чистый код, должно работать в браузере без сервера

Ответь <span class="hl">тремя блоками кода</span>, по одному на каждый файл, с подписью имени файла сверху.</div>
  </div>
</div>"""},

    # 14 · Создание проекта — три файла, три блока
    {"notes": "Покажите на проекторе: создаём 3 файла, копируем 3 блока кода, сохраняем, запускаем Live Server.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Создание проекта</div>
    <h2>Три файла, <span class="acc">три блока кода</span></h2>
  </div>
  <div class="grid-2" style="margin-top:8px">
    <ol class="steps steps--tight">
      <li>В VS Code откройте папку <span class="code-chip">D:/vibe-coding/lesson-02/</span></li>
      <li>Создайте 3 файла: <span class="code-chip">index.html</span>, <span class="code-chip">style.css</span>, <span class="code-chip">script.js</span></li>
      <li>В DeepSeek нажмите Copy на первом блоке (HTML) → вставьте в <span class="code-chip">index.html</span></li>
      <li>Тем же способом — со вторым (CSS) и третьим (JS)</li>
      <li>Сохраните все три файла (<span class="code-chip">Ctrl+S</span> в каждом)</li>
      <li>Правый клик по <span class="code-chip">index.html</span> → <b>Open with Live Server</b></li>
    </ol>
    <div class="ek-note ek-note--red">
      <h3>Если страница пустая</h3>
      <p>Откройте DevTools (F12) → вкладка <b>Console</b>. Там будет ошибка красным. Скопируйте её текст и отправьте в DeepSeek с вопросом «как исправить?».</p>
      <p style="margin-top:10px">В большинстве случаев нейросеть исправляет за один ответ.</p>
    </div>
  </div>
</div>"""},

    # 15 · Правка 1 — аватар
    {"notes": "Первая правка — добавляем настоящий аватар. Используем технику Итерации: «измени только Х, остальное не трогай».", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 1 · аватар</div>
    <h2>Точечная правка <span class="acc">через диалог</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Замени placeholder-аватар на <span class="hl">круглую картинку 140×140 пикселей</span>. Картинку возьми по ссылке https://api.dicebear.com/7.x/adventurer/svg?seed=Harry

Изменения <span class="hl">только в index.html</span> и в селекторе <span class="hl">.avatar в style.css</span>. Остальной код не трогай.

Верни мне только изменённые куски.</div>
  </div>
  <div class="ek-note">Замените <span class="code-chip">seed=Harry</span> на имя вашего персонажа.</div>
</div>"""},

    # 16 · Правка 2 — анимация чисел
    {"notes": "Вторая правка — в JS. Анимация чисел от 0 до значений. Покажите, как нейросеть добавляет функцию, не трогая существующие.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 2 · анимация чисел</div>
    <h2>Добавляем <span class="acc">поведение в JS</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">В script.js добавь функцию: при загрузке страницы числа характеристик (Сила, Ум, Харизма) <span class="hl">анимируются от 0 до своих значений за 1 секунду</span>.

Не трогай другие функции. Добавь новую и вызови её при <span class="hl">DOMContentLoaded</span>.

Верни только новый код, который нужно добавить.</div>
  </div>
  <div class="ek-note"><b>DOMContentLoaded</b> — событие, которое срабатывает, когда страница полностью загрузилась. Анимировать числа до загрузки бесполезно — на экране их ещё нет.</div>
</div>"""},

    # 17 · Правка 3 — 3D-наклон
    {"notes": "Самая зрелищная правка. Tilt 3D — карточка наклоняется в сторону курсора.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 3 · 3D-наклон</div>
    <h2>Эффект «наклон <span class="acc">в сторону курсора</span>»</h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:10px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Сейчас при наведении карточка просто увеличивается. Сделай эффект <span class="hl">3D-наклона</span>: карточка <span class="hl">наклоняется в сторону курсора</span>, как в интерфейсах с глубиной (например, на промо-страницах Apple).

Реализуй на <span class="hl">чистом JS в script.js</span>, через transform: rotateX(...) rotateY(...) и событие mousemove.

<span class="hl">Без библиотек</span>. Только то, что уже подключено.</div>
  </div>
</div>"""},

    # 18 · Точка отката / зацикливание
    {"notes": "Главный навык: фиксируйте точки отката. Перед серьёзной правкой — копия. Иначе можно случайно потерять час работы.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Полезный навык</div>
    <h2>Если правка <span class="acc">ломает код</span></h2>
  </div>
  <div class="grid-2" style="margin-top:8px">
    <div>
      <h3>Точка отката</h3>
      <p><b>Перед серьёзной правкой сохраняйте копию.</b></p>
      <ol class="steps steps--tight" style="margin-top:10px">
        <li>Скопируйте <span class="code-chip">index.html</span> в <span class="code-chip">index_v2.html</span></li>
        <li>Сделайте правку</li>
        <li>Не подошло — удалите изменённый файл, переименуйте копию обратно</li>
      </ol>
      <p style="margin-top:12px">С урока 3 будем делать это автоматически через Git. Пока — копируем руками.</p>
    </div>
    <div class="ek-note ek-note--red">
      <h3>Если нейросеть «зациклилась»</h3>
      <p>Иногда правки приводят к одной и той же ошибке. Откройте <b>новый чат</b> в DeepSeek.</p>
      <p style="margin-top:8px">В первом сообщении приложите <span class="hl">весь актуальный код</span> (3 файла) и опишите, что нужно сделать.</p>
      <p style="margin-top:8px">Длинные диалоги начинают «забываться». Свежий чат начинает с нуля.</p>
    </div>
  </div>
</div>"""},

    # 19 · Квиз
    {"notes": "Простой вопрос для проверки понимания. Подождите 10–15 секунд, потом разберите варианты ответов.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка</div>
    <h2>Изучите ситуацию <span class="acc">и ответьте</span></h2>
  </div>
  <div class="quiz-box" style="margin-top:8px">
    <span class="q-num">Вопрос</span>
    <p class="q-text">Вы сделали 5 правок подряд, последняя — добавление tilt-эффекта. После неё клик по карточке перестал открывать биографию. Какой промпт описывает ситуацию точнее всего?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>«После добавления tilt-эффекта перестал срабатывать обработчик click на карточке. Скорее всего, mousemove или transform мешает событию click. Как исправить, не убирая tilt? Верни только изменённый кусок script.js.»</p>
        <p>Здесь есть и описание ситуации, и гипотеза, и точечная правка, и формат ответа.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 20 · Пять привычек
    {"notes": "Закрепление. 5 правил, которые важно унести с урока.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запомните</div>
    <h2>Пять полезных <span class="acc">привычек</span></h2>
  </div>
  <div class="kv" style="margin-top:8px">
    <div class="kv-row"><div class="k">01 · Три файла</div><div class="v">Любой проект разбиваем на структуру (HTML), оформление (CSS), поведение (JS).</div></div>
    <div class="kv-row"><div class="k">02 · Маленькие промпты</div><div class="v">Одна правка — один промпт. Так проще сохранять контроль над проектом.</div></div>
    <div class="kv-row"><div class="k">03 · «Оставь всё как есть»</div><div class="v">Полезная фраза для точечных правок. Помогает нейросети не «расходиться».</div></div>
    <div class="kv-row"><div class="k">04 · Точка отката</div><div class="v">Перед серьёзным изменением — копия файла. Спасает время и работу.</div></div>
    <div class="kv-row"><div class="k">05 · Контекст устаревает</div><div class="v">Чат стал длинным и нейросеть путается — открывайте новый, прикладывайте актуальный код.</div></div>
  </div>
</div>"""},

    # 21 · ДЗ — галерея из трёх персонажей
    {"notes": "ДЗ: галерея из 3 героев + фильтр. Это шаг от одного компонента к мини-приложению.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Домашнее задание · около 30 минут</div>
    <h2>Галерея из трёх <span class="acc">персонажей</span></h2>
  </div>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card">
      <h3>HTML</h3>
      <p>Дополните <span class="code-chip">index.html</span> ещё двумя карточками. Получится 3 персонажа в одном проекте.</p>
    </div>
    <div class="info-card">
      <h3>CSS</h3>
      <p>Оформите <span class="hl">grid-сетку</span>: на десктопе — 3 в ряд, на мобильном — 1 в ряд. Используйте <span class="code-chip">@media</span>.</p>
    </div>
    <div class="info-card">
      <h3>JS</h3>
      <p>Добавьте <span class="hl">фильтр сверху</span>: кнопки «Все / Спорт / Кино / Игры». При клике показываются только нужные карточки.</p>
    </div>
  </div>
  <div class="ek-note ek-note--red">Пришлите в чат: скриншот галереи и один <span class="hl">самый удачный промпт</span> из своих за это задание.</div>
</div>"""},

    # 22 · Финал (green bubble) — анонс урока 3: события и DOM
    {"cls": "slide--green", "notes": "Закройте урок. На следующем уроке страница научится реагировать на действия пользователя: клики, ввод, события и DOM. Соберём список задач, который запоминает данные между перезагрузками через localStorage.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">D</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">O</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">M</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">J</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="bubble">
      <h1>До встречи<br>на уроке 3!</h1>
      <p>Сегодня собрали интерактивную карточку персонажа из трёх файлов и освоили пять техник промтинга. На следующем уроке страница научится реагировать на клики и ввод: соберём список задач, который запоминает данные между перезагрузками через localStorage.</p>
      <div class="cover-chips"><span class="chip">Урок 3 · События и DOM</span><span class="chip chip--green">localStorage</span><span class="chip chip--gray">Список задач</span></div>
    </div>
  </div>"""},
]
