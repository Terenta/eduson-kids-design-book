# -*- coding: utf-8 -*-
SLIDES = [
    # 12 · Готовый промпт для первого сайта
    {"notes": "Это слайд-шпаргалка. Каждый ученик копирует промпт целиком, заменяет {ИМЯ} на своё и отправляет в DeepSeek.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #1 · копируем целиком</div>
    <h2>Готовый промпт для <span class="acc">первого сайта</span></h2>
  </div>
  <p>Скопируйте промпт целиком, замените <span class="code-chip">{ИМЯ}</span> на своё имя и отправьте в DeepSeek.</p>
  <div class="prompt-card" style="margin-top:12px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты опытный веб-разработчик. Напиши HTML-страницу «Обо мне».

Условия:
- Один файл index.html, всё внутри (HTML и CSS в теге &lt;style&gt;)
- Сверху — большой заголовок с моим именем (вместо имени поставь {ИМЯ})
- Под заголовком — короткий абзац: где учусь, чем увлекаюсь
- Внизу — кнопка «Связаться», при наведении меняет цвет
- Цвета — тёмная тема: фон #0F172A, акцент фиолетовый
- Шрифт — Inter из Google Fonts
- Без JavaScript, без внешних библиотек

Ответь готовым кодом, который я могу скопировать в один файл и открыть в браузере.</div>
  </div>
</div>"""},

    # 13 · Перенесите код в проект
    {"notes": "Покажите на проекторе: жмём Copy в DeepSeek, идём в VS Code, выделяем всё (Ctrl+A), вставляем (Ctrl+V), сохраняем (Ctrl+S).", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Из чата → в файл</div>
    <h2>Перенесите код <span class="acc">в проект</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div>
      <h3>Из DeepSeek в VS Code</h3>
      <ol class="steps steps--tight">
        <li>В ответе DeepSeek нажмите кнопку <b>Copy</b> над блоком кода</li>
        <li>Вернитесь в VS Code, в файл <span class="code-chip">index.html</span></li>
        <li>Выделите всё: <span class="code-chip">Ctrl+A</span></li>
        <li>Удалите: <span class="code-chip">Delete</span></li>
        <li>Вставьте код: <span class="code-chip">Ctrl+V</span></li>
        <li>Сохраните: <span class="code-chip">Ctrl+S</span></li>
      </ol>
    </div>
    <div>
      <h3>Запуск в браузере</h3>
      <ol class="steps steps--tight">
        <li>В правом нижнем углу VS Code появится кнопка <b>Go Live</b></li>
        <li>Нажмите её</li>
        <li>Откроется браузер — там ваша страница</li>
      </ol>
      <div class="ek-note ek-note--red" style="margin-top:10px">Если кнопки «Go Live» нет — правый клик по <span class="code-chip">index.html</span> и выберите <b>Open with Live Server</b>.</div>
    </div>
  </div>
</div>"""},

    # 14 · Первый запуск: типичные ситуации
    {"notes": "Самые частые проблемы при первом запуске. Помните: 90% случаев решаются проверкой сохранения и пересмотром скопированного.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Если что-то пошло не так</div>
    <h2>Первый запуск: <span class="acc">типичные ситуации</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div class="ek-note ek-note--red">
      <h3>Страница белая</h3>
      <ul class="clean">
        <li>Проверьте, что файл сохранён (звёздочка рядом с именем означает «не сохранено»)</li>
        <li>Проверьте, что в файле есть код, а не пустота</li>
        <li>Если попался лишний текст — оставьте только содержимое между <span class="code-chip">```html</span> и <span class="code-chip">```</span></li>
      </ul>
    </div>
    <div class="ek-note ek-note--red">
      <h3>Live Server не запускается</h3>
      <ul class="clean">
        <li>Проверьте, что расширение установлено и активно</li>
        <li>Закройте лишние проекты, которые могли занять порт</li>
        <li>Перезапустите VS Code</li>
      </ul>
    </div>
  </div>
  <div class="ek-note" style="margin-top:12px">Если страница выдала ошибку — скопируйте текст ошибки и отправьте в DeepSeek с вопросом «как исправить?». Обычно нейросеть сразу предлагает рабочую правку.</div>
</div>"""},

    # 15 · Три правки через сообщения
    {"notes": "Покажите на одном ученике 3 правки, остальные параллельно делают свои. Главная мысль: не редактируйте код руками — попросите нейросеть.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Доработка через диалог</div>
    <h2>Три правки <span class="acc">через сообщения</span></h2>
  </div>
  <div class="grid-3" style="margin-top:6px">
    <div class="info-card">
      <span class="chip">Правка 1</span>
      <h3 style="margin-top:8px">Кнопка</h3>
      <p>«Сделай кнопку фиолетового цвета #7C3AED. При наведении пусть слегка увеличивается и появляется тень.»</p>
    </div>
    <div class="info-card">
      <span class="chip chip--gray">Правка 2</span>
      <h3 style="margin-top:8px">Аватарка</h3>
      <p>«Добавь круглую аватарку 120×120 пикселей сверху. Картинку возьми с api.dicebear.com/7.x/avataaars/svg?seed={имя}.»</p>
    </div>
    <div class="info-card">
      <span class="chip chip--green">Правка 3</span>
      <h3 style="margin-top:8px">Анимация</h3>
      <p>«Добавь плавное появление элементов при загрузке: выезжают снизу с задержкой 0.2 сек. между блоками. Чистый CSS, без JavaScript.»</p>
    </div>
  </div>
  <div class="ek-note" style="margin-top:12px">Алгоритм каждой правки одинаковый: пишете правку → копируете новый код → заменяете содержимое <span class="code-chip">index.html</span> → сохраняете. Live Server обновит страницу сам.</div>
</div>"""},

    # 16 · Квиз: белая страница
    {"notes": "Простой вопрос для проверки понимания. Подождите 10–15 секунд, потом разберите варианты ответов.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос</span>
    <p class="q-text">Вы скопировали код из DeepSeek в файл <span class="code-chip">index.html</span>, нажали Ctrl+S, открыли через Live Server — и видите белую страницу. Какие три причины самые вероятные?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>1. Файл сохранён под другим именем (например, <span class="code-chip">index.txt</span>) — Live Server не воспринимает его как HTML.</p>
        <p>2. В файл попал лишний текст-подпись — браузер не распознал его как валидный HTML.</p>
        <p>3. Файл сохранён, но был пуст — содержимое не было вставлено.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 17 · Полезные привычки вайб-кодера
    {"notes": "Это слайд для запоминания. Дайте ученикам сфоткать. 5 привычек, которые помогут на весь курс.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запомните</div>
    <h2>Полезные привычки <span class="acc">вайб-кодера</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">01 · Точность</div><div class="v">Чем точнее формулируете задачу, тем точнее результат. Указывайте числа, имена цветов, конкретные URL.</div></div>
    <div class="kv-row"><div class="k">02 · Маленькие шаги</div><div class="v">Лучше пять последовательных правок, чем один промпт «сделай идеально». На небольших шагах проще сохранять контроль.</div></div>
    <div class="kv-row"><div class="k">03 · Ошибка → диалог</div><div class="v">Если результат не работает, скопируйте ошибку и отправьте в чат. Нейросеть подскажет, как починить.</div></div>
    <div class="kv-row"><div class="k">04 · Копилка промптов</div><div class="v">Удачные формулировки складывайте в файл <span class="code-chip">prompts.md</span> в папке курса. Это поможет на следующих уроках.</div></div>
    <div class="kv-row"><div class="k">05 · Запуск после правки</div><div class="v">После каждой правки открывайте страницу в браузере. Видеть результат важнее, чем читать код.</div></div>
  </div>
</div>"""},

    # 18 · Финальная проверка
    {"notes": "Чек-лист для проверки. Пройдите по каждому пункту, ученики поднимают руку, если готово.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Финальная проверка</div>
    <h2>Готовность <span class="acc">к 55-й минуте</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div>
      <h3>Установлено</h3>
      <ul class="clean">
        <li>VS Code запускается</li>
        <li><span class="code-chip">python --version</span> отвечает в терминале</li>
        <li>Расширение Live Server активно</li>
        <li>Аккаунт DeepSeek работает</li>
      </ul>
    </div>
    <div>
      <h3>Сделано</h3>
      <ul class="clean">
        <li>Папка <span class="code-chip">D:/vibe-coding/lesson-01/</span></li>
        <li>В ней файл <span class="code-chip">index.html</span></li>
        <li>Сайт открывается в браузере</li>
        <li>Прошли минимум 3 правки через диалог</li>
        <li>На странице есть аватарка, кнопка, анимация</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 19 · Домашнее задание
    {"notes": "ДЗ — около 30 минут. Прислать скриншот сайта и скриншот диалога. По диалогу видно, как ученик формулирует.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Домашнее задание · около 30 минут</div>
    <h2>Доделайте свою <span class="acc">страницу</span></h2>
  </div>
  <p>Через диалог с DeepSeek добавьте к сайту 3 секции:</p>
  <div class="grid-3" style="margin-top:6px">
    <div class="info-card">
      <h3>Мои хобби</h3>
      <p>Горизонтальный ряд из 3 карточек: иконка, название, краткое описание.</p>
    </div>
    <div class="info-card">
      <h3>Мои проекты</h3>
      <p>Список из 2–3 пунктов: название и ссылка.</p>
    </div>
    <div class="info-card">
      <h3>Контакты</h3>
      <p>Telegram и email, оформленные как кликабельные ссылки.</p>
    </div>
  </div>
  <div class="ek-note ek-note--red" style="margin-top:12px">Пришлите в чат: скриншот итогового сайта + скриншот всего диалога с DeepSeek. Скриншот диалога важнее самого сайта — по нему видно, как вы формулируете промпты.</div>
</div>"""},

    # 20 · Шпаргалка по проблемам
    {"notes": "Этот слайд держите под рукой во время практики. Указывайте на него, когда у кого-то возникает проблема.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Шпаргалка по проблемам</div>
    <h2>Если возникнет <span class="acc">ситуация…</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">python не работает</div><div class="v">Пропущена галочка <span class="code-chip">Add to PATH</span>. Переустановите Python с этой галочкой.</div></div>
    <div class="kv-row"><div class="k">страница белая</div><div class="v">Файл не сохранён или пустой. Нажмите <span class="code-chip">Ctrl+S</span> и проверьте, что в нём есть код.</div></div>
    <div class="kv-row"><div class="k">DeepSeek по-английски</div><div class="v">В первом промпте напишите: «Отвечай на русском».</div></div>
    <div class="kv-row"><div class="k">Лишний текст в файле</div><div class="v">Берите только содержимое блока кода — между <span class="code-chip">```html</span> и <span class="code-chip">```</span>.</div></div>
    <div class="kv-row"><div class="k">Live Server не работает</div><div class="v">Перезапустите VS Code, проверьте во вкладке Extensions, что расширение Enabled.</div></div>
  </div>
</div>"""},

    # 21 · Итог урока
    {"notes": "Резюмируйте: за 60 минут — установка инструментов, первый сайт, 3 правки. Главное — у каждого появилась привычка вести диалог с нейросетью.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Итог урока</div>
    <h2>Что у вас есть <span class="acc">прямо сейчас</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div class="ek-note ek-note--green">
      <h3>Среда разработчика</h3>
      <p>VS Code, Python, Live Server, DeepSeek. Все инструменты установлены и готовы к использованию.</p>
    </div>
    <div class="ek-note ek-note--green">
      <h3>Первый сайт</h3>
      <p>Файл <span class="code-chip">index.html</span> открывается в браузере и выглядит аккуратно.</p>
    </div>
    <div class="ek-note ek-note--green">
      <h3>Алгоритм работы</h3>
      <p>Формулируете задачу → получаете код → запускаете → правите через диалог.</p>
    </div>
    <div class="ek-note ek-note--green">
      <h3>Полезные привычки</h3>
      <p>Точность, маленькие шаги, отправка ошибок в чат, копилка промптов, проверка в браузере.</p>
    </div>
  </div>
</div>"""},

    # 22 · Финал
    {"cls": "slide--green", "notes": "Закройте урок. Расскажите коротко, что будет на следующем уроке: разделение на 3 файла и продвинутый промтинг.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">H</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">T</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">M</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">L</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="bubble">
      <h1>До встречи<br>на уроке 2!</h1>
      <p>Сегодня установили инструменты, собрали первый сайт «Обо мне» и сделали 3 правки через диалог. На следующем уроке: разделение проекта на 3 файла (HTML, CSS, JS), пять техник промтинга и карточка любимого персонажа с интерактивными эффектами.</p>
    </div>
  </div>"""},
]
