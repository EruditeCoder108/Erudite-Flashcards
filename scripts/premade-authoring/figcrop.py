import sys, json, io
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pymupdf
from PIL import Image
from clean_pdf import clean
def export(pdf, crops, outdir, long_side=1000):
    d,_=clean(pdf); info={}
    for name,(page,r) in crops.items():
        R=pymupdf.Rect(*r); z=long_side/max(R.width,R.height)
        pix=d[page].get_pixmap(clip=R, matrix=pymupdf.Matrix(z,z), alpha=False)
        img=Image.open(io.BytesIO(pix.tobytes('png'))).convert('RGB')
        path=f'{outdir}/{name}.webp'; img.save(path,'WEBP',quality=82,method=6)
        words=[[w[4]]+[round((w[0]-R.x0)*z),round((w[1]-R.y0)*z),round((w[2]-w[0])*z),round((w[3]-w[1])*z)] for w in d[page].get_text('words',clip=R)]
        info[name]={'size':img.size,'words':words}
        import os; print(name, img.size, os.path.getsize(path)//1024,'KB', words)
    return info
