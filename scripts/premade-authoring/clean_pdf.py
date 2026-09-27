import pymupdf, sys
def clean(path):
    d=pymupdf.open(path)
    n=0
    for x in range(1, d.xref_length()):
        try:
            if d.xref_get_key(x,'OC')[0]!='null' and d.xref_is_stream(x):
                d.update_stream(x, b''); n+=1
        except Exception: pass
    return d,n
if __name__=='__main__':
    d,n=clean(sys.argv[1]); print('blanked',n)
    d[int(sys.argv[2])].get_pixmap(dpi=60).save(sys.argv[3])
