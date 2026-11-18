# Guto Kilishi — "Not Just Jerky" (12s, built for views)

**Format:** 9:16 vertical (1080×1920), 30 fps, 12.0 s, stereo sound design. Text stays inside the TikTok/Reels safe zone, clear of the right-side buttons and the bottom caption area.

## Why it's built to hold attention
- **Hook in under 0.5 s.** A "WARNING: HIGHLY ADDICTIVE" sticker shows while the pack trembles, then **tears open and erupts** at the camera. The first frame already asks a question.
- **New stimulus every 0.25–0.5 s.** Word-by-word slams with background color flips, a crown drop, a product spin-in and three callouts arrive faster than viewers can scroll away.
- **A pattern break at 7s.** The music cuts to silence for the **bite** and two crunches, then the beat drops back in on "HOOKED". That contrast is what makes people rewatch.
- **Clean ending.** The end card holds steady to the last frame instead of fading to black, so the clip loops smoothly. That helps the replay rate.

## Edit + sound sync (each sound is placed from the same timeline as its visual)
| Time | Visual | Sound |
|---|---|---|
| 0.00–0.40 | Pack trembles; "⚠ WARNING: HIGHLY ADDICTIVE" sticker pops and blinks | Low rumble building; pop |
| 0.40 | **Top of the pack tears off** | Rip (fast crackle) |
| 0.50 | **Kilishi, chilies and spice erupt** at the camera; white flash; camera push | Explosion impact + crunchy debris; **beat starts** |
| 1.15 | Push into the pack | Whoosh |
| 1.25–2.25 | **THIS / IS / NOT / JUST / JERKY.** One word every 1/8 beat, the background color flips each time, and "NOT" gets struck through | A slam on every word, rising in pitch; 16th-note hats |
| 2.50 | **IT'S KILISHI.** | Big slam + sub boom |
| 2.72 → 3.00 | Gold crown falls and lands on the word; sparkles | Falling whoosh → **metallic clink** |
| 3.25 → 3.60 | Pack spins in from the left and lands; dust ring | Panned whoosh (left→center) → thud |
| 3.9 / 4.2 / 4.5 | Callouts: **52G PROTEIN** (per 100g) · **100% BEEF** · **CHILI + SPICES** | Pop × 3, rising |
| 5.0–6.2 | **SPICE LEVEL** meter fills; flames rise and grow; pack wobbles from heat | Fire roar + sizzle swelling; 12 ticks rising in pitch |
| 6.25 | **PROPER HOT.** | Boom |
| 6.75 | A chili **slashes** across the screen | Blade "shing" + air |
| 6.85 | The screen splits diagonally and tears apart | Whoosh |
| 7.0 | "ONE BITE..." types on over real kilishi | **Music cuts to silence** |
| 7.4 / 7.75 | **Bite marks** appear, crumbs fly, zoom punch | **Crunch** × 2 |
| 7.9 | **...AND YOU'RE HOOKED.** | Big slam; **beat drops back in** |
| 8.0 / 8.5 / 9.0 / 9.5 | Photo montage with zoom punches: **TRADITIONAL / TASTE. / MODERN / STANDARD.** | Camera shutter on each cut |
| 9.5–10.0 | Push into the pack | Riser |
| 10.0 | End card: the pack drops in on red rays | Boom |
| 10.32 | Pack lands and the crown floats above it | Thud |
| 10.45 | *For those who appreciate good things.* | Sparkle |
| 10.7 | **ORDER NOW →** button pops, with a light sweep across it | Pop |
| 10.9 | @GUTO KILISHI | Shimmer |

## Real photos used
- **Pack (front and back):** cut out of your studio render. It's the pack that tears open, spins in, gets the callouts, and lands on the end card.
- **Exploding kilishi and bite piece:** every flying piece is filled with **real kilishi texture taken from your bowl photo**.
- **Backgrounds:** your lifestyle photo (blurred and tinted) sits behind the hook, the callouts and the end card. The bowl of chilies burns behind the spice meter. Real kilishi sits behind "IT'S KILISHI."
- **Word slams:** each word lands over a different real photo: the bowl, the studio pack, **your in-store photo**, the chilies, and kilishi up close.
- **Montage:** the bowl of kilishi → the studio front and back → **your two real packs on the table** → the lifestyle hero shot.

## Claims (all from the pack)
52g protein per 100g (nutrition panel) · 100% premium beef · beef, chili pepper and spices · "Traditional taste, modern standard" · "For those who appreciate good things."
"Highly addictive" and "Proper hot" are playful lines, not product claims.

## Files
- `guto_kilishi_viral_12s.mp4`: the finished ad.
- `ad.html`: the visuals. The `T` / `EVENTS` timeline at the top drives everything.
- `events.json`: that timeline, exported when rendering.
- `audio.py`: sound design built from `events.json` (`python3 audio.py events.json out.wav`).
- `render.js`: renders the frames (`DUR=12 node render.js frames 30`).

To change the timing, edit `T` in `ad.html` and re-render. The sounds move with the visuals automatically.
