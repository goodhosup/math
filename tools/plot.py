"""Simple SVG function plotter for the math site. Usage: import and call plot()."""
import math
from xml.sax.saxutils import escape
COLORS = ["#4f46e5", "#dc2626", "#059669", "#d97706"]

def plot(path, funcs, xr=(-4, 4), yr=(-4, 4), points=(), unit=36, labels=(), xticks=None, yticks=None, hlines=(), vlines=(), shade=None, segments=()):
    x0, x1 = xr; y0, y1 = yr
    pad = 24; padr = 70
    W = (x1 - x0) * unit + pad + padr; H = (y1 - y0) * unit + 2 * pad
    px = lambda x: pad + (x - x0) * unit
    py = lambda y: pad + (y1 - y) * unit
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" viewBox="0 0 {W:.0f} {H:.0f}" font-family="sans-serif" font-size="13">',
         f'<rect width="{W:.0f}" height="{H:.0f}" fill="#fff"/>']
    for i in range(math.ceil(x0), math.floor(x1) + 1):
        o.append(f'<line x1="{px(i):.1f}" y1="{py(y0):.1f}" x2="{px(i):.1f}" y2="{py(y1):.1f}" stroke="#eef0f3"/>')
    for j in range(math.ceil(y0), math.floor(y1) + 1):
        o.append(f'<line x1="{px(x0):.1f}" y1="{py(j):.1f}" x2="{px(x1):.1f}" y2="{py(j):.1f}" stroke="#eef0f3"/>')
    if shade:
        f, a, b, color = shade
        n = 200; pts = [(px(a), py(0))]
        for k in range(n + 1):
            x = a + (b - a) * k / n; pts.append((px(x), py(f(x))))
        pts.append((px(b), py(0)))
        o.append('<polygon points="' + " ".join(f"{u:.1f},{v:.1f}" for u, v in pts) + f'" fill="{color}" fill-opacity="0.25"/>')
    if y0 <= 0 <= y1:
        o.append(f'<line x1="{px(x0):.1f}" y1="{py(0):.1f}" x2="{px(x1):.1f}" y2="{py(0):.1f}" stroke="#111" stroke-width="1.4"/>')
        o.append(f'<text x="{px(x1) + 4:.1f}" y="{py(0) + 4:.1f}">x</text>')
    if x0 <= 0 <= x1:
        o.append(f'<line x1="{px(0):.1f}" y1="{py(y0):.1f}" x2="{px(0):.1f}" y2="{py(y1):.1f}" stroke="#111" stroke-width="1.4"/>')
        o.append(f'<text x="{px(0) - 4:.1f}" y="{py(y1) - 8:.1f}">y</text>')
        o.append(f'<text x="{px(0) - 14:.1f}" y="{py(0) + 15:.1f}">O</text>')
    for (xt, lab) in (xticks or []):
        o.append(f'<line x1="{px(xt):.1f}" y1="{py(0) - 3:.1f}" x2="{px(xt):.1f}" y2="{py(0) + 3:.1f}" stroke="#111"/><text x="{px(xt) - 6:.1f}" y="{py(0) + 16:.1f}">{escape(str(lab))}</text>')
    for (yt, lab) in (yticks or []):
        o.append(f'<line x1="{px(0) - 3:.1f}" y1="{py(yt):.1f}" x2="{px(0) + 3:.1f}" y2="{py(yt):.1f}" stroke="#111"/><text x="{px(0) + 6:.1f}" y="{py(yt) + 4:.1f}">{escape(str(lab))}</text>')
    for y in hlines:
        o.append(f'<line x1="{px(x0):.1f}" y1="{py(y):.1f}" x2="{px(x1):.1f}" y2="{py(y):.1f}" stroke="#9ca3af" stroke-dasharray="5 4"/>')
    for x in vlines:
        o.append(f'<line x1="{px(x):.1f}" y1="{py(y0):.1f}" x2="{px(x):.1f}" y2="{py(y1):.1f}" stroke="#9ca3af" stroke-dasharray="5 4"/>')
    o.append(f'<clipPath id="c"><rect x="{px(x0)}" y="{py(y1)}" width="{(x1-x0)*unit}" height="{(y1-y0)*unit}"/></clipPath>')
    for idx, fn in enumerate(funcs):
        f = fn[0]; color = fn[1] if len(fn) > 1 else COLORS[idx]
        dom = fn[2] if len(fn) > 2 else (x0, x1)
        n = 600; segs = []; cur = []
        for k in range(n + 1):
            x = dom[0] + (dom[1] - dom[0]) * k / n
            try:
                y = f(x)
            except (ValueError, ZeroDivisionError):
                y = None
            if y is None or isinstance(y, complex) or abs(y) > 1e3 or (y < y0 - 3 or y > y1 + 3):
                if len(cur) > 1: segs.append(cur)
                cur = []; continue
            cur.append((px(x), py(y)))
        if len(cur) > 1: segs.append(cur)
        for s in segs:
            o.append(f'<polyline clip-path="url(#c)" fill="none" stroke="{color}" stroke-width="2.5" points="' + " ".join(f"{u:.1f},{v:.1f}" for u, v in s) + '"/>')
    for (xa, ya, xb, yb, color, dash) in segments:
        d = ' stroke-dasharray="5 4"' if dash else ''
        o.append(f'<line x1="{px(xa):.1f}" y1="{py(ya):.1f}" x2="{px(xb):.1f}" y2="{py(yb):.1f}" stroke="{color}" stroke-width="2"{d}/>')
    for p in points:
        x, y = p[0], p[1]; lab = p[2] if len(p) > 2 else f"({x}, {y})"
        dx = p[3] if len(p) > 3 else 8; dy = p[4] if len(p) > 4 else -8
        o.append(f'<circle cx="{px(x):.1f}" cy="{py(y):.1f}" r="4.5" fill="#f59e0b"/>')
        if lab: o.append(f'<text x="{px(x) + dx:.1f}" y="{py(y) + dy:.1f}" paint-order="stroke" stroke="#fff" stroke-width="4">{escape(str(lab))}</text>')
    for (x, y, text, color) in labels:
        o.append(f'<text x="{px(x):.1f}" y="{py(y):.1f}" fill="{color}" font-size="14" font-weight="600" paint-order="stroke" stroke="#fff" stroke-width="4">{escape(text)}</text>')
    o.append('</svg>')
    open(path, 'w').write("\n".join(o))
