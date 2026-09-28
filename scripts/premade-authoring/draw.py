"""Self-drawn diagrams (free-body diagrams, graphs, vectors) saved as .webp card images.

Owner rule for physics: when an NCERT figure is cluttered or uses odd notation, draw a clean
one here instead. Build an SVG with Fig, then fig.save(media, name). PyMuPDF rasterises it
(it ignores <marker>, so arrows are drawn as explicit heads). Warm paper colours, dark ink.
Phone rule: keep the canvas about 600–650 units wide and text >= 19, so labels stay readable
when the image is shown ~340 px wide.

    f = Fig(400, 260)
    f.arrow(50, 200, 300, 200, cls='f1'); f.text(305, 205, 'x')
    f.label(120, 90, 'F', sub='net')
    f.save(MEDIA, 'fbd_block')
"""
import io, math, os
import pymupdf
from PIL import Image

INK, PAPER = '#1f2430', '#fbf8f1'
COL = {'ink': INK, 'blue': '#1d5fd6', 'red': '#c93b3f', 'green': '#1f8a4c', 'orange': '#c77700',
       'purple': '#7c3aed', 'grey': '#8a8373', 'light': '#d9d2c3'}
FONT = 'font-family="serif"'


def _esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


class Fig:
    def __init__(self, w, h, bg=PAPER):
        self.w, self.h, self.parts = w, h, []
        if bg:
            self.parts.append(f'<rect width="{w}" height="{h}" fill="{bg}"/>')

    def raw(self, s):
        self.parts.append(s); return self

    def line(self, x1, y1, x2, y2, c='ink', w=2, dash=None):
        da = f' stroke-dasharray="{dash}"' if dash else ''
        self.parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{COL.get(c, c)}" stroke-width="{w}" stroke-linecap="round"{da}/>')
        return self

    def arrow(self, x1, y1, x2, y2, c='ink', w=2.4, head=11, dash=None):
        ang = math.atan2(y2 - y1, x2 - x1)
        bx, by = x2 - head * 0.8 * math.cos(ang), y2 - head * 0.8 * math.sin(ang)
        self.line(x1, y1, bx, by, c, w, dash)
        pts = [(x2, y2)] + [(x2 - head * math.cos(ang + s * 0.42), y2 - head * math.sin(ang + s * 0.42)) for s in (1, -1)]
        self.parts.append('<polygon points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + f'" fill="{COL.get(c, c)}"/>')
        return self

    def poly(self, pts, c='ink', w=2, fill='none', closed=False, dash=None):
        tag = 'polygon' if closed else 'polyline'
        da = f' stroke-dasharray="{dash}"' if dash else ''
        f = COL.get(fill, fill)
        self.parts.append(f'<{tag} points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) +
                          f'" fill="{f}" stroke="{COL.get(c, c)}" stroke-width="{w}" stroke-linejoin="round"{da}/>')
        return self

    def curve(self, fn, x0, x1, X, Y, c='blue', w=2.6, n=120, dash=None):
        """Plot y = fn(x) for x in [x0, x1]; X, Y map data -> pixels."""
        pts = [(X(x0 + (x1 - x0) * i / n), Y(fn(x0 + (x1 - x0) * i / n))) for i in range(n + 1)]
        return self.poly(pts, c, w, dash=dash)

    def rect(self, x, y, w, h, c='ink', fill='none', sw=2, rx=0):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{COL.get(fill, fill)}" stroke="{COL.get(c, c)}" stroke-width="{sw}"/>')
        return self

    def circle(self, cx, cy, r, c='ink', fill='none', sw=2):
        self.parts.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{COL.get(fill, fill)}" stroke="{COL.get(c, c)}" stroke-width="{sw}"/>')
        return self

    def arc(self, cx, cy, r, a0, a1, c='ink', w=1.6):
        """Arc from angle a0 to a1 (degrees, anticlockwise from +x, y up)."""
        p = lambda a: (cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a)))
        (x0, y0), (x1, y1) = p(a0), p(a1)
        large = 1 if abs(a1 - a0) > 180 else 0
        sweep = 0 if a1 > a0 else 1
        self.parts.append(f'<path d="M{x0:.1f} {y0:.1f} A{r} {r} 0 {large} {sweep} {x1:.1f} {y1:.1f}" fill="none" stroke="{COL.get(c, c)}" stroke-width="{w}"/>')
        return self

    def text(self, x, y, s, c='ink', size=17, anchor='start', italic=False, bold=False, sub=None, sup=None):
        st = (' font-style="italic"' if italic else '') + (' font-weight="bold"' if bold else '')
        body = _esc(s)
        if sub:
            body += f'<tspan dy="5" font-size="{size * 0.68:.0f}">{_esc(sub)}</tspan>'
        if sup:
            body += f'<tspan dy="{-7 if not sub else -12}" font-size="{size * 0.68:.0f}">{_esc(sup)}</tspan>'
        self.parts.append(f'<text x="{x:.1f}" y="{y:.1f}" {FONT} font-size="{size}" fill="{COL.get(c, c)}" text-anchor="{anchor}"{st}>{body}</text>')
        return self

    def label(self, x, y, s, c='ink', size=18, sub=None, anchor='middle'):
        """Italic symbol label, e.g. label(x, y, 'v', sub='0')."""
        return self.text(x, y, s, c, size, anchor, italic=True, sub=sub)

    def axes(self, ox, oy, xlen, ylen, xl='x', yl='y', c='ink', neg_y=0, neg_x=0, size=20):
        self.arrow(ox - neg_x, oy, ox + xlen, oy, c, 1.8, 10)
        self.arrow(ox, oy + neg_y, ox, oy - ylen, c, 1.8, 10)
        self.text(ox + xlen - 2, oy + size + 6, xl, c, size, 'end', italic=True)
        self.text(ox - 8, oy - ylen + 8, yl, c, size, 'end', italic=True)
        return self

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}">'
                + ''.join(self.parts) + '</svg>')

    def save(self, media, name, long_side=1000):
        doc = pymupdf.open(stream=self.svg().encode('utf8'), filetype='svg')
        z = long_side / max(self.w, self.h)
        pix = doc[0].get_pixmap(matrix=pymupdf.Matrix(z, z), alpha=False)
        im = Image.open(io.BytesIO(pix.tobytes('png'))).convert('RGB')
        os.makedirs(media, exist_ok=True)
        p = os.path.join(media, name + '.webp')
        im.save(p, quality=86)
        print(name, im.size, os.path.getsize(p) // 1024, 'KB')
        return im.size
