# -*- coding: utf-8 -*-
SLIDES = [
    # 30 · ПРАВКА 5 · ВЫБОР СТИЛЯ СТАТЬИ
    {"notes": "Финальная правка добавляет новую фичу: пользователь выбирает стиль статьи — новость, научпоп или пост для соцсети. Стиль меняет системную роль, тема остаётся той же. Свяжите с уроком: одна и та же тема звучит по-разному, как temperature меняет характер, так и стиль меняет подачу. Дождитесь, пока у всех программа спрашивает стиль и статья приходит в выбранном тоне.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Правка 5 · выбор стиля</div>
      <h2>Одна тема — <span class="acc">разные стили</span></h2>
    </div>
    <p>Финальная фича: перед темой программа спрашивает <span class="hl">стиль</span>, и одна и та же тема раскрывается по-разному.</p>
    <div class="prompt-card prompt-card--copy" style="margin-top:14px">
      <span class="pc-tag">→ В тот же чат</span>
      <div class="pc-text">Добавь выбор стиля статьи: спроси у пользователя, в каком стиле писать — «новость», «научпоп» или «пост для соцсети». Под выбранный стиль подставь свою системную роль журналиста, тему оставь прежней.

Верни весь файл.</div>
    </div>
  </div>"""},

    # 31 · РАЗБОР · ВЫБОР СТИЛЯ
    {"notes": "Ключевой слайд правки. Покажите, что стиль меняет только системную роль — по выбору пользователя подставляется своя строка system, а user с темой тот же. Свяжите с системной ролью журналиста из правки 1: та же техника, теперь роль зависит от выбора. Дайте ученикам сгенерировать статью на одну тему во всех трёх стилях и сравнить.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Разбор кода</div>
      <h2>Стиль меняет <span class="acc">системную роль</span></h2>
    </div>
    <div class="code-win">
      <div class="code-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">PYTHON</span></div>
      <div class="code-body">styles = {
    <span class="st">"новость"</span>: <span class="st">"Ты журналист. Пиши сухую новость: факты, кратко."</span>,
    <span class="st">"научпоп"</span>: <span class="st">"Ты журналист. Пиши научпоп: просто и с примерами."</span>,
    <span class="st">"пост"</span>: <span class="st">"Ты журналист. Пиши лёгкий пост для соцсети с эмодзи."</span>,
}
choice = input(<span class="st">"Стиль (новость / научпоп / пост): "</span>)
system = styles[choice]                    <span class="cm"># выбранная системная роль</span>

response = client.chat.completions.create(
    model=<span class="st">"deepseek-chat"</span>,
    messages=[
        {<span class="st">"role"</span>: <span class="st">"system"</span>, <span class="st">"content"</span>: system},
        {<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: <span class="st">"Напиши статью на тему: "</span> + topic},
    ],
)</div>
    </div>
    <div class="ek-note">Меняется <b>только системная роль</b> — под выбор пользователя подставляем свою строку <span class="code-chip">system</span>, а тема в <span class="code-chip">user</span> остаётся прежней. Та же техника, что с ролью журналиста, только теперь роль зависит от выбора.</div>
  </div>"""},

    # 32 · MINI-QUIZ 1
    {"notes": "Квиз про temperature — прямое следствие правки 3 и разбора. Дайте 10–15 секунд, потом раскройте ответ. Свяжите с привычкой: temperature управляет строгостью и творческой свободой ответа.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Проверка · вопрос 1</div>
      <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
    </div>
    <div class="quiz-box" style="margin-top:10px">
      <span class="q-num">Вопрос 1</span>
      <p class="q-text">Для статьи-инструкции «как заварить чай» Лена поставила <span class="code-chip">temperature=0.9</span> и получила художественную историю вместо точной инструкции. Какое значение подошло бы и почему?</p>
      <div class="quiz-answer">
        <button class="quiz-btn" type="button">Показать ответ</button>
        <div class="quiz-reveal">
          <p>Для точных, фактических текстов нужна <b>низкая temperature</b> (около 0.2): ответы строгие и предсказуемые. Высокая (0.9) подходит для творческих задач — сказок, историй, необычных идей.</p>
          <p><span class="code-chip">temperature</span> управляет переходом от <b>строгого</b> к <b>более творческому</b> ответу. Для инструкции нужна точность.</p>
        </div>
      </div>
    </div>
  </div>"""},

    # 33 · MINI-QUIZ 2
    {"notes": "Квиз про base_url — главная мысль урока. Свяжите с привычкой: библиотеку openai можно направить к совместимому API DeepSeek через base_url.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Проверка · вопрос 2</div>
      <h2>Изучите ситуацию и <span class="acc">ответьте</span></h2>
    </div>
    <div class="quiz-box" style="margin-top:10px">
      <span class="q-num">Вопрос 2</span>
      <p class="q-text">Зачем при создании клиента писать <span class="code-chip">base_url="https://api.deepseek.com"</span>, если библиотека называется <span class="code-chip">openai</span>?</p>
      <div class="quiz-answer">
        <button class="quiz-btn" type="button">Показать ответ</button>
        <div class="quiz-reveal">
          <p>SDK <span class="code-chip">openai</span> умеет общаться с любым совместимым API. <b>base_url</b> перенаправляет запросы на серверы DeepSeek вместо OpenAI.</p>
          <p>Один и тот же код работает с разными провайдерами — меняется только <b>адрес и ключ</b>. Без <span class="code-chip">base_url</span> SDK пошёл бы на серверы OpenAI.</p>
        </div>
      </div>
    </div>
  </div>"""},

    # 34 · ОТЛАДКА
    {"notes": "Научите читать traceback снизу вверх — пригодится на всех уроках Python. Напомните привычку: непонятную ошибку целиком копируем в DeepSeek. Три поломки справа — самые частые именно в writer.py на SDK.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Отладка</div>
      <h2>Читаем <span class="acc">ошибки</span> SDK</h2>
    </div>
    <div class="grid-2">
      <div class="col">
        <div class="term">
          <div class="term-head"><span class="win-dots"><i></i><i></i><i></i></span><span class="lang-badge">ТЕРМИНАЛ</span></div>
          <div class="term-body"><span class="dim">Traceback (most recent call last):
  File "writer.py", line 12, in &lt;module&gt;
    response = client.chat.completions.create(...)</span>
openai.AuthenticationError: Incorrect API key</div>
        </div>
        <p style="margin-top:14px;font-size:15.5px">Traceback читаем <span class="hl">снизу вверх</span>: последняя строка — <b>что</b> случилось, строкой выше — <b>где</b>. <span class="code-chip">AuthenticationError</span> значит: ключ неверный или не подхватился из <span class="code-chip">.env</span>.</p>
      </div>
      <div class="info-card">
        <h3>Если застряли</h3>
        <ul class="clean">
          <li>Скопируйте <b>traceback целиком</b> в чат DeepSeek — попросите объяснить и починить</li>
          <li><span class="code-chip">ModuleNotFoundError: openai</span> — забыли <span class="code-chip">pip install openai</span></li>
          <li>Проверьте <span class="code-chip">DEEPSEEK_KEY</span> в <span class="code-chip">.env</span> и <span class="code-chip">base_url</span> DeepSeek</li>
        </ul>
        <p style="margin-top:12px;font-size:14px;color:var(--ek-gray)">Та же привычка, что <span class="code-chip">console.log</span> в «Змейке» и print-метки на уроке 5.</p>
      </div>
    </div>
  </div>"""},

    # 35 · ПРИВЫЧКИ
    {"notes": "5 привычек урока. Дайте сфотографировать слайд. Особо подчеркните вторую: библиотеку openai можно направить к DeepSeek через base_url. Третья и четвёртая — про настройки temperature и max_tokens.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Запомните</div>
      <h2>Привычки работы с <span class="acc">SDK</span></h2>
    </div>
    <div class="kv">
      <div class="kv-row"><div class="k">01 · SDK короче ручного requests</div><div class="v">Одна строка <span class="code-chip">client.chat.completions.create(...)</span> вместо <span class="code-chip">requests.post</span> с URL, заголовками и разбором JSON.</div></div>
      <div class="kv-row"><div class="k">02 · openai и base_url</div><div class="v"><span class="code-chip">base_url="https://api.deepseek.com"</span> перенаправляет запрос на DeepSeek. Один код — разные провайдеры.</div></div>
      <div class="kv-row"><div class="k">03 · temperature — стиль</div><div class="v">Около 0.2 — строго и по фактам, около 0.9 — свободнее и образнее. Настраивайте под задачу.</div></div>
      <div class="kv-row"><div class="k">04 · max_tokens — длина</div><div class="v">Ограничивает размер ответа. Обрывается на полуслове — увеличьте; хотите короче — уменьшите.</div></div>
      <div class="kv-row"><div class="k">05 · Ключ — это пароль</div><div class="v">Берём из <span class="code-chip">.env</span> (переменная <span class="code-chip">DEEPSEEK_KEY</span>). Не публикуем, на скриншотах скрываем.</div></div>
    </div>
  </div>"""},

    # 36 · ЧЕК-ЛИСТ
    {"notes": "Чек-лист завершения генератора статей. Кто отметил всё — пусть сгенерирует две статьи с разной temperature и сравнит. Это показывает, что настройка работает.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Чек-лист</div>
      <h2>Что должно быть к <span class="acc">55-й минуте</span></h2>
    </div>
    <div class="grid-2">
      <div class="info-card">
        <h3 style="color:var(--ek-green-deep)">Готово</h3>
        <ul class="clean">
          <li><span class="code-chip">writer.py</span> запускается командой <span class="code-chip">python writer.py</span></li>
          <li>Запрос идёт через <span class="code-chip">openai</span> SDK с <span class="code-chip">base_url</span> DeepSeek</li>
          <li>По теме приходит статья с заголовком и разделами</li>
          <li>Ключ берётся из <span class="code-chip">.env</span></li>
        </ul>
      </div>
      <div class="info-card">
        <h3 style="color:var(--ek-violet-deep)">Работает</h3>
        <ul class="clean">
          <li>Меняется <span class="code-chip">temperature</span> — видна разница 0.2 и 0.9</li>
          <li><span class="code-chip">max_tokens</span> ограничивает длину</li>
          <li>Статья сохраняется в <span class="code-chip">stat_тема.md</span></li>
          <li>Вывод цветной, генерация идёт по кругу</li>
        </ul>
      </div>
    </div>
    <div class="ek-note ek-note--green">Всё отмечено? Сгенерируйте статью на одну тему при <span class="code-chip">temperature=0.2</span> и <span class="code-chip">0.9</span> и сравните — генератор готов.</div>
  </div>"""},

    # 37 · ДЗ
    {"notes": "ДЗ — прокачать генератор, примерно 30 минут. Каждое улучшение — отдельный диалог с DeepSeek, не всё сразу. Напомните про ключ на скриншотах.",
     "html": r"""<div class="sl-body">
    <div>
      <div class="q-label">Домашнее задание · около 30 минут</div>
      <h2>Прокачайте <span class="acc">генератор</span></h2>
    </div>
    <p>Три улучшения — каждое через отдельный диалог с DeepSeek:</p>
    <div class="grid-3">
      <div class="info-card">
        <h3>Свой стиль</h3>
        <p>Добавьте к готовым стилям (новость, научпоп, пост) <b>свой четвёртый</b> — например, «сказка» или «инструкция» — со своей системной ролью.</p>
      </div>
      <div class="info-card">
        <h3>Заголовки</h3>
        <p>Пусть программа выдаёт <b>5 вариантов заголовка</b> к теме, чтобы можно было выбрать самый удачный.</p>
      </div>
      <div class="info-card">
        <h3>Своя тема</h3>
        <p>Сгенерируйте готовую статью для школьного проекта и сохраните её в файл <span class="code-chip">stat_тема.md</span>.</p>
      </div>
    </div>
    <div class="ek-note ek-note--red">Пришлите скриншот готовой статьи в терминале — <b>ключ скройте!</b> Ваш самый удачный промпт — отдельным сообщением.</div>
  </div>"""},

    # 38 · ФИНАЛ
    {"cls": "slide--green",
     "notes": "Закройте урок. Сегодня перешли на openai SDK и научились управлять ответом через temperature и max_tokens. На уроке 12 сделаем вывод постепенным: текст печатается по фрагментам, как в ChatGPT (стриминг), а системные промпты зададут личности AI-собеседника.",
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
    <div class="bubble">
      <h1>До встречи<br>на уроке 12!</h1>
      <p>Сегодня вы перешли на openai SDK и научились управлять ответом через temperature и max_tokens. На уроке 12 сделаем вывод постепенным: текст будет печататься по фрагментам, как в ChatGPT (стриминг), а системные промпты зададут личности AI-собеседника.</p>
    </div>
  </div>"""},
]
