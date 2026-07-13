# -*- coding: utf-8 -*-
SLIDES = [
    # 30 · ПРАВКА 5 · НАСТРОЕНИЕ И ЦВЕТ
    {"notes": "Финальная правка собирает дневник в законченный вид: появляется настроение, цветной вывод и резервная копия. Это заметный пользовательский результат, но правка сложная: mood — второй запрос к сети, а ANSI-цвета требуют аккуратности. Если группа отстаёт, оставьте только настроение, а раскраску и бэкап отдайте в ДЗ. После первой записи рядом с diary.json появится diary.bak — это резервная копия.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 5 · настроение и цвет</div>
    <h2>Настроение и <span class="acc">цвет</span></h2>
  </div>
  <div class="prompt-card prompt-card--copy" style="margin-top:6px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Финальная правка. Пусть нейросеть заодно определяет настроение записи одним словом (радость, грусть, злость или спокойствие) и сохраняет его в поле mood.

Раскрась вывод ANSI-кодами, без сторонних библиотек:
- дату — голубым
- теги — фиолетовым
- настроение — зелёным

И перед каждым сохранением делай резервную копию: скопируй diary.json в diary.bak. Верни весь файл.</div>
  </div>
</div>"""},

    # 31 · РАЗБОР · ПОЧЕМУ JSON НЕЛЬЗЯ ДОПИСЫВАТЬ
    {"notes": "Ключевой слайд урока. Подчеркните главное отличие от истории советчика: JSON нельзя дописывать режимом «a». Нужно прочитать весь список, добавить запись и записать весь список заново. Если этот шаг пропустить, файл будет ломаться.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Почему JSON нельзя <span class="acc">дописывать</span></h2>
  </div>
  <p>Новая запись добавляется в дневник в три шага — прочитать, добавить, сохранить целиком:</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">entries = load_entries()        <span class="cm"># прочитали весь список из файла</span>
entries.append(new_entry)       <span class="cm"># добавили запись в список</span>
save_entries(entries)           <span class="cm"># записали весь список заново</span></div>
  </div>
  <div class="ek-note ek-note--red">JSON <b>нельзя</b> открыть в режиме <span class="code-chip">'a'</span> и дописать словарь в конец: в файле окажется два JSON подряд, и прочитать его уже не получится. Это отличие от <span class="code-chip">history.txt</span> на уроке 5, где режим <span class="code-chip">'a'</span> работал.</div>
</div>"""},

    # 32 · КВИЗ 1 · РЕЖИМ 'a' И JSON
    {"notes": "Вопрос про режим «a» и JSON — прямое следствие предыдущего слайда. Дайте 10–15 секунд, потом раскройте ответ. Свяжите с правилом: читаем весь файл, пишем весь файл.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 1</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 1</span>
    <p class="q-text">Дима решил ускорить сохранение и открыл <span class="code-chip">diary.json</span> в режиме <span class="code-chip">'a'</span>, дописав новый словарь в конец. Программа сохранила без ошибок, но при следующем чтении упала с <span class="code-chip">JSONDecodeError</span>. Почему?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>В файле оказалось <b>два JSON подряд</b> — старый список и приписанный словарь. Это уже не валидный JSON, и <span class="code-chip">json.load</span> не может его прочитать.</p>
        <p>Правильно: прочитать весь список через <b>json.load</b>, добавить запись в список, сохранить весь список через <b>json.dump</b>.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 33 · КВИЗ 2 · ENSURE_ASCII
    {"notes": "Вопрос про ensure_ascii — вторая частая ошибка с JSON и русским текстом. Свяжите с правилом: для русского текста используем ensure_ascii=False.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 2</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 2</span>
    <p class="q-text">Настя записала «Выиграл турнир по шахматам», открыла <span class="code-chip">diary.json</span>, а там вместо слова «шахматы» — набор кодов вида <span class="code-chip">шах...</span>. Программа работает, но файл нечитаем. Что она забыла?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>Параметр <b>ensure_ascii=False</b> в <span class="code-chip">json.dump</span>. Без него русские буквы сохраняются как коды <span class="code-chip">\uXXXX</span>.</p>
        <p>С <span class="code-chip">ensure_ascii=False</span> в файле остаётся читаемый русский текст.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 34 · ОТЛАДКА · ЧИТАЕМ ОШИБКИ JSON
    {"notes": "Научите читать traceback снизу вверх — это пригодится на всех уроках Python. Напомните правило: непонятную ошибку целиком копируем в DeepSeek. Три проверки справа — самые частые именно в дневнике.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Отладка</div>
    <h2>Читаем <span class="acc">ошибки JSON</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div>
      <div class="term">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
        <div class="term-body">Traceback (most recent call last):
  File "diary.py", line 8, in load_entries
    return json.load(f)
<span class="usr">json.decoder.JSONDecodeError: Expecting value</span></div>
      </div>
      <p style="margin-top:8px"><b>Снизу вверх:</b> последняя строка — <span class="hl">что</span> случилось, строкой выше — <span class="hl">где</span>. <span class="code-chip">JSONDecodeError</span> значит: файл пустой или повреждён.</p>
    </div>
    <div>
      <div class="info-card">
        <h3>Если застряли</h3>
        <ul class="clean">
          <li>Скопируйте <b>traceback целиком</b> в чат DeepSeek — попросите объяснить и починить.</li>
          <li>Проверьте <span class="code-chip">ensure_ascii=False</span> и режим <span class="code-chip">'w'</span> при сохранении.</li>
          <li>Откройте <span class="code-chip">diary.json</span> глазами — валиден ли он.</li>
        </ul>
      </div>
      <p style="margin-top:8px">Тот же подход, что <span class="code-chip">console.log</span> в «Змейке» и print-метки на уроке 5.</p>
    </div>
  </div>
</div>"""},

    # 35 · ПРАВИЛА РАБОТЫ С ДАННЫМИ
    {"notes": "5 правил урока. Дайте сфотографировать слайд. Особо подчеркните второе: читаем весь файл, пишем весь файл — это главное про JSON.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запомните</div>
    <h2>Правила работы с <span class="acc">данными</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">01 · JSON — список словарей</div><div class="v">Структурированные данные вместо плоских строк: их можно искать и разбирать.</div></div>
    <div class="kv-row"><div class="k">02 · Читай весь, пиши весь</div><div class="v">JSON меняем так: <span class="code-chip">load</span> → изменили список → <span class="code-chip">dump</span>. Режим <span class="code-chip">'a'</span> не подходит.</div></div>
    <div class="kv-row"><div class="k">03 · ensure_ascii=False</div><div class="v">Всегда для русского текста, иначе в файле будут коды <span class="code-chip">\uXXXX</span>.</div></div>
    <div class="kv-row"><div class="k">04 · Ключ — это пароль</div><div class="v">Не публикуем, на скриншотах замазываем. На уроке 8 спрячем его в <span class="code-chip">.env</span>.</div></div>
    <div class="kv-row"><div class="k">05 · AI помогает с разметкой</div><div class="v">Нейросеть читает запись и подбирает теги — программа получает дополнительные данные для поиска.</div></div>
  </div>
</div>"""},

    # 36 · ЧЕК-ЛИСТ
    {"notes": "Чек-лист завершения дневника. Кто отметил всё, пусть напишет три записи и найдёт их по тегу. Это проверяет, что структура работает.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Чек-лист</div>
    <h2>Готовность <span class="acc">к 55-й минуте</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div class="info-card">
      <h3>Готово</h3>
      <ul class="clean">
        <li><span class="code-chip">diary.py</span> запускается командой <span class="code-chip">python diary.py</span></li>
        <li>Новая запись сохраняется в <span class="code-chip">diary.json</span></li>
        <li>Нейросеть подбирает теги к записи</li>
        <li>Настроение определяется автоматически</li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Работает</h3>
      <ul class="clean">
        <li>Пункт «показать все» печатает записи</li>
        <li>Поиск по тегу находит нужные записи</li>
        <li>Вывод цветной</li>
        <li>Есть резервная копия <span class="code-chip">diary.bak</span></li>
      </ul>
    </div>
  </div>
  <div class="ek-note ek-note--green">Всё отмечено? Напишите три записи и найдите их по тегу — дневник готов.</div>
</div>"""},

    # 37 · ДОМАШНЕЕ ЗАДАНИЕ
    {"notes": "ДЗ — доработать дневник, примерно 30 минут. Каждое улучшение — отдельный диалог с DeepSeek, не всё сразу. Напомните про ключ на скриншотах.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Домашнее задание · около 30 минут</div>
    <h2>Доработайте <span class="acc">дневник</span></h2>
  </div>
  <p>Три улучшения — каждое через отдельный диалог с DeepSeek:</p>
  <div class="grid-3" style="margin-top:6px">
    <div class="info-card">
      <h3>Статистика тегов</h3>
      <p>Добавьте пункт меню, который считает, сколько раз встречается каждый тег, и печатает топ самых частых.</p>
    </div>
    <div class="info-card">
      <h3>Экспорт в Markdown</h3>
      <p>Пункт «сохранить в <span class="code-chip">diary.md</span>»: все записи красивым текстом — заголовки с датой и списки тегов.</p>
    </div>
    <div class="info-card">
      <h3>Умный поиск</h3>
      <p>Пусть поиск находит записи не только по точному тегу, но и по слову в тексте записи.</p>
    </div>
  </div>
  <div class="ek-note ek-note--red">Пришлите скриншот дневника с записями — <b>ключ скройте!</b> Ваш самый удачный промпт — отдельным сообщением.</div>
</div>"""},

    # 38 · ФИНАЛ
    {"cls": "slide--green", "notes": "Закройте урок. Сегодня программа научилась хранить данные структурированно и размечать записи с помощью нейросети. На уроке 8 — внешние API, погода, AI-комментарии и безопасное хранение ключа в .env.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">J</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">S</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">O</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">N</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="bubble">
      <h1>До встречи<br>на уроке 8!</h1>
      <p>Сегодня программа научилась хранить данные структурированно в JSON и размечать записи AI-тегами и настроением. На уроке 8 выйдем в интернет: программа получит погоду из внешнего сервиса, нейросеть её прокомментирует, а ключи спрячем в файл .env.</p>
    </div>
  </div>"""},
]
