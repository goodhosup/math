"""docs/images 의 그래프 SVG를 다시 만드는 스크립트.  python3 tools/figures.py"""
import math, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from plot import plot

D = os.path.join(os.path.dirname(__file__), "..", "docs", "images")
B, R, G = "#4f46e5", "#dc2626", "#059669"

def figs():
    # 공통수학1 7. 이차함수
    plot(f"{D}/quad-basic.svg", [(lambda x: x**2, B), (lambda x: 2*x**2, R), (lambda x: -x**2, G)],
         xr=(-4, 4), yr=(-5, 6), labels=[(2.5, 4.5, "y = x²", B), (-3.8, 4.5, "y = 2x²", R), (1.8, -4.2, "y = −x²", G)])
    plot(f"{D}/quad-vertex.svg", [(lambda x: x**2 - 2*x - 3, B)], xr=(-3, 5), yr=(-5, 6),
         points=[(1, -4, "꼭짓점 (1, −4)", 8, 16), (-1, 0, "−1", -16, -8), (3, 0, "3", 6, -8), (0, -3, "(0, −3)", 6, 0)],
         vlines=[1], labels=[(2.2, 5.3, "y = x² − 2x − 3", B)])
    plot(f"{D}/quad-discriminant.svg", [(lambda x: x**2 - 2, B), (lambda x: x**2, R), (lambda x: x**2 + 2, G)],
         xr=(-3, 3), yr=(-3, 6), labels=[(1.5, -1.6, "D > 0", B), (1.9, 2.6, "D = 0", R), (1.0, 5.5, "D < 0", G)])
    # 공통수학2
    plot(f"{D}/c2-distance.svg", [], xr=(-1, 6), yr=(-1, 5),
         points=[(1, 1, "A(1, 1)", -10, 18), (4, 4, "B(4, 4)", 8, -6), (4, 1, "", 0, 0)],
         labels=[(2.1, 0.55, "가로 3", R), (4.2, 2.6, "세로 3", R), (1.4, 3.0, "AB = ?", B)],
         segments=[(1, 1, 4, 4, B, False), (1, 1, 4, 1, R, True), (4, 1, 4, 4, R, True)])
    plot(f"{D}/c2-line.svg", [(lambda x: 2*x - 1, B), (lambda x: -0.5*x + 2, R)], xr=(-3, 4), yr=(-3, 5),
         labels=[(2.0, 4.6, "y = 2x − 1", B), (-2.9, 3.6, "y = −½x + 2", R)], points=[(1.2, 1.4, "교점 (6/5, 7/5)", 8, 18)])
    plot(f"{D}/c2-circle.svg", [(lambda x: 1 + math.sqrt(max(0, 4 - (x - 2)**2)) if abs(x-2) <= 2 else None, B, (0, 4)),
                                (lambda x: 1 - math.sqrt(max(0, 4 - (x - 2)**2)) if abs(x-2) <= 2 else None, B, (0, 4))],
         xr=(-1, 5), yr=(-2, 4), points=[(2, 1, "중심 (2, 1)", -40, 20), (4, 1, "", 0, 0)],
         labels=[(2.6, 1.2, "r = 2", R), (2.6, 3.6, "(x−2)² + (y−1)² = 4", B)], segments=[(2, 1, 4, 1, R, False)])
    plot(f"{D}/c2-reflect.svg", [(lambda x: x, "#9ca3af")], xr=(-7, 5), yr=(-4, 4),
         points=[(2, 3, "P(2, 3)", 8, -6), (2, -3, "x축 대칭 (2, −3)", 8, 16), (-2, 3, "y축 대칭 (−2, 3)", -112, -6),
                 (-2, -3, "원점 대칭 (−2, −3)", -128, 16), (3, 2, "y = x 대칭 (3, 2)", 8, 16)])
    plot(f"{D}/c2-rational.svg", [(lambda x: 1/x, B), (lambda x: 1/(x - 1) + 2, R)], xr=(-4, 5), yr=(-3, 5),
         hlines=[2], vlines=[1], labels=[(2.6, 0.9, "y = 1/x", B), (2.0, 3.8, "y = 1/(x−1) + 2", R)])
    plot(f"{D}/c2-irrational.svg", [(lambda x: math.sqrt(x), B, (0, 6)), (lambda x: -math.sqrt(x), R, (0, 6)),
                                    (lambda x: math.sqrt(-x), G, (-6, 0))], xr=(-5, 6), yr=(-3, 3),
         labels=[(3.0, 2.3, "y = √x", B), (3.0, -2.4, "y = −√x", R), (-4.6, 2.2, "y = √(−x)", G)])

if __name__ == "__main__":
    figs()
