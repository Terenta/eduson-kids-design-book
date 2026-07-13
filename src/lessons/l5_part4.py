# -*- coding: utf-8 -*-
SLIDES = [
    # 30 · ПРАВКА 5 · ЦВЕТ В ТЕРМИНАЛЕ
    {"notes": "Последняя правка — косметика. Цвета сразу видны: советчик начинает выглядеть как настоящий продукт. Дождитесь, пока все запустят, потом идём к разбору.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Правка 5 · цвет в терминале</div>
    <h2>Раскрашиваем <span class="acc">советчика</span></h2>
  </div>
  <p>Советчик работает — теперь наведём красоту. Одна правка ANSI-кодами, и вывод оживёт цветом, без единой сторонней библиотеки.</p>
  <div class="prompt-card prompt-card--copy" style="margin-top:12px">
    <span class="pc-tag">→ В тот же чат</span>
    <div class="pc-text">Раскрась вывод советчика ANSI-кодами, <span class="hl">без сторонних библиотек</span>:
- Приветствие — фиолетовым
- Вопросы пользователю — голубым
- Ответ нейросети — <span class="hl">зелёным и жирным</span>
- Прощание — обычным цветом

Заведи в начале файла константы вроде VIOLET = '\033[35m'
и RESET = '\033[0m' и подставляй их в print через f-строки.

Верни весь обновлённый advisor.py.</div>
  </div>
</div>"""},

    # 31 · РАЗБОР · КАК ТЕРМИНАЛ ПОНИМАЕТ ЦВЕТ
    {"notes": "Разбор цветов. Покажите: пять констант в начале файла, дальше обычные f-строки. Если у кого-то цвета не появились — пусть проверит, что запускает программу во встроенном терминале VS Code.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор кода</div>
    <h2>Как терминал понимает <span class="acc">цвет</span></h2>
  </div>
  <p>Терминал следит за <span class="hl">специальными последовательностями</span> в тексте: <span class="code-chip">\033[35m</span> переключает цвет, <span class="code-chip">\033[0m</span> возвращает обычный. Удобно завести константы в начале файла:</p>
  <div class="code-win" style="margin-top:10px">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body">VIOLET = <span class="st">'\033[35m'</span>   <span class="cm"># фиолетовый</span>
CYAN   = <span class="st">'\033[96m'</span>   <span class="cm"># ярко-голубой</span>
GREEN  = <span class="st">'\033[92m'</span>   <span class="cm"># ярко-зелёный</span>
BOLD   = <span class="st">'\033[1m'</span>    <span class="cm"># жирный</span>
RESET  = <span class="st">'\033[0m'</span>    <span class="cm"># вернуть обычный вид</span>

print(f<span class="st">"{GREEN}{BOLD}Совет:{RESET}"</span>)</div>
  </div>
  <div class="ek-note ek-note--red">Работает во встроенном терминале VS Code. В старых системных консолях цвета могут не появиться — это <b>не ошибка вашего кода</b>.</div>
</div>"""},

    # 32 · КВИЗ 1 · РАЗНЫЕ ОТВЕТЫ
    {"notes": "Вопрос про природу нейросети. Дайте 10–15 секунд подумать, потом раскройте ответ. Это ключевое отличие от программ с заготовками — нейросеть генерирует текст заново.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 1</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 1</span>
    <p class="q-text">Маша задала советчику один и тот же вопрос два раза подряд — и получила два разных ответа. Серёжа говорит: «У тебя в программе ошибка». Прав ли он?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>Нет. Нейросеть <b>не достаёт ответ из готового списка</b> — она генерирует текст заново при каждом запросе, поэтому формулировки отличаются.</p>
        <p>Так работает и чат DeepSeek: задайте одинаковый вопрос дважды — получите разные ответы. Нейросеть каждый раз заново формулирует ответ.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 33 · КВИЗ 2 · РЕЖИМ ФАЙЛА
    {"notes": "Вопрос про режимы открытия файла. Частая ошибка — w вместо a. Свяжите с дневником: дневник не переписывают с нуля каждый день.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Проверка · вопрос 2</div>
    <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
  </div>
  <div class="quiz-box">
    <span class="q-num">Вопрос 2</span>
    <p class="q-text">Алина решила «улучшить» сохранение истории и поменяла режим открытия файла с <span class="code-chip">'a'</span> на <span class="code-chip">'w'</span>. Ошибок нет, но после каждого запуска в history.txt остаётся только последняя запись. Почему?</p>
    <div class="quiz-answer">
      <button class="quiz-btn" type="button">Показать ответ</button>
      <div class="quiz-reveal">
        <p>Режим <b>'w'</b> каждый раз создаёт файл заново и <b>стирает старое содержимое</b>. Для дневника нужен режим <b>'a'</b> — append, дозапись в конец файла.</p>
      </div>
    </div>
  </div>
</div>"""},

    # 34 · ОТЛАДКА · ЧИТАЕМ ОШИБКИ
    {"notes": "Научите читать traceback снизу вверх — это пригодится на всех уроках Python. Напомните привычку из «Змейки»: непонятная ошибка целиком уходит в DeepSeek. И новое: странные ответы нейросети чинятся в системной роли.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Отладка</div>
    <h2>Читаем <span class="acc">ошибки Python</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div>
      <h3 style="font:800 15px/1 var(--f-head);margin-bottom:8px">Traceback — снизу вверх</h3>
      <div class="term">
        <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
        <div class="term-body">Traceback (most recent call last):
  File "advisor.py", line 12, in &lt;module&gt;
    print(advise)
<span class="usr">NameError: name 'advise' is not defined</span></div>
      </div>
      <p style="font-size:13.5px;margin-top:8px;opacity:.75">Последняя строка — <b>что</b> случилось, строкой выше — <b>где</b>.</p>
    </div>
    <div>
      <h3 style="font:800 15px/1 var(--f-head);margin-bottom:8px">Если застряли</h3>
      <ul class="clean">
        <li><b>Ошибка непонятна</b> — скопируйте traceback целиком в чат DeepSeek и попросите объяснить и починить</li>
        <li><b>Программа молчит</b> — добавьте print-метки, чтобы увидеть, докуда дошло выполнение</li>
        <li><b>Ответ нейросети странный</b> — проблема почти всегда в системной роли: перечитайте её текст</li>
      </ul>
    </div>
  </div>
</div>"""},

    # 35 · ПРИВЫЧКИ РАЗРАБОТЧИКА
    {"notes": "5 привычек разработчика с нейросетью. Дайте сфотографировать слайд. Особо подчеркните первую: ключ — это пароль.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запомните</div>
    <h2>Привычки разработчика <span class="acc">с нейросетью</span></h2>
  </div>
  <div class="kv">
    <div class="kv-row"><div class="k">01 · Ключ — это пароль</div><div class="v">Не публикуем, не показываем на скриншотах. Утёк — перевыпускаем.</div></div>
    <div class="kv-row"><div class="k">02 · Промпт живёт в коде</div><div class="v">Системная роль решает, каким будет ответ. Меняешь её — меняется программа.</div></div>
    <div class="kv-row"><div class="k">03 · Терминал — друг</div><div class="v">Любой скрипт: <span class="code-chip">python имя_файла.py</span>. Библиотеки: <span class="code-chip">pip install</span>.</div></div>
    <div class="kv-row"><div class="k">04 · input → строка</div><div class="v">Всё из input приходит текстом. Число достаём через <span class="code-chip">int(...)</span>.</div></div>
    <div class="kv-row"><div class="k">05 · with open</div><div class="v">Файлы открываем только так — закроется сам. Режим <span class="code-chip">'a'</span> — дозапись.</div></div>
  </div>
</div>"""},

    # 36 · ЧЕК-ЛИСТ
    {"notes": "Чек-лист завершения советчика. Кто отметил всё — пусть даст соседу задать вопрос своему советчику и сравнит характеры.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Чек-лист</div>
    <h2>Готовность <span class="acc">к 55-й минуте</span></h2>
  </div>
  <div class="grid-2" style="margin-top:6px">
    <div>
      <h3 style="font:800 15px/1 var(--f-head);margin-bottom:10px">Готово</h3>
      <ul class="clean">
        <li><span class="code-chip">advisor.py</span> запускается командой <span class="code-chip">python advisor.py</span></li>
        <li>Советчик здоровается по имени</li>
        <li>Характер выбирается при запуске и реально меняет тон</li>
      </ul>
    </div>
    <div>
      <h3 style="font:800 15px/1 var(--f-head);margin-bottom:10px">Работает</h3>
      <ul class="clean">
        <li>Диалог идёт по кругу, пока не введёте «выход»</li>
        <li>Ответы генерирует нейросеть DeepSeek — не заготовки</li>
        <li>История дописывается в <span class="code-chip">history.txt</span> с датой</li>
        <li>Вывод цветной</li>
      </ul>
    </div>
  </div>
  <div class="ek-note ek-note--green">Всё отмечено? Дайте соседу задать вашему советчику вопрос — и сравните характеры.</div>
</div>"""},

    # 37 · ДОМАШНЕЕ ЗАДАНИЕ
    {"notes": "ДЗ — прокачать советчика, примерно 30 минут. Каждое улучшение — отдельный диалог с DeepSeek, не всё сразу. Напомните про ключ на скриншотах.", "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Домашнее задание · около 30 минут</div>
    <h2>Прокачайте <span class="acc">советчика</span></h2>
  </div>
  <p>Три улучшения — каждое через отдельный диалог с DeepSeek:</p>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card">
      <h3>Свой характер</h3>
      <p>Придумайте четвёртый характер — мудрый дедушка или капитан космического корабля — и добавьте в меню. Проверьте, как меняются ответы.</p>
    </div>
    <div class="info-card">
      <h3>Память разговора</h3>
      <p>Советчик забывает каждый вопрос. Попросите DeepSeek хранить прошлые сообщения в списке <span class="code-chip">messages</span> и слать их вместе с новым — советчик начнёт помнить разговор.</p>
    </div>
    <div class="info-card">
      <h3>ASCII-логотип</h3>
      <p>При старте советчик рисует надпись СОВЕТЧИК псевдографикой — попросите DeepSeek сгенерировать.</p>
    </div>
  </div>
  <div class="ek-note ek-note--red">Пришлите скриншот терминала с диалогом — <b>ключ скройте!</b> Ваш самый удачный промпт — отдельным сообщением.</div>
</div>"""},

    # 38 · ФИНАЛ
    {"cls": "slide--green", "notes": "Закройте урок. Сегодня двойной прорыв: первый Python-скрипт и первая программа с нейросетью внутри. На уроке 6 — циклы и функции, текстовая игра-приключение с сюжетом от нейросети.", "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">P</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">Y</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">I</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">A</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="bubble">
      <h1>До встречи<br>на уроке 6!</h1>
      <p>Сегодня двойной прорыв: первый Python-скрипт и первая программа с нейросетью внутри — input, API, системная роль, цикл, файлы, цвета. На уроке 6 берём циклы и функции по-настоящему: соберём текстовую игру-приключение, где сюжет на лету генерирует нейросеть.</p>
    </div>
  </div>"""},
]
