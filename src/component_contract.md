# Контракт интерактивного компонента дизайн-бука Eduson Kids

Ты собираешь ОДИН интерактивный блок для дизайн-бука HTML-презентаций Eduson Kids — онлайн-школы
программирования для детей 10–14 лет. Блок вставляется в готовую страницу, где уже подключены шрифты
(Inter Tight, Inter, JetBrains Mono) и базовый CSS (приведён ниже). Тексты на русском, обращение к ученику
на «ты», тон дружелюбный и конкретный, без сюсюканья и канцелярита.

Тематика демо-контента: урок №11 «Как работают вложенные и каскадные условия» (Python: if / elif / else,
логические операторы and / or / not, скобки в условиях).

## Формат ответа (структурированный вывод)

- `slug` — задан в задаче, вернуть как есть.
- `title` — название шаблона по-русски, коротко (например «Квиз: один правильный ответ»).
- `description` — 1–2 предложения: когда преподавателю использовать этот шаблон на занятии.
- `css` — ДОПОЛНИТЕЛЬНЫЕ стили только для этого блока. КАЖДЫЙ селектор начинается с `#ib-<slug>`.
  Без `@import`, без `@font-face`, без стилей на голые теги вне `#ib-<slug>`. Анимации/transition можно.
- `html` — разметка блока. Корень строго: `<div class="ek-ib" id="ib-<slug>">…</div>`.
  Внутри НЕТ `<style>` и `<script>`, НЕТ inline-обработчиков (onclick и т.п.).
- `js` — IIFE вида `(function(){ 'use strict'; var root=document.getElementById('ib-<slug>'); if(!root) return; … })();`
  Все выборки — только `root.querySelector/querySelectorAll`. Никаких глобальных переменных, никаких
  обращений к document по id, кроме корня. Обработчики — addEventListener.

## Базовый CSS страницы (УЖЕ подключён — используй эти переменные и классы, не переопределяй их)

