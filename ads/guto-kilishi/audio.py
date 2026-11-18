# 10s sound bed for the Guto Kilishi ad: light afro-groove (108 bpm) + hits synced to visuals.
# python3 audio.py out.wav
import sys, wave, numpy as np
SR=44100; N=SR*10; t=np.arange(N)/SR; rng=np.random.default_rng(9)
mix=np.zeros(N)
def add(at,seg,amp=1.0):
    s=int(at*SR)
    if s>=N: return
    e=min(len(seg),N-s); mix[s:s+e]+=amp*seg[:e]
def tt(d): return np.arange(int(d*SR))/SR
def kick(f0=50,d=.45):
    x=tt(d); f=f0+100*np.exp(-x*28); return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-x*8)
def shaker(d=.06):
    x=tt(d); return rng.standard_normal(len(x))*np.exp(-x*70)
def clap(d=.18):
    x=tt(d); n=rng.standard_normal(len(x)); e=sum(np.exp(-np.clip(x-o,0,None)*60)*(x>=o) for o in (0,.012,.024)); return n*e*.6
def logdrum(f,d=.35):
    x=tt(d); fs=f*(1+.5*np.exp(-x*40)); return np.sin(2*np.pi*np.cumsum(fs)/SR)*np.exp(-x*9)
beat=60/108; start=2.6   # groove kicks in when the pack drops
b=start
while b<9.7:
    i=round((b-start)/beat)
    add(b,kick(),.55)
    add(b+beat*.75,kick(),.3) if i%2==1 else None
    if i%2==1: add(b,clap(),.35)
    for k in range(4): add(b+k*beat/4,shaker(),.06 if k%2 else .1)
    notes=[55,55,65.4,73.4]; add(b+beat*.5,logdrum(notes[i%4]*2),.35)
    b+=beat
# intro: warm pad + sizzle
pad=(np.sin(2*np.pi*110*t)+.5*np.sin(2*np.pi*164.8*t)+.4*np.sin(2*np.pi*220.5*t))*.04
mix+=pad*np.clip(1-(t-2.6)/0.4,0,1)*np.clip(t/0.5,0,1)
n=rng.standard_normal(N); lp=np.convolve(n,np.ones(12)/12,'same'); mix+=.025*lp*(t<2.8)
# impact hits (match IMPACTS in ad.html)
for at,a in [(.4,.7),(1.05,.75),(2.95,1.0),(3.55,.4),(8.25,.5),(8.6,.6)]: add(at,kick(42,.6),a)
# whoosh into the red wipe
w=np.exp(-((t-2.55)/0.13)**2); mix+=.3*w*(n-lp)/np.abs(n-lp).max()
# badge pops + text pops
for at in (3.5,3.85,5.45,6.05,6.65):
    x=tt(.25); add(at,np.sin(2*np.pi*(700+500*np.exp(-x*30))*x)*np.exp(-x*20),.22)
# CTA ding
x=tt(1.0); add(9.0,(np.sin(2*np.pi*1046*x)+.5*np.sin(2*np.pi*1568*x))*np.exp(-x*4.5),.22)
mix*=np.clip(np.minimum(t/0.15,(10-t)/0.35),0,1)
mix=np.tanh(mix*1.3)*.85
with wave.open(sys.argv[1],'wb') as f:
    f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes((mix*32767).astype(np.int16).tobytes())
