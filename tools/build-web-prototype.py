"""Build the web prototype into one self-contained HTML page.

Embeds Pretendard (brand/fonts) as woff2, subset to the characters the page uses.
usage: python3 tools/build-web-prototype.py channels/web/prototype/src.html <out.html>
needs: pip install fonttools brotli
"""
import base64
import io
import pathlib
import sys

from fontTools import subset
from fontTools.ttLib import TTFont

root = pathlib.Path(__file__).resolve().parent.parent
src_path, out_path = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
src = src_path.read_text(encoding='utf-8')
assert '/* FONTS */' in src, 'source needs a /* FONTS */ placeholder'

chars = set(src) | {chr(c) for c in range(0x20, 0x7F)} | set('·▸—→')
text = ''.join(sorted(c for c in chars if ord(c) >= 0x20))

faces = []
for weight, name in [(400, 'Regular'), (600, 'SemiBold'), (700, 'Bold')]:
    opts = subset.Options()
    opts.flavor = 'woff2'
    opts.layout_features = ['tnum', 'kern', 'liga']
    font = TTFont(root / 'brand' / 'fonts' / f'Pretendard-{name}.woff2')
    sub = subset.Subsetter(options=opts)
    sub.populate(text=text)
    sub.subset(font)
    buf = io.BytesIO()
    font.flavor = 'woff2'
    font.save(buf)
    data = base64.b64encode(buf.getvalue()).decode()
    faces.append(
        f'@font-face{{font-family:"Pretendard";font-weight:{weight};font-style:normal;'
        f'font-display:swap;src:url(data:font/woff2;base64,{data}) format("woff2");}}'
    )

out_path.write_text(src.replace('/* FONTS */', '\n'.join(faces)), encoding='utf-8')
print(out_path, len(out_path.read_bytes()), 'bytes')
