# -*- coding: utf-8 -*-
"""
SymPyライブラリの使用例サンプル。

SymPyライブラリとは?
  * Python上で数式処理を可能にするライブラリ。
  * ex) (x^2 -2x + 1) = 0を解く
"""

# 変数を表すオブジェクト
from sympy import Symbol

# 因数に分解
from sympy import factor

# 式を展開する
from sympy import expand

# 可読性の高い形で表示する
from sympy import pprint

# 数式を単純化する
from sympy import simplify

# 文字列を数式に変換する
from sympy import sympify

# 方程式を解く
from sympy import solve


# 変数の代入と表示。
# (pprintを使うと、可読性の高い形式で出力できる。)
x = Symbol('x')
y = Symbol('y')
expr = x*x - y*y
pprint(expr)


# 因数分解
factors = factor(expr)
pprint(factors)


# 式の展開
pprint(expand(factors))


# 変数に値を代入する。
x = Symbol('x')
y = Symbol('y')
expr = x*x + 2*x*y + y*y

# 数値を代入してみる。
pprint(expr.subs({x:1, y:2}))

# 変数を代入することも可能
res = expr.subs({x:1-y})

# 変数を代入した場合、そのままでは代入直後の状態になる。
pprint(res)

# インタプリタに数式を解かせるためには、symplifyメソッドを呼ぶ必要がある。
pprint(simplify(res))


# 文字列からオブジェクトを生成する。
# sympify関数をコールすることで、文字列から数式オブジェクトを生成できる。
# (以下例のように、空白を含んでいても大丈夫。)
pprint(sympify(' x**2 + 2*x + 1 '))

# 方程式を解く
x = Symbol('x')

# 一次方程式を解く
# (方程式を解く場合、expr=0の形式で解いてくれる)
expr = x - 5 -7
pprint(solve(expr))

# 二次方程式を解く
expr = x**2 +5 * x + 4
pprint(solve(expr))

# 以下は、結果が虚数解となる例
expr = x**2 + x + 1
pprint(solve(expr))

# 変数が複数ある場合の解き方
# (以下では、x以外を定数とし、xについて解いてみる)
x = Symbol('x')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
expr = a*x*x + b*x + c
pprint(solve(expr, x))

# 連立方程式を解いてみる
x = Symbol('x')
y = Symbol('y')
expr1 = 2*x + 3*y -6
expr2 = 3*x + 2*y -12

# 連立方程式を解きたい場合、２つの方程式をタプルで渡せばOK
pprint(solve((expr1, expr2)))
