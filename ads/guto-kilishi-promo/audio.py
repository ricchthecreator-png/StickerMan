# 15s soundtrack for the Guto Kilishi promo: afro-trap groove (120 bpm), whoosh on every cut,
# riser into the podium drop, sparkle on the Instagram reveal.  python3 audio.py out.wav
import sys, wave, numpy as np
SR=44100; D=15; N=SR*D; t=np.arange(N)/SR; rng=np.random.default_rng(11)
L=np.zeros(N); R=np.zeros(N)
def add(at,seg,amp=1.0,pan=0.0):
    s=int(at*SR)
    if s>=N or s<0: return
    e=min(len(seg),N-s); L[s:s+e]+=amp*(1-pan)*seg[:e]; R[s:s+e]+=amp*(1+pan)*seg[:e]
def tt(d): return np.arange(int(d*SR))/SR
def kick(): x=tt(.4); f=48+120*np.exp(-x*30); return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-x*9)
def b808(freq,d): x=tt(d); f=freq*(1+.6*np.exp(-x*40)); return np.tanh(2*np.sin(2*np.pi*np.cumsum(f)/SR))*np.exp(-x*2.2)
def clap(): x=tt(.2); n=rng.standard_normal(len(x)); return n*sum((x>=o)*np.exp(-np.clip(x-o,0,None)*45) for o in (0,.01,.022))*.5
def hat(d=.04): x=tt(d); n=rng.standard_normal(len(x)); n=np.diff(n,prepend=0); return n*np.exp(-x*120)
def logdrum(f): x=tt(.3); fs=f*(1+.4*np.exp(-x*50)); return np.sin(2*np.pi*np.cumsum(fs)/SR)*np.exp(-x*10)
def whoosh(d=.35):
    x=tt(d); n=rng.standard_normal(len(x)); k=np.ones(8)/8; n=n-np.convolve(n,k,'same')
    return n*np.sin(np.pi*x/d)**2
def impact():
    x=tt(1.2); return (np.sin(2*np.pi*np.cumsum(38+60*np.exp(-x*8))/SR)*np.exp(-x*2.5)+.3*rng.standard_normal(len(x))*np.exp(-x*12))
beat=0.5; bar=4*beat
# intro texture 0-1.3: low swell + sizzle
add(0,np.sin(2*np.pi*55*tt(1.3))*np.linspace(0,1,int(1.3*SR))**2,.35)
add(0,rng.standard_normal(int(1.3*SR))*np.linspace(.0,.08,int(1.3*SR)))
notes=[55,55,65.41,49]          # A, A, C, G (808 roots)
melody=[440,523,587,523,440,392,440,0]
for b in np.arange(1.3,12.2,beat):
    i=int(round((b-1.3)/beat)); pos=i%8
    if pos in (0,3,6) or (pos==5 and i%16>7): add(b,kick(),.75)
    if pos in (2,6): add(b,clap(),.45)
    for k in range(2): add(b+k*beat/2,hat(),.10 if k else .14,pan=.3)
    if i%16 in (14,15):
        for k in range(4): add(b+k*beat/4,hat(.03),.08,pan=-.3)   # hat roll
    if pos==0: add(b,b808(notes[(i//8)%4],bar*.95),.32)
    m=melody[pos]
    if m and b<10.3: add(b+beat*.5,logdrum(m),.16,pan=-.2)
# riser 10.3 -> 12.4 into the podium drop
x=tt(2.1); n=rng.standard_normal(len(x)); n=n-np.convolve(n,np.ones(4)/4,'same')
add(10.3,n*(x/2.1)**2*.35+np.sin(2*np.pi*np.cumsum(200+1200*(x/2.1)**2)/SR)*(x/2.1)**2*.12)
# whooshes on every cut, impacts on landings
for c in (1.3,2.5,3.6,5.6,6.8,8.0,9.1,10.3,11.3,12.4,13.5): add(c-.17,whoosh(),.4,pan=.4 if int(c*10)%2 else -.4)
add(2.5,impact(),.35); add(11.3,impact(),.55); add(12.75,impact(),.9); add(12.75,b808(41,1.6),.5)
# outro: pad + sparkle when the icon lights up
x=tt(2.2); pad=(np.sin(2*np.pi*220*x)+np.sin(2*np.pi*277*x)+np.sin(2*np.pi*330*x))*np.minimum(x/.4,1)*np.exp(-x*.6)
add(12.8,pad,.08)
for k,f in enumerate((1318,1568,1976,2637)):
    x=tt(.8); add(14.05+k*.06,np.sin(2*np.pi*f*x)*np.exp(-x*6),.12,pan=(k-1.5)*.3)
env=np.clip(np.minimum(t/0.05,(D-t)/0.3),0,1)
out=np.stack([L*env,R*env],1); out=np.tanh(out*1.6)*.9
with wave.open(sys.argv[1],'wb') as f:
    f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR); f.writeframes((out*32767).astype(np.int16).tobytes())
