# -*- coding: utf-8 -*-
SLIDES = [
    # 30 · КВИЗ 1 — инкогнито и localStorage
    {"notes": "Простой вопрос. Подождите 10–15 секунд, потом раскройте ответ.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 1</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 1</span>
    <p class="q-text">Вы добавили в localStorage 5 задач. Открыли тот же сайт в режиме «инкогнито» — задач там нет. Почему?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>Режим «инкогнито» использует <b>отдельное</b> хранилище. Когда вы закрываете окно инкогнито, всё содержимое localStorage очищается. Так браузер защищает приватность.</p>
        <p>В обычной вкладке localStorage сохраняется, пока пользователь сам его не очистит.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 31 · КВИЗ 2 — скрипт в head, null
    {"notes": "Второй вопрос — про скрипт в head. Частая ошибка.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 2</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 2</span>
    <p class="q-text">Кнопка «Добавить» не реагирует на клик. В консоли — ошибка <span class="code-chip">Cannot read properties of null</span> на строке <span class="code-chip">addBtn.addEventListener(...)</span>. В чём причина?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>Скрипт подключён в <span class="code-chip">&lt;head&gt;</span> и выполняется <b>до</b> того, как браузер построил кнопку. <span class="code-chip">getElementById('add')</span> вернул <span class="out-chip">null</span> — кнопки ещё нет.</p>
        <p>Решение: перенести <span class="code-chip">&lt;script src="script.js"&gt;&lt;/script&gt;</span> в самый конец <span class="code-chip">&lt;body&gt;</span>.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 32 · Console — инструмент отладки
    {"notes": "Научите открывать DevTools. F12 → Console. Это главный инструмент отладки.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Инструмент отладки</div>
    <h2>Console — главный <span class="acc">друг</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div class="info-card">
      <h3>Как открыть</h3>
      <ol class="steps steps--tight">
        <li>В браузере нажмите <span class="code-chip">F12</span></li>
        <li>Перейдите на вкладку <b>Console</b></li>
        <li>Красные строки — ошибки в коде</li>
      </ol>
    </div>
    <div>
      <div class="code-win">
        <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">JAVASCRIPT</span></div>
        <div class="code-body">console.log(<span class="st">'Кнопка нажата'</span>);
console.log(<span class="st">'Сейчас задач:'</span>, tasks.length);
console.log(tasks);   <span class="cm">// покажет весь массив</span></div>
      </div>
      <div class="ek-note" style="margin-top:12px">Если непонятно, что происходит — печатайте состояние.</div>
    </div>
  </div>
</div>"""},

    # 33 · Шпаргалка: событие не срабатывает
    {"notes": "Шпаргалка по проблемам с событиями.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Если событие не срабатывает</div>
    <h2>Типичные <span class="acc">ситуации</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">кнопка не реагирует</div><div class="v">Скрипт в <span class="code-chip">&lt;head&gt;</span> и выполняется до DOM. Перенесите <span class="code-chip">&lt;script&gt;</span> в конец <span class="code-chip">&lt;body&gt;</span>.</div></div>
    <div class="kv-row"><div class="k">Cannot read of null</div><div class="v">id в HTML и в JS не совпадают. Проверьте написание.</div></div>
    <div class="kv-row"><div class="k">localStorage пустой</div><div class="v">Сохраняли через Live Server, открыли через <span class="code-chip">file://</span>. Это разные хранилища — используйте Live Server везде.</div></div>
    <div class="kv-row"><div class="k">удаляется всё сразу</div><div class="v">Обработчик на родителе вместо самой кнопки. Скопируйте код в DeepSeek с вопросом «почему все элементы удаляются?».</div></div>
  </div>
</div>"""},

    # 34 · Привычки урока (kv)
    {"notes": "5 привычек урока. Дайте сфотографировать.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запомните</div>
    <h2>Полезные <span class="acc">привычки</span> на сегодня</h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">01 · DOM = карта</div><div class="v">Каждый видимый элемент доступен из JS через id или querySelector.</div></div>
    <div class="kv-row"><div class="k">02 · События — сигналы</div><div class="v">click, input, change. Браузер сам отправляет, JS подписывается через addEventListener.</div></div>
    <div class="kv-row"><div class="k">03 · Скрипт — в конце body</div><div class="v">Так JS запускается после построения страницы, элементы уже доступны.</div></div>
    <div class="kv-row"><div class="k">04 · localStorage хранит строки</div><div class="v">Объекты и массивы — через <span class="code-chip">JSON.stringify</span> / <span class="code-chip">JSON.parse</span>.</div></div>
    <div class="kv-row"><div class="k">05 · Console — друг</div><div class="v">F12 → Console показывает ошибки и сообщения <span class="code-chip">console.log</span>.</div></div>
  </div>
</div>"""},

    # 35 · Чек-лист к 55-й минуте
    {"notes": "Чек-лист завершения. Пройдите по пунктам, ученики поднимают руку, если готово.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Финальная проверка</div>
    <h2>Готовность <span class="acc">к 55-й минуте</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div class="info-card">
      <h3>Готово</h3>
      <ul class="clean">
        <li>Папка <span class="code-chip">lesson-03</span> с 3 файлами</li>
        <li>Список открывается через Live Server</li>
        <li>Задачи добавляются по кнопке</li>
        <li>Каждая задача удаляется по «×»</li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Работает</h3>
      <ul class="clean">
        <li>Чекбокс зачёркивает задачу</li>
        <li>После перезагрузки задачи на месте</li>
        <li>Появление и удаление плавное</li>
        <li>Прошло минимум 4 правки через диалог</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 36 · Домашнее задание
    {"notes": "ДЗ — расширения списка. Каждое — отдельная правка через диалог.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Домашнее задание · около 30 минут</div>
    <h2>Расширьте свой <span class="acc">список</span></h2>
  </div>
  <p>Через диалог с DeepSeek добавьте три функции:</p>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card">
      <h3>Приоритеты</h3>
      <p>У каждой задачи — выпадающий список «Низкий / Средний / Высокий». Высокий — красная метка слева.</p>
    </div>
    <div class="info-card">
      <h3>Фильтр</h3>
      <p>Кнопки сверху: «Все / Активные / Выполненные». При клике показываются только нужные задачи.</p>
    </div>
    <div class="info-card">
      <h3>Счётчик</h3>
      <p>Внизу: «Осталось задач: N». Цифра обновляется при отметке выполненных.</p>
    </div>
  </div>
  <div class="ek-note ek-note--green" style="margin-top:14px">Пришлите скриншот списка с задачами и ваш самый удачный промпт за это задание.</div>
</div>"""},

    # 37 · Шпаргалка «что делать, если…»
    {"notes": "Расширенная шпаргалка по проблемам. Держите под рукой на следующих уроках.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Шпаргалка</div>
    <h2>Что делать, <span class="acc">если…</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">страница белая</div><div class="v">Файл не сохранён или пустой. <span class="code-chip">Ctrl+S</span> и проверьте код.</div></div>
    <div class="kv-row"><div class="k">кнопка молчит</div><div class="v">Скрипт в head или id не совпадает. Скрипт — в конец body.</div></div>
    <div class="kv-row"><div class="k">задачи пропали</div><div class="v">Открыли через file:// вместо Live Server. Запускайте через Live Server.</div></div>
    <div class="kv-row"><div class="k">в хранилище мусор</div><div class="v">Забыли <span class="code-chip">JSON.stringify</span> / <span class="code-chip">parse</span>. Отдайте код в DeepSeek.</div></div>
    <div class="kv-row"><div class="k">нейросеть переписала всё</div><div class="v">Промпт без «оставь всё как есть». Переформулируйте на точечную правку.</div></div>
  </div>
</div>"""},

    # 38 · ФИНАЛ (green bubble)
    {"cls": "slide--green", "notes": "Закройте урок. Следующий — собственная игра в браузере на Canvas.", "html": r"""<div class="sl-orbit">
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
      <h1>До встречи<br>на уроке 4!</h1>
      <p>Сегодня страница научилась отвечать на действия: список задач добавляет, удаляет, отмечает выполненное и не теряется при перезагрузке. На уроке 4 — своя браузерная игра: холст Canvas, движение и игровой цикл.</p>
    </div>
  </div>"""},
]
