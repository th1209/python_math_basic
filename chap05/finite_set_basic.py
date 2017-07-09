# -*- coding: utf-8 -*-
"""
Pythonの集合ライブラリFiniteSetのサンプル。

※finite: 有限の
"""

from fractions import Fraction

from sympy import FiniteSet


# 集合オブジェクトの基本。
s = FiniteSet(2, 4, 6)
print(s)
# 要素の長さ。
print(len(s))
# 要素が含まれるか。
print(4 in s)

# 集合オブジェクトには、型の異なる要素を代入することが可能。
s = FiniteSet(1, 1.5, Fraction(1, 5))

# 空集合。
e = FiniteSet()
print(e)

# 既存のリストなどから集合オブジェクトを作る例。
# (実引数にアスタリスクを付けた場合、リストやタプルを展開して引数に渡せる。)
l = [1, 2, 3]
print(FiniteSet(*l))

# 集合オブジェクトの特徴
# 集合オブジェクトは重複を許さない
s1 = FiniteSet(1, 3, 3, 5)
print(s1)

# 集合オブジェクトの順序は不定で、全ての要素が等しければ等価なオブジェクトである。
s2 = FiniteSet(5, 1, 3)
print(s1 == s2)


# 以下、集合に対する概念(若干マイナーな概念も含むかも...)。
sub = FiniteSet(1, 2)
super = FiniteSet(1, 2, 3)

# AはBの部分集合か?
print(sub.is_subset(super))

# AはBの上位集合か?
print(super.is_superset(sub))

# AはBの真部分集合か?
# ※真部分集合:Bが、Aにない要素を一つ以上含んでいる場合、BをAの真部分集合と呼ぶ。
print(sub.is_proper_subset(super))

# AはBの真上位集合か?
print(super.is_proper_superset(sub))

# 通常の上位集合と、真上位集合の違い。
print(FiniteSet(3, 1, 2).is_superset(super))
print(FiniteSet(3, 1, 2).is_proper_superset(super))

# 冪集合を求める例。
# ※冪集合:ある集合の、全ての部分集合を列挙した集合。
#        ある集合の濃度をsとすれば、部分集合の個数は、2^sとなることが知られている。
print(FiniteSet(3, 1, 2).powerset())


# 集合の和集合や積集合を求める。
s = FiniteSet(1, 2, 3)
t = FiniteSet(3, 4, 5)
u = FiniteSet(3, 6)

# 和集合を求める。
print(s.union(t))

# unionはメソッドチェーンして使用可能。
# 後述するintersectについても同様。
print(s.union(t).union(u))

# 積集合を求める。
print(s.intersect(t).intersect(u))

# 直積を求める。
# ※直積:それぞれの集合から要素を一つづつ選んでできる、全ての集合。
p = s * t * u

# そのままの状態では、各集合を表示できない(ProductSetオブジェクトが返る)。
print(p)
print(type(p))

# forで列挙すると、各集合を表示できる。
for elem in p:
    print(elem)
print(len(p))










