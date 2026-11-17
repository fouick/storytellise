import numpy as np, os
from PIL import Image, ImageFilter

src = open("make_v38.py").read()
header = src.split("NX, NY = 0.93")[0]
g = {}
exec(header, g)
pink_bands = g["pink_bands"]; ys = g["ys"]; h, w = g["h"], g["w"]
NW = 28

g32 = Image.open("/tmp/opencode/cascade-v32.gif")
pal_list = g32.getpalette()[:768]
pal_rgb = np.array(pal_list, dtype=np.int32).reshape(-1, 3)
N = 56
f32 = []
for i in range(N):
    g32.seek(i)
    f32.append(np.asarray(g32.convert("RGB")).astype(np.float32))
print("trames:", len(f32), f32[0].shape)

# LUT couleur -> index (pour les pixels intouchés)
pal_keys = pal_rgb[:,0].astype(np.int64)*65536 + pal_rgb[:,1]*256 + pal_rgb[:,2]
order = np.argsort(pal_keys)
sorted_keys = pal_keys[order]
sorted_idx = order

def exact_index(rgb_uint8):
    k = rgb_uint8[:,:,0].astype(np.int64)*65536 + rgb_uint8[:,:,1].astype(np.int64)*256 + rgb_uint8[:,:,2].astype(np.int64)
    pos = np.searchsorted(sorted_keys, k)
    pos = np.clip(pos, 0, len(sorted_keys)-1)
    ok = sorted_keys[pos] == k
    return sorted_idx[pos], ok

frames_out_rgb = []
frames_out_idx = []
for i in range(N):
    t = 2*np.pi*(i % NW)/NW
    out = f32[i].copy()
    touched = np.zeros((h, w), bool)
    for k in range(len(pink_bands)):
        phk = k * 0.4
        ddy_k = 2.2*np.sin(t - 0.45*np.sin(t) + phk)      # mouvement identique aux silhouettes
        ys_k = np.clip(np.round(ys[:,None] - ddy_k).astype(np.int32), 0, h-1)[:, 0].astype(np.int32)
        m_k = pink_bands[k][:, :, 0]
        out = out*(1 - m_k[:,:,None]) + f32[i][ys_k]*m_k[:,:,None]
        touched |= (m_k > 0.01)
    out8 = np.clip(out, 0, 255).astype(np.uint8)
    frames_out_rgb.append(out8)
    new_idx, ok = exact_index(out8)
    # pixels touchés sans correspondance exacte : plus proche couleur
    bad = touched & ~ok
    if bad.any():
        px = out8[bad].astype(np.float32)
        d2 = ((px[:, None, :] - pal_rgb[None, :, :])**2).sum(axis=2)
        new_idx[bad] = d2.argmin(axis=1)
    frames_out_idx.append(new_idx.astype(np.uint8))

img0 = Image.fromarray(frames_out_idx[0], mode="P")
img0.putpalette(pal_list)
frames_p = [img0]
for i in range(1, N):
    im = Image.fromarray(frames_out_idx[i], mode="P")
    im.putpalette(pal_list)
    frames_p.append(im)
OUT = "/tmp/opencode/cascade-v41.gif"
frames_p[0].save(OUT, save_all=True, append_images=frames_p[1:], duration=150, loop=0, optimize=True)
print("GIF v41:", os.path.getsize(OUT)//1024, "Ko")

os.makedirs("/tmp/opencode/v41_frames", exist_ok=True)
for i, fr in enumerate(frames_out_rgb):
    Image.fromarray(fr).save("/tmp/opencode/v41_frames/frame_%03d.png" % i)

# VÉRIFICATION : rendu décodé vs référence, hors bandes roses
g41 = Image.open(OUT)
PINK = np.load("/tmp/opencode/pink_boxes.npy")
# zone réelle = union des bandes (avec leur fondu)
pink_zone = np.zeros((h, w), bool)
for bk in pink_bands:
    pink_zone |= (bk[:, :, 0] > 0.001)
tot_hors = 0; tot_dans = 0
for i in [0, 9, 14, 28, 42]:
    g41.seek(i)
    a = np.asarray(g41.convert("RGB")).astype(np.int32)
    dd = np.abs(a - f32[i].astype(np.int32)).sum(axis=2)
    m = dd > 0
    tot_hors += (m & ~pink_zone).sum(); tot_dans += (m & pink_zone).sum()
print("V5 trames — hors zones roses:", tot_hors, "(attendu 0) | dans zones roses:", tot_dans)
