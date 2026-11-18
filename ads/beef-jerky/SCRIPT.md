# IRONSMOKE Beef Jerky — 10-Second Ad Script

**Format:** 9:16 vertical (1080×1920), 30 fps, 10.0 s — Reels / TikTok / Shorts / Stories
**Tone:** Bold, smoky, confident. Built to work with the sound off (all key messages are on screen).
**Tagline:** *Chew on something real.*

| Time | Visual | On-screen text | Voiceover (VO) | Sound |
|---|---|---|---|---|
| 0.0–0.4 | Fade up from black on a smoky, ember-lit backdrop. A huge glazed jerky strip slides in from the left in extreme close-up. | — | — | Fire crackle and low drone |
| 0.35 | Camera jolts. | **SLOW.** (cream, stamps in) | "Slow…" | Bass hit |
| 0.95 | Camera jolts. | **SMOKED.** (orange, stamps in) | "…smoked." | Bass hit |
| 1.75–2.5 | Strip and text punch toward the camera; a warm orange flash cuts to the next scene. | — | — | Whoosh |
| 2.1–2.9 | The IRONSMOKE bag drops in from the top and bounces to rest at center. | — | "Ironsmoke Beef Jerky." | Heavy hit when it lands |
| 2.45–3.0 | Five jerky strips fan out behind the bag like flames. | — | — | — |
| 3.1–4.9 | Bag floats gently. Embers keep rising. | **100% REAL BEEF** | "Real beef, smoked twelve hours over hickory." | Hit |
| 5.0–5.5 | Bag lifts and shrinks to make room. | — | — | — |
| 5.3 / 5.9 / 6.5 | Three badges slide in from the right, one after another. | **15G PROTEIN** · per serving / **SMOKED 12 HOURS** · over real hickory / **NO ADDED JUNK** | "Fifteen grams of protein. Nothing you don't need." | Pop × 3 |
| 7.8–8.2 | Badges sweep off to the left; bag settles. | — | — | — |
| 8.2 / 8.5 | Tagline stamps in. | **CHEW ON / SOMETHING REAL.** | "Chew on something real." | Hit, hit |
| 8.9–9.75 | A glowing CTA button pops and pulses. URL appears underneath. | **GRAB A BAG →** · IRONSMOKEJERKY.COM | "Grab a bag today." | Bright ding |
| 9.75–10.0 | Fade to black. | — | — | Tail out |

## Full voiceover (≈ 9 s, read with a deep, gravelly voice and short pauses)

> Slow… smoked.
> Ironsmoke Beef Jerky.
> Real beef, smoked twelve hours over hickory.
> Fifteen grams of protein. Nothing you don't need.
> Chew on something real. Grab a bag today.

**6-second cutdown VO:** "Slow-smoked. Fifteen grams of protein. Ironsmoke — chew on something real."

## Before you publish
- **Brand and product:** "Ironsmoke", the bag design, and the URL are placeholders. Swap in your real brand, logo, and flavor.
- **Claims:** "15g protein", "smoked 12 hours", and "no MSG / no nitrites added" are sample claims. Replace them with the numbers on your actual label, because ad claims have to match the product.

## Files
- `ironsmoke_jerky_ad_10s.mp4`: the finished clip, with a synthesized sound bed (no VO yet).
- `ad.html`: the animation source. Open it in a browser to watch it loop live. All text, colors, and timings are in this file.
- `render.js`: renders the clip frame by frame (`node render.js frames 30`, then encode with ffmpeg).
- `audio.py`: generates the synced sound bed (`python3 audio.py bed.wav`).
