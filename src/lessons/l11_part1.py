# -*- coding: utf-8 -*-
SLIDES = [
    # 1 · ТИТУЛ
    {"cls": "slide--violet",
     "notes": "Поприветствуйте. Сегодня соберём генератор статей: называете тему — нейросеть пишет статью с заголовком и разделами. Новое — переходим с ручного requests на аккуратный openai SDK и учимся управлять двумя настройками: temperature и max_tokens. К концу урока у каждого — рабочий writer.py в терминале.",
     "html": r"""<div class="sl-orbit">
    <i class="sl-ring"></i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:75px;top:20px;width:150px;height:150px;transform:rotate(-10deg)"><use href="#ek-i-trophy"/></svg>
    <i class="sl-letter" style="left:466px;top:13px;width:78px;height:78px;--fs:36px">A</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1040px;top:15px;width:130px;height:130px;transform:rotate(12deg)"><use href="#ek-i-heart"/></svg>
    <i class="sl-letter" style="left:68px;top:268px;width:100px;height:100px;--fs:46px">P</i>
    <i class="sl-letter" style="left:1137px;top:327px;width:95px;height:95px;--fs:44px">I</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:102px;top:532px;width:125px;height:125px;transform:rotate(-15deg)"><use href="#ek-i-star"/></svg>
    <i class="sl-letter" style="left:726px;top:613px;width:78px;height:78px;--fs:36px">S</i>
    <svg class="sl-ico" viewBox="0 0 100 100" style="left:1045px;top:540px;width:110px;height:110px;transform:rotate(8deg)"><use href="#ek-i-gem"/></svg>
  </div>
  <div class="cover-center">
    <div class="cover-card">
      <div class="badge">Урок №11</div>
      <div class="card-top"><span class="win-dots"><i></i><i></i><i></i></span><span class="win-close"></span></div>
      <h1>Как программы общаются с&nbsp;нейросетью</h1>
      <p class="cover-sub">Соберём генератор статей: вы называете тему — нейросеть пишет статью с заголовком и разделами. Переходим с ручного requests на openai SDK и учимся управлять temperature и max_tokens.</p>
      <div class="cover-chips"><span class="chip chip--gray">Python</span><span class="chip">openai SDK</span><span class="chip chip--green">temperature · max_tokens</span><span class="chip chip--gray">DeepSeek API</span></div>
    </div>
  </div>"""},

    # 2 · AGENDA
    {"notes": "План. Теории — минимум: уже на 12-й минуте каждый получает ответ нейросети через openai SDK, к 30-й — каркас writer.py. Дальше — 5 правок, как на прошлых уроках.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Agenda · план занятия</div>
    <h2>Как пройдут <span class="acc">60 минут</span></h2>
  </div>
  <div class="agenda">
    <div class="agenda-row"><span class="t">0–5</span><div><div class="tt">Разбор ДЗ</div><div class="dd">Смотрим Streamlit-приложения: оформление, вопрос по файлу, публичная ссылка.</div></div></div>
    <div class="agenda-row"><span class="t">5–12</span><div><div class="tt">SDK и две настройки</div><div class="dd">Минимум теории — только чтобы собрать генератор статей.</div></div></div>
    <div class="agenda-row"><span class="t">12–20</span><div><div class="tt">Промпт-разминка</div><div class="dd">warmup.py: один вопрос к deepseek-chat через openai SDK.</div></div></div>
    <div class="agenda-row"><span class="t">20–30</span><div><div class="tt">Каркас генератора</div><div class="dd">Клиент OpenAI, запрос к нейросети и печать статьи.</div></div></div>
    <div class="agenda-row"><span class="t">30–48</span><div><div class="tt">5 правок через диалог</div><div class="dd">Статьи → temperature → план и max_tokens → сохранение и цикл → стиль.</div></div></div>
    <div class="agenda-row"><span class="t">48–55</span><div><div class="tt">Мини-вопросы и отладка</div><div class="dd">Читаем ошибки, проверяем понимание temperature и base_url.</div></div></div>
    <div class="agenda-row"><span class="t">55–60</span><div><div class="tt">Демо в группе</div><div class="dd">Каждый называет тему и получает готовую статью.</div></div></div>
  </div>
</div>"""},

    # 3 · РАЗБОР ДЗ УРОКА 10
    {"notes": "Откройте 2–3 присланных Streamlit-приложения (на весь блок 5 минут). Разбирайте диалог с нейросетью, а не только результат. Подведите к главному: внутри Streamlit запрос к нейросети всё ещё собирали руками через requests. Сегодня заменим его на аккуратный openai SDK — тот же результат, но код короче.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Разбор ДЗ урока 10</div>
    <h2>Смотрим <span class="acc">Streamlit-приложения</span></h2>
  </div>
  <p>Открываем 2–3 присланных приложения и разбираем именно <span class="hl">диалог с нейросетью</span>: оформление и тема, вопрос по загруженному файлу, публичная ссылка.</p>
  <div class="grid-3" style="margin-top:8px">
    <div class="info-card"><h3>Что сработало</h3>Точечные промпты: своя тема и эмодзи через настройки, вопрос по файлу через <span class="code-chip">st.file_uploader</span>, ссылка, чтобы поделиться.</div>
    <div class="info-card"><h3>Что переделывали</h3>Где забыли «не трогай остальной код» — нейросеть заодно ломала рабочую функцию запроса.</div>
    <div class="info-card"><h3>Вывод</h3>Внутри приложения запрос к нейросети собирали руками через <span class="code-chip">requests</span>. Сегодня заменим его на аккуратный <span class="code-chip">openai</span> SDK.</div>
  </div>
</div>"""},

    # 4 · ИДЕЯ УРОКА
    {"notes": "Главная мысль: две новинки. Первая — переходим с ручного requests на openai SDK: тот же запрос, но короче и чище. Вторая — получаем две настройки ответа: temperature (насколько нейросеть креативна) и max_tokens (длина ответа). На этом соберём генератор статей writer.py.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Идея урока</div>
    <h2>Тот же запрос, но <span class="acc">чище и с настройками</span></h2>
  </div>
  <p>Всё это время запрос к нейросети мы собирали <span class="hl">руками через requests</span> (уроки 8–10) — со своим URL, заголовками и разбором JSON.</p>
  <div class="ek-note" style="margin-top:6px">Сегодня две новинки: переходим на <b>openai SDK</b> — библиотеку, которая делает то же самое короче, и получаем <b>две настройки ответа</b> — <span class="code-chip">temperature</span> (насколько нейросеть креативна) и <span class="code-chip">max_tokens</span> (длина ответа). На этом соберём <b>генератор статей</b> <span class="code-chip">writer.py</span>.</div>
  <p style="margin-top:6px">Идея урока 11: с ручного <b>requests</b> — на <b>openai SDK</b>, настраиваем <b>temperature</b> и <b>max_tokens</b>, называете тему — получаете <b>статью</b>.</p>
</div>"""},

    # 5 · ЧТО ТАКОЕ SDK
    {"notes": "Быстрый recap: как запрос выглядел через requests на уроках 8–10 — свой url, заголовки, json и разбор ответа. SDK делает ту же работу, только библиотека берёт URL, заголовки и разбор JSON на себя. Не углубляйтесь — главное впереди.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Вспоминаем</div>
    <h2>Что такое <span class="acc">SDK</span></h2>
  </div>
  <p>На уроках 8–10 запрос к нейросети мы собирали <span class="hl">вручную через requests</span>: свой адрес, заголовок с ключом, словарь с данными и разбор JSON в ответе.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">import</span> requests
url = <span class="st">"https://api.deepseek.com/chat/completions"</span>
headers = {<span class="st">"Authorization"</span>: <span class="st">"Bearer "</span> + API_KEY}
data = {<span class="st">"model"</span>: <span class="st">"deepseek-chat"</span>, <span class="st">"messages"</span>: messages}
response = requests.post(url, headers=headers, json=data)
answer = response.json()[<span class="st">"choices"</span>][0][<span class="st">"message"</span>][<span class="st">"content"</span>]</div>
  </div>
  <div class="info-card">SDK — это <span class="hl">библиотека-помощник</span>: она берёт URL, заголовки и разбор JSON на себя. Мы описываем только <b>суть запроса</b>, а не технику.</div>
</div>"""},

    # 6 · БИБЛИОТЕКА openai — НЕ ТОЛЬКО ПРО OpenAI
    {"notes": "Главная мысль урока: библиотека называется openai, но через base_url её можно использовать с совместимыми API, в том числе с DeepSeek. Это удобный клиент: один и тот же код работает с разными провайдерами, меняются только адрес и ключ. Подчеркните это несколько раз за урок.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Главная мысль</div>
    <h2>Библиотека openai — <span class="acc">не только про OpenAI</span></h2>
  </div>
  <p>Библиотека называется <span class="code-chip">openai</span>, но через <span class="code-chip">base_url</span> её можно направить к <span class="hl">совместимому API</span> — в том числе к DeepSeek.</p>
  <div class="code-win">
    <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
    <div class="code-body"><span class="kw">from</span> openai <span class="kw">import</span> OpenAI
client = OpenAI(api_key=API_KEY,
                base_url=<span class="st">"https://api.deepseek.com"</span>)  <span class="cm"># едем к DeepSeek</span></div>
  </div>
  <div class="ek-note">Именно <span class="hl">base_url</span> перенаправляет запрос на серверы DeepSeek. Без него SDK пошёл бы на серверы OpenAI. <b>Один и тот же код работает с разными провайдерами — меняется только адрес и ключ.</b></div>
</div>"""},

    # 7 · ДВЕ НАСТРОЙКИ: temperature И max_tokens
    {"notes": "Две настройки запроса. temperature от 0 до 1 управляет строгостью и креативностью: около 0.2 — строго и предсказуемо, около 0.9 — свободнее и образнее. max_tokens ограничивает длину ответа: обрывается на полуслове — увеличьте, хотите короче — уменьшите. Живую разницу temperature покажем позже на одной теме.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Новое · две настройки</div>
    <h2><span class="acc">temperature</span> и <span class="acc">max_tokens</span></h2>
  </div>
  <p>У запроса через SDK есть <span class="hl">две настройки</span>, с помощью которых управляем ответом нейросети.</p>
  <div class="vs">
    <div class="vs-col vs-col--plain">
      <h4>temperature (0 → 1)</h4>
      <p>Регулятор между строгим и творческим ответом. Около <b>0.2</b> — предсказуемо и по делу, около <b>0.9</b> — свободнее и образнее.</p>
      <p class="note">Для инструкции — низкая, для сказки — высокая.</p>
    </div>
    <div class="vs-col vs-col--win">
      <h4>max_tokens</h4>
      <p>Ограничение длины ответа. Обрывается на полуслове — увеличьте; хотите короче — уменьшите.</p>
      <p class="note">Один токен — примерно часть слова или короткое слово.</p>
    </div>
  </div>
  <p>Настройки <span class="code-chip">temperature</span> и <span class="code-chip">max_tokens</span> задаются прямо в запросе <span class="code-chip">create(...)</span>.</p>
</div>"""},

    # 8 · ПРОМПТ #1 · РАЗМИНКА
    {"notes": "Никакой долгой подготовки: сразу просим у DeepSeek маленький скрипт на openai SDK и запускаем. Промпт с ролью и форматом — техники прошлых уроков работают и здесь. Ученики копируют промпт целиком в новый чат DeepSeek.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Промпт #1 · разминка</div>
    <h2>warmup.py за <span class="acc">две минуты</span></h2>
  </div>
  <p>Не будем долго готовиться — попросим у DeepSeek маленький скрипт на openai SDK и сразу запустим его в терминале.</p>
  <div class="prompt-card" style="margin-top:10px">
    <span class="pc-tag">→ Новый чат DeepSeek</span>
    <div class="pc-text">Ты — опытный Python-разработчик и наставник школьника.
Напиши маленький скрипт warmup.py на библиотеке openai (SDK):
создай клиент OpenAI с api_key из константы и
base_url="https://api.deepseek.com", отправь один вопрос модели
deepseek-chat через client.chat.completions.create и распечатай
ответ. Прокомментируй, чем это короче ручного requests.
Ответь одним блоком.</div>
  </div>
</div>"""},

    # 9 · ЗАПУСК И РАЗБОР warmup.py
    {"notes": "Фундамент урока: дождитесь, пока у всех в терминале появится ответ нейросети. На живом коде показываем сразу три вещи: OpenAI(...) с base_url, client.chat.completions.create вместо requests.post и response.choices[0].message.content вместо длинного разбора JSON. Не идите дальше, пока не запустилось у каждого.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Запуск и разбор</div>
    <h2>Один вопрос через <span class="acc">openai SDK</span></h2>
  </div>
  <div class="grid-2">
    <div class="col">
      <ol class="steps steps--tight">
        <li><div>В <span class="code-chip">vibe-coding</span> создайте папку <span class="code-chip">lesson-11</span></div></li>
        <li><div>Выполните <span class="code-chip">pip install openai python-dotenv</span></div></li>
        <li><div>Создайте <span class="code-chip">warmup.py</span> и вставьте код из ответа</div></li>
        <li><div>Выполните <span class="code-chip">python warmup.py</span></div></li>
      </ol>
      <div class="ek-note ek-note--green" style="margin-top:14px">В терминале появился ответ нейросети? Значит, SDK работает — фундамент генератора готов.</div>
    </div>
    <div class="kv">
      <div class="kv-row"><div class="k" style="text-transform:none">OpenAI(...)</div><div class="v">Клиент с base_url DeepSeek.</div></div>
      <div class="kv-row"><div class="k" style="text-transform:none">create(...)</div><div class="v">Одна строка вместо requests.post.</div></div>
      <div class="kv-row"><div class="k" style="text-transform:none">choices[0]...</div><div class="v">Короткий путь к тексту ответа.</div></div>
    </div>
  </div>
</div>"""},

    # 10 · ЕСЛИ НЕ ЗАПУСТИЛОСЬ
    {"notes": "Шпаргалка по трём типичным проблемам запуска. Почините у всех — этот же клиент, ключ и папка нужны дальше для самого генератора статей.",
     "html": r"""<div class="sl-body">
  <div>
    <div class="q-label">Типичные ситуации запуска</div>
    <h2>Если warmup.py <span class="acc">не запустился</span></h2>
  </div>
  <div class="grid-3" style="margin-top:10px">
    <div class="ek-note ek-note--red"><b>ModuleNotFoundError: openai</b><br>Забыли установить библиотеку. Выполните в терминале <span class="code-chip">pip install openai python-dotenv</span> и запустите снова.</div>
    <div class="ek-note ek-note--red"><b>Ключ не подхватился</b><br>Ключ пустой или не там. Проверьте константу с ключом (или <span class="code-chip">DEEPSEEK_KEY</span> в <span class="code-chip">.env</span>) — как на уроках 8–10.</div>
    <div class="ek-note ek-note--red"><b>AuthenticationError</b><br>Ключ неверный. Скопируйте <span class="code-chip">DEEPSEEK_KEY</span> заново без лишних пробелов; на скриншотах ключ скрывайте.</div>
  </div>
</div>"""},
]
