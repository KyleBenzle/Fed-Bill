#!/bin/bash
# usage: render.sh name  (expects out/name.docx) -> out/name.pdf, render/name-N.png, render/name_sheet.png
set -e
cd "$(dirname "$0")/.."
n=$1
soffice --headless --convert-to pdf --outdir out "out/$n.docx" >/dev/null 2>&1
rm -f render/$n-*.png
pdftoppm -r ${2:-70} -png "out/$n.pdf" "render/$n"
/tmp/lv/bin/python - "$n" <<'PY'
import sys,glob
from PIL import Image
n=sys.argv[1]
fs=sorted(glob.glob(f'render/{n}-*.png'))
ims=[Image.open(f) for f in fs]
w,h=ims[0].size; cols=min(3,len(ims)); rows=(len(ims)+cols-1)//cols
m=Image.new('RGB',(w*cols,h*rows),'white')
for i,im in enumerate(ims): m.paste(im,((i%cols)*w,(i//cols)*h))
m.save(f'render/{n}_sheet.png'); print(n, len(ims),'pages')
PY
