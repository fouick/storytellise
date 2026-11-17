import numpy as np, os
from PIL import Image

src38 = open("make_v38.py").read()
header = src38.split("NX, NY = 0.93")[0]
g = {}
exec(header, g)
rect_mask = g["rect_mask"]; su = g["su"]; h, w = g["h"], g["w"]
xs = g["xs"]; ys = g["ys"]; smooth = g["smooth"]
trace_props = g["trace_props"]; bloc_statique = g["bloc_statique"]; blur1 = g["blur1"]
TRAYS = g["TRAYS"]

PTS_O = np.load("/tmp/opencode/trace_orange_src.npy")
dist_o, nx_o, ny_o, s_o, side_o = trace_props(xs[None,:], ys[:,None], PTS_O)
m_band_o = smooth(np.clip(1 - np.clip((dist_o - 16*su)/(24*su), 0, 1), 0, 1))
# exclusions identiques aux serpenteins : barquettes (au-delà de 12px côté sable) + zones vertes statiques
for (tx0, tx1, ty0, ty1) in TRAYS:
    sd = smooth(np.clip((side_o - 12*su)/(12*su), 0, 1))
    m_band_o = m_band_o * (1 - rect_mask(tx0, tx1, ty0, ty1, 20)[:,:,0] * sd)
m_band_o = bloc_statique(m_band_o[:,:,None])[:,:,0]
m_band_o = m_band_o * (1 - rect_mask(1385, 1745, 240, 445, 8)[:,:,0])   # barquette haute droite verrouillée
m_band_o = m_band_o * (1 - rect_mask(1065, 1395, 205, 428, 8)[:,:,0])   # barquette haute gauche verrouillée
m_band_o = blur1(m_band_o, 1.5)
print("bande orange: px >0.3 =", int((m_band_o > 0.3).sum()))

# base : flow-13 (courant)
g13 = Image.open("/Users/fouick/Documents/GitHub/storytellise/cascade-flow-13.gif")
g03 = Image.open("/tmp/opencode/cascade-v32.gif")
pal_list = g03.getpalette()[:768]
pal_rgb = np.array(pal_list, dtype=np.int32).reshape(-1, 3)
N = 56; NW = 28
f13 = []
for i in range(N):
    g13.seek(i); f13.append(np.asarray(g13.convert("RGB")).astype(np.float32))

pal_keys = pal_rgb[:,0].astype(np.int64)*65536 + pal_rgb[:,1]*256 + pal_rgb[:,2]
order = np.argsort(pal_keys); sk_ = pal_keys[order]; si_ = order
def exact_index(rgb):
    k = rgb[:,:,0].astype(np.int64)*65536 + rgb[:,:,1].astype(np.int64)*256 + rgb[:,:,2].astype(np.int64)
    pos = np.clip(np.searchsorted(sk_, k), 0, len(sk_)-1)
    return si_[pos], sk_[pos] == k

frames_out = []; frames_idx = []
for i in range(N):
    t = 2*np.pi*(i % NW)/NW
    out = f13[i].copy()
    # ressac identique aux serpenteins : flot rapide, jusant lent, crête voyageuse
    th = t + s_o/(280.0*su)
    dA = 8.0*np.sin(th - 0.45*np.sin(th))       # va-et-vient franc (±8 px)
    sx_r = np.clip(np.round(xs[None,:] - nx_o*dA).astype(np.int32), 0, w-1)
    sy_r = np.clip(np.round(ys[:,None] - ny_o*dA).astype(np.int32), 0, h-1)
    rows = np.arange(h)[:, None]
    out = out*(1 - m_band_o[:,:,None]) + f13[i][rows[np.arange(h)[:,None]*0+0], :][np.arange(h)[:,None]*0+0]*0  # placeholder
    out = f13[i].copy()
    lapped = f13[i][sy_r, sx_r]
    out = out*(1 - m_band_o[:,:,None]) + lapped*m_band_o[:,:,None]
    # respiration lumineuse liée à la vague (rend le mouvement lisible même sur l'eau lisse)
    crest = np.clip(np.sin(th - 0.45*np.sin(th)), 0, 1)**2          # crête de la vague
    out = out*(1 - m_band_o[:,:,None]*crest[:,:,None]*0.35) +           np.clip(out*1.35 + 18, 0, 255)*m_band_o[:,:,None]*crest[:,:,None]*0.35
    out = np.clip(out * (1 + 0.08*m_band_o[:,:,None]*np.sin(th - 0.45*np.sin(th) + 0.6)[:,:,None]), 0, 255)
    out8 = np.clip(out, 0, 255).astype(np.uint8)
    frames_out.append(out8)
    idx, ok = exact_index(out8)
    bad = (m_band_o > 0.01) & ~ok
    if bad.any():
        px = out8[bad].astype(np.float32)
        d2 = ((px[:, None, :] - pal_rgb[None, :, :])**2).sum(axis=2)
        idx[bad] = d2.argmin(axis=1)
    frames_idx.append(idx.astype(np.uint8))

img0 = Image.fromarray(frames_idx[0], mode="P"); img0.putpalette(pal_list)
frames_p = [img0]
for i in range(1, N):
    im = Image.fromarray(frames_idx[i], mode="P"); im.putpalette(pal_list)
    frames_p.append(im)
OUT = "/tmp/opencode/cascade-v58.gif"
frames_p[0].save(OUT, save_all=True, append_images=frames_p[1:], duration=150, loop=0, optimize=True)
print("GIF v58:", os.path.getsize(OUT)//1024, "Ko")

os.makedirs("/tmp/opencode/v58_frames", exist_ok=True)
for i, fr in enumerate(frames_out):
    Image.fromarray(fr).save("/tmp/opencode/v58_frames/frame_%03d.png" % i)

# vérification : seule la bande orange change vs flow-13
g48 = Image.open(OUT)
for i in [14, 28, 42]:
    g48.seek(i); a = np.asarray(g48.convert("RGB")).astype(np.int32)
    dd = np.abs(a - f13[i].astype(np.int32)).sum(axis=2)
    inband = (m_band_o > 0.01)
    hors = (dd > 15) & ~inband
    ciel = (dd[0:150, 0:365] > 15).sum()
    print(f"trame {i}: modifiés hors bande = {hors.sum()} (0 attendu) | ciel = {ciel} | dans bande = {(dd > 15).sum() - hors.sum()}")
