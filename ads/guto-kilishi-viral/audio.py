# Sound design for the Guto Kilishi viral ad.
# Reads events.json (exported from the same timeline that drives the visuals), so every SFX is frame-synced.
# python3 audio.py events.json out.wav
import sys, json, wave, numpy as np
SR=44100; D=12; N=SR*D; rng=np.random.default_rng(7)
ev=json.load(open(sys.argv[1]))
L=np.zeros(N); R=np.zeros(N); ML=np.zeros(N); MR=np.zeros(N)
def tt(d): return np.arange(int(d*SR))/SR
def put(at,seg,amp=1.0,pan=0.0,music=False):
    s=int(round(at*SR)); 
    if s>=N: return
    if s<0: seg=seg[-s:]; s=0
    e=min(len(seg),N-s); a,b=(ML,MR) if music else (L,R)
    a[s:s+e]+=amp*(1-pan)*seg[:e]; b[s:s+e]+=amp*(1+pan)*seg[:e]
def noise(d): return rng.standard_normal(int(d*SR))
def hp(x,k=6): return x-np.convolve(x,np.ones(k)/k,'same')
def lp(x,k=12): return np.convolve(x,np.ones(k)/k,'same')
def sweep(f0,f1,d,curve=1.0):
    x=tt(d); f=f0+(f1-f0)*(x/d)**curve; return np.sin(2*np.pi*np.cumsum(f)/SR)
def mix(*segs):
    n=max(len(x) for x in segs); return sum(np.pad(x,(0,n-len(x))) for x in segs)
def env(d,a=.005,dec=8.0): x=tt(d); return np.minimum(x/a,1)*np.exp(-x*dec)

# ---------------- SFX library ----------------
def sfx_rumble(p):
    d=p.get('dur',.4); x=tt(d); r=lp(noise(d),40)*6+np.sin(2*np.pi*42*x)*.8
    return r*(x/d)**1.5*(.7+.3*np.sin(2*np.pi*14*x))
def sfx_rip(p):          # zipper-like tear: dense crackle with fast AM, bright
    d=.2; x=tt(d); n=hp(noise(d),3); am=(np.sin(2*np.pi*90*x)>0)*.6+.4
    grains=(rng.random(len(x))<.02)*rng.standard_normal(len(x))*3
    return (n*am+grains)*np.minimum(x/.01,1)*np.exp(-x*9)*.9
def sfx_impact(d=1.4,f0=95,f1=32):
    x=tt(d); sub=np.sin(2*np.pi*np.cumsum(f1+(f0-f1)*np.exp(-x*9))/SR)*np.exp(-x*2.4)
    crack=noise(d)*np.exp(-x*22)*.8
    return np.tanh((sub*1.2+crack)*1.5)
def sfx_burst(p):        # pack explodes: big impact + crunchy debris
    d=1.0; x=tt(d); deb=sum((rng.random(len(x))<.004*np.exp(-x*4))*rng.standard_normal(len(x))*1.5 for _ in range(2))
    deb=np.convolve(deb,np.exp(-np.arange(300)/40),'same')
    return mix(sfx_impact(1.4),deb*.6)
def sfx_whoosh(p):
    d=p.get('dur',.3); x=tt(d); n=noise(d); 
    k=int(2+10*(1-0)); band=hp(lp(n,3),12)
    sh=np.sin(np.pi*x/d)**2 if not p.get('down') else (x/d)**2
    return band*sh*1.4
def sfx_slam(p):         # word slam: punchy kick + snare crack + tonal stab
    pt=p.get('pitch',1); d=.45; x=tt(d)
    kick=np.sin(2*np.pi*np.cumsum(50*pt+140*np.exp(-x*35))/SR)*np.exp(-x*10)
    snap=hp(noise(d),4)*np.exp(-x*30)*.7
    stab=(np.sin(2*np.pi*220*pt*x)+.5*np.sin(2*np.pi*330*pt*x))*np.exp(-x*12)*.25
    return np.tanh((kick+snap+stab)*1.6)
