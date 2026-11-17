import numpy as np, os
from PIL import Image

src38 = open("make_v38.py").read()
header = src38.split("NX, NY = 0.93")[0]
g = {}
exec(header, g)
rect_mask = g["rect_mask"]; su = g["su"]; h, w = g["h"], g["w"]

# base : flow-10 (la version validée) ; référence à figer : v32/flow-03
g10 = Image.open("/Users/fouick/Documents/GitHub/storytellise/cascade-flow-10.gif")
g03 = Image.open("/tmp/opencode/cascade-v32.gif")
pal_list = g03.getpalette()[:768]
pal_rgb = np.array(pal_list, dtype=np.int32).reshape(-1, 3)
N = 56
f10, f03 = [], []
for i in range(N):
    g10.seek(i); f10.append(np.asarray(g10.convert("RGB")).astype(np.float32))
    g03.seek(i); f03.append(np.asarray(g03.convert("RGB")).astype(np.float32))

# bloc haut-gauche à figer (ciel, pale mer, barrage au-dessus de la cascade)
freeze = rect_mask(-50, 1150, -50, 500, 30)     # (x0, x1, y0, y1) — ordre correct !
print("freeze max:", freeze.max(), "| px >0.5:", int((freeze[:,:,0] > 0.5).sum()))

# LUT index exact
pal_keys = pal_rgb[:,0].astype(np.int64)*65536 + pal_rgb[:,1]*256 + pal_rgb[:,2]
order = np.argsort(pal_keys); sorted_keys = pal_keys[order]; sorted_idx = order
def exact_index(rgb):
    k = rgb[:,:,0].astype(np.int64)*65536 + rgb[:,:,1].astype(np.int64)*256 + rgb[:,:,2].astype(np.int64)
    pos = np.clip(np.searchsorted(sorted_keys, k), 0, len(sorted_keys)-1)
    return sorted_idx[pos], sorted_keys[pos] == k

frames_out = []; frames_idx = []
for i in range(N):
    fz = freeze[:, :, 0]
    out = f10[i]*(1 - fz[:,:,None]) + f03[i]*fz[:,:,None]
    out8 = np.clip(out, 0, 255).astype(np.uint8)
    frames_out.append(out8)
    idx, ok = exact_index(out8)
    bad = (fz > 0.001) & ~ok
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
OUT = "/tmp/opencode/cascade-v47.gif"
frames_p[0].save(OUT, save_all=True, append_images=frames_p[1:], duration=150, loop=0, optimize=True)
print("GIF v47:", os.path.getsize(OUT)//1024, "Ko")

os.makedirs("/tmp/opencode/v47_frames", exist_ok=True)
for i, fr in enumerate(frames_out):
    Image.fromarray(fr).save("/tmp/opencode/v47_frames/frame_%03d.png" % i)

# vérifications
g47 = Image.open(OUT)
for i in [14, 28, 42]:
    g47.seek(i); a = np.asarray(g47.convert("RGB")).astype(np.int32)
    dz_haut = np.abs(a - f03[i].astype(np.int32)).sum(axis=2)   # vs référence dans le bloc figé
    dz_bas  = np.abs(a - f10[i].astype(np.int32)).sum(axis=2)   # vs flow-10 sous le bloc
    haut = (dz_haut[0:150, 0:365] > 15).sum()      # y<150 frame, x<365 = bloc figé
    bas  = (dz_bas[170:, :] > 15).sum()            # y>170 frame = zone feuilles
    print(f"trame {i}: bloc figé vs réf = {haut} (0 attendu) | bas vs flow-10 = {bas} (0 attendu)")
