#!/usr/bin/env python3
"""Assemble the Street 13 "Always Open" 15s 9:16 ad from the generated clips.

Usage: python3 assemble.py [music_version]   (default 3)
Inputs:  clips/<name>.mp4, endcard/endcard-9x16.png, music/street13-mix-music-v<N>.mp3
Output:  street13-always-open-9x16.mp4
"""
import subprocess, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
music = sys.argv[1] if len(sys.argv) > 1 else "3"

# (clip file, source in-point seconds, timeline start, timeline end)
# Timed to the voiceover: drop/"except Street 13" at 4.29s, food words 6.2-9.7s,
# "Dine in or delivery" 9.95s, "Street 13. Always open." from ~12.8s.
SHOTS = [
    ("1A-street.mp4",     0.5, 0.0,  2.2),
    ("1B-phone.mp4",      1.0, 2.2,  3.7),
    ("2A-storefront.mp4", 0.0, 3.7,  5.8),
    ("2B-fries.mp4",      0.8, 5.8,  7.35),
    ("3A-burger.mp4",     1.9, 7.35, 7.95),
    ("3B-bite.mp4",       1.0, 7.95, 8.56),
    ("3C-wings.mp4",      0.8, 8.56, 10.0),
    ("4A-delivery.mp4",   1.0, 10.0, 12.6),
]
END_START, TOTAL = 12.6, 15.0

args = ["ffmpeg", "-y", "-v", "error"]
filters, labels = [], []
for i, (f, src_in, t0, t1) in enumerate(SHOTS):
    args += ["-ss", str(src_in), "-t", f"{t1 - t0:.3f}", "-i", str(HERE / "clips" / f)]
    filters.append(
        f"[{i}:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
        f"fps=30,setsar=1,format=yuv420p,trim=duration={t1 - t0:.3f},setpts=PTS-STARTPTS[v{i}]"
    )
    labels.append(f"[v{i}]")

n = len(SHOTS)
end_dur = TOTAL - END_START
args += ["-loop", "1", "-t", f"{end_dur:.3f}", "-i", str(HERE / "endcard" / "endcard-9x16.png")]
frames = int(end_dur * 30)
filters.append(
    f"[{n}:v]scale=1080:1920,zoompan=z='1+0.04*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
    f":d={frames}:s=1080x1920:fps=30,setsar=1,format=yuv420p[v{n}]"
)
labels.append(f"[v{n}]")
args += ["-i", str(HERE / "music" / f"street13-mix-music-v{music}.mp3")]
music_idx = n + 1
filters.append("".join(labels) + f"concat=n={n + 1}:v=1:a=0[base]")

# Street 13 wordmark on the storefront sign: lights up on the beat drop (4.2s) and
# stays on for the rest of the storefront shot.
sign_start, sign_end = 4.2, SHOTS[2][3]
args += ["-loop", "1", "-t", str(TOTAL), "-i", str(HERE / "overlays" / "sign.png")]
filters.append(f"[{music_idx + 1}:v]format=rgba,fade=in:st={sign_start}:d=0.15:alpha=1[sign]")
filters.append(f"[base][sign]overlay=enable='between(t,{sign_start},{sign_end})'[s0]")

# Burned-in captions, timed to the voiceover.
CAPTIONS = [
    ("cap01", 0.10, 1.76), ("cap02", 2.50, 3.64), ("cap03", 4.30, 5.82),
    ("cap04", 6.19, 7.30), ("cap05", 7.35, 8.50), ("cap06", 8.56, 9.75),
    ("cap07", 9.95, 12.55), ("cap08", 12.84, TOTAL),
]
prev = "s0"
for k, (name, a, b) in enumerate(CAPTIONS):
    idx = music_idx + 2 + k
    args += ["-i", str(HERE / "overlays" / f"{name}.png")]
    nxt = "outv" if k == len(CAPTIONS) - 1 else f"c{k}"
    filters.append(f"[{prev}][{idx}:v]overlay=enable='between(t,{a},{b})'[{nxt}]")
    prev = nxt

out = HERE / "street13-always-open-9x16.mp4"
args += ["-filter_complex", ";".join(filters), "-map", "[outv]", "-map", f"{music_idx}:a",
         "-t", str(TOTAL), "-c:v", "libx264", "-preset", "medium", "-crf", "18",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out)]
subprocess.run(args, check=True)
print(out)