def sfx_slam_big(p):
    return mix(sfx_slam({'pitch':.8})*.8,sfx_impact(1.0,120,40)*.7)
def sfx_clink(p):        # metallic crown landing
    d=1.2; x=tt(d); s=sum(a*np.sin(2*np.pi*f*x)*np.exp(-x*dk) for f,a,dk in ((2093,1,4),(3322,.6,5),(5274,.4,7),(1567,.5,3.5),(7040,.2,10)))
    return (s*np.minimum(x/.002,1)+hp(noise(d),3)*np.exp(-x*60)*.6)*.6
def sfx_thud(p): x=tt(.6); return np.tanh(np.sin(2*np.pi*np.cumsum(40+70*np.exp(-x*25))/SR)*np.exp(-x*7)*2+lp(noise(.6),20)*np.exp(-x*15)*2)
def sfx_pop(p):
    pt=p.get('pitch',1); x=tt(.18); return np.sin(2*np.pi*np.cumsum(500*pt+900*pt*np.exp(-x*40))/SR)*np.exp(-x*22)
def sfx_fire(p):         # roaring flames + sizzle, swelling with the meter
    d=p.get('dur',1.7); x=tt(d); roar=lp(noise(d),30)*5*(.4+.6*(x/d))
    crack=np.convolve((rng.random(len(x))<.003)*rng.standard_normal(len(x)),np.exp(-np.arange(150)/20),'same')*1.5
    sizzle=hp(noise(d),2)*.25*(x/d)
    return (roar+crack+sizzle)*np.minimum(x/.15,1)*np.minimum((d-x)/.08,1)
def sfx_tick(p): pt=p.get('pitch',1); x=tt(.05); return np.sin(2*np.pi*1800*pt*x)*np.exp(-x*90)
def sfx_boom(p): return sfx_impact(2.0,80,28)
def sfx_slash(p):        # blade "shing" + air
    d=.35; x=tt(d); shing=sum(np.sin(2*np.pi*np.cumsum(f*(1-.35*x/d))/SR)*.5 for f in (3600,5100))*np.exp(-x*9)
    air=hp(noise(d),3)*np.sin(np.pi*np.clip(x/.18,0,1))**2
    return shing*.5+air
def sfx_crunch(p):       # dense crispy grains + jaw thump
    pt=p.get('pitch',1); d=.32; x=tt(d)
    g=(rng.random(len(x))<.05*np.exp(-x*9))*rng.standard_normal(len(x))*2.2
    g=hp(np.convolve(g,np.exp(-np.arange(60)/(8/pt)),'same'),3)
    thump=np.sin(2*np.pi*np.cumsum(70+60*np.exp(-x*30))/SR)*np.exp(-x*14)*.8
    return np.tanh((g+thump)*1.3)
def sfx_shutter(p):
    x=tt(.12); c=lambda o:(x>=o)*hp(noise(.12),2)*np.exp(-np.clip(x-o,0,None)*120)
    return (c(0)+c(.055)*.8)*.9+sfx_slam({'pitch':1.3})[:len(x)]*.3
def sfx_riser(p):
    d=p.get('dur',.5); x=tt(d); return (hp(noise(d),4)*.5+sweep(300,2400,d,2)*.35)*(x/d)**2
def sfx_sparkle(p):
    out=np.zeros(int(1.2*SR))
    for k,f in enumerate((1568,2093,2637,3136,4186)):
        s=int(k*.05*SR); x=tt(1.2-k*.05); out[s:s+len(x)]+=np.sin(2*np.pi*f*x)*np.exp(-x*5)*.5
    return out
def sfx_shimmer(p):  # reverse-swell into a bright sparkle
    sp=sfx_sparkle(p); rev=sp[::-1][-int(.4*SR):]*np.linspace(0,1,int(.4*SR))**2
    return np.concatenate([rev*.6,sp])
