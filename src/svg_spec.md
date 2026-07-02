# SVG asset pack for the "Eduson Kids" presentation design system

You are generating decorative SVG assets for a kids' coding school brand (ages 10–14, playful but clean).
Create ALL files listed below **in the current working directory** (create the `icons/` subfolder).

## Hard requirements (apply to every file)

- Pure static SVG 1.1, UTF-8, standalone (opens directly in a browser).
- No `<script>`, no external references, no `<image>`, no CSS classes — inline presentation attributes only.
- No raster data. No filters heavier than a simple blur (prefer none).
- Geometry style: chunky, rounded, friendly. Use `stroke-linejoin="round"` / `stroke-linecap="round"` where strokes are used. Prefer filled shapes over strokes for icons.
- Letters (X, Y, A, B) — Latin capitals. PREFER `<path>` outlines of bold geometric sans letters. If you cannot produce good letter paths, `<text>` with `font-family="Arial, Helvetica, sans-serif" font-weight="bold"` and `text-anchor="middle"` is acceptable.
- Exact palette (do not improvise):
  - violet background `#8C7FF6`, violet decor `#A79EF9`, violet light (letters) `#C4BEFA`
  - green background `#3DF79D`, green decor `#7BF9BD`, green light (letters) `#C4FCE0`
  - mint line `#C9F7E3`, mint fill `#97F3C8`, white `#FFFFFF`

## Icon shapes (used across files)

- **trophy**: classic cup with two side handles, thick stem, base plinth. Solid single-color silhouette.
- **heart**: rounded heart with a small "shine" notch cut or none; solid.
- **star**: 5-point star with rounded points; solid.
- **gem**: faceted diamond (emerald-cut top, pointed bottom); show 2–3 facet lines by cutting them out of the silhouette (background-color gaps), still single-color.
- **letter-circle**: solid filled circle with a bold capital letter centered inside, letter in the "light" tone of the palette.

## Files

### 1. `bg-orbit-violet.svg` — title-slide background, viewBox="0 0 1280 720"
1. Full-bleed rect fill `#8C7FF6`.
2. One large orbit ring: ellipse centered ~(640,360), rx≈520 ry≈330, `fill="none"`, `stroke="#A79EF9"`, `stroke-width="3"`, opacity 0.9.
3. Sitting ON the ring (centers lying close to the ring path), 8 decor elements, all fill `#A79EF9` (letters `#C4BEFA`):
   - trophy at ≈(150,95), width ≈150, rotated ≈ -10°
   - letter-circle "Y" at ≈(505,52), diameter ≈78
   - heart at ≈(1105,80), width ≈130, rotated ≈ 12°
   - letter-circle "X" at ≈(118,318), diameter ≈100
   - letter-circle "B" at ≈(1185,375), diameter ≈95
   - star at ≈(165,595), width ≈125, rotated ≈ -15°
   - letter-circle "A" at ≈(765,652), diameter ≈78
   - gem at ≈(1100,595), width ≈110, rotated ≈ 8°
4. Elements must overlap the ring (ring passes behind them) — draw ring first, icons after.
5. Composition must leave the center area (roughly x 220–1060, y 230–500) visually calm: nothing overlaps it except the ring line itself.

### 2. `bg-orbit-green.svg` — section-divider background, viewBox="0 0 1280 720"
Identical composition to file 1, recolored: rect `#3DF79D`, ring stroke `#7BF9BD`, icons `#7BF9BD`, letters `#C4FCE0`.

### 3. `decor-waves-mint.svg` — right-side decor for white slides, viewBox="0 0 520 720", TRANSPARENT background (no rect)
1. Two smooth vertical wavy lines flowing top→bottom (gentle S-curves, cubic Béziers), `stroke="#C9F7E3"`, `stroke-width="3"`, `fill="none"`. First line enters at top ≈x300 and exits bottom ≈x210; second enters at top ≈x480 and exits ≈x430.
2. Sitting on the lines, icons fill `#97F3C8` (letters `#FFFFFF`):
   - heart at ≈(330,95), width ≈120, rotated ≈ 10°
   - letter-circle "Y" at ≈(455,155), diameter ≈95
   - gem at ≈(255,330), width ≈115, rotated ≈ -8°
   - star at ≈(465,560), width ≈115, rotated ≈ 12°
   - letter-circle "A" at ≈(185,600), diameter ≈90
3. Lines drawn first, icons after (icons cover the line).

### 4. `icons/` — reusable single-color icons, each viewBox="0 0 100 100", fill="currentColor" on every shape (so CSS can tint them)
- `icons/trophy.svg`
- `icons/heart.svg`
- `icons/star.svg`
- `icons/gem.svg`
Each icon: the silhouette fills ~86% of the viewBox, centered, `fill="currentColor"` (no hardcoded colors anywhere in these 4 files).

## Acceptance checklist (verify before finishing)

1. 7 files exist: 3 backgrounds/decors + 4 icons in `icons/`.
2. Every file is valid XML and renders standalone in a browser.
3. Exact hex values from the palette; icons use ONLY `currentColor`.
4. Icons recognizable when rendered at 40×40 px.
5. Backgrounds: center safe-zone is clean; nothing clipped at viewBox edges in an ugly way (partial bleed off-edge is fine and even welcome for trophy/heart/star).
6. No text other than the letters X/Y/A/B.
