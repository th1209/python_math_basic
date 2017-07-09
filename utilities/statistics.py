# -*- coding: utf-8 -*-
"""統計に関するユーティリティ関数を提供するモジュール。"""

from collections import Counter


def calc_mean(numbers):
    """平均を求める。"""
    s = sum(numbers)
    n = len(numbers)
    return s / n


def calc_median(numbers):
    """中央値を求める。"""
    l = len(numbers)
    if l == 0:
        # 要素0の境界ケース
        return 0
    elif l % 2 == 0:
        # 要素が偶数個の場合(真ん中２つの要素の平均)
        m1 = numbers[int(l / 2) - 1]
        m2 = numbers[int(l / 2)]
        return (m1 + m2) / 2
    else:
        # 要素が奇数個の場合
        return numbers[l // 2]


def calc_mode(numbers):
    """最頻値を求める。

    以下2角要素を持つタプルのリストを返す。
    第一要素:値。 第二要素:データの個数。
    """
    counter = Counter(numbers)
    modes = counter.most_common()
    max_num = modes[0][1]

    ret = []
    for mode in modes:
        if mode[1] >= max_num:
            ret.append(mode)
        else:
            break
    return ret


def calc_variance(numbers):
    """分散を求める。"""
    if len(numbers) == 0:
        # 要素0の境界ケース
        return 0

    mean = calc_mean(numbers)
    numerator = 0
    for number in numbers:
        numerator += (number - mean) ** 2
    return numerator / len(numbers)


def calc_standard_deviation(numbers):
    """標準偏差を求める。"""
    return calc_variance(numbers) ** 0.5


def calc_covariance(x_list, y_list):
    """2つのリストの共分散を求める。"""
    # 最低限のエラーチェック
    if len(x_list) != len(y_list):
        raise ValueError()
    if (len(x_list) == 0) or (len(y_list) == 0):
        raise ValueError()

    # 平均を先に出しておく
    x_avg = calc_mean(x_list)
    y_avg = calc_mean(y_list)

    numerator = 0
    for xi, yi in zip(x_list, y_list):
        numerator += (xi - x_avg) * (yi - y_avg)

    return numerator / len(x_list)


def calc_correlation(x_list, y_list):
    """2つのリストの相関係数を求める。"""
    # 相関係数は、(共分散) / ((xの標準偏差) * (yの標準偏差))で求まる。
    numerator = calc_covariance(x_list, y_list)
    denominator = (calc_standard_deviation(x_list) *
                   calc_standard_deviation(y_list))
    return numerator / denominator
