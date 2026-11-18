# Guto Kilishi — 15s Promo (shot list)

**Style reference:** a fast-cut, CGI-style product commercial. It cuts about every 1.2 seconds, sends ingredients flying at the camera, uses neon-lit stages, orbits the product, shows macro close-ups of the label, ends on a podium and finishes with the social handle.
**Format:** 9:16 vertical (1080×1920), 30 fps, 15.0 s, with music and sound effects. There's no voiceover, because the reference is driven by music.
**Look:** the Guto Kilishi red and white with gold neon. Kilishi, dried chilies, peppercorns and spice dust stand in for the reference's chocolate, berries and oats.

| # | Time | Shot | Sound |
|---|---|---|---|
| 1 | 0.0–1.3 | **Ingredient burst.** A stream of spice pours from the top while kilishi, chilies and peppercorns fly toward the camera. | Low swell, sizzle |
| 2 | 1.3–2.5 | **Tilted stage.** Camera tilted at an angle over a crimson floor and dark wall split by a gold neon seam; a band of kilishi crumbs runs along the seam while chilies drop and bounce. | Beat drops (120 bpm afro-trap) |
| 3 | 2.5–3.6 | **Pack whip-in.** The pack flies in past neon pillars, spinning from back to front, trailing spice dust. | Whoosh + impact |
| 4 | 3.6–5.6 | **Neon tunnel orbit.** The pack floats in a tunnel of gold neon frames while a chili-red spice ribbon studded with chilies and kilishi orbits it. A light sweep crosses the pack. | Groove |
| 5 | 5.6–6.8 | **Logo macro.** Extreme close-up gliding across the "Guto Kilishi" logo, with blurred chilies drifting past in the foreground. | Whoosh |
| 6 | 6.8–8.0 | **Hero pull-back.** The camera pulls back from the pack as the ribbon swirls around it. | — |
| 7 | 8.0–9.1 | **Ring orbit.** The pack tilts inside a full ring of spice and chilies. | — |
| 8 | 9.1–10.3 | **Ingredient sphere.** A rotating ball of kilishi, chilies and peppercorns; the top of the pack rises into frame. | — |
| 9 | 10.3–11.3 | **Label macro pan** across "BEEF JERKY", the bowl of kilishi and "For those who appreciate good things." | Riser starts |
| 10 | 11.3–12.4 | **Top-down shot.** The pack lands on a radial burst of spice powder, sending out a shockwave ring. | Impact, riser builds |
| 11 | 12.4–13.5 | **Podium.** The pack drops onto a glowing gold-rimmed podium under light beams. | Big drop/boom |
| 12 | 13.5–15.0 | **Outro.** The scene dims; the Instagram icon lights up in color, followed by **@GUTO KILISHI** and *For those who appreciate good things.* | Pad + sparkle |

## Files
- `guto_kilishi_promo_15s.mp4`: the finished video.
- `ad.html`: the animation source. Every shot is one entry in the `SHOTS` array, so timings, colors and text are easy to change.
- `audio.py`: the soundtrack generator. `render.js` renders the frames (`DUR=15 node render.js frames 30`).
- `assets/`: the front and back pack cutouts, taken from your studio render.

## To go fully photoreal
The reference was made with 3D/AI tools. A photoreal version (real liquid spice splashes, real lighting) can be made with Higgsfield image-to-video using the pack photos. Your Higgsfield account currently has 0 credits, so it would need credits first.