```css
:root{
  --ek-violet:#8C7FF6; --ek-violet-soft:#A79EF9; --ek-violet-deep:#6F61E8; --ek-violet-bg:#F0EEFE;
  --ek-green:#3DF79D; --ek-green-soft:#7BF9BD; --ek-green-mint:#C9F7E3; --ek-green-pale:#E7FDF2; --ek-green-deep:#0FBF6E;
  --ek-ink:#17171C; --ek-gray:#8F8F98; --ek-gray-light:#EFEFF2; --ek-line:#E3E3EA; --ek-white:#fff;
  --ek-red:#FF6B6B; --ek-red-pale:#FFECEC; --ek-bg:#F7F7FB; --ek-radius:28px;
  --ek-font-head:'Inter Tight','Inter','Segoe UI',system-ui,sans-serif;
  --ek-font-body:'Inter','Segoe UI',system-ui,sans-serif;
  --ek-font-mono:'JetBrains Mono','Cascadia Mono','Consolas',monospace;
}
/* Карточка-поверхность (корень .ek-ib уже лежит на белой карточке страницы — свою карточку НЕ рисуй,
   если шаблону не нужна отдельная внутренняя, например флип-карта) */
.ek-ib{font-family:var(--ek-font-body);color:var(--ek-ink)}
/* Заголовок вопроса внутри блока */
.ek-q{font:800 22px/1.3 var(--ek-font-head);margin:0 0 18px}
/* Кнопки */
.ek-btn{font:700 15px/1 var(--ek-font-head);border:0;border-radius:14px;padding:14px 22px;cursor:pointer;transition:background .15s,transform .1s,opacity .15s}
.ek-btn:active{transform:scale(.97)}
.ek-btn--primary{background:var(--ek-violet);color:#fff}
.ek-btn--primary:hover{background:var(--ek-violet-deep)}
.ek-btn--green{background:var(--ek-green);color:var(--ek-ink)}
.ek-btn--ghost{background:transparent;border:2px solid var(--ek-line);color:var(--ek-ink)}
.ek-btn--ghost:hover{border-color:var(--ek-violet-soft)}
.ek-btn:disabled{opacity:.45;cursor:not-allowed}
/* Вариант ответа */
.ek-option{display:flex;align-items:center;gap:14px;width:100%;text-align:left;background:#fff;border:2px solid var(--ek-line);border-radius:16px;padding:14px 18px;font:600 16px/1.35 var(--ek-font-body);color:var(--ek-ink);cursor:pointer;transition:border-color .15s,background .15s}
.ek-option+.ek-option{margin-top:10px}
.ek-option:hover{border-color:var(--ek-violet-soft)}
.ek-option.is-selected{border-color:var(--ek-violet);background:var(--ek-violet-bg)}
.ek-option.is-correct{border-color:var(--ek-green-deep);background:var(--ek-green-pale)}
.ek-option.is-wrong{border-color:var(--ek-red);background:var(--ek-red-pale)}
.ek-option:disabled{cursor:default}
/* Буллит-кружок А/Б/В/Г */
.ek-chip{flex:0 0 auto;width:34px;height:34px;border-radius:50%;background:var(--ek-gray-light);display:flex;align-items:center;justify-content:center;font:800 14px var(--ek-font-head)}
.ek-option.is-correct .ek-chip{background:var(--ek-green)}
.ek-option.is-wrong .ek-chip{background:var(--ek-red);color:#fff}
/* Фидбек */
.ek-feedback{display:none;margin-top:16px;border-radius:14px;padding:14px 18px;font:600 14px/1.5 var(--ek-font-body)}
.ek-feedback.is-on{display:block}
.ek-feedback--ok{background:var(--ek-green-pale);color:#0B7A48}
.ek-feedback--err{background:var(--ek-red-pale);color:#C6403F}
/* Код Python */
.ek-code{background:#fff;border:2px solid var(--ek-ink);border-radius:14px;padding:18px 22px;font:500 14px/1.65 var(--ek-font-mono);color:var(--ek-ink);overflow-x:auto;white-space:pre;tab-size:4}
.ek-code .c{color:var(--ek-gray)}   /* комментарий */
.ek-code .k{font-weight:700}        /* ключевое слово */
/* Зелёный стикер-бейдж (наклон уже в классе) */
.ek-badge{display:inline-block;background:var(--ek-green);color:var(--ek-ink);font:800 14px/1 var(--ek-font-head);padding:9px 16px;border-radius:10px;transform:rotate(-3deg)}
.ek-badge--violet{background:var(--ek-violet);color:#fff}
/* Прогресс-точки */
.ek-dots{display:flex;gap:8px}
.ek-dots i{width:10px;height:10px;border-radius:50%;background:var(--ek-line)}
.ek-dots i.is-on{background:var(--ek-violet)}
.ek-dots i.is-done{background:var(--ek-green-deep)}
```

## Обязательные правила

1. Всё кликабельное — `<button type="button">` (для текстовых полей — `<input>`/`<label>`). Div-кнопки запрещены.
2. Состояния вариантов — только классы `.is-selected` / `.is-correct` / `.is-wrong` на `.ek-option`;
   фидбек — `.ek-feedback` + `.is-on` + модификатор `--ok`/`--err`.
3. Семантика цвета: верно = зелёный (--ek-green*), ошибка = коралловый (--ek-red*), выбор/акцент =
   фиолетовый. Других смысловых цветов не вводить.
4. Обязательна кнопка «Заново» (`class="ek-btn ek-btn--ghost"`), полностью сбрасывающая состояние блока.
   До первого действия пользователя она может быть disabled.
5. После проверки интерактив блокируется (disabled), повторные клики/двойная проверка не ломают состояние.
6. Доступность: aria-live="polite" на фидбеке; aria-pressed на кнопках-переключателях; фокус видим
   (outline не убирать без замены).
7. Корень блока резиновый: без фиксированной width; допустим max-width до 680px по центру.
8. Код Python — в `.ek-code` (white-space:pre уже включён), комментарии в `<span class="c">`,
   ключевые слова (if/elif/else/and/or/not/print/int/input) в `<span class="k">`.
9. Эмодзи — 0–2 на блок, только там, где уместно. Буллиты вариантов — «А/Б/В/Г» через `.ek-chip`.
10. Ничего внешнего: без библиотек, без картинок, без сетевых запросов, без localStorage.
11. JS обязан переживать повторную инициализацию страницы (никаких setInterval; setTimeout ≤ 600 мс и
    только для анимаций, с очисткой при «Заново»).
