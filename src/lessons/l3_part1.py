# -*- coding: utf-8 -*-
SLIDES = [
    # 1 · ТИТУЛ
    {"cls": "slide--violet", "notes": "Поздоровайтесь. Сегодня страницы научатся реагировать на действия пользователя — клики, ввод, отметки. К концу урока — рабочий список задач, который сохраняет данные между перезагрузками.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">D</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">O</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">M</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">JS</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="cover-card">
      <div class="badge">Урок №3</div>
      <div class="card-top"><span class="win-dots"><i></i><i></i><i></i></span><span class="win-close"></span></div>
      <h1>Интерактивность:<br>события и&nbsp;DOM</h1>
      <p class="cover-sub">Научимся слушать действия пользователя, менять страницу из JavaScript и сохранять данные локально. Соберём список задач, который не теряется при перезагрузке.</p>
      <div class="cover-chips"><span class="chip">JavaScript</span><span class="chip chip--green">DOM events</span><span class="chip chip--gray">localStorage</span><span class="chip chip--gray">DeepSeek</span></div>
    </div>
  </div>"""},

    # 2 · ПЛАН
    {"notes": "План на 60 минут. Подчеркните: основное время — на сборку списка задач. Это первый проект, который сохраняет данные.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Agenda · план занятия</div>
    <h2>Как пройдут <span class="acc">60 минут</span></h2>
  </div>
  <div class="agenda">
    <div class="agenda-row"><span class="t">0–5</span><div><div class="tt">Разбор домашнего задания</div><div class="dd">Смотрим 2–3 присланные галереи персонажей, разбираем удачные промпты.</div></div></div>
    <div class="agenda-row"><span class="t">5–15</span><div><div class="tt">DOM и события</div><div class="dd">Карта страницы и сигналы пользователя.</div></div></div>
    <div class="agenda-row"><span class="t">15–25</span><div><div class="tt">Стартовый промпт</div><div class="dd">Соберём каркас списка задач из 3 файлов.</div></div></div>
    <div class="agenda-row"><span class="t">25–45</span><div><div class="tt">5 правок через диалог</div><div class="dd">Добавление, удаление, чекбокс, localStorage, анимация.</div></div></div>
    <div class="agenda-row"><span class="t">45–55</span><div><div class="tt">Отладка и проверка</div><div class="dd">Console, мини-вопросы для группы.</div></div></div>
    <div class="agenda-row"><span class="t">55–60</span><div><div class="tt">Демо в группе</div><div class="dd">Скриншоты результата и разбор удачных промптов.</div></div></div>
  </div>
</div>"""},

    # 3 · РАЗБОР ДЗ
    {"notes": "Откройте 2–3 присланные галереи персонажей. Разбираем: какой промпт собрал галерею с первого раза, где фильтр «Все / Спорт / Кино / Игры» пришлось переформулировать. Главная мысль — точные формулировки экономят время.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор ДЗ урока 2</div>
    <h2>Смотрим <span class="acc">галереи персонажей</span></h2>
  </div>
  <p>Открываем 2–3 присланные работы — галерею из 3 карточек с фильтром «Все / Спорт / Кино / Игры» — и разбираем именно <span class="hl">диалог с нейросетью</span>, а не только результат.</p>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card">
      <h3>Что сработало</h3>
      <p>Промпты с ролью («ты senior-разработчик») и форматом («три карточки в ряд, над ними — кнопки фильтра»).</p>
    </div>
    <div class="info-card">
      <h3>Что переделывали</h3>
      <p>Фильтр показывал всех сразу или прятал не те карточки — забыли задать каждому персонажу его категорию.</p>
    </div>
    <div class="info-card">
      <h3>Вывод</h3>
      <p>Точная формулировка экономит время. Сегодня применяем эти же техники к списку задач.</p>
    </div>
  </div>
</div>"""},

    # 4 · ИДЕЯ УРОКА
    {"notes": "Объясните спокойно: до этого страница была статичной. Сегодня делаем настоящую реакцию — пользователь что-то делает, страница меняется в ответ.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Идея урока</div>
    <h2>Что значит <span class="acc">«страница интерактивна»</span></h2>
  </div>
  <p>Интерактивная страница умеет <span class="hl">отвечать на действия пользователя</span>: клик по кнопке, ввод текста, отметку чекбокса, прокрутку, наведение мыши.</p>
  <div class="ek-note" style="margin-top:6px">Кнопка с hover-эффектом из урока 2 — это ещё не интерактивность. Настоящая интерактивность — когда после действия пользователя <b>меняется содержимое страницы</b>: появляется новый элемент, обновляется текст, сохраняются данные.</div>
</div>"""},

    # 5 · ПРИМЕРЫ
    {"notes": "Приведите примеры из жизни подростка. Любое приложение, которым он пользуется — это набор реакций на события.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Примеры</div>
    <h2>Интерактивность <span class="acc">вокруг нас</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div class="info-card">
      <h3>Telegram</h3>
      <p>Нажал на сообщение — появилось меню. Напечатал текст — кнопка «отправить» стала активной.</p>
    </div>
    <div class="info-card">
      <h3>Игры в браузере</h3>
      <p>Нажал стрелку — персонаж пошёл. Кликнул по врагу — у него убавилось здоровье.</p>
    </div>
    <div class="info-card">
      <h3>Формы и анкеты</h3>
      <p>Ввёл короткий пароль — появилась подсказка «слишком короткий».</p>
    </div>
    <div class="info-card">
      <h3>Списки и чек-листы</h3>
      <p>Отметил задачу — она зачеркнулась. Перезагрузил — она осталась на месте.</p>
    </div>
  </div>
  <p style="margin-top:10px">Сегодня соберём последнее — <span class="hl">список задач</span>.</p>
</div>"""},

    # 6 · ТРИ ШАГА
    {"notes": "Главная схема урока: действие → событие → реакция. Запомнить.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Как это устроено</div>
    <h2>Три шага <span class="acc">интерактивности</span></h2>
  </div>
  <div class="grid-3" style="margin-top:6px">
    <div class="info-card">
      <h3>1 · Действие</h3>
      <p>Пользователь нажимает кнопку, печатает текст, отмечает чекбокс.</p>
    </div>
    <div class="info-card">
      <h3>2 · Событие</h3>
      <p>Браузер замечает действие и отправляет «событие» (event) в JavaScript.</p>
    </div>
    <div class="info-card">
      <h3>3 · Реакция</h3>
      <p>Скрипт получает событие и меняет страницу: добавляет элемент, обновляет текст, сохраняет данные.</p>
    </div>
  </div>
  <div class="ek-note" style="margin-top:12px">Сегодня учимся ловить эти события и менять страницу в ответ — через диалог с DeepSeek.</div>
</div>"""},

    # 7 · ЧТО ТАКОЕ DOM
    {"notes": "DOM — Document Object Model. Объясните как карту: страница в памяти браузера представлена деревом. JS может ходить по нему и менять любую веточку.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Карта страницы</div>
    <h2>Что такое <span class="acc">DOM</span></h2>
  </div>
  <p>DOM (Document Object Model) — это <span class="hl">модель страницы в памяти браузера</span>. Каждый тег HTML превращается в узел, к которому можно обратиться из JavaScript.</p>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>HTML — это текст</h4>
      <p>То, что вы пишете в файле <span class="code-chip">index.html</span>.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>DOM — это объекты</h4>
      <p>То, во что браузер превращает HTML, чтобы JS мог это менять «на лету».</p>
    </div>
  </div>
</div>"""},

    # 8 · ДЕРЕВО DOM
    {"notes": "Покажите дерево. Каждый вложенный тег — ветка. Из любого узла можно дойти до любого другого.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">DOM — это дерево</div>
    <h2>Страница как <span class="acc">дерево элементов</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div class="code-win">
      <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">HTML</span></div>
      <div class="code-body">&lt;body&gt;
  &lt;h1&gt;Мои задачи&lt;/h1&gt;
  &lt;input id=<span class="st">"field"</span>&gt;
  &lt;button id=<span class="st">"add"</span>&gt;Добавить&lt;/button&gt;
  &lt;ul id=<span class="st">"list"</span>&gt;
    &lt;li&gt;Купить хлеб&lt;/li&gt;
  &lt;/ul&gt;
&lt;/body&gt;</div>
    </div>
    <div class="code-win">
      <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ДЕРЕВО DOM</span></div>
      <div class="code-body">body
├── h1            <span class="st">"Мои задачи"</span>
├── input#field
├── button#add    <span class="st">"Добавить"</span>
└── ul#list
    └── li        <span class="st">"Купить хлеб"</span></div>
    </div>
  </div>
  <p style="margin-top:10px">JS умеет дойти до любого узла и изменить его.</p>
</div>"""},

    # 9 · КАК НАЙТИ ЭЛЕМЕНТ
    {"notes": "Два главных способа: getElementById и querySelector. Покажите оба.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Шаг 1 работы с DOM</div>
    <h2>Как JavaScript <span class="acc">находит элемент</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div class="code-win">
      <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ПО ID</span></div>
      <div class="code-body"><span class="cm">// HTML: &lt;button id="add"&gt;</span>
<span class="kw">const</span> btn = document.getElementById(<span class="st">'add'</span>);

<span class="cm">// Современный универсальный способ</span>
<span class="kw">const</span> btn2 = document.querySelector(<span class="st">'#add'</span>);</div>
    </div>
    <div class="code-win">
      <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ПО КЛАССУ / ТЕГУ</span></div>
      <div class="code-body"><span class="cm">// Первый элемент с классом .task</span>
<span class="kw">const</span> t = document.querySelector(<span class="st">'.task'</span>);

<span class="cm">// ВСЕ элементы &lt;li&gt; — список</span>
<span class="kw">const</span> all = document.querySelectorAll(<span class="st">'li'</span>);</div>
    </div>
  </div>
  <div class="ek-note ek-note--red" style="margin-top:12px"><b>Правило:</b> <span class="code-chip">querySelector</span> возвращает <span class="hl">один</span> элемент (первый совпавший). <span class="code-chip">querySelectorAll</span> — <span class="hl">список</span> всех совпавших.</div>
</div>"""},

    # 10 · КАК МЕНЯЕТ ЭЛЕМЕНТ
    {"notes": "Три главных операции: поменять текст, добавить/убрать класс, создать новый элемент.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Шаг 2 работы с DOM</div>
    <h2>Как JavaScript <span class="acc">меняет элемент</span></h2>
  </div>
  <div class="code-win" style="margin-top:6px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body"><span class="cm">// 1. Поменять текст</span>
document.querySelector(<span class="st">'h1'</span>).textContent = <span class="st">'Привет!'</span>;

<span class="cm">// 2. Добавить / убрать CSS-класс</span>
element.classList.add(<span class="st">'done'</span>);
element.classList.remove(<span class="st">'done'</span>);
element.classList.toggle(<span class="st">'done'</span>);   <span class="cm">// есть → убрать, нет → добавить</span>

<span class="cm">// 3. Создать новый элемент и вставить</span>
<span class="kw">const</span> li = document.createElement(<span class="st">'li'</span>);
li.textContent = <span class="st">'Новая задача'</span>;
document.querySelector(<span class="st">'ul'</span>).appendChild(li);

<span class="cm">// 4. Удалить элемент</span>
li.remove();</div>
  </div>
  <p style="margin-top:10px">Этих 4 операций хватит, чтобы собрать список задач целиком.</p>
</div>"""},
]
