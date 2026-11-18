import os, glob, sys
from PIL import Image, ImageOps

BASE = r"C:\Users\publi\Documents\deepseek-harness\default-workspace\delta-interactive\cast_original"
CW, CH, M, G = 840, 474, 2, 4
W, H = 2532, 956

NAMES = ["红狼", "蜂医", "比特", "赛伊德", "雷斯", "德穆兰",
         "哈德森", "格赫罗斯", "渡鸦", "哈夫克小兵", "阿萨拉卫队小兵"]

only = sys.argv[1:] if len(sys.argv) > 1 else NAMES
ok, missing = 0, []

for name in only:
    files = sorted(glob.glob(os.path.join(BASE, name + "_0[1-6]_*.png")))
    if len(files) != 6:
        missing.append((name, len(files)))
        continue
    canvas = Image.new("RGB", (W, H), (43, 43, 43))
    for i, f in enumerate(files):
        im = Image.open(f).convert("RGB")
        if im.size != (1672, 941):
            im = ImageOps.fit(im, (1672, 941), Image.LANCZOS)
            im.save(f, "PNG")
        cell = ImageOps.fit(im, (CW, CH), Image.LANCZOS)
        r, c = divmod(i, 3)
        canvas.paste(cell, (M + c * (CW + G), M + r * (CH + G)))
    out = os.path.join(BASE, name + "_六宫格.png")
    canvas.save(out, "PNG", optimize=True)
    print("OK", name, round(os.path.getsize(out) / 1024), "KB")
    ok += 1

print("built:", ok, "missing:", missing)
