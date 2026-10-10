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

if __name__ == "__main__":
    figs()
