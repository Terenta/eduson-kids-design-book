# -*- coding: utf-8 -*-
SLIDES = [
    # 20 · Правка 1 — добавление задач (промпт)
    {"notes": "Первая логика. Учим JS слушать клик и добавлять новый <li>.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 1 · добавление задач</div>
    <h2>Учим кнопку реагировать на <span class="acc">клик</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:6px">
    <span class="pc-tag">&rarr; В тот же чат</span>
    <div class="pc-text">В script.js напиши логику:
&bull; При клике на кнопку «Добавить» <span class="hl">прочитай текст из поля ввода</span>
&bull; Если поле <span class="hl">не пустое</span> — добавь новый &lt;li&gt; с этим текстом в &lt;ul id="list"&gt;
&bull; После добавления <span class="hl">очисти поле ввода</span>
&bull; Используй <span class="hl">addEventListener</span>

Изменения только в script.js. Не трогай index.html и style.css. Верни только содержимое script.js.</div>
  </div>
</div>"""},

    # 21 · Разбор кода правки 1
    {"notes": "Откройте сгенерированный script.js. Покажите построчно, как он работает: так ученики понимают, что именно дала нейросеть.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Что сгенерировала <span class="acc">нейросеть</span></h2>
  </div>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body"><span class="kw">const</span> field = document.getElementById(<span class="st">'field'</span>);   <span class="cm">// поле ввода</span>
<span class="kw">const</span> addBtn = document.getElementById(<span class="st">'add'</span>);     <span class="cm">// кнопка</span>
<span class="kw">const</span> list = document.getElementById(<span class="st">'list'</span>);      <span class="cm">// &lt;ul&gt;</span>

addBtn.addEventListener(<span class="st">'click'</span>, () =&gt; {           <span class="cm">// подписка на клик</span>
  <span class="kw">const</span> text = field.value.trim();                 <span class="cm">// что ввели</span>
  <span class="kw">if</span> (text === <span class="st">''</span>) <span class="kw">return</span>;                          <span class="cm">// пусто — выходим</span>

  <span class="kw">const</span> li = document.createElement(<span class="st">'li'</span>);          <span class="cm">// новый &lt;li&gt;</span>
  li.textContent = text;                            <span class="cm">// вставили текст</span>
  list.appendChild(li);                             <span class="cm">// добавили в список</span>

  field.value = <span class="st">''</span>;                                 <span class="cm">// очистили поле</span>
});</div>
  </div>
  <div class="ek-note">Прочитайте вслух каждую строку. Это ровно те 4 операции DOM со слайда 10.</div>
</div>"""},

    # 22 · Правка 2 — удаление (промпт)
    {"notes": "Удаление по клику. На каждой задаче — кнопка крестик.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 2 · удаление</div>
    <h2>Каждая задача с кнопкой <span class="acc">«&times;»</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:6px">
    <span class="pc-tag">&rarr; В тот же чат</span>
    <div class="pc-text">Доработай script.js:
&bull; При создании каждого &lt;li&gt; <span class="hl">добавляй внутрь него кнопку «&times;»</span> справа от текста
&bull; При клике на эту кнопку <span class="hl">удаляй именно её &lt;li&gt;</span>
&bull; В style.css добавь оформление кнопки: круглая, серая, при наведении — красная

Изменения в script.js и style.css. Верни только изменённые блоки.</div>
  </div>
</div>"""},

    # 23 · Тонкость — обработчик на самой кнопке
    {"notes": "Важная концепция. Объясните, почему обработчик вешается на саму кнопку «×», а не на весь список.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Важная тонкость</div>
    <h2>Почему обработчик — на <span class="acc">самой кнопке</span></h2>
  </div>
  <div class="vs" style="margin-top:6px">
    <div class="vs-col vs-col--plain">
      <h4>&times; Частая ошибка</h4>
      <p>Повесить один обработчик на весь <span class="code-chip">&lt;ul&gt;</span> — клик по любому месту удаляет всё подряд.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>&check; Правильно</h4>
      <p>Для каждой кнопки «&times;» — свой обработчик, который знает свой <span class="code-chip">&lt;li&gt;</span> и удаляет только его.</p>
    </div>
  </div>
  <div class="code-win" style="margin-top:12px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body"><span class="kw">const</span> del = document.createElement(<span class="st">'button'</span>);
del.textContent = <span class="st">'&times;'</span>;
del.addEventListener(<span class="st">'click'</span>, () =&gt; {
  li.remove();                 <span class="cm">// удаляем именно ЭТОТ li</span>
});
li.appendChild(del);</div>
  </div>
</div>"""},

    # 24 · Правка 3 — чекбокс «выполнено» (промпт)
    {"notes": "Чекбокс выполнено. Добавляем визуальный индикатор + класс .done.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 3 · отметка «выполнено»</div>
    <h2>Чекбокс на каждой <span class="acc">задаче</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:6px">
    <span class="pc-tag">&rarr; В тот же чат</span>
    <div class="pc-text">Доработай:
&bull; В каждом &lt;li&gt; <span class="hl">слева от текста</span> добавь <span class="hl">чекбокс</span> (input type="checkbox")
&bull; При отметке чекбокса задаче добавляется класс <span class="hl">done</span>
&bull; В style.css для класса <span class="hl">.done</span>: серый цвет текста, зачёркнутый текст (text-decoration: line-through)

Изменения в script.js и style.css. Верни только изменённые блоки.</div>
  </div>
</div>"""},

    # 25 · Правка 4 — сохранение в localStorage (промпт)
    {"notes": "Сохранение в localStorage. Это магия — задачи остаются после перезагрузки.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 4 · сохранение</div>
    <h2>Задачи не теряются при <span class="acc">перезагрузке</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:6px">
    <span class="pc-tag">&rarr; В тот же чат</span>
    <div class="pc-text">Добавь сохранение в <span class="hl">localStorage</span>:
&bull; При любом изменении (добавление, удаление, отметка) <span class="hl">сохраняй массив задач</span> в localStorage
&bull; При загрузке страницы — <span class="hl">прочитай задачи из localStorage</span> и отрисуй их

Каждая задача — объект с двумя полями: <span class="hl">{ text: string, done: boolean }</span>.

Изменения только в script.js. Верни целиком обновлённый script.js.</div>
  </div>
</div>"""},

    # 26 · Что такое localStorage
    {"notes": "Краткое объяснение, как работает localStorage. Привязан к домену сайта.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Полезное знание</div>
    <h2>Что такое <span class="acc">localStorage</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div>
      <p>localStorage — это <b>маленькое хранилище в браузере</b>. Данные не исчезают при перезагрузке и закрытии вкладки.</p>
      <ul class="clean" style="margin-top:10px">
        <li>До ~5 МБ на один сайт</li>
        <li>Хранит только <span class="hl">строки</span> (ключ &rarr; значение)</li>
        <li>Привязан к домену: другой сайт не увидит ваши данные</li>
      </ul>
    </div>
    <div class="code-win">
      <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
      <div class="code-body"><span class="cm">// Сохранить</span>
localStorage.setItem(<span class="st">'tasks'</span>, <span class="st">'...'</span>);

<span class="cm">// Прочитать</span>
<span class="kw">const</span> saved = localStorage.getItem(<span class="st">'tasks'</span>);

<span class="cm">// Удалить</span>
localStorage.removeItem(<span class="st">'tasks'</span>);</div>
    </div>
  </div>
</div>"""},

    # 27 · Массив → строка → массив (JSON)
    {"notes": "localStorage хранит строки. Массив объектов — через JSON.stringify туда и JSON.parse обратно.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Ключевой приём</div>
    <h2>Массив &rarr; строка &rarr; <span class="acc">массив</span></h2>
  </div>
  <p>localStorage хранит только <b>строки</b>. Массив задач превращаем в строку и обратно:</p>
  <div class="code-win" style="margin-top:6px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
    <div class="code-body"><span class="kw">const</span> tasks = [
  { text: <span class="st">'Купить хлеб'</span>, done: <span class="kw">false</span> },
  { text: <span class="st">'Сделать ДЗ'</span>,  done: <span class="kw">true</span>  },
];

<span class="cm">// Сохранить: массив &rarr; строка JSON</span>
localStorage.setItem(<span class="st">'tasks'</span>, JSON.stringify(tasks));

<span class="cm">// Прочитать: строка JSON &rarr; массив</span>
<span class="kw">const</span> saved = localStorage.getItem(<span class="st">'tasks'</span>);
<span class="kw">const</span> restored = saved ? JSON.parse(saved) : [];</div>
  </div>
  <div class="ek-note ek-note--red"><b>stringify</b> — «упаковать» в строку. <b>parse</b> — «распаковать» обратно. Без них в localStorage попадёт <span class="code-chip">[object Object]</span>.</div>
</div>"""},

    # 28 · Правка 5 — анимация (промпт)
    {"notes": "Финальная косметическая правка. Плавное появление и исчезновение задач.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 5 · анимация</div>
    <h2>Плавное появление и <span class="acc">удаление</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:6px">
    <span class="pc-tag">&rarr; В тот же чат</span>
    <div class="pc-text">Сделай анимации:
&bull; Новая задача <span class="hl">плавно появляется</span> (opacity 0 &rarr; 1, выезжает на 8px снизу) за 200мс
&bull; При удалении задача <span class="hl">плавно исчезает</span> (opacity 1 &rarr; 0, scale 1 &rarr; 0.95) за 200мс, и только потом удаляется из DOM

Используй CSS-переходы. Не трогай логику добавления/удаления — только добавь классы и переходы.

Изменения в style.css и небольшие правки в script.js. Верни изменённые блоки.</div>
  </div>
</div>"""},

    # 29 · Как работают CSS-переходы
    {"notes": "Объясните, как работает transition. Это анимация «между двумя состояниями».", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Полезное знание</div>
    <h2>Как работают <span class="acc">CSS-переходы</span></h2>
  </div>
  <p><span class="code-chip">transition</span> плавно анимирует изменение свойства между двумя состояниями.</p>
  <div class="code-win" style="margin-top:6px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">CSS</span></div>
    <div class="code-body">.task {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 200ms, transform 200ms;  <span class="cm">/* что и за сколько */</span>
}

<span class="cm">/* класс, который добавляет JS при удалении */</span>
.task.removing {
  opacity: 0;
  transform: scale(0.95);
}</div>
  </div>
  <div class="ek-note">JS только добавляет/убирает класс — всю плавность делает CSS. Это быстро и не нагружает страницу.</div>
</div>"""},
]