LIB={'rumble':(sfx_rumble,.5),'rip':(sfx_rip,.85),'burst':(sfx_burst,1.0),'whoosh':(sfx_whoosh,.5),'slam':(sfx_slam,.75),
     'slam_big':(sfx_slam_big,.9),'clink':(sfx_clink,.7),'thud':(sfx_thud,.8),'pop':(sfx_pop,.45),'fire':(sfx_fire,.35),
     'tick':(sfx_tick,.25),'boom':(sfx_boom,.95),'slash':(sfx_slash,.7),'crunch':(sfx_crunch,1.0),'shutter':(sfx_shutter,.7),
     'riser':(sfx_riser,.45),'sparkle':(sfx_sparkle,.35),'shimmer':(sfx_shimmer,.35)}

# ---------------- music bed (120 bpm afro-trap) ----------------
on=[e['t'] for e in ev if e['type']=='music_on']; off=[e['t'] for e in ev if e['type']=='music_off']
def music_live(t):
    last_on=max([o for o in on if o<=t],default=None); last_off=max([o for o in off if o<=t],default=-1)
    return last_on is not None and last_on>last_off
def kick(): x=tt(.4); return np.sin(2*np.pi*np.cumsum(48+120*np.exp(-x*30))/SR)*np.exp(-x*9)
def clap(): x=tt(.2); n=noise(.2); return n*sum((x>=o)*np.exp(-np.clip(x-o,0,None)*45) for o in (0,.01,.022))*.5
def hat(d=.04): x=tt(d); return hp(noise(d),2)*np.exp(-x*120)
def b808(f,d): x=tt(d); return np.tanh(2*np.sin(2*np.pi*np.cumsum(f*(1+.6*np.exp(-x*40)))/SR))*np.exp(-x*2)
def logd(f): x=tt(.3); return np.sin(2*np.pi*np.cumsum(f*(1+.4*np.exp(-x*50)))/SR)*np.exp(-x*10)
beat=.5; roots=[55,55,65.41,49]; mel=[880,0,784,659,0,587,659,0]
for k in range(int(D/ (beat/2))):
    b=k*beat/2; 
    if not music_live(b): continue
    i=k//2; pos=i%8; half=k%2
    words=1.25<=b<2.5
    if not half:
        if pos in (0,3,6) or (pos==5 and i%16>7): put(b,kick(),.7,music=True)
        if pos in (2,6): put(b,clap(),.4,music=True)
        if pos==0: put(b,b808(roots[(i//8)%4],2*beat*.95*2),.3,music=True)
        if mel[pos] and b<10: put(b,logd(mel[pos]),.11,-.25,music=True)
    put(b,hat(),.09 if half else .12,.3,music=True)
    if words: put(b+beat/4,hat(.03),.07,-.3,music=True)   # 16th hats under the word slams
# end card: warm chord pad under the CTA
x=tt(2.0); pad=sum(np.sin(2*np.pi*f*x) for f in (220,277.2,329.6,440))*np.minimum(x/.3,1)*np.exp(-x*.5)
put(10.0,pad,.05,music=True)

# ---------------- place SFX from the shared timeline ----------------
for e in ev:
    fn=LIB.get(e['type']); 
    if not fn: continue
    f,amp=fn; seg=f(e); seg=seg/ (np.abs(seg).max()+1e-9)
    pre=.04 if e['type'] in ('whoosh',) else 0
    put(e['t']-pre-(.4 if e['type']=='shimmer' else 0),seg,amp,e.get('pan',0))

# sidechain-ish duck: music dips under each hit
duck=np.ones(N)
for e in ev:
    if e['type'] in ('burst','slam','slam_big','boom','crunch','thud','clink'):
        s=int(e['t']*SR); x=tt(.35); d=1-.55*np.exp(-x*10); e2=min(len(d),N-s); duck[s:s+e2]=np.minimum(duck[s:s+e2],d[:e2])
L+=ML*duck; R+=MR*duck
out=np.stack([L,R],1)
tail=np.clip((D-np.arange(N)/SR)/.25,0,1)[:,None]
out=np.tanh(out*1.5)*.92*tail
with wave.open(sys.argv[2],'wb') as f:
    f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR); f.writeframes((out*32767).astype(np.int16).tobytes())
print('events placed:',sum(1 for e in ev if e['type'] in LIB))
