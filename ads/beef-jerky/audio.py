# Synthesizes a 10s sound bed (drone + sizzle + hits synced to the visuals): python3 audio.py out.wav
import sys, wave, numpy as np
SR=44100; N=SR*10; t=np.arange(N)/SR; rng=np.random.default_rng(3)
mix=np.zeros(N)
# warm low drone with slow swell
mix+=0.07*(np.sin(2*np.pi*55*t)+0.6*np.sin(2*np.pi*82.5*t))*(0.6+0.4*np.sin(2*np.pi*0.2*t))
# fire sizzle: one-pole lowpassed noise with crackle
n=rng.standard_normal(N); lp=np.zeros(N); a=0.08
for i in range(1,N): lp[i]=lp[i-1]+a*(n[i]-lp[i-1])
crackle=(rng.random(N)<0.0009)*rng.standard_normal(N)*0.6
mix+=0.05*lp/np.abs(lp).max()+np.convolve(crackle,np.exp(-np.arange(200)/30),'same')*0.15
def env(start,dur,decay):
    e=np.zeros(N); s=int(start*SR); k=np.arange(min(int(dur*SR),N-s)); e[s:s+len(k)]=np.exp(-k/SR*decay); return e
def kick(at,amp=0.8):
    s=int(at*SR); k=np.arange(int(0.5*SR)); tt=k/SR
    f=45+90*np.exp(-tt*25); ph=2*np.pi*np.cumsum(f)/SR
    seg=amp*np.sin(ph)*np.exp(-tt*7); e=min(len(seg),N-s); mix[s:s+e]+=seg[:e]
for at,amp in [(.35,.8),(.95,.85),(2.36,1.0),(3.1,.6),(8.2,.7),(8.5,.8)]: kick(at,amp)
# whoosh into the cut
w=np.exp(-((t-2.08)/0.12)**2); hp=n-lp; mix+=0.35*w*hp/np.abs(hp).max()
# badge pops
for at in (5.3,5.9,6.5):
    mix+=0.25*np.sin(2*np.pi*(660+400*np.exp(-(t-at)*30))*t)*env(at,.25,22)
# CTA ding
mix+=0.22*(np.sin(2*np.pi*988*t)+0.5*np.sin(2*np.pi*1482*t))*env(8.9,1.1,4.5)
mix*=np.clip(np.minimum(t/0.2,(10-t)/0.4),0,1)
mix=np.tanh(mix*1.2)*0.85
pcm=(mix*32767).astype(np.int16)
with wave.open(sys.argv[1],'wb') as f:
    f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(pcm.tobytes())
