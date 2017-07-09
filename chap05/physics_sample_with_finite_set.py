# -*- coding: utf-8 -*-
"""
集合オブジェクトFiniteSetを使う例。

単振り子に対する周期を求める例で、
通常のリストやタプルの代わりに、FiniteSetを使ってみる。
"""

from sympy import FiniteSet

from sympy import pi


def time_period(length, g=9.8):
    """
    単振り子の周期を求める。

    公式は以下。
    T = 2 * \pi * \sqrt{L / g}
    T :振り子の周期(一往復するまでにかかる時間)。
    L :振り子の長さ(cm)。
    g :重力加速度。地球上での平均は、9.8m/s^2
    """
    return 2*pi * ((length/g)**0.5)

l_list = FiniteSet(15, 18, 21, 22.5, 25)
g_list = FiniteSet(9.8, 9.78, 9.83)

# ヘッダを出力。
print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)', 'Gravity(m/^2)', 'Time Periods(s)'))

# 直積を求める。
# (この例で一番重要なのはここ。長さの異なる集合があって、
# 一つ一つの組み合わせに対し何かを適用したい時、FiniteSetが便利。)
product = l_list * g_list

for elem in product:
    l = elem[0]
    g = elem[1]

    # 振り子の周期を求める。
    t = time_period(l/100, g)

    print('{0:^15}{1:^15}{2:^15.3f}'.format(float(l), float(g), float(t)))
