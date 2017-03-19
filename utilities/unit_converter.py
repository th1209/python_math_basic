# -*- coding: utf-8 -*-
"""単位変換に関する関数をまとめたモジュール。"""


def km_miles(km):
    """Convert kilometers to miles."""
    return km / 1.609


def miles_km(miles):
    """Convert miles to kilometers."""
    return miles * 1.609


def pounds_kilograms(pounds):
    """Convert pounds to kilograms."""
    return pounds / 2.20462


def kilograms_pounds(kilograms):
    """Convert kilograms to pounds."""
    return kilograms * 2.20462


def celsius_fahrenheit(c):
    """Convert celsius temperature to fahrenheit one."""
    return ((c * 9) / 5) + 32


def fahrenheit_celsius(f):
    """Convert fahrenheit temperature to celsius one."""
    return (f - 32) * (5 / 9)
