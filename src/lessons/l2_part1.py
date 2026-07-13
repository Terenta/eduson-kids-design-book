# -*- coding: utf-8 -*-
SLIDES = [
    # 1 · ТИТУЛ
    {"cls": "slide--violet", "notes": "Поприветствуйте группу. Скажите, что сегодня вы научитесь раскладывать проект на 3 файла и пользоваться 5 техниками промтинга. К концу урока у каждого будет интерактивная карточка любимого персонажа.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">H</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">C</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">S</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">J</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="cover-card">
      <div class="badge">Урок №2</div>
      <div class="card-top"><span class="win-dots"><i></i><i></i><i></i></span><span class="win-close"></span></div>
      <h1>Сайт из трёх файлов<br>и техники работы с&nbsp;AI</h1>
      <p class="cover-sub">Разделим проект на 3 файла, изучим 5 техник промтинга и соберём карточку любимого персонажа с интерактивными эффектами.</p>
      <div class="cover-chips"><span class="chip">HTML</span><span class="chip chip--green">CSS</span><span class="chip chip--gray">JavaScript</span><span class="chip chip--gray">DeepSeek</span></div>
    </div>
  </div>"""},

    # 2 · AGENDA
    {"notes": "План на 60 минут. Разбор ДЗ занимает 5 минут, после переходим к архитектуре.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Agenda · план занятия</div>
    <h2>Как пройдут <span class="acc">60 минут</span></h2>
  </div>
  <div class="agenda">
    <div class="agenda-row"><span class="t">0–5</span><div><div class="tt">Разбор домашнего задания</div><div class="dd">Открываем 2–3 чужих диалога, разбираем удачные формулировки.</div></div></div>
    <div class="agenda-row"><span class="t">5–15</span><div><div class="tt">Архитектура простого сайта</div><div class="dd">Зачем 3 файла, что за что отвечает, как они связаны между собой.</div></div></div>
    <div class="agenda-row"><span class="t">15–30</span><div><div class="tt">5 техник промтинга</div><div class="dd">Роль · Контекст · Формат · Ограничения · Итерация.</div></div></div>
    <div class="agenda-row"><span class="t">30–50</span><div><div class="tt">Сборка карточки персонажа</div><div class="dd">3 файла, tilt-эффект, анимированные числа, биография по клику.</div></div></div>
    <div class="agenda-row"><span class="t">50–55</span><div><div class="tt">Если правка ломает код</div><div class="dd">Главное правило — фиксируйте точку отката.</div></div></div>
    <div class="agenda-row"><span class="t">55–60</span><div><div class="tt">Демо в группе</div><div class="dd">Скриншот карточки и один лучший промпт от каждого.</div></div></div>
  </div>
</div>"""},

    # 3 · ИДЕЯ УРОКА
    {"notes": "Идея урока: на уроке 1 вы делали проект в одном файле. Сегодня учимся раскладывать его на 3 файла — это пригодится для всех следующих проектов курса.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Идея урока</div>
    <h2>Что <span class="acc">нового</span> сегодня</h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div class="info-card">
      <h3>Архитектура проекта</h3>
      <p>Когда страница состоит из нескольких блоков с разным поведением, разработчики обычно разделяют код на три файла. У каждого файла своя понятная роль.</p>
    </div>
    <div class="info-card">
      <h3>Продвинутый промтинг</h3>
      <p>На уроке 1 мы давали готовые промпты. Сегодня учимся сочинять их сами, используя 5 техник, которые помогают нейросети точнее понять задачу.</p>
    </div>
  </div>
  <div class="ek-note">К концу урока вы соберёте карточку любимого персонажа — с <b>3D-наклоном</b>, анимированными числами и биографией, которая открывается по клику.</div>
</div>"""},

    # 4 · ТРИ ФАЙЛА — ТРИ РОЛИ
    {"notes": "Покажите диаграмму. Аналогия: HTML — скелет страницы, CSS — её внешний вид, JS — поведение при действиях пользователя. Простая, ясная, запоминается.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Архитектура любого сайта</div>
    <h2>Три файла — <span class="acc">три роли</span></h2>
  </div>
  <div class="grid-3" style="margin-top:6px">
    <div class="info-card">
      <h3>index.html</h3>
      <p><b>Структура</b> — скелет страницы: что на ней есть.</p>
    </div>
    <div class="info-card">
      <h3>style.css</h3>
      <p><b>Внешний вид</b> — оформление: как это выглядит.</p>
    </div>
    <div class="info-card">
      <h3>script.js</h3>
      <p><b>Поведение</b> — реакция: что происходит при клике.</p>
    </div>
  </div>
  <div class="ek-note"><b>Зачем разделять.</b> Меняете цвет — открываете только <span class="code-chip">style.css</span>. Меняете логику — только <span class="code-chip">script.js</span>. Это экономит время и помогает не сломать работающие части проекта.</div>
</div>"""},

    # 5 · СВЯЗЬ ЧЕРЕЗ INDEX.HTML
    {"notes": "Покажите: файлы лежат рядом, но «знают друг о друге» через теги link и script в index.html.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как файлы связаны</div>
    <h2>Связь через <span class="acc">index.html</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div class="term">
      <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">СТРУКТУРА ПАПКИ</span></div>
      <div class="term-body">lesson-02/
├── index.html  <span class="dim">← главный файл</span>
├── style.css   <span class="dim">← подключается через &lt;link&gt;</span>
└── script.js   <span class="dim">← подключается через &lt;script&gt;</span></div>
    </div>
    <div class="code-win">
      <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">INDEX.HTML</span></div>
      <div class="code-body">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;link rel=<span class="st">"stylesheet"</span> href=<span class="st">"style.css"</span>&gt;
&lt;/head&gt;
&lt;body&gt;

  <span class="cm">&lt;!-- весь контент здесь --&gt;</span>

  &lt;script src=<span class="st">"script.js"</span>&gt;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</div>
    </div>
  </div>
  <div class="ek-note"><span class="code-chip">&lt;link&gt;</span> ставится в <span class="code-chip">head</span>, чтобы стили загрузились до контента. <span class="code-chip">&lt;script&gt;</span> — в конце <span class="code-chip">body</span>, чтобы JS запускался после построения страницы. Без подключения файлы лежат рядом, но не «общаются»: без &lt;link&gt; страница откроется без стилей — текст без цветов и отступов, а без &lt;script&gt; не заработают кнопки и эффекты.</div>
</div>"""},

    # 6 · ОБЗОР 5 ТЕХНИК
    {"notes": "Меню. Это обзор, дальше каждая техника отдельным слайдом с примерами «без техники / с техникой». Дайте ученикам сфоткать.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Главная часть урока</div>
    <h2>Пять техник <span class="acc">продвинутого промтинга</span></h2>
  </div>
  <div class="kv" style="margin-top:6px">
    <div class="kv-row"><div class="k">1 · Роль</div><div class="v">Какую роль берёт нейросеть в этом ответе.</div></div>
    <div class="kv-row"><div class="k">2 · Контекст</div><div class="v">Для кого и зачем вы делаете проект.</div></div>
    <div class="kv-row"><div class="k">3 · Формат</div><div class="v">В каком виде нужен ответ.</div></div>
    <div class="kv-row"><div class="k">4 · Ограничения</div><div class="v">Что использовать не нужно.</div></div>
    <div class="kv-row"><div class="k">5 · Итерация</div><div class="v">Точечные правки.</div></div>
  </div>
  <div class="ek-note ek-note--red">Заведите файл <span class="code-chip">prompts.md</span> в папке курса. Записывайте удачные промпты — пригодится на следующих уроках.</div>
</div>"""},

    # 7 · ТЕХНИКА 1 · РОЛЬ
    {"notes": "Роль задаёт стиль ответа. Если попросить «дизайнера Apple» — получится одно решение, если попросить «художника Ghibli» — другое.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Техника 1 · Роль</div>
    <h2>Укажите <span class="acc">роль</span> нейросети</h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>Без роли</h4>
      <p>«Напиши код для карточки.»</p>
      <p class="note">Нейросеть выберет стиль на своё усмотрение.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>С ролью</h4>
      <p>«Ты <b>senior фронтенд-разработчик</b> с опытом в Apple и Stripe. Напиши код для карточки <b>в стиле Apple</b>: минималистично, много воздуха, лёгкие тени.»</p>
      <p class="note">Ответ будет в характерном стиле компании.</p>
    </div>
  </div>
  <div class="ek-note"><b>Полезные роли:</b> senior-дизайнер Apple, principal-инженер Google, креативный директор Pixar, художник студии Ghibli, UX-дизайнер из Linear.</div>
</div>"""},

    # 8 · ТЕХНИКА 2 · КОНТЕКСТ
    {"notes": "Контекст — для кого делаете. Помогает выбрать стиль и тон.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Техника 2 · Контекст</div>
    <h2>Расскажите, <span class="acc">для кого</span> делаете</h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>Без контекста</h4>
      <p>«Сделай мне сайт.»</p>
      <p class="note">Нейросеть не знает аудиторию и выбирает усреднённое решение.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>С контекстом</h4>
      <p>«Я делаю сайт-визитку для <b>портфолио школьника 14 лет</b>. Зрители — <b>преподаватели колледжа</b>, в который я хочу поступить. Цель — впечатление аккуратности и вкуса.»</p>
      <p class="note">Нейросеть подберёт стиль под конкретную аудиторию.</p>
    </div>
  </div>
</div>"""},

    # 9 · ТЕХНИКА 3 · ФОРМАТ
    {"notes": "Формат вывода — это вид ответа. Если не указать формат, нейросеть может выдать длинный текст с объяснениями.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Техника 3 · Формат</div>
    <h2>Скажите, <span class="acc">как ответить</span></h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>Без формата</h4>
      <p>«Расскажи, как сделать кнопку.»</p>
      <p class="note">Ответ будет с объяснениями, придётся фильтровать.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>С форматом</h4>
      <p>«Ответь <b>только готовым кодом</b>, без объяснений. Один блок <span class="code-chip">```html</span> — один файл. Если нужны три файла — <b>три блока с подписью имени файла сверху</b>.»</p>
      <p class="note">Ответ компактный, готов к копированию.</p>
    </div>
  </div>
  <div class="ek-note"><b>Полезные форматы:</b> «таблицей», «списком из N пунктов», «JSON», «псевдокодом», «диаграммой через ASCII-арт».</div>
</div>"""},

    # 10 · ТЕХНИКА 4 · ОГРАНИЧЕНИЯ
    {"notes": "Ограничения — что использовать не нужно. Например, без библиотек, без emoji, не более N строк.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Техника 4 · Ограничения</div>
    <h2>Укажите, <span class="acc">чего не использовать</span></h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>Без ограничений</h4>
      <p>«Сделай интерактивную карточку.»</p>
      <p class="note">Нейросеть может подключить библиотеки, которые не нужны учебному проекту.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>С ограничениями</h4>
      <p>«Сделай карточку. Ограничения: <b>без библиотек</b> (никаких jQuery, Bootstrap, React). Только чистый HTML/CSS/JS. <b>Не более 80 строк CSS</b>. <b>Не используй !important</b>.»</p>
      <p class="note">Код будет компактный и понятный.</p>
    </div>
  </div>
  <div class="ek-note"><b>Полезные ограничения:</b> «без сторонних библиотек», «без классов и фреймворков», «не более N строк», «работает в одном файле», «не используй устаревшие теги».</div>
</div>"""},

    # 11 · ТЕХНИКА 5 · ИТЕРАЦИЯ
    {"notes": "Самая важная техника на курсе. Если хотите изменить деталь — явно скажите: «оставь всё как есть, измени только Х».", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Техника 5 · Итерация</div>
    <h2>Делайте <span class="acc">точечные правки</span></h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>Слишком общая правка</h4>
      <p>«Перепиши всё, чтобы было лучше.»</p>
      <p class="note">Нейросеть может переписать весь код, и работающие части перестанут работать.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>Точечная правка</h4>
      <p>«<b>Оставь весь код как есть.</b> Измени <b>только одно</b>: в файле <span class="code-chip">style.css</span>, в селекторе <span class="code-chip">.button</span>, поменяй цвет фона с <span class="code-chip">#7C3AED</span> на <span class="code-chip">#06B6D4</span>. Верни мне <b>только этот изменённый кусок</b>.»</p>
      <p class="note">Изменится только нужное место.</p>
    </div>
  </div>
  <div class="ek-note ek-note--green"><b>Полезная формула:</b> «Оставь всё как есть. Измени только Х. Верни только изменённый кусок».</div>
</div>"""},
]
