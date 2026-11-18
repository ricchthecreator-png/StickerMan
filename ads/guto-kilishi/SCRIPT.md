# Guto Kilishi — 10-Second Ad Script

**Product:** Guto Kilishi Beef Jerky, 40 g pack. Authentic Nigerian snack.
**Format:** 9:16 vertical (1080×1920), 30 fps, 10.0 s, for Reels / TikTok / Shorts / Status
**Tone:** Warm, proud, appetizing. Built to work with the sound off (every key message is on screen).
**Brand lines (taken from the pack):** "Real Taste. Real Culture. Guto." · "For those who appreciate good things."

| Time | Visual | On-screen text | Voiceover (VO) | Sound |
|---|---|---|---|---|
| 0.0–2.4 | **Real lifestyle photo.** Opens tight on the bowl of spice-coated kilishi with dried chilies, then slowly pushes out to reveal the Guto Kilishi pack. | **REAL TASTE.** (0.4s, white) / **REAL CULTURE.** (1.05s, gold) | "Real taste… real culture." | Warm pad, sizzle, a bass hit on each line |
| 2.4–2.75 | A red circle grows out from the center and wipes into the brand's red. | — | — | Whoosh |
| 2.6–3.4 | Red stage with slowly spinning light rays and falling chili flakes. The pack drops in and bounces. | — | "Guto Kilishi." | Heavy hit on landing; the afro-groove beat (108 bpm) starts |
| 3.0–3.6 | Kilishi pieces burst out from behind the pack and float around it. | — | — | — |
| 3.5–5.0 | Pack floats gently. | **AUTHENTIC** (top) / **NIGERIAN KILISHI** / *Beef jerky · Beef · Chili · Spices* | "Authentic Nigerian kilishi — just beef, chili and spices." | Pops |
| 5.2–5.7 | Pack lifts up and shrinks. | — | — | — |
| 5.45 / 6.05 / 6.65 | Three white badges in brand red slide in, one after another. | **HIGH PROTEIN** · 52g protein per 100g / **100% PREMIUM BEEF** / **HYGIENICALLY PACKED** | "High protein. One hundred percent beef. Hygienically packed." | Pop × 3 |
| 7.7–8.3 | Badges sweep off to the left; pack settles at the top. | — | — | — |
| 8.25–8.95 | Tagline appears in script lettering. | *For those who appreciate* / ***good things.*** (gold) | "Guto Kilishi. For those who appreciate good things." | Hit, hit |
| 9.0–9.75 | A white "GRAB A PACK" button pops and pulses. | **GRAB A PACK →** · @Guto Kilishi · Proudly Nigerian · Locally Sourced | (music only) | Bright ding |
| 9.75–10.0 | Fade to black. | — | — | Tail out |

## Full voiceover (about 9 seconds; a warm, confident Nigerian voice)

> Real taste… real culture.
> Guto Kilishi — authentic Nigerian kilishi, just beef, chili and spices.
> High protein. One hundred percent beef.
> For those who appreciate good things.

**Shorter alternative (6 seconds):** "Real taste. Real culture. Guto Kilishi — for those who appreciate good things."

## Claims used (all from the pack)
- High protein: 52 g protein per 100 g, from the nutrition panel. That's about 21 g per 40 g pack.
- 100% premium beef, hygienically packed, "Authentic Nigerian Snack", and the "Traditional taste, modern standard" line on the retail pack.
- Ingredients: beef, chili pepper, spices, salt, natural flavour.

## Before posting
- Check the social handle. The pack says "@Guto Kilishi", but real handles can't contain spaces, so swap in the exact handle (for example @gutokilishi) and add a website or order link if you have one. Both are set in `ad.html`.

## Files
- `guto_kilishi_ad_10s.mp4`: the finished clip, with music and sound effects but no voiceover yet.
- `ad.html`: the animation source. Serve the folder and open the page to watch it loop. All text, colors and timings are in this file.
- `assets/`: your studio pack shot, the lifestyle photo, and the transparent pack cutout used in the animation.
- `render.js`: renders the clip frame by frame (`node render.js frames 30`, then encode with ffmpeg).
- `audio.py`: generates the synced music and sound effects (`python3 audio.py bed.wav`).
